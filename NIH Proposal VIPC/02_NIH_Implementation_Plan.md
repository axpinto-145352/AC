# NIH SBIR PHASE I -- IMPLEMENTATION PLAN

**Project Title:** AI-Driven Integrated Compliance, Care, and Revenue Optimization Platform for Rural Health Clinics
**Version:** 1.0 | **Classification:** Internal -- Authentic Consortium
**Prepared by:** Veteran Vectors (VV) Engineering
**Date:** February 25, 2026
**Purpose:** Detailed execution plan for the 3C Platform NIH SBIR Phase I research program (9 months, $256K)

---

## 1. EXECUTIVE SUMMARY

This implementation plan details the engineering and research execution strategy for the NIH SBIR Phase I project -- building and validating the **3C Platform** (Compliance, Care, Collect Cash) for Rural Health Clinics (RHCs). The platform is built on VV's proven stack: **n8n** (workflow automation), **PostgreSQL 16** (database), **Python/FastAPI** (API/ML), **React/Next.js** (frontend), and **Docker containers** on **Amazon GovCloud** (FedRAMP High, HIPAA-eligible).

**Key difference from the VIPC project:** The NIH SBIR scope emphasizes the **research and validation** dimensions -- AI model development, clinical outcome measurement, cross-domain interaction analysis, and rigorous statistical evaluation -- while the VIPC project focused on MVP deployment and investor presentation. The underlying platform technology is identical; the SBIR adds formal research methodology, IRB oversight, human subjects protections, and publication-quality analysis.

**Scope:** $256K total costs over 9 months. 2--3 Virginia RHC pilot sites. 50--100 RPM patients enrolled. Three research aims validated.

---

## 2. TECHNICAL ARCHITECTURE

### 2.1 Platform Stack (Identical to VIPC Deployment)

| Layer | Technology | Purpose | NIH SBIR Cost |
|---|---|---|---|
| **Hosting** | Amazon GovCloud (ECS Fargate + RDS + S3) | FedRAMP High, HIPAA BAA infrastructure | $750/month |
| **Workflow Engine** | n8n (self-hosted) | EHR integration, RPM ingestion, billing automation, compliance tasks, alert routing | Open-source (self-hosted) |
| **Database** | PostgreSQL 16 (Amazon RDS) | Central data store with RLS, AES-256, PGAudit | Included in GovCloud |
| **API/ML Layer** | Python/FastAPI | ML model serving, device data ingestion, FHIR transforms | Open-source |
| **Frontend** | React/Next.js | Clinic dashboard, research analytics dashboard | Open-source |
| **EHR Integration** | bonFHIR + n8n HTTP Request nodes | HL7 FHIR R4 connectivity | Open-source |
| **RPM Devices** | Tenovi / Smart Meter APIs | Cellular-connected monitoring devices | $150/unit avg |
| **Containerization** | Docker on ECS Fargate | Deployment, scaling, isolation | Included in GovCloud |
| **Reverse Proxy** | NGINX | TLS 1.2+, HSTS, CSP, rate limiting | Open-source |
| **ML Training** | XGBoost, scikit-learn, SHAP | Risk stratification, explainability | Open-source |
| **ML Compute** | GovCloud GPU (p3/p4 instances) | Model training and hyperparameter tuning | $2,500 total |

### 2.2 Phase I Architecture Diagram

