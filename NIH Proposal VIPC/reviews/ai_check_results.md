# AI QUALITY CHECK -- NIH SBIR PROPOSAL SUITE

**Date:** February 25, 2026
**Reviewer:** Automated AI Quality Checker (Final Pass)
**Documents Reviewed:**

| Doc # | File | Role |
|---|---|---|
| D1 | `01_NIH_SBIR_Proposal.md` | Primary NIH SBIR Phase I Proposal |
| D2 | `02_NIH_Implementation_Plan.md` | Internal Implementation/Execution Plan |
| D3 | `03_NIH_Technical_Guide.md` | Technical Reference Guide |
| S1 | `VIPC/01_VV_Technical_Brief.md` | Source VIPC Technical Brief (cross-reference) |
| S2 | `VIPC/02_Implementation_Guide.md` | Source VIPC Implementation Guide (cross-reference) |

---

## SUMMARY TABLE

| Category | Critical | Major | Minor | Info |
|---|---|---|---|---|
| 1. Placeholder Detection | 3 | 1 | 0 | 0 |
| 2. Cross-Document Consistency | 0 | 3 | 4 | 2 |
| 3. Accuracy / Contradictions | 1 | 3 | 2 | 0 |
| 4. Grammar & Spelling | 0 | 0 | 3 | 1 |
| 5. Formatting | 0 | 0 | 2 | 1 |
| 6. Tone | 0 | 0 | 1 | 2 |
| 7. Completeness | 2 | 2 | 1 | 0 |
| 8. NIH-Specific Compliance | 1 | 2 | 1 | 1 |
| **TOTALS** | **7** | **11** | **14** | **7** |

---

## 1. PLACEHOLDER DETECTION

### CRITICAL

| ID | Location | Placeholder Text | Issue |
|---|---|---|---|
| P-01 | D1, Line 339 | `*(To be obtained prior to submission)*` | **Letters of Support section is entirely placeholder.** All 5 letters (3 pilot clinics, Tenovi, Clinical Advisor) are listed as needing to be obtained. NIH reviewers may reject without these. |
| P-02 | D1, Lines 397-410 | `*(Standard NIH Biosketch format -- to be completed per NIH Biosketch guidelines)*` and `*(To be populated per applicant's credentials)*` and `*(To be populated with relevant publications, presentations, and project outcomes)*` | **Biographical Sketch is entirely placeholder.** Education/Training, and Contributions to Science are empty. This is a required NIH component. |
| P-03 | D2, Lines 375-377 | Co-Investigator: `TBD`, Data Engineer: `TBD`, Clinical Informatics Specialist: `TBD` | **Three of four core team members are unnamed (TBD).** While the Implementation Plan is marked "Internal," if any of this information feeds the proposal's Key Personnel section, reviewers will note the lack of identified team members. The Co-I is also TBD in D1 (line 282 references "A board-certified physician" without naming them). |

### MAJOR

| ID | Location | Placeholder Text | Issue |
|---|---|---|---|
| P-04 | D1, Lines 150-153 | Acceptance criteria use `- [ ]` checkbox notation | These are unchecked markdown checkboxes appearing in the Sprint 1 section of the Implementation Plan (D2). While not technically placeholders, the unchecked boxes throughout D2 (Sprints 1-18) could be misread as incomplete items if this document is shared. Not an issue for the primary proposal (D1), but notable for D2. |

---

## 2. CROSS-DOCUMENT CONSISTENCY

### Cross-Reference Matrix: Key Numerical Values

