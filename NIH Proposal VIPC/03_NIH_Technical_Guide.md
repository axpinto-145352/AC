# NIH SBIR PHASE I -- TECHNICAL GUIDE

**Project Title:** AI-Driven Integrated Compliance, Care, and Revenue Optimization Platform for Rural Health Clinics
**Version:** 1.0 | **Classification:** Internal -- Authentic Consortium
**Prepared by:** Veteran Vectors (VV) Engineering
**Date:** February 25, 2026
**Purpose:** Comprehensive technical reference for the 3C Platform architecture, AI/ML methodology, data pipeline design, and security framework supporting the NIH SBIR Phase I research

---

## 1. TECHNICAL OVERVIEW

The **3C Platform** (Compliance, Care, Collect Cash) is an AI-driven integrated healthcare technology platform designed specifically for Rural Health Clinics (RHCs). This technical guide documents the complete engineering architecture, AI/ML methodology, data pipeline design, integration specifications, and security framework.

### 1.1 Design Principles

| Principle | Implementation |
|---|---|
| **Open-source first** | n8n, PostgreSQL, Python/FastAPI, React/Next.js, Docker -- zero licensing dependencies |
| **GovCloud-native** | All components deployed on Amazon GovCloud (FedRAMP High, HIPAA BAA) |
| **Configuration-driven** | Multi-tenant via feature flags and template workflows, not separate codebases |
| **FHIR-native** | Data model aligned with HL7 FHIR R4; EHR integration via bonFHIR and standard FHIR APIs |
| **Explainable AI** | Every prediction accompanied by SHAP-based feature explanations; no black-box outputs |
| **Defense-grade security** | Same architecture and security patterns used for DoD classified system deployments |
| **Rural-first design** | Cellular device connectivity (no WiFi dependency); asynchronous data sync for unreliable broadband |

### 1.2 System Context Diagram

```
+------------------------------------------------------------------+
|                    EXTERNAL SYSTEMS                                |
|                                                                   |
|  +-----------+  +------------+  +----------+  +---------------+   |
|  | EHR       |  | RPM Device |  | CMS      |  | Clearinghouse |   |
|  | Systems   |  | Vendors    |  | Databases |  | (Phase 2)     |   |
|  | (FHIR R4) |  | (REST API) |  | (Batch)  |  | (X12/HL7)     |   |
|  +-----------+  +------------+  +----------+  +---------------+   |
|       |               |              |               |            |
+-------|---------------|--------------|---------------|------------+
        |               |              |               |
+-------|---------------|--------------|---------------|------------+
|       v               v              v               v            |
|  +--------------------------------------------------------+      |
|  |              n8n WORKFLOW ENGINE                         |      |
|  |  - FHIR R4 workflows (bonFHIR node)                     |      |
|  |  - RPM device polling workflows                          |      |
|  |  - Billing threshold automation                          |      |
|  |  - Compliance task scheduling                            |      |
|  |  - Alert routing (email/SMS/webhook)                     |      |
|  |  - CMS data import workflows                             |      |
|  +--------------------------------------------------------+      |
|       |                                                           |
|       v                                                           |
|  +--------------------------------------------------------+      |
|  |            Python / FastAPI Services                     |      |
|  |  - ML model serving (risk stratification)                |      |
|  |  - FHIR data transforms (device → Observation)           |      |
|  |  - Temporal analytics (deterioration detection)          |      |
|  |  - De-identification pipeline                            |      |
|  |  - Research analytics API                                |      |
|  +--------------------------------------------------------+      |
|       |                                                           |
|       v                                                           |
|  +--------------------------------------------------------+      |
|  |      PostgreSQL 16 (Amazon RDS -- GovCloud)              |      |
|  |  - FHIR-aligned data model                               |      |
|  |  - Row-level security (clinic isolation)                  |      |
|  |  - AES-256 encryption at rest (KMS)                      |      |
|  |  - PGAudit (HIPAA audit trail)                           |      |
|  |  - Cross-domain materialized views                       |      |
|  +--------------------------------------------------------+      |
|       |                                                           |
|       v                                                           |
|  +--------------------------------------------------------+      |
|  |          React / Next.js Dashboard                       |      |
|  |  - Patient 360 view                                      |      |
|  |  - Compliance tracker                                    |      |
|  |  - Billing tracker + MIPS dashboard                      |      |
|  |  - Risk stratification display (with SHAP)               |      |
|  |  - Research analytics panels                             |      |
|  +--------------------------------------------------------+      |
|                                                                   |
|              3C PLATFORM (Amazon GovCloud)                         |
+------------------------------------------------------------------+
```

---

## 2. AI/ML ARCHITECTURE

### 2.1 Risk Stratification Engine (Aim 1)

#### 2.1.1 Model Architecture

**Primary Model: XGBoost Gradient Boosted Ensemble**

```
Input Features (50+)                    Model Pipeline
+------------------------+     +----------------------------------+
| Demographics           |     |                                  |
| - Age, Sex, BMI        |     |  Missing Value Imputation        |
| - Rural isolation index |     |  (iterative imputer, MICE)       |
|                        |     |          |                        |
| Diagnosis History      |     |          v                        |
| - ICD-10 codes (top 50)|     |  Feature Scaling                 |
| - Condition count      |     |  (robust scaler)                 |
| - Comorbidity index    |     |          |                        |
|                        |     |          v                        |
| Utilization Patterns   |     |  XGBoost Ensemble                |
| - ED visits (6/12 mo)  |     |  - 500 trees                     |
| - Hospitalizations     |     |  - max_depth: 6                  |
| - Missed appointments  |     |  - learning_rate: 0.05           |
| - Provider visit freq  |     |  - subsample: 0.8                |
|                        |     |  - colsample_bytree: 0.8         |
| Lab Values             |     |  - min_child_weight: 5           |
| - A1C (latest + trend) |     |  - reg_alpha: 0.1                |
| - eGFR                 |     |  - reg_lambda: 1.0               |
| - Lipid panel          |     |          |                        |
| - CBC components       |     |          v                        |
|                        |     |  SHAP Explainer                  |
| Medication             |     |  (TreeExplainer)                 |
| - Active med count     |     |          |                        |
| - Adherence proxy      |     |          v                        |
| - High-risk meds       |     |  +----------------------------+  |
|                        |     |  | Risk Score (0-100)         |  |
| Social Determinants    |     |  | Top-K Feature Contributions|  |
| - Broadband access     |     |  | Confidence Interval        |  |
| - Transportation index |     |  | Risk Stratum (Low/Med/High)|  |
| - SVI score            |     |  +----------------------------+  |
+------------------------+     +----------------------------------+
```

