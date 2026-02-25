# VV TECHNICAL IMPLEMENTATION BRIEF

**Prepared for:** Will Nelson (Technical Presenter) | Authentic Consortium
**Presentation:** VIPC VVP Launch Grant -- Final Presentation (Wednesday, Feb 26, 2026)
**Audience:** Jennifer O'Daniel (VVP Lead), Michael Jarvis (Healthcare Investor), Tai Mai (VIPC Healthcare Lead / MEDA Ventures)
**Classification:** Internal Prep Document -- Do Not Distribute

---

## EXECUTIVE SUMMARY

Authentic Consortium (ACT) is presenting the **3C Platform** -- a purpose-built solution for rural health clinics (RHCs) that solves three compounding crises: **Compliance**, **Care**, and **Collect Cash** (cost/revenue). Veteran Vectors (VV) designs and builds the platform using the same proven stack VV deploys for defense clients: **n8n** (workflow automation), **PostgreSQL** (database), and **Docker containers** on **Amazon GovCloud** (FedRAMP High, HIPAA-eligible). The platform is designed as a turnkey system deployable to any RHC, then customizable per clinic's EHR, device mix, payer landscape, and workflows. **All intellectual property is owned by Authentic Consortium (ACT).** VV builds and maintains the system under ACT's direction -- no enterprise licensing, no per-seat fees, no vendor lock-in. The modular architecture allows clinics to subscribe to only the modules they need, scaling from a single-module Essentials tier to a full-platform Enterprise tier.

---

## 1. THE PROBLEM: WHY RURAL CLINICS ARE FAILING

Virginia has **106 Rural Health Clinics** and 27 FQHCs (5,500+ RHCs nationally) facing a convergence of crises -- with 3 Virginia RHCs closing in 2025 alone due to federal funding cuts and 9 rural hospitals at risk of closure:

- **Compliance burden:** HIPAA, HRSA reporting, CMS quality metrics, FCC (telehealth/broadband) -- each with different reporting cadences, data formats, and penalty structures. A single RHC may face 15+ distinct regulatory obligations. Non-compliance triggers loss of Medicare/Medicaid reimbursement -- which is 60--80% of RHC revenue
- **Care gaps:** Provider shortages (1 physician per 2,500+ patients in some Virginia counties), chronic disease prevalence 30--40% above urban averages, limited specialist access, no preventive care infrastructure. Patients present late-stage because there's no monitoring between annual visits
- **Revenue leakage:** Undercoding, missed quality bonuses (MIPS/APM), denied claims from documentation gaps, and inability to capture RPM/CCM reimbursement codes that CMS now pays for. RHCs leave an estimated $195K--$267K per clinic per year on the table in unrealized RPM, CCM, and quality bonus revenue (based on conservative RPM/CCM enrollment rates and MIPS penalty avoidance)

**The key insight:** These three problems are interconnected. Compliance failures cause revenue loss. Care gaps drive costly ER utilization. Revenue shortfalls prevent investment in better care. No one is offering a unified platform that treats all three as a single system.

---

## 2. THE 3C PLATFORM: TECHNICAL ARCHITECTURE

### 2.1 Platform Foundation -- Proven VV Stack on Amazon GovCloud

The 3C Platform uses the **same architecture VV deploys for defense clients** -- containerized, self-hosted, and portable:

- **Amazon GovCloud** -- FedRAMP High authorized, HIPAA BAA, ITAR-compliant. Same infrastructure hosting DoD health systems. RDS PostgreSQL, ECS Fargate, S3, KMS, CloudTrail all HIPAA-eligible
- **n8n** (self-hosted) -- Visual workflow automation and integration engine. Handles EHR integration, RPM device ingestion, billing threshold automation, compliance task scheduling, and alert routing. Template workflows cloned and configured per clinic
- **PostgreSQL 16** (Amazon RDS) -- Central data store with row-level security for multi-tenant clinic isolation. AES-256 encryption at rest via KMS. PGAudit for HIPAA audit logging
- **Python/FastAPI** -- Backend API layer for ML model serving, high-frequency device data ingestion, and FHIR data transforms
- **React/Next.js** -- Clinic-facing dashboard. Patient 360, compliance tracker, billing tracker, MIPS dashboard
- **NGINX** -- Reverse proxy with TLS 1.2+, HSTS, CSP, rate limiting
- **Docker** -- Containerized deployment. Same delivery model as VV's defense deployments
- **bonFHIR** -- Community n8n node providing native FHIR R4 actions and triggers for EHR connectivity, supplemented by n8n HTTP Request nodes for direct FHIR R4 API calls

**This is not a prototype stack.** VV is currently building a classified gap analysis platform for a defense client on this exact architecture (n8n + PostgreSQL + NGINX + Docker on GovCloud), with a deployment path from unclassified through TS/SCI. The 3C Platform applies the same proven components to healthcare.

### 2.2 Three Integrated Modules

```
+------------------------------------------------------------------+
|              3C PLATFORM (Amazon GovCloud)                         |
|                                                                   |
|  +------------------+  +------------------+  +------------------+ |
|  |   COMPLIANCE     |  |      CARE        |  |   COLLECT CASH   | |
|  |   MODULE         |  |      MODULE      |  |   MODULE         | |
|  |                  |  |                  |  |                  | |
|  | - HIPAA Audit    |  | - AI Risk        |  | - RPM/CCM Billing| |
|  |   Automation     |  |   Stratification |  |   Capture        | |
|  | - HRSA UDS       |  | - RPM Device     |  | - Coding         | |
|  |   Reporting      |  |   Integration    |  |   Optimization   | |
|  | - CMS Quality    |  | - Care Gap       |  | - Denial         | |
|  |   Dashboards     |  |   Detection      |  |   Prevention     | |
|  | - FCC Broadband  |  | - Deterioration  |  | - MIPS/APM       | |
|  |   Compliance     |  |   Early Warning  |  |   Optimization   | |
|  | - Regulatory     |  | - Telehealth     |  | - Revenue Cycle  | |
|  |   Change Engine  |  |   Orchestration  |  |   Analytics      | |
|  +------------------+  +------------------+  +------------------+ |
|                              |                                    |
|         +--------------------+--------------------+               |
|         |            AI/ML ENGINE (VV)            |               |
|         | - Risk Stratification (XGBoost + SHAP)  |               |
|         | - NLP for Documentation (spaCy/MedCAT)  |               |
|         | - Anomaly Detection (RPM trends)        |               |
|         +--------------------+--------------------+               |
|                              |                                    |
|         +--------------------+--------------------+               |
|         |    n8n WORKFLOW ENGINE + Python Services |               |
|         | - EHR FHIR R4 (bonFHIR node)            |               |
|         | - RPM device API ingestion              |               |
|         | - Billing threshold triggers             |               |
|         | - Compliance task automation             |               |
|         | - Alert routing + notifications          |               |
|         +-----------------------------------------+               |
+------------------------------------------------------------------+
```

### 2.3 The "Out of the Box, Then Customize" Model

Each clinic deployment starts from a **base configuration** that works immediately, then customizes:

| Layer | Out of the Box | Customized Per Clinic |
|---|---|---|
| **n8n workflows** | Template workflows for RPM ingestion, billing triggers, compliance tasks, care gap detection, alert routing | Configured for clinic's specific EHR (eCW vs athena vs Azalea), device vendor (Tenovi vs Smart Meter), and payer mix |
| **Dashboard** | Standard 3C dashboard with all modules, pre-built MIPS measures, billing tracker, patient 360 | Custom branding, role-specific views (provider vs admin vs billing), clinic-specific quality measures |
| **Data model** | Standard patient, encounter, RPM reading, billing event, compliance task tables (PostgreSQL with RLS) | Custom fields per clinic (referral workflows, specialty tracking, local program enrollment) |
| **Alert rules** | Clinical defaults (BP >180, SpO2 <90, weight gain >3 lbs/day, A1C >9) | Provider-tuned thresholds per patient population and clinical preference |
| **Billing rules** | Standard CMS RPM/CCM/TCM codes and thresholds | Clinic-specific payer rules, MAC-specific requirements, state Medicaid variations |

