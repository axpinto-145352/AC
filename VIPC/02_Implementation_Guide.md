# 3C PLATFORM -- IMPLEMENTATION GUIDE

**Version:** 3.0 | **Classification:** Internal -- Authentic Consortium
**Prepared by:** Veteran Vectors (VV) Engineering
**Date:** February 25, 2026
**Purpose:** Actionable build plan for the 3C Platform assuming VIPC VVP Launch Grant award ($50K)

---

## 1. EXECUTIVE SUMMARY

This is the engineering and business execution plan for the **3C Platform** -- a unified solution for Rural Health Clinics (RHCs) addressing **Compliance**, **Care**, and **Collect Cash**. The platform is built on VV's proven stack: **n8n** (workflow automation), **PostgreSQL 16** (database), **Python/FastAPI** (API/ML), **React/Next.js** (frontend), and **Docker containers** on **Amazon GovCloud**. This is the same architecture VV deploys for defense clients, adapted for healthcare.

**Key architecture decision:** No enterprise SaaS dependencies. **All intellectual property is owned by Authentic Consortium (ACT).** VV develops the platform under ACT's direction via a work-for-hire arrangement. The $50K VIPC grant funds infrastructure and operations -- not licensing fees or contract developers. VV's technical lead builds and maintains the system. The modular architecture supports three service tiers (Essentials, Professional, Enterprise) so clinics pay only for the modules they need.

**Scope:** $50K VIPC grant funds Phase 1 (MVP). Subsequent phases funded by pilot revenue and Series A.

---

## 2. TECHNICAL ARCHITECTURE

### 2.1 Platform Stack

| Layer | Technology | Purpose | Cost Model |
|---|---|---|---|
| **Hosting** | Amazon GovCloud (ECS Fargate + RDS + S3) | FedRAMP High, HIPAA BAA, ITAR-compliant infrastructure | Pay-as-you-go (~$750/month at pilot scale) |
| **Workflow Engine** | n8n (self-hosted, Community Edition) | EHR integration, RPM ingestion orchestration, billing automation, compliance workflows, alert routing | Free (open-source) |
| **Database** | PostgreSQL 16 (Amazon RDS Multi-AZ) | Central data store. Row-level security for multi-tenant clinic isolation. PGAudit for HIPAA audit trail | Included in GovCloud hosting |
| **API / ML** | Python 3.11 + FastAPI | ML model serving (risk stratification), high-frequency RPM data ingestion, FHIR data transforms | Free (open-source) |
| **Frontend** | React / Next.js | Clinic dashboard: Patient 360, compliance tracker, billing tracker, MIPS dashboard, RPM data display | Free (open-source) |
| **Reverse Proxy** | NGINX | TLS 1.2+ termination, HSTS, CSP headers, rate limiting | Free (open-source) |
| **FHIR Integration** | bonFHIR n8n node (@bonfhir/n8n-nodes-bonfhir) + direct FHIR R4 HTTP calls | Native FHIR R4 actions and triggers for EHR connectivity | Free (Apache 2.0 license) |
| **Containers** | Docker + ECS Fargate | Containerized deployment. Same delivery model as VV defense deployments | Included in GovCloud hosting |
| **Security** | AWS KMS + PGAudit + CloudTrail + application-level field encryption | AES-256 at rest, TLS 1.2+ in transit, HIPAA audit logging, PHI field encryption | KMS: ~$1/key/month; rest included |
| **Monitoring** | CloudWatch + CloudWatch Logs | Application performance, error tracking, HIPAA log archival | Included in GovCloud |
| **DevOps** | GitHub (private repos) + GitHub Actions CI/CD | Source control, automated testing, container builds | GitHub Team: $4/user/month |

### 2.2 Phase 1 MVP Architecture

```
+------------------------------------------------------------------+
|              PHASE 1 MVP (Amazon GovCloud, $50K Budget)           |
|                                                                   |
|  +---------------------------+  +------------------------------+  |
|  | React/Next.js Frontend    |  | Python/FastAPI Services       |  |
|  | (ECS Fargate)             |  | (ECS Fargate)                |  |
|  |                           |  |                              |  |
|  | - Patient 360 dashboard   |  | - Risk stratification model  |  |
|  | - Compliance tracker      |  |   (XGBoost + SHAP)           |  |
|  | - RPM data display        |  | - RPM data ingestion service |  |
|  | - Billing tracker         |  |   (polls device vendor APIs) |  |
|  | - MIPS quality dashboard  |  | - FHIR data transforms       |  |
|  | - Care gap alerts         |  |   (device → Observation)     |  |
|  +------------+--------------+  +--------------+---------------+  |
|               |                                |                  |
|  +------------+--------------------------------+---------------+  |
|  |                    n8n (ECS Fargate)                         |  |
|  |                                                             |  |
|  |  - EHR FHIR integration (bonFHIR node)                     |  |
|  |  - RPM threshold monitoring + alert routing                 |  |
|  |  - Billing event generation (16-day, 20-min triggers)      |  |
|  |  - Compliance task scheduling + reminders                   |  |
|  |  - Care gap detection (scheduled)                          |  |
|  |  - Notification pipelines (email/SMS)                      |  |
|  +-----+------------------+------------------+----------------+  |
|        |                  |                  |                    |
|  +-----+------+  +-------+-------+  +-------+----------------+  |
|  | PostgreSQL |  | EHR (FHIR R4) |  | RPM Device APIs        |  |
|  | 16 (RDS)   |  | (1 system:    |  | (Tenovi or Smart Meter |  |
|  | + PGAudit  |  |  eCW/athena/  |  |  cellular devices)     |  |
|  | + RLS      |  |  Azalea)      |  |                        |  |
|  +------------+  +---------------+  +------------------------+  |
+------------------------------------------------------------------+
```

