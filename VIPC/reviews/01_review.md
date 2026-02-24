# REVIEW: VV Technical Implementation Brief (01_VV_Technical_Brief.md)

**Reviewer:** Senior Healthcare Technology Consultant
**Date:** February 24, 2026
**Review Against:** 02_Implementation_Guide.md (cross-consistency check)
**Presentation Date:** Wednesday, February 26, 2026

---

## 1. Overall Assessment

**Grade: B+**

This is a strong prep document with clear structure, well-articulated talking points, and a compelling narrative. The 3C framework is memorable, the audience-specific angles are smart, and the technical depth is appropriate for an investor-facing presentation. However, there are several inconsistencies with the Implementation Guide that could surface during Q&A, a few unsupported claims, and some missed opportunities to land harder with this specific panel. These are fixable before tomorrow. The issues below are ordered by severity.

---

## 2. Section-by-Section Review

### Section: Executive Summary (Lines 10-12)

**Strengths:**
- The 3C framing is crisp and memorable.
- Correctly positions VV as the technical backbone, not the whole product.
- The DoD connection is planted early.

**Issues:**
- Line 12: "demonstrated through active DoD AI/health contracts" -- this is asserted but never substantiated anywhere in the document. No contract names, no agencies, no performance data. If Will says this, Tai Mai or Michael Jarvis will ask "which contracts?" and Will needs a concrete answer.

**Fix required:** Either add a sidebar with 1-2 specific DoD contract references (even if redacted/generalized), or soften the language to avoid inviting a question Will cannot answer publicly.

---

### Section 1: The Problem (Lines 16-24)

**Strengths:**
- The "370+ Virginia / 5,500+ nationally" framing is effective for VIPC audience.
- The three crises are well-defined and the interconnection insight on line 24 is the strongest single sentence in the document.
- Specific, quantified pain points (15+ regulatory obligations, 60-80% revenue from Medicare/Medicaid, $50K-$150K leakage).

**Issues:**
- Line 20: "A single RHC may face 15+ distinct regulatory obligations" -- no source cited. This number is plausible but will be challenged by Tai Mai (physician background). Needs sourcing or qualification.
- Line 21: "1 physician per 2,500+ patients in some Virginia counties" -- which counties? A specific example here would be devastating for the narrative and would resonate with Jennifer O'Daniel (Virginia focus).
- Line 21: "chronic disease prevalence 30--40% above urban averages" -- for which conditions? This is a broad claim. The CDC and HRSA publish county-level data. A citation would make this bulletproof.
- Line 22: The $50K-$150K revenue leakage estimate is repeated throughout both documents but never sourced. The Implementation Guide (lines 201-209) provides a bottoms-up calculation showing $195K-$267K per clinic, which is actually HIGHER than $50K-$150K. This inconsistency is discussed further in Section 3 below.

---

### Section 2: Technical Architecture (Lines 28-78)

**Strengths:**
- The ASCII architecture diagram is clear and effective for a technical audience.
- The three-module layout with VV AI/ML engine underneath tells the right story.
- Including the Integration Layer shows infrastructure maturity.

**Issues:**
- Line 35: "Native EHR integration via HL7 FHIR R4 and MuleSoft connectors" -- **CRITICAL INCONSISTENCY.** The Implementation Guide explicitly states (line 71): "No MuleSoft in Phase 1. MuleSoft starts at ~$50K/year minimum -- that's our entire grant." The Technical Brief presents MuleSoft as a current capability. If Will says "we use MuleSoft" and then gets asked about Phase 1 costs, this falls apart. The brief must distinguish between the target architecture and the MVP architecture.
- Line 72: The architecture diagram shows "HL7 FHIR R4 / MuleSoft" in the integration layer. This needs an asterisk or verbal note that Phase 1 uses Salesforce Connect + Apex REST callouts, with MuleSoft in Phase 2.
- Lines 50-51: The diagram lists "AI Risk Stratification" and "Wearable/RPM Integration" without any visual distinction of what is Phase 1 vs. later. This is fine for the vision, but Will should be prepared to say "in our Phase 1 MVP, we focus on X and Y."

---

### Section 3: VV's Technical Role -- Module by Module (Lines 82-118)

#### 3.1 Compliance Module (Lines 84-98)

**Strengths:**
- The table format (Capability / How VV Builds It / Technology) is excellent for a technical presenter.
- The HADRIUS-specific talk-to on line 97 is the strongest panelist-targeted content in the document. It directly validates Michael Jarvis's investment thesis while differentiating.

**Issues:**
- Line 93: "MuleSoft integration to EHR" for HRSA UDS Report Generation -- again, MuleSoft is not in the Phase 1 build. The Implementation Guide (line 138) places UDS reporting in Phase 2 entirely. Will should not present UDS reporting as a Phase 1 capability.
- Line 95: "NLP-powered monitoring of Federal Register" for the Regulatory Change Engine -- the Implementation Guide (line 140) places this in Phase 3. If Will presents this as a current capability, it overstates what the grant funds.
- Line 97: "predicts where a clinic is going to fall out of compliance 60--90 days in advance" -- this is a strong claim. Is there any validation data for this? Even from the DoD work? If not, consider softening to "is designed to predict" or "will predict."