**Onboarding a new clinic:** Clone base n8n workflow templates, configure EHR credentials via Named Credentials, set up device vendor API connection, customize alert thresholds, train staff on dashboard. Target: **clinic live in 2 weeks** after initial onboarding meeting.

### 2.4 Modular Service Tiers -- Adapt to Any Clinic Size

Not every clinic needs every module. The 3C Platform is architected as **independent, composable modules** activated per clinic via configuration flags -- not separate codebases:

| Tier | Modules Included | Target Clinic | Price Range |
|---|---|---|---|
| **Essentials** | Compliance Module only (HIPAA tracker, risk assessment, CMS quality dashboard) | Small RHCs (<500 patients) needing compliance automation first | $500--$1,000/month |
| **Professional** | Compliance + Care (adds RPM device integration, AI risk stratification, care gap detection, deterioration alerts) | Mid-size RHCs (500--1,500 patients) ready for RPM/CCM programs | $1,500--$2,500/month |
| **Enterprise** | All 3 modules: Compliance + Care + Collect Cash (adds RPM/CCM billing automation, MIPS optimization, coding optimization, denial prevention) | Larger RHCs and FQHCs (1,500+ patients) maximizing revenue capture | $2,500--$4,000/month |

**How modularity works technically:**
- Each module is a set of n8n workflow templates, Python services, and React dashboard components
- A `clinic_config` table in PostgreSQL stores which modules are active per clinic (`modules_enabled: ['compliance', 'care', 'billing']`)
- Feature flags control which workflows execute and which dashboard panels render
- Upgrading a clinic from Essentials to Professional means flipping a flag and deploying pre-built workflow templates -- not writing new code
- This is the same configuration-driven deployment pattern VV uses for defense clients where different tiers get different capabilities

**Why this matters for scalability:** A 200-patient RHC that only needs HIPAA tracking pays $500/month. A 2,000-patient FQHC running full RPM/CCM programs pays $4,000/month. Same platform, same codebase, different configuration. This lets ACT serve the full spectrum of rural healthcare facilities without maintaining multiple products.

---

## 3. VV'S TECHNICAL ROLE -- MODULE BY MODULE

### 3.1 Compliance Module: Automated Regulatory Intelligence

**The problem VV solves:** RHC administrators spend 15--20 hours/week on manual compliance tasks -- tracking HIPAA training, assembling HRSA UDS reports, monitoring CMS quality measures, documenting FCC broadband obligations. When they miss something, the penalties are existential.

| Capability | How VV Builds It | Technology |
|---|---|---|
| **HIPAA Compliance Automation** | Continuous monitoring of system access logs, PHI handling, security controls. Automated risk assessments per NIST SP 800-66. Real-time alerts for policy violations | PostgreSQL audit triggers + PGAudit + n8n monitoring workflows + VV anomaly detection models |
| **HRSA UDS Report Generation** *(Phase 2)* | Automated data extraction from EHR via FHIR. Pre-populated UDS tables with validation checks | n8n EHR workflows (bonFHIR node) + Python data transformation pipeline |
| **CMS Quality Dashboard** | Real-time MIPS quality measures, PI scores, improvement activities. Automated gap identification | React dashboard + PostgreSQL analytics views + VV predictive models |
| **Regulatory Change Engine** *(Phase 3)* | NLP monitoring of Federal Register, CMS/HRSA policy updates. Automated impact assessment | VV NLP pipeline (Python) + n8n scheduled workflows for feed monitoring |