```
+----------------------------------------------------------------------+
|               3C PLATFORM -- NIH SBIR PHASE I (Amazon GovCloud)       |
|                                                                       |
|  +------------------+  +------------------+  +--------------------+   |
|  |   COMPLIANCE     |  |      CARE        |  |   COLLECT CASH     |   |
|  |   MODULE         |  |      MODULE      |  |   MODULE           |   |
|  |                  |  |                  |  |                    |   |
|  | - HIPAA Audit    |  | - AI Risk        |  | - RPM/CCM Billing  |   |
|  |   Automation     |  |   Stratification |  |   Threshold Track  |   |
|  | - CMS Quality    |  |   (Aim 1)        |  |   (Aim 2)          |   |
|  |   Dashboard      |  | - RPM Device     |  | - Billing Event    |   |
|  | - Compliance     |  |   Integration    |  |   Generation       |   |
|  |   Task Tracker   |  |   (Aim 2)        |  | - MIPS/APM         |   |
|  |                  |  | - Deterioration  |  |   Dashboard        |   |
|  |                  |  |   Early Warning  |  | - Revenue Forecast |   |
|  |                  |  | - Care Gap       |  |                    |   |
|  |                  |  |   Detection      |  |                    |   |
|  +------------------+  +------------------+  +--------------------+   |
|                              |                                        |
|         +--------------------+------------------------+               |
|         |          AI/ML ENGINE (Aim 1)                |               |
|         | - Risk Stratification (XGBoost + SHAP)       |               |
|         | - Temporal Deterioration (sliding-window)     |               |
|         | - Anomaly Detection (RPM trends)              |               |
|         | - Bias Audit (fairness metrics)               |               |
|         +--------------------+------------------------+               |
|                              |                                        |
|         +--------------------+------------------------+               |
|         | UNIFIED DATA ARCHITECTURE (Aim 3)             |               |
|         | - PostgreSQL 16 with RLS                       |               |
|         | - Cross-domain materialized views              |               |
|         | - FHIR R4-aligned resource model               |               |
|         | - PGAudit + CloudTrail audit logging            |               |
|         +--------------------+------------------------+               |
|                              |                                        |
|         +--------------------+------------------------+               |
|         |  n8n WORKFLOW ENGINE + Python Services        |               |
|         | - EHR FHIR R4 (bonFHIR node)                  |               |
|         | - RPM device API ingestion                     |               |
|         | - Billing threshold triggers                    |               |
|         | - Compliance task automation                    |               |
|         | - Alert routing + notifications                 |               |
|         +-------------------------------------------------+           |
|                                                                       |
|         +-------------------------------------------------+           |
|         |  RESEARCH ANALYTICS LAYER (Phase I Addition)      |           |
|         | - Model performance tracking (AUC, sensitivity)    |           |
|         | - Cross-domain correlation analysis                |           |
|         | - De-identification pipeline for data sharing       |           |
|         | - Study outcome tracking dashboard                  |           |
|         +-------------------------------------------------+           |
+----------------------------------------------------------------------+
```

### 2.3 Research-Specific Architecture Additions

The NIH SBIR Phase I adds a **Research Analytics Layer** not present in the VIPC deployment:

| Component | Purpose | Technology |
|---|---|---|
| **Model Performance Tracker** | Continuous monitoring of AUC-ROC, sensitivity, specificity, calibration across risk strata | Python (scikit-learn metrics) + PostgreSQL logging + React dashboard |
| **Fairness Audit Module** | Compute equalized odds and demographic parity across protected characteristics | AIF360 / Fairlearn Python libraries |
| **Cross-Domain Correlation Engine** | Statistical analysis of compliance-care-revenue interactions | Python (scipy, statsmodels) + PostgreSQL materialized views |
| **De-Identification Pipeline** | HIPAA Safe Harbor de-identification for data sharing and publication | Python pipeline (presidio / custom) + PostgreSQL anonymized views |
| **Outcome Tracking Dashboard** | Track study endpoints: hospitalizations, ED visits, billing events, compliance scores | React dashboard + PostgreSQL time-series analytics |
| **IRB Audit Trail** | Enhanced logging for IRB compliance: consent tracking, data access logs, protocol deviation documentation | PGAudit extensions + custom n8n audit workflows |

---

## 3. DETAILED SPRINT PLAN

### 3.1 Sprint Overview (9-Month Phase I)

The 9-month Phase I is divided into **18 two-week sprints** organized into three overlapping tracks aligned with the three research aims.

| Sprint | Dates | Primary Focus | Aims Active |
|---|---|---|---|
| **S1** | Month 1, Wk 1--2 | Infrastructure + Data Acquisition | 1, 3 |
| **S2** | Month 1, Wk 3--4 | Data Model + Feature Engineering | 1, 3 |
| **S3** | Month 2, Wk 1--2 | Model Training + EHR Integration | 1, 2 |
| **S4** | Month 2, Wk 3--4 | Model Validation + Device Pipeline | 1, 2 |
| **S5** | Month 3, Wk 1--2 | IRB Submission + Billing Logic | 2, 3 |
| **S6** | Month 3, Wk 3--4 | Compliance Module + Consent Workflow | 2, 3 |
| **S7** | Month 4, Wk 1--2 | Pilot Clinic Onboarding (Clinic 1) | 1, 2, 3 |
| **S8** | Month 4, Wk 3--4 | Pilot Go-Live (Clinic 1) + Clinic 2 Prep | 1, 2, 3 |
| **S9** | Month 5, Wk 1--2 | Pilot Expansion (Clinic 2) + Data Collection | 1, 2, 3 |
| **S10** | Month 5, Wk 3--4 | Deterioration Detection Deployment | 1, 2 |
| **S11** | Month 6, Wk 1--2 | Full Pipeline Operational + Clinic 3 | 2, 3 |
| **S12** | Month 6, Wk 3--4 | Cross-Domain Analytics Development | 3 |
| **S13** | Month 7, Wk 1--2 | Model Performance Evaluation | 1 |
| **S14** | Month 7, Wk 3--4 | Revenue Impact Measurement | 2 |
| **S15** | Month 8, Wk 1--2 | Bias Audit + Fairness Evaluation | 1 |
| **S16** | Month 8, Wk 3--4 | Cross-Domain Findings Analysis | 3 |
| **S17** | Month 9, Wk 1--2 | Final Validation + Report Drafting | 1, 2, 3 |
| **S18** | Month 9, Wk 3--4 | Final Report + Phase II Preparation | 1, 2, 3 |

