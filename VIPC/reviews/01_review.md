# REVIEW: VV Technical Implementation Brief (01_VV_Technical_Brief.md)

**Reviewer:** Senior Healthcare Technology Consultant
**Date:** February 25, 2026
**Review Against:** 02_Implementation_Guide.md (cross-consistency check)
**Presentation Date:** Wednesday, February 26, 2026
**Document Version Reviewed:** Version 2.0 (February 24, 2026) -- post-Salesforce-to-n8n stack migration

---

## 1. Overall Assessment

**Grade: B+**

This is a markedly improved document from any Salesforce-based predecessor. The migration to n8n + PostgreSQL + Python/FastAPI + React on GovCloud is a stronger technical story for this audience -- it eliminates the licensing cost vulnerability, strengthens the open-source/no-vendor-lock-in narrative, and makes the 97% gross margin claim defensible. The 3C framework is memorable, the audience-specific talking points are well-crafted, and the Q&A prep now includes hard questions. The two documents (Brief and Implementation Guide) are largely consistent, which is a significant improvement.

However, there remain several numerical inconsistencies, a handful of unsupported claims that could embarrass the presenter under scrutiny, some internal math errors, and a few places where the Brief overstates what Phase 1 actually delivers. These are all fixable before tomorrow. Issues below are ordered by severity within each section.

---

## 2. Section-by-Section Review

### Executive Summary (Lines 10-13)

**Strengths:**
- The 3C framing is crisp and immediately understandable.
- "Same proven stack VV deploys for defense clients" is the right lead -- establishes credibility immediately.
- "No enterprise licensing, no per-seat fees, no vendor lock-in" is a strong differentiator that will resonate with all three panelists.

**Issues:**

1. **Line 12: "The platform ships as a turnkey system deployable to any RHC, then customizable per clinic's EHR, device mix, payer landscape, and workflows."** The word "ships" implies a finished product. This is a pre-MVP grant pitch. The Implementation Guide makes clear this is Months 1-4 build work. The word choice creates an expectation gap.

**OLD TEXT (Line 12):**
```
The platform ships as a turnkey system deployable to any RHC, then customizable per clinic's EHR, device mix, payer landscape, and workflows.
```

**NEW TEXT:**
```
The platform is designed as a turnkey system deployable to any RHC, then customizable per clinic's EHR, device mix, payer landscape, and workflows.
```

---

### Section 1: The Problem (Lines 16-24)

**Strengths:**
- The "106 RHCs + 27 FQHCs" Virginia framing is specific and verifiable (CMS Provider of Services file).
- The "3 Virginia RHCs closing in 2025" is topical and powerful.
- The interconnection insight on Line 24 is the single best sentence in the document.

**Issues:**

2. **Line 18: "106 Rural Health Clinics and 27 FQHCs (5,500+ RHCs nationally)"** -- These numbers are inconsistent with Section 5 (Line 189), which says "106 RHCs + 27 FQHCs" totaling 133, but then the Virginia TAM on Line 191 calculates based on 133 clinics at $2K-$4K/month and arrives at "$3.2M--$6.4M/year." Let us check: 133 clinics x $2,000/month x 12 = $3.19M and 133 x $4,000 x 12 = $6.38M. The math checks out. Good -- this is internally consistent.

3. **Line 20: "A single RHC may face 15+ distinct regulatory obligations"** -- No source cited. This number is plausible (HIPAA Privacy Rule, HIPAA Security Rule, HIPAA Breach Notification, OSHA, CLIA, CMS CoPs, Stark Law, Anti-Kickback, state licensure, CMS quality reporting/MIPS, FCC broadband, HRSA reporting for FQHCs, state Medicaid, 42 CFR Part 2, ADA). That actually gets to ~15, so the claim holds. But Tai Mai (physician background) may challenge it. Recommend adding "(HIPAA, CLIA, CMS CoPs, MIPS, FCC, OSHA, state licensure, and others)" in parentheses to make it concrete.

4. **Line 22: "$100K--$250K per clinic per year on the table in unrealized RPM, CCM, and quality bonus revenue"** -- The Implementation Guide (Lines 203-211) calculates $195K-$267K using a bottoms-up model (80 RPM patients + 120 CCM patients + MIPS penalty avoidance). The Brief says $100K-$250K. These ranges overlap but the low end of the Brief ($100K) is far below the Guide's low end ($195K), and the high end of the Brief ($250K) is below the Guide's high end ($267K). The discrepancy signals that one document used rough estimates while the other did real math. **Use the Implementation Guide's numbers -- they are sourced from CPT codes and are more defensible.**

**OLD TEXT (Line 22):**
```
RHCs leave an estimated $100K--$250K per clinic per year on the table in unrealized RPM, CCM, and quality bonus revenue
```

**NEW TEXT:**
```
RHCs leave an estimated $195K--$267K per clinic per year on the table in unrealized RPM, CCM, and quality bonus revenue (based on conservative RPM/CCM enrollment rates and MIPS penalty avoidance)
```