**Talk-to for Michael Jarvis (HADRIUS investor):** "Michael, you know from HADRIUS how painful healthcare compliance is. We're taking that compliance-automation concept and purpose-building it for rural clinics -- a segment nobody's serving. Our platform doesn't just track compliance status; it monitors trending data, staffing changes, and regulatory calendars to flag compliance risks before they become violations. As we accumulate clinic data during the pilot, we'll build the predictive models that can forecast risk 60--90 days in advance. And we built it on the same GovCloud infrastructure we use for our defense clients -- FedRAMP High, not FedRAMP Moderate like the commercial SaaS platforms."

---

### 3.2 Care Module: AI-Driven Preventive Healthcare & RPM

**The problem VV solves:** Rural patients with chronic conditions only see their provider a few times per year. Between visits, zero monitoring. CMS is actively paying for RPM and CCM, but RHCs lack the technology to capture these services.

| Capability | How VV Builds It | Technology |
|---|---|---|
| **AI Risk Stratification** | Score every patient by risk of hospitalization/ER visit within 30/60/90 days. Top contributing factors explained via SHAP values | VV ML models (XGBoost + logistic regression) trained on CMS public use files; served via FastAPI on GovCloud |
| **RPM Device Integration** | Ingest continuous data from cellular-connected RPM devices (BP cuffs, glucose monitors, pulse ox, scales). Zero patient tech setup required | Python ingestion service polling Tenovi/Smart Meter APIs → PostgreSQL → n8n alert workflows when thresholds exceeded |
| **Deterioration Early Warning** | Detect trending deterioration (rising BP, A1C drift, weight gain in CHF, SpO2 decline). Alert care team before acute episode | VV temporal analytics (sliding-window trend analysis); n8n alert routing to provider email/SMS |
| **Care Gap Detection** | Identify patients overdue for screenings, immunizations, chronic disease follow-ups, annual wellness visits | n8n scheduled workflows comparing patient records against USPSTF/CMS preventive care guidelines |

**Talk-to for Michael Jarvis (OHM/wearables investor):** "Michael, you see with OHM where wearables are going. The missing piece for rural clinics isn't the device -- it's the platform that ingests that data, runs analytics on it, and makes it actionable for a provider with 2,500 patients and 10 minutes per visit. Every RPM patient generates $100--$180/month in CMS reimbursement (CPT 99454 at $52 plus 99457 clinician time at $52, with additional billing for extended management) that these clinics are currently leaving on the table. We use cellular-connected devices so they work for rural patients without WiFi."

**Talk-to for Tai Mai (physician/scientist, MEDA Ventures):** "Tai, our AI risk stratification is built on validated clinical frameworks -- trained on CMS public use files and clinical datasets. Every risk score comes with the top contributing factors via SHAP values -- so the provider sees 'high risk driven by rising A1C, missed cardiology referral, and 3 ER visits in 6 months.' The provider always retains decision authority. Phase 1 targets AUC-ROC above 0.75 with sensitivity above 80% for the highest-risk decile -- and we measure actual outcomes against predictions during the pilot."

---

### 3.3 Collect Cash Module: Revenue Optimization

**The problem VV solves:** RHCs systematically under-bill. They lack technology to capture RPM/CCM reimbursement, optimize coding, prevent denials, and maximize quality bonuses.

| Capability | How VV Builds It | Technology |
|---|---|---|
| **RPM/CCM Billing Capture** | Automated tracking of device data transmission days (16-day minimum for 99454), clinician time (20-min minimum for 99457/99458), CCM time (20-min for 99490). Auto-generates billable events | n8n scheduled workflows aggregating RPM readings + clinician time from PostgreSQL; auto-flags billable thresholds |
| **Automated Coding Optimization** *(Phase 2)* | NLP analysis of clinical documentation to identify missed HCC codes and documentation gaps | VV NLP models (spaCy + MedCAT); served via FastAPI |
| **Denial Prevention** *(Phase 3)* | Pre-submission claims scrubbing against payer rules, prior auth tracking, documentation completeness | VV predictive model + n8n rules engine + clearinghouse integration (Office Ally first) |
| **MIPS/APM Dashboard** | Real-time MIPS scores across Quality (30%), Cost (30%), PI (25%), IA (15%). Payment adjustment projection | React dashboard + PostgreSQL analytics + VV scoring models |

