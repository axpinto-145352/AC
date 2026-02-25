# PEER REVIEW: NIH SBIR Phase I Implementation Plan

**Document Reviewed:** `02_NIH_Implementation_Plan.md`
**Reviewer Role:** NIH Program Officer / Research Implementation Reviewer
**Review Date:** February 25, 2026
**Source Documents Cross-Referenced:**
- `VIPC/01_VV_Technical_Brief.md` (VIPC VVP Launch Grant presentation brief)
- `VIPC/02_Implementation_Guide.md` (VIPC implementation guide, $50K scope)

---

## 1. EXECUTIVE ASSESSMENT

**Overall Rating: STRONG with Reservations**

This implementation plan demonstrates a well-organized engineering approach to translating the commercially oriented 3C Platform (developed under the VIPC VVP Launch Grant) into a research-grade NIH SBIR Phase I project. The plan is technically detailed, correctly scoped to a 9-month / $256K budget, and appropriately identifies the key difference from the VIPC project: the addition of formal research methodology, IRB oversight, human subjects protections, and statistical evaluation.

**Feasibility:** The core technical platform is plausible and built on proven open-source components. The plan benefits from the assertion that the VIPC-funded MVP will precede or overlap with the SBIR work, reducing technical risk. However, the plan does not clearly articulate the dependency between the two funding streams -- whether the VIPC MVP must be complete before the SBIR starts, or whether they run in parallel. This ambiguity introduces significant schedule risk.

**Completeness:** The plan covers all essential domains -- architecture, sprint plan, team, budget, data management, QA, regulatory, and risk management. It is missing several elements that NIH reviewers will expect: (1) a formal Gantt chart or dependency diagram, (2) a human subjects protection narrative beyond the IRB summary table, (3) letters of support or clinic commitment documentation, (4) a formal statistical analysis plan with power calculations, and (5) an explicit Data Safety Monitoring Plan (DSMP).

**SBIR Alignment:** The plan correctly frames the work as research validation of an existing technology platform. The three-aim structure (AI risk stratification, RPM integration/billing, cross-domain interactions) maps well to a Phase I feasibility study. However, the plan reads more like a software engineering build document than a research protocol. The research hypotheses, study design, outcome variables, and analytical approach are insufficiently articulated for NIH review standards.

**Key Concern:** The plan relies on a single PI (Will Nelson) for 6.0 calendar months of effort covering architecture, AI/ML development, n8n workflows, EHR/FHIR integration, RPM pipeline, GovCloud deployment, research protocol design, and the final report. This is an extraordinary scope of responsibility for one person. While the PI may be exceptionally capable, NIH reviewers will flag the bus-factor risk and question whether the research dimensions receive adequate attention when the PI is simultaneously responsible for all engineering.

---

## 2. SPRINT PLAN EVALUATION

### 2.1 Overall Structure

The 18-sprint plan over 9 months is well-organized and follows a logical progression: infrastructure (Sprints 1-2), development (Sprints 3-6), pilot deployment (Sprints 7-11), and evaluation/reporting (Sprints 12-18). The overlapping aims across sprints reflect realistic parallelism.

### 2.2 Timeline Concerns

**IRB Timing is Critically Optimistic:**
- The plan schedules IRB protocol drafting in Sprint 1 and submission in Sprint 5 (Month 3). However, IRB expedited review typically takes 2-6 weeks after submission, and revisions commonly add another 2-4 weeks. The plan assumes IRB approval by end of Sprint 6 (Month 3), which leaves zero margin for revisions.
- Pilot Clinic 1 onboarding is scheduled for Sprint 7 (Month 4, Weeks 1-2), requiring IRB approval, EHR integration, device procurement, staff training, and consent process establishment -- all within 2 weeks of presumed IRB clearance. This is unrealistic.
- **Recommendation:** Move IRB protocol drafting to pre-award or Week 1, and submit by Sprint 3 (Month 2) at the latest. Add a 4-week IRB buffer between submission and pilot clinic go-live.

**EHR Integration Underestimated:**
- Sprint 3 initiates EHR FHIR R4 integration with "sandbox" access. Sprint 7 targets live EHR data flowing from Clinic 1. The 8-week window from sandbox to production EHR integration is aggressive, particularly for eClinicalWorks or athenahealth, which require developer program enrollment (2-4 weeks), sandbox provisioning (1-2 weeks), and production credentialing (2-6 weeks).
- Risk R1 acknowledges this but only budgets "2 extra weeks." Based on real-world FHIR integration timelines, 4-6 extra weeks is more appropriate.
- **Recommendation:** Begin EHR developer program enrollment in pre-award. Add explicit milestones for sandbox access, production credentialing, and data validation between Sprints 3 and 7.

**Pilot Enrollment Ramp is Aggressive:**
- Clinic 1 goes live in Sprint 8 (Month 4), Clinic 2 in Sprint 9 (Month 5), and Clinic 3 (optional) in Sprint 11 (Month 6). The plan targets 50-100 RPM patients across sites.
- RPM enrollment in rural clinics typically proceeds slowly -- patients must consent to clinical RPM, Medicare RPM billing, AND research participation (three consent hurdles). Achieving 50+ enrolled patients by Month 6 requires approximately 8-10 patients/week enrollment rate across sites, which is ambitious for rural clinics with limited staff.
- **Recommendation:** Provide enrollment projections by month with milestones. Define minimum viable enrollment (e.g., 30 patients) for meaningful statistical analysis. Add enrollment incentive details.

