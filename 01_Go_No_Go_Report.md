# GO / NO-GO DECISION REPORT

**Version:** 1.1 (Revised) | **Classification:** CUI | **Distribution:** Internal Consortium Only

## DIU AI-Assisted Triage & Treatment Challenge (PROJ00628)
### Prepared for: Veteran Vectors (Prime) | Authentic Consortium
### Date: February 24, 2026

---

## 1. OPPORTUNITY SUMMARY

| Field | Detail |
|---|---|
| **Solicitation** | DIU CSO HQ0845-20-S-C001 (New AOI posted under existing CSO umbrella) |
| **Project ID** | PROJ00628 |
| **Contracting Authority** | Defense Innovation Unit (DIU) |
| **Requirements Sponsor** | PM Soldier Medical Devices (PEO Soldier) |
| **Operational User** | 30th Medical Brigade |
| **Award Type** | Prize Challenge (up to 8 finalists); pathway to OTA Prototype Agreement |
| **Prize Pool** | $999,000 (split among finalists; may be tiered based on ranking, est. $50K-$200K per finalist) |
| **Open Call Close** | March 2, 2026 |
| **Semi-Finalist Notification** | ~March 9, 2026 |
| **Pitch Days** | April 7-8, 2026 |
| **Live Demo (Sword 2026)** | May 8-12, 2026 |
| **Deliverable Scale** | 30 units by May 2026; 15,000 units/yr by May 2027 |
| **Evaluation Criteria** | Introduction, System Effectiveness, Technical Feasibility, Scalability/Economics, Commercial Viability, Submission Quality |

---

## 2. REQUIREMENT FIT ANALYSIS

### 2.1 Core Need
The DoD requires a **portable, ruggedized, network-capable hemodynamic status monitoring system** for forward (Role 1/2) combat medics performing Tactical Combat Casualty Care (TCCC), CASEVAC, and MEDEVAC operations. The system must operate in Disconnected, Intermittent, and Limited-bandwidth (DDIL) environments.

### 2.2 Capability Alignment Matrix

| Requirement | Consortium Capability | Fit |
|---|---|---|
| Hemodynamic monitoring (vitals, trend analytics) | Software/AI analytics layer -- Veteran Vectors core competency in AI/ML edge inference and time-series analytics | STRONG |
| Hardware (ruggedized, wearable/standoff, 72-hr battery) | Requires hardware partner within consortium (medical device OEM) | MODERATE -- requires partner validation |
| BATDOK/ATAK/EHR integration | Software integration -- achievable via standard APIs and military data standards. Note: BATDOK API access not yet confirmed | MODERATE -- contingent on API access confirmation |
| Cloud + on-premise/DDIL edge compute | Edge AI deployment is Veteran Vectors' strength; demonstrated on ARM platforms | STRONG |
| FDA 510(k) clearance | Must leverage consortium partner with existing 510(k) pathway or predicate device | CRITICAL GAP -- no partner confirmed |
| IL-5 ATO/FedRAMP | Consortium experience with gov cloud compliance; IL-5 NOT required for prize challenge phase, required for follow-on OTA | MODERATE -- Phase 3 requirement |
| Manufacturing scale (15K units/yr) | Requires manufacturing consortium partner | MODERATE -- requires partner validation |
| AI-assisted triage decision support | Core alignment with Veteran Vectors AI/ML capabilities | STRONG |

### 2.3 Consortium Status
- **Veteran Vectors (Prime):** Veteran-owned small business; AI/ML software development; edge computing; DoD-cleared personnel; mission-driven culture with first-hand understanding of battlefield conditions

**IMPORTANT: As of February 24, 2026, no consortium partners have been formally committed.** The following roles require confirmed partners before submission:

- **Authentic Consortium Partners (Required -- Not Yet Confirmed):**
  - Medical device OEM partner (hardware, FDA 510(k)) -- **CRITICAL: Must be confirmed before March 2**
  - Cloud/cybersecurity partner (IL-5, FedRAMP)
  - Manufacturing/logistics partner (scale production)
  - Clinical/TCCC subject matter experts

---

## 3. RISK ASSESSMENT