---

### Section 2: Technical Architecture (Lines 28-97)

**Strengths:**
- The stack description (Lines 33-41) is clean, specific, and matches the Implementation Guide exactly.
- The architecture diagram (Lines 47-83) correctly shows the three modules, AI/ML engine, and n8n workflow layer.
- The "Out of the Box, Then Customize" table (Lines 89-96) is excellent presentation material -- concrete, actionable, and demonstrates deployment maturity.
- bonFHIR is correctly described as a "community n8n node" -- this matches its actual status.

**Issues:**

5. **Line 34: "FedRAMP High authorized, HIPAA BAA, ITAR-compliant"** -- Amazon GovCloud is FedRAMP High authorized and does offer HIPAA BAAs. The ITAR claim is also correct. However, the platform itself is not FedRAMP High authorized just because it runs on GovCloud. The infrastructure is FedRAMP High; the application inherits some controls but is not itself FedRAMP authorized. This distinction matters for a healthcare-savvy audience. In Section 7 (Line 231), the Q&A answer correctly says "runs on Amazon GovCloud -- FedRAMP High authorized" -- the "runs on" framing is accurate. But in Section 4.2 (Line 169), the comparison table says "Compliance posture: FedRAMP High (GovCloud)" for the VV platform vs. "FedRAMP Moderate" for Salesforce. This is misleading -- neither the VV platform nor Salesforce Health Cloud are themselves FedRAMP authorized; it is their hosting infrastructure that carries the authorization. Recommend qualifying.

**OLD TEXT (Line 169):**
```
| **Compliance posture** | FedRAMP Moderate | **FedRAMP High** (GovCloud) |
```

**NEW TEXT:**
```
| **Compliance posture** | FedRAMP Moderate infrastructure | **FedRAMP High** infrastructure (GovCloud) |
```

6. **Line 41: "bonFHIR -- Community n8n node providing native FHIR R4 actions and triggers for EHR connectivity"** -- bonFHIR is a real project (Apache 2.0 license). However, as of early 2026, bonFHIR is primarily a React framework and TypeScript SDK for building FHIR applications. There is an n8n community node (`@bonfhir/n8n-nodes-bonfhir`), but its maturity should be verified. The Implementation Guide (Line 32, Line 79) correctly notes it is a "community node" and adds "direct FHIR R4 HTTP calls" as a fallback. The Brief should mirror this fallback language -- if bonFHIR's n8n node is immature, direct HTTP Request nodes in n8n are the real integration path.

**OLD TEXT (Line 41):**
```
- **bonFHIR** -- Community n8n node providing native FHIR R4 actions and triggers for EHR connectivity
```

**NEW TEXT:**
```
- **bonFHIR** -- Community n8n node providing native FHIR R4 actions and triggers for EHR connectivity, supplemented by n8n HTTP Request nodes for direct FHIR R4 API calls
```

7. **Line 43: "VV is currently building a classified gap analysis platform for a defense client on this exact architecture (n8n + PostgreSQL + NGINX + Docker on GovCloud), with a deployment path from unclassified through TS/SCI."** -- This is a strong credibility claim but potentially problematic. If the defense work is classified, Will cannot provide details under questioning. The claim is also hard to verify. The phrase "this exact architecture" is valuable but should be accurate -- is the defense platform really using n8n, or is that an adaptation for the healthcare version? If the defense platform uses a different workflow engine, this claim becomes misleading. Will should be prepared to answer "can you tell us more about that defense project?" honestly.

8. **Line 78: "n8n scheduled workflows aggregating RPM readings + clinician time from PostgreSQL"** -- This is a reasonable architecture. However, the Implementation Guide (Line 77-78) notes that n8n Community Edition handles ~23 req/s in single mode, with the platform needing ~1-5 req/s at peak for 2-3 clinics. This is fine for Phase 1 but the Brief never mentions this throughput ceiling. If a technically savvy panelist asks about scale, Will should know this number.

9. **Line 97: "Target: clinic live in 2 weeks after initial onboarding meeting."** -- The Implementation Guide's Phase 1 roadmap (Lines 270-276) shows Month 1 for foundation, Month 2 for EHR/RPM integration, Month 3 for billing, and Month 4 for pilot launch. That is 4 months of build before any clinic goes live. The "2 weeks" claim refers to post-build onboarding of additional clinics using the completed platform -- not the initial deployment. This distinction must be crystal clear in the presentation, or it sounds like the platform already exists.

---

### Section 3: VV's Technical Role (Lines 101-145)

#### 3.1 Compliance Module (Lines 103-114)

**Strengths:**
- Table format (Capability / How VV Builds It / Technology) is excellent.
- Phase markers are correctly applied to UDS (Phase 2) and Regulatory Change Engine (Phase 3).
- The Michael Jarvis HADRIUS talk-to (Line 114) is the strongest audience-targeted content in the document.