**Evaluation Phase is Compressed:**
- Sprints 13-16 (Months 7-8) attempt model performance evaluation, revenue impact measurement, bias audit, and cross-domain analysis -- each in a single 2-week sprint. These are analytically intensive tasks that typically require iterative analysis, review, and revision.
- The cross-domain analysis (Sprint 16) requires sufficient accumulated data. With pilot clinics operational for only 2-4 months by this point, the sample sizes for interrupted time-series analysis and cross-domain correlations may be insufficient.
- **Recommendation:** Begin preliminary analysis earlier (Sprint 11-12) to identify data gaps. Extend evaluation into Sprint 17. Provide minimum data requirements for each analysis.

### 2.3 Sprint Dependencies Not Explicit

The plan lacks a dependency diagram. Several implicit dependencies are not called out:

- Sprint 5 (IRB submission) depends on Sprint 1 (IRB draft) but also on clinical advisor input, clinic identification, and consent form finalization -- none of which are tracked as sprint deliverables.
- Sprint 7 (Clinic 1 onboarding) depends on IRB approval (Sprint 5-6), device procurement, EHR integration (Sprint 3-4), and staff training materials -- a convergence of multiple workstreams.
- Sprint 12 (cross-domain analytics) depends on sufficient accumulated pilot data from Sprints 8-11 -- but no minimum data volume is specified.

**Recommendation:** Add a dependency table or PERT chart showing critical path items and float.

---

## 3. TEAM STRUCTURE REVIEW

### 3.1 Staffing Adequacy

The team is lean -- four funded positions totaling 14.5 person-months for a 9-month project. This is typical for an SBIR Phase I ($256K), but the distribution of responsibilities raises concerns.

**PI (Will Nelson, 6.0 calendar months):**
- The PI carries virtually all technical, engineering, and research responsibilities. This includes: platform architecture, AI/ML model development, n8n workflow design, EHR/FHIR integration, RPM data pipeline, GovCloud infrastructure, research protocol design, statistical analysis, and final report authorship.
- At 6.0 calendar months over 9 months, this implies 67% effort. For a sole-developer, sole-PI role, this is insufficient for the scope described. The plan essentially requires a full-stack engineer AND a research scientist AND a data scientist AND a systems architect AND a project manager -- all in one person at two-thirds time.
- **Recommendation:** Increase PI effort to 8.0-9.0 calendar months (near full-time) or redistribute engineering tasks to the Data Engineer. Alternatively, add a part-time Research Coordinator role to handle IRB management, consent tracking, enrollment logistics, and data quality monitoring.

**Co-Investigator / Clinical Advisor (TBD, 1.0 calendar month):**
- One calendar month of clinical advisor effort across 9 months is very thin. This person must provide clinical domain expertise, validate model features, design alert thresholds, oversee the pilot protocol, and co-author the outcomes report.
- Being TBD at proposal submission is a significant weakness. NIH reviewers strongly prefer named investigators with biosketches.
- **Recommendation:** Name the Co-I before submission. Increase effort to 2.0-3.0 calendar months to cover clinical workflow validation during pilot operations (Months 4-6).

**Data Engineer (TBD, 4.5 calendar months):**
- Adequate effort for the described scope, but being TBD weakens the proposal.
- **Recommendation:** Name the candidate or provide hiring criteria and timeline.

**Clinical Informatics Specialist (TBD, 3.0 calendar months):**
- Appropriate for billing logic, compliance workflows, and consent management. However, 3.0 months is tight for encoding CMS billing rules AND managing consent workflows AND validating billing accuracy across the pilot period.
- **Recommendation:** Consider increasing to 4.0 months or splitting the consent/IRB duties to a coordinator role.

### 3.2 Missing Roles

- **Biostatistician:** The plan describes AUC-ROC analysis, fairness metrics, interrupted time-series, cross-domain correlations, and statistical significance testing. No biostatistician is identified. The PI appears to self-serve all statistical analysis. NIH reviewers will want to see statistical expertise, especially for the Aim 3 cross-domain analysis.
- **Research Coordinator:** No one is explicitly responsible for IRB management, consent tracking, enrollment logistics, adverse event monitoring, or data quality oversight. These are non-trivial in a human subjects study.
- **Recommendation:** Add a part-time biostatistician (0.5-1.0 calendar months, can be consultant) and a research coordinator (1.0-2.0 calendar months).

### 3.3 Advisory Roles

The unfunded advisory roles (Pilot Clinic Medical Directors, Compliance Officer, Billing Manager, IRB Liaison) are appropriate but should include estimated time commitments and letters of support confirming their participation.

---

## 4. BUDGET EXECUTION

### 4.1 Monthly Allocation Analysis

The budget totals $226,750 in direct costs, with ~$29,250 for indirect costs and contingency, reaching $256,000 total. This structure is reasonable for an SBIR Phase I.

**Personnel ($195,000 / 76.6% of total):**
- At $21,667/month flat across all 9 months, the personnel burn is uniform. This is unusual -- personnel effort typically varies as team members ramp on and off. A flat rate suggests simplified budgeting rather than actual effort-based costing.
- $195,000 for 14.5 person-months implies an average loaded rate of ~$13,448/person-month. This is low for the roles described (PI/Lead Developer, Clinical Advisor physician, Data Engineer, Clinical Informatics Specialist). It may be appropriate if the PI takes a below-market salary as is common in early-stage SBIR, but it should be justified.
- **Recommendation:** Break down personnel costs by individual (PI salary, Co-I consulting rate, Data Engineer salary/contract, CIS salary/contract) rather than presenting a flat monthly aggregate. NIH budget justification requires individual salary levels.