**Baseline Model: Logistic Regression**

A logistic regression model with L2 regularization serves as the interpretable baseline for comparison. Same feature set, standardized coefficients provide direct feature importance without SHAP computation.

#### 2.1.2 Training Data Pipeline

```
CMS Public Use Files                    Pilot Clinic EHR Data
+---------------------------+           +---------------------------+
| Medicare Provider          |           | FHIR R4 Resources:        |
|   Utilization Data         |           | - Patient                 |
| Chronic Conditions         |           | - Condition               |
|   Prevalence               |           | - Encounter               |
| Hospital Readmissions      |           | - Observation             |
|   Reduction Program        |           | - MedicationRequest       |
| SDOH Indicators            |           | - Claim (if available)    |
+---------------------------+           +---------------------------+
            |                                       |
            v                                       v
    +--------------------------------------------------+
    |         Feature Engineering Pipeline               |
    |                                                    |
    |  1. ICD-10 code grouping (CCS categories)          |
    |  2. Temporal feature extraction (trends, velocity)  |
    |  3. Comorbidity index computation (Elixhauser)      |
    |  4. Utilization pattern encoding                    |
    |  5. Lab value normalization + trend features         |
    |  6. Missing value indicators (missingness patterns)  |
    |  7. Social determinant index computation             |
    +--------------------------------------------------+
            |
            v
    +--------------------------------------------------+
    |         Training / Validation Split                 |
    |                                                    |
    |  CMS Data: 5-fold stratified cross-validation       |
    |  Pilot Data: Temporal split (train on months 1-6,   |
    |              validate on months 7-9)                 |
    |  Outcome: 30/60/90-day hospitalization or ED visit   |
    +--------------------------------------------------+
            |
            v
    +--------------------------------------------------+
    |         Hyperparameter Optimization                 |
    |                                                    |
    |  Method: Bayesian (Optuna)                          |
    |  Objective: AUC-ROC on validation fold               |
    |  Search space: learning_rate, max_depth, n_trees,    |
    |    subsample, colsample_bytree, min_child_weight,    |
    |    reg_alpha, reg_lambda                              |
    |  Budget: 200 trials                                  |
    +--------------------------------------------------+
```

#### 2.1.3 Model Evaluation Framework

| Metric | Target | Measurement |
|---|---|---|
| **AUC-ROC** | > 0.75 | Area under receiver operating characteristic curve |
| **Sensitivity (top decile)** | > 80% | True positive rate for highest-risk 10% of patients |
| **Specificity** | > 60% | True negative rate (minimize alert fatigue) |
| **Calibration** | Within 10% across strata | Predicted probability matches observed rate per risk quintile |
| **Positive Predictive Value** | > 30% (top decile) | Proportion of high-risk alerts that result in actual events |
| **AUC-PR** | Reported | Area under precision-recall curve (important for imbalanced data) |
| **Brier Score** | < 0.15 | Overall calibration quality |

**Fairness Metrics (computed per subgroup):**

| Metric | Definition | Threshold |
|---|---|---|
| **Equalized Odds** | TPR and FPR equal across groups | Difference < 0.05 |
| **Demographic Parity** | Positive prediction rate equal across groups | Difference < 0.10 |
| **Predictive Parity** | PPV equal across groups | Difference < 0.10 |

Subgroups: Age (< 65, 65--74, 75+), race/ethnicity (as available), rural isolation quartile, gender.

#### 2.1.4 SHAP Explainability Implementation

```python
# SHAP computation for each prediction
import shap

# TreeExplainer for XGBoost (exact SHAP values, fast)
explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(patient_features)

# Per-prediction output structure
prediction_output = {
    "patient_id": "uuid",
    "risk_score": 78,                    # 0-100 scaled
    "risk_stratum": "HIGH",              # LOW/MEDIUM/HIGH
    "prediction_horizon": "30_day",       # 30/60/90
    "confidence_interval": [72, 84],      # Bootstrap CI
    "top_contributing_factors": [
        {"feature": "ed_visits_6mo", "value": 3, "shap": 0.24,
         "direction": "increases_risk",
         "display": "3 ED visits in past 6 months"},
        {"feature": "a1c_latest", "value": 9.2, "shap": 0.18,
         "direction": "increases_risk",
         "display": "A1C of 9.2 (above target)"},
        {"feature": "missed_appts_12mo", "value": 4, "shap": 0.12,
         "direction": "increases_risk",
         "display": "4 missed appointments in past year"},
    ],
    "model_version": "v1.2.0",
    "timestamp": "2026-10-15T14:30:00Z"
}
```

**Provider-facing display:** The React dashboard renders SHAP values as a horizontal bar chart showing top contributing factors with clinical labels, not raw feature names. Each factor includes the patient's actual value and a natural-language explanation. The provider can drill into any factor for additional context.

### 2.2 Temporal Deterioration Detection

#### 2.2.1 Algorithm Design

```
RPM Data Stream (per patient, per vital sign)
+--------------------------------------------+
| Timestamp | Value | Device | Valid |
|-----------|-------|--------|-------|
| 2026-10-01 08:00 | 142/88 | BP    | Yes   |
| 2026-10-01 20:00 | 148/92 | BP    | Yes   |
| 2026-10-02 08:15 | 151/94 | BP    | Yes   |
| ...                                         |
+--------------------------------------------+
            |
            v
+--------------------------------------------+
| Sliding Window Analysis                     |
|                                             |
| Window sizes: 7-day, 14-day, 30-day         |
|                                             |
| Metrics per window:                          |
| - Mean, median, std deviation                |
| - Linear trend (slope)                       |
| - Volatility (coefficient of variation)      |
| - Threshold breach count                     |
| - Missing reading count (adherence)          |
+--------------------------------------------+
            |
            v
+--------------------------------------------+
| Alert Rules Engine                           |
|                                             |
| Static thresholds (immediate):               |
| - BP > 180/120 → URGENT                     |
| - SpO2 < 90% → URGENT                       |
| - Blood glucose > 400 mg/dL → URGENT        |
| - Weight gain > 3 lbs/day (CHF) → HIGH      |
|                                             |
| Trend thresholds (7-day window):             |
| - Systolic BP slope > 2 mmHg/day → MEDIUM   |
| - Glucose slope > 5 mg/dL/day → MEDIUM      |
| - SpO2 slope < -0.5%/day → HIGH             |
| - Weight slope > 0.5 lbs/day (CHF) → MEDIUM |
|                                             |
| Combined scoring:                            |
| - Static breach + trending = escalate 1 level|
| - Multiple vital trends = escalate 1 level   |
+--------------------------------------------+
            |
            v
+--------------------------------------------+
| Alert Routing (n8n workflow)                 |
|                                             |
| URGENT → Immediate: SMS + dashboard + email  |
| HIGH → Within 1 hour: dashboard + email      |
| MEDIUM → Within 4 hours: dashboard           |
| LOW → Next business day: dashboard           |
+--------------------------------------------+
```

