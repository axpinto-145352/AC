# SOFTWARE DEVELOPMENT ACTION PLAN

**Version:** 1.1 (Revised) | **Classification:** CUI | **Distribution:** Internal Consortium Only

## DIU AI-Assisted Triage & Treatment (PROJ00628)
### Veteran Vectors (Prime) | Authentic Consortium
### Date: February 24, 2026

All software components developed by Veteran Vectors as consortium prime; hardware firmware developed by hardware consortium partner.

---

## 1. EXECUTIVE SUMMARY

This action plan defines the software architecture, development roadmap, toolchain, cost estimates, and data flows for the AI-Assisted Triage & Treatment system. The software platform is the **primary differentiator** for the Authentic Consortium -- layering advanced AI/ML analytics on COTS hemodynamic monitoring hardware to deliver battlefield-ready decision support.

---

## 2. SYSTEM ARCHITECTURE

### 2.1 High-Level Architecture

```
+------------------------------------------------------------------+
|                    CLOUD TIER (IL-5 / FedRAMP)                   |
|  +--------------------+  +------------------+  +---------------+ |
|  | Analytics Dashboard|  | Model Training   |  | EHR Sync      | |
|  | (Provider Portal)  |  | Pipeline (MLOps) |  | (HL7/FHIR)   | |
|  +--------------------+  +------------------+  +---------------+ |
+------------------------------|-----------------------------------+
                               | (when connected)
                    TLS 1.3 / MQTT / REST
                               |
+------------------------------|-----------------------------------+
|                    EDGE TIER (DDIL-Capable)                      |
|  +--------------------+  +------------------+  +---------------+ |
|  | Edge AI Engine     |  | BATDOK Gateway   |  | ATAK Plugin   | |
|  | (Inference, Triage |  | (Data Translator)|  | (Blue Force   | |
|  |  Scoring, Alerts)  |  |                  |  |  Tracker Intg)| |
|  +--------------------+  +------------------+  +---------------+ |
|  +--------------------+  +------------------+                    |
|  | Local Data Store   |  | Mesh Network Mgr |                    |
|  | (SQLite)           |  | (Sync & Queue)   |                    |
|  +--------------------+  +------------------+                    |
+------------------------------|-----------------------------------+
                               | BLE / Wi-Fi / USB
+------------------------------|-----------------------------------+
|                    DEVICE TIER (Sensor Hardware)                  |
|  +--------------------+  +------------------+  +---------------+ |
|  | Hemodynamic Sensors|  | Onboard MCU      |  | Battery Mgmt  | |
|  | (SpO2, BP, HR,     |  | (Signal Process, |  | (72hr runtime)| |
|  |  Temp, EtCO2)      |  |  BLE Broadcast)  |  |               | |
|  +--------------------+  +------------------+  +---------------+ |
+------------------------------------------------------------------+
```

### 2.2 Component Breakdown

| Component | Function | Technology | Owner |
|---|---|---|---|
| **Edge AI Engine** | Real-time inference, triage scoring (MARCH/TCCC), trend detection, deterioration alerts | C++ inference via ONNX Runtime C API; Python for development and testing only | Veteran Vectors |
| **BATDOK Gateway** | Translate sensor data into BATDOK-compatible format for medic tablet | HL7 FHIR adapter, custom serial protocol | Veteran Vectors |
| **ATAK Plugin** | Overlay patient status on Blue Force Tracker; CASEVAC request automation | Java/Kotlin (Android ATAK SDK) | Veteran Vectors |
| **EHR Sync Module** | Bidirectional sync with Theater Medical Information Program (TMIP) / MHS GENESIS | HL7 FHIR R4, REST APIs | Veteran Vectors |
| **Cloud Analytics** | Aggregate data, model retraining, provider dashboards, population health | AWS GovCloud (IL-5) / Azure Gov, React dashboard | Veteran Vectors |
| **Mesh Network Manager** | Store-and-forward queue for DDIL; sync when connectivity resumes | MQTT broker (Mosquitto), conflict-free replicated data types (CRDTs) | Veteran Vectors |
| **Device Firmware** | Sensor signal processing, BLE broadcast, power management | C/Embedded (Zephyr RTOS or FreeRTOS) | Hardware Partner |
| **MLOps Pipeline** | Model versioning, training data management, A/B deployment | MLflow, DVC, containerized training (Docker) | Veteran Vectors |