---

## 4. TECHNICAL DIFFERENTIATORS

### 4.1 Military-Grade Applied to Healthcare

| DoD Capability | Rural Healthcare Application |
|---|---|
| AI triage classification in austere environments | AI risk stratification for underserved rural populations |
| DDIL-native architecture (works without connectivity) | Architecture designed for unreliable rural broadband: cellular RPM devices bypass clinic WiFi; asynchronous data sync tolerates intermittent connectivity |
| Containerized deployments for classified networks (GovCloud → Game Warden) | Same containerized deployment for HIPAA-compliant healthcare |
| n8n workflow automation replacing Power Automate | n8n workflow automation replacing Salesforce/enterprise SaaS |
| PostgreSQL with row-level security for data isolation | PostgreSQL with row-level security for multi-clinic tenant isolation |
| NIST 800-171 / CMMC compliance | HIPAA Security Rule / HITECH compliance |
| HL7 FHIR / EHR integration (MHS GENESIS) | HL7 FHIR / EHR integration (eClinicalWorks, athenahealth, MEDITECH, Azalea Health) |

### 4.2 Why Custom-Built Beats Enterprise SaaS

| Factor | Enterprise SaaS (Salesforce, etc.) | VV Custom Platform |
|---|---|---|
| **Per-clinic COGS** | ~$650/month (licenses alone) | ~$100--150/month at scale (infrastructure only, no licensing) |
| **Gross margin at $2K/month** | ~67% | **93--95%** (at scale; 97%+ at $4K tier) |
| **Vendor lock-in** | Complete | **Zero** -- VV owns the code |
| **Compliance posture** | FedRAMP Moderate infrastructure | **FedRAMP High** infrastructure (GovCloud) |
| **Customization** | Limited to platform capabilities | **Unlimited** -- it's our code |
| **Scale economics** | Costs scale linearly per seat | Costs scale sublinearly with infrastructure (shared resources across clinics) |
| **Year 1 licensing cost** | ~$150K+ (Salesforce + MuleSoft) | **$0** (open-source stack) |

### 4.3 The "Systems Approach" Advantage

Competitors sell point solutions:
- Compliance tools (Compliancy Group, HIPAA One, Intraprise Health) -- compliance only
- RPM platforms (TelliHealth, Rimidi, Optimize Health) -- care/monitoring only
- Revenue cycle (Waystar, Athena RCM, AdvancedMD) -- billing only

**The 3C Platform unifies all three on a single data model.** Compliance data feeds care decisions. Care activities generate revenue. Revenue funds better care. This flywheel only works when all three modules share the same patient record, analytics engine, and workflow platform.

### 4.4 Intellectual Property Strategy

**All 3C Platform IP is owned by Authentic Consortium (ACT).** Veteran Vectors (VV) develops the platform under a work-for-hire arrangement with ACT. This means:

| IP Asset | Type | Owner | Protection |
|---|---|---|---|
| **3C Platform software** (all source code, configurations, templates) | Copyright / Trade Secret | **ACT** | Private GitHub repos; copyright registration; work-for-hire agreement with VV |
| **"Compliance → Care → Cash" unified data model** | Patent (provisional) | **ACT** | Provisional patent application targeting Month 2--3 |
| **Automated RPM/CCM billing threshold detection and revenue optimization pipeline** | Patent (provisional) | **ACT** | Method for automated tracking of device transmission days, clinician time, and mutual exclusivity logic (99445/99454, 99470/99457) to generate verified billable events |
| **n8n workflow template library** (EHR integration, RPM ingestion, billing automation) | Trade Secret | **ACT** | Proprietary clinic-specific workflow configurations are core competitive advantage |
| **ML models** (risk stratification, deterioration prediction, coding optimization) | Trade Secret | **ACT** | Trained model weights, feature engineering, SHAP-based explainability pipeline |
| **Clinical rules engine** (care gap detection, MIPS scoring, regulatory compliance logic) | Trade Secret | **ACT** | Proprietary encoding of CMS/HIPAA/HRSA rules into automated workflows |

**What is patentable:**
1. **The unified compliance-care-revenue platform architecture** -- the specific method of integrating regulatory compliance event tracking, AI-driven clinical risk stratification, and automated CMS billing capture on a single shared data model with bidirectional data flows where compliance status informs risk scoring, risk scores trigger care workflows that generate billable events, and billing outcomes feed back into compliance reporting. This creates a closed-loop system that no existing RHC platform implements
2. **The automated RPM/CCM billing threshold detection and revenue optimization pipeline** -- the specific method of ingesting device data, tracking transmission days and clinician time against CMS billing rules, and auto-generating billable events with mutual exclusivity logic (99445 vs 99454, 99470 vs 99457)
3. **The configuration-driven multi-tenant clinic deployment model** -- the method of deploying a standardized healthcare platform via feature flags and template workflows that adapt to each clinic's EHR, device mix, payer landscape, and regulatory requirements without custom code (protected as trade secret; configuration-driven deployment elements are folded into Patent #1 as part of the unified architecture)

**Patent timeline:** File 2 provisional patent applications during Phase 1 (Months 2--3) to establish priority date -- one covering the unified platform architecture with configuration-driven modularity, one covering the automated billing threshold detection pipeline. Convert to full utility patent applications within 12 months. Budget: ~$5,000--$7,000 from contingency for 2 provisional filings (patent attorney + USPTO fees). The configuration-driven deployment model is additionally protected as a trade secret (proprietary workflow templates and clinic configuration logic).

---

## 5. MARKET OPPORTUNITY -- VIRGINIA FIRST, THEN NATIONAL

| Metric | Virginia | National |
|---|---|---|
| Rural Health Clinics (+ FQHCs) | 106 RHCs + 27 FQHCs | 5,500+ RHCs |
| Est. SaaS Revenue per Clinic (3 tiers) | $500--$4,000/month | $500--$4,000/month |
| Virginia TAM (133 clinics) | $3.2M--$6.4M/year | -- |
| National TAM | -- | $132M--$264M/year |
| Revenue Unlock per Clinic | $195K--$267K/year | -- |

---

## 6. IMPLEMENTATION ROADMAP

| Phase | Timeline | Deliverables |
|---|---|---|
| **Phase 1: MVP** *(VIPC Grant)* | Months 1--4 | All 3 service tiers shippable: Essentials (compliance), Professional (+ care/RPM), Enterprise (+ billing). Provisional patent applications filed (Months 2--3). 2--3 Virginia RHCs live across tiers |
| **Phase 2: Full Product** | Months 5--10 | Tiers hardened. Additional EHR integrations. NLP coding, telehealth, denial prevention. 10+ Virginia RHCs. Land-and-expand (tier upgrades tracked). Provisional patents converted to utility applications |
| **Phase 3: Scale** | Months 11--18 | Multi-region GovCloud. Automated onboarding (<1 day any tier). 50+ VA → national (WV, KY, TN, NC). Series A based on ARR, outcomes, patent portfolio |

**$50K VIPC Grant Allocation:**

