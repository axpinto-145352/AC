# NIH SBIR PHASE I PROPOSAL

**Title:** AI-Driven Integrated Compliance, Care, and Revenue Optimization Platform for Rural Health Clinics

**Funding Opportunity:** NIH SBIR Phase I (R43)
**Applicant Organization:** Authentic Consortium (ACT)
**Principal Investigator / Program Director:** Will Nelson
**Requested Budget:** $256,000 (Direct Costs) over 9 months
**Proposed Start Date:** October 1, 2026
**NIH Institute (Primary):** National Institute on Minority Health and Health Disparities (NIMHD)
**NIH Institute (Secondary):** National Institute of General Medical Sciences (NIGMS)
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

**Hypothesis:** An XGBoost ensemble model incorporating clinical, social determinant, and utilization features will achieve AUC-ROC >= 0.75 and sensitivity >= 80% for the highest-risk decile when predicting 90-day hospitalization or ED visit among rural chronic disease patients, significantly exceeding a logistic regression baseline (paired DeLong test, alpha = 0.05).

### Aim 2: Build and Pilot an Integrated RPM Data Ingestion and Automated CMS Billing Pipeline

Design and deploy a system that ingests continuous physiological data from cellular-connected RPM devices (blood pressure, glucose, pulse oximetry, weight), detects clinical deterioration trends via temporal analytics, and automatically tracks CMS billing thresholds (16-day transmission minimum for CPT 99454, 20-minute clinician interaction for CPT 99457/99458, CCM time thresholds for CPT 99490). **Success criterion:** Automated capture of > 90% of billable RPM/CCM events across pilot clinics, with a projected revenue increase of $195,000--$267,000 per clinic per year in previously unrealized CMS reimbursement.

**Hypothesis:** An automated device-to-billing pipeline will capture >= 90% of billable RPM/CCM events (measured against manual chart review as gold standard), with a false-positive billing event rate < 5%, enabling a statistically significant increase in monthly RPM/CCM revenue per clinic compared to pre-deployment baseline (paired t-test, alpha = 0.05).

### Aim 3: Design and Evaluate a Unified Compliance-Care-Revenue Data Architecture with Cross-Domain Feedback Loops

Create a shared data model (PostgreSQL with row-level security for multi-tenant clinic isolation) where compliance status, clinical care activities, and revenue cycle data interconnect -- enabling automated identification of how compliance gaps affect reimbursement, how care activities generate billable events, and how revenue trends predict compliance risk. **Success criterion:** Demonstrate at least 3 measurable cross-domain interactions (e.g., compliance documentation completeness correlating with claims acceptance rate) validated in pilot clinic data.

**Hypothesis:** A unified data architecture will reveal at least 3 statistically significant cross-domain correlations (Pearson r > 0.3, p < 0.05 after Bonferroni correction for multiple comparisons) between compliance, care, and revenue variables (e.g., compliance task completion rate inversely correlated with claims denial rate) that are not detectable in siloed data systems.

**Impact:** If successful, this Phase I research will demonstrate the feasibility of an integrated AI-driven platform that transforms rural health clinic operations from reactive to proactive -- addressing health disparities affecting 62 million rural Americans. Phase II will expand to 50+ clinics across Appalachian states (Virginia, West Virginia, Kentucky, Tennessee, North Carolina), conduct an adequately powered prospective clinical outcome study, and prepare for FDA regulatory pathway assessment. The research addresses NIH priorities in health disparities reduction, rural health, digital health innovation, and AI-driven clinical decision support, while validating a scalable approach applicable to 5,500+ Rural Health Clinics nationally.

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

The 3C Platform introduces a **novel unified data architecture** (provisional patent application planned for filing during Phase I to establish priority date) where compliance, care, and revenue data share a single PostgreSQL data model with row-level security for multi-tenant clinic isolation. This is technically novel because:

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

**This technology stack is proven in production environments.** The development team currently builds classified systems for a defense client on this exact architecture (n8n + PostgreSQL + NGINX + Docker on GovCloud), with deployment paths from unclassified through TS/SCI. The 3C Platform applies the same proven components to healthcare.

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
  - CPT 99453 (initial RPM device setup): One-time billing at patient enrollment
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