**Infrastructure ($7,000 / 2.8%):**
- $750/month for GovCloud is consistent with the VIPC documents and is reasonable for pilot-scale ECS Fargate + RDS deployment.
- Month 1 shows $1,250 (presumably one-time setup costs). This should be itemized.
- The $2,500 for GPU compute (mentioned in Section 2.1) does not appear as a line item in the budget table. It may be folded into "Other" but should be explicit.
- **Recommendation:** Add GPU compute as a separate line or note its inclusion in the infrastructure or Other category.

**Devices ($3,750 / 1.5%):**
- $3,750 for RPM devices at $150/unit average = 25 devices. For 50-100 patients, this implies some patients share devices or only a subset are monitored. The VIPC budget allocated $2,500 for 15-20 devices. The increase to $3,750 is proportional but may still be insufficient for 50-100 patients.
- **Recommendation:** Clarify how many devices are needed for the target enrollment. If 50 patients, 25 devices requires device rotation or re-use protocol. If 100 patients, the budget is clearly insufficient.

**Travel ($6,500 / 2.6%):**
- Allocated across Months 3-5 and 7-9, covering clinic onboarding visits, training, and presumably NIH meetings or conferences. Reasonable for 2-3 Virginia clinic sites.

**Other ($14,500 / 5.7%):**
- Includes Month 2 ($1,500), Month 3 ($3,000), Month 7 ($5,000). The $5,000 in Month 7 is unexplained. This likely covers patent filing, legal fees, or publication costs, but should be itemized.
- **Recommendation:** Provide line-item detail for "Other" costs. NIH requires justification for all budget categories.

**Indirect Costs and Contingency (~$29,250 / ~$4,250 noted for contingency):**
- The gap between $226,750 direct and $256,000 total is $29,250. The plan notes "$4,250 allocated to indirect costs and contingency." The remaining ~$25,000 is unaccounted.
- SBIR Phase I indirect cost rates must be negotiated or use a de minimis rate (typically 10%). At 10% of $226,750, indirect would be ~$22,675, leaving ~$6,575 for contingency. This math should be made explicit.
- **Recommendation:** Specify the indirect cost rate used. Separate indirect costs from contingency. If no negotiated rate exists, state use of de minimis rate.

### 4.2 Budget Controls

The budget controls section (monthly monitoring, cost optimization, contingency triggers at 120%) is adequate. Quarterly NIH financial reporting is correctly identified. However, the plan does not mention NIH prior approval requirements for budget transfers exceeding 25% between categories, which is a standard SBIR requirement.

---

## 5. QUALITY ASSURANCE

### 5.1 Testing Strategy Assessment

The testing strategy is comprehensive and appropriate for a healthcare platform handling PHI:

- **Unit testing (>85% coverage, 100% for billing logic):** Excellent standard. Billing logic must be deterministic and verifiable.
- **Integration testing (every sprint):** Appropriate cadence for FHIR and RPM API testing.
- **Model validation (monthly):** Correct for a research study evaluating AI performance.
- **Security testing (quarterly):** Adequate for Phase I scope, though an initial penetration test before pilot go-live should be mandated.
- **UAT (pre-go-live and monthly):** Good frequency. The 4.0/5.0 clinician satisfaction target and 90% task completion rate are measurable and appropriate.
- **Billing accuracy audit (<5% discrepancy):** Strong standard that directly supports Aim 2.
- **Data quality checks (daily automated, >95% completeness):** Essential for research validity. The <1% duplicate rate target is good.

### 5.2 CI/CD Pipeline

The 10-step CI/CD pipeline (lint, unit tests, integration tests, security scan, build, deploy staging, smoke tests, manual approval, deploy production, health checks) is well-designed and includes appropriate gates. The manual approval gate before production is essential for a HIPAA environment.

**Gap:** The pipeline does not mention database migration management, n8n workflow version control, or ML model versioning. Since n8n workflows are a core component, their deployment and version tracking should be explicitly addressed.

**Recommendation:** Add n8n workflow export/import automation to the CI/CD pipeline. Add ML model registry (MLflow or equivalent) for model versioning and reproducibility.

### 5.3 Incident Response

The four-tier incident response framework is appropriate. Critical incidents correctly include PHI exposure and billing errors affecting live claims. The response times (1 hour for critical, 4 hours for high) are aggressive for a small team but appropriate given the PHI stakes.

**Gap:** The plan does not address incident documentation, root cause analysis, or post-incident review processes. For an NIH study, incidents must also be reported to the IRB and documented in the research record.

**Recommendation:** Add post-incident review requirement. Add IRB notification to High-severity incidents (not just Critical) when they affect patient data or care delivery. Define what constitutes a protocol deviation versus an adverse event.

---

## 6. REGULATORY COMPLIANCE

### 6.1 HIPAA Framework

The HIPAA compliance framework is thorough and correctly identifies all major requirements: Privacy Rule, Security Rule, Breach Notification, BAAs, Risk Assessment, and Training. The implementation details (AES-256, TLS 1.2+, RLS, PGAudit, MFA) are technically sound.

**Gap:** The plan does not address the HIPAA minimum necessary standard in the context of the research use of PHI. Research use of PHI under HIPAA requires either patient authorization or an IRB waiver of authorization. The three-part consent described in Section 8.3 should explicitly address HIPAA authorization for research use.

**Recommendation:** Add a HIPAA research authorization component to the consent workflow (or document the IRB waiver of authorization strategy).

### 6.2 FDA Regulatory Position

The FDA CDS exemption analysis under the 21st Century Cures Act is well-reasoned and correctly cites all four criteria. However:

- **Criterion 1 is arguable:** The plan states the platform "does not acquire or process signals from a medical device." However, the platform ingests RPM device data (blood pressure cuffs, pulse oximeters, glucose monitors, scales) via vendor APIs. The distinction between "acquiring signals directly from a device" and "acquiring signals via a vendor API intermediary" is precisely the kind of gray area that FDA enforcement discretion evaluates.
- The January 2026 FDA CDS guidance update is referenced but not cited. Reviewers may want to verify this reference.
- **Recommendation:** Strengthen the Criterion 1 analysis by citing the specific FDA guidance language that distinguishes direct device signal acquisition from API-mediated data ingestion. Add the specific FDA guidance document citation. Consider adding a brief risk assessment of what happens if FDA disagrees with the CDS exemption analysis.

### 6.3 IRB Protocol

The IRB summary is adequate but abbreviated. For an NIH proposal, the human subjects section typically requires:

- Inclusion/exclusion criteria with justification
- Recruitment procedures and setting
- Description of the intervention versus standard of care
- Detailed risk/benefit analysis
- Data safety monitoring plan
- Provisions for vulnerable populations (if applicable -- rural populations may have limited health literacy)
- Plans for withdrawal of subjects
- Privacy and confidentiality protections beyond HIPAA

**Missing:** The plan does not mention 42 CFR Part 46 (Common Rule) requirements, which apply to all federally funded human subjects research. It also does not address whether the study requires ClinicalTrials.gov registration (likely not for a Phase I technology feasibility study, but should be explicitly addressed).

**Recommendation:** Expand the IRB protocol summary to address Common Rule requirements. Add inclusion/exclusion criteria. Add a Data Safety Monitoring Plan (DSMP). Address ClinicalTrials.gov registration determination.

---

## 7. RISK MANAGEMENT

### 7.1 Risk Register Completeness

The 10-item risk register covers the major technical, operational, and regulatory risks. Each entry includes probability, impact, mitigation, and owner -- a complete risk management framework.

**Well-Identified Risks:**
- R1 (EHR integration delays) and R2 (low enrollment) are the two highest-probability, highest-impact risks and are correctly prioritized.
- R8 (PHI security incident) is correctly rated Low probability / Critical impact, reflecting the GovCloud security posture.
- R10 (insufficient cross-domain data for Aim 3) is an honest and important acknowledgment.

**Missing Risks:**
- **Pilot clinic staff turnover:** Rural clinics have high staff turnover. If the trained clinic champion leaves mid-pilot, enrollment and data quality suffer. This is distinct from R5 (clinic drops out).
- **Device failure or patient non-compliance with RPM:** RPM adherence rates in rural populations are typically 50-70%. The plan assumes consistent device data transmission but does not address what happens when patients stop using devices.
- **CMS reimbursement rate changes mid-study:** The plan includes new 2026 CPT codes (99445, 99470). If CMS modifies or rescinds these codes during the study, the billing logic and Aim 2 analysis are affected.
- **n8n Community Edition limitations at scale:** The VIPC Implementation Guide identifies this as a known risk (no SSO/LDAP, no RBAC). The NIH plan does not acknowledge this gap.
- **Data quality issues in EHR data:** FHIR data from rural EHRs is often incomplete or inconsistently coded. The plan assumes clean data flow but does not address data cleaning or imputation strategies.
- **PI burnout or health event:** With one person carrying the entire technical and research burden, any PI unavailability (even a 2-week illness) can cascade across all workstreams. R7 (key personnel unavailability) partially addresses this but understates the severity given the PI's singular role.

**Recommendation:** Add risks for staff turnover, RPM adherence, data quality, and n8n access control limitations. Increase R7 severity rating from "Low probability / High impact" to "Medium probability / Critical impact" given the extreme concentration of responsibility on the PI.

### 7.2 Go/No-Go Decision Points

The five decision points are well-chosen and cover the critical junctures. The relaxed interim criteria (AUC-ROC > 0.70 at Sprint 13, <10% billing discrepancy at Sprint 14) with escalation paths are pragmatic.

**Gap:** No Go/No-Go point for IRB approval. If IRB approval is not received by end of Sprint 6, the entire pilot timeline shifts. This should be an explicit decision point with a defined fallback (e.g., proceed with de-identified CMS data analysis only).

**Gap:** No decision point for minimum enrollment. If only 15 patients are enrolled by Month 6, the statistical power for Aim 1 and Aim 3 analyses may be insufficient.

**Recommendation:** Add IRB approval and minimum enrollment as Go/No-Go decision points.

---

## 8. DATA MANAGEMENT

### 8.1 Data Types and Sources

The data management plan correctly identifies seven data types with sources, volumes, and sensitivity classifications. The distinction between PHI-protected and de-identified data is clear.

**Gap:** The plan does not address data provenance tracking. For research validity, it must be possible to trace any analytical result back to its source data, including version and transformation history. This is especially important for the de-identified research analytics data.

**Gap:** No mention of data dictionaries or metadata standards. NIH expects data to be described using standard metadata schemas for repository deposit.

**Recommendation:** Add data provenance tracking requirements. Specify metadata standards for the NIH repository deposit (e.g., CEDAR metadata, Common Data Elements).

### 8.2 Data Storage and Security

The storage and security controls are comprehensive and well-mapped to HIPAA requirements. The disaster recovery parameters (RTO 4 hours, RPO 1 hour) are appropriate for a pilot-scale research system.