**Issues:**

10. **Line 114: "it's designed to predict where a clinic is at risk of falling out of compliance 60--90 days in advance"** -- Good that this has been softened to "designed to predict." However, no validation data exists for this claim. The Implementation Guide does not describe a compliance prediction model anywhere -- the compliance module is a task tracker with reminders (Lines 141-147), not a predictive system. The "60-90 days in advance" prediction would require historical compliance failure data that does not exist yet. This claim should be further softened or reframed as a Phase 2+ aspiration.

**OLD TEXT (Line 114):**
```
Our platform doesn't just track compliance status; it's designed to predict where a clinic is at risk of falling out of compliance 60--90 days in advance based on trending data, staffing changes, and regulatory calendar analysis.
```

**NEW TEXT:**
```
Our platform doesn't just track compliance status; it monitors trending data, staffing changes, and regulatory calendars to flag compliance risks before they become violations. As we accumulate clinic data during the pilot, we'll build the predictive models that can forecast risk 60--90 days in advance.
```

#### 3.2 Care Module (Lines 118-131)

**Strengths:**
- The RPM integration story maps directly to CMS reimbursement -- the revenue justification is built into the care narrative.
- Both the Michael Jarvis talk-to (Line 129) and Tai Mai talk-to (Lines 131) are well-crafted.
- SHAP values and AUC-ROC targets are now included in the Tai Mai talk-to -- excellent for a physician/scientist.

**Issues:**

11. **Line 129: "$100--$180/month in CMS reimbursement (CPT 99454 at $52 plus 99457 clinician time at $52, with additional billing for extended management)"** -- The Implementation Guide (Lines 188-201) shows 99454 at $52.11 and 99457 at $51.77, totaling $103.88. To reach $180, you need at least one additional 99458 ($41.42) bringing the total to $145.30, or two 99458 units ($186.72). The "$100-$180" range is defensible but the parenthetical math ("$52 plus $52") only explains the bottom of the range. This is acceptable as-is but Will should know the components if challenged.

12. **Line 129: "We use cellular-connected devices so they work for rural patients without WiFi."** -- This is a strong point that correctly matches the Implementation Guide's device strategy (Lines 106-117). No issue here -- noting it as a positive correction from what appears to have been a consumer-device-centric earlier draft.

13. **Line 131: "Phase 1 targets AUC-ROC above 0.75 with sensitivity above 80% for the highest-risk decile"** -- These are reasonable Phase 1 targets for a model trained on CMS public use files. However, the phrase "highest-risk decile" combined with "sensitivity above 80%" needs clarification. Sensitivity of 80% for the top decile means that among all patients who are actually hospitalized/visit the ER within 90 days, 80% of them are in the top-scoring 10% of the model. This is ambitious but not unreasonable for a well-constructed model with strong predictors. Will should be prepared to explain what "sensitivity for the top decile" means if Tai Mai asks -- she will understand the terminology.

#### 3.3 Collect Cash Module (Lines 135-145)

**Strengths:**
- RPM/CCM billing capture correctly describes the 16-day threshold for 99454 and 20-minute threshold for 99457/99458.
- Phase markers (Phase 2, Phase 3) are correctly applied to Coding Optimization and Denial Prevention.
- The MIPS weight breakdown (Quality 30%, Cost 30%, PI 25%, IA 15%) matches CMS 2026 MIPS.

**Issues:**

14. **Line 144: MIPS weights "Quality (30%), Cost (30%), PI (25%), IA (15%)"** -- These weights are for CY 2025 MIPS. CMS has been adjusting these weights annually. For CY 2026, the proposed rule may change them. The weights listed are the most recent finalized weights and are likely to remain close. This is acceptable but Will should note "based on current CMS MIPS methodology" if challenged.

---

### Section 4: Technical Differentiators (Lines 148-181)

**Strengths:**
- The DoD-to-rural-health translation table (Lines 152-160) is genuinely compelling. "AI triage classification in austere environments" mapping to "AI risk stratification for underserved rural populations" is a powerful framing.
- The comparison table (Lines 164-172) makes a strong case on cost, margins, and control.
- The competitor list (Lines 176-179) is accurate and well-segmented.

**Issues:**

15. **Line 155: "DDIL-native architecture (works without connectivity) | Cellular-connected RPM devices for clinics with unreliable broadband"** -- The mapping is somewhat strained. DDIL (Denied, Degraded, Intermittent, Limited) connectivity refers to the platform itself operating offline. Cellular-connected RPM devices are a device-layer choice, not an architecture-layer DDIL capability. The Implementation Guide does not describe any offline capability for the platform itself. If the platform's GovCloud services go down, the system does not function. The DDIL comparison should be reframed honestly.

**OLD TEXT (Lines 155):**
```
| DDIL-native architecture (works without connectivity) | Cellular-connected RPM devices for clinics with unreliable broadband |
```