#### C.7 Statistical Analysis Plan

**Aim 1 -- Model Validation:**
- **Primary metric:** AUC-ROC for 90-day hospitalization/ED visit prediction, with 95% confidence intervals computed via bootstrapping (2,000 iterations). Model comparison via paired DeLong test (XGBoost vs. logistic regression baseline, alpha = 0.05).
- **Sample size justification:** Using the method of Obuchowski (1994), with anticipated AUC = 0.78, prevalence of outcome = 15% (based on CMS readmission data for chronic disease), and desired confidence interval width of +/- 0.05, a minimum of 80 outcome events is required. With 50--100 RPM patients over 5 months of prospective tracking, and an estimated 15% event rate, we expect 8--15 events. **Limitation:** This Phase I sample is underpowered for definitive model validation; the primary endpoint is feasibility demonstration with Phase II providing adequately powered validation across 50+ clinics. CMS public use file pre-training (n > 100,000) provides the statistical foundation; pilot data validates transfer to the clinical deployment context.
- **Secondary metrics:** Sensitivity, specificity, positive predictive value, calibration (Hosmer-Lemeshow test and calibration curves), Brier score, AUC-PR, and decision curve analysis for clinical utility.
- **Fairness analysis:** Equalized odds and demographic parity computed per subgroup (age, race/ethnicity, rural isolation quartile). Disparity threshold: absolute difference in TPR or FPR > 0.05 triggers bias review and potential retraining with fairness constraints.
- **Comparison baselines:** LACE Index (Length of stay, Acuity, Comorbidities, Emergency visits) and HOSPITAL Score as established clinical risk prediction benchmarks.

**Aim 2 -- Billing Pipeline Validation:**
- **Primary metric:** Billing event capture rate (automated/total billable events identified via manual chart review). Target: >= 90%. Confidence interval via exact binomial test.
- **Secondary metrics:** False-positive billing event rate (target: < 5%), time savings (automated vs. manual billing identification in staff-hours/month), revenue delta (paired t-test, pre-deployment baseline vs. post-deployment monthly revenue, alpha = 0.05).
- **Sample size:** With 50--100 patients generating an estimated 3--5 billing events per patient per month, we expect 150--500 billing events per month for accuracy assessment.

**Aim 3 -- Cross-Domain Correlations:**
- **Primary analysis:** Pearson correlation coefficients with Bonferroni correction for 5 pre-specified cross-domain relationships (corrected alpha = 0.01). Target: at least 3 of 5 achieve r > 0.3 with p < 0.01.
- **Exploratory analysis:** Interrupted time series analysis (pre/post platform deployment) using segmented regression to assess trend changes in compliance scores, billing capture rates, and clinical outcomes.
- **Multiple comparison correction:** Bonferroni adjustment for all pre-specified analyses. Exploratory analyses reported with unadjusted p-values and flagged as hypothesis-generating.
- **Missing data:** Multiple imputation (5 imputations) for covariates missing at random; sensitivity analysis with complete cases.

#### C.8 Data Safety Monitoring Plan

Given that this research involves AI-driven clinical decision support that may influence provider actions, the following safety monitoring plan will be implemented:

- **Safety Monitor:** The Co-Investigator (physician) will serve as the independent Data Safety Monitor, reviewing all clinical alerts, model outputs, and adverse events.
- **Monitoring frequency:** Monthly during the active pilot period (Months 4--9). Ad hoc review within 24 hours for any serious adverse event.
- **Adverse event definitions:**
  - **Serious:** Hospitalization, ED visit, or clinical deterioration that occurred despite the platform generating an alert (system failure) or that was potentially attributable to a false-negative alert (missed risk).
  - **Non-serious:** False-positive alerts causing unnecessary clinical follow-up; patient anxiety from monitoring; device malfunction.