**Gap:** The data retention policy states "PHI retained per HIPAA requirements (6 years minimum); research data retained per NIH policy." NIH policy requires research data retention for a minimum of 3 years after the final expenditure report, or longer if required by the award terms. The plan should specify the exact retention period and the disposition of PHI at study conclusion.

**Gap:** The de-identification methodology references "HIPAA Safe Harbor method" but does not detail which of the 18 Safe Harbor identifiers will be removed or how quasi-identifiers (e.g., rural ZIP codes with small populations) will be handled. Rural health data is particularly susceptible to re-identification due to small population sizes.

**Recommendation:** Specify the retention period for both PHI and research data. Detail the Safe Harbor de-identification process with attention to rural re-identification risks (e.g., ZIP code generalization to 3-digit level, age top-coding at 89).

### 8.3 Data Sharing

The data sharing plan is adequate at a high level but lacks specifics:

- "De-identified, aggregated pilot data deposited within 12 months of Phase I completion" -- which repository? NIH expects a named repository (e.g., dbGaP, NCBI, or a domain-specific repository).
- "Model artifacts: Trained model weights are trade secrets owned by ACT" -- this is in tension with NIH data sharing expectations. The 2023 NIH Data Management and Sharing Policy requires that scientific data be shared. Model weights may be excluded as "proprietary software," but the training data, feature definitions, and model performance metrics must be shared.
- **Recommendation:** Name the target NIH repository. Clarify what will be shared (de-identified data, code for analysis, model architecture and hyperparameters) versus what is retained as proprietary (trained weights, workflow templates). Ensure compliance with the 2023 NIH DMSP requirements.

---

## 9. CROSS-DOCUMENT CONSISTENCY

### 9.1 Inconsistencies Between NIH Implementation Plan and VIPC Documents

| Issue | NIH Plan | VIPC Documents | Assessment |
|---|---|---|---|
| **Platform name** | "3C Platform" | "3C Platform" | Consistent |
| **Technology stack** | n8n, PostgreSQL 16, Python/FastAPI, React/Next.js, Docker, GovCloud | Identical | Consistent |
| **GovCloud cost** | $750/month (line item) but $1,250 in Month 1 | $750/month | Mostly consistent; Month 1 difference unexplained |
| **RPM device cost** | $150/unit average | $80-$300 range depending on device type | Consistent (NIH uses midpoint) |
| **RPM device count** | $3,750 budget / $150 avg = 25 units | VIPC: 15-20 units for $2,500 | Proportional increase; consistent |
| **Patient enrollment target** | 50-100 RPM patients | VIPC: 15-20 per pilot clinic (30+ total) | NIH is more ambitious; justified by longer timeline |
| **AUC-ROC target** | >0.75 (Sprint 13 relaxed to >0.70) | VIPC: >0.75 | Consistent, with appropriate interim relaxation |
| **ML model** | XGBoost + logistic regression baseline + SHAP | Same | Consistent |
| **CMS billing codes** | Includes 99445, 99470 (2026 codes) | Same | Consistent |
| **MIPS weighting** | Quality 30%, Cost 30%, PI 25%, IA 15% | Same | Consistent |
| **IP ownership** | "Model artifacts: trade secrets owned by ACT" | "All IP owned by ACT" | Consistent |
| **PI effort** | 6.0 calendar months | VIPC: 40 hrs/week (full-time sweat equity) | **Inconsistency:** NIH reduces PI effort to ~67% while scope increases significantly |
| **Team composition** | PI + Co-I + Data Engineer + Clinical Informatics | VIPC: Will + Cari Ann + Jim + Jessica | **Inconsistency:** NIH plan has different team structure; no mention of VIPC team members |
| **Clinical advisor** | "TBD (Board-certified physician, rural health)" | VIPC: "Cari Ann (ACT) + pilot clinic provider" | **Inconsistency:** Is Cari Ann the Co-I? If so, name her. If not, explain the different team |
| **NLP capabilities** | Not mentioned in NIH plan | VIPC Technical Brief: spaCy/MedCAT for NLP coding optimization | **Inconsistency:** VIPC architecture includes NLP engine; NIH plan AI/ML engine diagram omits it |
| **Service tiers** | Not discussed | VIPC: Essentials / Professional / Enterprise tiers | **Inconsistency:** NIH plan does not address modular tiering, which is a core commercial architecture feature |
| **n8n HIPAA gap** | Not addressed | VIPC Implementation Guide: explicitly identifies Community Edition SSO/RBAC gap with mitigation | **Gap in NIH plan:** Regulatory compliance section should address this known access control limitation |
| **Deterioration detection** | Sprint 10 (Month 5): sliding-window algorithms | VIPC Implementation Guide: Phase 1 is rule-based; ML trend analysis is Phase 2 | **Inconsistency:** NIH plan describes ML-grade temporal analytics in Sprint 10 that VIPC reserves for Phase 2 |
| **Telehealth** | Not mentioned | VIPC: Phase 2 feature (Zoom/Doxy.me integration) | Consistent (correctly excluded from NIH Phase I) |
| **Patent strategy** | "Submit provisional patent application(s)" in Sprint 18 | VIPC: File provisional in Months 2-3 | **Inconsistency:** VIPC plans patent filing early; NIH delays to final sprint. This may be intentional (different IP may be patented) but should be clarified |
| **42 CFR Part 2** | Not mentioned | VIPC Implementation Guide: mentions if pilot clinics treat SUDs | **Gap in NIH plan:** Should address 42 CFR Part 2 applicability |
| **VCDPA** | Not mentioned | VIPC Implementation Guide: mentions Virginia data privacy act | **Gap in NIH plan:** Should address state privacy law |