**Key MVP decisions:**
- **Hybrid ingestion pattern.** Python/FastAPI service handles high-frequency RPM device data polling (Tenovi/Smart Meter APIs). n8n handles workflow orchestration on top -- alert routing when thresholds are exceeded, billing event generation, care gap detection. This split is based on production architecture research: n8n excels at workflow orchestration but dedicated services are more robust for high-frequency data ingestion
- **n8n Community Edition is sufficient for Phase 1.** Throughput: ~15--23 req/s single mode depending on instance size (n8n benchmarks show ~15 req/s stable on smaller instances; ~23 req/s on larger instances with elevated failure rates). Our load: ~1--5 req/s at peak with 2--3 clinics -- well within single-mode capacity. Queue mode (available in Community Edition with Redis) is a Phase 2 upgrade path when scaling to 10+ clinics. n8n Enterprise adds multi-main HA and worker monitoring UI if needed
- **bonFHIR for FHIR integration.** Purpose-built n8n community node (Apache 2.0) providing native FHIR R4 actions and triggers. Chosen specifically because it was designed for self-hosted HIPAA-compliant n8n deployments
- **PostgreSQL row-level security for multi-tenancy.** Each clinic is a tenant. RLS policies enforce data isolation at the database level -- not just application code. PGAudit logs every query against PHI tables. This pattern is validated by AWS reference architectures and HIPAA compliance guidance
- **n8n Community Edition HIPAA access control gap.** Community Edition lacks SSO/LDAP and RBAC (Enterprise-only features). Phase 1 mitigation: restrict n8n UI access to VV engineering team only via VPN + NGINX IP allowlisting. All clinic staff interact exclusively through the React frontend, which implements application-level RBAC. n8n processes PHI in workflows but no clinic user directly accesses the n8n interface. Phase 2: evaluate n8n Enterprise or implement external auth proxy (e.g., OAuth2 Proxy) in front of n8n
- **Application-level field encryption for sensitive PHI.** AES-256 via AWS KMS envelope encryption on SSN, diagnosis codes, treatment notes. Provides breach safe harbor under HIPAA Breach Notification Rule -- encrypted data is "unreadable, unusable, and indecipherable". Performance note: encrypted fields cannot be used in PostgreSQL WHERE clauses without decryption; design queries to filter by non-encrypted fields (patient_id, clinic_id, date ranges) first, then decrypt at the application layer

### 2.3 EHR Integration Strategy

**Target EHR systems for RHC market:**

| EHR | RHC Relevance | FHIR R4 Support | Integration Approach |
|---|---|---|---|
| **eClinicalWorks** | Largest cloud ambulatory install base, strong in FQHCs and primary care | Yes (ONC-certified) | bonFHIR node + eCW FHIR API; SMART on FHIR Backend Services auth |
| **athenahealth** | Best in KLAS 2025 for independent practices; developer-friendly APIs | Yes (ONC-certified) | bonFHIR node + athenahealth FHIR API; integrated RCM data |
| **MEDITECH Expanse** | Dominant in rural/community hospitals; 29 of Becker's "2025 Great Community Hospitals" use MEDITECH | Yes | FHIR endpoints via HTTP Request node; may need HL7v2 bridge for older installs |
| **Azalea Health** | Purpose-built for RHCs; native RHC billing (UB04/CMS1500); HITRUST E1 certified | Yes (ONC-certified) | bonFHIR node + Azalea FHIR API; ideal if pilot clinics use Azalea |
| **TruBridge/CPSI** | Specifically for rural/community hospitals | Partial | May need HL7v2 interface for older versions; FHIR for Evident Thrive |

**Phase 1:** Integrate with **1 EHR system** (whichever the pilot clinic uses). Prioritize eCW or athenahealth (best FHIR support + developer programs). Azalea is ideal if available.

**FHIR Implementation Guides:**
- US Core (v8.0.1 / STU8) -- mandatory baseline
- SMART on FHIR (Backend Services flow for system-to-system auth -- n8n handles OAuth 2.0 via generic credential config)
- Bulk FHIR (panel-level data extraction)
- DaVinci DEQM (quality measure reporting) -- Phase 2
- DaVinci CRD/PAS (prior auth support) -- Phase 2

**SMART on FHIR auth in n8n:** n8n supports generic OAuth 2.0 credentials. For Backend Services (system-to-system, no user in the loop): use a Code node to sign JWT with private key and exchange for access token. For Standalone Launch: use n8n's built-in OAuth 2.0 credential type with EHR's authorization/token endpoints and SMART scopes.

### 2.4 RPM Device Integration

**Cellular-connected devices are mandatory for rural patients.** Most lack reliable WiFi or smartphones.

| Device Type | Recommended Device | Approx. Cost/Unit | Integration |
|---|---|---|---|
| **Blood Pressure Cuff** | Smart Meter iBloodPressure (cellular) or Omron VitalSight via Tenovi | $80--$150 | Python ingestion service → PostgreSQL |
| **Pulse Oximeter** | Smart Meter iPulseOx (cellular) or Nonin 3230 via Tenovi | $100--$300 | Python ingestion service → PostgreSQL |
| **Glucose Monitor** | Smart Meter iGlucose Plus (cellular) or Dexcom Stelo OTC CGM | $70--$150/month | Python ingestion service → PostgreSQL |
| **Weight Scale** | Smart Meter iScale (cellular) or BodyTrace e-Scale | $50--$120 | Python ingestion service → PostgreSQL |

**Recommended Phase 1 approach:** Partner with **Tenovi** (40+ FDA-cleared devices, single API, cellular gateway) or go direct with **Smart Meter** (proprietary cellular devices, zero patient setup).

**Data flow:**
```
Patient device (cellular) → Device vendor cloud (Smart Meter / Tenovi)
                                            |
                           Python ingestion service (ECS Fargate)
                           - Polls vendor API on interval
                           - Validates + normalizes readings
                           - Writes to PostgreSQL (RPM_Reading table)
                                            |
                                   n8n workflow triggered
                           - Checks thresholds (BP>180, SpO2<90, etc.)
                           - If exceeded: create alert, notify provider
                           - Nightly: count transmission days per patient
                           - If ≥16 days: flag billable for CPT 99454
```

### 2.5 Modular Service Tiers

The 3C Platform is architected as **independent, composable modules** controlled by per-clinic configuration flags. This enables ACT to serve clinics of all sizes -- from a 200-patient solo-provider RHC that only needs compliance tracking, to a 2,000-patient FQHC running full RPM/CCM/billing programs.

