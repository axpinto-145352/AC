# PEER REVIEW: NIH SBIR Phase I Technical Guide (03_NIH_Technical_Guide.md)

**Reviewer Role:** Healthcare IT Architect / NIH Technical Reviewer
**Document Reviewed:** NIH SBIR Phase I -- Technical Guide, Version 1.0, February 25, 2026
**Cross-Referenced Against:**
- `01_VV_Technical_Brief.md` (VIPC VVP Launch Grant technical brief)
- `02_Implementation_Guide.md` (3C Platform implementation guide)

**Review Date:** February 25, 2026

---

## 1. TECHNICAL ARCHITECTURE ASSESSMENT

### Platform Stack Evaluation

The 3C Platform stack (n8n, PostgreSQL 16, Python/FastAPI, React/Next.js, NGINX, Docker on Amazon GovCloud) represents a sound, defensible set of technology choices for a Phase I SBIR. The open-source-first approach eliminates licensing cost as a scaling bottleneck and directly supports the stated design principle of zero vendor lock-in.

**Design Principle Alignment:**

| Principle | Assessment |
|---|---|
| Open-source first | **Strong.** Every core component is open-source or open-standard. No proprietary runtime dependencies. |
| GovCloud-native | **Strong.** FedRAMP High authorization exceeds the FedRAMP Moderate baseline typical of commercial healthcare SaaS. This is a genuine differentiator for NIH reviewers accustomed to seeing HIPAA-only compliance claims. |
| Configuration-driven multi-tenancy | **Good but needs stress-testing detail.** The feature-flag/template-workflow approach is well-articulated, but the guide does not address how conflicting configurations across tenants are validated, nor does it describe a configuration schema versioning strategy. |
| FHIR-native | **Good.** FHIR R4 alignment across the data model and integration layer is appropriate. However, the document should clarify which US Core profiles are mandatory and how profile validation is performed. |
| Explainable AI | **Strong.** SHAP integration at the architectural level (not bolted on) is the right design choice for clinical decision support. |
| Rural-first design | **Good.** Cellular-first RPM device connectivity is well-reasoned. The asynchronous sync pattern for unreliable broadband is mentioned but not technically detailed (e.g., conflict resolution during offline periods, queue-and-forward mechanisms). |

**Scalability Concerns:**

The architecture is well-suited for Phase I (2-3 clinics, ~200 patients), but the Technical Guide should explicitly address the scaling inflection points:

- **n8n Community Edition** runs in single mode (not queue mode). The guide cites 15-23 req/s capacity, but this is for the n8n web UI/API, not necessarily for workflow execution throughput under concurrent trigger conditions. For an NIH reviewer, a more rigorous throughput analysis under realistic concurrent workflow scenarios (e.g., 200 patients x 15-min RPM polling + hourly EHR sync + nightly billing batch) would strengthen the case.
- **PostgreSQL RDS** scaling path from single-AZ pilot to Multi-AZ production is mentioned in the Implementation Guide but not in this Technical Guide. The Technical Guide should include the HA/DR strategy.
- **ECS Fargate** auto-scaling policies, task placement constraints, and container resource limits are not specified. For a technical guide, this level of detail is expected.

### Architecture Diagram Quality

The system context diagram (Section 1.2) is clear and well-structured, showing the flow from external systems through the workflow engine, API layer, database, and frontend. However, it places the "3C PLATFORM (Amazon GovCloud)" label at the bottom, after the dashboard layer, which creates visual confusion -- the label should wrap or precede the internal components.

---

## 2. AI/ML METHODOLOGY REVIEW

### Model Architecture (Section 2.1.1)

**XGBoost as the primary model** is an appropriate and defensible choice for structured tabular data in healthcare risk prediction. The specific hyperparameter set (500 trees, max_depth 6, learning_rate 0.05, subsample/colsample at 0.8, min_child_weight 5, regularization terms) reflects thoughtful initial configuration that balances model capacity with overfitting risk.

**Strengths:**
- The logistic regression baseline provides a direct interpretability comparison, which is best practice in health services research.
- The 50+ feature set spanning demographics, diagnosis history, utilization patterns, labs, medications, and social determinants is comprehensive and clinically meaningful.
- MICE imputation for missing values is appropriate for healthcare data with systematic missingness patterns.
- Robust scaler (instead of standard scaler) is the right choice given the prevalence of outliers in clinical data.

**Concerns:**

1. **Training data provenance is underspecified.** The guide mentions "CMS Public Use Files" and "Pilot Clinic EHR Data" but does not enumerate the specific CMS datasets (e.g., Medicare Provider Utilization & Payment Data, CMS Chronic Conditions Data Warehouse, Hospital Readmissions Reduction Program data). NIH reviewers will want to see exact dataset names, years, sample sizes, and the inclusion/exclusion criteria for the training cohort.

2. **The training/validation split strategy has a temporal inconsistency.** The guide states "CMS Data: 5-fold stratified cross-validation" and "Pilot Data: Temporal split (train on months 1-6, validate on months 7-9)." However, Phase I is only 9 months long. If the pilot doesn't launch until Month 4-5, the platform would have at most 4-5 months of pilot data by the end of Phase I, making a "months 1-6 train / months 7-9 validate" split infeasible within the Phase I timeline. The CMS data cross-validation can begin immediately, but the pilot data validation timeline needs to be reconciled with the actual study timeline.

3. **Label definition needs more rigor.** "30/60/90-day hospitalization or ED visit" is stated as the outcome variable, but the guide does not specify: (a) whether these are all-cause or condition-specific events, (b) how observation stays vs. full admissions are classified, (c) how ED visits that result in inpatient admission are counted (double-counted or deduplicated), or (d) the expected event rate (base rate) in the target population. The base rate is critical for interpreting AUC-ROC and setting the PPV target.