- **Reporting:** Serious adverse events reported to IRB within 5 business days and to NIH per reporting requirements. Non-serious events documented in quarterly monitoring reports.
- **Stopping rules:** The pilot will pause enrollment and undergo full safety review if: (a) any patient death potentially related to platform failure; (b) 3 or more serious adverse events in any 30-day period; (c) false-negative alert rate exceeds 20% (provider-assessed).
- **Provider authority:** All platform outputs (risk scores, deterioration alerts, billing recommendations) are advisory only. The licensed provider retains full clinical decision authority. The platform does not make autonomous clinical decisions or withhold information from providers.

#### C.9 Preliminary Data

While this proposal describes the Phase I research program, the applicant organization has relevant preliminary data supporting feasibility:

1. **Defense platform deployment:** The development team has successfully deployed the identical technology stack (n8n + PostgreSQL + NGINX + Docker on Amazon GovCloud) for a classified Department of Defense client, validating the infrastructure, security controls, and deployment methodology. This production experience with GovCloud, containerized deployments, and HIPAA-equivalent security controls (NIST 800-171 / CMMC) directly transfers to the healthcare domain.

2. **CMS public use file analysis:** Preliminary analysis of CMS Medicare Provider Utilization data and Chronic Conditions Prevalence files demonstrates the predictive signal available in the training data. Initial XGBoost models trained on CMS hospitalization data achieve AUC-ROC > 0.70 using demographic, diagnostic, and utilization features alone, suggesting that enrichment with EHR clinical data and RPM device data in the pilot will enable the > 0.75 target.

3. **VIPC VVP Launch Grant:** ACT has been selected as a finalist for the Virginia Innovation Partnership Corporation (VIPC) VVP Launch Grant ($50,000), which funds initial MVP development and pilot clinic deployment. If awarded, the VIPC-funded MVP (4-month timeline) will provide a functional platform baseline that the NIH SBIR research builds upon, significantly reducing technical risk for the SBIR Phase I research activities.

4. **Pilot clinic engagement:** Letters of intent have been obtained from Virginia Rural Health Clinics expressing interest in pilot participation, confirming access to the clinical environment, EHR systems, and patient populations required for the research.

#### C.10 References

1. Gong G, Phillips SG, Hudson C, et al. Higher US rural mortality rates linked to socioeconomic status, physician shortages, and lack of health insurance. *Health Affairs*. 2019;38(12):2003-2010.
2. Hung P, Henning-Smith CE, Casey MM, Kozhimannil KB. Access to obstetric services in rural counties still declining. *Health Affairs*. 2017;36(9):1663-1671.
3. Noah B, Keller MS, Mosadeghi S, et al. Impact of remote patient monitoring on clinical outcomes: an updated meta-analysis of randomized controlled trials. *NPJ Digital Medicine*. 2018;1:20172.
4. Chen T, Guestrin C. XGBoost: A scalable tree boosting system. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. 2016:785-794.
5. Lundberg SM, Lee SI. A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems*. 2017;30.
6. Obermeyer Z, Powers B, Vogeli C, Mullainathan S. Dissecting racial bias in an algorithm used to manage the health of populations. *Science*. 2019;366(6464):447-453.
7. Obuchowski NA. Computing sample size for receiver operating characteristic studies. *Investigative Radiology*. 1994;29(2):238-243.
8. Centers for Medicare & Medicaid Services. Rural Health Clinic (RHC) Center. 2025. Accessed February 2026.
9. Douthit N, Kiv S, Dwolatzky T, Biswas S. Exposing some important barriers to health care access in the rural USA. *Public Health*. 2015;129(6):611-620.
10. Kvedar JC, Coye MJ, Everett W. Connected health: a review of technologies and strategies to improve patient care with telemedicine and telehealth. *Health Affairs*. 2014;33(2):194-199.

#### C.11 Human Subjects Considerations

This research involves collection and analysis of protected health information (PHI) from pilot clinic patients enrolled in RPM programs. The research qualifies for expedited IRB review as minimal risk (no intervention beyond standard-of-care RPM monitoring).