| Tier | Modules | Target Clinic | Price |
|---|---|---|---|
| **Essentials** | Compliance only (HIPAA tracker, risk assessment, CMS quality dashboard) | Small RHCs (<500 patients) | $500--$1,000/mo |
| **Professional** | Compliance + Care (adds RPM integration, AI risk stratification, care gaps, deterioration alerts) | Mid-size RHCs (500--1,500 patients) | $1,500--$2,500/mo |
| **Enterprise** | All 3C modules: Compliance + Care + Collect Cash (adds billing automation, MIPS optimization, coding, denial prevention) | Larger RHCs and FQHCs (1,500+ patients) | $2,500--$4,000/mo |

**Technical implementation:**
- `clinic_config` table stores module activation flags per clinic: `modules_enabled JSONB DEFAULT '["compliance"]'`
- n8n workflow templates are grouped by module -- only active module workflows execute for each clinic
- React dashboard conditionally renders module panels based on `modules_enabled`
- Python/FastAPI services check module entitlement before processing (e.g., ML risk scoring only runs for clinics with "care" module active)
- Upgrading a clinic tier = updating `modules_enabled` + deploying pre-built workflow templates. No custom code required

**Why modular matters:**
- **Lower barrier to entry:** Clinics can start with Essentials ($500/mo) and upgrade as they see ROI
- **Broader addressable market:** Not every RHC can justify $2K+/month. The Essentials tier captures small clinics that competitors miss
- **Net revenue expansion:** Clinics that start on Essentials naturally upgrade as they discover compliance savings and want care/billing capabilities (land-and-expand)
- **Simpler sales motion:** "Start with what you need, add modules when you're ready"

---

## 3. MODULE BUILD SPECIFICATIONS

### 3.1 Compliance Module

| Feature | Implementation | Custom Development | Phase |
|---|---|---|---|
| **HIPAA Compliance Tracker** | PostgreSQL table: `compliance_tasks` (clinic_id, task_type, due_date, assignee, status, evidence_url). n8n scheduled workflow for reminders and escalation | React UI for task management | Phase 1 |
| **HIPAA Risk Assessment** | Pre-built assessment questionnaire (React form) mapped to NIST SP 800-66 controls. Auto-scores risk level and generates PDF report | Python report generator | Phase 1 |
| **HRSA UDS Report Generation** | n8n workflows pulling patient, encounter, diagnosis, demographics data via FHIR. Pre-built reports matching UDS table structure. **Note:** UDS is mandatory for FQHCs, not standalone RHCs, but positions all clinics for value-based care | Python data aggregation + report export | Phase 2 |
| **CMS Quality Dashboard** | React dashboard tracking MIPS measures: Quality (30%), Cost (30%), PI (25%), IA (15%). Real-time score projection | Python scheduled job calculating measure numerators/denominators | Phase 1 (basic), Phase 2 (full) |
| **Regulatory Change Alerts** | n8n scheduled workflow polling Federal Register API + CMS/HRSA RSS feeds. Python NLP classifier for relevance filtering | Python NLP service (spaCy) | Phase 3 |

### 3.2 Care Module

| Feature | Implementation | Custom Development | Phase |
|---|---|---|---|
| **Patient Risk Stratification** | XGBoost model trained on CMS Public Use Files. Features: age, HCC risk score, diagnosis count, utilization history, medication count, SVI. Output: risk score (0--100) + tier + top 3 SHAP factors | FastAPI model server on ECS Fargate; called by n8n for batch scoring or React for on-demand | Phase 1 |
| **RPM Data Ingestion** | PostgreSQL table: `rpm_readings` (clinic_id, patient_id, device_type, value, reading_date, device_id, transmission_flag). Python ingestion service on ECS Fargate polls vendor APIs | Python ingestion service + n8n threshold monitoring | Phase 1 |
| **Deterioration Alerts** | n8n workflow triggered on new RPM readings. Evaluates threshold rules (BP >180, SpO2 <90, weight gain >3 lbs/day). Creates alert task, sends provider notification | Phase 1: rule-based. Phase 2: ML trend analysis (sliding-window anomaly detection) | Phase 1 |
| **Care Gap Detection** | n8n scheduled workflow comparing patient records against USPSTF/CMS preventive care guidelines. Generates care gap records for overdue screenings, immunizations, AWVs | Python guideline rules engine | Phase 1 |
| **Care Plan Management** | PostgreSQL tables for care plan templates (diabetes, hypertension, COPD, CHF, depression). React UI for plan assignment and progress tracking | React care plan UI | Phase 1 |
| **Telehealth Integration** | n8n integration with Zoom for Healthcare or Doxy.me via API. Embedded video link in patient record | React embedded widget + n8n scheduling workflow | Phase 2 |

**ML Model Specification (Risk Stratification):**

| Parameter | Value |
|---|---|
| **Algorithm** | XGBoost (gradient-boosted trees); logistic regression baseline for comparison |
| **Training Data** | CMS Medicare Public Use Files (100% sample claims data), CMS Chronic Conditions Data Warehouse, MIMIC-IV (if needed) |
| **Features** | Age, sex, HCC risk score, diagnosis count (ICD-10 categories), medication count, ED visits (12 mo), inpatient admits (12 mo), primary care visits (12 mo), days since last visit, social vulnerability index (SVI) |
| **Target** | Binary: hospitalization or ED visit within 90 days |
| **Output** | Risk score (0--100) + tier (Low/Medium/High/Critical) + top 3 contributing factors (SHAP values) |
| **Performance Target** | AUC-ROC >0.75; sensitivity >80% for top-decile risk patients |
| **Framework** | scikit-learn + XGBoost; model serialized with joblib; served via FastAPI on ECS Fargate |
| **Retraining** | Quarterly with updated claims data; triggered if AUC drops below 0.72 |
| **Interpretability** | SHAP (SHapley Additive exPlanations) for per-patient feature importance |

### 3.3 Collect Cash Module