### 3.1 Key Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| **No FDA 510(k) predicate device in consortium** | HIGH | HIGH | Identify and onboard medical device partner with existing clearance pathway immediately; no confirmed partner = NO-GO |
| **Software development timeline (12-week sprint)** | HIGH | MEDIUM | Use COTS hardware base; develop against hardware abstraction layer + simulators from Week 1; parallel tracks |
| **Hardware procurement timeline (30 units by May 2026)** | HIGH | MEDIUM | COTS platform selection by Feb 26; procurement by Apr 15, allowing 3 weeks for SW integration |
| **Significant investment with no guaranteed return** | MEDIUM | HIGH | Total exposure if selected as finalist: ~$661K vs. ~$125K est. prize share. Gap funded by consortium cost-sharing and Veteran Vectors operating capital. View as OTA pipeline investment |
| **BATDOK / ATAK API access not confirmed** | MEDIUM | MEDIUM | Submit API access requests by Mar 5 (BATDOK) and Mar 10 (ATAK SDK); fallback to standard HL7 FHIR if BATDOK API delayed |
| **Consortium formation legal/administrative timeline** | MEDIUM | MEDIUM | Execute Letters of Intent by Mar 2; full teaming agreements by Mar 15; engage legal counsel immediately |
| **Training data access (JTTR DUA)** | MEDIUM | MEDIUM | Begin JTTR Data Use Agreement process immediately; develop initial models on MIMIC-III/IV (publicly available); fine-tune on JTTR when available |
| **Competition from established medical device companies** | MEDIUM | HIGH | Differentiate on AI/ML analytics, DDIL-native edge AI, and BATDOK/ATAK integration -- capabilities incumbents lack |
| **IP and data rights in OTA/prize structure** | MEDIUM | LOW | Clarify IP allocation among consortium partners in teaming agreement; negotiate government purpose rights in OTA terms |
| **Hardware ruggedization requirements** | MEDIUM | LOW | Partner with proven mil-spec device manufacturer |
| **DDIL edge compute performance** | MEDIUM | LOW | Leverage ONNX Runtime on ARM; prototype and benchmark early |
| **Manufacturing scale to 15K/yr** | MEDIUM | MEDIUM | Contract manufacturing partner with DoD supply chain experience |

### 3.2 Showstoppers
1. **FDA pathway** -- Without a consortium member possessing a 510(k)-cleared hemodynamic monitoring device (or credible predicate device pathway), the proposal will score poorly on System Effectiveness. As of this report date, no medical device partner is confirmed.
2. **Hardware availability** -- Delivering 30 functional units by May 2026 requires starting from a COTS platform, not a custom build.
3. **Unvalidated technical claims** -- The White Paper cites specific performance targets (>95% sensitivity, <50ms inference, 15--30 minute early warning) that have not been validated against the proposed hardware platform. These must be framed as design targets with validation plans.

---

## 4. FINANCIAL ANALYSIS

### 4.1 Investment Tiers

| Tier | Scope | Estimated Cost | Timing |
|---|---|---|---|
| **Tier 1: Submission** | Solution Brief + White Paper preparation, consortium formation | $15,000 - $25,000 | Feb-Mar 2026 |
| **Tier 2: Finalist Execution** | Software development (~$556K) + 30 prototype units (30 x $3,500 = $105K) | ~$661,000 | Mar-May 2026 |
| **Tier 3: Production Scale** | Sustained engineering, FDA, ATO, manufacturing integration | ~$1.5M/year | Jun 2026-May 2027 |

### 4.2 Revenue Potential

| Item | Estimate |
|---|---|
| **Prize Award (if selected finalist)** | $50,000 - $200,000 per finalist (tiered; 8-way split not guaranteed) |
| **Follow-on OTA Prototype Value** | $2M - $10M (typical DIU prototype OTA range) |
| **Production Contract Potential** | $37.5M--$52.5M/yr (15,000 units x $2,500--$3,500 gov contract price); multi-year IDIQ could exceed $100M |

### 4.3 Cash Flow Analysis

| Period | Outflow | Inflow | Net Position |
|---|---|---|---|
| Feb-Mar 2026 (Submission) | -$25,000 | $0 | -$25,000 |
| Mar-May 2026 (If selected as finalist) | -$661,000 | +$125,000 (est. prize) | -$561,000 |
| Jun 2026+ (If awarded OTA) | -$1.3M/yr | +$2M-$10M OTA | Positive |

**Funding gap:** If selected as finalist, the consortium must fund ~$561,000 net before any OTA award (including submission costs). This must be covered by:
- Veteran Vectors operating capital (Tier 1 submission costs)
- Consortium partner cost-sharing (hardware procurement, FDA, and ATO costs borne by respective partners)
- Prize award partial offset

**Note:** Cost-sharing model among consortium partners must be defined in the Teaming Agreement. The medical device OEM and manufacturing partners are expected to bear hardware and production costs; Veteran Vectors bears software development costs.

