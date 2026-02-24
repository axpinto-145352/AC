# 3C PLATFORM -- IMPLEMENTATION GUIDE

**Version:** 1.0 | **Classification:** Internal -- Authentic Consortium
**Prepared by:** Veteran Vectors (VV) Engineering
**Date:** February 24, 2026
**Purpose:** Actionable build plan for the 3C Platform assuming VIPC VVP Launch Grant award ($50K)

---

## 1. EXECUTIVE SUMMARY

This document is the engineering and business execution plan for building the **3C Platform** -- a unified Salesforce Health Cloud solution for Rural Health Clinics (RHCs) that addresses **Compliance**, **Care**, and **Collect Cash**. It covers the technical architecture, specific tools and licenses, development phases, cost breakdowns, team requirements, partner dependencies, and pilot strategy. This is a build document, not a pitch deck -- every line item is something VV will execute.

**Scope:** $50K VIPC grant funds Phase 1 (MVP). Subsequent phases funded by pilot revenue and Series A.

---

## 2. TECHNICAL ARCHITECTURE -- DETAILED BUILD SPECIFICATION

### 2.1 Platform Stack

| Layer | Technology | Purpose | License Model |
|---|---|---|---|
| **CRM/Core** | Salesforce Health Cloud (Enterprise) | Patient 360, care plans, provider workflows | $325/user/month |
| **Integration** | MuleSoft Anypoint (or Salesforce Connect + custom APIs) | EHR, wearable, clearinghouse connections | See cost analysis Sec. 6 |
| **AI/ML** | Salesforce Einstein + custom Python models (scikit-learn, XGBoost, PyTorch) | Risk stratification, NLP, anomaly detection | Einstein: $150/user/month (Agentforce Healthcare); custom models: self-hosted |
| **Security** | Salesforce Shield (Platform Encryption + Event Monitoring) | HIPAA encryption, audit trails, PHI access monitoring | ~30% of SF license spend |
| **Analytics** | Salesforce CRM Analytics (Tableau CRM) | Compliance dashboards, MIPS tracking, revenue analytics | Included in Health Cloud Enterprise |
| **Database** | Salesforce platform (PostgreSQL-backed) + external data warehouse (BigQuery or Snowflake) for ML training | Operational data in SF; analytics/training data in warehouse | SF: included; warehouse: usage-based |
| **Hosting (custom models)** | Google Cloud Platform (GCP) Healthcare API or AWS HealthLake | HIPAA-eligible model serving, FHIR data store | GCP: ~$500--$2,000/month at pilot scale |
| **DevOps** | GitHub (private repos) + GitHub Actions CI/CD | Source control, automated testing, deployment | GitHub Team: $4/user/month |
| **Monitoring** | Salesforce Event Monitoring + Datadog (APM) | Application performance, error tracking | Datadog: ~$15/host/month |

### 2.2 Phase 1 (MVP) Architecture -- What We Actually Build First

For the $50K grant phase, we do NOT build the full architecture. We build a functional MVP on a constrained stack:

```
+------------------------------------------------------------------+
|              PHASE 1 MVP ARCHITECTURE ($50K Budget)               |
|                                                                   |
|  +---------------------------+  +------------------------------+  |
|  | Salesforce Health Cloud   |  | Custom AI Microservices      |  |
|  | (Enterprise, 5 users)     |  | (GCP Cloud Run, Python)      |  |
|  |                           |  |                              |  |
|  | - Patient records (360)   |  | - Risk stratification model |  |
|  | - Care plan templates     |  |   (XGBoost on CMS PUF data) |  |
|  | - Compliance task mgmt    |  | - Basic NLP for coding      |  |
|  | - MIPS quality tracking   |  |   suggestions (spaCy +      |  |
|  | - RPM data display        |  |   MedCAT)                   |  |
|  | - Basic billing tracking  |  |                              |  |
|  +------------+--------------+  +--------------+---------------+  |
|               |                                |                  |
|               +----------+  +------------------+                  |
|                          |  |                                     |
|               +----------+--+------------------+                  |
|               | Integration Layer              |                  |
|               | (Salesforce Connect +          |                  |
|               |  Named Credentials +           |                  |
|               |  Apex REST callouts)           |                  |
|               +---------+-----------+----------+                  |
|                         |           |                             |
|            +------------+    +------+--------+                    |
|            | EHR (FHIR R4)   | RPM Devices   |                   |
|            | (1-2 systems)   | (BLE/API)     |                   |
|            +----------------+ +--------------+                    |
+------------------------------------------------------------------+
```

**Key MVP decisions:**
- **No MuleSoft in Phase 1.** MuleSoft starts at ~$50K/year minimum -- that's our entire grant. Use Salesforce Connect, Named Credentials, and Apex REST callouts for Phase 1 integrations. MuleSoft comes in Phase 2 when revenue supports it.
- **Custom AI models hosted externally.** Salesforce Einstein for basic automation (lead scoring, flow triggers). Custom ML models (risk stratification, NLP) deployed as containerized Python services on GCP Cloud Run (HIPAA-eligible with BAA). Called from Salesforce via REST API.
- **Shield encryption required from Day 1.** Non-negotiable for HIPAA. Budget for it.
- **5 Salesforce users for pilot.** Enough for 2--3 clinic staff + VV admin/support users.

### 2.3 EHR Integration Strategy

**Target EHR systems for RHC market** (by market share in small/rural practices):

