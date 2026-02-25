# NIH SBIR PHASE I PROPOSAL

**Title:** AI-Driven Integrated Compliance, Care, and Revenue Optimization Platform for Rural Health Clinics

**Funding Opportunity:** NIH SBIR Phase I (R43)
**Applicant Organization:** Authentic Consortium (ACT)
**Principal Investigator / Program Director:** Will Nelson
**Requested Budget:** $256,000 (Direct Costs) over 9 months
**Proposed Start Date:** October 1, 2026
**NIH Institute:** National Institute of General Medical Sciences (NIGMS) / National Institute on Minority Health and Health Disparities (NIMHD)
**Study Section:** Biomedical Computing and Health Informatics (BCHI)

---

## SPECIFIC AIMS

Rural Health Clinics (RHCs) serve as the primary care safety net for 62 million Americans in medically underserved communities. Virginia alone has 106 RHCs and 27 Federally Qualified Health Centers (FQHCs), with 3 RHCs closing in 2025 due to federal funding cuts and 9 rural hospitals at imminent risk of closure. These clinics face a convergence of three compounding crises that existing point solutions fail to address:

1. **Compliance burden:** Each RHC faces 15+ distinct regulatory obligations (HIPAA, HRSA UDS, CMS quality metrics, FCC broadband), consuming 15--20 administrator hours per week. Non-compliance triggers loss of Medicare/Medicaid reimbursement -- which constitutes 60--80% of RHC revenue.

2. **Care gaps:** Provider shortages (1 physician per 2,500+ patients in some Virginia counties), chronic disease prevalence 30--40% above urban averages, and zero monitoring between infrequent visits result in preventable hospitalizations and emergency department utilization.

3. **Revenue leakage:** Systematic undercoding, missed quality bonuses (MIPS/APM), and inability to capture Remote Patient Monitoring (RPM) and Chronic Care Management (CCM) reimbursement leaves an estimated $195,000--$267,000 per clinic per year in unrealized CMS revenue on the table.

**The critical insight is that these three problems are interconnected.** Compliance failures cause revenue loss. Care gaps drive costly ER utilization. Revenue shortfalls prevent investment in better care. No existing technology platform treats all three as a unified system -- existing solutions address compliance (Compliancy Group, HIPAA One), care monitoring (TelliHealth, Optimize Health), or revenue cycle (Waystar, AdvancedMD) in isolation, missing the cross-domain interactions that determine RHC viability.

**The long-term goal** of this research program is to develop and validate an AI-driven integrated platform -- the **3C Platform (Compliance, Care, Collect Cash)** -- that unifies regulatory compliance automation, AI-driven preventive care, and automated revenue optimization on a single shared data model, specifically designed for the operational constraints and clinical workflows of rural health clinics.

### Aim 1: Develop and Validate an AI Risk Stratification Engine for Rural Patient Populations

Develop machine learning models (XGBoost ensemble with SHAP-based explainability) trained on CMS public use files and pilot clinic electronic health record (EHR) data to predict 30/60/90-day risk of hospitalization or emergency department visit for rural patients with chronic conditions. **Success criterion:** AUC-ROC > 0.75 with sensitivity > 80% for the highest-risk decile, validated prospectively during the pilot period.

**Hypothesis:** An AI risk stratification model incorporating clinical, social determinant, and utilization data can identify high-risk rural patients with sufficient accuracy to enable targeted preventive interventions, reducing preventable hospitalizations in the pilot population.

### Aim 2: Build and Pilot an Integrated RPM Data Ingestion and Automated CMS Billing Pipeline

Design and deploy a system that ingests continuous physiological data from cellular-connected RPM devices (blood pressure, glucose, pulse oximetry, weight), detects clinical deterioration trends via temporal analytics, and automatically tracks CMS billing thresholds (16-day transmission minimum for CPT 99454, 20-minute clinician interaction for CPT 99457/99458, CCM time thresholds for CPT 99490). **Success criterion:** Automated capture of > 90% of billable RPM/CCM events across pilot clinics, with a projected revenue increase of $195,000--$267,000 per clinic per year in previously unrealized CMS reimbursement.

**Hypothesis:** An integrated device-to-billing pipeline that automates data ingestion, clinical alerting, and billing threshold tracking can enable resource-constrained RHCs to operate RPM/CCM programs that are financially self-sustaining through CMS reimbursement.

### Aim 3: Design and Evaluate a Unified Compliance-Care-Revenue Data Architecture with Cross-Domain Feedback Loops