**NEW TEXT:**
```
| DDIL-native architecture (works without connectivity) | Architecture designed for unreliable rural broadband: cellular RPM devices bypass clinic WiFi; asynchronous data sync tolerates intermittent connectivity |
```

16. **Line 166: "Per-clinic COGS: ~$30--50/month (infrastructure)"** -- The Implementation Guide (Line 338) shows per-clinic COGS at 100 clinics as "$100-$150/month," not $30-$50. The $30-$50 figure appears to be the Phase 1 per-clinic infrastructure cost ($750/month divided by 2-3 clinics = $250-$375/clinic), which is actually HIGHER than what is stated. At scale (100 clinics), the Guide says $10K-$15K/month total = $100-$150/clinic. The $30-$50 figure is not supported by either document.

**OLD TEXT (Line 166):**
```
| **Per-clinic COGS** | ~$650/month (licenses alone) | ~$30--50/month (infrastructure) |
```

**NEW TEXT:**
```
| **Per-clinic COGS** | ~$650/month (licenses alone) | ~$100--150/month at scale (infrastructure only, no licensing) |
```

17. **Line 167: "Gross margin at $2K/month: 97%+"** -- If per-clinic COGS is $100-$150/month (not $30-$50), then gross margin at $2K/month is ($2000 - $150) / $2000 = 92.5% to ($2000 - $100) / $2000 = 95%. Still excellent, but not 97%+. At $4K/month, it would be 96-97.5%. The 97%+ claim is only true at the high end of pricing with the low end of COGS.

**OLD TEXT (Line 167):**
```
| **Gross margin at $2K/month** | ~67% | **97%+** |
```

**NEW TEXT:**
```
| **Gross margin at $2K/month** | ~67% | **93--95%** (at scale; 97%+ at $4K tier) |
```

18. **Line 171: "Scale economics: Costs scale linearly per seat (SaaS) vs. Costs scale with infrastructure (logarithmic)"** -- "Logarithmic" is a specific mathematical claim. Infrastructure costs do exhibit sublinear scaling due to shared resources, but "logarithmic" overstates it. The Implementation Guide's scaling table (Lines 330-337) shows costs going from $750/mo (3 clinics) to $10K-$15K/mo (100 clinics) -- that is roughly a 15-20x cost increase for a 33-50x clinic increase. This is sublinear but closer to square-root scaling than logarithmic. Recommend "sublinear" instead.

**OLD TEXT (Line 171):**
```
| **Scale economics** | Costs scale linearly per seat | Costs scale with infrastructure (logarithmic) |
```

**NEW TEXT:**
```
| **Scale economics** | Costs scale linearly per seat | Costs scale sublinearly with infrastructure (shared resources across clinics) |
```

---

### Section 5: Market Opportunity (Lines 185-194)

**Strengths:**
- Virginia/National TAM table is clean.
- Virginia TAM math is internally consistent (133 x $2K-$4K x 12 = $3.2M-$6.4M).

**Issues:**

19. **Line 192: National TAM "$132M--$264M/year"** -- Let us check: 5,500 RHCs x $2,000/month x 12 = $132M. 5,500 x $4,000 x 12 = $264M. The math checks out. However, there are no FQHCs included in the national TAM, while the Virginia number includes 27 FQHCs. This is inconsistent. If FQHCs are part of the addressable market (and they should be -- there are ~1,400 FQHCs nationally with ~14,000 delivery sites), the national TAM should include them or the Virginia TAM should exclude them. Additionally, no market capture rate is assumed -- this is 100% penetration, which no investor will take seriously. A 5-10% capture rate ($6.6M-$26.4M) would be more credible as a "serviceable obtainable market" (SOM).

20. **Line 193: Revenue Unlock per Clinic "$195K--$267K/year"** -- This is consistent with the Implementation Guide (Line 211). Good. However, this is the BRIEF's number, and Line 22 in the Problem section still says "$100K--$250K." See Issue #4 above.

---

### Section 6: Implementation Roadmap (Lines 196-221)

**Strengths:**
- Three-phase structure now matches the Implementation Guide exactly.
- Phase 1 timeline (Months 1-4) matches the Guide.
- Phase 1 deliverables are appropriately scoped.
- Grant budget allocation matches the Guide line-for-line.

**Issues:**

21. **Line 201: Phase 1 says "2--3 Virginia RHCs live"** -- The Implementation Guide (Line 268) also says 2-3. Consistent. Good.

22. **Line 216: Contingency is $34,000 (68%)** -- The Implementation Guide (Line 318) also shows $34,000 contingency. Consistent. However, 68% contingency in a grant budget will draw scrutiny from Jennifer O'Daniel. The Brief addresses this (Line 221) with the explanation that Will is the developer, eliminating the largest cost. This is a reasonable explanation but Will should be prepared for the question "why not use that $34K to fund additional clinics or hire help?" The Implementation Guide (Line 327) provides a better answer: "add pilot clinics, hire specialized help if needed, or absorb EHR integration surprises." Will should internalize this answer.