#### 2.2.2 Configurable Thresholds

All thresholds are stored in a `clinic_alert_config` table and are adjustable per clinic and per patient by the medical director:

```sql
CREATE TABLE clinic_alert_config (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID REFERENCES patients(id),  -- NULL = clinic default
    vital_type TEXT NOT NULL,  -- 'bp_systolic', 'bp_diastolic', 'spo2', 'glucose', 'weight'
    threshold_type TEXT NOT NULL,  -- 'static_urgent', 'static_high', 'trend_7day', 'trend_14day'
    threshold_value DECIMAL NOT NULL,
    direction TEXT NOT NULL,  -- 'above', 'below'
    enabled BOOLEAN DEFAULT TRUE,
    updated_by UUID NOT NULL REFERENCES users(id),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 3. DATA PIPELINE ARCHITECTURE

### 3.1 RPM Device Data Ingestion (Aim 2)

```
Cellular RPM Devices                    Tenovi / Smart Meter Cloud
(at patient home)                       (device vendor)
+------------------+                    +------------------+
| BP Cuff          | --- cellular --->  | Vendor API       |
| Glucose Monitor  |                    | (REST/JSON)      |
| Pulse Oximeter   |                    |                  |
| Weight Scale     |                    +------------------+
+------------------+                            |
                                                | HTTPS
                                                v
+----------------------------------------------------------------------+
|  n8n RPM Ingestion Workflow (runs every 15 minutes)                   |
|                                                                       |
|  1. Poll Tenovi API: GET /readings?since={last_poll_timestamp}        |
|  2. Parse response: extract patient_id, device_type, reading, ts      |
|  3. Validate: range check, duplicate detection, device calibration    |
|  4. Transform: map to FHIR Observation resource structure              |
|  5. Store: INSERT into observations table (PostgreSQL)                 |
|  6. Evaluate: check reading against alert thresholds                   |
|  7. Alert: if threshold breached, trigger alert workflow                |
|  8. Track: update device_transmission_days for billing (CPT 99454)     |
|  9. Log: audit entry for every reading processed                       |
+----------------------------------------------------------------------+
```

### 3.2 EHR Integration via FHIR R4

```
Clinic EHR (eClinicalWorks / athenahealth)
+------------------------------------------+
| FHIR R4 Server                            |
| Base URL: https://fhir.{ehr}.com/r4       |
| Auth: OAuth 2.0 (client_credentials)      |
+------------------------------------------+
            |
            | HTTPS + OAuth 2.0
            v
+------------------------------------------+
| n8n EHR Sync Workflow                      |
| (bonFHIR node + HTTP Request nodes)        |
|                                            |
| Resources synced:                          |
| - Patient (demographics, identifiers)      |
| - Condition (diagnoses, ICD-10 codes)      |
| - Encounter (visits, admissions, ED)       |
| - Observation (labs, vitals from EHR)      |
| - MedicationRequest (active prescriptions) |
| - AllergyIntolerance                       |
| - Procedure                                |
| - DiagnosticReport                         |
|                                            |
| Sync modes:                                |
| - Full sync: nightly (2:00 AM local)       |
| - Incremental: every 2 hours (_lastUpdated)|
| - On-demand: triggered by dashboard action |
|                                            |
| Conflict resolution:                       |
| - EHR is source of truth for clinical data |
| - Platform is source of truth for RPM data |
| - Billing events generated from combined   |
+------------------------------------------+
```

### 3.3 CMS Billing Automation Pipeline (Aim 2)

```
+----------------------------------------------------------------------+
| BILLING THRESHOLD TRACKING (n8n scheduled workflow -- runs daily)      |
|                                                                       |
| FOR EACH enrolled RPM patient:                                        |
|                                                                       |
| 1. COUNT device transmission days this billing period (30 days)       |
|    - Unique calendar days with at least 1 valid reading               |
|    - Source: observations table WHERE device_sourced = TRUE            |
|                                                                       |
| 2. EVALUATE against CPT code thresholds:                              |
|                                                                       |
|    CPT 99453 (Initial device setup):                                  |
|    - One-time, first month only                                       |
|    - Triggered when first reading received                            |
|                                                                       |
|    CPT 99454 (Device supply + data transmission):                     |
|    - Requires >= 16 days of data transmission per 30-day period       |
|    - Track: transmission_days >= 16 → BILLABLE                        |
|    - Reimbursement: ~$52/month                                        |
|                                                                       |
|    CPT 99457 (RPM treatment management, first 20 min):                |
|    - Requires >= 20 minutes clinician interactive time per month       |
|    - Track: SUM(clinician_time_entries) >= 20 min → BILLABLE          |
|    - Reimbursement: ~$52/month                                        |
|                                                                       |
|    CPT 99458 (Additional 20-min increments):                          |
|    - Each additional 20-min block beyond 99457                        |
|    - Track: (total_time - 20) / 20 = additional billable units        |
|    - Reimbursement: ~$42/unit                                         |
|                                                                       |
|    CPT 99490 (CCM, 20 min clinical staff time):                       |
|    - Requires >= 20 min clinical staff time for CCM activities        |
|    - Separate from RPM time tracking                                  |
|    - Reimbursement: ~$64/month                                        |
|                                                                       |
|    CPT 99445 (2-15 day RPM -- NEW 2026):                              |
|    - For patients with 2-15 transmission days (below 99454 threshold) |
|    - Enables partial-month billing                                    |
|    - MUTUALLY EXCLUSIVE with 99454                                    |
|                                                                       |
|    CPT 99470 (Abbreviated RPM interaction -- NEW 2026):               |
|    - For shorter clinician interactions (< 20 min)                    |
|    - MUTUALLY EXCLUSIVE with 99457                                    |
|                                                                       |
| 3. APPLY mutual exclusivity rules:                                    |
|    - 99454 XOR 99445 (cannot bill both same period)                   |
|    - 99457 XOR 99470 (cannot bill both same period)                   |
|    - Maximize: prefer higher-value code when threshold met             |
|                                                                       |
| 4. GENERATE billing events:                                           |
|    INSERT INTO billing_events (patient_id, cpt_code, period,          |
|      amount, status, evidence_json, generated_at)                     |
|    Status: 'pending_review' → clinic billing staff reviews →          |
|            'approved' → submitted to clearinghouse                     |
|                                                                       |
| 5. CONSENT verification:                                              |
|    - Check patient_consents table for active RPM + Medicare consent    |
|    - Block billing event generation if consent expired or missing      |
+----------------------------------------------------------------------+
```

---

## 4. DATABASE SCHEMA (Aim 3)

### 4.1 Core Data Model

```sql
-- ============================================================
-- 3C PLATFORM DATABASE SCHEMA (PostgreSQL 16)
-- FHIR R4-aligned, multi-tenant with row-level security
-- ============================================================