---

## 3. AI/ML MODEL STRATEGY

### 3.1 Triage Classification Model
- **Purpose:** Classify casualty status per TCCC MARCH protocol (Massive hemorrhage, Airway, Respiration, Circulation, Hypothermia)
- **Inputs:** Heart rate, SpO2, blood pressure (continuous/non-invasive), respiratory rate, skin temperature, trend deltas
- **Output:** Triage category (Immediate/Delayed/Minimal/Expectant) + confidence score + recommended interventions
- **Architecture:** Gradient-boosted ensemble (XGBoost) for initial deployment; LSTM-based temporal model for v2
- **Training Data:** MIMIC-III/IV, DoD Trauma Registry (JTTR), PhysioNet datasets, consortium clinical partner data
- **Edge Deployment:** PyTorch -> ONNX export -> ONNX Runtime Mobile (C++ API); quantized INT8 for low-power inference (<50ms latency design target, to be validated on candidate hardware in Week 2)

### 3.2 Deterioration Early Warning
- **Purpose:** Predict hemodynamic deterioration 15--30 minutes before clinical onset
- **Architecture:** Temporal convolutional network (TCN) on sliding window of vitals
- **Alert Mechanism:** Audible/visual alert on medic device + push to ATAK overlay

### 3.3 Model Governance
- All models versioned and traceable per FDA Software as a Medical Device (SaMD) guidelines
- Pre-defined performance thresholds (sensitivity >95%, specificity >85% for critical triage categories)
- Human-in-the-loop: AI recommends, medic decides -- no autonomous treatment actions

---

## 4. DEVELOPMENT ROADMAP

### Phase 1: Prototype (Weeks 1-8 | Mar-Apr 2026)
| Week | Milestone | Deliverables |
|---|---|---|
| 1-2 | Architecture finalization & local environment setup | Design docs, CI/CD pipeline, Docker Compose local dev environments (GovCloud provisioning in parallel, available ~Week 5) |
| 3-4 | Edge AI engine v0.1 + sensor integration | Working inference on dev hardware, BLE data ingestion |
| 5-6 | BATDOK gateway + ATAK plugin alpha | Data flowing from sensor -> edge -> BATDOK/ATAK |
| 7-8 | Integration testing + Pitch Day prep | 30-unit deployment packages (contingent on hardware availability by Week 6), demo environment, pitch materials |

### Phase 2: Demonstration (Weeks 9-12 | May 2026 -- Sword Exercise)
| Week | Milestone | Deliverables |
|---|---|---|
| 9 | Field-ready software load on 30 units | Validated firmware + software images |
| 10-11 | Sword 2026 live demo | Operational demo with live medics, real-time triage display |
| 12 | After-action report + data collection | Performance metrics, user feedback, model accuracy report |

### Phase 3: Scale (Months 4-14 | Jun 2026 - May 2027)
| Month | Milestone | Deliverables |
|---|---|---|
| 4-8 | FDA 510(k) submission support (led by medical device partner; Veteran Vectors provides SaMD documentation) | Clinical validation data, SaMD documentation per IEC 62304, risk file per ISO 14971 |
| 6-10 | Cloud tier deployment / IL-5 ATO (led by cloud/cyber partner) | GovCloud infrastructure, SSP, ATO package, 3PAO assessment |
| 8-10 | Manufacturing software integration | Factory provisioning tools, OTA update system |
| 10-14 | Scale to 15,000 units/yr | Automated provisioning, fleet management dashboard |

---

## 5. TECHNOLOGY STACK & TOOLS