| Data Point | D1 (Proposal) | D2 (Impl. Plan) | D3 (Tech Guide) | S1 (VIPC Brief) | S2 (VIPC Impl.) | Status |
|---|---|---|---|---|---|---|
| Total budget | $256,000 | $256K (line 7) | Not stated | N/A ($50K VIPC) | N/A ($50K VIPC) | CONSISTENT |
| Project duration | 9 months | 9 months | Not stated | 4 months (VIPC) | 4 months (VIPC) | CONSISTENT (different projects) |
| Pilot clinics | 2-3 | 2-3 | Not stated | 2-3 | 2-3 | CONSISTENT |
| RPM patients | 50-100 | 50-100 | Not stated | 15-20/clinic | 15-20/clinic | CONSISTENT (different scope) |
| AUC-ROC target | >0.75 | >0.75 (with 0.70 interim) | >0.75 | >0.75 | >0.75 | CONSISTENT |
| Sensitivity target | >80% (top decile) | >80% (top decile) | >80% (top decile) | >80% (top decile) | >80% (top decile) | CONSISTENT |
| Revenue per clinic | $195K-$267K/yr | Not re-stated | Not re-stated | $195K-$267K/yr | $195K-$267K/yr | CONSISTENT |
| VA RHCs | 106 RHCs + 27 FQHCs | Not re-stated | Not re-stated | 106 RHCs + 27 FQHCs | Not re-stated | CONSISTENT |
| National RHCs | 5,500+ | Not re-stated | Not re-stated | 5,500+ | Not re-stated | CONSISTENT |
| GovCloud monthly cost | $750/month | $750/month | Not stated | $750/month | $750/month | CONSISTENT |
| Personnel costs | $195,000 | $195,000 | Not stated | Sweat equity | Sweat equity | CONSISTENT (different projects) |
| Tier pricing | $500-$4,000/mo | Not re-stated | Not re-stated | $500-$4,000/mo | $500-$4,000/mo | CONSISTENT |
| National TAM | $132M-$264M/yr | Not re-stated | Not re-stated | $132M-$264M/yr | Not re-stated | CONSISTENT |
| Sprints | Not stated | 18 (2-week) | Not stated | 8 (2-week) | 8 (2-week) | CONSISTENT (different scope) |
| RPM device units | 25 units | Not re-stated | Not stated | 15-20 | 15-20 | CONSISTENT (different scope) |
| RPM device cost | $3,750 (25 units) | $3,750 | Not stated | $2,500 | $2,500 | CONSISTENT (different scope) |
| MIPS weights | Not stated | Quality 30%, Cost 30%, PI 25%, IA 15% | Not stated | Not stated | Quality 30%, Cost 30%, PI 25%, IA 15% | CONSISTENT |

### MAJOR

| ID | Issue | Details |
|---|---|---|
| C-01 | **Budget math: Infrastructure cost discrepancy (D1 vs. D2)** | D1 Budget (line 266): AWS GovCloud = $6,750 (9 months x $750/month). D2 Monthly Budget Table (line 442): Infrastructure total = $7,000. Month 1 shows $1,250 instead of $750 for infrastructure. The $250 difference may reflect one-time setup costs, but this is not explained, and D1's line item says "$750/month" flat. If $7,000 is correct, D1 should say $7,000; if $6,750 is correct, D2 Month 1 should be $750. |
| C-02 | **Budget math: Total direct costs reconciliation (D2)** | D2 line 442 shows monthly totals summing to $226,750. D2 line 444 notes "Remaining ~$4,250 allocated to indirect costs and contingency. Total with indirect: $256,000." This means indirect costs = $256,000 - $226,750 = $29,250. But D1 line 275 says indirect costs = $25,000 (10.8%). $256,000 - $25,000 = $231,000 direct costs (matches D1 line 274). However, D2's $226,750 does not match D1's $231,000 direct costs. The $4,250 gap is unaccounted for -- it could be the difference between D1's infrastructure ($6,750) vs. D2's ($7,000) plus rounding, but this needs explicit reconciliation. |
| C-03 | **Travel budget discrepancy (D1 vs. D2)** | D1 Budget: Travel = $4,500 (clinic visits) + $3,000 (NIH travel) = $7,500 total. D2 Monthly Budget: Travel total = $6,500. Discrepancy of $1,000. |

### MINOR