-- Clinic tenant table
CREATE TABLE clinics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    npi TEXT UNIQUE,
    address JSONB,
    ehr_system TEXT,  -- 'eclinicalworks', 'athenahealth', 'meditech', 'azalea'
    modules_enabled TEXT[] DEFAULT '{"compliance"}',
    tier TEXT DEFAULT 'essentials',  -- 'essentials', 'professional', 'enterprise'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Patient table (FHIR Patient resource aligned)
CREATE TABLE patients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    mrn TEXT,  -- medical record number (clinic-specific)
    fhir_id TEXT,  -- FHIR resource ID from EHR
    given_name TEXT,
    family_name TEXT,
    birth_date DATE,
    gender TEXT,
    address JSONB,
    phone TEXT,
    email TEXT,
    insurance JSONB,  -- payer information
    risk_score INTEGER,  -- latest risk stratification score (0-100)
    risk_stratum TEXT,  -- 'LOW', 'MEDIUM', 'HIGH'
    rpm_enrolled BOOLEAN DEFAULT FALSE,
    ccm_enrolled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- RPM/clinical observations (FHIR Observation resource aligned)
CREATE TABLE observations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    fhir_id TEXT,
    category TEXT NOT NULL,  -- 'vital-signs', 'laboratory', 'survey'
    code TEXT NOT NULL,  -- LOINC code
    code_display TEXT,  -- human-readable name
    value_quantity DECIMAL,
    value_unit TEXT,
    value_string TEXT,
    effective_dt TIMESTAMPTZ NOT NULL,
    device_sourced BOOLEAN DEFAULT FALSE,  -- TRUE = RPM device
    device_id TEXT,
    vendor TEXT,  -- 'tenovi', 'smart_meter', 'ehr'
    status TEXT DEFAULT 'final',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Conditions (FHIR Condition resource aligned)
CREATE TABLE conditions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    fhir_id TEXT,
    code TEXT NOT NULL,  -- ICD-10 code
    code_display TEXT,
    clinical_status TEXT,  -- 'active', 'resolved', 'inactive'
    onset_dt DATE,
    recorded_dt DATE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Encounters (FHIR Encounter resource aligned)
CREATE TABLE encounters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    fhir_id TEXT,
    encounter_type TEXT,  -- 'ambulatory', 'emergency', 'inpatient'
    status TEXT,
    period_start TIMESTAMPTZ,
    period_end TIMESTAMPTZ,
    provider_id UUID,
    reason_code TEXT,  -- primary reason ICD-10
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Billing events (platform-generated)
CREATE TABLE billing_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    cpt_code TEXT NOT NULL,
    billing_period_start DATE NOT NULL,
    billing_period_end DATE NOT NULL,
    amount_expected DECIMAL,
    transmission_days INTEGER,  -- for 99454/99445
    clinician_minutes INTEGER,  -- for 99457/99458/99470
    status TEXT DEFAULT 'pending_review',
    -- 'pending_review', 'approved', 'submitted', 'paid', 'denied'
    evidence JSONB,  -- supporting data for audit trail
    reviewed_by UUID,
    reviewed_at TIMESTAMPTZ,
    submitted_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Compliance tasks (platform-generated)
CREATE TABLE compliance_tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    task_type TEXT NOT NULL,
    -- 'hipaa_risk_assessment', 'hipaa_training', 'ehr_audit',
    -- 'hrsa_uds_report', 'cms_quality_submission', 'fcc_broadband'
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    regulatory_body TEXT,  -- 'hipaa', 'hrsa', 'cms', 'fcc'
    status TEXT DEFAULT 'pending',
    -- 'pending', 'in_progress', 'completed', 'overdue'
    assigned_to UUID,
    completed_at TIMESTAMPTZ,
    evidence_url TEXT,
    risk_level TEXT,  -- 'low', 'medium', 'high', 'critical'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Patient consents (required for RPM billing)
CREATE TABLE patient_consents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    consent_type TEXT NOT NULL,
    -- 'rpm_clinical', 'rpm_medicare', 'ccm_clinical', 'research'
    status TEXT DEFAULT 'active',  -- 'active', 'revoked', 'expired'
    obtained_date DATE NOT NULL,
    expiry_date DATE,
    obtained_by UUID,
    revoked_date DATE,
    document_url TEXT,  -- stored consent form
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Risk stratification results
CREATE TABLE risk_scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    model_version TEXT NOT NULL,
    prediction_horizon TEXT NOT NULL,  -- '30_day', '60_day', '90_day'
    risk_score INTEGER NOT NULL,  -- 0-100
    risk_stratum TEXT NOT NULL,  -- 'LOW', 'MEDIUM', 'HIGH'
    confidence_lower INTEGER,
    confidence_upper INTEGER,
    shap_values JSONB,  -- top contributing factors
    features_used JSONB,  -- input feature values (de-identifiable)
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Audit log (HIPAA compliance)
CREATE TABLE audit_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID,
    user_id UUID,
    action TEXT NOT NULL,  -- 'read', 'create', 'update', 'delete', 'export'
    resource_type TEXT NOT NULL,  -- 'patient', 'observation', 'billing_event', etc.
    resource_id UUID,
    details JSONB,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Device transmission tracking (for billing threshold calculation)