#### 3.2 Care Module (Lines 101-118)

**Strengths:**
- The RPM/wearable integration story is compelling and directly maps to CMS reimbursement.
- Both Michael Jarvis talk-to (line 115) and Tai Mai talk-to (line 117) are well-crafted. The Tai Mai angle about augmenting not replacing clinical judgment is essential for a physician audience.
- The $120-$180/month per RPM patient figure (line 115) gives Michael a revenue anchor.

**Issues:**
- Line 110: Lists "Apple Health, Google Health Connect, Withings, Omron, Dexcom, iHealth" as wearable ecosystems. The Implementation Guide (lines 100-111) identifies a completely different device strategy centered on cellular-connected devices (Smart Meter, Tenovi gateway) because rural patients often lack WiFi/smartphones. The brief's wearable list reads like a consumer health app, not a rural-appropriate clinical RPM program. This is a significant mismatch that Tai Mai (clinical background) would catch immediately.
- Line 115: "$120--$180/month in CMS reimbursement" -- The Implementation Guide (line 126) shows CPT 99454 at $52.11 and CPT 99457 at $51.77, totaling $103.88/month. To reach $120-$180, you need to assume additional 99458 billing (extra 20-min increments) or CCM stacking. The number is defensible but the brief should show the math or say "up to $180/month" with the components.
- Line 109: "gradient-boosted ensemble + logistic regression baseline" is appropriately technical. However, there is no mention of the interpretability approach (SHAP values) that the Implementation Guide details on line 173. For Tai Mai, the ability to explain why a patient was flagged is arguably more important than the algorithm itself.

#### 3.3 Collect Cash Module (Lines 121-133)

**Strengths:**
- The NLP coding optimization and denial prevention stories are compelling.
- The MIPS/APM dashboard ties back to real revenue impact.

**Issues:**
- Line 129: NLP coding optimization is presented as a current VV capability. The Implementation Guide (line 182) places this in Phase 2. This is a pattern -- the brief presents the full vision as current, which is dangerous in a Q&A setting.
- Line 131: "Salesforce integration with clearinghouses (Availity, Change Healthcare) via MuleSoft" -- MuleSoft is Phase 2, and the Implementation Guide (line 376) identifies Office Ally as the Phase 2 clearinghouse first target, not Availity/Change Healthcare (which are Phase 3). Another inconsistency that could surface under questioning.
- Line 130: The RPM/CCM billing capture description mentions "16-day minimum for 99457/99458" -- this is incorrect. The 16-day requirement applies to CPT 99454 (device supply/data transmission), not 99457/99458 (which are time-based at 20-minute thresholds). The Implementation Guide (line 126) has this correct. This is a factual error that would undermine credibility with anyone who knows CMS billing codes.

---

### Section 4: Technical Differentiators (Lines 136-165)

**Strengths:**
- The DoD-to-rural-health translation table (lines 142-150) is genuinely compelling and unique. This is the single strongest differentiation story.
- The "flywheel" concept (lines 161-165) is well-articulated.
- The systems approach vs. point solutions framing is clear and defensible.

**Issues:**
- Line 145: "Offline-capable modules for clinics with unreliable broadband" -- is this actually built? The Implementation Guide does not mention offline capability anywhere. This is a feature claim with no backing in the build plan. Either remove it or add it to the Implementation Guide as a future capability.
- Line 155: Listing HADRIUS as a competitor may be awkward given that Michael Jarvis is an investor in HADRIUS. Will should frame this as "complementary players" or "adjacent solutions" rather than "competitors." The talk-to on line 97 already does this well ("a segment HADRIUS and others don't specifically serve"), but the competitor list on line 155 contradicts that tone.

---

### Section 5: Market Opportunity (Lines 169-179)

**Strengths:**
- The Virginia/National TAM table is clean and credible.
- Virginia-first alignment with VIPC mission is well-stated.

**Issues:**
- Line 174: "$2,000--$4,000/month" SaaS pricing. The Implementation Guide (lines 469-473) shows a tiered model with a Starter tier at $500/month. Omitting the Starter tier here is probably intentional (higher TAM), but if asked about entry pricing, Will should know the $500 Starter exists.
- Line 175: Virginia TAM of $8.9M-$17.8M assumes 100% penetration of 370+ clinics. No realistic market capture rate is given. A 10-20% capture rate ($0.9M-$3.6M) would be more credible for a 3-5 year projection. Sophisticated investors (Tai Mai) will do this math instantly.
- Line 177: RPM Revenue Unlock of $50K-$150K per clinic is contradicted by the Implementation Guide's own calculation of $195K-$267K (lines 201-209). Pick one number and be consistent. The Implementation Guide number is better sourced (bottoms-up CPT code calculation), so either use it or explain the discrepancy.