Create a shared data model (PostgreSQL with row-level security for multi-tenant clinic isolation) where compliance status, clinical care activities, and revenue cycle data interconnect -- enabling automated identification of how compliance gaps affect reimbursement, how care activities generate billable events, and how revenue trends predict compliance risk. **Success criterion:** Demonstrate at least 3 measurable cross-domain interactions (e.g., compliance documentation completeness correlating with claims acceptance rate) validated in pilot clinic data.

**Hypothesis:** A unified data architecture that captures the interdependencies between compliance, care, and revenue can reveal actionable cross-domain insights not available from siloed point solutions, enabling more effective resource allocation in resource-constrained RHCs.

**Impact:** If successful, this Phase I research will demonstrate the feasibility of an integrated AI-driven platform that transforms rural health clinic operations from reactive to proactive. Phase II will expand to 50+ clinics across Appalachian states (Virginia, West Virginia, Kentucky, Tennessee, North Carolina), validate clinical outcome improvements, and prepare for FDA regulatory pathway assessment. The platform addresses NIH priorities in health disparities, rural health, and digital health innovation while creating a commercially viable, scalable solution for a $132M--$264M national market (5,500+ RHCs at $2,000--$4,000/month).

---

## RESEARCH STRATEGY

### A. SIGNIFICANCE

#### A.1 The Rural Health Crisis Is an Urgent National Priority

Rural Americans experience significantly worse health outcomes than urban populations across nearly every metric. Rural communities face higher rates of chronic disease (diabetes prevalence 30--40% above urban averages), greater barriers to care (provider shortages, transportation, broadband access), and systematic underfunding of healthcare infrastructure. The closure of 3 Virginia RHCs in 2025 alone -- driven by federal funding cuts and regulatory compliance costs -- exemplifies a national trend threatening the primary care safety net for 62 million Americans.

CMS data demonstrates that Rural Health Clinics leave an estimated $195,000--$267,000 per clinic per year in unrealized RPM, CCM, and quality bonus revenue. This is based on conservative RPM/CCM enrollment rates (30% of eligible chronic disease patients at $100--$180/month in CMS reimbursement per patient via CPT codes 99454, 99457, 99458, 99490) and MIPS penalty avoidance (up to -9% Medicare payment adjustment). This revenue gap is not due to ineligibility -- it is due to lack of technological infrastructure to capture, document, and bill for services that CMS explicitly funds.

#### A.2 Existing Solutions Fail Rural Clinics

Current healthcare technology is designed for large health systems with dedicated IT departments, not for 3--5 provider RHCs with total IT budgets of $34,000--$95,000/year. Existing solutions fall into three siloed categories:

- **Compliance tools** (Compliancy Group, HIPAA One, Intraprise Health): Track compliance status but have no clinical or revenue components. Cost: $3,000--$15,000/year.
- **RPM/CCM platforms** (TelliHealth, Rimidi, Optimize Health): Monitor patients and manage RPM programs but have no compliance or revenue cycle integration. Cost: $5,000--$30,000/year per provider.
- **Revenue cycle management** (Waystar, Athena RCM, AdvancedMD): Optimize billing but have no clinical intelligence or compliance automation. Cost: $10,000--$50,000/year.

A clinic deploying all three categories faces $18,000--$95,000/year in licensing costs, three separate data silos with no cross-domain analytics, and the administrative overhead of managing three vendor relationships. This is economically and operationally infeasible for most RHCs.

#### A.3 The Innovation Gap: No Unified Compliance-Care-Revenue Platform Exists

A systematic review of the healthcare IT landscape reveals no commercially available platform that integrates regulatory compliance automation, AI-driven clinical risk stratification, and automated CMS billing capture on a shared data model. This gap exists because:

1. **Market segmentation:** Healthcare IT vendors specialize in narrow domains (EHR, RCM, compliance, RPM) and lack incentive to build cross-domain platforms for a 5,500-clinic niche market.
2. **Technical barriers:** Integrating compliance, clinical, and financial data requires HL7 FHIR R4 interoperability, complex CMS billing logic, and domain-specific AI models that span multiple disciplines.
3. **Economic barriers:** Enterprise healthcare platforms (e.g., Salesforce Health Cloud) carry licensing costs ($100K+/year) that exceed the total IT budget of most RHCs.

**This research addresses a significant gap** by developing and validating the first integrated platform purpose-built for the unique operational, clinical, and financial constraints of rural health clinics.

#### A.4 Alignment with NIH Priorities