### 5.1 Development Tools
| Category | Tool | Purpose |
|---|---|---|
| **Language (Edge)** | Python 3.11+ / C++17 | AI inference / performance-critical paths |
| **Language (Mobile)** | Kotlin / Java | ATAK plugin development |
| **Language (Cloud)** | Python / TypeScript | Backend services / frontend dashboard |
| **ML Framework** | PyTorch -> ONNX export | Model training -> edge deployment |
| **Edge Runtime** | ONNX Runtime Mobile (C++ API) | Optimized inference on ARM/embedded |
| **Database (Edge)** | SQLite | Local time-series storage (lightweight, edge-optimized) |
| **Database (Cloud)** | PostgreSQL + TimescaleDB | Aggregate analytics |
| **Message Broker** | Eclipse Mosquitto (MQTT) | DDIL-resilient pub/sub |
| **Containerization** | Docker / Podman | Consistent build & deploy |
| **Orchestration** | Direct container deployment (prototype); K3s (Phase 3 fleet); EKS (cloud) | Streamlined prototype deployment; K3s for fleet-scale management in Phase 3 |
| **CI/CD** | GitHub Actions + ArgoCD | Build, test, deploy automation |
| **MLOps** | MLflow + DVC | Model versioning, experiment tracking |
| **Monitoring** | Prometheus + Grafana | System health, model performance |
| **Security** | HashiCorp Vault, STIG compliance tools | Secrets management, hardening |
| **Documentation** | MkDocs + Confluence | Technical docs, compliance artifacts |

### 5.2 Development Environments
- **Local Dev:** Docker Compose stack simulating full 3-tier architecture
- **Integration/Test:** AWS GovCloud staging environment
- **Production (Prototype):** Hardened edge compute units + IL-5 cloud instance

---

## 6. COST ESTIMATES

### 6.1 Software Development Costs (Phase 1-2: Prototype through Sword Demo)

| Role | FTEs | Duration | Rate/Hr | Cost |
|---|---|---|---|---|
| Technical Lead / Architect | 1 | 12 weeks | $225 | $108,000 |
| ML Engineer (Triage Models) | 1 | 12 weeks | $200 | $96,000 |
| Edge Software Engineer | 1 | 12 weeks | $190 | $91,200 |
| ATAK/Mobile Developer | 0.5 | 8 weeks | $185 | $29,600 |
| BATDOK Integration Engineer | 0.5 | 8 weeks | $185 | $29,600 |
| DevOps / Cloud Engineer | 0.5 | 12 weeks | $195 | $46,800 |
| QA / Test Engineer | 0.5 | 8 weeks | $170 | $27,200 |
| **Subtotal Labor** | | | | **$428,400** |

*Note: Labor rates are fully-burdened rates inclusive of fringe, overhead, G&A, and fee for Veteran Vectors employees.*

| Non-Labor Item | Cost |
|---|---|
| Cloud infrastructure (GovCloud dev/staging) | $22,000 |
| Development hardware / sensor dev kits (5 units) | $25,000 |
| ATAK developer licenses & SDK access | $5,000 |
| ML training compute (GPU instances, commercial cloud for non-sensitive training) | $10,000 |
| Security scanning tools (STIG, DISA) | $5,000 |
| Travel (Pitch Day + Sword 2026) | $20,000 |
| Management reserve (8%) | $41,000 |
| **Subtotal Non-Labor** | **$128,000** |

| **TOTAL PHASE 1-2** | **$556,400** |

### 6.2 Software Development Costs (Phase 3: Scale to 15K/yr)

| Item | Annual Cost |
|---|---|
| Engineering team (sustained development) | $850,000 |
| Cloud infrastructure (IL-5 production) | $120,000 |
| FDA SaMD compliance / regulatory (Veteran Vectors SW documentation; medical device partner owns 510(k) submission costs separately) | $200,000 |
| ATO / cybersecurity compliance (cloud/cyber partner leads; Veteran Vectors provides system documentation) | $150,000 |
| MLOps / model maintenance | $60,000 |
| Management reserve (8%) | $110,000 |
| **Total Phase 3 (Annual, Veteran Vectors scope only)** | **$1,490,000** |

*Note: FDA regulatory consulting ($300K--$500K) and 3PAO assessment ($200K--$400K) costs borne by respective consortium partners are not included in this Veteran Vectors software development budget.*

### 6.3 Per-Unit Software Cost at Scale
| Volume | Software License / Unit | Notes |
|---|---|---|
| 30 units (prototype) | $0 (included in dev) | Prototype phase |
| 1,000 units | $350/unit | Amortized dev cost + cloud |
| 15,000 units/yr | $85/unit | Full production scale |

---

## 7. DATA FLOW DIAGRAMS