| EHR | RHC Market Share | FHIR R4 Support | Integration Approach |
|---|---|---|---|
| **eClinicalWorks (eCW)** | ~12% ambulatory (largest cloud ambulatory install base, 850K+ physicians) | Yes (certified) | eCW FHIR API; strong in FQHCs and primary care |
| **athenahealth** | ~7% ambulatory (Best in KLAS 2025 for independent practices) | Yes (certified) | athenahealth FHIR APIs (well-documented, developer-friendly); integrated RCM |
| **MEDITECH Expanse** | ~13% acute care (dominant in rural/community hospitals) | Yes | MEDITECH FHIR endpoints; 29 of Becker's "2025 Great Community Hospitals" use MEDITECH |
| **Azalea Health** | Niche (purpose-built for RHCs) | Yes (ONC-certified) | Cloud-based, integrated clearinghouse, handles RHC split billing and UB04/CMS1500 formats. HITRUST E1 certified |
| **TruBridge/CPSI (Evident)** | ~9% acute care (specifically for rural/community hospitals) | Partial | Integrated clearinghouse and RCM; may need HL7v2 interface for older versions |

**Phase 1 pilot target:** Integrate with **1 EHR system** used by the pilot clinics. Prioritize eClinicalWorks or athenahealth -- both have the best FHIR R4 support and developer programs. If pilot clinics use **Azalea Health**, that's ideal since Azalea is purpose-built for RHCs and has native RHC billing support.

**FHIR Implementation Guides to follow:**
- US Core (v6.1.0) -- mandatory baseline for all US clinical data exchange
- SMART on FHIR (for app authorization)
- Bulk FHIR (for panel-level data extraction)
- DaVinci DEQM (Data Exchange for Quality Measures) -- for MIPS/eCQM reporting via FHIR
- DaVinci CRD/PAS (Coverage Requirements Discovery / Prior Authorization Support) -- Phase 2 for claims optimization
- C-CDA on FHIR -- bridge for legacy EHRs that still produce C-CDA documents rather than native FHIR

### 2.4 Wearable/RPM Device Integration

**Phase 1 target devices** (most commonly used in clinical RPM programs):

| Device Type | Recommended Device | Approx. Cost/Unit | Integration Method |
|---|---|---|---|
| **Blood Pressure Cuff** | Smart Meter iBloodPressure (cellular, no WiFi needed) or Omron VitalSight (BP8000-M) | $80--$150 | Cellular direct to cloud (Smart Meter API) or Tenovi gateway API |
| **Pulse Oximeter** | Smart Meter iPulseOx (cellular) or Nonin 3230 (BLE via Tenovi) | $100--$300 | Smart Meter API or Tenovi aggregator API |
| **Glucose Monitor** | Smart Meter iGlucose Plus (cellular) or Dexcom Stelo (OTC CGM, no prescription) | $70--$150/month | Smart Meter API or Dexcom Clarity API |
| **Weight Scale** | Smart Meter iScale (cellular) or BodyTrace e-Scale (cellular) | $50--$120 | Smart Meter API or BodyTrace API |

**Critical for rural: Cellular-connected devices are mandatory.** Rural patients often lack reliable WiFi or smartphones. Devices from Smart Meter and Prevounce (Pylo) transmit data via built-in cellular modems (multi-carrier SIM) with zero patient tech setup. BLE-based devices (Omron, Withings, Nonin) require a gateway -- **Tenovi** provides a cellular hub that bridges 40+ FDA-cleared BLE devices to their cloud API, making them viable for rural use.

**Recommended Phase 1 approach:** Partner with **Tenovi** as the device aggregation layer. One API integration covers 40+ devices from A&D Medical, Omron, Transtek, Trividia, Nonin, and Welch Allyn. Alternatively, go direct with **Smart Meter** for the simplest rural deployment (proprietary cellular devices, zero patient setup).

**RPM data flow (Phase 1):**
```
Patient device (cellular) -> Device vendor cloud (Smart Meter / Tenovi)
                                              |
                             VV integration service (GCP Cloud Run)
                                              |
                                    Transform to FHIR Observation
                                              |
                                    POST to Salesforce Health Cloud
                                              |
                                    Trigger alert Flow if threshold exceeded
```

**Billing trigger logic:** Track device data transmission days per patient per month. When a patient hits 16 days of data in a calendar month, auto-flag as billable for CPT 99454 ($52.11). Track clinician interactive time for 99457/99458.

---

## 3. MODULE BUILD SPECIFICATIONS

### 3.1 Compliance Module -- Build Details

| Feature | Salesforce Implementation | Custom Development | Phase |
|---|---|---|---|
| **HIPAA Compliance Tracker** | Custom object: `HIPAA_Compliance_Task__c` with fields for task type, due date, assignee, status, evidence attachment. Flow-based reminders and escalation | None -- pure configuration | Phase 1 |
| **HIPAA Risk Assessment** | Pre-built assessment questionnaire (Salesforce Survey or custom LWC form) mapped to NIST SP 800-66 controls. Auto-scores risk level | LWC (Lightning Web Component) for assessment UI | Phase 1 |
| **HRSA UDS Data Aggregation** | Report type pulling from Patient, Encounter, Diagnosis, and Demographics objects. Pre-built reports matching UDS Table structure (Tables 3A, 3B, 4, 5, 6A, 6B, 7, 8A, 9D, 9E). **Note:** UDS reporting is mandatory for HRSA-funded health centers (FQHCs), not standalone RHCs. However, many RHCs are also FQHCs, and building this positions all clinics for value-based care | Apex batch job to aggregate data across reporting period; export to UDS-compatible format | Phase 2 |
| **CMS Quality Measure Dashboard** | CRM Analytics dashboard tracking MIPS measures: Quality (30%), Cost (30%), Promoting Interoperability (25%), Improvement Activities (15%). Real-time score projection | Apex scheduled job to calculate measure numerators/denominators from clinical data | Phase 1 (basic), Phase 2 (full) |
| **Regulatory Change Alerts** | Integration with Federal Register API + CMS/HRSA RSS feeds. Flow-triggered notifications when relevant changes detected | Python NLP service to classify regulatory updates by relevance to RHC operations | Phase 3 |
| **FCC Broadband Compliance** | Custom object tracking E-Rate/RHC Program filings, deadlines, and documentation | None -- pure configuration | Phase 2 |