This research directly aligns with:
- **NIMHD:** Addresses health disparities in rural and medically underserved populations
- **NIGMS:** Develops innovative biomedical informatics approaches to clinical decision support
- **NIH Strategic Plan for Data Science:** Leverages AI/ML for clinical prediction and health services optimization
- **21st Century Cures Act:** Advances interoperable health IT using HL7 FHIR R4 standards
- **Healthy People 2030:** Targets reduction in preventable hospitalizations and improved chronic disease management in underserved populations

---

### B. INNOVATION

#### B.1 Novel Unified Data Architecture (Compliance + Care + Revenue)

The 3C Platform introduces a **patent-pending unified data architecture** where compliance, care, and revenue data share a single PostgreSQL data model with row-level security for multi-tenant clinic isolation. This is technically novel because:

- **Cross-domain feedback loops:** Compliance documentation completeness directly affects claims acceptance rates. Care activities (RPM readings, CCM interactions) automatically generate billable events. Revenue trend anomalies (declining reimbursement) trigger compliance risk alerts. No existing system captures these interdependencies.
- **Configuration-driven multi-tenancy:** A single platform instance serves multiple clinics with different EHRs, device mixes, payer landscapes, and regulatory requirements via feature flags and template workflows -- not separate codebases. This deployment model enables sublinear cost scaling ($100--$150/month infrastructure per clinic at scale vs. $650+/month for enterprise SaaS licensing alone).

#### B.2 AI Risk Stratification with SHAP-Based Clinical Explainability

The risk stratification engine uses an XGBoost ensemble model trained on CMS public use files with SHAP (SHapley Additive exPlanations) values providing feature-level explanations for every prediction. This is innovative in the RHC context because:

- **Designed for sparse rural data:** Rural patients have fewer encounters, fewer lab results, and more fragmented records than urban patients. The model architecture is specifically designed to perform with incomplete data, using imputation strategies validated against CMS datasets.
- **Actionable explainability:** Every risk score includes the top contributing factors (e.g., "high risk driven by rising A1C, missed cardiology referral, 3 ER visits in 6 months"), enabling the provider to make informed clinical decisions. This satisfies the 21st Century Cures Act clinical decision support exemption criteria.
- **Temporal deterioration detection:** Beyond static risk scoring, the platform implements sliding-window trend analysis on RPM data streams (BP trending, A1C drift, weight gain patterns in CHF, SpO2 decline) to detect clinical deterioration before acute episodes.

#### B.3 Automated CMS Billing Threshold Detection and Revenue Optimization

The automated billing pipeline is technically novel in its integration of:

- **Device-to-bill automation:** RPM device data flows from cellular-connected devices through API ingestion, clinical alert evaluation, trend analysis, and CMS billing threshold tracking (16-day transmission minimums, clinician time tracking, mutual exclusivity logic between competing CPT codes) in a single automated pipeline.
- **New 2026 CPT code integration:** The platform incorporates the new 2026 CPT codes (99445 for 2--15 day monitoring, 99470 for shorter clinician interactions) that expand billing opportunities for clinics that cannot meet the traditional 16-day threshold with all patients.
- **Revenue forecasting:** Predictive models project per-clinic revenue based on current enrollment, device compliance, and billing patterns, enabling clinic administrators to make data-driven staffing and investment decisions.

#### B.4 Military-Grade Security Applied to Healthcare

The platform leverages the same architecture that the development team deploys for Department of Defense clients: containerized applications on Amazon GovCloud (FedRAMP High authorized, HIPAA BAA). This is a higher security posture than any commercial healthcare SaaS platform (which typically operates at FedRAMP Moderate or below). Technical security innovations include:

- **GovCloud deployment:** FedRAMP High infrastructure meeting the same standards as DoD health systems (MHS GENESIS)
- **AES-256 encryption at rest** with customer-managed AWS KMS keys
- **PostgreSQL row-level security** for cryptographic clinic data isolation
- **PGAudit** for complete, tamper-evident audit trails meeting HIPAA Security Rule requirements
- **Application-level field encryption** for the most sensitive PHI fields beyond database-level encryption

---

### C. APPROACH

#### C.1 Platform Architecture and Technology Stack

The 3C Platform is built on a proven, production-grade technology stack:

| Layer | Technology | Purpose |
|---|---|---|
| **Hosting** | Amazon GovCloud (ECS Fargate + RDS + S3) | FedRAMP High, HIPAA-eligible infrastructure |
| **Workflow Engine** | n8n (self-hosted) | Visual workflow automation for EHR integration, RPM ingestion, billing automation, compliance tasks, alert routing |
| **Database** | PostgreSQL 16 (Amazon RDS) | Central data store with row-level security, AES-256 encryption, PGAudit |
| **API/ML Layer** | Python/FastAPI | ML model serving, high-frequency device data ingestion, FHIR data transforms |
| **Frontend** | React/Next.js | Clinic-facing dashboard (Patient 360, compliance tracker, billing tracker, MIPS dashboard) |
| **EHR Integration** | bonFHIR + n8n HTTP Request nodes | HL7 FHIR R4 connectivity to eClinicalWorks, athenahealth, MEDITECH, Azalea Health |
| **RPM Devices** | Tenovi / Smart Meter APIs | Cellular-connected BP cuffs, glucose monitors, pulse oximeters, scales |
| **Containerization** | Docker on ECS Fargate | Consistent deployment, horizontal scaling |
| **Reverse Proxy** | NGINX | TLS 1.2+, HSTS, CSP, rate limiting |

**This is not a prototype stack.** The development team currently builds classified systems for a defense client on this exact architecture (n8n + PostgreSQL + NGINX + Docker on GovCloud), with deployment paths from unclassified through TS/SCI. The 3C Platform applies the same proven components to healthcare.

#### C.2 Research Plan -- Aim 1: AI Risk Stratification Engine

**Phase 1A (Months 1--3): Model Development and Training**

- **Data sources:** CMS public use files (Medicare Provider Utilization and Payment Data, Chronic Conditions Prevalence, Hospital Readmissions Reduction Program data), supplemented by pilot clinic EHR data via FHIR R4 extraction
- **Feature engineering:** Demographics, diagnosis history (ICD-10), medication adherence proxies, utilization patterns (ED visits, hospitalizations, missed appointments), laboratory values (A1C, lipid panels, eGFR), social determinant indicators (rural isolation index, transportation access, broadband availability)
- **Model architecture:** XGBoost gradient-boosted ensemble as primary model, with logistic regression as interpretable baseline. Hyperparameter optimization via Bayesian search (Optuna). 5-fold stratified cross-validation
- **Explainability:** SHAP values computed for every prediction. Top-k feature contributions displayed to providers. SHAP summary plots generated for population-level insights
- **Bias mitigation:** Fairness metrics (equalized odds, demographic parity) computed across age, race/ethnicity, and rural isolation categories. Iterative retraining with fairness constraints if disparities exceed predefined thresholds
- **Clinical validation criteria:** AUC-ROC > 0.75, sensitivity > 80% for highest-risk decile, calibration within 10% across risk strata

**Phase 1B (Months 3--6): Temporal Deterioration Detection**

- **Algorithm:** Sliding-window trend analysis on RPM time-series data (blood pressure, glucose, weight, SpO2)
- **Alerting logic:** Configurable thresholds (defaults: BP > 180/120, SpO2 < 90%, weight gain > 3 lbs/day for CHF, A1C > 9.0) with provider-tunable sensitivity
- **Validation:** Retrospective validation against pilot clinic data; prospective tracking of alert-to-intervention-to-outcome chains during pilot period

#### C.3 Research Plan -- Aim 2: RPM Data Ingestion and Billing Pipeline

**Phase 2A (Months 1--3): Device Integration and Data Pipeline**

- **RPM device connectivity:** Integration with Tenovi API (40+ FDA-cleared cellular-connected devices via single API) and Smart Meter API. Cellular connectivity eliminates WiFi dependency for rural patients
- **Data pipeline:** Python ingestion service → PostgreSQL (FHIR-compliant Observation resources) → n8n alert workflows → provider notification (email/SMS/dashboard)
- **Data validation:** Automated range checks, device calibration verification, duplicate detection, gap analysis (missed transmission days)

**Phase 2B (Months 3--6): Automated Billing Threshold Tracking**

- **CMS billing logic implementation:**
  - CPT 99454 (RPM device supply/data transmission): Track 16-day minimum per 30-day period
  - CPT 99457 (RPM clinician interaction): Track 20-minute minimum per month
  - CPT 99458 (additional RPM clinician time): Track additional 20-minute increments
  - CPT 99490 (CCM): Track 20-minute minimum clinical staff time per month
  - CPT 99445 (2--15 day RPM monitoring -- new 2026): Track sub-threshold billing opportunities
  - CPT 99470 (shorter RPM interactions -- new 2026): Track abbreviated clinician encounters
  - Mutual exclusivity logic: Enforce correct code selection when overlapping codes apply
