# VV TECHNICAL IMPLEMENTATION BRIEF

**Prepared for:** Will Nelson (Technical Presenter) | Authentic Consortium
**Presentation:** VIPC VVP Launch Grant -- Final Presentation (Wednesday, Feb 26, 2026)
**Audience:** Jennifer O'Daniel (VVP Lead), Michael Jarvis (Healthcare Investor), Tai Mai (VIPC Healthcare Lead / MEDA Ventures)
**Classification:** Internal Prep Document -- Do Not Distribute

---

## EXECUTIVE SUMMARY

Authentic Consortium (ACT) is presenting the **3C Platform** -- a unified Salesforce-based solution for rural health clinics (RHCs) that solves three compounding crises: **Compliance**, **Care**, and **Collect Cash** (cost/revenue). Veteran Vectors (VV) serves as the technical backbone, providing AI/ML analytics, cybersecurity/compliance automation, wearable device integration, and cloud infrastructure. This brief equips Will to speak authoritatively on how VV's technical capabilities -- informed by DoD AI/health program experience including edge computing, DDIL architectures, and HIPAA-equivalent protections -- translate directly to solving rural healthcare's hardest problems.

---

## 1. THE PROBLEM: WHY RURAL CLINICS ARE FAILING

Virginia has **106 Rural Health Clinics** and 27 FQHCs (5,500+ RHCs nationally) facing a convergence of crises -- with 3 Virginia RHCs closing in 2025 alone due to federal funding cuts and 9 rural hospitals at risk of closure:

- **Compliance burden:** HIPAA, HRSA reporting, CMS quality metrics, FCC (telehealth/broadband) -- each with different reporting cadences, data formats, and penalty structures. A single RHC may face 15+ distinct regulatory obligations. Non-compliance triggers loss of Medicare/Medicaid reimbursement -- which is 60--80% of RHC revenue
- **Care gaps:** Provider shortages (1 physician per 2,500+ patients in some Virginia counties), chronic disease prevalence 30--40% above urban averages, limited specialist access, no preventive care infrastructure. Patients present late-stage because there's no monitoring between annual visits
- **Revenue leakage:** Undercoding, missed quality bonuses (MIPS/APM), denied claims from documentation gaps, and inability to capture RPM/CCM reimbursement codes that CMS now pays for. RHCs leave an estimated $100K--$250K per clinic per year on the table in unrealized RPM, CCM, and quality bonus revenue

**The key insight:** These three problems are interconnected. Compliance failures cause revenue loss. Care gaps drive costly ER utilization. Revenue shortfalls prevent investment in better care. No one is offering a unified platform that treats all three as a single system.

---

## 2. THE 3C PLATFORM: TECHNICAL ARCHITECTURE

### 2.1 Platform Foundation -- Salesforce Health Cloud

The 3C Platform is built on **Salesforce Health Cloud** as the backbone, which provides:

- HIPAA-compliant infrastructure (BAA-covered, SOC 2 Type II, FedRAMP Moderate)
- Native EHR integration via HL7 FHIR R4 (Phase 1: Salesforce Connect + Apex REST; Phase 2+: MuleSoft connectors)
- Built-in workflow automation (Flow Builder) for compliance task management
- Patient 360 views aggregating clinical, compliance, and billing data
- AppExchange ecosystem for rapid capability extension

### 2.2 Three Integrated Modules

