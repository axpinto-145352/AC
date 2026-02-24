# Document Polish Summary

**Date:** February 24, 2026
**Reviewer:** Final Polish Pass (Pre-Presentation)

---

## 01_VV_Technical_Brief.md

### Grammar and Style
- Changed "RHCs leave an estimated $50K--$150K" to "$100K--$250K" with clarifying phrase "in unrealized RPM, CCM, and quality bonus revenue" (line 22) for consistency with Implementation Guide's $195K--$267K calculation
- Softened "demonstrated through active DoD AI/health contracts" to "informed by DoD AI/health program experience" (line 12) to avoid unsubstantiated claims
- Changed "MuleSoft connectors" to "Phase 1: Salesforce Connect + Apex REST; Phase 2+: MuleSoft connectors" (line 35) for accuracy
- Changed "predicts where a clinic is going to fall out of compliance" to "is designed to predict where a clinic is at risk of falling out of compliance" (line 97) to frame as design goal
- Added SHAP explainability and AUC-ROC target to Tai Mai talk-to (line 117) for clinical depth
- Added "cellular-connected" device emphasis and Tenovi/Smart Meter references throughout (lines 110, 213) for rural accuracy
- Qualified RPM revenue as "$100--$180/month" with component breakdown (line 115) for defensibility

### Formatting Consistency
- Used en-dash convention (--) consistently throughout for ranges and parenthetical asides
- Phase markers added to all non-Phase-1 capabilities: *(Phase 2)* for UDS, NLP coding; *(Phase 3)* for Regulatory Change Engine, Denial Prevention
- CRM Analytics references updated to "Reports & Dashboards (Phase 1; CRM Analytics Phase 2+)" in both dashboard entries (lines 94, 132)
- Integration layer in architecture diagram updated to "SF Connect (MuleSoft P2)" (line 72)

### Content Additions
- Added "HARD QUESTIONS" adversarial Q&A section (after Section 7) with 4 prepared responses:
  - Clinical validation question
  - Incumbent competition question
  - Pilot failure question
  - FDA regulatory risk question
- Enhanced Jennifer O'Daniel talk-to with specific numbers: $173K total project value, $123K sweat equity, 4--6 Virginia roles (line 227)

### Cross-Document Reconciliation
- Replaced Epic/Cerner with eClinicalWorks, athenahealth, MEDITECH, Azalea Health in all EHR references (lines 147, 213)
- Updated Virginia RHC count from "370+" to "106 Rural Health Clinics and 27 FQHCs" (line 18)
- Reconciled grant budget to match Implementation Guide's itemized $50K breakdown (lines 191--198)
- Aligned revenue figures to $195K--$267K from Implementation Guide's bottoms-up calculation (line 177)
- Removed HADRIUS from competitor list; replaced with Intraprise Health (line 155)
- Fixed TLS version from "1.3" to "1.2+" (line 210)
- Fixed RPM billing code error: 16-day rule applies to CPT 99454, not 99457/99458 (line 130)
- Replaced consumer wearables (Apple Health, Google Health Connect, Withings) with clinical/cellular devices (Tenovi, Smart Meter) (line 110)

---

## 02_Implementation_Guide.md

### Grammar and Style
- Fixed "Heath care" typo to "Healthcare" (line 380)
- Changed "that's our entire grant" to "that's more than our entire grant" for MuleSoft $80K reference (line 71)
- Changed enrollment math from "10% enrolled in RPM (80 patients)" to "40% of eligible enrolled in RPM (80 patients)" to fix logical inconsistency (line 204)

### Technical Corrections
- Updated CRM Analytics from "Included in Health Cloud Enterprise" to "Reports/Dashboards: included; CRM Analytics: add-on ~$75--$150/user/month" (line 28)
- Removed "PostgreSQL-backed" parenthetical from Salesforce platform description (line 29)
- Updated US Core FHIR IG from "v6.1.0" to "v8.0.1 / STU8" with development version note (line 91)
- Corrected CPT 99458 rate from "$52.00" to "~$41.42" and removed incorrect "up to 3x/month" cap (line 193)
- Corrected CPT 99487 rate from "$144.00" to "~$131.65" (line 198)
- Added new 2026 RPM codes: CPT 99445 (2--15 day device supply) and CPT 99470 (10-min interactive) (lines 194--195)
- Updated MuleSoft Phase 2 cost from "~$50,000" to "~$80,000 (minimum)" (line 328)
- Fixed Phase 1 MVP diagram: replaced NLP coding suggestions with "FHIR data transforms" (lines 48--50) since NLP coding is Phase 2
- Updated RPM Data Ingestion row to reference "Tenovi or Smart Meter" instead of "Omron, Withings, Dexcom" (line 155)
- Fixed CCM module inline rate reference from "$144.00" to "~$131.65" for 99487 (line 180)