**Salesforce objects to create (Phase 1):**
- `Compliance_Task__c` (master-detail to Account)
- `Risk_Assessment__c` (master-detail to Account)
- `Risk_Assessment_Response__c` (master-detail to Risk_Assessment__c)
- `Quality_Measure__c` (lookup to Account)
- `Quality_Measure_Result__c` (master-detail to Quality_Measure__c, lookup to Contact/Patient)

### 3.2 Care Module -- Build Details

| Feature | Salesforce Implementation | Custom Development | Phase |
|---|---|---|---|
| **Patient Risk Stratification** | Einstein prediction on Contact (Patient) object, or external model score written back to custom field `Risk_Score__c` | XGBoost model trained on CMS Public Use Files (Medicare claims, chronic conditions). Features: age, diagnosis codes (HCCs), utilization history, medication count, social determinants. Deployed on GCP Cloud Run, called via Apex REST callout | Phase 1 |
| **RPM Data Ingestion** | Custom objects: `RPM_Reading__c` (master-detail to Contact). Fields: device type, measurement value, measurement date, device ID, transmission flag | Python integration service on GCP Cloud Run. Pulls from device manufacturer APIs (Omron, Withings, Dexcom), transforms to `RPM_Reading__c` records via Salesforce REST API | Phase 1 |
| **Deterioration Alerts** | Flow triggered on `RPM_Reading__c` insert. Evaluates against threshold rules (e.g., systolic BP >180, SpO2 <90, weight gain >3 lbs/day). Creates Task for care team, sends push notification | Phase 1: rule-based thresholds. Phase 2: ML trend analysis model (sliding-window anomaly detection) | Phase 1 (rules), Phase 2 (ML) |
| **Care Gap Detection** | Scheduled Apex job comparing patient records against USPSTF/CMS preventive care guidelines. Generates `Care_Gap__c` records for overdue screenings, immunizations, annual wellness visits | Guideline rules engine in Apex. Initial rule set: A1C testing (diabetics), mammography, colorectal screening, flu/pneumonia vaccines, annual wellness visit, depression screening (PHQ-9) | Phase 1 |
| **Care Plan Management** | Health Cloud native Care Plan object with custom care plan templates for top chronic conditions (diabetes, hypertension, COPD, CHF, depression) | None -- Health Cloud configuration + custom templates | Phase 1 |
| **Telehealth Integration** | Embedded video link (Zoom for Healthcare or Doxy.me) in patient record. One-click launch from Salesforce | Zoom API or Doxy.me widget embedded via LWC | Phase 2 |

**ML Model Specification (Risk Stratification):**

| Parameter | Value |
|---|---|
| **Algorithm** | XGBoost (gradient-boosted trees) -- baseline; logistic regression for interpretability comparison |
| **Training Data** | CMS Medicare Public Use Files (100% sample claims data), CMS Chronic Conditions Data Warehouse (CCW) public data, MIMIC-IV (if needed for clinical validation) |
| **Features** | Age, sex, HCC risk score, diagnosis count (ICD-10 categories), medication count, ED visits (12 months), inpatient admits (12 months), primary care visits (12 months), days since last visit, social vulnerability index (SVI) by census tract |
| **Target Variable** | Binary: hospitalization or ED visit within 90 days |
| **Output** | Risk score (0--100) + risk tier (Low/Medium/High/Critical) + top 3 contributing factors (SHAP values) |
| **Performance Target** | AUC-ROC >0.75; sensitivity >80% for top-decile risk patients |
| **Framework** | scikit-learn + XGBoost (Python); model serialized with joblib; served via FastAPI on GCP Cloud Run |
| **Retraining Cadence** | Quarterly with updated claims data; triggered retraining if AUC drops below 0.72 |
| **Interpretability** | SHAP (SHapley Additive exPlanations) for per-patient feature importance; required for clinical adoption |

### 3.3 Collect Cash Module -- Build Details