| ID | Issue | Details |
|---|---|---|
| C-04 | **RPM device cost per unit** | D1 (line 290): "$100-$150 per unit at pilot pricing." D2 (line 33): "$150/unit avg." D1 calculates 25 units at $3,750, which is $150/unit exactly -- matching D2 but contradicting D1's own "$100-$150" range language. Consider saying "approximately $150 per unit" in D1 for consistency. |
| C-05 | **CPT 99453 (device setup) mentioned in D3 and S2 but absent from D1 and D2** | D3 (line 408-410) and S2 (line 214) describe CPT 99453 (initial device setup, $22.00) in the billing pipeline. D1's billing code list (lines 177-183) and D2's Sprint 5 billing logic (lines 202-208) do not mention 99453. It is a billable code relevant to the revenue pipeline. |
| C-06 | **Phase II budget: D1 vs. D2** | D1 (line 374): Phase II mentions "Months 10-18" expansion. D2 (lines 599-611): Phase II budget estimate = ~$800,000 over 18 months. NIH SBIR Phase II is typically $1M over 2 years. The $800K figure is within range but the 18-month duration is shorter than the standard 24 months. Not a contradiction but worth aligning with NIH norms. |
| C-07 | **Onboarding time target** | S1 (line 97): "clinic live in 2 weeks." S2 (line 500): "New clinic onboarding time: <2 weeks." D2 does not explicitly re-state onboarding time target for the NIH context, but Sprint 7 (clinic 1 onboarding) and Sprint 8 (go-live) span a full month (4 weeks). The VIPC target of 2 weeks may not apply during the research pilot phase where IRB and research consent add complexity, but worth noting. |

### INFO

| ID | Note |
|---|---|
| C-08 | D2 and D3 are marked "Internal -- Authentic Consortium" classification. This is appropriate since only D1 would be submitted to NIH. D2 and D3 serve as supporting internal reference documents. |
| C-09 | The VIPC documents (S1, S2) describe a $50K, 4-month MVP project. The NIH documents describe a $256K, 9-month research project. The underlying technology is identical but the scope, rigor, and objectives differ appropriately. No conflicting claims were found between the two project scopes. |

---

## 3. ACCURACY / CONTRADICTIONS

### CRITICAL

| ID | Issue | Details |
|---|---|---|
| A-01 | **Budget addition error in D1** | D1 Budget Summary (lines 253-276): Manually summing all line items: $90,000 + $15,000 + $54,000 + $36,000 + $0 + $4,500 + $3,000 + $6,750 + $3,750 + $2,500 + $1,500 + $5,000 + $5,000 + $2,000 + $2,000 = **$231,000**. This matches the stated "Subtotal Direct Costs: $231,000." Adding indirect costs of $25,000 = $256,000. **However**, the indirect cost rate is stated as "estimated 10.8%." 10.8% of $231,000 = $24,948, which rounds to $25,000. This is technically correct but borderline. The actual effective rate is 10.82%. Minor issue but NIH budget reviewers may scrutinize. Verify the negotiated indirect cost rate is exactly 10.8% or adjust. |

### MAJOR

| ID | Issue | Details |
|---|---|---|
| A-02 | **D2 monthly personnel allocation does not match D1 personnel budget** | D2 (line 442): Personnel total = $195,000 over 9 months ($21,667/month flat). D1 Personnel: PI ($90,000) + Co-I ($15,000) + Data Engineer ($54,000) + Clinical Informatics ($36,000) = $195,000. The math checks. However, the flat $21,667/month allocation in D2 implies all personnel are active every month at equal cost. In reality, the Co-I is 1.0 calendar month, the Data Engineer is 4.5 months, and the Clinical Informatics Specialist is 3.0 months. The personnel spend should be variable month-to-month, not flat. This flat allocation weakens the credibility of the monthly budget table in D2. |
| A-03 | **"Other Direct Costs" in D2 do not reconcile with D1** | D2 "Other" column totals $14,500. D1 "Other Direct Costs" items: GovCloud ($6,750) + RPM devices ($3,750) + ML compute ($2,500) + EHR access ($1,500) + Legal ($5,000) + Patent ($5,000) + Software tools ($2,000) + Participant support ($2,000) = $28,500. But D2 separates Infrastructure ($7,000) and Devices ($3,750) into their own columns, so D2 "Other" = $28,500 - $7,000 - $3,750 = $17,750 expected. Actual D2 "Other" = $14,500. Discrepancy of $3,250. |
| A-04 | **Participant support costs** | D1 (line 273): "Participant support (patient device training materials): $2,000." NIH treats participant support costs differently from other direct costs -- they are excluded from the indirect cost base and have special restrictions. The budget justification does not explicitly address this NIH-specific treatment. If these are truly participant support costs (direct payments/materials to research participants), they should be broken out per NIH SF424 requirements. |

### MINOR