| Feature | Implementation | Custom Development | Phase |
|---|---|---|---|
| **RPM Billing Tracker** | PostgreSQL table: `billing_events` (clinic_id, patient_id, cpt_code, service_date, status). n8n nightly workflow: count transmission days per patient → flag billable when ≥16 days (99454) or ≥2 days (99445 new 2026 code). Track clinician time for 99457/99458/99470 | n8n workflows + React billing dashboard | Phase 1 |
| **CCM Time Tracking** | PostgreSQL table: `ccm_activities` (patient_id, clinician_id, activity_type, duration_minutes, date). React timer component for real-time capture. n8n workflow: when cumulative minutes ≥20, flag for 99490 ($66.30). Track complex CCM (60 min) for 99487 (~$144.29) | React timer component + n8n billing logic | Phase 1 |
| **Patient Consent Capture** | React consent form (clinical + Medicare RPM consent). Digital signature capture. Stored in PostgreSQL with audit trail. Required before RPM billing | React consent form UI | Phase 1 |
| **TCM Workflow** | n8n workflow triggered on discharge notification (ADT feed via FHIR or HL7v2). Auto-creates tasks: contact within 2 days, med reconciliation, visit within 7/14 days. Tracks for 99495/99496 | n8n workflow + hospital ADT integration | Phase 2 |
| **Coding Optimization** | NLP analysis of clinical notes for missed HCC codes | Python NLP (spaCy + MedCAT) via FastAPI | Phase 2 |
| **Denial Prevention** | Rules engine checking claims against payer denial patterns before submission | Python rules engine + clearinghouse integration (Office Ally first) | Phase 3 |
| **MIPS Payment Projection** | React dashboard modeling projected MIPS payment adjustment. Shows gap to avoid -9% penalty | Python scoring engine using CMS MIPS methodology | Phase 1 (basic), Phase 2 (full) |

**CMS Reimbursement Reference (2026 Rates):**

| CPT Code | Service | 2026 Rate | Billing Threshold |
|---|---|---|---|
| 99453 | RPM device setup (one-time) | $22.00 | Initial setup + patient education; requires minimum 2 days of monitoring data (2026 rule change -- reduced from prior 16-day requirement) |
| 99454 | RPM device supply/data (monthly) | $52.11 | 16+ days of data transmission |
| 99445 | RPM device supply/data (2--15 days) -- NEW 2026 | ~$52.11 | 2--15 days of data transmission (mutually exclusive with 99454; bill one per 30-day period) |
| 99457 | RPM first 20 min interactive (monthly) | $51.77 | 20 min clinician time |
| 99458 | RPM additional 20 min | ~$41.52 | Each additional 20 min beyond 99457 |
| 99470 | RPM first 10 min interactive -- NEW 2026 | ~$26.05 | 10--19 min clinician time (mutually exclusive with 99457; bill one per calendar month) |
| 99490 | CCM first 20 min (monthly) | $66.30 | 20 min staff time, 2+ chronic conditions |
| 99439 | CCM additional 20 min (up to 2x/month) | $50.56 | Each additional 20 min |
| 99487 | Complex CCM first 60 min (monthly) | ~$144.29 | 60 min staff time, complex needs |
| 99489 | Complex CCM additional 30 min | ~$78.16 | Each additional 30 min |
| 99495 | TCM moderate complexity | $220.00 | Contact within 2 days, visit within 14 days |
| 99496 | TCM high complexity | $298.00 | Contact within 2 days, visit within 7 days |

**Revenue unlock per clinic (target estimate, assumes mature program):**
Assume 800 Medicare patients, 25% chronic disease prevalence (200 eligible), 40% enrolled RPM (80 patients), 60% enrolled CCM (120 patients):

| Revenue Stream | Patients | Monthly/Patient | Annual Revenue |
|---|---|---|---|
| RPM (99454 + 99457) | 80 | $103.88 | $99,725 |
| CCM (99490) | 120 | $66.30 | $95,472 |
| MIPS penalty avoidance (-9% on Medicare) | -- | -- | $36,000--$72,000 |
| **Total new annual revenue per clinic** | | | **$195,000--$267,000** |

---

## 4. DATABASE SCHEMA (Phase 1)

### 4.1 Multi-Tenant Architecture

**Pattern:** Shared database, shared schema, PostgreSQL row-level security (RLS).

Every table with PHI includes a `clinic_id` column. RLS policies enforce that each clinic can only see its own data. This is the same pattern VV uses for the BVG defense platform.

```sql
-- Enable RLS on all PHI tables
ALTER TABLE patients ENABLE ROW LEVEL SECURITY;
CREATE POLICY clinic_isolation ON patients
  USING (clinic_id = current_setting('app.current_clinic')::int);

-- Set clinic context at connection level (not per-query)
SET app.current_clinic = '42';
```

**Why RLS over schema-per-tenant:** O(1) migrations (single schema), simpler connection pooling, scales to hundreds of tenants. HIPAA auditors require demonstrable isolation, not a specific mechanism. RLS + PGAudit provides both isolation and audit proof.

**Security note:** The application database role used by FastAPI/n8n must NOT have superuser or BYPASSRLS privileges. The RDS master user (which bypasses RLS) must be secured separately and never used for application connections. RLS policies do not apply to table owners by default -- use `ALTER TABLE ... FORCE ROW LEVEL SECURITY` if the application role owns PHI tables, or ensure PHI tables are owned by a separate administrative role.

### 4.2 Core Tables

```
clinics              -- tenant: clinic info, settings, EHR config
users                -- staff accounts, roles, clinic_id
patients             -- demographics, insurance, clinic_id
encounters           -- visit records, linked to patients
rpm_readings         -- device data: type, value, date, device_id, clinic_id
billing_events       -- CPT code, patient, status, service date, clinic_id
compliance_tasks     -- HIPAA/regulatory tasks, due dates, clinic_id
care_gaps            -- overdue screenings/immunizations, clinic_id
care_plans           -- care plan assignments, templates, clinic_id
risk_scores          -- ML model output, SHAP values, clinic_id
ccm_activities       -- clinician time tracking for CCM billing, clinic_id
audit_trail          -- application-level PHI access log (who, what, when)
```

### 4.3 Testing Strategy

| Level | Approach | Target |
|---|---|---|
| **Unit tests** | pytest for Python services, Jest for React components | 80%+ code coverage |
| **Integration tests** | FHIR endpoint integration tests against EHR sandbox, RPM API integration tests against vendor sandbox | All integration paths tested |
| **RLS isolation tests** | Automated tests verifying cross-tenant data leakage is impossible | Run in CI pipeline on every deploy |
| **UAT** | Pilot clinic staff test workflows with real (de-identified) data | Clinic sign-off before go-live |
| **Load testing** | Simulate 500 RPM readings/hour, 50 concurrent dashboard users | Verify <2s response time |