| Feature | Salesforce Implementation | Custom Development | Phase |
|---|---|---|---|
| **RPM Billing Tracker** | Custom object: `Billing_Event__c` (master-detail to Contact). Automated tracking of device data transmission days per patient per month. Flow logic: when `RPM_Reading__c` count >= 16 in a calendar month, create billable event for CPT 99454 ($52.11). Clinician time tracking for 99457/99458 | Apex scheduled batch: nightly roll-up of RPM readings per patient, flagging billable thresholds | Phase 1 |
| **CCM Time Tracking** | Custom object: `CCM_Activity__c` with fields for patient, clinician, activity type, duration (minutes), date. Flow logic: when cumulative minutes >= 20 in a calendar month, flag for CPT 99490 ($66.30). Track complex CCM threshold (60 min) for 99487 ($144.00) | Timer LWC component embedded in patient record for real-time time capture | Phase 1 |
| **TCM Workflow** | Flow triggered on `Discharge_Notification__c` creation. Auto-creates tasks: (1) patient contact within 2 business days, (2) medication reconciliation, (3) face-to-face visit within 7 or 14 days. Tracks completion for CPT 99495 ($220) / 99496 ($298) | ADT (Admit/Discharge/Transfer) feed integration from hospital EHR (HL7v2 ADT message or FHIR Encounter) | Phase 2 |
| **Coding Optimization** | NLP analysis of clinical notes to suggest missed diagnosis codes (HCCs) that affect risk adjustment and reimbursement | Python NLP pipeline: spaCy + MedCAT (medical concept annotation) + custom HCC mapping. Deployed on GCP Cloud Run | Phase 2 |
| **Denial Prevention** | Rules engine checking claims against common denial reasons (missing auth, timely filing, documentation gaps) before submission | Apex rules engine with payer-specific rule sets; integration with clearinghouse pre-adjudication API | Phase 3 |
| **MIPS Payment Projection** | CRM Analytics dashboard modeling projected MIPS payment adjustment based on current performance scores. Shows gap to avoid -9% penalty and path to positive adjustment | Apex calculation engine using CMS MIPS scoring methodology (Quality 30%, Cost 30%, PI 25%, IA 15%) | Phase 1 (basic), Phase 2 (full) |

**CMS Reimbursement Reference (2026 Rates):**

| CPT Code | Service | 2026 Rate | Billing Threshold |
|---|---|---|---|
| 99453 | RPM device setup (one-time) | $22.00 | Initial setup + 2 days monitoring |
| 99454 | RPM device supply/data (monthly) | $52.11 | 16+ days of data transmission |
| 99457 | RPM first 20 min interactive (monthly) | $51.77 | 20 min clinician time |
| 99458 | RPM additional 20 min (up to 3x/month) | $52.00 | Each additional 20 min |
| 99490 | CCM first 20 min (monthly) | $66.30 | 20 min staff time, 2+ chronic conditions |
| 99439 | CCM additional 20 min (up to 2x/month) | $50.56 | Each additional 20 min |
| 99487 | Complex CCM first 60 min (monthly) | $144.00 | 60 min staff time, complex needs |
| 99489 | Complex CCM additional 30 min | $78.00 | Each additional 30 min |
| 99495 | TCM moderate complexity | $220.00 | Contact within 2 days, visit within 14 days |
| 99496 | TCM high complexity | $298.00 | Contact within 2 days, visit within 7 days |

**Revenue unlock per clinic (conservative estimate):**
Assume a pilot clinic with 800 Medicare patients, 25% chronic disease prevalence (200 patients eligible for CCM/RPM), 10% enrolled in RPM in Year 1 (80 patients), 15% enrolled in CCM (120 patients):

| Revenue Stream | Patients | Monthly/Patient | Annual Revenue |
|---|---|---|---|
| RPM (99454 + 99457) | 80 | $103.88 | $99,725 |
| CCM (99490) | 120 | $66.30 | $95,472 |
| MIPS penalty avoidance (-9% on Medicare) | -- | -- | $36,000--$72,000 (depending on Medicare volume) |
| **Total new annual revenue per clinic** | | | **$195,000--$267,000** |

---

## 4. DEVELOPMENT ROADMAP

### Phase 1: MVP / Proof of Concept (Months 1--4, $50K VIPC Grant)

**Goal:** Working 3C Platform deployed at 2--3 Virginia RHCs with core functionality in all three modules.

| Month | Sprint | Deliverables |
|---|---|---|
| **Month 1** | Sprint 1--2 | **Foundation:** Salesforce Health Cloud instance provisioned (Enterprise, 5 users). Shield encryption enabled. Core data model deployed (custom objects, fields, relationships). Patient import from pilot clinic EHR (manual CSV or FHIR bulk export). HIPAA compliance task tracker live. Care plan templates configured for diabetes, hypertension, CHF |
| **Month 2** | Sprint 3--4 | **Care + RPM:** EHR FHIR integration with pilot clinic EHR (athenahealth or eCW -- read-only patient/encounter data). RPM device integration (1--2 device types: BP cuff + scale or glucose monitor). RPM data flowing into Salesforce. Alert rules configured (threshold-based). Care gap detection rules for top 6 preventive measures. Risk stratification model v1 trained and deployed (GCP Cloud Run) |
| **Month 3** | Sprint 5--6 | **Collect Cash + Quality:** RPM billing tracker live (auto-flagging billable thresholds for 99453/99454/99457). CCM time tracking LWC deployed. MIPS quality measure dashboard (basic -- 3--5 key measures). Compliance dashboard for pilot clinics. End-to-end testing with pilot clinic staff |
| **Month 4** | Sprint 7--8 | **Pilot Launch:** 2--3 Virginia RHCs live on 3C Platform. Staff training completed. Baseline metrics captured (compliance scores, care gaps, billing capture rate). Bug fixes and UX refinements based on staff feedback. Pilot outcomes report for Series A / next funding round |

### Phase 2: Full Product (Months 5--10, funded by pilot revenue + seed investment)

| Month | Deliverables |
|---|---|
| **5--6** | MuleSoft integration layer (replace Apex callouts). Additional EHR integrations (2--3 more EHR systems). HRSA UDS report automation. Full MIPS dashboard (all 4 categories). Telehealth integration (Zoom for Healthcare) |
| **7--8** | NLP coding optimization engine (spaCy + MedCAT). TCM workflow automation (ADT feed integration). Denial prevention rules engine (top 20 denial reasons). ML-based deterioration prediction (replaces rule-based alerts). Additional RPM devices (3--5 device types total) |
| **9--10** | Multi-clinic deployment (10+ Virginia RHCs). Regulatory change monitoring (Federal Register NLP). AppExchange packaging exploration (ISV partner program). Performance benchmarking and case study publication |