### 3.2 Sprint Details

#### Sprint 1 (Month 1, Weeks 1--2): Infrastructure and Data Acquisition

**Deliverables:**
- Amazon GovCloud account provisioned (ECS Fargate cluster, RDS PostgreSQL 16, S3 buckets, KMS keys, CloudTrail)
- HIPAA BAA executed with AWS
- CMS public use files downloaded and staged (Medicare Provider Utilization, Chronic Conditions, Hospital Readmissions)
- Development environment established (n8n, Docker Compose, CI/CD pipeline)
- IRB protocol draft initiated

**Acceptance Criteria:**
- [ ] GovCloud infrastructure passes security checklist (encryption at rest, TLS 1.2+, audit logging active)
- [ ] CMS data files loaded into staging PostgreSQL schema
- [ ] n8n accessible via HTTPS with authentication
- [ ] CI/CD pipeline deploys to GovCloud on merge to main

#### Sprint 2 (Month 1, Weeks 3--4): Data Model and Feature Engineering

**Deliverables:**
- PostgreSQL schema deployed: Patient, Encounter, Observation, Condition, MedicationRequest, Claim, ComplianceTask, BillingEvent, AuditLog tables
- Row-level security policies active (clinic-level isolation)
- Feature engineering pipeline: demographics, diagnosis history, utilization patterns, lab values, social determinant indicators
- CMS data transformed into training feature matrix

**Acceptance Criteria:**
- [ ] RLS policies verified: Clinic A cannot query Clinic B data
- [ ] Feature matrix generated from CMS data (target: 50+ features per patient record)
- [ ] Data quality report: completeness, distribution, outlier analysis
- [ ] PGAudit logging verified for all PHI-containing tables

#### Sprint 3 (Month 2, Weeks 1--2): Model Training and EHR Integration

**Deliverables:**
- XGBoost model trained on CMS data with 5-fold stratified cross-validation
- Logistic regression baseline model trained
- SHAP values computed for test set predictions
- EHR FHIR R4 integration initiated (eClinicalWorks or athenahealth sandbox)
- bonFHIR n8n node configured for Patient, Condition, Observation, Encounter resources

**Acceptance Criteria:**
- [ ] XGBoost cross-validation AUC-ROC documented (target: > 0.70 on CMS data alone)
- [ ] SHAP summary plot generated showing top-20 feature contributions
- [ ] FHIR R4 sandbox connection established (read Patient, Condition resources)
- [ ] Model training pipeline reproducible (versioned data + code + parameters)

#### Sprint 4 (Month 2, Weeks 3--4): Model Validation and Device Pipeline

**Deliverables:**
- Model performance report: AUC-ROC, sensitivity, specificity, calibration curves, confusion matrices by risk strata
- Fairness baseline metrics computed (equalized odds across available demographics)
- RPM device API integration (Tenovi): data pull, parsing, storage in PostgreSQL
- n8n workflow for RPM data ingestion (scheduled polling, range validation, dedup)

**Acceptance Criteria:**
- [ ] Model performance documented with confidence intervals
- [ ] Fairness metrics baseline report generated
- [ ] Tenovi API returns device readings into PostgreSQL Observation table
- [ ] n8n RPM ingestion workflow operational on 15-minute polling cycle

#### Sprint 5 (Month 3, Weeks 1--2): IRB Submission and Billing Logic

**Deliverables:**
- Full IRB protocol submitted for expedited review
- CMS billing threshold logic implemented in n8n workflows:
  - CPT 99454: 16-day device transmission tracking
  - CPT 99457/99458: Clinician time tracking (20-min increments)
  - CPT 99490: CCM monthly time tracking
  - CPT 99445: 2--15 day monitoring (new 2026 code)
  - CPT 99470: Abbreviated clinician interaction (new 2026 code)
  - Mutual exclusivity rules between competing codes
- Billing event data model and auto-generation logic