| ID | Issue | Details |
|---|---|---|
| A-05 | **XGBoost hyperparameters stated as both default and optimized** | D3 (lines 110-117) lists specific XGBoost hyperparameters (500 trees, max_depth: 6, learning_rate: 0.05, etc.) as if they are final values. But D3 (lines 176-184) states Bayesian hyperparameter optimization via Optuna with 200 trials will search over these parameters. The listed values should be labeled as "initial defaults" or "starting configuration" rather than presented as the model architecture. |
| A-06 | **Pilot data temporal split** | D3 (line 169): "Pilot Data: Temporal split (train on months 1-6, validate on months 7-9)." But per the timeline, pilot clinics go live in Month 4 (Sprint 7-8), meaning only Months 4-9 have live data (6 months). A train-on-months-1-6 split would include months with no pilot data (Months 1-3). This likely refers to the CMS data training period plus pilot validation, but the language is ambiguous. |

---

## 4. GRAMMAR & SPELLING

### MINOR

| ID | Location | Issue |
|---|---|---|
| G-01 | D1, throughout | Use of en-dashes (`--`) is inconsistent with standard markdown. Some instances use `--` (double hyphen) while the intended rendering may be an em-dash. This is a stylistic choice but should be consistent. The documents consistently use `--` which is acceptable. |
| G-02 | D1, Line 114 | "99445 for 2--15 day monitoring, 99470 for shorter clinician interactions" -- These are described as "new 2026 CPT codes." If these are proposed/finalized CMS codes for 2026, verify the exact code numbers are confirmed in the CMS Final Rule. If they are placeholder designations, note this. |
| G-03 | D2, Line 487 | Section numbering error: Section 10 "SUCCESS METRICS" contains subsections numbered "9.1 Phase 1 KPIs" and "9.2 Series A Metrics" (should be 10.1 and 10.2). Then Section 10 appears again as "COMPETITIVE LANDSCAPE" (line 515). Two sections are numbered "10." |

### INFO

| ID | Note |
|---|---|
| G-04 | Overall prose quality is strong. Technical terminology is used correctly throughout. Acronyms are defined on first use in D1. The glossary in D3 (Section 10) is comprehensive. |

---

## 5. FORMATTING

### MINOR

| ID | Location | Issue |
|---|---|---|
| F-01 | D3, ASCII diagrams (lines 29-84, 97-131, etc.) | ASCII art diagrams are well-structured but may not render consistently across all markdown viewers. The box-drawing characters (+, -, |) are standard ASCII and should render in most environments. However, if these documents are converted to PDF for NIH submission, alignment may shift depending on the font. Recommend testing PDF rendering. |
| F-02 | D2, Sprint details (Sprints 13-16) | Sprints 13-16 (lines 326-350) are grouped together with less detail than Sprints 1-12. While this may be intentional (evaluation phase is more flexible), the format inconsistency is notable compared to the earlier sprint detail level. |

### INFO

| ID | Note |
|---|---|
| F-03 | All markdown tables appear well-formed with consistent column separators. No broken tables detected. Header hierarchy (H1, H2, H3) is consistent within each document. |

---

## 6. TONE

### MINOR

| ID | Location | Issue |
|---|---|---|
| T-01 | D1, Line 147 | "**This is not a prototype stack.**" -- While factually accurate and impactful, the bold emphasis and declarative tone is slightly more aggressive than typical NIH SBIR prose. Consider softening to: "This technology stack is proven in production environments." NIH reviewers expect confidence but in a measured, evidence-based register. |

### INFO

| ID | Note |
|---|---|
| T-02 | Overall tone is appropriate for an NIH SBIR submission. The writing balances technical rigor with accessibility. The Specific Aims section follows the standard NIH structure well (problem statement, gap, long-term goal, specific aims with hypotheses). |
| T-03 | D2 and D3 appropriately use a more internal/engineering tone since they are classified as "Internal -- Authentic Consortium" documents. The VIPC source documents (S1, S2) contain investor-facing "talk-to" sections and competitive positioning language that has been correctly excluded from the NIH proposal (D1). |

---

## 7. COMPLETENESS (NIH SBIR Phase I Requirements)

### CRITICAL

| ID | Requirement | Status | Details |
|---|---|---|---|
| CMP-01 | **Biosketches for all Senior/Key Personnel** | MISSING | D1 (lines 395-411): Only the PI biosketch is included and it is a placeholder. The Co-Investigator biosketch is entirely absent. NIH requires biosketches for ALL Senior/Key Personnel. The Data Engineer and Clinical Informatics Specialist may also need biosketches depending on their role classification. |
| CMP-02 | **Letters of Support** | MISSING | D1 (line 339): Explicitly marked "To be obtained prior to submission." All five letters are absent. While these can be obtained later, the proposal cannot be submitted without them. |