### Compliance and Regulatory
- Expanded HIPAA breach notification to cover all scenarios: individual notification within 60 days, HHS + media for 500+, annual report for <500 (line 406)
- Updated audit logging to specify Field Audit Trail, Shield retention limits, and external archive strategy (line 404)
- Expanded FDA SaMD analysis with all four 21st Century Cures Act criteria and January 2026 guidance update (line 415)

### Cost and Budget
- Updated Salesforce Phase 2 subtotal from "~$118,700" to "~$148,700" to reflect MuleSoft increase (line 329)
- Updated Phase 2 total cost from "$300K--$400K" to "$330K--$430K" (line 358)
- Updated 18-month total from "$950K--$1.25M" to "$980K--$1.28M" (line 360)
- ISV Partner Program benefit clarified: 2 free Sales Cloud (NOT Health Cloud) licenses; budget assumes full list price (line 319)
- Replaced "Silverline, Penrod" with "independent consultants, Trailblazer community referrals" as partner options (line 371)

### Partners and Next Steps
- Changed RPM vendor outreach from "Omron, Withings" to "Tenovi, Smart Meter" with API documentation request (line 518)
- Added EHR developer program access to Next Steps table (line 520)
- Fixed churn metric from "<5% monthly" (= ~46% annual) to "<10% annual" (line 443)

---

## Cross-Document Consistency Checks

| Item | Status |
|---|---|
| Virginia RHC count (106 + 27 FQHCs) | Consistent |
| Phase 1 timeline (Months 1--4) | Consistent |
| Phase 1 budget ($50K cash + $123K in-kind = $173K) | Consistent -- all line items match |
| Pilot clinic count (2--3) | Consistent |
| Revenue unlock ($195K--$267K/year) | Consistent |
| EHR targets (eCW, athenahealth, MEDITECH, Azalea) | Consistent |
| RPM device strategy (cellular-first: Tenovi, Smart Meter) | Consistent |
| Integration approach (SF Connect + Apex REST Phase 1; MuleSoft Phase 2) | Consistent |
| Risk model spec (XGBoost, AUC-ROC >0.75, SHAP) | Consistent |
| MIPS categories and weights (30/30/25/15) | Consistent |
| Encryption (AES-256 at rest, TLS 1.2+ in transit) | Consistent |
| Phase markers (UDS: P2, NLP coding: P2, Reg Change: P3, Denial: P3) | Consistent |
| CRM Analytics clarification (Reports/Dashboards P1, CRM Analytics P2) | Consistent |
| MuleSoft cost ($80K/year minimum) | Consistent |

---

## Items NOT Changed (Intentional)

- **"15+ distinct regulatory obligations" per RHC (Brief line 20):** Not independently sourced, but plausible and used as a framing number in a presentation prep document, not external submission. Acceptable with qualification.
- **"1 physician per 2,500+ patients" (Brief line 21):** Not sourced to specific Virginia counties. Acceptable as a presentation talking point with verbal qualification ("in some of the most underserved counties").
- **"chronic disease prevalence 30--40% above urban averages" (Brief line 21):** Directionally correct per CDC rural health data. Not independently verified to specific conditions for this polish pass.
- **Double-dash (--) for em dashes:** Maintained throughout as the Markdown convention. The PDF conversion script handles rendering.
- **"850K+ physicians" for eClinicalWorks (Guide line 82):** Commonly cited by eCW marketing. May include all healthcare professionals. Acceptable for internal use.
- **Technical Brief architecture diagram shows full vision without phase markers:** Intentional -- the diagram represents the end-state product vision. Phase-specific detail is provided in the tables below.

---

*Polish completed February 24, 2026. Documents ready for presentation prep.*