| Item | Cost |
|---|---|
| AWS GovCloud (ECS Fargate + RDS + S3 + KMS, 4 months) | $3,000 |
| RPM devices for pilot (15--20 units, cellular-connected) | $2,500 |
| Pilot clinic onboarding (travel, training, materials) | $4,500 |
| ML model training compute (GovCloud GPU instances) | $1,500 |
| Legal (HIPAA BAA templates, pilot agreements) | $3,000 |
| EHR developer program access + FHIR sandbox fees | $500 |
| Domain, SSL, email, monitoring tools | $1,000 |
| **Contingency / additional pilots** | **$34,000** |
| **Total** | **$50,000** |

**Total project value:** ~$194,000 ($50K VIPC grant + ~$144K team sweat equity in-kind: Will at 640 hrs, plus clinical advisory, project management, and compliance expertise)

**Why 68% contingency?** Will is the developer. No contract developer cost. No enterprise licensing cost. The $50K funds infrastructure and operations -- not salaries or SaaS subscriptions. This gives ACT flexibility to expand the pilot, accelerate development, or absorb unexpected costs.

---

## 7. PRESENTATION Q&A PREP

### "How does the AI actually work?"
"Gradient-boosted ensemble models trained on CMS public use datasets -- the same data used in peer-reviewed health services research. The models produce risk scores with SHAP values explaining the contributing factors. Every output is advisory -- the provider sees the score and the reasoning, but they make the clinical decision. The models run as Python microservices on Amazon GovCloud, the same infrastructure we use for our defense AI work."

### "What about HIPAA and security?"
"The 3C Platform runs on Amazon GovCloud -- FedRAMP High authorized, which is a higher security posture than any commercial healthcare SaaS. We use AES-256 encryption at rest with customer-managed KMS keys, TLS 1.2+ in transit, PostgreSQL row-level security for clinic data isolation, PGAudit for complete audit trails, and application-level field encryption for the most sensitive PHI. Every access to patient data is logged, anomalies are flagged in real time, and we automate the documentation that proves compliance to auditors."

### "How do you integrate with existing clinic systems?"
"HL7 FHIR R4 -- the standard CMS mandated for interoperability. We use bonFHIR, a purpose-built FHIR integration library, inside our n8n workflow engine to connect to whichever EHR the clinic runs -- eClinicalWorks, athenahealth, MEDITECH, Azalea Health. Integration workflows are visual and clonable -- onboarding a new clinic with the same EHR takes hours, not weeks. For RPM devices, we integrate through cellular-connected aggregators like Tenovi (40+ FDA-cleared devices, single API) so they work for rural patients without WiFi."

### "What's the revenue model?"
"SaaS subscription -- $500 to $4,000 per clinic per month across three tiers. At the Enterprise tier, the platform unlocks $195,000 to $267,000 per year in new CMS reimbursement. Even at the Professional tier, RPM device monitoring alone can generate $50,000 or more in new annual revenue per clinic -- well above the subscription cost. And because we built on open-source infrastructure, our gross margins are 93--95% at scale. No enterprise licensing eating our unit economics."

### "Why not use Salesforce or an existing platform?"
"Cost and control. Salesforce Health Cloud licensing alone could consume 15--20% of the VIPC grant, and at scale, enterprise healthcare SaaS licensing can easily exceed $100K/year before serving a single patient. That kills unit economics for clinics with $34K--$95K total IT budgets. With our stack, each clinic costs us $100--$150/month in infrastructure at scale. We also get a higher security posture -- GovCloud is FedRAMP High vs Salesforce's FedRAMP Moderate. And we can customize every deployment to match each clinic's specific workflow, EHR, and payer mix."

### "Can you really build all this for $50K?"
"Yes -- because I'm the developer. There's no contract developer cost and no licensing fees. The $50K funds infrastructure, devices, legal, and pilot operations. The development is sweat equity -- ~$144K in in-kind value. I'm building this on the same stack I use for our defense clients -- n8n, PostgreSQL, Docker on GovCloud. The technology isn't novel; what's novel is applying it to this market with this clinical and billing logic."

### HARD QUESTIONS