---

### Section 6: Implementation Roadmap (Lines 183-198)

**Issues -- MAJOR INCONSISTENCY WITH IMPLEMENTATION GUIDE:**

| Aspect | Technical Brief (Sec 6) | Implementation Guide (Sec 4) | Discrepancy |
|---|---|---|---|
| **Phase 1 duration** | Months 1-3 | Months 1-4 | Brief is 1 month shorter |
| **Phase 1 scope** | "HIPAA compliance module live; EHR integration with 2 pilot clinic EHR systems" | "EHR FHIR integration with pilot clinic EHR (athenahealth or eCW -- read-only)" -- 1 EHR, not 2 | Brief overpromises |
| **Phase structure** | 5 phases | 3 phases | Brief has 5 granular phases; Guide has 3 broader phases. The naming and boundaries don't align |
| **Pilot clinics live** | Phase 4, Months 6-10 (5-10 clinics) | Phase 1, Month 4 (2-3 clinics) | Brief delays pilot significantly vs. Guide |
| **When pilot clinics go live** | Months 6-10 | Month 4 | 2-6 month gap in timelines |
| **Number of pilot clinics** | 5-10 (line 190) | 2-3 (line 217) | Brief says 5-10, Guide says 2-3 |

This is the single most dangerous set of inconsistencies in the document. If the presentation says "5-10 pilot clinics by month 10" but the detailed plan says "2-3 by month 4," it signals either that the team hasn't coordinated or that the brief is aspirational fiction. Will should present the Implementation Guide's more conservative and credible timeline.

**Grant budget allocation (lines 193-198) vs. Implementation Guide (lines 258-269):**

| Line Item | Brief | Guide |
|---|---|---|
| Salesforce licenses | $15K | $6,500 (licenses) + $1,950 (Shield) = $8,450 |
| AI model development | $20K | $1,500 (compute) + sweat equity |
| Pilot onboarding | $10K | $3,000 (travel/training) + $1,500 (RPM devices) |
| Compliance content | $5K | Not separately itemized |
| Contract SF developer | Not listed | $30,000 |
| Legal | Not listed | $2,000 |
| Misc | Not listed | $1,550 |

The two documents tell completely different stories about how the $50K is spent. The Implementation Guide's breakdown is far more detailed and credible (it actually adds up to $50K). The brief's breakdown appears to be an earlier draft that was never updated. This MUST be reconciled before the presentation. Jennifer O'Daniel (VVP Lead) will care deeply about grant fund allocation.

---

### Section 7: Presentation Talking Points (Lines 201-217)

**Strengths:**
- Well-structured Q&A format. These are the right questions to prepare for.
- The answers are technically sound and appropriately detailed.
- The "Why Salesforce" answer (line 216) is particularly strong.

**Issues:**
- Line 207: "TLS 1.3" -- the Implementation Guide (line 400) specifies "TLS 1.2+" and Salesforce enforces TLS 1.2 minimum. Stating TLS 1.3 specifically could be challenged. Change to "TLS 1.2+" for accuracy.
- Line 210: "We use MuleSoft (Salesforce's integration platform)" -- again, not in Phase 1. This talking point will trigger a cost question Will cannot answer favorably. Rephrase to say "Salesforce's integration tools" or "we leverage Salesforce's native integration capabilities in Phase 1 and MuleSoft at scale."
- Line 210: Lists "Epic, Cerner" as EHR targets. The Implementation Guide (lines 80-87) does not list Epic or Cerner at all -- the RHC market runs eClinicalWorks, athenahealth, MEDITECH, Azalea, and TruBridge. Epic and Cerner are hospital/large health system EHRs, not RHC EHRs. Mentioning them to this panel (who understand healthcare deeply) signals unfamiliarity with the target market. Replace with the actual target EHRs.

---

### Section 8: Know Your Audience (Lines 220-233)

**Strengths:**
- Identifying each panelist's investment portfolio and interests is smart preparation.
- The Michael Jarvis "intersection of your two investment themes" angle is excellent.
- The Tai Mai clinical framing is appropriate for a physician/scientist.

**Issues:**
- Line 224: The Jennifer O'Daniel talk-to mentions "creates technical jobs in Virginia" but gives no specifics. How many jobs? What kinds? The Implementation Guide (Section 5) lists specific roles (Salesforce Developer, ML Engineer, Implementation Specialist, Customer Success). Will should cite "4-6 technical roles in Virginia by Month 10" or similar.
- Line 230-232: The Tai Mai section doesn't mention FDA/SaMD considerations at all. Tai Mai, as a physician/scientist VC, may ask about regulatory classification of the AI. The Implementation Guide addresses this (line 413). Will should be prepared with the 21st Century Cures Act clinical decision support exemption argument.
- Missing entirely: No preparation for potential TOUGH questions. What if Tai Mai asks "what clinical validation have you done?" What if Michael asks "why wouldn't HADRIUS just add this?" What if Jennifer asks "what happens if the pilot fails?" Add a "Hard Questions" section.