---

## 5. DEVELOPMENT ROADMAP

### Phase 1: MVP (Months 1--4, $50K VIPC Grant)

**Goal:** Working 3C Platform at 2--3 Virginia RHCs. MVP delivers all three tiers so pilot clinics can validate the full modular model.

**MVP = Essentials tier fully functional + Professional tier core features + Enterprise tier billing basics.** This means every pilot clinic can demonstrate the full compliance→care→revenue flywheel, while the modular architecture proves that smaller clinics could subscribe to just Essentials.

| Month | Sprint | Deliverables | Tier Unlocked |
|---|---|---|---|
| **Month 1** | Sprint 1--2 | **Foundation + Essentials Tier:** GovCloud environment provisioned (ECS Fargate, RDS PostgreSQL, S3, KMS). Database schema deployed with RLS + `clinic_config` module flags. NGINX + TLS configured. React scaffold with auth (Keycloak or custom JWT). Patient import from pilot clinic (CSV or FHIR bulk). **HIPAA compliance tracker live.** CMS quality dashboard (basic). Care plan templates for diabetes, hypertension, CHF. **Engage patent attorney for provisional patent applications** | **Essentials: shippable** |
| **Month 2** | Sprint 3--4 | **Professional Tier:** EHR FHIR integration with pilot clinic EHR (bonFHIR node in n8n, Backend Services auth). RPM device integration (Python ingestion service + 1--2 device types via Tenovi/Smart Meter). RPM data flowing into PostgreSQL + displayed in dashboard. Alert rules configured. Care gap detection for top 6 preventive measures. Risk stratification model v1 trained and deployed (FastAPI on Fargate). **File provisional patent applications (unified architecture + billing pipeline)** | **Professional: shippable** |
| **Month 3** | Sprint 5--6 | **Enterprise Tier:** RPM billing tracker live (n8n auto-flagging 99453/99454/99445/99457 thresholds). CCM time tracking (React timer + n8n billing logic). MIPS quality measure dashboard (basic, 3--5 measures). Patient consent capture workflow. End-to-end testing with pilot clinic staff | **Enterprise: shippable** |
| **Month 4** | Sprint 7--8 | **Pilot Launch:** 2--3 Virginia RHCs live (at least 1 on each tier to validate tiering model). Staff training completed. Baseline metrics captured. Bug fixes and UX refinements. Pilot outcomes report for Series A / next funding round | **All 3 tiers validated** |

### Phase 2: Full Product (Months 5--10, funded by pilot revenue + seed)

**Goal:** Harden all three tiers. Expand to 10+ clinics. Validate land-and-expand motion (clinics upgrading from Essentials → Professional → Enterprise).

| Month | Deliverables | Tier Enhancement |
|---|---|---|
| **5--6** | Additional EHR integrations (2--3 more systems via n8n + bonFHIR). n8n Enterprise upgrade for queue mode (scale to 10+ clinics). HRSA UDS report automation. Full MIPS dashboard (all 4 categories). Telehealth integration (Zoom/Doxy.me via n8n). **Convert provisional patent(s) to full utility applications** | Professional + Enterprise enriched |
| **7--8** | NLP coding optimization (spaCy + MedCAT via FastAPI). TCM workflow (ADT feed integration). Denial prevention rules engine. ML deterioration prediction (replaces rule-based alerts). Additional RPM devices (3--5 types total) | Enterprise features completed |
| **9--10** | 10+ Virginia RHCs live (target mix: 3--4 Essentials, 4--5 Professional, 2--3 Enterprise). Regulatory change monitoring (Federal Register NLP). **Automated clinic onboarding workflow** (new clinic deploys from template in <1 day). Performance benchmarking and case study publication. Track tier upgrade conversions | All tiers production-hardened |

### Phase 3: Scale (Months 11--18, funded by Series A)

**Goal:** National expansion. Automated onboarding. 100+ clinics across all tiers.

| Month | Deliverables | Scale Target |
|---|---|---|
| **11--13** | Multi-region GovCloud deployment for HA/DR. Automated provisioning (new clinic live in hours, any tier). Self-service tier upgrade in dashboard. 50+ Virginia RHCs | 50+ clinics, majority on Professional/Enterprise |
| **14--16** | National expansion (WV, KY, TN, NC -- high RHC density). Advanced AI (population health analytics, predictive staffing). Clearinghouse direct integration (Availity, Change Healthcare). **File additional patents as platform evolves** | Multi-state presence |
| **17--18** | 100+ RHCs nationally. Series A close based on ARR + clinical outcomes. SOC 2 Type II audit. HITRUST certification pathway. Potential FQHC-specific tier (adds UDS reporting, HRSA compliance) | 100+ clinics, $1M+ ARR target |

---

## 6. TEAM & BUDGET

### 6.1 Phase 1 Team (Months 1--4)

| Role | Who | Commitment | Cost |
|---|---|---|---|
| **Technical Lead / Full-Stack Developer** | VV Technical Lead | 40 hrs/week | Sweat equity |
| **ML Engineering** | VV Technical Lead | Included above | Sweat equity |
| **Clinical Advisor / SME** | Cari Ann (ACT) + pilot clinic provider | 5 hrs/week | ACT sweat equity |
| **Project Manager / Business Development** | Jim Pfautz (ACT CEO) | 10 hrs/week | ACT sweat equity |
| **Compliance / Preventive Health** | Jessica (ACT) | 5 hrs/week | ACT sweat equity |

### 6.2 Phase 1 Budget ($50K VIPC Grant)