CREATE TABLE device_transmissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    transmission_date DATE NOT NULL,
    device_type TEXT NOT NULL,
    reading_count INTEGER DEFAULT 1,
    UNIQUE (clinic_id, patient_id, transmission_date, device_type)
);

-- Clinician time tracking (for billing threshold calculation)
CREATE TABLE clinician_time_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id UUID NOT NULL REFERENCES clinics(id),
    patient_id UUID NOT NULL REFERENCES patients(id),
    clinician_id UUID NOT NULL,
    service_type TEXT NOT NULL,  -- 'rpm', 'ccm'
    duration_minutes INTEGER NOT NULL,
    activity_description TEXT,
    entry_date DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 4.2 Row-Level Security (Multi-Tenant Isolation)

```sql
-- Enable RLS on all PHI-containing tables
ALTER TABLE patients ENABLE ROW LEVEL SECURITY;
ALTER TABLE observations ENABLE ROW LEVEL SECURITY;
ALTER TABLE conditions ENABLE ROW LEVEL SECURITY;
ALTER TABLE encounters ENABLE ROW LEVEL SECURITY;
ALTER TABLE billing_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE compliance_tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE patient_consents ENABLE ROW LEVEL SECURITY;
ALTER TABLE risk_scores ENABLE ROW LEVEL SECURITY;

-- RLS policy: users can only access their clinic's data
-- Application sets current_setting('app.current_clinic_id') on each connection
CREATE POLICY clinic_isolation ON patients
    FOR ALL
    USING (clinic_id = current_setting('app.current_clinic_id')::UUID);

-- Same policy applied to all tables (shown for patients as example)
-- Repeated for: observations, conditions, encounters, billing_events,
--               compliance_tasks, patient_consents, risk_scores

-- Research role can access de-identified views only
CREATE ROLE research_analyst;
GRANT SELECT ON research_deidentified_patients TO research_analyst;
GRANT SELECT ON research_deidentified_observations TO research_analyst;
```

### 4.3 Cross-Domain Materialized Views (Aim 3)

```sql
-- Cross-domain view: Compliance documentation ↔ Claims denial rate
CREATE MATERIALIZED VIEW xd_compliance_claims AS
SELECT
    c.clinic_id,
    DATE_TRUNC('month', be.billing_period_start) AS billing_month,
    COUNT(DISTINCT ct.id) FILTER (WHERE ct.status = 'completed')::FLOAT /
        NULLIF(COUNT(DISTINCT ct.id), 0) AS compliance_completion_rate,
    COUNT(DISTINCT be.id) FILTER (WHERE be.status = 'denied')::FLOAT /
        NULLIF(COUNT(DISTINCT be.id), 0) AS claims_denial_rate,
    COUNT(DISTINCT be.id) AS total_claims,
    SUM(be.amount_expected) FILTER (WHERE be.status = 'paid') AS revenue_collected
FROM clinics c
LEFT JOIN compliance_tasks ct ON ct.clinic_id = c.id
LEFT JOIN billing_events be ON be.clinic_id = c.id
    AND DATE_TRUNC('month', be.billing_period_start) = DATE_TRUNC('month', ct.due_date)
GROUP BY c.clinic_id, DATE_TRUNC('month', be.billing_period_start);

-- Cross-domain view: RPM device adherence ↔ Clinical outcomes
CREATE MATERIALIZED VIEW xd_rpm_outcomes AS
SELECT
    p.clinic_id,
    p.id AS patient_id,
    DATE_TRUNC('month', dt.transmission_date) AS month,
    COUNT(DISTINCT dt.transmission_date) AS transmission_days,
    COUNT(DISTINCT e.id) FILTER (WHERE e.encounter_type = 'emergency') AS ed_visits,
    COUNT(DISTINCT e.id) FILTER (WHERE e.encounter_type = 'inpatient') AS hospitalizations,
    rs.risk_score AS latest_risk_score
FROM patients p
LEFT JOIN device_transmissions dt ON dt.patient_id = p.id
LEFT JOIN encounters e ON e.patient_id = p.id
    AND DATE_TRUNC('month', e.period_start) = DATE_TRUNC('month', dt.transmission_date)
LEFT JOIN LATERAL (
    SELECT risk_score FROM risk_scores
    WHERE patient_id = p.id
    ORDER BY created_at DESC LIMIT 1
) rs ON TRUE
WHERE p.rpm_enrolled = TRUE
GROUP BY p.clinic_id, p.id, DATE_TRUNC('month', dt.transmission_date), rs.risk_score;

-- Cross-domain view: MIPS quality ↔ Reimbursement trends
CREATE MATERIALIZED VIEW xd_mips_revenue AS
SELECT
    c.clinic_id,
    DATE_TRUNC('quarter', be.billing_period_start) AS quarter,
    SUM(be.amount_expected) FILTER (WHERE be.status = 'paid') AS quarterly_revenue,
    AVG(be.amount_expected) FILTER (WHERE be.status = 'paid') AS avg_claim_amount,
    COUNT(DISTINCT ct.id) FILTER (
        WHERE ct.task_type LIKE 'cms_quality%' AND ct.status = 'completed'
    )::FLOAT / NULLIF(COUNT(DISTINCT ct.id) FILTER (
        WHERE ct.task_type LIKE 'cms_quality%'
    ), 0) AS quality_completion_rate
FROM clinics c
LEFT JOIN billing_events be ON be.clinic_id = c.id
LEFT JOIN compliance_tasks ct ON ct.clinic_id = c.id
    AND DATE_TRUNC('quarter', ct.due_date) = DATE_TRUNC('quarter', be.billing_period_start)
GROUP BY c.clinic_id, DATE_TRUNC('quarter', be.billing_period_start);

-- Refresh materialized views nightly
-- (n8n scheduled workflow triggers: REFRESH MATERIALIZED VIEW CONCURRENTLY)
```

---

## 5. SECURITY ARCHITECTURE

### 5.1 Defense-in-Depth Security Model