---

## 3. Cross-Document Consistency

Summary of all inconsistencies found (consolidated from above, prioritized by risk of surfacing during Q&A):

| # | Topic | Brief Says | Guide Says | Severity |
|---|---|---|---|---|
| 1 | **MuleSoft in Phase 1** | Used throughout as current integration tool (lines 35, 72, 93, 131, 210) | Explicitly excluded from Phase 1 (line 71). $50K/yr cost = entire grant | CRITICAL |
| 2 | **Grant budget allocation** | $15K SF, $20K AI, $10K pilot, $5K compliance (lines 194-197) | $8,450 SF, $30K contract dev, $3K pilot, $2K legal, etc. (lines 260-269) | CRITICAL |
| 3 | **Phase 1 timeline** | Months 1-3 (line 187) | Months 1-4 (line 215) | HIGH |
| 4 | **Pilot clinic count** | 5-10 clinics, Months 6-10 (line 190) | 2-3 clinics, Month 4 (line 217) | HIGH |
| 5 | **Revenue unlock per clinic** | $50K-$150K/year (lines 22, 163, 177) | $195K-$267K/year (line 209) | HIGH |
| 6 | **Wearable device strategy** | Consumer ecosystems: Apple Health, Google Health Connect, Withings, Omron, Dexcom, iHealth (line 110) | Clinical/cellular: Smart Meter, Tenovi gateway, cellular-connected devices mandatory for rural (lines 100-111) | HIGH |
| 7 | **Target EHRs** | Epic, Cerner, eClinicalWorks, athenahealth (lines 147, 210) | eClinicalWorks, athenahealth, MEDITECH, Azalea, TruBridge (lines 80-87). No Epic/Cerner | MEDIUM |
| 8 | **NLP coding optimization phase** | Presented as current (line 129) | Phase 2 (line 182) | MEDIUM |
| 9 | **UDS reporting phase** | Presented as current (line 93) | Phase 2 (line 138) | MEDIUM |
| 10 | **Regulatory Change Engine phase** | Presented as current (line 95) | Phase 3 (line 140) | MEDIUM |
| 11 | **Clearinghouse partners** | Availity, Change Healthcare (line 131) | Office Ally first, Availity secondary, Trizetto Phase 3 (line 376) | LOW |
| 12 | **TLS version** | TLS 1.3 (line 207) | TLS 1.2+ (line 400) | LOW |
| 13 | **Offline capability** | Claimed (line 145) | Not mentioned anywhere in build plan | LOW |
| 14 | **RPM billing code error** | "16-day minimum for 99457/99458" (line 130) | 16-day for 99454; 99457/99458 are time-based (line 126) | MEDIUM |

---

## 4. Audience Alignment

### Jennifer O'Daniel (VVP Lead)

**Current alignment: GOOD, but thin on specifics.**

She cares about: grant ROI, Virginia economic impact, job creation, scalable model.

- The Virginia-first narrative is solid.
- The grant-to-Series-A pipeline is mentioned but not quantified. Add: "Phase 1 pilot data targets 2-3 clinics generating measurable outcomes by Month 4, positioning ACT for a seed/Series A raise of $X by Month 10."
- Job creation is mentioned vaguely. Add specific numbers: "Phase 2 creates 4-6 Virginia-based technical roles."
- Missing: No mention of how ACT's success contributes to Virginia's healthcare innovation ecosystem more broadly. Jennifer represents VIPC -- she needs to justify this grant to her board. Give her the ammunition.

### Michael Jarvis (HADRIUS + OHM investor)

**Current alignment: STRONG -- best-targeted panelist in the document.**

- The HADRIUS compliance angle is well-played (line 97). Not competitive, complementary market segment.
- The OHM/wearables angle (line 115) connects his investment thesis to the revenue model.
- The "intersection of your two investment themes" line (line 228) is the best single line in the audience section.
- Risk: Listing HADRIUS as a "competitor" in Section 4.2 (line 155) undercuts the relationship-building in the talk-to sections. Remove HADRIUS from the competitor list or relabel the section "Adjacent Solutions."

### Tai Mai (MEDA Ventures -- Physician/Scientist)

**Current alignment: ADEQUATE, but needs clinical depth.**