```
+------------------------------------------------------------------+
|                     3C PLATFORM (Salesforce Health Cloud)          |
|                                                                   |
|  +------------------+  +------------------+  +------------------+ |
|  |   COMPLIANCE     |  |      CARE        |  |   COLLECT CASH   | |
|  |   MODULE         |  |      MODULE      |  |   MODULE         | |
|  |                  |  |                  |  |                  | |
|  | - HIPAA Audit    |  | - AI Risk        |  | - Auto-Coding    | |
|  |   Automation     |  |   Stratification |  |   Optimization   | |
|  | - HRSA UDS       |  | - Wearable/RPM   |  | - RPM/CCM Billing| |
|  |   Reporting      |  |   Integration    |  |   Capture        | |
|  | - CMS Quality    |  | - Care Gap       |  | - Denial         | |
|  |   Dashboards     |  |   Detection      |  |   Prevention     | |
|  | - FCC Broadband  |  | - Chronic Disease |  | - MIPS/APM       | |
|  |   Compliance     |  |   Monitoring     |  |   Optimization   | |
|  | - Policy Engine  |  | - Telehealth     |  | - Revenue Cycle  | |
|  |   (Auto-Update)  |  |   Orchestration  |  |   Analytics      | |
|  +------------------+  +------------------+  +------------------+ |
|                              |                                    |
|         +--------------------+--------------------+               |
|         |            AI/ML ENGINE (VV)            |               |
|         | - Predictive Analytics                  |               |
|         | - NLP for Documentation                 |               |
|         | - Risk Scoring Models                   |               |
|         | - Anomaly Detection                     |               |
|         +--------------------+--------------------+               |
|                              |                                    |
|         +--------------------+--------------------+               |
|         |         INTEGRATION LAYER (VV)          |               |
|         | - HL7 FHIR R4 / SF Connect (MuleSoft P2)|               |
|         | - Wearable Device APIs                  |               |
|         | - CMS/HRSA Data Feeds                   |               |
|         | - Clearinghouse Connections              |               |
|         +-----------------------------------------+               |
+------------------------------------------------------------------+
```

---

## 3. VV'S TECHNICAL ROLE -- MODULE BY MODULE

### 3.1 Compliance Module: Automated Regulatory Intelligence

**The problem VV solves:** RHC administrators spend 15--20 hours/week on manual compliance tasks -- tracking HIPAA training, assembling HRSA UDS reports, monitoring CMS quality measures, documenting FCC broadband obligations. When they miss something, the penalties are existential (loss of RHC certification = loss of enhanced Medicare reimbursement).

**VV's technical implementation:**

| Capability | How VV Builds It | Technology |
|---|---|---|
| **HIPAA Compliance Automation** | Continuous monitoring of access logs, PHI handling, security controls. Automated risk assessments per NIST SP 800-66 (HIPAA Security Rule mapping). Real-time alerts for policy violations | Salesforce Shield (Event Monitoring) + VV custom anomaly detection models + encrypted audit trail |
| **HRSA UDS Report Generation** *(Phase 2)* | Automated data extraction from EHR, patient demographics, and clinical quality measures. Pre-populated UDS tables with validation checks before submission | EHR integration (Salesforce Connect/FHIR) + Salesforce Reports + VV data transformation engine |
| **CMS Quality Dashboard** | Real-time tracking of MIPS quality measures, promoting interoperability scores, and improvement activities. Automated gap identification with provider-specific action items | Salesforce Health Cloud Reports & Dashboards (Phase 1; CRM Analytics Phase 2+) + VV predictive models for quality measure trending |
| **Regulatory Change Engine** *(Phase 3)* | NLP-powered monitoring of Federal Register, CMS/HRSA policy updates, and state regulatory changes. Automated impact assessment and policy update workflows | VV NLP pipeline (fine-tuned language models) + Salesforce Flow for workflow triggers |

**Talk-to for Michael Jarvis (HADRIUS investor):** "Michael, you know from HADRIUS how painful healthcare compliance is. We're taking that same compliance-automation concept and purpose-building it for the rural clinic market -- a segment HADRIUS and others don't specifically serve. Our AI engine doesn't just track compliance status; it's designed to predict where a clinic is at risk of falling out of compliance 60--90 days in advance based on trending data, staffing changes, and regulatory calendar analysis -- that's the capability we're building in Phase 1 and validating in the pilot. That's the difference between reactive penalty management and proactive compliance assurance."

---

### 3.2 Care Module: AI-Driven Preventive Healthcare & Wearables

**The problem VV solves:** Rural patients with chronic conditions (diabetes, hypertension, COPD, heart failure) only see their provider a few times per year. Between visits, there's zero monitoring. By the time they return -- or present at the ER -- their condition has deteriorated significantly. Meanwhile, CMS is actively paying for Remote Patient Monitoring (RPM) and Chronic Care Management (CCM), but RHCs lack the technology infrastructure to capture these services.