```
+------------------------------------------------------------------+
|  LAYER 1: Network Security                                        |
|  - Amazon GovCloud VPC with private subnets                       |
|  - Security groups: least-privilege port access                   |
|  - WAF (Web Application Firewall) on ALB                         |
|  - VPC Flow Logs → CloudWatch → anomaly detection                 |
+------------------------------------------------------------------+
|  LAYER 2: Transport Security                                      |
|  - TLS 1.2+ on all connections (NGINX reverse proxy)              |
|  - HSTS (HTTP Strict Transport Security)                          |
|  - Certificate pinning for EHR/device vendor connections          |
|  - mTLS for inter-service communication (future)                  |
+------------------------------------------------------------------+
|  LAYER 3: Application Security                                    |
|  - OAuth 2.0 / OIDC authentication                               |
|  - Role-based access control (RBAC)                               |
|  - Input validation on all API endpoints                          |
|  - CSRF, XSS, SQL injection protections                           |
|  - Content Security Policy (CSP) headers                          |
|  - Rate limiting per user/clinic                                  |
+------------------------------------------------------------------+
|  LAYER 4: Data Security                                           |
|  - AES-256 encryption at rest (AWS KMS, customer-managed keys)    |
|  - PostgreSQL row-level security (clinic isolation)               |
|  - Application-level field encryption for sensitive PHI           |
|  - PGAudit for complete query audit trail                         |
|  - Data masking in non-production environments                    |
+------------------------------------------------------------------+
|  LAYER 5: Monitoring and Response                                 |
|  - CloudTrail for all AWS API activity                            |
|  - CloudWatch Logs + alarms for anomalies                         |
|  - Application audit log for all PHI access                       |
|  - Automated alerting for suspicious access patterns              |
|  - Incident response plan (1-hour SLA for critical events)        |
+------------------------------------------------------------------+
```

### 5.2 HIPAA Security Rule Mapping

| HIPAA Requirement | Implementation | Verification |
|---|---|---|
| **Access Controls (§164.312(a))** | PostgreSQL RLS, application RBAC, OAuth 2.0 | RLS unit tests; access control matrix |
| **Audit Controls (§164.312(b))** | PGAudit, CloudTrail, application audit log | Monthly audit log review; automated alerts |
| **Integrity Controls (§164.312(c))** | AES-256 encryption, checksums, version control | Integrity verification scripts |
| **Transmission Security (§164.312(e))** | TLS 1.2+, HSTS, certificate management | SSL Labs scan (A+ target) |
| **Authentication (§164.312(d))** | OAuth 2.0, MFA for admin access, session management | Penetration testing; MFA enforcement |
| **Encryption (§164.312(a)(2)(iv))** | AES-256 at rest (KMS), TLS 1.2+ in transit, field-level encryption for SSN/DOB | Encryption audit; key rotation schedule |
| **Emergency Access (§164.312(a)(2)(ii))** | Break-glass procedure documented; dual-authorization for emergency PHI access | Annual drill; access log review |
| **Automatic Logoff (§164.312(a)(2)(iii))** | 15-minute session timeout; re-authentication for sensitive actions | Session management tests |
| **Risk Assessment (§164.308(a)(1))** | Annual HIPAA Security Risk Assessment per NIST SP 800-66 | Assessment report on file |
| **Workforce Training (§164.308(a)(5))** | HIPAA training for all team members; annual refresher | Training completion records |

### 5.3 Encryption Key Management

```
AWS KMS (GovCloud)
+---------------------------------------------+
| Customer-Managed Key (CMK)                    |
| - Algorithm: AES-256-GCM                      |
| - Key rotation: Annual (automatic)            |
| - Key policy: restrict to platform IAM roles  |
|                                               |
| Data Keys (generated per use):                |
| - RDS encryption: automatic via KMS           |
| - S3 encryption: SSE-KMS                      |
| - EBS encryption: automatic via KMS           |
| - Application field encryption: envelope      |
|   encryption (KMS wraps data key)             |
+---------------------------------------------+

Application-Level Field Encryption:
+---------------------------------------------+
| Fields encrypted at application layer:        |
| - SSN (Social Security Number)                |
| - Full name (when stored outside Patient)     |
| - Date of birth (exact)                       |
| - Phone number                                |
| - Email address                               |
| - Insurance member ID                         |
|                                               |
| Method: AES-256-GCM via AWS KMS envelope      |
| encryption (data key cached in memory,        |
| wrapped key stored alongside ciphertext)       |
+---------------------------------------------+
```

---

## 6. API REFERENCE

### 6.1 FastAPI Service Endpoints

#### Risk Stratification API

```
POST /api/v1/risk/score
Authorization: Bearer {token}
Content-Type: application/json
X-Clinic-ID: {clinic_uuid}

Request:
{
    "patient_id": "uuid",
    "prediction_horizon": "30_day"  // "30_day", "60_day", "90_day"
}

Response (200):
{
    "patient_id": "uuid",
    "risk_score": 78,
    "risk_stratum": "HIGH",
    "prediction_horizon": "30_day",
    "confidence_interval": [72, 84],
    "top_contributing_factors": [
        {
            "feature": "ed_visits_6mo",
            "value": 3,
            "shap_value": 0.24,
            "direction": "increases_risk",
            "display": "3 ED visits in past 6 months"
        }
    ],
    "model_version": "v1.2.0",
    "computed_at": "2026-10-15T14:30:00Z"
}
```

#### Batch Risk Scoring API

```
POST /api/v1/risk/batch
Authorization: Bearer {token}
X-Clinic-ID: {clinic_uuid}

Request:
{
    "patient_ids": ["uuid1", "uuid2", ...],
    "prediction_horizon": "30_day"
}

Response (202 Accepted):
{
    "job_id": "uuid",
    "status": "processing",
    "patient_count": 150,
    "estimated_completion": "2026-10-15T14:35:00Z"
}
```

#### RPM Data Ingestion API

```
POST /api/v1/rpm/reading
Authorization: Bearer {token}
X-Clinic-ID: {clinic_uuid}

Request:
{
    "patient_id": "uuid",
    "device_type": "blood_pressure",
    "vendor": "tenovi",
    "readings": [
        {
            "timestamp": "2026-10-15T08:00:00Z",
            "systolic": 142,
            "diastolic": 88,
            "pulse": 72,
            "device_id": "TEN-12345"
        }
    ]
}

Response (201):
{
    "readings_accepted": 1,
    "readings_rejected": 0,
    "alerts_generated": 0,
    "transmission_day_recorded": true,
    "billing_status": {
        "99454_days_this_period": 12,
        "99454_threshold": 16,
        "days_remaining_to_threshold": 4
    }
}
```

#### Billing Events API