### Phase 3: Scale (Months 11--18, funded by Series A)

| Month | Deliverables |
|---|---|
| **11--13** | AppExchange managed package (ISV distribution). Automated onboarding workflow (clinic self-provisioning). White-label/partner channel strategy. 50+ Virginia RHCs |
| **14--16** | National expansion (target states: West Virginia, Kentucky, Tennessee, North Carolina -- high RHC density). Advanced AI features (population health analytics, predictive staffing). Clearinghouse direct integration (Availity, Change Healthcare/Optum) |
| **17--18** | 100+ RHCs nationally. Series A close based on ARR and clinical outcomes data. SOC 2 Type II audit. HITRUST certification pathway |

---

## 5. TEAM REQUIREMENTS

### 5.1 Phase 1 Team (Months 1--4) -- Minimum Viable Team

| Role | Who | Commitment | Rate/Cost |
|---|---|---|---|
| **Technical Lead / Salesforce Architect** | Will Nelson (VV) | 30 hrs/week | Sweat equity (VV contribution to ACT) |
| **Salesforce Developer** | Contract (Salesforce certified, Health Cloud experience) | 30 hrs/week x 4 months | $125--$150/hr = $60K--$72K (over budget -- see note below) |
| **ML Engineer** | Contract or VV team member | 15 hrs/week x 3 months (Months 1--3) | $150/hr = $27K (or VV sweat equity) |
| **Clinical Advisor / SME** | Cari Ann (ACT) + pilot clinic provider | 5 hrs/week | ACT sweat equity |
| **Project Manager** | Jim Pfautz (ACT CEO) | 5 hrs/week | ACT sweat equity |

**Budget reality check:** A fully-contracted team exceeds $50K. The model that works:

| Item | Funded by VIPC Grant | Funded by VV/ACT Sweat Equity |
|---|---|---|
| Salesforce licenses (5 users x 4 months) | $6,500 | -- |
| Salesforce Shield (4 months) | $1,950 | -- |
| GCP hosting (HIPAA, 4 months) | $2,000 | -- |
| RPM devices for pilot (10--15 units) | $1,500 | -- |
| Contract Salesforce developer (part-time, 3 months) | $30,000 | -- |
| ML model development tools/compute | $1,500 | -- |
| Pilot clinic onboarding (travel, training) | $3,000 | -- |
| Legal (HIPAA BAA, pilot agreements) | $2,000 | -- |
| Miscellaneous (domain, email, tools) | $1,550 | -- |
| **VIPC Grant Total** | **$50,000** | -- |
| Technical Lead (Will, 480 hrs) | -- | ~$72,000 (in-kind) |
| ML Engineering (VV team, 180 hrs) | -- | ~$27,000 (in-kind) |
| Clinical Advisory (Cari Ann, 80 hrs) | -- | ~$12,000 (in-kind) |
| Project Management (Jim, 80 hrs) | -- | ~$12,000 (in-kind) |
| **Total Project Value (Phase 1)** | **$50,000 cash** | **~$123,000 in-kind** |

### 5.2 Phase 2 Team Additions (Months 5--10)

| Role | Needed | Estimated Annual Cost |
|---|---|---|
| Full-time Salesforce Developer | 1 FTE | $120,000--$140,000 |
| Full-time ML/Data Engineer | 1 FTE | $130,000--$150,000 |
| Implementation Specialist (clinic onboarding + training) | 1 FTE | $70,000--$85,000 |
| Customer Success / Support | 0.5 FTE | $35,000--$42,000 |
| Sales / Business Development | 1 FTE (likely Jim/ACT) | Sweat equity or $80,000--$100,000 |

**Phase 2 run rate:** ~$435,000--$517,000/year (team + infrastructure). Funded by combination of pilot clinic SaaS revenue, ACT operating capital, and seed investment.

### 5.3 Key Hires -- What to Look For

**Contract Salesforce Developer (Phase 1 -- critical hire):**
- Must have: Salesforce Health Cloud certification, Apex development, LWC, FHIR integration experience
- Nice to have: Experience with healthcare payer/provider workflows, HIPAA compliance
- Where to find: Salesforce Talent Alliance, Upwork (vetted Salesforce pros), Toptal, or Salesforce partner firms (10th Magnitude, Deloitte Digital -- may be too expensive)
- Budget option: Offshore Salesforce developer ($50--$75/hr) with US-based oversight by Will

**ML Engineer (Phase 1):**
- Must have: Python, scikit-learn/XGBoost, healthcare data experience (claims data, ICD-10, HCC)
- Nice to have: FHIR, GCP, FastAPI deployment experience
- Budget option: VV internal resource or university partnership (Virginia Tech, UVA -- health informatics graduate students)

---

## 6. DETAILED COST ANALYSIS

### 6.1 Salesforce Licensing -- Realistic Costs

**Phase 1 (MVP, 5 users, 4 months):**

| Line Item | Monthly | 4-Month Total |
|---|---|---|
| Health Cloud Enterprise (5 users x $325) | $1,625 | $6,500 |
| Shield encryption (~30% of license) | $488 | $1,950 |
| Einstein/Agentforce (defer to Phase 2) | $0 | $0 |
| MuleSoft (defer to Phase 2) | $0 | $0 |
| **Salesforce Subtotal** | **$2,113** | **$8,450** |