**Acceptance Criteria:**
- [ ] IRB protocol submitted with all required documents
- [ ] Billing logic passes unit tests against 50+ test scenarios
- [ ] Billing events correctly generated for simulated RPM data
- [ ] Mutual exclusivity rules prevent double-billing violations

#### Sprint 6 (Month 3, Weeks 3--4): Compliance Module and Consent Workflow

**Deliverables:**
- HIPAA compliance tracking module (audit automation, risk assessment, policy monitoring)
- CMS quality dashboard (MIPS measures: Quality 30%, Cost 30%, PI 25%, IA 15%)
- Patient consent workflow (clinical RPM consent + Medicare RPM consent + research consent)
- Compliance task automation (scheduled reminders, deadline tracking, completion verification)

**Acceptance Criteria:**
- [ ] HIPAA tracker displays current compliance status with risk scoring
- [ ] MIPS dashboard calculates estimated scores from sample data
- [ ] Consent workflow captures three consent types with audit trail
- [ ] Compliance tasks auto-generate based on regulatory calendar

#### Sprint 7 (Month 4, Weeks 1--2): Pilot Clinic 1 Onboarding

**Deliverables:**
- Pilot Clinic 1 EHR integration configured (Named Credentials, FHIR endpoints)
- Clinic staff training completed (dashboard, RPM workflow, billing tracker)
- RPM devices shipped and configured for initial patient cohort (15--20 patients)
- Alert thresholds configured per clinic medical director preferences
- Research consent process established with clinic staff

**Acceptance Criteria:**
- [ ] EHR data flowing into platform (Patient, Condition, Encounter resources)
- [ ] Staff can log in, view dashboard, acknowledge alerts
- [ ] Devices activated and transmitting test data to platform
- [ ] Research consent forms approved by IRB and available to clinic
- [ ] Go/no-go checklist completed for pilot launch

#### Sprint 8 (Month 4, Weeks 3--4): Pilot Go-Live and Clinic 2 Preparation

**Deliverables:**
- Pilot Clinic 1 goes live with enrolled RPM patients
- Real patient data flowing: RPM readings, clinical encounters, billing events
- Risk stratification model generating scores for enrolled patients
- Billing threshold tracking active
- Pilot Clinic 2 EHR integration initiated

**Acceptance Criteria:**
- [ ] RPM data from live patients visible in dashboard
- [ ] Risk scores generated with SHAP explanations for enrolled patients
- [ ] Billing events auto-generated when thresholds met
- [ ] No PHI security incidents during first 2 weeks of operation
- [ ] Clinic 2 EHR sandbox connection established

#### Sprint 9 (Month 5, Weeks 1--2): Pilot Expansion and Data Collection

**Deliverables:**
- Pilot Clinic 2 goes live
- Cross-clinic data collection protocol operational
- Research outcome tracking initiated: baseline ED visits, hospitalization rates, billing revenue
- Model refinement with live EHR data (transfer learning from CMS-trained model)

**Acceptance Criteria:**
- [ ] Clinic 2 operational with RPM patients enrolled
- [ ] Baseline outcome metrics captured for all enrolled patients
- [ ] Model retrained with pilot EHR data; performance delta documented
- [ ] RLS isolation verified between Clinic 1 and Clinic 2 data

#### Sprint 10 (Month 5, Weeks 3--4): Deterioration Detection Deployment

**Deliverables:**
- Temporal deterioration detection algorithms deployed:
  - BP trending (7-day, 14-day, 30-day sliding windows)
  - Weight gain velocity (CHF patients: > 3 lbs/day, > 5 lbs/week)
  - A1C trajectory (based on glucose monitor trends)
  - SpO2 decline detection (COPD/respiratory patients)
- Alert routing configured: provider email/SMS/dashboard notifications
- Alert-to-intervention tracking (time from alert to clinical action)

**Acceptance Criteria:**
- [ ] Deterioration algorithms generate alerts on live patient data
- [ ] Alerts delivered to providers within 5 minutes of threshold breach
- [ ] Alert-to-intervention time tracked in database
- [ ] False alert rate < 20% (provider-confirmed)

#### Sprint 11 (Month 6, Weeks 1--2): Full Pipeline Operational

**Deliverables:**
- Pilot Clinic 3 (optional) onboarded
- Full end-to-end pipeline verified: device → ingestion → analytics → alerts → billing → compliance
- All three modules operational across pilot clinics
- Billing accuracy audit against manual review

**Acceptance Criteria:**
- [ ] End-to-end data flow verified for all three modules
- [ ] Billing audit: < 5% discrepancy between automated and manual billing identification
- [ ] All pilot clinics stable and operational
- [ ] No unresolved PHI security incidents

#### Sprint 12 (Month 6, Weeks 3--4): Cross-Domain Analytics Development