4. **Class imbalance handling is not addressed.** Rural Medicare populations typically have 10-15% annual hospitalization rates, meaning the 30-day event rate may be 3-5%. The guide does not mention how class imbalance will be handled (e.g., SMOTE, class weighting in XGBoost's `scale_pos_weight`, threshold optimization). This is a significant omission.

5. **Confidence intervals via bootstrap are mentioned** (line 225) but not detailed. The number of bootstrap iterations, the bootstrap methodology (percentile vs. BCa), and the confidence level (presumably 95%) should be specified.

### Evaluation Framework (Section 2.1.3)

The evaluation metrics table is comprehensive and includes the right metrics for clinical ML:

- **AUC-ROC > 0.75** is a reasonable Phase I target for a risk stratification model, consistent with published literature (e.g., LACE index typically achieves 0.68-0.72, HOSPITAL score 0.65-0.72).
- **Sensitivity > 80% for top decile** is appropriate for a screening tool where missing high-risk patients is the primary harm.
- **AUC-PR reported** (not targeted) is the right approach given that AUC-PR is sensitive to class imbalance and the baseline will vary.
- **Brier score < 0.15** is a reasonable calibration target.

**Missing elements:**
- **Net Reclassification Improvement (NRI)** or **Integrated Discrimination Improvement (IDI)** against existing clinical risk scores (e.g., LACE, HOSPITAL) should be included to demonstrate incremental value.
- **Decision curve analysis** should be mentioned as a secondary evaluation to demonstrate net benefit at clinically relevant threshold probabilities.
- **External validation plan.** The guide implies the model will be trained on CMS data and validated on pilot data, but this should be explicitly framed as external validation with expected domain shift acknowledgment.

### Fairness Metrics (Section 2.1.3)

The fairness framework is well-designed:
- Equalized Odds (TPR/FPR parity) at < 0.05 difference is a stringent and appropriate threshold.
- Demographic Parity and Predictive Parity at < 0.10 are reasonable.
- Subgroups (age, race/ethnicity, rural isolation quartile, gender) are well-chosen.

**Concern:** The guide states race/ethnicity "as available." In rural RHC populations, race/ethnicity data completeness is often poor (30-50% missing). The guide should describe the plan for fairness assessment when subgroup membership data is incomplete. Imputation of race/ethnicity is ethically fraught -- the guide should state the approach explicitly (e.g., assessment restricted to patients with documented race/ethnicity, or use of indirect standardization methods like BISG).

### SHAP Implementation (Section 2.1.4)

The SHAP implementation is well-specified and production-ready:
- `TreeExplainer` for XGBoost provides exact (not approximate) SHAP values in polynomial time.
- The per-prediction output structure includes all elements needed for clinical display.
- The provider-facing display description (horizontal bar chart with clinical labels) is appropriate.

**One technical note:** The code sample uses `shap.TreeExplainer(xgb_model)` which, for XGBoost, computes interventional SHAP values by default. The guide should specify whether interventional or observational (tree-path-dependent) SHAP values are used and justify the choice. For clinical decision support where feature independence may not hold (e.g., A1C and diabetes diagnosis are correlated), interventional SHAP values may overstate the independent contribution of correlated features. This is a known limitation that should be acknowledged.

---

## 3. DATA PIPELINE EVALUATION

### RPM Device Data Ingestion (Section 3.1)

The RPM ingestion pipeline is well-designed with clear steps (poll, parse, validate, transform, store, evaluate, alert, track, log). The 15-minute polling interval is appropriate for clinical RPM.

**Strengths:**
- Mapping device readings to FHIR Observation resources is the correct approach.
- Range checking, duplicate detection, and device calibration validation are included.
- Billing-relevant tracking (transmission days for CPT 99454) is integrated into the ingestion flow.

**Concerns:**
1. **Polling vs. webhook.** The pipeline polls the Tenovi API every 15 minutes. Most modern device aggregators (including Tenovi) support webhook-based push notifications. The guide should justify the polling approach (e.g., GovCloud network restrictions, webhook reliability in asynchronous environments) or state plans to migrate to webhooks in a future phase.
2. **Data validation specifics.** "Range check" is mentioned but the specific physiological plausibility ranges are not defined (except in Section 9.1 for alert thresholds). The ingestion validation ranges should be documented separately from alert thresholds -- a reading of systolic BP 250 is physiologically implausible and should be flagged as a device error, not just an alert.
3. **Idempotency.** The pipeline does not explicitly address idempotent ingestion. If the polling service re-processes an already-ingested batch (e.g., due to retry logic), duplicate readings could be stored. The `device_transmissions` table has a UNIQUE constraint on `(clinic_id, patient_id, transmission_date, device_type)` which prevents duplicate transmission day counting, but the `observations` table has no such deduplication constraint.

### EHR Integration via FHIR R4 (Section 3.2)

The EHR sync design is clear and operationally sound:
- Full sync nightly + incremental sync every 2 hours using `_lastUpdated` is the standard FHIR bulk sync pattern.
- Conflict resolution rules (EHR = source of truth for clinical; platform = source of truth for RPM) are correctly specified.
- bonFHIR for FHIR operations in n8n is a reasonable choice.

**Concerns:**
1. **FHIR pagination.** FHIR search results are paginated (typically 20-100 resources per page). The guide does not describe how the sync workflow handles pagination (following Bundle.link[rel=next]) for large patient panels.
2. **Error handling and retry.** What happens when an EHR FHIR endpoint is down during a scheduled sync? The guide should describe retry policies, dead-letter queuing, and data freshness alerting.
3. **FHIR resource versioning.** The guide does not address how versioned FHIR resources are handled. If a Condition resource is updated in the EHR, does the platform overwrite or maintain history?

### CMS Billing Automation Pipeline (Section 3.3)

This is one of the strongest sections of the Technical Guide. The billing threshold logic is precisely specified with:
- Exact CPT code thresholds (16-day for 99454, 20-min for 99457, etc.)
- 2026 CMS code updates (99445, 99470) with mutual exclusivity rules
- Revenue maximization logic (prefer higher-value code when threshold met)
- Consent verification before billing event generation

**One concern:** The billing pipeline generates events with status `pending_review`. The guide should specify the maximum number of days a billing event can remain in `pending_review` before escalation, and whether there is a billing period close-out mechanism to prevent stale billing events from accumulating indefinitely.

---

## 4. DATABASE SCHEMA REVIEW

### Core Data Model (Section 4.1)

The schema is well-designed, FHIR R4-aligned, and includes the essential tables for Phase I operations:

**Strengths:**
- UUID primary keys throughout (avoids integer ID collision in multi-tenant contexts).
- `clinic_id` foreign key on every PHI table (required for RLS).
- FHIR alignment (fhir_id, standard coding columns, LOINC/ICD-10 codes).
- JSONB columns for flexible data (address, insurance, SHAP values, evidence) where appropriate.
- `device_transmissions` table with compound UNIQUE constraint for billing accuracy.
- `patient_consents` table with status lifecycle (active/revoked/expired) and audit fields.

**Concerns:**

1. **Missing indexes.** The schema does not include any index definitions. At minimum, the following indexes are critical for query performance:
   - `observations(clinic_id, patient_id, effective_dt)` -- RPM data queries
   - `observations(clinic_id, device_sourced, effective_dt)` -- billing day counting
   - `billing_events(clinic_id, patient_id, billing_period_start, cpt_code)` -- billing queries
   - `risk_scores(patient_id, created_at DESC)` -- latest risk score lookup (used in materialized view LATERAL join)
   - `device_transmissions(clinic_id, patient_id, transmission_date)` -- billing threshold calculation
   - `compliance_tasks(clinic_id, status, due_date)` -- compliance dashboard

   For an NIH technical guide, omitting indexes is a minor issue, but for reviewers assessing production-readiness, adding at least the critical indexes would strengthen the document.

2. **No `updated_at` column on most tables.** The `patients` table has `updated_at`, but `observations`, `conditions`, `encounters`, `billing_events`, `compliance_tasks`, `patient_consents`, and `risk_scores` do not. This will complicate incremental sync, change detection, and audit trail reconstruction.

3. **The `patients.risk_score` and `patients.risk_stratum` denormalized columns** create a data consistency risk. These are also stored in the `risk_scores` table. If the materialized risk score is updated in one location but not the other, the dashboard may display stale data. The guide should either (a) document the update trigger/mechanism that keeps these in sync, or (b) remove the denormalized columns from `patients` and always join to `risk_scores`.

4. **No `medications` table.** The feature engineering pipeline references "active med count," "adherence proxy," and "high-risk meds" as input features, and the FHIR sync includes MedicationRequest. But there is no corresponding table in the schema. This is a gap.

5. **The `audit_log` table does not have RLS enabled** (it is not listed in the RLS ALTER TABLE statements in Section 4.2). This is likely intentional (audit logs may need to be accessible to administrative roles across clinics), but the rationale should be stated explicitly. An alternative is to enable RLS on the audit log but grant a separate audit_admin role that bypasses it.

### Row-Level Security (Section 4.2)

The RLS implementation is well-documented:
- RLS enabled on all PHI tables (8 tables listed).
- Policy uses `current_setting('app.current_clinic_id')` session variable.
- Research analyst role with de-identified view access only.

**Concerns:**
1. **`FORCE ROW LEVEL SECURITY` is not specified.** The Implementation Guide (02) correctly notes that RLS policies do not apply to table owners by default and recommends using `ALTER TABLE ... FORCE ROW LEVEL SECURITY`. However, the Technical Guide's RLS section does not include this. For consistency and security, the Technical Guide should include `FORCE ROW LEVEL SECURITY` on all PHI tables.

2. **The RLS policy is `FOR ALL`** (covers SELECT, INSERT, UPDATE, DELETE). This is correct for reads but means that inserts and updates also require `app.current_clinic_id` to be set. The guide should document how this works for system-level operations (e.g., n8n workflows that process multiple clinics in a single execution, batch risk scoring across all patients).

3. **The `device_transmissions` table is not listed in RLS-enabled tables** even though it contains `clinic_id` and `patient_id`. This table is used for billing calculations and should have RLS.

4. **The `clinician_time_entries` table is also not listed in RLS-enabled tables.** Same concern -- it contains PHI-adjacent data (which clinician spent time on which patient).

### Cross-Domain Materialized Views (Section 4.3)

The three materialized views (compliance-claims, RPM-outcomes, MIPS-revenue) are well-conceived and directly support Aim 3 (cross-domain analytics). The SQL is syntactically correct and uses appropriate aggregation patterns.

**Concerns:**
1. **The `xd_compliance_claims` view joins compliance_tasks and billing_events by month.** This temporal join assumes a 1:1 monthly mapping between compliance task due dates and billing periods. In practice, compliance tasks may span multiple months or have due dates that do not align with billing periods. The join condition should be documented more carefully.

2. **The `xd_rpm_outcomes` view uses a LATERAL join** for the latest risk score, which is correct but may be slow without the recommended index on `risk_scores(patient_id, created_at DESC)`.

3. **Materialized views bypass RLS.** The guide does not address this. If a research analyst queries these views, they would see data across all clinics. The `research_analyst` role is granted access to de-identified views, but these materialized views are not de-identified. Either: (a) create de-identified versions of the materialized views, (b) add clinic_id filtering at the application layer, or (c) create RLS-enabled wrapper views on top of the materialized views.

4. **Concurrent refresh.** The guide mentions `REFRESH MATERIALIZED VIEW CONCURRENTLY` (line 754) but concurrent refresh requires a UNIQUE index on the materialized view. The guide does not define these unique indexes.

---

## 5. SECURITY ARCHITECTURE

### Defense-in-Depth Model (Section 5.1)

The five-layer security model (Network, Transport, Application, Data, Monitoring) is comprehensive and well-articulated. This is one of the strongest sections of the document and will resonate with NIH reviewers who are accustomed to seeing security treated as an afterthought.

**Strengths:**
- WAF on ALB (Layer 1) is appropriate for a public-facing healthcare application.
- Certificate pinning for EHR/device vendor connections (Layer 2) shows security maturity.
- Three-layer audit logging (CloudTrail + PGAudit + application audit log) exceeds HIPAA minimum requirements.
- 1-hour SLA for critical incident response (Layer 5) is aggressive and demonstrates seriousness.

**Concerns:**
1. **mTLS for inter-service communication is listed as "future."** For Phase I on ECS Fargate within the same VPC, security group isolation is likely sufficient. However, the guide should explicitly state that inter-service communication within the VPC is over private subnets with security group enforcement, and that mTLS is a Phase II enhancement.

2. **VPC Flow Logs to CloudWatch with anomaly detection** is mentioned but not detailed. Is this using CloudWatch Anomaly Detection, GuardDuty, or a custom alerting pipeline? The implementation mechanism should be specified.

3. **Break-glass procedure** (Section 5.2, Emergency Access) is mentioned but not described. For HIPAA compliance, the break-glass procedure should include: (a) who can invoke it, (b) what access it grants, (c) how it is logged, (d) the post-incident review process. A brief description would strengthen this section.

### HIPAA Security Rule Mapping (Section 5.2)

The mapping table covers all required HIPAA Security Rule administrative, physical, and technical safeguards. Each requirement is mapped to a specific implementation and verification method.

**One omission:** The HIPAA Security Rule requires a **Disaster Recovery Plan** (Section 164.308(a)(7) -- Contingency Plan). The guide mentions Multi-AZ RDS (implied in the infrastructure diagram) but does not describe a formal DR plan, including RPO (Recovery Point Objective), RTO (Recovery Time Objective), backup procedures, or restoration testing. This should be added.

### Encryption Key Management (Section 5.3)

The KMS envelope encryption approach is well-specified. Customer-managed keys (CMK) with annual automatic rotation, restricted key policies, and per-service data key generation is the correct GovCloud pattern.

**Concern:** The guide lists "Full name (when stored outside Patient)" as an application-level encrypted field. But in the `patients` table schema, `given_name` and `family_name` are stored as plaintext `TEXT` columns. If application-level encryption is applied to these fields, the schema should reflect that they store ciphertext (e.g., `BYTEA` type), or the guide should clarify that the Patient table is an exception to the field-level encryption rule because it is protected by RLS and RDS-level encryption.

---

## 6. API DESIGN

### FastAPI Service Endpoints (Section 6.1)

The API design is clean, RESTful, and includes:
- Versioned endpoints (`/api/v1/`)
- Bearer token authentication
- Clinic context via `X-Clinic-ID` header
- Appropriate HTTP status codes (200, 201, 202)
- Descriptive response payloads with nested structures

**Strengths:**
- The `POST /api/v1/risk/batch` endpoint returns `202 Accepted` with a job ID, correctly modeling asynchronous batch processing.
- The RPM reading response includes `billing_status` with days remaining to billing threshold -- this is operationally useful and a good design choice.
- The cross-domain analytics endpoint returns statistical measures (correlation coefficient, p-value, interpretation text).

**Concerns:**

1. **Error response format is not specified.** The guide shows success responses but not error responses. For an NIH technical guide, a standard error response format should be documented:
   ```json
   {
     "error": "validation_error",
     "message": "Patient not found",
     "details": [...],
     "request_id": "uuid"
   }
   ```

2. **Rate limiting details are not specified.** NGINX rate limiting is mentioned in the stack (Section 1.1) and in the security model, but the actual rate limits (requests per second per user, per clinic, per endpoint) are not documented.

3. **Pagination for list endpoints.** The billing events GET endpoint does not include pagination parameters (offset/limit or cursor-based). For clinics with hundreds of billing events, this will be necessary.

4. **The `X-Clinic-ID` header for tenant context** is a reasonable approach, but the guide should clarify how this header is validated against the authenticated user's clinic membership. Without validation, a user with a valid token could potentially set X-Clinic-ID to a different clinic's UUID and bypass application-level access control (RLS would still protect at the database level, but the API should enforce this before hitting the database).

5. **FHIR write-back.** The FHIR resource mapping table (Section 8.2) mentions "Observation (RPM): Platform -> EHR (future)" but no write-back API endpoint is documented. This is acceptable for Phase I but should be noted as a Phase II requirement.

### n8n Workflow Templates (Section 6.2)

The workflow template table is operationally useful and shows a mature understanding of the scheduling requirements. The specific cron schedules (15-min RPM poll, 2-hour EHR incremental, nightly billing/MV refresh, weekly risk scoring) are reasonable.

**Concern:** There is no mention of workflow execution monitoring, failure alerting, or retry policies for n8n workflows. If the nightly billing threshold check fails silently, revenue is lost. n8n provides execution logging, but the guide should describe how workflow execution health is monitored (e.g., n8n execution success rate exposed as a CloudWatch custom metric).

---

## 7. INFRASTRUCTURE

### GovCloud Deployment (Section 7.1)

The Terraform-described infrastructure is well-architected:
- Two availability zones with public/private/data subnet tiers
- ALB in public subnet; ECS Fargate in private subnets; RDS in data subnets
- NAT Gateways in both AZs for outbound traffic
- Shared services (S3, KMS, CloudTrail, CloudWatch, ECR, Secrets Manager) appropriately placed

**Strengths:**
- Private subnets for compute and data layers is the correct pattern.
- Secrets Manager for credential storage (EHR credentials, API keys) is appropriate.

**Concerns:**
1. **Dual NAT Gateways** in both public subnets is expensive for a Phase I pilot (~$100+/month). A single NAT Gateway with cross-AZ failover may be sufficient for Phase I, with dual NAT Gateways introduced for production HA.

2. **n8n standby in Subnet B** is shown in the diagram, but n8n Community Edition does not natively support active-standby failover (that requires Enterprise Edition queue mode with Redis). The diagram implies HA for n8n that may not be achievable in Phase I. This should be clarified.

3. **No mention of AWS WAF rules.** WAF is listed in the security model but no rule sets (e.g., OWASP Top 10, rate-based rules, IP reputation lists) are specified.

4. **No VPN or bastion host for administrative access.** The Implementation Guide mentions VPN + IP allowlisting for n8n access, but the Technical Guide infrastructure section does not show a VPN endpoint or bastion host. This should be included.

### Container Architecture (Section 7.2)

The Docker Compose / ECS mapping is clear and includes all required services (nginx, n8n, fastapi, nextjs, postgres, redis).

**Concern:** The Docker Compose shows `EXECUTIONS_MODE=queue` and `QUEUE_BULL_REDIS_HOST=redis` for n8n. However, queue mode is an n8n Enterprise feature (or requires manual self-hosted configuration with Redis). The Implementation Guide correctly identifies that Phase I will use single mode, not queue mode. The Technical Guide should either: (a) note that queue mode is a Phase II configuration, or (b) show the Phase I single-mode configuration.

### Monitoring and Observability (Section 7.3)

The monitoring table is comprehensive, covering infrastructure, application, database, security, ML model, uptime, and alerting. The inclusion of ML model monitoring (AUC-ROC drift, prediction distribution shift, feature importance stability) is forward-thinking and will impress NIH reviewers.

**Concern:** No mention of **log aggregation and search.** CloudWatch Logs is mentioned for archival, but for debugging and incident investigation, a structured logging approach (e.g., JSON-formatted logs with request_id, clinic_id, user_id correlation) should be described. This becomes critical during HIPAA breach investigations.

---

## 8. EHR INTEGRATION

### FHIR R4 Approach (Section 8)

The EHR integration strategy is well-documented with:
- Five target EHR systems prioritized by rural market relevance
- FHIR R4 resource mapping with sync direction and frequency
- SMART on FHIR authentication flow with refresh token management

**Strengths:**
- The priority ordering (eCW, athenahealth for Phase I; MEDITECH, Azalea, TruBridge for Phase II) is appropriate given FHIR maturity levels.
- Storing refresh tokens in AWS Secrets Manager is the correct approach.
- Auto-refresh on 401 response is operationally necessary.

**Concerns:**

1. **The authentication flow mixes two patterns.** Section 8.3 describes an "OAuth 2.0 Authorization Code flow" initiated by a clinic administrator, then stores a refresh token for backend sync. For SMART on FHIR Backend Services (system-to-system), the standard pattern is not Authorization Code -- it is JWT-based client assertion (described correctly in the Implementation Guide Section 2.3). The Technical Guide should clarify which flow is used for which scenario: (a) Backend Services (JWT assertion) for automated sync, (b) Authorization Code for initial clinic onboarding/authorization.

2. **SMART scopes are underspecified.** The guide lists `patient/*.read` and similar broad scopes. Most EHR systems in production require specific resource-level scopes (e.g., `patient/Patient.read`, `patient/Observation.read`). The guide should list the specific FHIR scopes requested.

3. **No mention of FHIR validation.** When resources are received from EHRs, they should be validated against US Core profiles before storage. Invalid resources (missing required elements, non-conformant codes) should be logged and handled gracefully, not silently dropped or stored with bad data.

4. **Azalea Health is listed as "HTTP Request + API key"** (Section 8.1) rather than bonFHIR + OAuth 2.0. This inconsistency should be explained -- is Azalea's FHIR API not mature enough for standard SMART on FHIR authentication? If so, what are the security implications of API key-based authentication?

5. **Write-back strategy is unclear.** RPM observations are shown as "Platform -> EHR (future)" in the resource mapping, but the clinical utility of the platform is diminished if providers must check two systems. The guide should describe the Phase I workaround (e.g., manual data entry into EHR, or PDF summary reports that can be imported).

---

## 9. CROSS-DOCUMENT CONSISTENCY

### Inconsistencies Between Technical Guide and VIPC Documents

| Issue | Technical Guide (03) | VIPC Brief (01) / Implementation Guide (02) | Impact |
|---|---|---|---|
| **RLS type casting** | `current_setting('app.current_clinic_id')::UUID` | `current_setting('app.current_clinic')::int` (02, Section 4.1) | **High.** One casts to UUID, the other to INT. These must be consistent. Since the schema uses UUID primary keys, the UUID cast is correct. The Implementation Guide should be updated. |
| **n8n execution mode** | Docker Compose shows `EXECUTIONS_MODE=queue` | Implementation Guide states Phase I is single mode (02, Section 2.2) | **Medium.** The Technical Guide's Docker Compose implies queue mode, which requires Redis and is an Enterprise/self-hosted feature. Phase I should show single mode configuration. |
| **modules_enabled data type** | Schema: `TEXT[] DEFAULT '{"compliance"}'` | Implementation Guide: `modules_enabled JSONB DEFAULT '["compliance"]'` (02, Section 2.5) | **Medium.** One uses a PostgreSQL TEXT array, the other uses JSONB. Choose one and be consistent. TEXT[] is simpler for this use case; JSONB is more flexible. |
| **Risk score tiers** | `'LOW', 'MEDIUM', 'HIGH'` (three tiers) | Implementation Guide: "Low/Medium/High/Critical" (four tiers, 02, Section 3.2) | **Low.** The Technical Guide uses three tiers while the Implementation Guide mentions four. Align on one system. |
| **Prediction target** | "30/60/90-day hospitalization or ED visit" (03, Section 2.1.2) | "Binary: hospitalization or ED visit within 90 days" (02, Section 3.2) | **Low.** The Technical Guide models three horizons (30/60/90); the Implementation Guide describes only 90-day. Clarify whether three separate models are trained or one model with configurable horizons. |
| **Phase I duration** | 9 months (NIH SBIR standard) | 4 months (VIPC grant, 02, Section 5) | **Context-dependent.** The Technical Guide is for the NIH SBIR proposal (9 months). The Implementation Guide is for the VIPC grant (4 months). This is not a true inconsistency, but the Technical Guide should be explicit that the 9-month timeline refers to the NIH Phase I, not the 4-month VIPC pilot. The training data temporal split (months 1-6 train / months 7-9 validate) depends on this distinction. |
| **Table naming** | `observations` table | Implementation Guide references `rpm_readings` table (02, Section 3.2) | **Medium.** The Technical Guide uses a single `observations` table for both EHR and RPM data (distinguished by `device_sourced` flag). The Implementation Guide creates a separate `rpm_readings` table. These are architecturally different choices. The unified `observations` table in the Technical Guide is the better design (FHIR-aligned), but the documents should be aligned. |
| **Auth approach** | "OAuth 2.0 / OIDC authentication" (Section 5.1) | "Keycloak or custom JWT auth" (02, Section 5) | **Low.** Not contradictory, but the Technical Guide should name the specific identity provider if it has been decided by this point. |
| **99453 billing rule** | Not mentioned with 2-day requirement | "requires minimum 2 days of monitoring data (2026 rule change)" (02, Section 3.3) | **Low.** The Technical Guide's billing pipeline (Section 3.3) lists 99453 as one-time initial setup but does not mention the 2026 2-day monitoring data requirement. This should be added for accuracy. |

---

## 10. STRENGTHS

- **Unified architecture across compliance, care, and revenue** on a single shared data model is a genuine technical innovation and is well-articulated throughout. The cross-domain materialized views concretely demonstrate the analytical value of this integration.
- **SHAP explainability is architecturally integrated,** not retrofitted. The per-prediction output structure, provider-facing display design, and storage of SHAP values in the risk_scores table demonstrate that explainability is a first-class concern.
- **Defense-in-depth security model** with five layers, three-tier audit logging, and field-level encryption exceeds typical SBIR Phase I security specifications. The GovCloud FedRAMP High posture is a genuine differentiator.
- **FHIR R4-aligned data model** across both the database schema and EHR integration layer demonstrates standards awareness and positions the platform for interoperability with the broader health IT ecosystem.
- **Comprehensive billing automation pipeline** with 2026 CPT code updates, mutual exclusivity logic, and consent verification is one of the most detailed billing automation specifications seen in an SBIR technical guide.
- **Open-source stack eliminates licensing cost as a scaling variable,** which is a genuine economic advantage and is well-documented with specific per-clinic COGS calculations.
- **Rural-first design decisions** (cellular RPM devices, asynchronous sync, configuration-driven multi-tenancy) are appropriate and well-justified.
- **The schema is well-normalized** with proper UUID primary keys, foreign key constraints, FHIR alignment, and JSONB columns where flexibility is needed.
- **The API design is clean and RESTful** with appropriate async patterns (202 for batch scoring), informative response payloads, and billing status integration into the RPM ingestion response.
- **Temporal deterioration detection** with configurable thresholds (per-clinic, per-patient) and combined static + trend scoring demonstrates clinical sophistication.
- **Model evaluation framework** includes both discrimination metrics (AUC-ROC, sensitivity) and calibration metrics (Brier score, calibration across strata), which is best practice.
- **Fairness metrics framework** with specific thresholds for equalized odds, demographic parity, and predictive parity across clinically relevant subgroups is well-designed and responsive to NIH health equity priorities.

---

## 11. WEAKNESSES

- **Class imbalance handling is not addressed.** For a 30-day hospitalization prediction task with an expected 3-5% event rate, the guide must describe the class imbalance mitigation strategy (e.g., scale_pos_weight, SMOTE, threshold optimization). **Recommended fix:** Add a "Class Imbalance Handling" subsection to Section 2.1.2 specifying the approach.

- **Training data provenance is underspecified.** "CMS Public Use Files" is not sufficient for NIH reviewers. Specific dataset names, years, sample sizes, and inclusion/exclusion criteria are required. **Recommended fix:** Create a table listing each CMS dataset with name, year, sample size, and relevant variables.

- **The temporal validation split is infeasible within Phase I.** "Train on months 1-6, validate on months 7-9" of pilot data requires 9 months of pilot operations, but the pilot likely starts in Month 4-5. **Recommended fix:** Revise the pilot data validation strategy to align with the actual study timeline (e.g., train on months 1-3 of pilot, validate on months 4-5, or use leave-one-clinic-out cross-validation across pilot sites).

- **Missing database indexes.** The schema defines no indexes, which will cause performance degradation even at moderate data volumes. **Recommended fix:** Add index definitions for all high-frequency query patterns.

- **Incomplete RLS coverage.** `device_transmissions`, `clinician_time_entries`, and `audit_log` tables are not covered by RLS policies. The first two contain PHI-adjacent billing data. **Recommended fix:** Add RLS to `device_transmissions` and `clinician_time_entries`. Document the explicit rationale for excluding `audit_log`.

- **Materialized views bypass RLS,** creating a potential data exposure path for the research analyst role or any role with SELECT access to these views. **Recommended fix:** Create de-identified wrapper views or add clinic_id filtering at the application layer for materialized view access.

- **No error response format is documented for the API.** NIH reviewers and downstream integrators need to understand how errors are surfaced. **Recommended fix:** Add a "Standard Error Response" subsection to Section 6.1.

- **No disaster recovery plan.** HIPAA requires a documented contingency plan. The guide mentions Multi-AZ RDS but does not specify RPO, RTO, backup frequency, or restoration testing procedures. **Recommended fix:** Add a "Disaster Recovery" subsection to Section 5 or Section 7.

- **n8n Community Edition HIPAA gap is acknowledged in the Implementation Guide but not in the Technical Guide.** The lack of SSO/LDAP and RBAC in n8n CE is a known risk that should be documented with the mitigation strategy (VPN + IP allowlisting) in this document. **Recommended fix:** Add n8n CE access control mitigation to Section 5.

- **No medications table in the schema** despite medications being a key feature group for the risk stratification model. **Recommended fix:** Add a `medications` or `medication_requests` table aligned with FHIR MedicationRequest.

- **FHIR resource validation is not described.** Resources ingested from EHRs should be validated against US Core profiles. **Recommended fix:** Describe the FHIR validation approach (e.g., HAPI FHIR validator, profile validation on ingest).

- **The Docker Compose configuration shows queue mode for n8n,** which contradicts the Phase I plan of using single mode. **Recommended fix:** Show the Phase I (single mode) configuration as the primary, with queue mode annotated as Phase II.

- **Observation table deduplication.** There is no UNIQUE constraint or deduplication logic preventing duplicate RPM readings in the `observations` table during re-polls or retries. **Recommended fix:** Add a composite unique constraint or a deduplication check in the ingestion pipeline.

- **The `patients.risk_score` denormalized field** creates a consistency risk with the `risk_scores` table. **Recommended fix:** Either document the synchronization mechanism (trigger or update workflow) or remove the denormalized columns and use a view/join.

---

## 12. SPECIFIC RECOMMENDED CHANGES

1. **Section 2.1.2 (Training Data Pipeline):** Add a table listing each CMS dataset by name (e.g., "Medicare Provider Utilization and Payment Data, Physician and Other Practitioners, 2022"), year, approximate sample size, and key variables extracted. NIH reviewers expect this level of data provenance documentation.

2. **Section 2.1.2 (Training Data Pipeline):** Add a new subsection "Class Imbalance Handling" with content: "Given the expected 30-day hospitalization event rate of 3-5% in the target population, class imbalance is addressed via: (a) XGBoost `scale_pos_weight` parameter set to the inverse of the positive class proportion, (b) threshold optimization using the F1-score on the validation set rather than the default 0.5 threshold, (c) stratified sampling in all cross-validation folds to preserve class proportions."

3. **Section 2.1.2 (Training Data Pipeline):** Revise the pilot data validation split. Replace "Pilot Data: Temporal split (train on months 1-6, validate on months 7-9)" with a timeline-feasible strategy: "Pilot Data: Given the NIH Phase I 9-month timeline with pilot deployment beginning in Month 3-4, we will use (a) leave-one-clinic-out cross-validation across the 2-3 pilot sites, and (b) a prospective validation window in the final 2 months of the study period, comparing model predictions made in Month 6-7 against observed outcomes in Months 7-9."

4. **Section 2.1.3 (Model Evaluation):** Add Net Reclassification Improvement (NRI) and decision curve analysis to the evaluation framework. Add row: "NRI vs. LACE Index | Positive | Net improvement in classification of high-risk vs. low-risk patients compared to LACE" and "Decision Curve Analysis | Net benefit > treat-all/treat-none | Clinical utility across relevant threshold probabilities."

5. **Section 2.1.3 (Fairness Metrics):** Add text: "For subgroups with >30% missing race/ethnicity data, fairness assessment will be limited to patients with documented race/ethnicity. We will report the missingness rate and assess whether missingness itself is associated with model performance using a missingness indicator variable."

6. **Section 2.1.4 (SHAP Implementation):** Add a note after the code sample: "Note: TreeExplainer computes interventional SHAP values by default, which assume feature independence. For correlated clinical features (e.g., A1C and diabetes diagnosis), SHAP values may overstate independent contributions. We will assess the impact of feature correlations on SHAP stability using the SHAP interaction values matrix and report results."

7. **Section 3.3 (CMS Billing Pipeline):** Add the 99453 2026 rule change. In the CPT 99453 block, add: "Requires minimum 2 days of monitoring data (2026 CMS rule change -- reduced from prior 16-day initial monitoring requirement)."

8. **Section 4.1 (Core Data Model):** Add a `medication_requests` table:
   ```sql
   CREATE TABLE medication_requests (
       id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
       clinic_id UUID NOT NULL REFERENCES clinics(id),
       patient_id UUID NOT NULL REFERENCES patients(id),
       fhir_id TEXT,
       code TEXT NOT NULL,  -- RxNorm code
       code_display TEXT,
       status TEXT,  -- 'active', 'completed', 'stopped'
       authored_on DATE,
       dosage JSONB,
       created_at TIMESTAMPTZ DEFAULT NOW(),
       updated_at TIMESTAMPTZ DEFAULT NOW()
   );
   ```

9. **Section 4.1 (Core Data Model):** Add `updated_at TIMESTAMPTZ DEFAULT NOW()` to the `observations`, `conditions`, `encounters`, `billing_events`, `compliance_tasks`, `patient_consents`, and `risk_scores` tables.

10. **Section 4.1 (Core Data Model):** Add a "Key Indexes" subsection after the schema:
    ```sql
    CREATE INDEX idx_observations_clinic_patient_dt ON observations(clinic_id, patient_id, effective_dt);
    CREATE INDEX idx_observations_device_sourced ON observations(clinic_id, device_sourced, effective_dt);
    CREATE INDEX idx_billing_events_period ON billing_events(clinic_id, patient_id, billing_period_start, cpt_code);
    CREATE INDEX idx_risk_scores_patient_latest ON risk_scores(patient_id, created_at DESC);
    CREATE INDEX idx_device_tx_billing ON device_transmissions(clinic_id, patient_id, transmission_date);
    CREATE INDEX idx_compliance_tasks_status ON compliance_tasks(clinic_id, status, due_date);
    CREATE INDEX idx_encounters_patient_period ON encounters(clinic_id, patient_id, period_start);
    ```

11. **Section 4.2 (Row-Level Security):** Add `FORCE ROW LEVEL SECURITY` statements:
    ```sql
    ALTER TABLE patients FORCE ROW LEVEL SECURITY;
    -- (repeat for all PHI tables)
    ```
    Also add `device_transmissions` and `clinician_time_entries` to the RLS-enabled table list.

12. **Section 4.2 (Row-Level Security):** Add a note explaining system-level operations: "For batch operations that span multiple clinics (e.g., weekly risk scoring, cross-clinic analytics), a dedicated `batch_processor` role is used with `SET ROLE` to temporarily adopt the appropriate clinic context per iteration, ensuring RLS is respected even in batch contexts."

13. **Section 4.3 (Materialized Views):** Add UNIQUE indexes required for CONCURRENTLY refresh:
    ```sql
    CREATE UNIQUE INDEX ON xd_compliance_claims(clinic_id, billing_month);
    CREATE UNIQUE INDEX ON xd_rpm_outcomes(clinic_id, patient_id, month);
    CREATE UNIQUE INDEX ON xd_mips_revenue(clinic_id, quarter);
    ```

14. **Section 4.3 (Materialized Views):** Add a note: "Materialized views bypass PostgreSQL row-level security. Access to these views is restricted to administrative and research roles. The research_analyst role accesses only de-identified versions of these views (created as separate views with direct identifiers removed)."

15. **Section 5 (Security Architecture):** Add a "Disaster Recovery" subsection:
    - RPO: 5 minutes (RDS Multi-AZ synchronous replication)
    - RTO: < 30 minutes (RDS automatic failover + ECS service relaunch)
    - Daily automated backups to S3 with 35-day retention
    - Monthly restoration testing from backup
    - Documented failover procedure with annual drill

16. **Section 5 (Security Architecture):** Add the n8n Community Edition HIPAA access control mitigation: "n8n Community Edition lacks enterprise SSO/LDAP and RBAC features. During Phase I, access to the n8n administrative interface is restricted to the VV engineering team via VPN + NGINX IP allowlisting. All clinic staff interact exclusively through the React frontend, which implements application-level RBAC. No clinic user has direct access to the n8n interface. Phase II evaluation: n8n Enterprise Edition or external OAuth2 Proxy."

17. **Section 6.1 (API Reference):** Add a "Standard Error Response" subsection documenting the error response format, including validation errors (400), authentication failures (401), authorization failures (403), not found (404), and server errors (500), each with example payloads.

18. **Section 6.1 (API Reference):** Add pagination parameters to the billing events GET endpoint: `?offset=0&limit=50` with a note on maximum page size and cursor-based pagination for large result sets.

19. **Section 6.1 (API Reference):** Add a note under the `X-Clinic-ID` header: "The X-Clinic-ID header is validated against the authenticated user's clinic membership(s) in the JWT claims. Requests with an X-Clinic-ID not present in the user's authorized clinics are rejected with 403 Forbidden before reaching the database layer."

20. **Section 7.2 (Container Architecture):** Change the n8n Docker Compose environment to show Phase I single-mode configuration:
    ```yaml
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - EXECUTIONS_MODE=regular  # Phase I: single mode
      # Phase II: EXECUTIONS_MODE=queue with Redis
    ```

21. **Section 8.3 (FHIR Authentication):** Clarify the two authentication patterns: "For automated system-to-system sync (Backend Services): JWT-based client assertion per SMART on FHIR Backend Services specification (no user in the loop). For initial clinic authorization: OAuth 2.0 Authorization Code flow initiated by clinic administrator to grant platform access."

22. **Section 8.3 (FHIR Authentication):** Replace broad SMART scopes with specific resource-level scopes: "`system/Patient.read`, `system/Condition.read`, `system/Encounter.read`, `system/Observation.read`, `system/MedicationRequest.read`, `system/AllergyIntolerance.read`."

23. **Section 3.1 (RPM Data Ingestion):** Add an "Observation Deduplication" step: "Step 3a: De-duplicate readings using composite key (patient_id, device_id, timestamp). If a reading with the same composite key already exists in the observations table, skip insertion and log as duplicate."

24. **Section 2.1.2 (Training Data Pipeline):** Add a subsection specifying the outcome label definition: "The binary outcome label is defined as any all-cause acute care utilization (unplanned inpatient admission or emergency department visit) within the prediction horizon. Observation stays are classified as inpatient. ED visits resulting in inpatient admission are counted once (as inpatient). The expected base rate in the target population is 3-5% at 30 days and 10-15% at 90 days, based on CMS public use file analysis."

25. **Section 1.2 (System Context Diagram):** Move the "3C PLATFORM (Amazon GovCloud)" label from below the dashboard to above the internal components (or use it as a wrapper), so the diagram clearly shows the boundary between external systems and the internal platform.

---

*Review prepared for internal use by the Authentic Consortium technical team. This review is intended to strengthen the NIH SBIR Phase I Technical Guide before submission and does not constitute an official NIH review.*