**Note on discounts:** Apply for the Salesforce ISV Partner Program (free to join). ISV partners get 2 free Enterprise Sales Cloud licenses and access to discounted development environments. Also explore the Salesforce Startup Program -- potential for significant discount or free first year. This could reduce Phase 1 Salesforce costs by 25--50%.

**Phase 2 (10 users, full year):**

| Line Item | Monthly | Annual |
|---|---|---|
| Health Cloud Enterprise (10 users x $325) | $3,250 | $39,000 |
| Shield (~30%) | $975 | $11,700 |
| Agentforce Healthcare (10 users x $150) | $1,500 | $18,000 |
| MuleSoft Anypoint (Integration Starter) | ~$4,200 | ~$50,000 |
| **Salesforce Subtotal** | **~$9,925** | **~$118,700** |

### 6.2 Infrastructure Costs

**Phase 1:**

| Item | Monthly | 4-Month Total |
|---|---|---|
| GCP Cloud Run (HIPAA BAA, model serving) | $300--$500 | $1,200--$2,000 |
| GCP Cloud Storage (training data, backups) | $50 | $200 |
| GitHub Team (5 users) | $20 | $80 |
| Domain + SSL + email (Google Workspace) | $60 | $240 |
| **Infrastructure Subtotal** | **~$530** | **~$2,120** |

**Phase 2 (annual):**

| Item | Annual |
|---|---|
| GCP (expanded: Cloud Run + BigQuery + Cloud SQL) | $12,000--$18,000 |
| Datadog APM | $3,600 |
| GitHub Team (10 users) | $480 |
| Google Workspace | $720 |
| **Infrastructure Subtotal** | **~$17,000--$23,000** |

### 6.3 Total Cost Summary

| Phase | Timeline | Cash Cost | In-Kind (Sweat Equity) | Total Value |
|---|---|---|---|---|
| **Phase 1 (MVP)** | Months 1--4 | $50,000 (VIPC grant) | ~$123,000 | ~$173,000 |
| **Phase 2 (Full Product)** | Months 5--10 | ~$300,000--$400,000 | ~$150,000 | ~$450,000--$550,000 |
| **Phase 3 (Scale)** | Months 11--18 | ~$600,000--$800,000 | ~$100,000 | ~$700,000--$900,000 |
| **Total through Month 18** | | **~$950,000--$1,250,000** | **~$373,000** | **~$1,320,000--$1,620,000** |

---

## 7. PARTNER DEPENDENCIES

### 7.1 Required Partners (Phase 1)

| Partner Type | Why Needed | Candidates | Status |
|---|---|---|---|
| **Pilot RHCs (2--3 clinics)** | Live environment to deploy, test, and demonstrate the platform. Must have Medicare patient panel, chronic disease population, and willingness to participate | Virginia RHCs -- identify through Virginia Rural Health Association or HRSA Health Center database. Target clinics using athenahealth or eCW for easier EHR integration | **Must secure by Month 1** |
| **Salesforce Implementation Partner** | Optional but valuable -- can provide discounted licenses through partner program, development support, and AppExchange guidance | Small Salesforce Health Cloud partners: Silverline, Penrod, or local Virginia firms | Explore in Month 1 |
| **RPM Device Vendor / Aggregator** | Device supply for pilot patients, API access for data integration, and potential reseller arrangement. **Cellular connectivity required for rural patients** | **Tenovi** (device aggregation platform, 40+ FDA-cleared devices, cellular gateway, single API); **Smart Meter** (proprietary cellular devices, zero patient setup, multi-carrier SIM); **Prevounce/Pylo** (integrated device + platform line) | **Must secure by Month 2** |

### 7.2 Required Partners (Phase 2--3)

| Partner Type | Why Needed | Candidates | Timeline |
|---|---|---|---|
| **Clearinghouse** | Claims submission, eligibility verification, ERA/EOB processing | **Office Ally** (free for claim submission, 80K+ healthcare orgs, easiest setup) as Phase 2 first target. Availity (free for payer-sponsored eligibility checks) as secondary. Trizetto/Cognizant for advanced scrubbing in Phase 3 | Phase 2 |
| **Billing Service / Coding Experts** | Validate coding optimization logic, provide training data for NLP model, clinical coding advisory | Local medical billing company or AAPC-certified coders | Phase 2 |
| **HIPAA/Compliance Counsel** | BAA review, HIPAA policies, compliance attestation support | Heath care IT law firm (Virginia-based) | Phase 1 (BAA), Phase 2 (full) |
| **Salesforce ISV Partner** | Required for AppExchange distribution, managed package development | Self (VV registers as ISV partner -- free) | Phase 2 |

### 7.3 Strategic Relationships

| Entity | Value | Approach |
|---|---|---|
| **Virginia Rural Health Association** | Clinic introductions, market validation, policy advocacy | Jim/Mandy relationship-building; potential advisory board member |
| **HRSA / Federal Office of Rural Health Policy** | Grant opportunities (HRSA has rural health IT grants), regulatory guidance, credibility | Monitor HRSA funding announcements; apply for Rural Health IT Network grant |
| **Virginia Department of Health** | State-level rural health initiatives, Medicaid waivers, pilot endorsement | Mandy's political connections |
| **University Partners (UVA, VT, VCU)** | Health informatics talent, clinical research collaboration, IRB for outcomes studies | Internship pipeline, joint publications, capstone project sponsorship |

---

## 8. COMPLIANCE & SECURITY REQUIREMENTS