**Deliverables:**
- Cross-domain materialized views in PostgreSQL:
  - Compliance documentation completeness ↔ claims denial rate
  - RPM device adherence ↔ clinical outcomes (ED/hospitalization)
  - MIPS quality scores ↔ reimbursement rate trends
  - Care gap closure ↔ RPM retention
  - Staffing patterns ↔ compliance task completion
- Statistical analysis pipeline (Python: scipy, statsmodels)
- Cross-domain analytics dashboard panels

**Acceptance Criteria:**
- [ ] Materialized views compute correctly from live pilot data
- [ ] At least 3 cross-domain correlations calculable from available data
- [ ] Dashboard displays cross-domain insights
- [ ] Statistical methodology documented for peer review

#### Sprints 13--16 (Months 7--8): Evaluation and Analysis

**Sprint 13: Model Performance Evaluation**
- Prospective validation of risk stratification against observed outcomes
- AUC-ROC, sensitivity, specificity with confidence intervals on pilot data
- Calibration analysis across risk strata
- Model comparison: XGBoost vs. logistic regression baseline

**Sprint 14: Revenue Impact Measurement**
- Billing event capture rate calculation (automated vs. total billable)
- Revenue impact: projected annual revenue increase per clinic
- False positive billing event rate
- Time savings: automated vs. manual billing identification workflow

**Sprint 15: Bias Audit and Fairness Evaluation**
- Fairness metrics: equalized odds, demographic parity across age, race/ethnicity, rural isolation
- Subgroup performance analysis (model accuracy by patient subpopulation)
- Bias mitigation recommendations for Phase II
- Documentation of any disparities with explanation and remediation plan

**Sprint 16: Cross-Domain Findings Analysis**
- Statistical significance testing for cross-domain correlations
- Effect size estimation for compliance-revenue, care-billing interactions
- Interrupted time series analysis (pre/post platform deployment)
- Qualitative analysis: clinic staff interviews on cross-domain insights

#### Sprints 17--18 (Month 9): Final Validation and Reporting

**Sprint 17: Final Validation and Report Drafting**
- Aggregate results across all three aims
- Draft Phase I final report (NIH format)
- Draft manuscript for peer-reviewed publication
- De-identified dataset preparation for NIH data repository

**Sprint 18: Final Report and Phase II Preparation**
- Submit Phase I final report to NIH
- Submit provisional patent application(s)
- Prepare Phase II proposal based on Phase I findings
- Document lessons learned and Phase II scope adjustments

---

## 4. TEAM STRUCTURE AND ROLES

### 4.1 Core Team

| Role | Person | Effort | Responsibilities |
|---|---|---|---|
| **PI / Lead Developer** | Will Nelson | 6.0 cal. months | Platform architecture, AI model development, n8n workflows, EHR/FHIR integration, RPM pipeline, GovCloud deployment, research protocol, final report |
| **Co-Investigator / Clinical Advisor** | TBD (Board-certified physician, rural health) | 1.0 cal. month | Clinical domain expertise, model feature validation, alert threshold design, pilot protocol oversight, co-author outcomes report |
| **Data Engineer** | TBD | 4.5 cal. months | PostgreSQL data model, RLS, RPM data pipeline, billing threshold logic, cross-domain materialized views, de-identification pipeline |
| **Clinical Informatics Specialist** | TBD | 3.0 cal. months | CMS billing rules encoding, compliance workflow automation, clinical workflow mapping, billing accuracy validation, consent workflow |

### 4.2 Advisory Roles (Unfunded)

| Role | Contribution |
|---|---|
| **Pilot Clinic Medical Director(s)** | Clinical workflow validation, alert threshold approval, staff coordination, patient enrollment |
| **Compliance Officer (Pilot Clinic)** | HIPAA compliance validation, regulatory requirement verification |
| **Billing Manager (Pilot Clinic)** | RPM/CCM billing logic validation, revenue impact verification |
| **IRB Liaison** | Protocol review coordination, amendment processing |

---

## 5. DATA MANAGEMENT PLAN

### 5.1 Data Types and Sources

| Data Type | Source | Volume | Sensitivity |
|---|---|---|---|
| **CMS Public Use Files** | CMS.gov | ~5 GB | Public (de-identified) |
| **EHR Clinical Data** | Pilot clinic EHRs via FHIR R4 | ~500 MB/clinic | PHI (HIPAA-protected) |
| **RPM Device Data** | Tenovi/Smart Meter APIs | ~100 MB/month | PHI (HIPAA-protected) |
| **Billing Events** | Platform-generated | ~10 MB/month | PHI (HIPAA-protected) |
| **Compliance Records** | Platform-generated | ~5 MB/month | Sensitive (internal) |
| **Model Outputs** | Platform-generated | ~50 MB/month | PHI-derived (HIPAA-protected) |
| **Research Analytics** | Platform-generated (de-identified) | ~100 MB | De-identified |