### MAJOR

| ID | Requirement | Status | Details |
|---|---|---|---|
| CMP-03 | **Human Subjects and Clinical Trials Information** | PARTIAL | D1 (lines 237-246) includes a brief Human Subjects section. However, NIH requires a detailed Human Subjects section addressing: (a) Risks to subjects, (b) Adequacy of protection against risks, (c) Potential benefits, (d) Importance of knowledge to be gained, (e) Inclusion of women, minorities, and children. The current section is abbreviated. Also, the Inclusion Enrollment Report (PHS Inclusion Enrollment Report) form is not referenced. |
| CMP-04 | **Data Management and Sharing Plan** | PARTIAL | D1 (lines 349-356) includes a Resource Sharing Plan. However, since January 2023, NIH requires a separate Data Management and Sharing Plan (DMS Plan) per the NIH Data Management and Sharing Policy. D2 Section 5 has a detailed data management plan, but this content needs to be in or referenced from D1. |

### MINOR

| ID | Requirement | Status | Details |
|---|---|---|---|
| CMP-05 | **Vertebrate Animals** | PRESENT (N/A) | Not applicable and not mentioned. Should include a brief "Not applicable" statement similar to the Authentication of Key Biological Resources section (D1, line 318). |

### NIH SBIR Required Sections Checklist

| Section | Present in D1? | Completeness |
|---|---|---|
| Specific Aims (1 page) | Yes | Complete |
| Research Strategy: Significance | Yes | Complete |
| Research Strategy: Innovation | Yes | Complete |
| Research Strategy: Approach | Yes | Complete |
| Timeline/Milestones | Yes | Complete |
| Potential Pitfalls and Mitigation | Yes | Complete |
| Human Subjects | Yes | Needs expansion |
| Budget and Justification | Yes | Complete (verify math) |
| Facilities and Other Resources | Yes | Complete |
| Equipment | Yes (None) | Complete |
| Biographical Sketch(es) | PLACEHOLDER | Critical gap |
| Letters of Support | PLACEHOLDER | Critical gap |
| Resource Sharing Plan | Yes | Complete |
| Authentication of Key Resources | Yes (N/A) | Complete |
| Consortium Arrangements | Yes | Complete |
| Commercialization Plan | Yes | Complete |
| Data Management and Sharing Plan | MISSING | Major gap |

---

## 8. NIH-SPECIFIC COMPLIANCE

### CRITICAL

| ID | Issue | Details |
|---|---|---|
| N-01 | **Page limit verification needed** | NIH SBIR Phase I Research Strategy is limited to **6 pages**. D1's Research Strategy section (Significance + Innovation + Approach, lines 51-245) is approximately 5,500 words. At standard NIH formatting (11pt Arial, 0.5" margins), this is estimated at 8-10 pages, which **likely exceeds the 6-page limit**. The Approach section alone (lines 129-245) is very detailed with multiple tables and could consume 4-5 pages. Specific Aims is limited to 1 page and the current content (lines 15-47) appears to be approximately 1 page. **Must format in NIH-compliant fonts/margins and verify page count.** |

### MAJOR

| ID | Issue | Details |
|---|---|---|
| N-02 | **Scoring criteria alignment** | NIH SBIR review uses 5 scored criteria: (1) Significance, (2) Investigator(s), (3) Innovation, (4) Approach, (5) Environment. The "Investigator(s)" criterion is weakened by the placeholder biosketch and unnamed Co-I/team. The "Environment" criterion is addressed by Facilities section but could be strengthened by specific institutional resources. |
| N-03 | **SBIR-specific requirements** | NIH SBIR requires: (a) Small business status documentation, (b) 67% minimum work performed by applicant organization (Phase I), (c) SBIR/STTR funding agreement certification, (d) Commercialization Plan. Items (a), (b), and (c) are not explicitly addressed in D1. The Consortium/Contractual Arrangements section notes VV as a subcontractor, which is fine, but the 67% rule should be explicitly confirmed. |

### MINOR