### 7.1 Real-Time Triage Flow
```
Sensor (BLE) --> Edge Gateway --> Signal Processing --> AI Inference Engine
                                                            |
                                    +-----------------------+-----------------------+
                                    |                       |                       |
                              Triage Score            Trend Alert              Raw Vitals
                                    |                       |                       |
                              BATDOK Display          ATAK Overlay          Local Time-Series DB
                              (Medic Tablet)          (Commander View)      (Store & Forward)
                                                                                    |
                                                                            (When Connected)
                                                                                    |
                                                                            Cloud Analytics
                                                                            + EHR Sync
```

### 7.2 DDIL Sync Flow
```
[CONNECTED MODE]
  Sensor -> Edge -> Cloud (real-time sync via MQTT/TLS)

[DISCONNECTED MODE]
  Sensor -> Edge -> Local Store (SQLite queue)
                    |
                    +-> CRDT-based merge log

[RECONNECTION]
  Local Store -> Sync Manager -> Cloud
                    |
                    +-> Conflict resolution (last-write-wins + clinical priority override)
                    +-> Backfill analytics dashboard
```

### 7.3 Model Update Flow
```
Cloud: New Training Data -> MLflow Pipeline -> Validated Model -> ONNX Export
                                                                      |
                                                              Model Registry
                                                                      |
                                                          OTA Update Package
                                                          (signed, encrypted)
                                                                      |
                                                          Edge Device
                                                                      |
                                                          Canary Deploy -> Validate
                                                                      |
                                                          IF PASS: Promote to active
                                                          IF FAIL: Rollback to previous validated model
                                                                   + alert MLOps team
                                                                   + log event for FDA audit trail
                                                                   (rollback within 30s, zero monitoring interruption)
```

### 7.4 Multi-Casualty Data Flow
```
Sensor A (BLE) --+
Sensor B (BLE) --+--> Edge Device (BLE multiplexing, max 7-10 simultaneous)
Sensor C (BLE) --+          |
  ...            |          +--> Parallel AI Inference (per-patient)
                 |          |         |
                 |          |    Prioritized Triage Dashboard
                 |          |    (sorted by severity: Immediate > Delayed > Minimal > Expectant)
                 |          |         |
                 |          |    BATDOK Multi-Patient View
                 |          |    ATAK Multi-Casualty Overlay
                 |          |
                 |     If >10 casualties (BLE limit):
                 |          +--> Mesh Network to additional edge devices
                 |               (MQTT mesh handles overflow; each edge device manages 7-10 patients)
```

---

## 8. VERIFICATION & VALIDATION STRATEGY

### 8.1 Test Levels (per IEC 62304)
| Test Level | Approach | Coverage Target |
|---|---|---|
| **Unit Testing** | Automated (pytest / Google Test); safety-critical modules | >90% code coverage for triage classification and alerting modules |
| **Integration Testing** | Edge-to-cloud, sensor-to-BATDOK, sensor-to-ATAK end-to-end | All data paths validated with simulated sensor inputs |
| **System Testing** | Full 3-tier stack with representative hardware | Acceptance criteria: <50ms inference, correct triage output, DDIL sync/reconnect |
| **Clinical Validation** | Sensitivity/specificity against labeled MIMIC-IV trauma data + controlled simulation | Target: >95% sensitivity, >85% specificity for critical triage categories |
| **Regression Testing** | Automated suite run on every model update and code change | Full regression before any deployment; model rollback if performance degrades |
| **Interoperability Testing** | BATDOK conformance, TAK Product Center plugin certification, HL7 FHIR validation | Tested against government reference implementations where available |

### 8.2 Configuration Management
- Git-based version control with trunk-based development and release branches
- Semantic versioning (MAJOR.MINOR.PATCH) for all software components
- Unique software build ID embedded in every deployed device image for traceability
- Full traceability from requirements -> design -> code -> test -> validation per IEC 62304 design controls

---

## 9. SECURITY & COMPLIANCE ARCHITECTURE