23. **Line 219: "Total project value: $200,000+ ($50K VIPC grant + ~$150K+ Will/team sweat equity in-kind)"** -- The Implementation Guide (Line 325) calculates in-kind as ~$144,000 (Will $96K + Cari Ann $12K + Jim $24K + Jessica $12K = $144K), making total project value ~$194,000. The Brief rounds up to "$200,000+" and says "$150K+ sweat equity." These are close enough for a presentation but technically inconsistent.

**OLD TEXT (Line 219):**
```
**Total project value:** $200,000+ ($50K VIPC grant + ~$150K+ Will/team sweat equity in-kind)
```

**NEW TEXT:**
```
**Total project value:** ~$194,000 ($50K VIPC grant + ~$144K team sweat equity in-kind: Will at 640 hrs, plus clinical advisory, project management, and compliance expertise)
```

---

### Section 7: Presentation Q&A Prep (Lines 225-258)

**Strengths:**
- Covers both standard and hard questions -- significant improvement.
- The "Can you really build all this for $50K?" answer (Line 243) is the single most important answer in the document and it is excellent.
- The FDA/SaMD answer (Line 257) correctly cites the 21st Century Cures Act and the four CDS exemption criteria.
- The "What happens if the pilot fails?" answer (Line 254) is well-structured with multiple fallback strategies.

**Issues:**

24. **Line 234: "HL7 FHIR R4 -- the standard CMS mandated for interoperability. We use bonFHIR, a purpose-built FHIR integration library, inside our n8n workflow engine to connect to whichever EHR the clinic runs -- eClinicalWorks, athenahealth, MEDITECH, Azalea Health."** -- Correct EHR list, correct FHIR standard. However, "CMS mandated" is an overstatement. The ONC Cures Act Final Rule and CMS Interoperability rules require certified EHR technology to support FHIR R4 APIs, but CMS did not mandate FHIR R4 for all interoperability. The nuance: CMS mandated that payers provide FHIR-based Patient Access APIs, and ONC required certified EHRs to support standardized FHIR APIs. Saying "the standard ONC and CMS require for interoperability" is more precise. This is a minor point but could matter to Tai Mai.

25. **Line 237: "SaaS subscription -- $2,000 to $4,000 per clinic per month. The platform unlocks $195,000 to $267,000 per year in new CMS reimbursement per clinic. That's an 8--11x ROI."** -- Let us check the ROI math. At $2K/month ($24K/year) unlocking $195K: ROI = $195K / $24K = 8.1x. At $4K/month ($48K/year) unlocking $267K: ROI = $267K / $48K = 5.6x. At $2K/month unlocking $267K: ROI = 11.1x. At $4K/month unlocking $195K: ROI = 4.1x. The "8-11x" range cherry-picks the best combinations ($2K cost / $195K-$267K revenue). The worst case ($4K cost / $195K revenue) yields only 4.1x. This is misleading. The honest range is 4-11x, or the presentable range at the $2K tier is 8-11x with the qualifier.

**OLD TEXT (Line 237):**
```
"SaaS subscription -- $2,000 to $4,000 per clinic per month. The platform unlocks $195,000 to $267,000 per year in new CMS reimbursement per clinic. That's an 8--11x ROI.
```

**NEW TEXT:**
```
"SaaS subscription -- $2,000 to $4,000 per clinic per month depending on tier. At the entry tier, the platform unlocks $195,000 to $267,000 per year in new CMS reimbursement -- an 8--11x return on the clinic's subscription cost.
```

26. **Line 240: "Salesforce Health Cloud licensing alone would consume 17% of the VIPC grant"** -- This is a legacy Salesforce comparison. Let us check: 17% of $50K = $8,500. The Implementation Guide does not mention Salesforce costs. This talking point is still useful for comparison purposes but the 17% figure should be verifiable. Salesforce Health Cloud Enterprise Edition is roughly $300/user/month. For 5 users x $300 x 4 months = $6,000 (12% of grant). With Shield encryption ($150/user/month), that is $450/user/month x 5 users x 4 months = $9,000 (18%). The 17% figure is in the right range but imprecise. Since this is a verbal talking point, the approximation is acceptable. However, the "$150K+/year before serving a single patient" claim should be checked: Salesforce Health Cloud + MuleSoft at enterprise scale could plausibly reach $150K/year, but this is the high end. Recommend "can easily exceed $100K/year" for defensibility.

**OLD TEXT (Line 240):**
```
Salesforce Health Cloud licensing alone would consume 17% of the VIPC grant, and at scale it's $150K+/year before serving a single patient.
```

**NEW TEXT:**
```
Salesforce Health Cloud licensing alone could consume 15-20% of the VIPC grant, and at scale, enterprise healthcare SaaS licensing can easily exceed $100K/year before serving a single patient.
```