- **Billing event generation:** n8n workflows aggregate daily device readings and clinician time entries, automatically flag when thresholds are met, and generate structured billing events for claim submission
- **Patient consent workflow:** Automated capture and tracking of clinical consent and Medicare-specific RPM consent (required for RPM billing)

**Phase 2C (Months 6--9): Pilot Validation**

- **Pilot sites:** 2--3 Virginia RHCs selected based on EHR compatibility (eClinicalWorks or athenahealth initial targets), chronic disease patient volume, and willingness to participate
- **Patient enrollment target:** 50--100 RPM patients across pilot sites, drawn from chronic disease populations (hypertension, diabetes, CHF, COPD)
- **Success metrics:** > 90% automated billing event capture rate, < 5% false positive billing events, clinician satisfaction score > 4.0/5.0, measurable revenue increase vs. baseline

#### C.4 Research Plan -- Aim 3: Unified Data Architecture

**Phase 3A (Months 1--4): Schema Design and Implementation**

- **Core data model:** Patient, Encounter, Observation (RPM readings), Condition, MedicationRequest, Claim, ComplianceTask, BillingEvent, AuditLog tables with FHIR R4-aligned resource structure
- **Row-level security:** PostgreSQL RLS policies enforcing cryptographic clinic-level data isolation. Each clinic's data is invisible to other clinic tenants at the database level
- **Cross-domain linkages:** Foreign key relationships and materialized views connecting compliance status → claim acceptance rates, care activities → billing events, revenue trends → compliance risk indicators

**Phase 3B (Months 4--9): Cross-Domain Analytics and Validation**

- **Target cross-domain interactions to validate:**
  1. Compliance documentation completeness score ↔ claims denial rate
  2. RPM device adherence (transmission days/month) ↔ clinical outcome indicators (ED visits, hospitalizations)
  3. MIPS quality measure performance ↔ reimbursement rate trends
  4. Care gap closure rate ↔ RPM program retention rate
  5. Staffing pattern changes ↔ compliance task completion rate
- **Statistical methods:** Correlation analysis, interrupted time series (pre/post platform deployment), propensity score matching for clinic-level comparisons where feasible
- **Data visualization:** React/Next.js dashboard with cross-domain analytics panels demonstrating the interconnections to clinic administrators

#### C.5 Timeline and Milestones

| Month | Aim 1: Risk Stratification | Aim 2: RPM/Billing Pipeline | Aim 3: Unified Architecture |
|---|---|---|---|
| **1** | CMS data acquisition; feature engineering | GovCloud infrastructure; device API integration | Schema design; PostgreSQL RLS |
| **2** | Model training (XGBoost + baseline) | n8n workflow development for RPM ingestion | Core data model deployment |
| **3** | Cross-validation; SHAP implementation | Billing threshold logic; consent workflow | Cross-domain linkage development |
| **4** | Pilot clinic EHR integration; model refinement | Pilot clinic device deployment | Materialized views; analytics queries |
| **5** | Prospective validation begins | Billing automation testing with live data | Cross-domain interaction analysis |
| **6** | Deterioration detection deployment | Full billing pipeline operational | Dashboard development |
| **7** | Model performance evaluation | Revenue impact measurement | Statistical validation |
| **8** | Bias audit; fairness metric evaluation | Billing accuracy audit | Cross-domain findings report |
| **9** | Final model validation report | Final billing pipeline report | Final architecture evaluation |

#### C.6 Potential Pitfalls and Mitigation Strategies

| Risk | Probability | Mitigation |
|---|---|---|
| **EHR integration delays** | Medium | Fall back to CSV import for initial pilot; prioritize single EHR (eClinicalWorks, largest RHC market share) |
| **Low RPM patient enrollment** | Medium | Provide devices at no cost to patients; cellular connectivity eliminates WiFi barrier; involve clinic staff in enrollment workflow design |
| **Insufficient pilot data for ML validation** | Low-Medium | Supplement with CMS public use files; use transfer learning from larger datasets; adjust model complexity to available data |
| **Staff adoption resistance** | Medium | Co-design Sprint 1 UI with clinic staff; match existing workflows; provide on-site training |
| **Model performance below AUC threshold** | Low | Pre-trained on CMS data with established predictive signal; fallback to simpler logistic regression model with validated features |
| **Regulatory changes to RPM billing** | Low | Modular billing rules engine allows rapid adaptation to code changes; CMS trend is toward expanding (not restricting) RPM reimbursement |

#### C.7 Human Subjects Considerations