- The "augmenting not replacing clinical judgment" framing (line 117) is correct and essential.
- Missing: No discussion of clinical validation methodology. Tai Mai will want to know how you prove the AI works. Mention the AUC-ROC >0.75 target, SHAP interpretability, and the plan for outcomes measurement during the pilot (the Implementation Guide has this on lines 420-432).
- Missing: No mention of FDA/SaMD considerations. As a physician/scientist VC, regulatory risk is on Tai Mai's radar. The 21st Century Cures Act exemption argument (Implementation Guide line 413) should be in Will's back pocket.
- Missing: No discussion of health equity / disparities angle. MEDA Ventures is a physician-led VC. The narrative that rural populations are underserved and this platform addresses structural health inequity is powerful. The data is already in the brief (line 21) but not framed as a health equity argument.
- Risk: The wearable device list (line 110) naming consumer products (Apple Health, Google Health Connect) rather than clinically appropriate rural devices (cellular-connected monitors) will read as naive to a physician who understands rural patient populations.

---

## 5. Technical Accuracy

### Claims That Are Unsupported or Overstated

| # | Claim | Location | Issue |
|---|---|---|---|
| 1 | "active DoD AI/health contracts" | Line 12 | No specific contracts cited. If challenged, Will has no backup. |
| 2 | "predicts where a clinic is going to fall out of compliance 60--90 days in advance" | Line 97 | No validation data. Model has not been built yet per the Implementation Guide. This is a design goal, not a demonstrated capability. |
| 3 | "370+ Rural Health Clinics" in Virginia | Line 18 | Plausible based on CMS data but should cite source (CMS Provider of Services file or Virginia DMAS). |
| 4 | "15+ distinct regulatory obligations" per RHC | Line 20 | Not sourced. |
| 5 | "1 physician per 2,500+ patients" | Line 21 | Not sourced. Which counties? |
| 6 | "chronic disease prevalence 30--40% above urban averages" | Line 21 | Not sourced. Which conditions? |
| 7 | "$50K--$150K per clinic per year" revenue leakage | Line 22 | Not sourced, and contradicted by the Guide's own math ($195K-$267K). |
| 8 | "$120--$180/month in CMS reimbursement" per RPM patient | Line 115 | Guide shows $103.88/month for 99454+99457. $180 requires additional 99458 billing. Needs qualification. |
| 9 | Offline-capable modules | Line 145 | Not in the build plan anywhere. |
| 10 | "16-day minimum for 99457/99458" | Line 130 | Factually incorrect. 16-day rule is for CPT 99454. CPT 99457/99458 are time-based (20-minute thresholds). |

---

## 6. Missing Content

### High Priority (add before presentation)

1. **Hard Questions prep section.** The Q&A section covers friendly questions. Add preparation for adversarial questions:
   - "What clinical validation have you completed?" (Answer: Phase 1 pilot IS the validation; model trained on CMS public data; AUC-ROC target; outcomes tracked per Implementation Guide Section 9.)
   - "Why wouldn't an existing player (HADRIUS, athenahealth, Waystar) just build this?" (Answer: Different market segment; integration across compliance+care+revenue requires a systems approach no incumbent has incentive to build.)
   - "What happens if the pilot fails or clinics don't adopt?" (Answer: Fallback plan per risk register; clinic involvement from Sprint 1; revenue impact demonstrated early.)
   - "What's your FDA regulatory risk?" (Answer: Clinical decision support exemption under 21st Century Cures Act; human-in-the-loop design.)

2. **Phase 1 MVP scope distinction.** The brief presents the full vision without clearly delineating what the $50K grant actually builds. Add a brief "What the grant builds" subsection or callout box that mirrors the Implementation Guide's Phase 1 scope (lines 34-74).

3. **Specific DoD contract references or, alternatively, removal of unsubstantiated DoD claims.** The DoD angle is a differentiator only if it can be substantiated.

4. **Corrected grant budget allocation** matching the Implementation Guide's itemized breakdown.

### Medium Priority (add if time permits)

5. **Health equity framing** for Tai Mai -- rural health disparities as a structural inequity that technology can address.
6. **Rural Health Transformation (RHT) Program** funding tailwind (Implementation Guide line 477). This is a powerful point: clinics can potentially fund their 3C subscription through federal grants. Jennifer O'Daniel would find this compelling (it means the market can actually pay).
7. **Competitive moat discussion from Implementation Guide Section 10.3** -- the brief's competitor section is weaker than the Guide's.
8. **Success metrics** from Implementation Guide Section 9 -- gives the panel something concrete to evaluate the pilot against.

### Low Priority

9. **Team slide / team credibility.** No mention of who is actually building this beyond "VV." The Implementation Guide has a team section (Section 5). Investors fund teams, not just products.
10. **IP / defensibility discussion.** What is proprietary? The AI models? The Salesforce configuration? The clinical workflow design?

---

## 7. Specific Recommended Changes

Each change below specifies the exact old text and new text for the brief. Line numbers reference `/home/user/AC/VIPC/01_VV_Technical_Brief.md`.

### Change 1: Soften DoD claim (Line 12)

**Old text:**
```
This brief equips Will to speak authoritatively on how VV's proven technical capabilities -- demonstrated through active DoD AI/health contracts -- translate directly to solving rural healthcare's hardest problems.
```