### 9.2 Relationship Between VIPC and NIH Projects

The plan's Executive Summary states: "The underlying platform technology is identical; the SBIR adds formal research methodology, IRB oversight, human subjects protections, and publication-quality analysis."

This raises a critical question: **Is the NIH SBIR funding the research layer on top of an already-built platform, or is it funding the platform build AND the research?** The sprint plan appears to fund both -- Sprints 1-6 include significant platform development (infrastructure, data model, ML training, EHR integration, billing logic, compliance module) that overlaps with the VIPC-funded MVP.

If the VIPC MVP is expected to be complete before SBIR starts, then Sprints 1-6 are redundant and the SBIR budget could be more efficiently allocated to research activities. If the projects run concurrently, then the plan must address how costs are allocated to avoid double-charging federal and state funds for the same work.

**Recommendation:** Explicitly state the temporal relationship between VIPC and SBIR funding. If concurrent, add a cost allocation methodology showing which development activities are charged to which funding source. If sequential, adjust the sprint plan to reflect an already-built platform and focus SBIR sprints on research-specific additions.

---

## 10. STRENGTHS

- **Technically detailed and specific:** The plan provides concrete technology choices, acceptance criteria, and measurable targets rather than vague descriptions. Sprint deliverables include specific acceptance criteria with checkboxes.
- **Appropriate technology stack:** The open-source, GovCloud-hosted architecture is well-suited for HIPAA compliance and cost efficiency. The use of proven components (PostgreSQL, FastAPI, React) reduces technical risk.
- **Well-structured sprint plan:** The 18-sprint progression from infrastructure to development to deployment to evaluation follows sound engineering practice with logical aim alignment.
- **Strong security posture:** FedRAMP High (GovCloud), AES-256, TLS 1.2+, RLS, PGAudit, and CloudTrail provide defense-in-depth for PHI protection. The security framework exceeds many SBIR Phase I projects.
- **Honest risk acknowledgment:** Risk R10 (insufficient cross-domain data for Aim 3) demonstrates intellectual honesty about a genuine limitation of a 9-month study with small sample sizes.
- **Go/No-Go decision points with relaxed interim criteria:** The pragmatic approach of relaxing AUC-ROC from 0.75 to 0.70 at interim evaluation, with escalation paths, shows mature project management.
- **Billing logic specificity:** The plan correctly identifies 2026 CMS billing codes (including new 99445 and 99470), mutual exclusivity rules, and threshold logic. This level of billing domain expertise is uncommon in research proposals.
- **Cross-domain research design (Aim 3):** The study of compliance-care-revenue interactions is a genuinely novel research contribution that could yield insights applicable beyond this platform.
- **FHIR R4 interoperability commitment:** Using standard FHIR R4 with bonFHIR for EHR integration demonstrates adherence to ONC interoperability mandates.
- **Comprehensive CI/CD pipeline:** The 10-step pipeline with security scanning, staging deployment, and manual production gates reflects production-grade engineering discipline.

---

## 11. WEAKNESSES

- **Excessive reliance on a single PI for all technical, engineering, and research responsibilities.** The PI (Will Nelson) is sole architect, developer, ML engineer, systems administrator, research designer, and primary author. Any PI unavailability for even 2 weeks cascades across all workstreams. NIH reviewers will question whether one person can competently execute all these roles simultaneously.
  - **Fix:** Redistribute engineering responsibilities to the Data Engineer. Add a part-time research coordinator. Increase PI effort to 8-9 calendar months.

- **All three non-PI team members are TBD.** NIH strongly prefers named investigators and key personnel with biosketches. Three TBD positions out of four total funded positions is a significant proposal weakness.
  - **Fix:** Name the Co-Investigator, Data Engineer, and Clinical Informatics Specialist before submission. Include biosketches for all named personnel.

- **No formal statistical analysis plan.** The plan describes analytical methods at a high level (AUC-ROC, fairness metrics, interrupted time-series, cross-domain correlations) but lacks a formal statistical analysis plan with hypotheses, sample size calculations, power analysis, primary and secondary endpoints, and pre-specified analytical approaches.
  - **Fix:** Add a Statistical Analysis Plan section with power calculations, pre-specified hypotheses for each aim, primary and secondary outcome definitions, and planned analytical methods with software specifications.

- **No Data Safety Monitoring Plan (DSMP).** NIH requires a DSMP for all clinical research involving human subjects. The plan mentions "quarterly data safety monitoring" in the IRB summary but provides no detail.
  - **Fix:** Add a dedicated DSMP section specifying monitoring frequency, criteria for study modification or termination, adverse event definitions and reporting procedures, and the composition of the data monitoring entity.

- **IRB timeline is critically tight with no buffer.** IRB submission in Sprint 5 with assumed approval by Sprint 6 and pilot go-live in Sprint 7 leaves zero weeks for IRB revisions or stipulations.
  - **Fix:** Submit IRB protocol by Sprint 3. Add a 4-week buffer between IRB submission and pilot go-live. Consider pre-IRB engagement (pre-submission meeting) to identify likely concerns.

- **Budget presentation lacks NIH-standard line-item detail.** Personnel costs are presented as a flat monthly aggregate rather than individual salary breakdowns. "Other" costs are not itemized. Indirect cost rate is not specified.
  - **Fix:** Restructure budget to show individual salary/effort levels. Itemize "Other" costs. State the indirect cost rate (negotiated or de minimis).