```
GET /api/v1/billing/events?period=2026-10&status=pending_review
Authorization: Bearer {token}
X-Clinic-ID: {clinic_uuid}

Response (200):
{
    "billing_events": [
        {
            "id": "uuid",
            "patient_id": "uuid",
            "patient_name": "John D.",
            "cpt_code": "99454",
            "period": "2026-10-01/2026-10-31",
            "amount_expected": 52.00,
            "transmission_days": 18,
            "status": "pending_review",
            "evidence": {
                "transmission_dates": ["2026-10-01", "2026-10-02", ...],
                "device_types": ["blood_pressure", "weight_scale"],
                "total_readings": 54
            }
        }
    ],
    "summary": {
        "total_pending": 45,
        "total_expected_revenue": 5840.00
    }
}
```

#### Cross-Domain Analytics API

```
GET /api/v1/analytics/cross-domain?view=compliance_claims&period=2026-Q4
Authorization: Bearer {token}
X-Clinic-ID: {clinic_uuid}

Response (200):
{
    "view": "compliance_claims",
    "period": "2026-Q4",
    "data": {
        "compliance_completion_rate": 0.87,
        "claims_denial_rate": 0.03,
        "correlation_coefficient": -0.72,
        "p_value": 0.003,
        "interpretation": "Higher compliance task completion is significantly associated with lower claims denial rate"
    }
}
```

### 6.2 n8n Workflow Templates

| Workflow | Trigger | Schedule | Description |
|---|---|---|---|
| **RPM Device Poll** | Cron | Every 15 min | Poll Tenovi API, ingest readings, evaluate alerts |
| **EHR Full Sync** | Cron | Daily 2:00 AM | Full FHIR resource sync from clinic EHR |
| **EHR Incremental Sync** | Cron | Every 2 hours | Sync only resources updated since last sync |
| **Billing Threshold Check** | Cron | Daily 6:00 AM | Evaluate all patients against billing thresholds |
| **Compliance Task Generator** | Cron | Weekly Monday 8:00 AM | Generate upcoming compliance tasks from regulatory calendar |
| **Alert Router** | Webhook | On alert | Route clinical alerts to appropriate provider via email/SMS/dashboard |
| **Risk Score Batch** | Cron | Weekly Sunday 2:00 AM | Re-score all active patients with latest data |
| **MV Refresh** | Cron | Daily 3:00 AM | Refresh cross-domain materialized views |
| **Audit Report** | Cron | Monthly 1st 6:00 AM | Generate monthly audit report for compliance review |
| **Data Quality Check** | Cron | Daily 4:00 AM | Validate data completeness, duplicates, anomalies |

---

## 7. DEPLOYMENT AND INFRASTRUCTURE

### 7.1 GovCloud Infrastructure (Terraform)

```
Amazon GovCloud (US-East)
+------------------------------------------------------------------+
|  VPC: 10.0.0.0/16                                                 |
|                                                                   |
|  +-------------------+  +-------------------+                     |
|  | Public Subnet A   |  | Public Subnet B   |                     |
|  | (us-gov-east-1a)  |  | (us-gov-east-1b)  |                     |
|  |                   |  |                   |                     |
|  | [ALB]             |  |                   |                     |
|  | [NAT Gateway]     |  | [NAT Gateway]     |                     |
|  +-------------------+  +-------------------+                     |
|                                                                   |
|  +-------------------+  +-------------------+                     |
|  | Private Subnet A  |  | Private Subnet B  |                     |
|  |                   |  |                   |                     |
|  | [ECS Fargate]     |  | [ECS Fargate]     |                     |
|  | - n8n             |  | - n8n (standby)   |                     |
|  | - FastAPI         |  | - FastAPI         |                     |
|  | - Next.js         |  | - Next.js         |                     |
|  | - NGINX           |  | - NGINX           |                     |
|  +-------------------+  +-------------------+                     |
|                                                                   |
|  +-------------------+  +-------------------+                     |
|  | Data Subnet A     |  | Data Subnet B     |                     |
|  |                   |  |                   |                     |
|  | [RDS PostgreSQL   |  | [RDS PostgreSQL   |                     |
|  |  Primary]         |  |  Standby]         |                     |
|  +-------------------+  +-------------------+                     |
|                                                                   |
|  Shared Services:                                                  |
|  - S3 (document storage, backups, ML artifacts)                    |
|  - KMS (encryption keys)                                           |
|  - CloudTrail (audit)                                              |
|  - CloudWatch (monitoring, alarms)                                 |
|  - ECR (container registry)                                        |
|  - Secrets Manager (credentials)                                   |
+------------------------------------------------------------------+
```

### 7.2 Container Architecture

```yaml
# Docker Compose (development) / ECS Task Definitions (production)
services:
  nginx:
    image: nginx:alpine
    ports: ["443:443"]
    # TLS termination, reverse proxy, rate limiting

  n8n:
    image: n8nio/n8n:latest
    # Workflow automation engine
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - EXECUTIONS_MODE=queue
      - QUEUE_BULL_REDIS_HOST=redis

  fastapi:
    image: ${ECR_REPO}/3c-api:latest
    # ML model serving, RPM ingestion, FHIR transforms
    environment:
      - DATABASE_URL=postgresql://...
      - MODEL_PATH=/models/risk_v1.2.0
      - SHAP_ENABLED=true

  nextjs:
    image: ${ECR_REPO}/3c-dashboard:latest
    # Clinic-facing React dashboard
    environment:
      - API_BASE_URL=https://api.3cplatform.health

  postgres:
    image: postgres:16
    # Only for development; production uses RDS
    volumes: ["pgdata:/var/lib/postgresql/data"]

  redis:
    image: redis:7-alpine
    # n8n job queue, session cache
```

### 7.3 Monitoring and Observability

| Component | Tool | Metrics |
|---|---|---|
| **Infrastructure** | CloudWatch | CPU, memory, disk, network, RDS connections, ECS task health |
| **Application** | CloudWatch Logs + custom metrics | Request latency, error rates, RPM ingestion rate, billing events/day |
| **Database** | RDS Performance Insights + PGAudit | Query performance, connection count, RLS enforcement, audit trail |
| **Security** | CloudTrail + GuardDuty | API calls, IAM activity, anomalous access patterns |
| **ML Model** | Custom dashboard (React) | AUC-ROC drift, prediction distribution shift, feature importance stability |
| **Uptime** | CloudWatch Synthetics | Endpoint availability, SSL certificate expiry, EHR connectivity |
| **Alerts** | CloudWatch Alarms → SNS → PagerDuty | Critical: system down, PHI breach. High: degraded performance. Medium: anomalies |