### 5.2 Data Storage and Security

| Control | Implementation |
|---|---|
| **Encryption at Rest** | AES-256 via AWS KMS (customer-managed keys) |
| **Encryption in Transit** | TLS 1.2+ for all connections |
| **Access Control** | PostgreSQL RLS (clinic-level isolation) + application RBAC |
| **Audit Logging** | PGAudit (database) + CloudTrail (infrastructure) + application audit log |
| **Backup** | Automated daily RDS snapshots, 30-day retention, cross-region replication |
| **Disaster Recovery** | RTO 4 hours, RPO 1 hour (RDS point-in-time recovery) |
| **Data Retention** | PHI retained per HIPAA requirements (6 years minimum); research data retained per NIH policy |
| **De-identification** | HIPAA Safe Harbor method for all research datasets and publications |
| **Data Destruction** | Cryptographic erasure via KMS key rotation for decommissioned data |

### 5.3 Data Sharing

- **NIH Data Repository:** De-identified, aggregated pilot data deposited within 12 months of Phase I completion
- **Publication Data:** De-identified datasets supporting published findings made available per journal requirements
- **Platform Data:** PHI and clinic-specific data remain under clinic control; not shared externally
- **Model Artifacts:** Trained model weights are trade secrets owned by ACT; model performance metrics and methodology are published

---

## 6. BUDGET EXECUTION PLAN

### 6.1 Monthly Budget Allocation

| Month | Personnel | Infrastructure | Devices | Travel | Other | Monthly Total |
|---|---|---|---|---|---|---|
| **1** | $21,667 | $1,250 | $0 | $0 | $1,000 | $23,917 |
| **2** | $21,667 | $750 | $0 | $0 | $1,500 | $23,917 |
| **3** | $21,667 | $750 | $3,750 | $750 | $3,000 | $29,917 |
| **4** | $21,667 | $750 | $0 | $2,250 | $1,500 | $26,167 |
| **5** | $21,667 | $750 | $0 | $750 | $500 | $23,667 |
| **6** | $21,667 | $750 | $0 | $0 | $1,000 | $23,417 |
| **7** | $21,667 | $750 | $0 | $750 | $5,000 | $28,167 |
| **8** | $21,667 | $750 | $0 | $750 | $500 | $23,667 |
| **9** | $21,667 | $750 | $0 | $1,250 | $500 | $24,167 |
| **Total** | **$195,000** | **$7,000** | **$3,750** | **$6,500** | **$14,500** | **$226,750** |

*Note: Remaining ~$4,250 allocated to indirect costs and contingency. Total with indirect: $256,000.*

### 6.2 Key Budget Controls

- **Monthly burn rate monitoring:** Track actual vs. planned spend by category
- **GovCloud cost optimization:** Right-size instances monthly; use Fargate Spot for non-production workloads
- **Personnel cost management:** Subcontract agreements with defined deliverables and payment milestones
- **Contingency triggers:** If any single budget category exceeds 120% of plan, escalate to PI for reallocation decision
- **NIH reporting:** Quarterly financial reports per NIH SBIR requirements

---

## 7. QUALITY ASSURANCE AND TESTING

### 7.1 Testing Strategy

| Test Type | Scope | Frequency | Standard |
|---|---|---|---|
| **Unit Tests** | All Python services, n8n workflow logic, billing calculations | Every commit | > 85% code coverage; all billing logic 100% covered |
| **Integration Tests** | EHR FHIR connectivity, RPM API ingestion, end-to-end billing pipeline | Every sprint | All FHIR resources read/write correctly; billing events generated from device data |
| **Model Validation** | AI risk stratification, deterioration detection | Monthly during pilot | AUC-ROC, sensitivity, specificity, calibration, fairness metrics tracked |
| **Security Testing** | Penetration testing, HIPAA audit, RLS verification | Quarterly | No critical/high vulnerabilities; RLS isolation verified |
| **User Acceptance Testing** | Clinic staff test dashboard, alerts, workflows | Pre-go-live and monthly | Clinician satisfaction > 4.0/5.0; task completion rate > 90% |
| **Billing Accuracy Audit** | Automated vs. manual billing identification | Monthly during pilot | < 5% discrepancy rate |
| **Data Quality Checks** | Completeness, accuracy, consistency of ingested data | Daily (automated) | > 95% completeness; < 1% duplicate rate |