This research involves collection and analysis of protected health information (PHI) from pilot clinic patients enrolled in RPM programs.

- **IRB Review:** Full IRB protocol submission prior to pilot clinic deployment (Month 3). Anticipate expedited review as minimal risk research.
- **Informed Consent:** Two-stage consent: (1) Clinical consent for RPM monitoring; (2) Research consent for de-identified data use in model validation
- **Data Protection:** All PHI stored in HIPAA-compliant Amazon GovCloud environment with AES-256 encryption, row-level security, and PGAudit logging. De-identified datasets used for model training and validation.
- **Privacy Risk Mitigation:** PHI access restricted to authorized clinic staff and research team with role-based access controls. Audit trails for all data access. Annual HIPAA Security Risk Assessment.
- **Vulnerable Populations:** Rural populations may face digital literacy and broadband access barriers. Cellular-connected devices mitigate broadband issues. Clinic staff provide device training in patients' preferred language.

---

## BUDGET AND BUDGET JUSTIFICATION

### Budget Summary (9-month Phase I)

| Category | Cost |
|---|---|
| **Senior Personnel** | |
| PI / Lead Developer (Will Nelson) -- 6.0 calendar months effort | $90,000 |
| Co-Investigator / Clinical Advisor -- 1.0 calendar month effort | $15,000 |
| **Other Personnel** | |
| Data Engineer -- 4.5 calendar months effort | $54,000 |
| Clinical Informatics Specialist -- 3.0 calendar months effort | $36,000 |
| **Equipment** | $0 |
| **Travel** | |
| Pilot clinic onboarding visits (3 clinics x 2 visits x $750) | $4,500 |
| NIH-required PI travel (study section, program meetings) | $3,000 |
| **Other Direct Costs** | |
| AWS GovCloud infrastructure (9 months x $750/month) | $6,750 |
| RPM devices for pilot (25 units, cellular-connected) | $3,750 |
| ML model training compute (GovCloud GPU instances) | $2,500 |
| EHR developer program access + FHIR sandbox fees | $1,500 |
| Legal (HIPAA BAA templates, pilot agreements, IRB) | $5,000 |
| Provisional patent filing (patent attorney + USPTO fees) | $5,000 |
| Software and monitoring tools | $2,000 |
| Participant support (patient device training materials) | $2,000 |
| **Subtotal Direct Costs** | $231,000 |
| **Indirect Costs (estimated 10.8% -- small business rate)** | $25,000 |
| **TOTAL** | **$256,000** |

### Budget Justification

**PI / Lead Developer (Will Nelson, 6.0 calendar months, $90,000):** The PI will lead all technical development, including platform architecture, AI model development and training, n8n workflow design, EHR integration via FHIR R4, and RPM device pipeline implementation. The PI has direct experience building classified systems on the identical technology stack (n8n + PostgreSQL + Docker on Amazon GovCloud) for Department of Defense clients, ensuring rapid development with minimal technical risk. The PI will also oversee pilot clinic deployment, IRB protocol development, and Phase I reporting.

**Co-Investigator / Clinical Advisor (1.0 calendar month, $15,000):** A board-certified physician with rural health experience will provide clinical domain expertise for AI model feature selection, risk stratification validation, clinical alert threshold design, and pilot protocol oversight. The Co-I will review all clinical logic, validate model outputs against clinical judgment, and co-author the outcomes report.

**Data Engineer (4.5 calendar months, $54,000):** Will build the PostgreSQL data model, implement row-level security, develop the RPM device data ingestion pipeline, create billing threshold tracking logic, and design cross-domain analytics materialized views. Critical for Aims 2 and 3.

**Clinical Informatics Specialist (3.0 calendar months, $36,000):** Will encode CMS billing rules into the automated billing pipeline, develop compliance task automation workflows, map clinical workflows to platform features during clinic onboarding, and validate billing accuracy. Essential for translating clinical and regulatory domain knowledge into platform logic.

**AWS GovCloud Infrastructure ($6,750):** ECS Fargate (containerized compute), RDS PostgreSQL (database), S3 (object storage), KMS (encryption key management), CloudTrail (audit logging). FedRAMP High authorization provides the highest commercially available security posture for HIPAA-regulated workloads. Estimated $750/month at pilot scale with 2--3 clinics.

**RPM Devices ($3,750):** 25 cellular-connected devices (blood pressure cuffs, glucose monitors, pulse oximeters, scales) from Tenovi at approximately $100--$150 per unit at pilot pricing. Cellular connectivity is critical for rural patients without reliable WiFi. Devices remain with patients during the pilot period.