**VV's technical implementation:**

| Capability | How VV Builds It | Technology |
|---|---|---|
| **AI Risk Stratification** | Analyze patient panel data (demographics, diagnoses, labs, utilization history, social determinants) to score every patient by risk of hospitalization, ER visit, or clinical deterioration within 30/60/90 days | VV ML models (gradient-boosted ensemble + logistic regression baseline) trained on CMS public use files and clinical datasets; deployed as Salesforce Einstein custom models or external API |
| **Wearable/RPM Integration** | Ingest continuous data streams from clinical-grade RPM devices (blood pressure cuffs, glucose monitors, pulse oximeters, weight scales). Cellular-connected devices prioritized for rural patients without reliable WiFi. Transform into structured FHIR Observations for clinical use | VV device integration layer via RPM aggregator API (Tenovi or Smart Meter -- cellular-connected, zero patient tech setup); FHIR R4 Observation resources stored in Salesforce Health Cloud |
| **Deterioration Early Warning** | Continuous analysis of RPM data streams to detect trending deterioration (rising BP, A1C drift, weight gain patterns in CHF, SpO2 decline). Alert care team before acute episode | VV temporal analytics models (sliding-window trend analysis, anomaly detection); alert routing through Salesforce Flow to provider mobile app and care coordinator dashboard |
| **Care Gap Detection** | Identify patients overdue for preventive screenings, immunizations, chronic disease follow-ups, and annual wellness visits. Auto-generate outreach lists and patient communications | Salesforce Health Cloud care plan templates + VV analytics comparing patient records against USPSTF/CMS preventive care guidelines |
| **Telehealth Orchestration** | Integrated scheduling, virtual visit workflow, and documentation for telehealth encounters. Ensures RPM data is available to provider during virtual visit | Salesforce Health Cloud + VV integration with telehealth platforms (Zoom for Healthcare, Doxy.me) via APIs |

**Talk-to for Michael Jarvis (OHM/wearables investor):** "Michael, you see with OHM where heart monitoring and wearables are going. The missing piece for rural clinics isn't the device -- it's the platform that ingests that data, runs clinical analytics on it, and makes it actionable for a provider who has 2,500 patients and 10 minutes per visit. We've built the AI layer that turns raw wearable data into clinical intelligence -- risk scores, trend alerts, care gap notifications -- all surfaced inside the workflow the clinic already uses. And here's the revenue angle: every RPM patient generates $100--$180/month in CMS reimbursement (CPT 99454 device monitoring at $52 plus 99457 clinician time at $52, with additional billing for extended management) that these clinics are currently leaving on the table."

**Talk-to for Tai Mai (physician/scientist, MEDA Ventures):** "Tai, from a clinical perspective, our AI risk stratification is built on validated clinical frameworks -- we're not replacing clinical judgment, we're augmenting it. The models are trained on CMS public use files and clinical datasets, producing risk scores that map to established clinical intervention pathways. Critically, every risk score comes with the top contributing factors explained using SHAP values -- so the provider doesn't just see 'high risk,' they see 'high risk driven by rising A1C, missed cardiology referral, and 3 ER visits in 6 months.' The provider always retains decision authority. The AI surfaces the patients who need attention most, which is transformative when you have one provider managing thousands of patients in a rural county with no specialists within 60 miles. Our Phase 1 performance target is AUC-ROC above 0.75 with sensitivity above 80% for the highest-risk decile -- and we'll measure actual outcomes against predictions during the pilot."

---

### 3.3 Collect Cash Module: Revenue Optimization

**The problem VV solves:** RHCs operate on razor-thin margins. They systematically under-bill because they lack the technology to optimize coding, capture new reimbursement categories (RPM, CCM, TCM), prevent denials, and maximize quality bonuses. Meanwhile, CMS has created numerous incentive programs specifically to encourage the care activities the 3C Platform enables -- but clinics can't capture the revenue without the documentation and data infrastructure.

**VV's technical implementation:**