| Item | Cost | Notes |
|---|---|---|
| AWS GovCloud (ECS Fargate + RDS PostgreSQL Multi-AZ + S3 + KMS, 4 months) | $3,000 | ~$750/month at pilot scale |
| RPM devices for pilot (15--20 units, cellular-connected) | $2,500 | Tenovi or Smart Meter; assumes pilot pricing |
| Pilot clinic onboarding (travel, training, materials) | $4,500 | 2--3 clinics in Virginia |
| ML model training compute (GovCloud GPU instances) | $1,500 | Training runs for risk stratification model |
| Legal (HIPAA BAA templates, pilot agreements, consent forms) | $3,000 | Healthcare IT attorney |
| EHR developer program access + FHIR sandbox fees | $500 | athenahealth / eCW / Azalea developer programs |
| Domain, SSL (ACM), email (SES), monitoring | $1,000 | Annual domain + minimal SES + CloudWatch |
| **Contingency / additional pilots** | **$34,000** | 68% of grant available for expansion or unexpected costs |
| **VIPC Grant Total** | **$50,000** | |
| VV Technical Lead (640 hrs @ $150/hr) | -- | ~$96,000 in-kind |
| Cari Ann (Clinical Advisory, 80 hrs @ $150/hr) | -- | ~$12,000 in-kind |
| Jim (Project Management, 160 hrs @ $150/hr) | -- | ~$24,000 in-kind |
| Jessica (Compliance/Health, 80 hrs @ $150/hr) | -- | ~$12,000 in-kind |
| **Total In-Kind** | -- | **~$144,000** |
| **Total Project Value (Phase 1)** | **$50,000 cash + ~$144,000 in-kind = ~$194,000** |

**Why 68% contingency?** VV's technical lead builds the platform -- no contract developer cost ($25K--$30K saved). No enterprise licensing ($8,450+ saved). The technology stack is free. The $50K funds operations and infrastructure. The large contingency gives ACT optionality: add pilot clinics, hire specialized help if needed, or absorb EHR integration surprises.

### 6.3 Infrastructure Costs at Scale

| Scale | Monthly Infra | Annual Infra |
|---|---|---|
| Phase 1 (2--3 clinics, ~200 patients) | ~$750 | ~$9,000 |
| Phase 2 (10 clinics, ~2,000 patients) | ~$2,000--$3,000 | ~$24,000--$36,000 |
| Phase 3 (50 clinics, ~10,000 patients) | ~$5,000--$8,000 | ~$60,000--$96,000 |
| 100 clinics, ~20,000 patients | ~$10,000--$15,000 | ~$120,000--$180,000 |

**Per-clinic COGS at 100 clinics: ~$100--$150/month** (vs ~$650/month for Salesforce licenses alone).

### 6.4 Phase 2--3 Cost Summary

| Phase | Timeline | Cash Cost | In-Kind | Total Value |
|---|---|---|---|---|
| **Phase 1 (MVP)** | Months 1--4 | $50,000 | ~$144,000 | ~$194,000 |
| **Phase 2 (Full Product)** | Months 5--10 | ~$250,000--$350,000 | ~$150,000 | ~$400,000--$500,000 |
| **Phase 3 (Scale)** | Months 11--18 | ~$500,000--$700,000 | ~$100,000 | ~$600,000--$800,000 |

---

## 7. PARTNER DEPENDENCIES

### 7.1 Required Partners (Phase 1)

| Partner | Why Needed | Candidates | Deadline |
|---|---|---|---|
| **Pilot RHCs (2--3 clinics)** | Live environment to deploy, test, demonstrate. Must have Medicare panel + chronic disease population | Virginia RHCs via Virginia Rural Health Association or HRSA database. Target clinics on eCW/athena/Azalea | **Month 1** |
| **RPM Device Vendor** | Device supply for pilot patients, API access. Cellular required for rural | **Tenovi** (40+ devices, single API, cellular gateway) or **Smart Meter** (proprietary cellular, zero patient setup) | **Month 2** |
| **HIPAA/Compliance Counsel** | BAA review, HIPAA policies, consent form templates | Healthcare IT law firm (Virginia-based) | **Month 1** |

### 7.2 Required Partners (Phase 2--3)

| Partner | Why Needed | Candidates | Timeline |
|---|---|---|---|
| **Clearinghouse** | Claims submission, eligibility verification | **Office Ally** (free for claim submission, easiest setup). Availity (free for payer-sponsored eligibility) | Phase 2 |
| **Billing/Coding Experts** | Validate coding logic, training data for NLP | Local medical billing company or AAPC-certified coders | Phase 2 |

### 7.3 Strategic Relationships

| Entity | Value |
|---|---|
| **Virginia Rural Health Association** | Clinic introductions, market validation, policy advocacy |
| **HRSA / Federal Office of Rural Health Policy** | Grant opportunities, regulatory guidance, credibility |
| **University Partners (UVA, VT, VCU)** | Health informatics talent, clinical research, IRB for outcomes studies |

---

## 8. COMPLIANCE & SECURITY

### 8.1 HIPAA Compliance (Day 1)

| Requirement | Implementation |
|---|---|
| **BAAs** | Execute with: AWS (standard GovCloud BAA via AWS Artifact), RPM device vendor, EHR vendor (if applicable), any subcontractor with PHI access. **Must be in place before any patient data** |
| **Encryption at Rest** | RDS encryption via AWS KMS (customer-managed key, AES-256). S3 SSE-KMS. Application-level field encryption for SSN, diagnosis codes, treatment notes (AES-256 via KMS envelope encryption) |
| **Encryption in Transit** | TLS 1.2+ enforced by NGINX and ALB. All API calls HTTPS only. FHIR endpoints authenticated via OAuth 2.0 / SMART on FHIR. RDS SSL enforced (`rds.force_ssl = 1`) |
| **Access Control** | PostgreSQL RLS for clinic isolation. Application-level RBAC: clinic admin, provider, care coordinator, VV admin. Keycloak or custom JWT auth |
| **Audit Logging** | Three layers: (1) CloudTrail for AWS infrastructure, (2) PGAudit for database queries on PHI tables, (3) application-level `audit_trail` table (who viewed/modified which patient record, when, from where). CloudWatch Logs for real-time monitoring. Archive to S3 Glacier for 6+ year retention |
| **Workforce Training** | All team members with PHI access complete HIPAA training before pilot. Annual refresher |
| **Incident Response** | Documented breach response per 45 CFR 164.400--414. All breaches: individual notification within 60 days. 500+ individuals: HHS + media within 60 days. <500: HHS annual report |
| **Risk Assessment** | HIPAA Security Rule risk assessment (NIST SP 800-66) completed before pilot launch |