**a) Risks to Subjects:**
- **Privacy risk:** Collection and storage of PHI including vital signs, diagnoses, and demographic data. Mitigated by HIPAA-compliant Amazon GovCloud infrastructure with AES-256 encryption, row-level security, and PGAudit logging.
- **Clinical risk (minimal):** AI risk scores and deterioration alerts are advisory only -- all clinical decisions remain with the licensed provider. False positive alerts may cause unnecessary follow-up; false negatives are mitigated by maintaining existing care protocols alongside the platform.
- **Digital equity risk:** Participants may face digital literacy barriers. Mitigated by zero-configuration cellular devices and clinic staff-assisted enrollment.

**b) Adequacy of Protection Against Risks:**
- **IRB Review:** Full IRB protocol submission prior to pilot clinic deployment (Month 3). Anticipate expedited review under 45 CFR 46.110 Category 7 (research on individual or group characteristics).
- **Informed Consent:** Three-stage consent process: (1) Clinical consent for RPM monitoring; (2) Medicare-specific consent for RPM billing; (3) Research consent for de-identified data use in model validation. Consent forms in plain language at 6th-grade reading level. Participants may withdraw at any time without affecting their clinical care.
- **Data Protection:** All PHI stored in HIPAA-compliant Amazon GovCloud (FedRAMP High). AES-256 encryption at rest, TLS 1.2+ in transit, PostgreSQL row-level security for clinic isolation, PGAudit for complete audit trails. De-identified datasets (HIPAA Safe Harbor method) used for model training, validation, and publication.
- **PHI access restricted** to authorized clinic staff and research team with role-based access controls. Audit trails for all data access. Annual HIPAA Security Risk Assessment per NIST SP 800-66.
- **Data Safety Monitoring:** Quarterly data safety review by PI and Co-Investigator. Adverse event reporting to IRB within 5 business days (serious) or at next continuing review (minor). Protocol deviation documentation and reporting per IRB requirements.

**c) Potential Benefits:**
- **Direct benefits to participants:** Continuous RPM monitoring between clinic visits, earlier detection of clinical deterioration, proactive care coordination, and potential revenue generation for their clinic (sustaining rural healthcare access).
- **Benefits to the community:** Validated technology for improving rural health outcomes, reducing preventable hospitalizations, and strengthening rural clinic financial viability.

**d) Importance of Knowledge to Be Gained:**
The knowledge gained from this research -- validated AI risk stratification for rural populations, demonstrated cross-domain compliance-care-revenue interactions, and proven automated RPM billing capture -- addresses a significant gap in rural health informatics. The potential benefits to 62 million rural Americans served by RHCs outweigh the minimal risks to individual participants.

**e) Inclusion of Women, Minorities, and Children:**
- **Women:** Expected to constitute approximately 55% of enrolled RPM patients based on rural RHC demographics. No exclusion by sex.
- **Minorities:** Pilot clinics serve diverse rural populations. Enrollment will reflect clinic demographics. Fairness metrics (equalized odds, demographic parity) will be computed across available race/ethnicity categories to ensure the AI model does not produce disparate predictions.
- **Children:** Excluded. RPM enrollment targets adult patients (18+) with chronic conditions (hypertension, diabetes, CHF, COPD). Pediatric chronic disease management in RHCs has different clinical protocols and billing rules requiring separate study design.
- **PHS Inclusion Enrollment Report:** Will be completed and submitted with the application, reflecting projected enrollment demographics based on pilot clinic patient populations.

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
| Participant support costs (patient device training materials) | $2,000 |
| **Subtotal Direct Costs** | $231,000 |
| *Note: Participant support costs ($2,000) are excluded from indirect cost base per NIH policy* | |
| **Indirect Costs (estimated 10.9% of modified total direct costs)** | $25,000 |
| **TOTAL** | **$256,000** |

### Budget Justification

**PI / Lead Developer (Will Nelson, 6.0 calendar months, $90,000):** The PI will lead all technical development, including platform architecture, AI model development and training, n8n workflow design, EHR integration via FHIR R4, and RPM device pipeline implementation. The PI has direct experience building classified systems on the identical technology stack (n8n + PostgreSQL + Docker on Amazon GovCloud) for Department of Defense clients, ensuring rapid development with minimal technical risk. The PI will also oversee pilot clinic deployment, IRB protocol development, and Phase I reporting.