| ID | Issue | Details |
|---|---|---|
| N-04 | **NIH Institute targeting** | D1 (line 10): Lists both NIGMS and NIMHD as target institutes. The proposal should target one primary institute. While dual-assignment is possible, the applicant should verify whether both institutes accept SBIR applications with this focus area and identify which is primary. |

### INFO

| ID | Note |
|---|---|
| N-05 | The Study Section suggestion (BCHI -- Biomedical Computing and Health Informatics) is appropriate for this application's focus on AI/ML in healthcare informatics. |

---

## CROSS-DOCUMENT CONSISTENCY: TECHNOLOGY CLAIMS MATRIX

| Technology Claim | D1 | D2 | D3 | S1 | S2 | Consistent? |
|---|---|---|---|---|---|---|
| Stack: n8n + PostgreSQL + FastAPI + React + Docker on GovCloud | Yes | Yes | Yes | Yes | Yes | YES |
| PostgreSQL version: 16 | Yes | Yes | Yes (implied) | Yes | Yes | YES |
| Encryption: AES-256 at rest, TLS 1.2+ in transit | Yes | Yes | Yes | Yes | Yes | YES |
| EHR Integration: bonFHIR + n8n HTTP nodes | Yes | Yes | Yes | Yes | Yes | YES |
| Target EHRs Phase I: eClinicalWorks, athenahealth | Yes | Yes | Yes | Yes | Yes | YES |
| RPM Vendors: Tenovi + Smart Meter | Yes | Yes | Yes | Yes | Yes | YES |
| ML: XGBoost + SHAP + Logistic Regression baseline | Yes | Yes | Yes | Yes | Yes | YES |
| Hyperparameter tuning: Optuna (Bayesian) | Yes | Yes | Yes | N/A | N/A | YES |
| FedRAMP High (GovCloud) | Yes | Yes | Yes | Yes | Yes | YES |
| Row-level security (PostgreSQL) | Yes | Yes | Yes | Yes | Yes | YES |
| PGAudit for HIPAA audit trails | Yes | Yes | Yes | Yes | Yes | YES |
| 3 service tiers (Essentials/Professional/Enterprise) | Yes | N/A | N/A | Yes | Yes | YES |
| Gross margin: 93-95% at $2K/month | Yes | N/A | N/A | Yes | Yes | YES |
| Per-clinic infra cost: $100-$150/month at scale | Yes | N/A | N/A | Yes | Yes | YES |
| Patent: provisional in Phase I | Yes | Yes | N/A | Yes | Yes | YES |
| FDA CDS exemption (21st Century Cures Act, 4 criteria) | Yes | Yes | N/A | Yes | Yes | YES |
| January 2026 FDA CDS guidance update | Yes | Yes | N/A | Yes | Yes | YES |

---

## PRIORITY ACTION ITEMS

### MUST FIX (Before Submission)