27. **Line 240: "clinics with $34K--$95K total IT budgets"** -- This is an important claim about RHC IT budget constraints. No source is cited. HRSA and NACHC publish some data on FQHC operational costs, but RHC-specific IT budget data is harder to find. The range is plausible for small rural practices but should be qualified as "typically" or "estimated" unless Will has a specific source.

28. **Line 257: "The January 2026 FDA CDS guidance update broadens enforcement discretion in our favor."** -- This is a specific regulatory claim about a recent FDA action. If accurate, it is a strong point. Will should be able to cite the specific guidance document title if Tai Mai asks. If this guidance does not exist or has different implications, it would be damaging to cite it. Recommend verifying and having the document title ready.

---

### Section 8: Know Your Audience (Lines 261-274)

**Strengths:**
- Each panelist is profiled with specific investment interests and tailored talking points.
- The Michael Jarvis "intersection of your two investment themes" line (Line 269) is excellent.
- Jennifer O'Daniel framing includes grant ROI, Virginia impact, and Series A pipeline.

**Issues:**

29. **Line 265: "$50K from VIPC plus $150K+ in sweat equity"** -- Should be "$144K in sweat equity" per the Implementation Guide's calculation. See Issue #23. Also: "Pilot data positions ACT for Series A by Month 10, funding 4--6 Virginia-based technical roles." -- The Implementation Guide (Lines 297-306) lists 5 team members, not 4-6 new roles. These are the existing team, not new hires. If Will claims the Series A funds 4-6 NEW Virginia technical roles, he needs a hiring plan. The Implementation Guide does not include one for Phase 2 headcount specifically. This claim should either be substantiated or removed.

**OLD TEXT (Line 265):**
```
Pilot data positions ACT for Series A by Month 10, funding 4--6 Virginia-based technical roles.
```

**NEW TEXT:**
```
Pilot data positions ACT for a seed or Series A raise by Month 10, enabling ACT to hire Virginia-based technical and implementation staff to support statewide rollout.
```

30. **Line 273: "97% gross margins on a SaaS with built-in revenue justification for every buyer -- that's the Series A story."** -- Per Issue #17, the actual margin at $2K/month is 93-95% at scale, not 97%. This talking point repeats the inflated number.

**OLD TEXT (Line 273):**
```
And 97% gross margins on a SaaS with built-in revenue justification for every buyer -- that's the Series A story.
```

**NEW TEXT:**
```
And 93-95% gross margins on a SaaS with built-in revenue justification for every buyer -- that's the Series A story.
```

---

## 3. Cross-Document Consistency Table

Summary of all inconsistencies between `01_VV_Technical_Brief.md` and `02_Implementation_Guide.md`, prioritized by risk of surfacing during Q&A:

| # | Topic | Brief Says | Guide Says | Severity |
|---|---|---|---|---|
| 1 | **Revenue unlock per clinic** | $100K-$250K/year (Line 22) | $195K-$267K/year (Line 211) | HIGH -- two different numbers in the same presentation materials |
| 2 | **Total in-kind / project value** | "$150K+" / "$200,000+" (Line 219) | $144,000 / $194,000 (Line 325) | MEDIUM -- $6K gap in in-kind, $6K gap in total |
| 3 | **Per-clinic COGS** | $30-$50/month (Line 166) | $100-$150/month at 100 clinics (Line 338) | HIGH -- 3x difference undermines unit economics story |
| 4 | **Gross margin** | 97%+ (Lines 167, 269, 273) | Implied 93-95% based on Guide's COGS numbers | MEDIUM -- still excellent margins, but 97% is not supported |
| 5 | **Pricing tiers** | $2,000-$4,000/month (Line 190) | $500-$4,000/month with 3 tiers (Guide Line 452) | MEDIUM -- Brief omits Starter tier at $500/month |
| 6 | **ROI claim** | 8-11x (Line 237) | Math shows 4-11x range depending on tier | MEDIUM -- cherry-picked range |
| 7 | **4-6 Virginia technical roles** | Claimed (Line 265) | No Phase 2 hiring plan in Guide | LOW -- aspirational but unsubstantiated |
| 8 | **bonFHIR description** | "Community n8n node" only (Line 41) | "Community n8n node + direct FHIR R4 HTTP calls" (Guide Line 32) | LOW -- Brief omits fallback approach |
| 9 | **Compliance prediction** | "Designed to predict 60-90 days" (Line 114) | No predictive compliance model described; module is task tracker + reminders (Guide Lines 141-147) | MEDIUM -- Brief promises capability not in build plan |
| 10 | **January 2026 FDA CDS guidance** | Cited (Line 257) | Cited (Guide Line 396) | LOW -- consistent, but verify it exists |

---

## 4. Technical Accuracy Assessment

### Claims That Are Accurate and Strong