- **The plan reads as an engineering document, not a research protocol.** The research hypotheses, study design, outcome variable definitions, and analytical framework are subordinate to the engineering sprint plan. NIH reviewers evaluate research significance, innovation, and approach -- the plan should lead with these.
  - **Fix:** Add a Research Design section (between Executive Summary and Technical Architecture) that articulates hypotheses, study design, outcome variables, and the statistical analysis plan before presenting the engineering execution.

- **No power calculation or minimum sample size determination.** The plan targets 50-100 RPM patients but does not justify this range statistically. For Aim 1 (model validation), what is the minimum n needed for meaningful AUC-ROC estimation? For Aim 3 (cross-domain correlations), what effect sizes are detectable with 50-100 patients over 4-5 months?
  - **Fix:** Add power calculations for each aim. Specify minimum viable sample sizes. Define what constitutes a "successful" Phase I demonstration at different enrollment levels.

- **De-identification approach underspecified for rural populations.** HIPAA Safe Harbor is referenced but rural health data presents unique re-identification risks due to small community sizes. Three-digit ZIP codes in rural Virginia may still identify specific communities.
  - **Fix:** Detail the de-identification methodology with rural-specific protections (ZIP code generalization, age top-coding, rare condition suppression).

- **No mention of the VIPC/SBIR funding overlap.** The sprint plan includes significant platform development (Sprints 1-6) that appears to overlap with the VIPC-funded MVP. The temporal and financial relationship between the two funding sources is not addressed.
  - **Fix:** Add a section explicitly describing the VIPC/SBIR relationship, timeline dependencies, and cost allocation methodology.

- **Missing n8n Community Edition access control limitation.** The VIPC Implementation Guide explicitly identifies the lack of SSO/RBAC in n8n Community Edition as a known HIPAA gap with a specific mitigation (VPN + IP allowlisting, clinic staff access React only). The NIH plan omits this.
  - **Fix:** Add this known limitation and its mitigation to the HIPAA compliance section.

---

## 12. SPECIFIC RECOMMENDED CHANGES

1. **Section 1 (Executive Summary):** Add a paragraph explicitly describing the temporal and financial relationship between the VIPC-funded MVP and the NIH SBIR Phase I. State whether the projects are sequential or concurrent, and how cost allocation avoids double-charging. Include a sentence such as: "The VIPC VVP Launch Grant ($50K, 4 months) funds the initial platform MVP. The NIH SBIR Phase I ($256K, 9 months) begins [before/after/concurrently with] the VIPC project and funds the research validation layer, formal clinical study, and statistical evaluation. Platform development costs charged to the SBIR are limited to research-specific additions (Research Analytics Layer, de-identification pipeline, IRB audit trail, model performance tracking) that are not part of the VIPC scope."

2. **New Section (insert between Sections 1 and 2):** Add a "Research Design" section containing: (a) formally stated hypotheses for each of the three aims, (b) study design description (prospective observational cohort study), (c) primary and secondary outcome variables with operational definitions, (d) sample size justification with power calculations, (e) statistical analysis plan for each aim, and (f) study timeline aligned with the sprint plan.

3. **Section 3.2, Sprint 5:** Change IRB submission from Sprint 5 to Sprint 3 (Month 2). Change the text from "Full IRB protocol submitted for expedited review" to "Full IRB protocol submitted for expedited review (drafted in Sprint 1, reviewed by Co-I in Sprint 2, submitted early Sprint 3)." Add an acceptance criterion: "Pre-submission meeting with IRB completed and feedback incorporated."

4. **Section 4.1 (Team):** Replace "TBD" for the Co-Investigator with a named physician. Add a biosketch reference. Change effort from "1.0 cal. month" to "2.0 cal. months" and add responsibilities: "Monthly clinical review of model outputs during pilot, enrollment protocol oversight, adverse event adjudication, co-author Phase I final report and manuscript."

5. **Section 4.1 (Team):** Add two additional roles: (a) "Biostatistician (Consultant) | TBD (PhD-level) | 0.5 cal. month | Power calculations, statistical analysis plan, Aim 3 cross-domain analysis, manuscript statistical review" and (b) "Research Coordinator (Part-time) | TBD | 1.5 cal. months | IRB management, consent tracking, enrollment logistics, data quality monitoring, adverse event documentation."

6. **Section 5.3 (Data Sharing):** Replace "NIH Data Repository" with a specific named repository (e.g., "NCBI dbGaP for patient-level de-identified data; Zenodo for analysis code and model architecture documentation"). Add: "Consistent with the 2023 NIH Data Management and Sharing Policy, the following will be shared: (1) de-identified patient-level data; (2) analysis code (Python scripts, statistical models); (3) model architecture and hyperparameters; (4) feature definitions and data dictionaries. Proprietary elements excluded from sharing: trained model weights, n8n workflow templates, and clinic-specific configurations, which constitute trade secrets."

7. **Section 6.1 (Budget):** Restructure the budget table to show individual personnel costs. Example format: "PI (W. Nelson): X months at $Y/month = $Z | Co-I (Name): X months at $Y/month = $Z | Data Engineer (Name): X months at $Y/month = $Z | Clinical Informatics (Name): X months at $Y/month = $Z | Biostatistician (Consultant): X hours at $Y/hour = $Z | Research Coordinator: X months at $Y/month = $Z." Add a row for GPU compute ($2,500). Itemize "Other" costs (legal, patent, publications, IRB fees). State the indirect cost rate explicitly.

8. **Section 7.1 (Testing, CI/CD):** Add to the CI/CD pipeline: "11. n8n workflow version export and deployment (automated export of workflow JSON, versioned in Git, deployed via n8n API)" and "12. ML model registry update (model artifacts, performance metrics, and training data hash logged to MLflow or equivalent)."