### 8.2 Regulatory

| Requirement | Notes |
|---|---|
| **FDA SaMD** | Risk stratification qualifies for CDS exemption under 21st Century Cures Act Section 3060(a) / FD&C Act 520(o) -- meets all four criteria. January 2026 FDA guidance broadens enforcement discretion. Maintain regulatory file documenting intended use and compliance with all four criteria |
| **CMS Conditions of Participation** | All auto-generated billing events validated against actual clinical documentation. No false claims |
| **42 CFR Part 2** | If any pilot clinic treats substance use disorders, additional consent and segmentation requirements apply |
| **VCDPA** | Health data exemptions exist for HIPAA-covered data; verify for any non-PHI patient data |

---

## 9. INTELLECTUAL PROPERTY STRATEGY

### 9.1 IP Ownership

**All 3C Platform intellectual property is owned by Authentic Consortium (ACT).** VV develops the platform under a work-for-hire arrangement with ACT. This structure ensures:

- ACT controls all IP for licensing, fundraising, and exit purposes
- VV operates as the contracted technical development arm
- IP assignment is documented in the VV-ACT services agreement
- All code, models, configurations, and documentation are ACT property

### 9.2 IP Portfolio

| IP Asset | Type | Protection Strategy | Timeline |
|---|---|---|---|
| **3C Platform source code** (Python, React, n8n configs, SQL) | Copyright / Trade Secret | Private GitHub repos under ACT org. Copyright registration. All contributors sign IP assignment | Day 1 |
| **"Compliance → Care → Cash" unified architecture** | Utility Patent (provisional first) | Provisional patent covering the novel method of integrating regulatory compliance automation, AI clinical risk stratification, and automated CMS billing capture on a shared data model | Months 2--3 |
| **Automated RPM/CCM billing threshold detection pipeline** | Utility Patent (provisional first) | Method patent covering automated tracking of device transmission days, clinician time, and mutual exclusivity logic (99445/99454, 99470/99457) to generate billable events | Months 2--3 |
| **Configuration-driven multi-tenant healthcare deployment** | Utility Patent (provisional first) | Method patent covering the deployment of a standardized healthcare platform via feature flags and template workflows that adapt to each clinic's EHR, device mix, payer landscape, and module tier | Phase 2 |
| **ML risk stratification models** | Trade Secret | Trained model weights, feature engineering pipeline, SHAP-based explainability configuration. Not published. Served only via API | Ongoing |
| **n8n workflow template library** | Trade Secret | Proprietary clinic-specific workflow templates for EHR integration, RPM ingestion, billing automation, compliance tasks. Core competitive advantage | Ongoing |
| **Clinical rules engine** | Trade Secret | Proprietary encoding of CMS/HIPAA/HRSA regulatory rules, MIPS scoring logic, care gap detection criteria | Ongoing |
| **3C Platform trademark** | Trademark | File intent-to-use trademark application for "3C Platform" and ACT branding | Phase 1 |

### 9.3 Patent Strategy

**What makes the 3C Platform patentable:**
- No existing system combines regulatory compliance automation, AI clinical risk stratification, and automated CMS billing capture for any healthcare segment on a unified data model
- The specific method of using configuration-driven feature flags to deploy a standardized healthcare platform across clinics with different EHRs, device vendors, payer mixes, and regulatory requirements is novel
- The automated billing pipeline that tracks device transmission days, clinician interaction time, and applies mutual exclusivity rules across 2026 CMS codes is a novel process

**Patent timeline and budget:**
- **Months 2--3:** File 1--2 provisional patent applications (establishes priority date, 12-month window to convert). Cost: ~$3,000--$5,000 from contingency (patent attorney + USPTO fees)
- **Months 12--14:** Convert provisionals to full utility patent applications before 12-month deadline. Cost: ~$8,000--$15,000 (Phase 2 budget)
- **Ongoing:** Trade secret protections (NDAs with all team members, contractors, and pilot clinic staff who access proprietary systems)

### 9.4 Open-Source vs. Proprietary Boundary

| Layer | Open Source (Free) | Proprietary (ACT IP) |
|---|---|---|
| **Infrastructure** | n8n Community Edition, PostgreSQL, React, FastAPI, NGINX, Docker | -- |
| **Integration** | bonFHIR (Apache 2.0), FHIR R4 standard | Specific workflow templates, EHR configuration logic, data mapping rules |
| **Clinical Logic** | CMS published billing rules, USPSTF guidelines, MIPS methodology | Risk model training pipeline, feature engineering, SHAP configuration, care gap detection algorithms |
| **Business Logic** | -- | Module tiering system, clinic configuration engine, billing optimization pipeline, compliance scoring |
| **Data** | CMS Public Use Files (public) | Trained model weights, clinic-specific configurations, proprietary analytics |

**The moat is not the tools -- it's the specific clinical, regulatory, and billing logic encoded into the platform.** Anyone can deploy n8n and PostgreSQL. Nobody else has built the 3C clinical workflow library, the automated billing pipeline, or the compliance automation rules for RHCs.

---

## 10. SUCCESS METRICS

### 10.1 Phase 1 KPIs (Month 4 Report)

| Category | Metric | Target |
|---|---|---|
| **Compliance** | HIPAA task completion rate | >90% |
| **Compliance** | MIPS measures tracked | 5+ per clinic |
| **Care** | Patients enrolled in RPM | 15--20 per pilot clinic (30+ across all pilots; constrained by 15--20 pilot devices budgeted) |
| **Care** | Care gaps identified and addressed | 50+ per clinic |
| **Care** | Risk model AUC-ROC | >0.75 |
| **Cost** | New RPM/CCM revenue captured per clinic (monthly) | $5,000+ |
| **Cost** | RPM billing events auto-flagged correctly | >95% accuracy |
| **Platform** | Clinic staff adoption (weekly active users) | >80% |
| **Platform** | System uptime | >99.5% |
| **Platform** | New clinic onboarding time | <2 weeks |

### 10.2 Series A Metrics (Month 10)