| Capability | How VV Builds It | Technology |
|---|---|---|
| **Automated Coding Optimization** *(Phase 2)* | NLP analysis of clinical documentation to identify under-coded encounters, missed HCC (Hierarchical Condition Category) codes, and documentation gaps that reduce reimbursement | VV NLP models (spaCy + MedCAT) fine-tuned on medical coding datasets; integrated as real-time suggestions during documentation workflow in Salesforce |
| **RPM/CCM Billing Capture** | Automated tracking of RPM device data transmission days (16-day minimum for 99454), clinician interactive time (20-minute minimum for 99457/99458), CCM time tracking (20-minute minimum for 99490), and TCM follow-up windows. Auto-generates billable encounter records | VV time/event tracking engine integrated with Salesforce Health Cloud; automated claims preparation for clearinghouse submission |
| **Denial Prevention** *(Phase 3)* | Pre-submission claims scrubbing against payer rules, prior authorization tracking, and documentation completeness verification. ML model trained on historical denial patterns to flag high-risk claims | VV predictive model + rules engine; Salesforce integration with clearinghouses (Office Ally Phase 2; Availity/Change Healthcare Phase 3) |
| **MIPS/APM Dashboard** | Real-time tracking of Merit-based Incentive Payment System scores across all four categories (Quality, Cost, Promoting Interoperability, Improvement Activities). Projected payment adjustment modeling | Salesforce Reports & Dashboards (Phase 1; CRM Analytics Phase 2+) + VV scoring models pulling from clinical, EHR, and claims data |

---

## 4. TECHNICAL DIFFERENTIATORS -- WHAT MAKES VV UNIQUE

### 4.1 Military-Grade Applied to Healthcare

VV's work on DoD health AI projects (edge computing, DDIL environments, HIPAA-equivalent PHI protections under DoD 6025.18-R) translates directly:

| DoD Capability | Rural Healthcare Application |
|---|---|
| AI triage classification in austere environments | AI risk stratification for underserved rural populations |
| DDIL-native architecture (works without connectivity) | Resilient architecture designed for clinics with unreliable broadband (cellular-connected devices, asynchronous data sync) |
| Edge inference on low-power devices | Wearable data processing without constant cloud dependency |
| HL7 FHIR / EHR integration (MHS GENESIS) | HL7 FHIR / EHR integration (eClinicalWorks, athenahealth, MEDITECH, Azalea Health) |
| NIST 800-171 / CMMC compliance | HIPAA Security Rule / HITECH compliance |
| Real-time monitoring with deterioration alerts | RPM with chronic disease deterioration early warning |
| Multi-casualty triage prioritization | Multi-patient panel risk stratification and care prioritization |

### 4.2 The "Systems Approach" Advantage

Competitors in this space sell point solutions:
- Compliance tools (Compliancy Group, HIPAA One, Intraprise Health) -- compliance only, not RHC-specific
- RPM platforms (BioIntelliSense, Rimidi, Optimize Health) -- care/monitoring only
- Revenue cycle (Waystar, Athena RCM, AdvancedMD) -- billing only

**ACT's 3C Platform is the only solution that unifies all three on a single data model.** This matters because:

1. **Compliance data feeds care decisions** -- knowing which quality measures a clinic must meet shapes which patients need outreach
2. **Care activities generate revenue** -- every RPM reading, CCM call, and AWV captured is a billable event
3. **Revenue funds better care** -- the incremental $195K--$267K/clinic/year in new CMS revenue pays for the staff and tools to deliver preventive care

This flywheel only works when all three modules share the same patient record, the same analytics engine, and the same workflow platform.

---

## 5. MARKET OPPORTUNITY -- VIRGINIA FIRST, THEN NATIONAL

| Metric | Virginia | National |
|---|---|---|
| Rural Health Clinics (+ FQHCs) | 106 RHCs + 27 FQHCs | 5,500+ RHCs |
| Est. SaaS Revenue per Clinic | $2,000--$4,000/month | $2,000--$4,000/month |
| Virginia TAM (133 clinics) | $3.2M--$6.4M/year | -- |
| National TAM | -- | $132M--$264M/year |
| RPM/CCM/MIPS Revenue Unlock per Clinic | $195K--$267K/year (new CMS revenue, conservative estimate based on 80 RPM + 120 CCM patients) | -- |