**Provisional Patent ($5,000):** Filing provisional patent application(s) covering: (1) the unified compliance-care-revenue platform architecture; (2) the automated RPM/CCM billing threshold detection pipeline; (3) the configuration-driven multi-tenant clinic deployment model. Establishing priority date during Phase I protects commercialization pathway for Phase II.

---

## FACILITIES AND OTHER RESOURCES

### Computational Resources

- **Amazon GovCloud (US-East / US-West):** FedRAMP High authorized cloud infrastructure providing ECS Fargate (container orchestration), RDS PostgreSQL 16 (managed database with AES-256 encryption), S3 (object storage), KMS (encryption key management), CloudTrail (audit logging), and GPU instances (p3/p4 for ML training). HIPAA Business Associate Agreement in place.
- **Development Environment:** Self-hosted n8n workflow engine, Docker containerization, CI/CD pipeline (GitHub Actions), code repository (private GitHub Enterprise).

### Clinical Pilot Resources

- **Pilot Clinic Network:** Letters of support from 2--3 Virginia Rural Health Clinics willing to participate in the pilot study. Clinics selected based on: (1) EHR compatibility (eClinicalWorks or athenahealth); (2) chronic disease patient volume sufficient for 20--40 RPM enrollments per clinic; (3) administrative capacity for pilot participation; (4) geographic accessibility for on-site visits.
- **RPM Device Vendor:** Established relationship with Tenovi (40+ FDA-cleared cellular-connected monitoring devices via single API integration). Smart Meter API access as secondary vendor.

### Organizational Resources

- **Authentic Consortium (ACT):** Virginia-registered entity. All intellectual property developed under this project is owned by ACT. Technical development is performed by Veteran Vectors (VV) under ACT's direction via work-for-hire arrangement.
- **Defense Technology Transfer:** The development team has active projects deploying the identical technology stack (n8n + PostgreSQL + NGINX + Docker on Amazon GovCloud) for Department of Defense classified systems. This defense heritage provides validated deployment patterns, security hardening procedures, and operational experience directly transferable to the healthcare domain.
- **Clinical Advisory Network:** Access to practicing rural health physicians, compliance officers, and billing specialists in the Virginia RHC network for domain expertise, workflow validation, and pilot clinic recruitment.

---

## AUTHENTICATION OF KEY BIOLOGICAL AND/OR CHEMICAL RESOURCES

Not applicable. This research does not involve biological or chemical resources.

---

## CONSORTIUM / CONTRACTUAL ARRANGEMENTS

Veteran Vectors (VV) will serve as the technical development subcontractor under a work-for-hire arrangement with Authentic Consortium (ACT). All intellectual property, source code, trained models, and platform configurations developed under this project are owned exclusively by ACT. VV provides:

- Technical architecture and software development (n8n, PostgreSQL, Python/FastAPI, React/Next.js)
- AI/ML model development, training, and deployment
- Amazon GovCloud infrastructure management
- EHR integration via HL7 FHIR R4
- RPM device vendor integration
- Security hardening and HIPAA compliance engineering

The PI (Will Nelson) serves in dual capacity as ACT principal investigator and VV technical lead, ensuring alignment between research objectives and technical execution.

---

## LETTERS OF SUPPORT

*(To be obtained prior to submission)*

1. **Pilot Clinic #1:** Letter from Medical Director confirming participation, EHR details, chronic disease patient volume, and willingness to support RPM enrollment
2. **Pilot Clinic #2:** Letter confirming participation and clinic-specific details
3. **Pilot Clinic #3 (optional):** Letter confirming participation
4. **Tenovi (RPM Device Vendor):** Letter confirming API access, device pricing, and cellular connectivity coverage in pilot clinic areas
5. **Clinical Advisor:** Letter from Co-Investigator confirming role and commitment

---

## RESOURCE SHARING PLAN

- **Software:** The 3C Platform core architecture will be maintained as proprietary software owned by ACT for commercialization. However, the research team commits to publishing:
  - De-identified model performance metrics and validation methodology
  - The cross-domain interaction framework (compliance-care-revenue linkage model)
  - Clinical decision support design patterns for rural health applications
- **Data:** De-identified, aggregated pilot data will be deposited in an appropriate NIH-designated repository within 12 months of study completion, consistent with NIH Data Sharing Policy and HIPAA de-identification standards (Safe Harbor method).
- **Publications:** Research findings will be submitted for publication in peer-reviewed journals (target: JAMIA, Journal of Rural Health, npj Digital Medicine) within 12 months of Phase I completion.