9. **Section 8.1 (HIPAA):** Add a row to the HIPAA table: "**n8n Access Control** | n8n Community Edition lacks SSO/LDAP and RBAC (Enterprise-only features). Mitigation: n8n UI access restricted to engineering team via VPN + NGINX IP allowlisting. All clinic staff interact exclusively through the React frontend with application-level RBAC. n8n processes PHI in workflows but no clinic user directly accesses the n8n interface. Phase II: evaluate n8n Enterprise or external auth proxy."

10. **Section 8.1 (HIPAA):** Add a row: "**Research Authorization** | HIPAA authorization for research use of PHI obtained as part of the three-part consent workflow (clinical RPM consent + Medicare RPM billing consent + HIPAA research authorization/research data use consent). Alternatively, if IRB grants a waiver of HIPAA authorization under 45 CFR 164.512(i), document the waiver criteria."

11. **Section 8.2 (FDA):** Strengthen Criterion 1 analysis. Change "Does not acquire or process signals from a medical device -- platform ingests data from external devices via API, does not control device acquisition" to: "Does not acquire, process, or analyze a signal from an in vitro diagnostic device or a signal acquisition system -- the platform receives pre-processed, validated readings from FDA-cleared RPM devices via the device vendor's cloud API (Tenovi/Smart Meter). The platform does not directly interface with, control, or acquire raw signals from any medical device. Per FDA guidance (September 2022 CDS Final Guidance, updated January 2026), this API-mediated ingestion of pre-processed readings does not constitute signal acquisition under Section 520(o)(1)(A) of the FD&C Act."

12. **Section 8.3 (IRB):** Expand the IRB protocol summary to include: (a) inclusion criteria: "Adults age 18+ with at least one chronic condition (diabetes, hypertension, CHF, COPD, CKD) receiving care at a participating RHC and eligible for CMS RPM services"; (b) exclusion criteria: "Patients unable to consent, patients with active substance use disorder treatment (42 CFR Part 2 considerations), patients declining research participation"; (c) a Data Safety Monitoring Plan paragraph specifying quarterly review, stopping rules, and adverse event definitions; (d) a statement on ClinicalTrials.gov registration: "This study evaluates a health IT platform and does not meet the NIH definition of a clinical trial requiring ClinicalTrials.gov registration, as it does not prospectively assign participants to an intervention to evaluate health outcomes."

13. **Section 9.1 (Risk Register):** Add the following risks: "R11 | Pilot clinic staff turnover during study | Medium | Medium | Cross-train 2+ staff at each clinic; document all workflows; PI provides direct clinic support if champion leaves | PI + Co-I" and "R12 | RPM device adherence below 60% | Medium | High | Proactive patient engagement calls at Days 3, 7, 14; cellular devices eliminate WiFi barriers; clinic staff reinforce device use at visits; analyze adherence data weekly and intervene for non-adherent patients | Co-I" and "R13 | EHR data quality insufficient for model training | Medium | Medium | Data quality assessment in Sprint 2; define minimum completeness thresholds; supplement with CMS public use file data; document data quality limitations in final report | Data Engineer."

14. **Section 9.2 (Go/No-Go):** Add two decision points: "**IRB Approved** | End of Sprint 4 | IRB expedited approval received or clear timeline to approval within 4 weeks | Proceed with CMS data analysis only; submit protocol revision; delay pilot by 1 sprint" and "**Minimum Enrollment** | End of Sprint 9 | At least 30 RPM patients enrolled across sites | Intensify recruitment; extend enrollment by 1 month with compressed evaluation; adjust statistical analysis for smaller sample."

15. **Section 5 (Data Management), Section 5.2:** Add to the de-identification methodology: "Given the small population sizes in rural Virginia communities, the Safe Harbor de-identification will include the following additional protections: (a) ZIP codes generalized to 3-digit prefix; if 3-digit ZIP has population <20,000, replaced with '000'; (b) ages above 89 recorded as '90+'; (c) rare conditions (prevalence <5 in the dataset) suppressed or generalized to ICD-10 category level; (d) dates shifted by a random offset (constant per patient, range +/- 180 days) to preserve intervals while obscuring actual dates."

16. **Section 10 (Communication and Reporting):** Add a line item for NIH RPPR (Research Performance Progress Report) submission requirements: "RPPR | Annually or as required by NoA | Research accomplishments, products, participants, changes, special reporting." Also add a reference to the requirement for NIH prior approval for budget transfers exceeding 25% between categories.

---

## SUMMARY ASSESSMENT

This implementation plan demonstrates strong technical execution capability and a well-structured engineering approach to the 3C Platform. The plan would benefit significantly from: (1) reframing the document to lead with research design rather than engineering execution; (2) naming all key personnel; (3) adding a formal statistical analysis plan with power calculations; (4) adding a Data Safety Monitoring Plan; (5) adjusting the IRB timeline to include realistic review buffers; (6) explicitly addressing the VIPC/SBIR funding overlap; and (7) adding the missing regulatory and risk items identified in this review.

With these revisions, the plan would present a compelling case for NIH SBIR Phase I funding. The core concept -- validating an AI-driven integrated compliance, care, and revenue platform for rural health clinics -- addresses a genuine unmet need with clear commercial potential, which is precisely the SBIR mandate.

**Recommendation: Revise and resubmit with the changes enumerated above before final NIH submission.**

---

*Review prepared for internal use by Authentic Consortium.*
*This review reflects the assessment of a simulated NIH peer reviewer and should not be construed as an official NIH determination.*