**Co-Investigator / Clinical Advisor (1.0 calendar month, $15,000):** A board-certified physician with rural health experience will provide clinical domain expertise for AI model feature selection, risk stratification validation, clinical alert threshold design, and pilot protocol oversight. The Co-I will review all clinical logic, validate model outputs against clinical judgment, and co-author the outcomes report.

**Data Engineer (4.5 calendar months, $54,000):** Will build the PostgreSQL data model, implement row-level security, develop the RPM device data ingestion pipeline, create billing threshold tracking logic, and design cross-domain analytics materialized views. Critical for Aims 2 and 3.

**Clinical Informatics Specialist (3.0 calendar months, $36,000):** Will encode CMS billing rules into the automated billing pipeline, develop compliance task automation workflows, map clinical workflows to platform features during clinic onboarding, and validate billing accuracy. Essential for translating clinical and regulatory domain knowledge into platform logic.

**AWS GovCloud Infrastructure ($6,750):** ECS Fargate (containerized compute), RDS PostgreSQL (database), S3 (object storage), KMS (encryption key management), CloudTrail (audit logging). FedRAMP High authorization provides the highest commercially available security posture for HIPAA-regulated workloads. Estimated $750/month at pilot scale with 2--3 clinics.

**RPM Devices ($3,750):** 25 cellular-connected devices (blood pressure cuffs, glucose monitors, pulse oximeters, scales) from Tenovi at approximately $150 per unit at negotiated pilot pricing. Cellular connectivity is critical for rural patients without reliable WiFi. Devices remain with patients during the pilot period.

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

**SBIR Work Performance Requirement:** A minimum of 67% of the research effort (measured by direct costs for personnel and other direct costs attributable to the applicant organization) will be performed by Authentic Consortium (ACT) and its affiliated personnel. VV operates as a subcontractor under ACT's direction; the combined ACT/VV effort constitutes the applicant organization's performance. This arrangement satisfies the SBIR Phase I minimum work requirement per SBA regulations (13 CFR 121.702).

---

## SBIR ELIGIBILITY

Authentic Consortium (ACT) certifies that it meets all SBIR eligibility requirements:

- **Small Business Concern:** ACT is a Virginia-registered small business with fewer than 500 employees, meeting the SBA size standard for SBIR eligibility.
- **U.S. Ownership and Control:** ACT is majority-owned and controlled by U.S. citizens or permanent residents.
- **Principal Place of Performance:** All research will be performed in the United States.
- **67% Work Performance (Phase I):** A minimum of 67% of research effort will be performed by the applicant organization (ACT and its affiliated technical team).
- **SBIR/STTR Funding Agreement Certification:** ACT will execute the required SBIR Funding Agreement Certification at the time of award.

---

## VERTEBRATE ANIMALS

Not applicable. This research does not involve vertebrate animals.

---

## INCLUSION OF WOMEN AND MINORITIES

This research will enroll adult patients with chronic conditions (hypertension, diabetes, CHF, COPD) at pilot Rural Health Clinics in Virginia. Enrollment will reflect the demographic composition of the pilot clinic patient populations.

**Expected enrollment demographics** (based on Virginia rural RHC population data):
- **Sex/Gender:** Approximately 55% female, 45% male. No exclusion by sex or gender.
- **Race/Ethnicity:** Enrollment will reflect pilot clinic demographics. Virginia rural populations include significant representation of non-Hispanic White, non-Hispanic Black, and Hispanic/Latino populations. No exclusion by race or ethnicity.
- **Recruitment:** Clinic staff will identify eligible patients (chronic disease diagnosis, provider recommendation for RPM) and offer enrollment regardless of sex, race, or ethnicity. Recruitment materials will be available in English and Spanish.
- **Analysis:** Model performance (AUC-ROC, sensitivity, fairness metrics) will be stratified by sex and available race/ethnicity categories. Any disparities exceeding predefined thresholds (equalized odds difference > 0.05) will be investigated, documented, and addressed through model retraining with fairness constraints.
- **PHS Inclusion Enrollment Report:** Will be submitted with the application reflecting projected enrollment demographics.

---

## INCLUSION OF CHILDREN