| Claim | Assessment |
|---|---|
| Amazon GovCloud is FedRAMP High and HIPAA BAA eligible | **Correct.** AWS GovCloud (US) regions are FedRAMP High authorized. |
| n8n is open-source, self-hostable workflow automation | **Correct.** n8n is source-available (Sustainable Use License for Enterprise, MIT-like for Community). Self-hosting is the standard deployment model. |
| PostgreSQL 16 with RLS for multi-tenancy | **Correct and well-architected.** RLS is a validated pattern for multi-tenant HIPAA workloads. PGAudit for audit logging is standard. |
| AES-256 encryption at rest via KMS | **Correct.** RDS encryption uses AES-256 with KMS customer-managed keys. |
| PGAudit for HIPAA audit logging | **Correct.** PGAudit is the standard PostgreSQL audit extension and is supported on RDS. |
| n8n Community Edition ~23 req/s in single mode | **Plausible.** This is cited in n8n's documentation for single-instance deployments. Actual throughput depends on workflow complexity. |
| SHAP values for model interpretability | **Correct.** SHAP (SHapley Additive exPlanations) is the standard approach for XGBoost interpretability. |
| 21st Century Cures Act CDS exemption (four criteria) | **Correct.** The four criteria under Section 3060(a) are accurately described (Line 257). |
| CPT 99454 requires 16+ days of data transmission | **Correct.** CMS requires 16 calendar days of data transmission per 30-day period. |
| CPT 99457 requires 20 minutes of clinician interactive time | **Correct.** |
| Tenovi: 40+ FDA-cleared devices, single API | **Correct** as of Tenovi's published specifications. |

### Claims That Are Unsupported or Overstated

| # | Claim | Location | Issue | Risk Level |
|---|---|---|---|---|
| 1 | "Same proven stack VV deploys for defense clients" | Line 12, 43 | Credibility depends on defense project actually using n8n + PostgreSQL. If defense project uses different components, "same stack" is false. Cannot verify from documents. | MEDIUM |
| 2 | "Designed to predict compliance risk 60-90 days in advance" | Line 114 | No predictive compliance model in the build plan. Module is a task tracker. | MEDIUM |
| 3 | "$30-$50/month per-clinic COGS" | Line 166 | Contradicted by Guide's own numbers ($100-$150/clinic at scale) | HIGH |
| 4 | "97%+ gross margin" | Lines 167, 269, 273 | Does not hold at $2K/month with $100-$150 COGS ($2K tier is 93-95%) | MEDIUM |
| 5 | "Logarithmic" scale economics | Line 171 | Overstates sublinear scaling; Guide's numbers suggest square-root-like scaling | LOW |
| 6 | "15+ distinct regulatory obligations" | Line 20 | Plausible but unsourced | LOW |
| 7 | "1 physician per 2,500+ patients in some Virginia counties" | Line 21 | Unsourced; which counties? | LOW |
| 8 | "$34K-$95K total IT budgets" for RHCs | Line 240 | Unsourced | LOW |
| 9 | "January 2026 FDA CDS guidance update" | Line 257 | Specific regulatory event -- must be verifiable | MEDIUM |
| 10 | "$100K-$250K revenue leakage" | Line 22 | Own Implementation Guide calculates $195K-$267K | HIGH |

### Claims That Are Technically Correct but Need Nuance

| Claim | Nuance Needed |
|---|---|
| "FedRAMP High" as compliance posture (Line 169) | The infrastructure is FedRAMP High; the application is not FedRAMP authorized. |
| "CMS mandated" FHIR R4 (Line 234) | ONC required certified EHRs to support FHIR R4 APIs; CMS mandated payer Patient Access APIs. More precise: "ONC and CMS require." |
| "Clinic live in 2 weeks" (Line 97) | After platform is built and base configuration exists. Not from a standing start. |
| Platform described as "turnkey" (Line 12) | Not yet built. "Designed as turnkey" is more honest. |

---

## 5. Missing Critical Information

### High Priority (add before presentation)

1. **Correct the revenue unlock number in Section 1.** The $100K-$250K range on Line 22 is contradicted by the Guide's $195K-$267K bottoms-up calculation. Use the defensible number.

2. **Correct per-clinic COGS and gross margin claims.** The $30-$50/month COGS and 97%+ margin are the most dangerous numbers in the document because they are central to the investment thesis and they are wrong per the team's own Implementation Guide. A sophisticated investor will check this math.

3. **Add the Implementation Guide's pricing tier structure as a verbal backup.** The Brief shows $2K-$4K/month. The Guide shows $500-$4K/month with 3 tiers. If asked "isn't that expensive for a small RHC?", Will needs to know the $500 Starter tier exists.

4. **Prepare a "What does Phase 1 actually deliver?" one-liner.** The Brief presents the full vision. Will needs a rehearsed 30-second summary: "The $50K grant builds the core platform on GovCloud, deploys to 2-3 Virginia RHCs with HIPAA compliance tracking, EHR integration with one system, RPM device monitoring with billing capture, and AI risk stratification v1. That is the Phase 1 MVP we validate in four months."