### 8.1 HIPAA Compliance (Day 1 Requirements)

| Requirement | Implementation |
|---|---|
| **Business Associate Agreements (BAAs)** | Execute BAAs with: Salesforce (standard BAA available), GCP (standard BAA), any EHR vendor, any RPM device vendor, any subcontractor with PHI access. **Must be in place before any patient data enters the system** |
| **Encryption at Rest** | Salesforce Shield Platform Encryption (AES-256, tenant-specific keys). GCP default encryption (AES-256) with customer-managed keys (CMEK) for additional control |
| **Encryption in Transit** | TLS 1.2+ (Salesforce enforces by default). All custom API calls use HTTPS only. FHIR endpoints authenticated via OAuth 2.0 / SMART on FHIR |
| **Access Control** | Salesforce profiles + permission sets (RBAC). Principle of least privilege. Separate profiles for: clinic admin, provider, care coordinator, VV admin |
| **Audit Logging** | Salesforce Shield Event Monitoring (login, API, data export, record access). Retain logs for 6 years (HIPAA requirement) |
| **Workforce Training** | All VV and ACT team members with PHI access complete HIPAA training before pilot launch. Annual refresher. Document completion |
| **Incident Response Plan** | Document and test PHI breach response procedure per HIPAA Breach Notification Rule (45 CFR 164.400--414). 60-day notification window to HHS if >500 individuals affected |
| **Risk Assessment** | Complete HIPAA Security Rule risk assessment (NIST SP 800-66 methodology) before pilot launch. Document findings and remediation plan |

### 8.2 State and Federal Regulatory

| Requirement | Notes |
|---|---|
| **Virginia Consumer Data Protection Act (VCDPA)** | Health data exemptions exist for HIPAA-covered data, but verify applicability for any non-PHI patient data |
| **42 CFR Part 2** | If any pilot clinic treats substance use disorders, additional consent and segmentation requirements apply |
| **FDA SaMD** | Risk stratification AI that informs clinical decisions may be subject to FDA Software as a Medical Device regulation. However, if positioned as "clinical decision support" that a provider reviews and acts on (not autonomous), likely qualifies for exemption under 21st Century Cures Act Section 3060(a). Document intended use carefully |
| **CMS Conditions of Participation** | Any software used for billing must not create false claims. Validate all auto-generated billing events against actual clinical documentation |

---

## 9. SUCCESS METRICS

### 9.1 Phase 1 Pilot KPIs (Month 4 Report)

| Category | Metric | Target |
|---|---|---|
| **Compliance** | HIPAA compliance task completion rate | >90% |
| **Compliance** | MIPS quality measures tracked and reported | 5+ measures per clinic |
| **Care** | Patients enrolled in RPM | 30+ per pilot clinic |
| **Care** | Care gaps identified and addressed | 50+ per clinic |
| **Care** | Risk stratification model AUC-ROC | >0.75 |
| **Cost** | New RPM/CCM revenue captured per clinic (monthly) | $5,000+ |
| **Cost** | RPM billing events auto-flagged correctly | >95% accuracy |
| **Platform** | Clinic staff adoption (weekly active users) | >80% of licensed users |
| **Platform** | System uptime | >99.5% |

### 9.2 Metrics for Series A Pitch (Month 10)

| Metric | Target |
|---|---|
| Clinics live on platform | 10+ |
| ARR (Annual Recurring Revenue) | $240,000+ ($2K/month x 10 clinics) |
| Net revenue unlock per clinic | $100,000+/year |
| Clinic retention (churn) | <5% monthly |
| NPS (staff satisfaction) | >50 |
| MIPS penalty avoidance demonstrated | 100% of pilot clinics |

---

## 10. COMPETITIVE LANDSCAPE

### 10.1 Direct Competitors

| Competitor | What They Do | Pricing | Why 3C Wins |
|---|---|---|---|
| **Compliancy Group (The Guard)** | HIPAA compliance tracking only | ~$300/month | Compliance only -- no care or billing |
| **HIPAA One / Intraprise Health** | HIPAA risk assessments | ~$200--$500/month | Compliance only |
| **Optimize Health** | RPM platform only | $6--$12/patient/month | Care/RPM only -- no compliance or billing optimization |
| **Rimidi** | Chronic disease management + RPM | Custom pricing | Care only -- no compliance or billing |
| **ThoroughCare** | CCM/RPM/TCM/AWV workflow + billing | ~$3--$8/patient/month | Closest competitor -- but no compliance module, no AI risk stratification, not Salesforce-native |
| **ChartSpan** | Outsourced CCM services | Revenue share model | Service, not software -- takes margin from clinic |
| **Waystar / Availity** | Revenue cycle management | $500--$2,000/month | Billing only -- no clinical or compliance |
| **athenahealth RCM** | EHR + built-in billing | Bundled with EHR | General-purpose -- not optimized for RHC-specific programs (RPM/CCM/MIPS) |
| **TelliHealth** | End-to-end RPM (devices + platform + monitoring) | Per patient/month | 4G LTE devices, good rural fit -- but RPM only, no compliance or billing optimization |
| **HealthSnap** | RPM with clinical monitoring | Per patient/month | Strong outcomes data -- but RPM only |
| **Azalea Health** | RHC-specific EHR + billing | Bundled | Closest RHC-specific competitor -- but no AI, limited RPM, no standalone compliance module |

### 10.2 Pricing Strategy