---

## PHASE II COMMERCIALIZATION PLAN

### Market Opportunity

| Metric | Virginia | National |
|---|---|---|
| Rural Health Clinics (+ FQHCs) | 106 RHCs + 27 FQHCs | 5,500+ RHCs |
| Estimated SaaS Revenue per Clinic | $500--$4,000/month (3 tiers) | $500--$4,000/month |
| Virginia Total Addressable Market | $3.2M--$6.4M/year | -- |
| National Total Addressable Market | -- | $132M--$264M/year |
| Revenue Unlock per Clinic | $195K--$267K/year | -- |

### Commercialization Strategy

**Phase II (Months 10--18):** Expand from 2--3 pilot clinics to 10+ Virginia RHCs. Harden all three service tiers. Add additional EHR integrations (MEDITECH, Azalea Health, TruBridge). Implement NLP coding optimization (Phase 2 feature), telehealth orchestration, and denial prevention. Convert provisional patent to utility patent. Target: $200K+ ARR from paying clinics.

**Phase III (Months 19--36):** Multi-region GovCloud deployment. Automated onboarding (<1 day per clinic). Scale to 50+ clinics across Virginia, then national expansion (West Virginia, Kentucky, Tennessee, North Carolina). Series A fundraise based on ARR, clinical outcome data, and patent portfolio. Target: $1M+ ARR.

### Service Tier Model

| Tier | Modules | Target Clinic | Price |
|---|---|---|---|
| **Essentials** | Compliance Module only | Small RHCs (<500 patients) | $500--$1,000/month |
| **Professional** | Compliance + Care (RPM, AI risk stratification) | Mid-size RHCs (500--1,500 patients) | $1,500--$2,500/month |
| **Enterprise** | All 3 modules (Compliance + Care + Collect Cash) | Larger RHCs/FQHCs (1,500+ patients) | $2,500--$4,000/month |

### Unit Economics

- **Per-clinic infrastructure cost at scale:** $100--$150/month (open-source stack, shared GovCloud resources)
- **Gross margin at $2,000/month subscription:** 93--95%
- **Customer ROI:** Clinic subscription of $24,000--$48,000/year unlocks $195,000--$267,000/year in previously unrealized CMS reimbursement (8--11x return)
- **No vendor lock-in:** Platform built on open-source components (n8n, PostgreSQL, Docker). No enterprise licensing dependencies.

---

## BIOGRAPHICAL SKETCH

*(Standard NIH Biosketch format -- to be completed per NIH Biosketch guidelines)*

**Will Nelson, Principal Investigator**

**Position Title:** Technical Lead, Veteran Vectors; Principal Investigator, Authentic Consortium

**Education/Training:**
*(To be populated per applicant's credentials)*

**Personal Statement:**
I lead the technical development of AI-driven platforms for both defense and healthcare applications. My team currently builds classified systems on Amazon GovCloud using the identical technology stack proposed for this research (n8n, PostgreSQL, Docker, Python/FastAPI). This defense experience provides validated deployment patterns, security hardening expertise, and operational discipline directly transferable to HIPAA-regulated healthcare environments. I am uniquely positioned to execute this research because I combine hands-on technical capability in AI/ML, cloud architecture, and workflow automation with a deep understanding of the rural health clinic operational environment through our partnership with Virginia RHC networks. The proposed research directly extends our proven defense technology stack to address a critical gap in rural healthcare infrastructure.

**Contributions to Science:**
*(To be populated with relevant publications, presentations, and project outcomes)*

---

## SPECIFIC AIMS PAGE SUMMARY

| Element | Content |
|---|---|
| **Problem** | 62M rural Americans served by clinics facing compounding compliance, care, and revenue crises; 3 Virginia RHCs closed in 2025 |
| **Gap** | No integrated platform addresses compliance + care + revenue as unified system for RHCs |
| **Long-term Goal** | Validate AI-driven integrated 3C Platform for national RHC deployment |
| **Aim 1** | AI risk stratification engine (XGBoost + SHAP, AUC-ROC > 0.75) |
| **Aim 2** | RPM data ingestion + automated CMS billing pipeline (> 90% capture rate) |
| **Aim 3** | Unified compliance-care-revenue data architecture with cross-domain feedback loops |
| **Impact** | Feasibility demonstration for Phase II national expansion; addresses NIH health disparities, rural health, digital innovation priorities |

---

*Prepared by: Authentic Consortium / Veteran Vectors*
*Version 1.0 -- February 25, 2026*