**New text:**
```
This brief equips Will to speak authoritatively on how VV's technical capabilities -- informed by DoD AI/health program experience including edge computing, DDIL architectures, and HIPAA-equivalent protections -- translate directly to solving rural healthcare's hardest problems.
```

### Change 2: Fix MuleSoft references in platform foundation (Line 35)

**Old text:**
```
- Native EHR integration via HL7 FHIR R4 and MuleSoft connectors
```

**New text:**
```
- Native EHR integration via HL7 FHIR R4 (Phase 1: Salesforce Connect + Apex REST; Phase 2+: MuleSoft connectors)
```

### Change 3: Fix MuleSoft in architecture diagram (Line 72)

**Old text:**
```
|         | - HL7 FHIR R4 / MuleSoft               |               |
```

**New text:**
```
|         | - HL7 FHIR R4 / SF Connect (MuleSoft P2)|               |
```

### Change 4: Fix MuleSoft in HRSA UDS row (Line 93)

**Old text:**
```
| **HRSA UDS Report Generation** | Automated data extraction from EHR, patient demographics, and clinical quality measures. Pre-populated UDS tables with validation checks before submission | MuleSoft integration to EHR + Salesforce Reports + VV data transformation engine |
```

**New text:**
```
| **HRSA UDS Report Generation** *(Phase 2)* | Automated data extraction from EHR, patient demographics, and clinical quality measures. Pre-populated UDS tables with validation checks before submission | EHR integration (Salesforce Connect/FHIR) + Salesforce Reports + VV data transformation engine |
```

### Change 5: Add phase marker to Regulatory Change Engine (Line 95)

**Old text:**
```
| **Regulatory Change Engine** | NLP-powered monitoring of Federal Register, CMS/HRSA policy updates, and state regulatory changes. Automated impact assessment and policy update workflows | VV NLP pipeline (fine-tuned language models) + Salesforce Flow for workflow triggers |
```

**New text:**
```
| **Regulatory Change Engine** *(Phase 3)* | NLP-powered monitoring of Federal Register, CMS/HRSA policy updates, and state regulatory changes. Automated impact assessment and policy update workflows | VV NLP pipeline (fine-tuned language models) + Salesforce Flow for workflow triggers |
```

### Change 6: Soften predictive compliance claim (Line 97)

**Old text:**
```
Our AI engine doesn't just track compliance status; it predicts where a clinic is going to fall out of compliance 60--90 days in advance based on trending data, staffing changes, and regulatory calendar analysis.
```

**New text:**
```
Our AI engine doesn't just track compliance status; it's designed to predict where a clinic is at risk of falling out of compliance 60--90 days in advance based on trending data, staffing changes, and regulatory calendar analysis -- that's the capability we're building in Phase 1 and validating in the pilot.
```

### Change 7: Fix wearable device ecosystems for rural context (Line 110)

**Old text:**
```
| **Wearable/RPM Integration** | Ingest continuous data streams from consumer and clinical-grade wearables (blood pressure cuffs, glucose monitors, pulse oximeters, weight scales, smartwatches). Transform into structured FHIR Observations for clinical use | VV device integration layer: BLE/API connectors for major device ecosystems (Apple Health, Google Health Connect, Withings, Omron, Dexcom, iHealth); FHIR R4 Observation resources stored in Salesforce Health Cloud |
```

**New text:**
```
| **Wearable/RPM Integration** | Ingest continuous data streams from clinical-grade RPM devices (blood pressure cuffs, glucose monitors, pulse oximeters, weight scales). Cellular-connected devices prioritized for rural patients without reliable WiFi. Transform into structured FHIR Observations for clinical use | VV device integration layer via RPM aggregator API (Tenovi or Smart Meter -- cellular-connected, zero patient tech setup); FHIR R4 Observation resources stored in Salesforce Health Cloud |
```

### Change 8: Add SHAP interpretability to Tai Mai talk-to (Line 117)

**Old text:**
```
"Tai, from a clinical perspective, our AI risk stratification is built on validated clinical frameworks -- we're not replacing clinical judgment, we're augmenting it. The models are trained on CMS public use files and clinical datasets, producing risk scores that map to established clinical intervention pathways. The provider always retains decision authority. The AI surfaces the patients who need attention most, which is transformative when you have one provider managing thousands of patients in a rural county with no specialists within 60 miles."
```

**New text:**
```
"Tai, from a clinical perspective, our AI risk stratification is built on validated clinical frameworks -- we're not replacing clinical judgment, we're augmenting it. The models are trained on CMS public use files and clinical datasets, producing risk scores that map to established clinical intervention pathways. Critically, every risk score comes with the top contributing factors explained using SHAP values -- so the provider doesn't just see 'high risk,' they see 'high risk driven by rising A1C, missed cardiology referral, and 3 ER visits in 6 months.' The provider always retains decision authority. The AI surfaces the patients who need attention most, which is transformative when you have one provider managing thousands of patients in a rural county with no specialists within 60 miles. Our Phase 1 performance target is AUC-ROC above 0.75 with sensitivity above 80% for the highest-risk decile -- and we'll measure actual outcomes against predictions during the pilot."
```