**Target RHC IT budget reality:** 81% of rural providers cite budget constraints as the biggest obstacle to new technology (Black Book Research, 2025). A typical 3-provider RHC spends $34,000--$95,000/year on all IT. Our pricing must land in a range that fits within existing budgets while being justified by revenue unlock.

| Tier | Monthly Price | Includes | Target Clinic |
|---|---|---|---|
| **Starter** (Compliance + Basic Care) | $500/month | HIPAA compliance tracker, care gap detection, basic MIPS dashboard, 50 patients | Small RHC, 1--2 providers |
| **Professional** (Full 3C) | $2,000/month | All three modules, RPM integration, AI risk stratification, up to 200 patients | Mid-size RHC, 3--5 providers |
| **Enterprise** | $4,000/month | Full 3C + NLP coding optimization, unlimited patients, dedicated support | Large RHC or multi-site |

**Revenue justification:** At $2,000/month ($24,000/year), the platform unlocks $195,000--$267,000/year in new RPM/CCM/MIPS revenue. That's an **8--11x ROI**. The platform sells itself on the math.

**Key funding tailwind:** The **Rural Health Transformation (RHT) Program** allocates **$50 billion over 5 years** to states, with permissible uses including software, hardware, cybersecurity, remote monitoring, and AI. Position the 3C Platform as eligible technology spend under this program -- clinics may be able to fund their subscription through RHT grants.

### 10.3 Competitive Moat

1. **Unified platform:** No competitor offers compliance + care + revenue on one platform. Clinics currently buy 3--5 separate tools that don't talk to each other
2. **RHC-specific:** Purpose-built for the regulatory, clinical, and financial realities of Rural Health Clinics -- not a hospital product scaled down
3. **Salesforce ecosystem:** Builds on enterprise infrastructure that scales; avoids the "small vendor" risk that RHCs worry about
4. **AI-first revenue optimization:** The AI doesn't just track -- it finds money. Risk stratification identifies patients who need (and qualify for) RPM/CCM. NLP finds missed codes. MIPS projection prevents penalties. The platform literally pays for itself
5. **Virginia-first strategy:** Deep local relationships, VIPC backing, state policy alignment -- hard for national competitors to replicate

---

## 11. RISK REGISTER

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| **Salesforce costs exceed budget** | HIGH | MEDIUM | Apply for ISV Partner Program and Startup Program discounts immediately. Negotiate multi-year commit. Phase 1 uses minimal user count (5). If costs still prohibitive, evaluate Salesforce Platform (cheaper) instead of Health Cloud |
| **Pilot clinic EHR integration harder than expected** | HIGH | MEDIUM | Start with manual data import (CSV) as fallback. Prioritize EHRs with strong FHIR support (athenahealth, eCW). Budget 2 extra weeks for integration troubleshooting |
| **Clinic staff adoption resistance** | HIGH | MEDIUM | Involve clinic staff in design from Sprint 1. Keep UI simple (max 3 clicks to any action). Provide on-site training. Show revenue impact early to build buy-in |
| **RPM patient enrollment lower than expected** | MEDIUM | HIGH | Offer device-included model (clinic provides devices to patients at no cost -- devices paid by VIPC grant). Start with highest-risk patients who benefit most. Have clinic champion (MA or nurse) lead enrollment |
| **ML model performance below threshold** | MEDIUM | LOW | Fall back to rule-based risk scoring (validated clinical risk scores like LACE index). ML model is enhancement, not dependency |
| **HIPAA breach during pilot** | HIGH | LOW | Shield encryption from Day 1. BAAs with all vendors. Minimize PHI in development/testing environments (use synthetic data). Incident response plan documented before pilot launch |
| **FDA classifies risk model as SaMD** | MEDIUM | LOW | Position as clinical decision support (provider reviews and acts on all outputs). Document intended use per 21st Century Cures Act exemption criteria. Consult regulatory counsel if needed |
| **Salesforce platform changes/price increases** | MEDIUM | MEDIUM | Build with standard Salesforce APIs and metadata (avoid deep platform coupling). Maintain architecture flexibility for future platform migration if needed |
| **Contract developer unavailable or underperforms** | HIGH | MEDIUM | Begin recruiting immediately upon grant award. Have backup candidates identified. Will can cover gap temporarily for simpler configuration work |

---

## 12. IMMEDIATE NEXT STEPS (Post-Grant Award)

| Action | Owner | Deadline | Dependency |
|---|---|---|---|
| Register as Salesforce ISV Partner | Will | Week 1 | None |
| Apply for Salesforce Startup Program discount | Will | Week 1 | None |
| Provision Salesforce Health Cloud dev environment | Will | Week 1 | ISV registration |
| Execute GCP BAA for HIPAA workloads | Will | Week 1 | None |
| Post contract Salesforce developer job listing | Will + Jim | Week 1 | None |
| Identify and contact 5--10 candidate pilot RHCs in Virginia | Jim + Mandy | Week 1--2 | None |
| Execute HIPAA BAA with Salesforce | Will | Week 1 | SF provisioning |
| Reach out to RPM device vendors (Omron, Withings) for partnership | Will + Jim | Week 2 | None |
| Complete HIPAA Security Rule risk assessment | Will + Cari Ann | Week 2--3 | None |
| Select and onboard pilot clinic (first) | Jim | Week 3--4 | Clinic outreach |
| Begin Sprint 1 development | Will + Contract Dev | Week 2 | SF environment ready |
| Contact Virginia Rural Health Association for introductions | Jim + Mandy | Week 2 | None |

---

*Prepared by: Veteran Vectors Engineering | Authentic Consortium*
*This is a living document -- updated as implementation progresses*