| Metric | Target |
|---|---|
| Clinics live | 10+ |
| ARR | $240,000+ ($2K/month x 10 clinics) |
| Net revenue unlock per clinic | $100,000+/year |
| Annual churn | <10% |
| NPS (staff satisfaction) | >50 |
| MIPS penalty avoidance | 100% of pilot clinics |

---

## 11. COMPETITIVE LANDSCAPE

| Competitor | What They Do | Why 3C Wins |
|---|---|---|
| **Compliancy Group** | HIPAA compliance only | No care or billing |
| **Optimize Health** | RPM only | No compliance or billing optimization |
| **ThoroughCare** | CCM/RPM/TCM workflow + billing | Closest competitor -- no compliance module, no AI risk stratification, not purpose-built for RHC |
| **ChartSpan** | Outsourced CCM services | Service, not software -- takes margin from clinic |
| **Waystar / Availity** | Revenue cycle management | Billing only -- no clinical or compliance |
| **TelliHealth** | End-to-end RPM (devices + platform) | 4G LTE devices, good rural fit -- RPM only |
| **Azalea Health** | RHC-specific EHR + billing | No AI, limited RPM, no standalone compliance module |

**Competitive moat:**
1. **Unified platform** -- no competitor offers compliance + care + revenue on one platform
2. **IP-protected** -- provisional patent on unified architecture; all IP owned by ACT; trade secrets in clinical logic, ML models, and workflow templates
3. **Modular and scalable** -- three tiers serve clinics from 200 to 2,000+ patients; same codebase, configuration-driven
4. **93--95% gross margins** -- custom stack eliminates enterprise licensing costs
5. **RHC-specific** -- purpose-built for rural clinic workflows, not a hospital product scaled down
6. **VV defense pedigree** -- GovCloud infrastructure, security-first architecture, classified deployment experience
7. **Virginia-first** -- local relationships, VIPC backing, state policy alignment

**Pricing:** $500--$4,000/month per clinic (3 tiers). At the Professional tier ($2,000/month typical), the platform unlocks $195K--$267K/year in new CMS reimbursement -- an **8--11x return on subscription cost.** Even Essentials-tier clinics see ROI through compliance automation and MIPS penalty avoidance.

**Funding tailwind:** $50B Rural Health Transformation (RHT) Program (Public Law 119-21, $10B/year FY2026--FY2030) allocates funding to states for healthcare technology infrastructure. Virginia's FY2026 allocation is estimated at $147M--$281M. Position 3C as eligible technology spend for RHT state grants.

---

## 12. RISK REGISTER

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| **Pilot clinic EHR integration harder than expected** | HIGH | MEDIUM | Start with CSV import as fallback. Prioritize EHRs with strong FHIR (eCW, athena). Budget extra time. bonFHIR community provides support |
| **Clinic staff adoption resistance** | HIGH | MEDIUM | Involve staff in Sprint 1 design. Keep UI simple (max 3 clicks). On-site training. Show revenue impact early |
| **RPM patient enrollment low** | MEDIUM | HIGH | Provide devices at no cost (grant-funded). Start with highest-risk patients. Clinic champion (MA/nurse) leads enrollment |
| **ML model underperforms** | MEDIUM | LOW | Fall back to validated clinical risk scores (LACE index). ML is enhancement, not dependency |
| **HIPAA breach during pilot** | HIGH | LOW | KMS encryption from Day 1. BAAs with all vendors. Synthetic data for dev/test. Incident response plan before pilot |
| **n8n Community Edition throughput limit** | LOW | LOW | 23 req/s single mode is 10x our Phase 1 load. Upgrade to queue mode with Redis workers in Phase 2 if needed (available in Community Edition) |
| **EHR vendor blocks API access** | MEDIUM | LOW | Apply for developer program early. Backup: CSV/manual import. Multiple pilot clinics reduces single-EHR dependency |
| **AWS GovCloud cost overrun** | LOW | LOW | $34K contingency. GovCloud pricing is well-documented. Set billing alerts at $1K/month |
| **Pilot clinic drops out mid-project** | HIGH | MEDIUM | Secure LOIs from 4--5 candidate clinics. Maintain "cold start" demo mode with synthetic data. 2--3 clinic target provides redundancy |
| **n8n Community Edition lacks SSO/RBAC (HIPAA access control gap)** | MEDIUM | HIGH (certainty) | Restrict n8n UI to VV engineering via VPN + IP allowlisting. Clinic staff access React frontend only (application-level RBAC). Evaluate n8n Enterprise or external auth proxy for Phase 2 |

---

## 13. IMMEDIATE NEXT STEPS (Post-Grant Award)

| Action | Owner | Deadline | Dependency |
|---|---|---|---|
| Provision AWS GovCloud environment (ECS, RDS, S3, KMS) | VV Tech Lead | Week 1 | None |
| Execute AWS GovCloud BAA | VV Tech Lead | Week 1 | None |
| Deploy n8n + PostgreSQL + NGINX containers on Fargate | VV Tech Lead | Week 1 | GovCloud provisioned |
| Apply for EHR developer program (eCW / athena / Azalea) | VV Tech Lead | Week 1 | None |
| Identify and contact 5--10 candidate pilot RHCs | Jim + Mandy | Week 1--2 | None |
| Engage HIPAA compliance counsel | VV Tech Lead + Cari Ann | Week 1 | None |
| Complete HIPAA Security Rule risk assessment | VV Tech Lead + Cari Ann | Week 2--3 | None |
| Reach out to RPM device vendors (Tenovi, Smart Meter) -- API docs + pilot pricing | VV Tech Lead + Jim | Week 2 | None |
| Select and onboard first pilot clinic | Jim | Week 3--4 | Clinic outreach |
| Begin Sprint 1 development (database schema, React scaffold, auth) | VV Tech Lead | Week 1 | GovCloud ready |
| Contact Virginia Rural Health Association for introductions | Jim + Mandy | Week 2 | None |
| Engage patent attorney for provisional patent application | Jim + VV Tech Lead | Week 4--6 | Architecture documented |
| Execute VV-ACT work-for-hire / IP assignment agreement | Jim + VV Tech Lead | Week 1 | None |

---

*Prepared by: Veteran Vectors Engineering | Authentic Consortium*
*This is a living document -- updated as implementation progresses*