### 4.4 ROI Assessment
Even at the maximum Tier 2 investment of ~$661K, the potential follow-on OTA ($2M-$10M) and production contract ($37.5M+/yr) represent a strong ROI. However, the investment is significant and requires consortium cost-sharing to be viable for Veteran Vectors as a small business.

---

## 5. COMPETITIVE POSITIONING

### Advantages
- **Veteran-owned:** SDVOSB status; authentic understanding of combat medic challenges (founding team includes combat veterans)
- **AI/ML differentiation:** Edge AI triage classification and deterioration early warning -- capabilities no existing battlefield monitor provides; incumbents are hardware-first, VitalEdge AI is AI-first
- **DDIL-native architecture:** Purpose-built for disconnected operations, not retrofitted cloud systems
- **Military integration:** Purpose-built BATDOK and ATAK integration, not aftermarket adapters
- **Consortium model:** Best-of-breed team without single-vendor overhead

### Disadvantages
- Medical device incumbents (Philips, Masimo, Zoll) have existing FDA-cleared platforms and may propose with minimal modification
- Hardware development is not a core Veteran Vectors competency -- dependent on consortium partner
- No prior DIU award history (White Paper states "Prior DIU Awards: N/A")
- No confirmed consortium partners as of report date -- risk of being perceived as a "paper consortium"
- No demonstrated past performance in medical device development specifically
- No existing relationship with PM Soldier Medical Devices or 30th Medical Brigade
- Prize challenges attract large applicant pools, including well-funded startups with working prototypes

### Competitor Strategy Assessment
- **Masimo:** Likely to propose existing RAD-67 or similar with AI software enhancement. Strong FDA pathway and hardware, but weaker on DDIL edge AI and military system integration
- **Zoll:** Propaq-based monitoring with existing military contracts. Strong logistics and manufacturing, but limited AI/ML differentiation
- **Philips:** IntelliVue platform adapted for field use. Deep FDA and clinical validation, but bulky form factor and cloud-dependent analytics
- **Startups:** Various AI health startups may propose novel approaches but likely lack DoD integration experience and FDA-cleared hardware

---

## 6. GO / NO-GO RECOMMENDATION

### **RECOMMENDATION: CONDITIONAL GO**

**Conditions for GO (Tiered Milestones):**

| Milestone | Deadline | Required Action |
|---|---|---|
| **Verbal commitment from medical device OEM partner** with identified FDA 510(k) predicate device | Feb 26, 2026 | Named partner + specific predicate device 510(k) number |
| **COTS hardware platform selected** and procurement path for 30 units confirmed | Feb 26, 2026 | Delivery by Apr 15, 2026 (3 weeks for SW integration before Sword) |
| **Letters of Intent executed** with all consortium partners | Mar 2, 2026 | Signed LOIs before Solution Brief submission |
| **Total submission investment stays under $25,000** | Mar 2, 2026 | Tier 1 costs only; Tier 2 finalist execution authorized separately |
| **Full Teaming Agreement with cost-sharing** | Mar 15, 2026 | IP allocation, revenue split, cost ownership defined |

**Rationale:**
The opportunity is strategically valuable. The pathway to a multi-million-dollar OTA prototype agreement and subsequent production contract ($37.5M+/yr) makes this a high-value pipeline opportunity. Veteran Vectors' AI/ML software capabilities are a strong differentiator for the analytics, decision-support, and integration layers. The consortium model covers hardware and regulatory gaps. However, proceeding without a confirmed FDA 510(k) pathway would be a losing proposition, and the ~$661K finalist execution cost requires consortium cost-sharing to be viable.

**If conditions are met: FULL GO -- proceed with Solution Brief and White Paper submission.**
**If conditions are NOT met by Feb 26: NO-GO -- preserve resources for better-aligned opportunities.**

**NO-GO actions if triggered:**
- Cease all bid preparation activity
- Notify any partially engaged potential partners
- Document lessons learned for future DIU opportunities
- Evaluate whether the VitalEdge AI concept has value for other solicitations or as a software-only offering on another team's proposal

**Fallback strategy:** If the full consortium cannot be formed but a medical device OEM partner is confirmed, Veteran Vectors could explore joining another team's proposal as the AI/software component provider rather than serving as prime.

---

**Decision Authority:** _________________________ (Veteran Vectors CEO/President)

**Consortium Lead Concurrence:** _________________________ (Authentic Consortium Lead)

---

*Prepared by: AI Strategy Analysis | Authentic Consortium Bid Team*
*Version 1.1 -- Revised per internal review recommendations*