| Requirement | Approach |
|---|---|
| **IL-5 ATO** | AWS GovCloud / Azure Gov; STIG-hardened containers (DISA Container Platform SRG, Kubernetes STIG); continuous monitoring (Prisma Cloud) |
| **FedRAMP** | Leverage CSP inherited controls; SSP documentation; 3PAO assessment (Phase 3) |
| **Data at Rest** | AES-256 encryption (FIPS 140-3 validated modules or FIPS 140-2 modules within active validation period) |
| **Data in Transit** | TLS 1.3 minimum; MQTT over TLS; BLE 5.0+ with LE Secure Connections (FIPS-compliant pairing); application-layer encryption above BLE for PHI |
| **Access Control** | CAC/PIV authentication; RBAC; least privilege |
| **Audit Logging** | Immutable audit trail; SIEM integration (Splunk/ELK) |
| **CMMC / NIST 800-171** | All CUI handling per NIST SP 800-171 Rev 2 controls; CMMC Level 2 compliance pathway |
| **PHI Protection** | Patient data handling compliant with DoD 6025.18-R (DoD Health Information Privacy Regulation) and aligned with HIPAA Security Rule controls |
| **FDA SaMD** | IEC 62304 software lifecycle; risk management per ISO 14971; ISO 13485 quality management; 21 CFR Part 820 compliance |
| **Supply Chain** | SBOM generation (CycloneDX); dependency scanning; signed, reproducible builds |
| **Section 508** | Cloud analytics dashboard and provider portal compliant with Section 508 / WCAG 2.1 Level AA |
| **Data Retention** | Edge data purged after cloud sync confirmation; retention per DoD policy; device decommissioning per NIST SP 800-88 media sanitization guidelines |

---

## 10. KEY RISKS & MITIGATIONS

| Risk | Impact | Mitigation |
|---|---|---|
| Sensor hardware delays impact software timeline | HIGH | Develop against hardware abstraction layer + simulators from Week 1; hardware partner milestone tracked separately |
| FDA SaMD classification risk (Class II vs. Class III) | HIGH | Engage FDA Q-Submission (Pre-Submission) in Phase 1 for early classification guidance; limit intended-use claims to "clinical decision support" (not autonomous diagnosis) to maintain Class II 510(k) pathway |
| Training data access (JTTR DUA may take 3--6 months) | HIGH | Begin DUA process immediately; develop initial models on MIMIC-III/IV (public); validate and fine-tune on JTTR when available; domain adaptation techniques for sensor gap |
| BATDOK API changes or access restrictions | MEDIUM | Early engagement with PM Soldier Medical Devices for API documentation; fallback to standard HL7 FHIR interface |
| ATAK plugin certification delays | MEDIUM | Begin TAK Product Center engagement immediately; Phase 1-2 delivers alpha plugin, certification deferred to Phase 3 |
| Edge compute hardware performance | MEDIUM | Performance benchmarking on candidate hardware in Week 2; minimum requirements: ARM Cortex-A class, 4 GB RAM, 32 GB storage; fallback to dedicated inference co-processor if needed |
| ML model accuracy below threshold | MEDIUM | Ensemble approach; fallback to rule-based TCCC scoring per established clinical guidelines if thresholds not met |
| Consortium partner integration delays | MEDIUM | Formal interface control documents (ICDs) with each partner by Week 2; weekly consortium integration meetings |
| IL-5 ATO timeline exceeds prototype phase | LOW | Operate at IL-4 for prototype; IL-5 for production |
| Key personnel availability | MEDIUM | Cross-train team members; document architecture decisions thoroughly |

---

## 11. DECISION POINTS & NEXT STEPS

| Decision | Deadline | Owner |
|---|---|---|
| Confirm hardware partner & sensor platform | Feb 26, 2026 | Consortium Lead |
| BATDOK API access request submitted | Mar 5, 2026 | Tech Lead |
| ATAK SDK license secured | Mar 10, 2026 | Mobile Dev Lead |
| Cloud environment provisioned (GovCloud) | Mar 15, 2026 | DevOps Lead |
| ML training data agreements executed | Mar 15, 2026 | ML Lead |
| Edge AI prototype (v0.1) on dev hardware | Apr 1, 2026 | Edge Lead |
| Pitch Day rehearsal complete | Apr 4, 2026 | All Leads |

---

*Prepared by: Veteran Vectors Software Engineering Division | Authentic Consortium*