### Medium Priority

5. **Quantify the "3 Virginia RHCs closing in 2025" claim.** Which clinics? This is a powerful data point that becomes devastating with specifics.

6. **Prepare the Salesforce comparison as a contrast point, not a straw man.** The current "Why not Salesforce" answer (Line 239-240) is strong but includes a specific percentage (17%) that is approximately right. Will should know the exact math if challenged.

7. **Health equity framing for Tai Mai.** The rural health disparities data is already in the Brief (Line 21) but is not framed as a health equity argument. A single sentence -- "This is fundamentally a health equity platform" -- would resonate with a physician/scientist evaluator.

### Low Priority

8. **Team credibility beyond Will.** The Brief mentions "VV's technical lead" but does not describe the broader team. The Guide lists Jim Pfautz (CEO), Cari Ann (clinical), Jessica (compliance). Investors fund teams. A verbal mention of "our clinical advisor validates every workflow" would strengthen the story.

9. **IP discussion.** What is proprietary? The n8n workflows? The ML models? The clinical logic? The React dashboard? All of it is custom code owned by VV, which is the answer -- but Will should be ready to articulate it.

---

## 6. Summary of All Recommended Changes

Each change specifies exact old and new text. Line numbers reference `/home/user/AC/VIPC/01_VV_Technical_Brief.md`.

| # | Line(s) | Issue | Severity |
|---|---|---|---|
| 1 | 12 | "ships" implies finished product | LOW |
| 2 | 22 | Revenue unlock inconsistent with Guide ($100K-$250K vs $195K-$267K) | HIGH |
| 3 | 41 | bonFHIR missing HTTP fallback language | LOW |
| 4 | 114 | Compliance prediction claim not in build plan | MEDIUM |
| 5 | 155 | DDIL mapping is strained | LOW |
| 6 | 166 | Per-clinic COGS wrong ($30-$50 vs Guide's $100-$150) | HIGH |
| 7 | 167 | Gross margin overstated (97%+ vs 93-95%) | MEDIUM |
| 8 | 169 | FedRAMP High framing misleading | LOW |
| 9 | 171 | "Logarithmic" scaling overstated | LOW |
| 10 | 219 | Total project value inflated vs Guide | MEDIUM |
| 11 | 237 | ROI range cherry-picked (8-11x vs actual 4-11x) | MEDIUM |
| 12 | 240 | Salesforce cost comparison approximations | LOW |
| 13 | 265 | "4-6 Virginia technical roles" unsubstantiated | LOW |
| 14 | 273 | 97% margin repeated in Tai Mai talking point | MEDIUM |

### Priority Actions Before Tomorrow

1. **IMMEDIATE (tonight):** Fix revenue unlock number in Section 1 (Change #2). This number is repeated in the presentation and the Guide contradicts it with better math.
2. **IMMEDIATE (tonight):** Fix per-clinic COGS and gross margin (Changes #6, #7, #14). These are central to the investment thesis and are verifiably wrong against the team's own Implementation Guide.
3. **IMMEDIATE (tonight):** Fix total project value to match Guide (Change #10). Jennifer O'Daniel will scrutinize grant math.
4. **HIGH (tonight if time):** Fix ROI range or qualify it (Change #11). Investors will check the math.
5. **HIGH (tonight if time):** Soften compliance prediction claim (Change #4). Tai Mai will probe AI capabilities.
6. **MEDIUM (morning prep):** Remaining changes are verbal-prep items Will should internalize.

---

## 7. What the Brief Gets Right

To be balanced: this document does several things very well that should not be lost in revision.

1. **The stack migration from Salesforce to n8n/PostgreSQL was the right call.** The open-source stack eliminates the most dangerous objection (licensing costs eating the grant) and makes the "no vendor lock-in" claim honest.

2. **The 3C framework is memorable and maps cleanly to real problems.** "Compliance, Care, Collect Cash" is a presentation-ready mnemonic that every panelist will remember.

3. **The DoD-to-healthcare translation table is genuinely differentiated.** No other RHC platform vendor can claim GovCloud defense experience.

4. **The Q&A section now covers hard questions.** The "What if the pilot fails?" and "FDA regulatory risk?" answers are particularly well-constructed.

5. **The cellular-connected device strategy is clinically appropriate.** Unlike consumer wearables, this addresses the real connectivity challenges of rural patients.

6. **The audience-specific talking points demonstrate genuine preparation.** Knowing Michael Jarvis's HADRIUS and OHM investments, and crafting specific angles for each, shows professionalism.

7. **The contingency explanation is honest and compelling.** "68% contingency because the developer is the founder" is a strength, not a weakness, when framed correctly.

---

*Review completed February 25, 2026. Presentation is tomorrow. Focus on the HIGH-severity numerical corrections tonight -- the narrative and structure are strong.*