### Change 9: Fix RPM revenue figure or qualify it (Line 115)

**Old text:**
```
every RPM patient generates $120--$180/month in CMS reimbursement that these clinics are currently leaving on the table.
```

**New text:**
```
every RPM patient generates $100--$180/month in CMS reimbursement (CPT 99454 device monitoring at $52 plus 99457 clinician time at $52, with additional billing for extended management) that these clinics are currently leaving on the table.
```

### Change 10: Fix RPM billing code error (Line 130)

**Old text:**
```
| **RPM/CCM Billing Capture** | Automated tracking of RPM device data transmission days (16-day minimum for 99457/99458), CCM time tracking (20-minute minimum for 99490), and TCM follow-up windows. Auto-generates billable encounter records | VV time/event tracking engine integrated with Salesforce Health Cloud; automated claims preparation for clearinghouse submission |
```

**New text:**
```
| **RPM/CCM Billing Capture** | Automated tracking of RPM device data transmission days (16-day minimum for 99454), clinician interactive time (20-minute minimum for 99457/99458), CCM time tracking (20-minute minimum for 99490), and TCM follow-up windows. Auto-generates billable encounter records | VV time/event tracking engine integrated with Salesforce Health Cloud; automated claims preparation for clearinghouse submission |
```

### Change 11: Fix MuleSoft in denial prevention (Line 131)

**Old text:**
```
| **Denial Prevention** | Pre-submission claims scrubbing against payer rules, prior authorization tracking, and documentation completeness verification. ML model trained on historical denial patterns to flag high-risk claims | VV predictive model + rules engine; Salesforce integration with clearinghouses (Availity, Change Healthcare) via MuleSoft |
```

**New text:**
```
| **Denial Prevention** *(Phase 3)* | Pre-submission claims scrubbing against payer rules, prior authorization tracking, and documentation completeness verification. ML model trained on historical denial patterns to flag high-risk claims | VV predictive model + rules engine; Salesforce integration with clearinghouses (Office Ally Phase 2; Availity/Change Healthcare Phase 3) |
```

### Change 12: Remove or relabel HADRIUS as competitor (Line 155)

**Old text:**
```
- Compliance tools (HADRIUS, Compliancy Group, HIPAA One) -- compliance only
```

**New text:**
```
- Compliance tools (Compliancy Group, HIPAA One, Intraprise Health) -- compliance only, not RHC-specific
```

### Change 13: Remove offline capability claim or qualify it (Line 145)

**Old text:**
```
| DDIL-native architecture (works without connectivity) | Offline-capable modules for clinics with unreliable broadband |
```

**New text:**
```
| DDIL-native architecture (works without connectivity) | Resilient architecture designed for clinics with unreliable broadband (cellular-connected devices, asynchronous data sync) |
```

### Change 14: Fix EHR list in Q&A talking point (Line 210)

**Old text:**
```
"HL7 FHIR R4 is our integration standard -- it's the same standard CMS mandated for interoperability. We use MuleSoft (Salesforce's integration platform) to connect to whichever EHR the clinic runs -- Epic, Cerner, eClinicalWorks, athenahealth, or any FHIR-enabled system. For wearables, we connect via device manufacturer APIs and health data aggregators. The clinic doesn't rip and replace anything -- we layer on top of their existing systems."
```

**New text:**
```
"HL7 FHIR R4 is our integration standard -- it's the same standard CMS mandated for interoperability. We use Salesforce's native integration capabilities and FHIR APIs to connect to whichever EHR the clinic runs -- eClinicalWorks, athenahealth, MEDITECH, Azalea Health, or any FHIR-enabled system. These are the EHRs that actually dominate the rural clinic market. For wearables, we integrate through RPM device aggregators like Tenovi that support 40+ FDA-cleared devices over a single API. The clinic doesn't rip and replace anything -- we layer on top of their existing systems."
```

### Change 15: Fix TLS version (Line 207)

**Old text:**
```
We layer on encrypted PHI at rest (AES-256) and in transit (TLS 1.3),
```

**New text:**
```
We layer on encrypted PHI at rest (AES-256) and in transit (TLS 1.2+),
```

### Change 16: Fix implementation roadmap to match Implementation Guide (Lines 185-198)