| Priority | ID(s) | Action | Effort |
|---|---|---|---|
| 1 | P-02, CMP-01 | **Complete the PI Biographical Sketch** (Education/Training, Contributions to Science). **Obtain and include Co-Investigator biosketch.** Without these, the application will be returned without review. | HIGH |
| 2 | P-01, CMP-02 | **Obtain all Letters of Support** (minimum: 2 pilot clinics, Tenovi, Clinical Advisor). These are required for submission. Begin outreach immediately. | HIGH |
| 3 | N-01 | **Format the Research Strategy in NIH-compliant formatting (11pt Arial, 0.5" margins) and verify it fits within the 6-page limit.** The current content likely exceeds the limit. If so, condense the Approach section -- move detailed sprint-level information to D2 (internal reference) and keep D1 focused on the research methodology, not project management. | HIGH |
| 4 | CMP-04 | **Draft a Data Management and Sharing Plan** per NIH's 2023 DMS Policy. This is a separate required attachment. Content from D2 Section 5 can be adapted. | MEDIUM |
| 5 | A-01, C-01, C-02, C-03, A-03 | **Reconcile all budget figures across D1 and D2.** Specific issues: (a) Infrastructure: $6,750 vs. $7,000; (b) Travel: $7,500 vs. $6,500; (c) D2 monthly totals ($226,750) vs. D1 direct costs ($231,000); (d) D2 "Other" column ($14,500) vs. expected ($17,750). Create a single authoritative budget table and ensure both documents match exactly. | MEDIUM |
| 6 | P-03 | **Identify and name the Co-Investigator, Data Engineer, and Clinical Informatics Specialist.** Even if final hiring is pending, NIH reviewers evaluate the team. Name specific individuals or state "To Be Named" with explicit qualifications required. | MEDIUM |
| 7 | CMP-03 | **Expand the Human Subjects section** to address all five required elements per NIH guidelines (risks, protections, benefits, knowledge importance, inclusion). Include or reference a PHS Inclusion Enrollment Report. | MEDIUM |

### SHOULD FIX (Strengthens Application)

| Priority | ID(s) | Action | Effort |
|---|---|---|---|
| 8 | N-03 | **Add explicit SBIR eligibility statements:** Confirm small business status, 67% work-performance requirement, and reference the SBIR/STTR Funding Agreement Certification. | LOW |
| 9 | A-04 | **Clarify participant support costs** treatment in the budget. If the $2,000 is truly participant support (not consultant or subcontract), it must be excluded from the indirect cost base and noted accordingly. | LOW |
| 10 | N-04 | **Clarify primary NIH Institute.** Choose NIMHD or NIGMS as primary and note the other as secondary. Verify SBIR funding availability at each institute for this topic area. | LOW |
| 11 | C-05 | **Add CPT 99453** (initial device setup, $22/patient one-time) to D1's billing code list (Section C.3) and D2's Sprint 5 billing logic. This is a legitimate billable code in the RPM pipeline. | LOW |
| 12 | G-03 | **Fix section numbering in D2** -- Section 10 appears twice (Success Metrics and Competitive Landscape). Subsections under Success Metrics are numbered 9.1/9.2 instead of 10.1/10.2. | LOW |
| 13 | T-01 | **Soften declarative tone** in D1 line 147 ("This is not a prototype stack"). Rephrase to evidence-based language suitable for NIH review. | LOW |
| 14 | A-05 | **Clarify XGBoost hyperparameters in D3** -- Label listed values as "initial/default configuration subject to Bayesian optimization" rather than final model parameters. | LOW |
| 15 | N-02 | **Strengthen Investigator(s) criterion** by including specific relevant publications, prior project outcomes, or preliminary data in the biosketch. Even without peer-reviewed publications, relevant DoD project experience and technical capabilities should be documented. | MEDIUM |
| 16 | A-02 | **Revise D2 monthly budget table** to show variable personnel spend by month rather than flat $21,667/month. This better reflects the actual effort distribution and strengthens internal planning credibility. | LOW |

---

## OVERALL ASSESSMENT

**Submission Readiness: NOT YET READY -- 7 CRITICAL items require resolution**

The three NIH SBIR documents form a comprehensive and technically strong proposal suite. The core scientific and technical content -- the three research aims, the technology stack description, the market analysis, and the commercialization plan -- are well-developed, internally consistent, and appropriate for an NIH SBIR Phase I application.

**Key Strengths:**
- The Specific Aims section is well-structured with clear hypotheses and measurable success criteria
- Technology claims are consistent across all five documents reviewed
- The unified compliance-care-revenue concept is a genuine innovation well-articulated for NIH reviewers
- The VIPC-to-NIH translation is appropriate -- the NIH documents correctly emphasize research rigor, statistical methodology, and clinical validation rather than investor metrics
- The security narrative (GovCloud, FedRAMP High, defense heritage) is compelling and well-supported
- The Commercialization Plan is detailed and realistic

**Key Weaknesses:**
- The biographical sketch and letters of support are entirely placeholder -- these are submission blockers
- The Research Strategy likely exceeds the 6-page limit and needs condensation
- Budget figures have small but notable discrepancies across documents that need reconciliation
- The Human Subjects section needs expansion to meet NIH requirements
- A Data Management and Sharing Plan is required but missing
- Three of four core team members are unnamed

**Recommendation:** Address all "Must Fix" items before submission. The "Should Fix" items will strengthen the application but are not submission blockers. The technical and scientific foundation is strong; the gaps are primarily in NIH-specific administrative and procedural requirements.

---

*Generated by: AI Quality Checker (Final Pass Review)*
*Review Date: February 25, 2026*
*Documents Reviewed: 5 (3 NIH + 2 VIPC source)*