**Virginia-first strategy aligns with VIPC mission:** Job creation (technical implementation, training, support roles), Virginia-based RHC outcomes improvement, and a scalable model that exports nationally.

---

## 6. IMPLEMENTATION ROADMAP

| Phase | Timeline | Deliverables |
|---|---|---|
| **Phase 1: MVP** *(VIPC Grant)* | Months 1--4 | Salesforce Health Cloud configured (5 users); HIPAA compliance tracker live; EHR FHIR integration with 1 pilot clinic EHR; AI risk stratification model v1 deployed; RPM integration (1--2 device types); RPM/CCM billing tracker live; 2--3 Virginia RHCs live on platform; baseline outcomes measured |
| **Phase 2: Full Product** | Months 5--10 | MuleSoft integration layer; additional EHR integrations (2--3 systems); NLP coding optimization; telehealth integration; ML-based deterioration prediction; HRSA UDS automation; 10+ Virginia RHCs live |
| **Phase 3: Scale** | Months 11--18 | AppExchange managed package; 50+ Virginia RHCs; national expansion (WV, KY, TN, NC); Series A raise based on ARR and clinical outcomes data |

**$50K VIPC Grant Allocation:**
- Contract Salesforce developer (part-time, 3 months): $30,000
- Salesforce Health Cloud licenses + Shield encryption (5 users, 4 months): $8,450
- Pilot clinic onboarding (travel, training, RPM devices): $4,500
- GCP hosting for AI models (HIPAA BAA, 4 months): $2,000
- Legal (HIPAA BAA, pilot agreements): $2,000
- ML model development tools/compute: $1,500
- Miscellaneous (domain, tools): $1,550

**Total project value:** $173,000 ($50K VIPC grant + $123K team sweat equity in-kind)

---

## 7. PRESENTATION TALKING POINTS -- TECHNICAL Q&A PREP

### "How does the AI actually work?"
"We use gradient-boosted ensemble models and NLP pipelines for three core functions: patient risk stratification, clinical documentation analysis, and regulatory change monitoring. The models are trained on CMS public use datasets and clinical data, and they run inside the Salesforce platform using Einstein AI or as external microservices via API. The key is that every AI output is advisory -- the provider sees a risk score and a recommended action, but they make the clinical decision. We follow the same human-in-the-loop design philosophy we use in our DoD clinical AI work."

### "What about HIPAA and security?"
"Security is in our DNA -- we build systems for DoD environments that are far more restrictive than HIPAA. The 3C Platform inherits Salesforce's FedRAMP Moderate and SOC 2 Type II certifications. We layer on encrypted PHI at rest (AES-256) and in transit (TLS 1.2+), role-based access control, immutable audit logging, and continuous compliance monitoring. Every access to patient data is logged, anomalies are flagged in real time, and we automate the documentation that proves compliance to auditors."

### "How do you integrate with existing clinic systems?"
"HL7 FHIR R4 is our integration standard -- it's the same standard CMS mandated for interoperability. We use Salesforce's native integration capabilities and FHIR APIs to connect to whichever EHR the clinic runs -- eClinicalWorks, athenahealth, MEDITECH, Azalea Health, or any FHIR-enabled system. These are the EHRs that actually dominate the rural clinic market. For wearables, we integrate through RPM device aggregators like Tenovi that support 40+ FDA-cleared devices over a single API -- all cellular-connected so they work for rural patients without WiFi or smartphones. The clinic doesn't rip and replace anything -- we layer on top of their existing systems."

### "What's the revenue model?"
"SaaS subscription -- $2,000 to $4,000 per clinic per month depending on module configuration and patient volume. But here's the critical point: the platform unlocks $195,000 to $267,000 per year in new CMS reimbursement per clinic through RPM, CCM, and quality bonus optimization. The platform pays for itself multiple times over. That's not theoretical -- those are existing CMS billing codes that clinics simply can't capture without the technology infrastructure."