Children (individuals under 18 years of age) are **excluded** from this research. Justification:

1. **Clinical scope:** The RPM program targets adult chronic conditions (hypertension, Type 2 diabetes, CHF, COPD) that are predominantly adult-onset diseases. Pediatric chronic disease management involves different clinical protocols, medication regimens, and monitoring thresholds.
2. **CMS billing:** RPM/CCM billing codes (CPT 99453, 99454, 99457, 99458, 99490) apply to Medicare beneficiaries, who are predominantly adults aged 65+. Pediatric RPM billing follows different pathways (Medicaid EPSDT) requiring separate platform logic.
3. **IRB considerations:** Inclusion of children would require additional consent procedures (parental consent, child assent) and pediatric-specific safety monitoring that are outside the scope of this Phase I feasibility study.
4. **Phase II consideration:** Pediatric chronic disease management in rural settings may be addressed in Phase II or subsequent research if Phase I demonstrates feasibility of the adult platform.

---

## OTHER SUPPORT

*(To be completed at time of submission with current and pending support for all Senior/Key Personnel)*

**Will Nelson (PI):**
- **Active:** VIPC VVP Launch Grant (if awarded), $50,000, March 2026 -- June 2026. Role: PI/Technical Lead. Scope: MVP development of 3C Platform for 2--3 Virginia RHC pilots. *Overlap assessment:* The VIPC grant funds initial platform MVP development (4 months) and is expected to conclude before the NIH SBIR start date (October 2026). The NIH SBIR Phase I builds upon the VIPC-funded platform baseline to conduct formal research validation. No overlap in effort or scope.
- **Pending:** This NIH SBIR Phase I application, $256,000, October 2026 -- June 2027.

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

## DATA MANAGEMENT AND SHARING PLAN

Per the NIH Data Management and Sharing Policy (effective January 25, 2023), this plan describes how scientific data generated during this project will be managed and shared.

### Data Types and Scope

| Data Type | Format | Volume | Sharing Applicability |
|---|---|---|---|
| CMS public use files (training data) | CSV/Parquet | ~5 GB | Already public; no sharing required |
| EHR clinical data (pilot clinics) | FHIR R4 JSON | ~500 MB/clinic | PHI -- share de-identified only |
| RPM device readings | JSON/PostgreSQL | ~100 MB/month | PHI -- share de-identified only |
| AI model performance metrics | CSV/JSON | ~50 MB | Shareable (no PHI) |
| Cross-domain correlation analyses | CSV/JSON | ~10 MB | Shareable (aggregate, no PHI) |
| Billing event data | PostgreSQL | ~10 MB/month | PHI -- share de-identified only |
| Trained model weights | Binary (pickle/ONNX) | ~100 MB | Trade secret -- not shared |

### De-identification Method

All shared datasets will be de-identified using the **HIPAA Safe Harbor method** (45 CFR 164.514(b)(2)), removing all 18 categories of identifiers. Date shifting (random offset per patient, preserving intervals) will be applied to temporal data. Geographic data will be generalized to state level.

### Repository and Timeline

- **Primary repository:** NIH-designated repository (NCBI dbGaP for controlled-access clinical data; Zenodo or Dryad for model performance data and analysis code)
- **Timeline:** De-identified datasets deposited within 12 months of Phase I completion; updated with Phase II data as generated
- **Access:** Model performance metrics and aggregate cross-domain analyses available under open access. De-identified clinical data available via controlled access through dbGaP with DUA requirement.
- **Metadata:** All datasets accompanied by data dictionaries, codebooks, and methodology documentation sufficient for independent analysis.

### Data Preservation

- **Active project:** All data stored in HIPAA-compliant Amazon GovCloud with automated backups, 30-day snapshot retention, and cross-region replication
- **Post-project:** De-identified research datasets preserved in designated repository for minimum 10 years. PHI destroyed via cryptographic erasure (KMS key deletion) within 6 months of project closure, per HIPAA retention requirements and clinic agreements.

### Oversight

The PI will be responsible for implementing this DMS Plan. Compliance will be reviewed at each quarterly progress report.

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