### "What clinical validation have you completed?"
"Phase 1 IS the clinical validation. The risk model targets AUC-ROC above 0.75 with sensitivity above 80% for the highest-risk decile. During the 4-month pilot, we measure actual patient outcomes against predictions -- that's the validation data. The pilot outcomes report positions us for Series A."

### "Why wouldn't athenahealth or Waystar just build this?"
"Incumbents are optimized for their lane. athena is an EHR -- they won't build compliance or purpose-build for RHC workflows. Waystar is revenue cycle -- no clinical or compliance play. ThoroughCare covers CCM/RPM billing but has no compliance module or AI risk stratification. Building all three on a single data model requires a platform approach no incumbent has incentive to pursue for a 5,500-clinic niche."

### "What happens if the pilot fails?"
"We target 2--3 pilot clinics, not one -- a single dropout doesn't kill it. If staff adoption is low, we involve clinic staff in Sprint 1 design so the UI matches their workflow. If RPM enrollment is low, we provide devices at no cost to patients. If EHR integration takes longer than expected, we fall back to CSV import. And with $34K in contingency, we have budget to pivot."

### "Who owns the IP? Is this patentable?"
"All intellectual property is owned by Authentic Consortium. VV develops the platform under a work-for-hire arrangement with ACT. We've identified three areas of protectable innovation: the unified compliance-care-revenue platform architecture, the automated RPM/CCM billing threshold detection pipeline, and the configuration-driven clinic deployment model. We plan to file provisional patents on the first two in Months 2--3 to establish our priority date, and protect the configuration and workflow logic as trade secrets. The underlying open-source tools are free to use -- what's proprietary is our specific integration architecture, our clinical logic, our workflow templates, and our trained ML models. That's the IP."

### "What's your FDA regulatory risk?"
"Our risk stratification qualifies for the clinical decision support exemption under the 21st Century Cures Act -- all four criteria: doesn't acquire device signals, displays medical information, supports provider recommendations, and the provider can independently review the basis for every score via SHAP values. The January 2026 FDA CDS guidance update broadens enforcement discretion in our favor."

---

## 8. KNOW YOUR AUDIENCE

### Jennifer O'Daniel (VVP Lead)
- **Cares about:** Virginia economic impact, job creation, grant ROI, scalability, IP creation
- **Hit:** "The $50K grant funds 2--3 Virginia RHC pilots over 4 months. Combined project value is ~$194K -- $50K from VIPC plus ~$144K in sweat equity. All IP is owned by ACT, a Virginia entity -- we're filing 2 provisional patents on the unified platform architecture and the billing automation pipeline during Phase 1. Because we built on open-source infrastructure, $34K of the grant is contingency. Pilot data positions ACT for a seed or Series A raise by Month 10, enabling ACT to hire Virginia-based technical and implementation staff to support statewide rollout. The modular tiering means we can serve every rural clinic in Virginia, from the smallest 200-patient RHC to the largest FQHC."

### Michael Jarvis (Investor -- HADRIUS/Compliance + OHM/Wearables)
- **Cares about:** Compliance tech market, wearables/preventive health, investment thesis validation
- **Hit:** "We sit at the intersection of your two investment themes -- compliance automation and wearable health monitoring -- for a market segment nobody's serving. Our unit economics are compelling -- 93--95% gross margins because we own the stack. That's our moat."

### Tai Mai (MEDA Ventures -- Physician/Scientist)
- **Cares about:** Clinical validity, patient outcomes, scalable health impact, Series A viability
- **Hit:** "The clinical logic is straightforward -- risk-stratify, intervene early, monitor continuously. The technology makes this possible for a solo provider managing 2,500 patients. The CMS reimbursement model means the clinic can afford it. And 93--95% gross margins on a SaaS with built-in revenue justification for every buyer -- that's the Series A story."

---

*Prepared by: VV Technical Strategy | Authentic Consortium*
*Version 3.0 -- February 25, 2026*