### "Why Salesforce and not a custom build?"
"Three reasons. First, Salesforce Health Cloud is already HIPAA-compliant and FedRAMP-authorized -- that's millions in compliance infrastructure we don't have to build. Second, Salesforce's integration ecosystem gives us connectivity to every major EHR, clearinghouse, and health data system -- native FHIR support in Phase 1, MuleSoft connectors at scale. Third, it's a platform RHC staff can actually use -- Salesforce's UI is designed for non-technical users, which matters when your clinic administrator wears five hats. We focus our engineering on the AI layer and integrations that differentiate the product, not on rebuilding infrastructure that already exists."

### HARD QUESTIONS -- ADVERSARIAL Q&A PREP

### "What clinical validation have you completed?"
"Phase 1 IS the clinical validation. We're training the risk stratification model on CMS public use files -- the same datasets used in peer-reviewed health services research. The model targets AUC-ROC above 0.75 with sensitivity above 80% for the highest-risk decile. During the 4-month pilot, we'll measure actual patient outcomes against model predictions -- that's the validation data set. This is a build-measure-learn approach, and the pilot outcomes report is what positions us for Series A."

### "Why wouldn't an existing player (athenahealth, Waystar, etc.) just build this?"
"Incumbents are optimized for their lane. athenahealth is an EHR -- they'll improve billing within their ecosystem but won't build a compliance module or purpose-build for RHC-specific workflows. Waystar is revenue cycle -- they have no clinical or compliance play. The competitors who come closest, like ThoroughCare, cover CCM/RPM billing but don't do compliance and don't have AI risk stratification. Building all three modules on a single data model requires a platform approach that no incumbent has incentive to pursue for a 5,500-clinic niche. That's our window."

### "What happens if the pilot fails or clinics don't adopt?"
"Our risk register accounts for this. If clinic staff adoption is low, we've built in Sprint 1 clinic involvement so the UI matches their actual workflow -- not what we think it should be. If RPM enrollment is low, we offer a device-included model so cost isn't a barrier for patients. If the EHR integration takes longer than expected, we fall back to manual CSV data import. The key mitigation is that we're targeting 2--3 pilot clinics, not one -- so a single clinic dropout doesn't kill the pilot."

### "What's your FDA regulatory risk for the AI?"
"We've analyzed this carefully. Our risk stratification tool qualifies for the clinical decision support exemption under the 21st Century Cures Act -- it meets all four criteria: it doesn't acquire signals from devices, it displays and analyzes medical information, it's intended to support provider recommendations, and the provider can independently review the basis for every score. We show the SHAP values -- the contributing factors -- for every risk score. The January 2026 FDA CDS guidance update actually broadens enforcement discretion in our favor. We document intended use from Day 1 and maintain a regulatory file."

---

## 8. KNOW YOUR AUDIENCE -- PERSONALIZED ANGLES

### Jennifer O'Daniel (VVP Lead)
- **Cares about:** Virginia economic impact, job creation, grant ROI, scalability
- **Hit:** "The $50K grant funds a proof-of-concept at 2--3 Virginia RHCs over 4 months. The combined project value is $173,000 -- $50K from VIPC and $123K in team sweat equity. The pilot data positions ACT for a seed/Series A raise by Month 10, which funds 4--6 Virginia-based technical roles (Salesforce developer, ML engineer, implementation specialists). This is a force multiplier -- every clinic we bring online improves health outcomes for thousands of rural Virginians and creates the workforce to scale statewide."

### Michael Jarvis (Investor -- HADRIUS/Compliance + OHM/Wearables)
- **Cares about:** Compliance tech market, wearables/preventive health, investment thesis validation
- **Hit:** "Michael, we sit at the intersection of your two investment themes -- compliance automation and wearable health monitoring -- but for a market segment nobody's serving. Rural clinics need both, and they need them integrated. That's our moat."

### Tai Mai (MEDA Ventures -- Physician/Scientist)
- **Cares about:** Clinical validity, patient outcomes, scalable health impact, Seed/Series A viability
- **Hit:** "Tai, the clinical logic is straightforward -- risk-stratify the panel, intervene early, monitor continuously between visits. The technology finally makes that possible for a solo provider managing 2,500 patients in a rural county. And the CMS reimbursement model means the clinic can afford to do it."

---

*Prepared by: VV Technical Strategy | Authentic Consortium*
*Version 1.0 -- February 24, 2026*