### 7.2 Continuous Integration / Continuous Deployment

```
Developer Push → GitHub Actions CI:
  1. Lint (Python: ruff; JS: eslint)
  2. Unit tests (pytest; jest)
  3. Integration tests (against test GovCloud environment)
  4. Security scan (Trivy container scan, Bandit Python security)
  5. Build Docker images
  6. Deploy to staging (GovCloud staging cluster)
  7. Smoke tests on staging
  8. Manual approval gate for production
  9. Deploy to production (GovCloud production cluster)
  10. Post-deploy health checks
```

### 7.3 Incident Response

| Severity | Definition | Response Time | Notification |
|---|---|---|---|
| **Critical** | PHI exposure, system down, billing error affecting live claims | 1 hour | PI + clinic medical director + IRB |
| **High** | Feature failure affecting patient care alerts, data ingestion gap | 4 hours | PI + clinic staff |
| **Medium** | Dashboard display issue, non-critical workflow failure | 24 hours | PI |
| **Low** | Cosmetic issues, documentation gaps | Next sprint | Sprint backlog |

---

## 8. REGULATORY AND COMPLIANCE FRAMEWORK

### 8.1 HIPAA Compliance

| Requirement | Implementation |
|---|---|
| **Privacy Rule** | PHI access limited to authorized clinic staff and research team; minimum necessary standard enforced via RBAC |
| **Security Rule** | AES-256 encryption, TLS 1.2+, RLS, PGAudit, MFA for all administrative access |
| **Breach Notification** | Incident response plan with 24-hour internal notification, 60-day HHS/individual notification per HIPAA |
| **BAA** | Business Associate Agreements with AWS (GovCloud), Tenovi (RPM vendor), pilot clinics |
| **Risk Assessment** | Annual HIPAA Security Risk Assessment per NIST SP 800-66; initial assessment in Sprint 1 |
| **Training** | HIPAA training for all team members with annual refresher; documented completion |

### 8.2 FDA Regulatory Position

The 3C Platform's clinical decision support functionality (risk stratification, deterioration alerts) qualifies for the **21st Century Cures Act CDS exemption** based on all four criteria:

1. **Does not acquire or process signals from a medical device** -- platform ingests data from external devices via API, does not control device acquisition
2. **Displays, analyzes, or prints medical information** -- risk scores and SHAP explanations are informational displays
3. **Supports or provides recommendations to healthcare professionals** -- all outputs are advisory to the licensed provider
4. **Enables the healthcare professional to independently review the basis** -- SHAP values provide feature-level transparency for every prediction

The January 2026 FDA CDS guidance update broadens enforcement discretion for software meeting these criteria. Phase II will include formal FDA regulatory assessment if the platform scope expands to include device-controlling or autonomous clinical functions.

### 8.3 IRB Protocol Summary

| Element | Detail |
|---|---|
| **Review Type** | Expedited (minimal risk -- no intervention beyond standard RPM care) |
| **Population** | Adult patients (18+) at pilot RHCs with chronic conditions eligible for RPM |
| **Consent** | Three-part: clinical RPM consent, Medicare RPM billing consent, research data use consent |
| **Risks** | Minimal: data breach (mitigated by GovCloud security), false positive alerts (mitigated by provider review of all alerts), privacy concerns (mitigated by de-identification for research use) |
| **Benefits** | Direct: improved monitoring, earlier intervention, potential revenue increase. Indirect: contributes to rural health knowledge base |
| **Data Handling** | All PHI in GovCloud; de-identified data only for research analysis and publication |
| **Monitoring** | Quarterly data safety monitoring; adverse event reporting to IRB and NIH |

---

## 9. RISK MANAGEMENT

### 9.1 Risk Register

| ID | Risk | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| **R1** | EHR integration takes longer than planned | Medium | High | Prioritize single EHR (eClinicalWorks); fall back to CSV import; budget 2 extra weeks | PI |
| **R2** | Low RPM patient enrollment | Medium | High | Free devices to patients; cellular (no WiFi needed); clinic staff-led enrollment; incentive structure | PI + Co-I |
| **R3** | IRB review delayed beyond Month 3 | Low | High | Submit in Sprint 5 (Month 3); begin non-PHI development in parallel; pre-IRB engagement with review board | PI |
| **R4** | Model AUC-ROC below 0.75 threshold | Low-Med | Medium | Pre-trained on CMS data with known signal; fallback to simpler model; adjust threshold definition; document with explanation | PI |
| **R5** | Pilot clinic drops out | Medium | Medium | Target 2--3 clinics (redundancy); replacement clinic identified in advance; modular deployment enables rapid redeployment | PI |
| **R6** | GovCloud cost overrun | Low | Low | Monthly cost monitoring; right-sizing; Fargate Spot for dev/test; $4,250 contingency | PI |
| **R7** | Key personnel unavailability | Low | High | Cross-training on critical systems; documented deployment procedures; PI can cover data engineering tasks | PI |
| **R8** | PHI security incident | Low | Critical | GovCloud FedRAMP High controls; RLS; PGAudit; incident response plan; encryption at rest and in transit | PI |
| **R9** | Regulatory change to RPM billing codes | Low | Medium | Modular billing rules engine; CMS trend is toward expansion; monitor Federal Register | Clinical Informatics |
| **R10** | Insufficient cross-domain data for Aim 3 | Medium | Medium | Supplement with synthetic data analysis; adjust statistical methods; document limitations transparently | PI |