---

## 8. EHR INTEGRATION SPECIFICATIONS

### 8.1 Supported EHR Systems

| EHR | Market Position | FHIR R4 Support | Phase | Integration Method |
|---|---|---|---|---|
| **eClinicalWorks** | Largest cloud ambulatory (850K+ providers) | Full FHIR R4 API | **Phase I** | bonFHIR + OAuth 2.0 |
| **athenahealth** | Strong in independent practices | Full FHIR R4 API | **Phase I** | bonFHIR + OAuth 2.0 |
| **MEDITECH** | Strong in rural/community hospitals | FHIR R4 (Expanse) | Phase II | bonFHIR + OAuth 2.0 |
| **Azalea Health** | Purpose-built for rural clinics | FHIR R4 (growing) | Phase II | HTTP Request + API key |
| **TruBridge** | Rural hospital focus | FHIR R4 (limited) | Phase II | CSV fallback + API |

### 8.2 FHIR R4 Resource Mapping

| FHIR Resource | Platform Table | Sync Direction | Frequency |
|---|---|---|---|
| Patient | patients | EHR → Platform | Nightly + incremental |
| Condition | conditions | EHR → Platform | Nightly + incremental |
| Encounter | encounters | EHR → Platform | Nightly + incremental |
| Observation (labs/vitals) | observations | EHR → Platform | Nightly + incremental |
| Observation (RPM) | observations | Platform → EHR (future) | On creation |
| MedicationRequest | *(Phase II table)* | EHR → Platform | Nightly |
| AllergyIntolerance | *(Phase II table)* | EHR → Platform | Nightly |
| DiagnosticReport | *(Phase II table)* | EHR → Platform | Nightly |

### 8.3 FHIR Authentication Flow

```
1. Platform registers as SMART on FHIR application with EHR vendor
2. Clinic administrator authorizes platform access (one-time):
   - OAuth 2.0 Authorization Code flow
   - Scopes: patient/*.read, observation/*.read, condition/*.read
3. Platform stores refresh_token in AWS Secrets Manager (encrypted)
4. n8n workflows use refresh_token to obtain access_token per sync
5. Access tokens expire in 15 minutes; auto-refresh on 401 response
6. All FHIR API calls logged in audit_log table
```

---

## 9. RPM DEVICE SPECIFICATIONS

### 9.1 Supported Devices (via Tenovi API)

| Device Type | Clinical Use | LOINC Code | Alert Thresholds (Default) | CMS Billing Relevance |
|---|---|---|---|---|
| **Blood Pressure Cuff** | Hypertension, CHF, CKD | 85354-9 | Systolic > 180 (urgent), > 140 (high); Diastolic > 120 (urgent), > 90 (high) | 99454 transmission day |
| **Blood Glucose Monitor** | Diabetes (Type 1, 2) | 2345-7 | > 400 mg/dL (urgent), > 250 (high), < 70 (high) | 99454 transmission day |
| **Pulse Oximeter** | COPD, CHF, respiratory | 2708-6 | < 90% (urgent), < 93% (high) | 99454 transmission day |
| **Weight Scale** | CHF, obesity management | 29463-7 | > 3 lbs/day gain (high, CHF); trending per sliding window | 99454 transmission day |
| **Thermometer** | Post-surgical, infection | 8310-5 | > 101.3°F (high), > 103°F (urgent) | 99454 transmission day |

### 9.2 Cellular Connectivity

All RPM devices use **cellular connectivity** (Tenovi's built-in cellular modem or Smart Meter's cellular gateway):

- **No WiFi required:** Critical for rural patients without reliable broadband
- **Automatic transmission:** Patient takes reading; device transmits automatically via cellular
- **Coverage:** Tenovi uses multi-carrier cellular (AT&T, T-Mobile, Verizon) for rural coverage
- **Battery life:** 6--12 months typical (device-dependent)
- **Patient setup:** Zero configuration required; devices pre-provisioned at factory

---

## 10. GLOSSARY

| Term | Definition |
|---|---|
| **3C Platform** | Compliance, Care, Collect Cash -- the integrated healthcare platform |
| **ACT** | Authentic Consortium -- the entity that owns all platform IP |
| **AUC-ROC** | Area Under the Receiver Operating Characteristic Curve -- model performance metric |
| **bonFHIR** | Open-source FHIR integration library providing n8n nodes for FHIR R4 |
| **CCM** | Chronic Care Management -- CMS program (CPT 99490) |
| **CDS** | Clinical Decision Support -- software that assists clinical decision-making |
| **CMS** | Centers for Medicare & Medicaid Services |
| **CPT** | Current Procedural Terminology -- medical billing codes |
| **ECS Fargate** | AWS Elastic Container Service (serverless container hosting) |
| **EHR** | Electronic Health Record |
| **FedRAMP** | Federal Risk and Authorization Management Program |
| **FHIR R4** | HL7 Fast Healthcare Interoperability Resources, Release 4 |
| **FQHC** | Federally Qualified Health Center |
| **HIPAA** | Health Insurance Portability and Accountability Act |
| **HRSA** | Health Resources and Services Administration |
| **ICD-10** | International Classification of Diseases, 10th Revision |
| **KMS** | AWS Key Management Service |
| **LOINC** | Logical Observation Identifiers Names and Codes |
| **MIPS** | Merit-based Incentive Payment System |
| **n8n** | Open-source workflow automation engine |
| **NPI** | National Provider Identifier |
| **PGAudit** | PostgreSQL extension for detailed audit logging |
| **PHI** | Protected Health Information |
| **RDS** | Amazon Relational Database Service |
| **RHC** | Rural Health Clinic |
| **RLS** | Row-Level Security (PostgreSQL feature) |
| **RPM** | Remote Patient Monitoring |
| **SHAP** | SHapley Additive exPlanations -- model interpretability framework |
| **SVI** | Social Vulnerability Index (CDC) |
| **UDS** | Uniform Data System (HRSA reporting) |
| **VV** | Veteran Vectors -- the technical development team |
| **XGBoost** | Extreme Gradient Boosting -- machine learning algorithm |

---

*Prepared by: Authentic Consortium / Veteran Vectors Engineering*
*Version 1.0 -- February 25, 2026*