**Old text:**
```
| Phase | Timeline | Deliverables |
|---|---|---|
| **Phase 1: Foundation** | Months 1--3 | Salesforce Health Cloud instance configured; HIPAA compliance module live; EHR integration (HL7 FHIR) with 2 pilot clinic EHR systems; core data model deployed |
| **Phase 2: Care Engine** | Months 3--6 | AI risk stratification models trained and deployed; wearable/RPM integration (3--5 device types); care gap detection live; telehealth integration |
| **Phase 3: Revenue** | Months 4--8 | RPM/CCM billing automation; coding optimization NLP; denial prevention engine; MIPS dashboard |
| **Phase 4: Pilot** | Months 6--10 | 5--10 Virginia RHCs live on full 3C Platform; measure outcomes (compliance scores, care gaps closed, revenue captured) |
| **Phase 5: Scale** | Months 10--18 | Virginia-wide rollout; national expansion playbook; Series A fundraising based on pilot data |

**$50K VIPC Grant Use:**
- Salesforce Health Cloud licenses and development environment: $15K
- VV AI model development and integration engineering: $20K
- Pilot clinic onboarding (2--3 clinics for proof-of-concept): $10K
- Compliance module regulatory content development: $5K
```

**New text:**
```
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
```

### Change 17: Fix EHR list in DoD comparison table (Line 147)

**Old text:**
```
| HL7 FHIR / EHR integration (MHS GENESIS) | HL7 FHIR / EHR integration (Epic, Cerner, eClinicalWorks, athenahealth) |
```

**New text:**
```
| HL7 FHIR / EHR integration (MHS GENESIS) | HL7 FHIR / EHR integration (eClinicalWorks, athenahealth, MEDITECH, Azalea Health) |
```

### Change 18: Add job creation specifics for Jennifer O'Daniel (Line 224)

**Old text:**
```
- **Hit:** "The $50K grant funds a proof-of-concept at 2--3 Virginia RHCs. The pilot data positions ACT for Series A and creates technical jobs in Virginia to support statewide rollout. This is a force multiplier -- every clinic we bring online improves health outcomes for thousands of rural Virginians."
```

**New text:**
```
- **Hit:** "The $50K grant funds a proof-of-concept at 2--3 Virginia RHCs over 4 months. The combined project value is $173,000 -- $50K from VIPC and $123K in team sweat equity. The pilot data positions ACT for a seed/Series A raise by Month 10, which funds 4--6 Virginia-based technical roles (Salesforce developer, ML engineer, implementation specialists). This is a force multiplier -- every clinic we bring online improves health outcomes for thousands of rural Virginians and creates the workforce to scale statewide."
```

### Change 19: Add NLP coding optimization phase marker (Line 129)

**Old text:**
```
| **Automated Coding Optimization** | NLP analysis of clinical documentation to identify under-coded encounters, missed HCC (Hierarchical Condition Category) codes, and documentation gaps that reduce reimbursement | VV NLP models fine-tuned on medical coding datasets; integrated as real-time suggestions during documentation workflow in Salesforce |
```

**New text:**
```
| **Automated Coding Optimization** *(Phase 2)* | NLP analysis of clinical documentation to identify under-coded encounters, missed HCC (Hierarchical Condition Category) codes, and documentation gaps that reduce reimbursement | VV NLP models (spaCy + MedCAT) fine-tuned on medical coding datasets; integrated as real-time suggestions during documentation workflow in Salesforce |
```

### Change 20: Add revenue unlock consistency note to market table (Line 177)

**Old text:**
```
| RPM Revenue Unlock per Clinic | $50K--$150K/year (new CMS revenue) | -- |
```

**New text:**
```
| RPM/CCM/MIPS Revenue Unlock per Clinic | $195K--$267K/year (new CMS revenue, conservative estimate based on 80 RPM + 120 CCM patients) | -- |
```

---

## Summary of Priority Actions Before Tomorrow

1. **IMMEDIATE (tonight):** Reconcile the grant budget allocation (Change 16). Jennifer O'Daniel will ask about this.
2. **IMMEDIATE (tonight):** Fix all MuleSoft references (Changes 2, 3, 4, 11, 14). This is the most pervasive inconsistency.
3. **IMMEDIATE (tonight):** Fix the RPM billing code error (Change 10). Factual errors destroy credibility.
4. **IMMEDIATE (tonight):** Fix the wearable device list (Change 7). Rural-inappropriate devices signal market unfamiliarity.
5. **IMMEDIATE (tonight):** Fix the EHR targets (Changes 14, 17). Epic/Cerner are not the RHC market.
6. **HIGH (tonight if time):** Add phase markers to capabilities not in Phase 1 (Changes 4, 5, 11, 19).
7. **HIGH (tonight if time):** Strengthen Tai Mai prep with SHAP/AUC details (Change 8) and FDA talking point.
8. **HIGH (tonight if time):** Add hard questions prep section.
9. **MEDIUM (morning prep):** Soften unsupported claims (Changes 1, 6, 13).
10. **MEDIUM (morning prep):** Remove HADRIUS from competitor list (Change 12).

---

*Review completed February 24, 2026. Good luck tomorrow.*