### 9.2 Go/No-Go Decision Points

| Decision Point | Timing | Criteria | Fallback |
|---|---|---|---|
| **Infrastructure Ready** | End of Sprint 1 | GovCloud operational, security verified | Delay pilot by 2 weeks; escalate AWS support |
| **IRB Approved** | End of Sprint 6 | IRB expedited approval received | Proceed with de-identified CMS data only; submit protocol revision |
| **Pilot Clinic 1 Go-Live** | End of Sprint 7 | EHR integrated, staff trained, devices deployed, consent process ready | Delay 1 sprint; identify alternative clinic |
| **Model Performance Gate** | End of Sprint 13 | AUC-ROC > 0.70 (relaxed from 0.75 for interim check) | Retrain with additional features; simplify model; adjust success criteria with NIH program officer |
| **Billing Accuracy Gate** | End of Sprint 14 | < 10% discrepancy rate (relaxed from 5% for interim) | Debug billing logic; manual review supplement; adjust target |

---

## 10. COMMUNICATION AND REPORTING

### 10.1 Internal Communication

| Meeting | Frequency | Participants | Purpose |
|---|---|---|---|
| **Sprint Planning** | Biweekly | Full team | Plan next sprint deliverables |
| **Daily Standup** | Daily (15 min) | PI + active team members | Blockers, progress, coordination |
| **Pilot Clinic Check-in** | Weekly | PI + clinic point of contact | Operational issues, enrollment status, feedback |
| **Clinical Review** | Monthly | PI + Co-I + clinic medical director | Model outputs review, alert accuracy, clinical workflow |

### 10.2 NIH Reporting

| Report | Timing | Content |
|---|---|---|
| **Progress Report** | Month 4 (interim) | Aims 1--3 status, pilot enrollment, preliminary findings |
| **Financial Report** | Quarterly | Budget execution, variances, justification |
| **Final Report** | Month 9 | Complete Phase I findings, all aims, Phase II plan |
| **Invention Report** | As applicable | Patent filings, IP disclosures |
| **Human Subjects Report** | Annual / at close | Enrollment, adverse events, protocol deviations |

---

## 11. PHASE II TRANSITION PLAN

### 11.1 Phase I → Phase II Bridge

| Phase I Outcome | Phase II Action |
|---|---|
| **Model AUC-ROC > 0.75 validated** | Expand to 50+ clinics; refine with multi-site data; pursue clinical outcome study |
| **Billing capture > 90% validated** | Add NLP coding optimization, denial prevention, clearinghouse integration |
| **Cross-domain interactions demonstrated** | Develop predictive compliance risk model; publish in JAMIA/Journal of Rural Health |
| **Patent provisional filed** | Convert to utility patent; file additional claims based on Phase I innovations |
| **2--3 pilot clinics operational** | Scale to 10+ Virginia clinics; add MEDITECH, Azalea Health, TruBridge EHR support |

### 11.2 Phase II Budget Estimate

| Category | Phase II (18 months) |
|---|---|
| **Personnel** (expanded team: 2 additional engineers, clinical research coordinator) | $450,000 |
| **Infrastructure** (GovCloud scale-up for 50+ clinics) | $54,000 |
| **RPM Devices** (200+ units for expanded pilot) | $30,000 |
| **Clinical Research** (outcome study, multi-site coordination) | $100,000 |
| **Legal/IP** (utility patent, additional filings) | $25,000 |
| **Travel** (clinic onboarding, conferences, NIH meetings) | $20,000 |
| **Other** (EHR access, monitoring, audit) | $21,000 |
| **Indirect** | $100,000 |
| **Total Phase II** | **~$800,000** |

---

*Prepared by: Authentic Consortium / Veteran Vectors Engineering*
*Version 1.0 -- February 25, 2026*
