# DETAILED REVIEW: Software Development Action Plan (02_Software_Action_Plan.md)

## DIU AI-Assisted Triage & Treatment (PROJ00628) -- Veteran Vectors / Authentic Consortium

### Reviewer: Defense Software Engineering & Technical Proposal Review
### Date: February 24, 2026

---

## OVERALL ASSESSMENT

**Rating: STRONG DRAFT with SIGNIFICANT GAPS requiring revision before submission.**

The Software Action Plan demonstrates solid architectural thinking and a credible technology stack for an edge-AI medical system. The three-tier architecture is well-conceived for DDIL operations, and the AI/ML model strategy is technically sound. However, the document has notable weaknesses in cost realism, timeline feasibility for the FDA/ATO pathway, incomplete risk coverage, and several missing elements that a DIU evaluator will expect. The recommendations below are prioritized by impact on proposal competitiveness.

---

## 1. TECHNICAL ACCURACY

### Strengths
- **Three-tier architecture is appropriate.** The Device/Edge/Cloud separation with DDIL-native design is the correct pattern for this operational environment. The decision to make all critical functions edge-resident with cloud as enhancement-only is strategically sound and aligns with what DIU evaluators want to see.
- **AI/ML model selection is defensible.** XGBoost for initial deployment with LSTM upgrade path is pragmatic. XGBoost is well-understood, fast to train, and performs well on tabular physiological data. The ONNX export to TF Lite pipeline is a proven path for edge deployment.
- **Technology stack is coherent.** The toolchain (PyTorch -> ONNX -> TF Lite, K3s for edge orchestration, MQTT for DDIL messaging, CRDTs for conflict resolution) represents current best practices for edge-AI systems.

### Issues and Recommendations

**ISSUE 1.1 (HIGH): Python on the edge compute is a significant concern.**
Section 2.2 lists "Python/C++ with ONNX Runtime" for the Edge AI Engine. Running Python on a ruggedized ARM-based edge device introduces memory overhead, startup latency, and battery drain. For a medical device with a 72-hour battery target, this is problematic.

- **Recommendation:** Clarify the Python/C++ split explicitly. State that inference is C++ via ONNX Runtime C API, and Python is used only for development/testing. Alternatively, specify that the edge compute unit is a tablet-class device (not MCU) where Python overhead is acceptable. The current ambiguity will raise questions from technical evaluators.

**ISSUE 1.2 (MEDIUM): K3s on edge devices may be over-engineered for 30-unit prototype.**
Kubernetes on edge devices adds operational complexity. For a prototype phase with 30 units, K3s may introduce more problems than it solves -- particularly for medics who are not sysadmins.

- **Recommendation:** Specify K3s as the Phase 3 fleet management solution. For Phase 1-2, use a simpler deployment model (direct container deployment or bare-metal image). Add a sentence: "K3s orchestration introduced in Phase 3 for fleet-scale management; prototype phase uses streamlined direct deployment."

**ISSUE 1.3 (MEDIUM): TimescaleDB on edge alongside SQLite creates unnecessary complexity.**
Section 2.2 lists "SQLite + TimescaleDB (lite)" for edge storage. TimescaleDB requires PostgreSQL, which is heavyweight for an embedded edge device. SQLite alone is sufficient for local time-series buffering.

- **Recommendation:** Use SQLite exclusively on the edge tier. Reserve TimescaleDB for the cloud tier where aggregate analytics justify it. The current design doubles the database operational burden on a resource-constrained device.

**ISSUE 1.4 (LOW): ONNX Runtime Mobile vs. TensorFlow Lite -- pick one.**
Section 5.1 lists the ML pipeline as "PyTorch -> ONNX -> TF Lite" but the Edge Runtime as "ONNX Runtime Mobile." These are two different inference runtimes. Either you deploy ONNX models on ONNX Runtime, or you convert to TFLite format and run on TF Lite runtime.

- **Recommendation:** Standardize on one path: either "PyTorch -> ONNX -> ONNX Runtime Mobile" or "PyTorch -> ONNX -> TF Lite conversion -> TF Lite Runtime." The current description suggests the team has not finalized this decision, which is a minor credibility hit.

---

## 2. COST REALISM

### Strengths
- The labor role breakdown is reasonable for the scope of work.
- Non-labor line items are plausible and include often-forgotten items like ATAK licenses and security scanning tools.

### Issues and Recommendations

**ISSUE 2.1 (HIGH): Labor rates are 15-25% below market for cleared DoD AI/ML engineers.**
The proposed rates ($170-$225/hr) are below typical rates for engineers with active clearances doing AI/ML work on DoD contracts in 2026:
- A cleared ML Engineer typically bills at $235-$275/hr on DoD contracts, not $200/hr.
- A cleared Technical Lead/Architect is typically $260-$300/hr, not $225/hr.
- A cleared DevOps engineer with GovCloud/ATO experience is typically $220-$260/hr, not $195/hr.

If these are actual company rates (e.g., Veteran Vectors employees, not subcontractors), this is fine -- but the document should clarify that these are fully-burdened rates inclusive of overhead, G&A, and profit. If they are subcontractor rates, they are unrealistically low and the budget will blow out.

- **Recommendation:** Add a footnote clarifying these are "fully-burdened labor rates inclusive of fringe, overhead, G&A, and fee" or adjust rates upward to reflect market reality. DIU evaluators familiar with DoD labor markets will question below-market rates as either unsustainable or an indicator of under-scoped work.

**ISSUE 2.2 (HIGH): Hours calculation appears incorrect for ATAK/Mobile and BATDOK roles.**
The ATAK/Mobile Developer at 0.5 FTE for 8 weeks at $185/hr shows $29,600. At 0.5 FTE, that is 20 hours/week x 8 weeks = 160 hours x $185 = $29,600. The math checks out, but 160 hours for ATAK plugin development including TAK Product Center certification engagement is severely under-scoped. ATAK plugin development, testing, and certification typically requires 400-600 hours minimum.

- **Recommendation:** Either increase the ATAK/Mobile Developer to 1.0 FTE for 12 weeks, or explicitly state that Phase 1-2 delivers an alpha ATAK plugin with certification deferred to Phase 3. The same concern applies to BATDOK integration at 160 hours.

**ISSUE 2.3 (MEDIUM): GovCloud dev/staging at $15,000 for 12 weeks is thin.**
AWS GovCloud costs approximately $3,000-$5,000/month for a minimal development environment with compute, storage, and networking. For 3 months, $15,000 is the absolute floor with no margin for GPU training instances or unexpected usage.

- **Recommendation:** Increase to $20,000-$25,000 or separate the GPU training compute line item ($8,000) and clarify whether it covers GovCloud GPU instances or commercial cloud for non-sensitive training data.

**ISSUE 2.4 (MEDIUM): Phase 3 annual cost of $1.28M is low for the stated scope.**
Phase 3 includes FDA 510(k) submission support, IL-5 ATO, manufacturing integration, AND scaling to 15,000 units -- all in one year. FDA regulatory consulting alone (pre-submission meetings, clinical validation, 510(k) dossier preparation) typically costs $300,000-$500,000, not $150,000. The IL-5 ATO package with 3PAO assessment can run $200,000-$400,000, not $100,000.

- **Recommendation:** Either increase the Phase 3 budget to $1.8M-$2.2M or explicitly state that certain costs (FDA consulting, 3PAO assessment) are borne by consortium partners and not included in the software development budget. Clarity on cost ownership across the consortium is essential.

**ISSUE 2.5 (LOW): No contingency/management reserve.**
There is no management reserve or contingency line item. Standard practice for DoD proposals is 5-10% management reserve.

- **Recommendation:** Add a 7-10% management reserve line item to Phase 1-2 and Phase 3 budgets.

---

## 3. TIMELINE FEASIBILITY

### Strengths
- The 8-week prototype cadence with 2-week sprints is aggressive but achievable for the software layer, assuming hardware is available.
- The decision to use COTS hardware (per the Go/No-Go report) makes the timeline realistic for the software team.

### Issues and Recommendations

**ISSUE 3.1 (CRITICAL): Weeks 1-2 architecture finalization + CI/CD + dev environments is unrealistic if GovCloud is not already provisioned.**
GovCloud account provisioning alone can take 2-4 weeks due to organizational verification and compliance checks. If the team is starting from zero, they will not have a GovCloud staging environment until Week 4-6 at the earliest.

- **Recommendation:** The decision points table (Section 10) correctly identifies March 15 as the GovCloud provisioning deadline. However, the development roadmap should reflect that GovCloud will not be available for Weeks 1-4 of development. Explicitly state that Weeks 1-4 use local Docker Compose environments and that GovCloud staging comes online in Week 5-6. This is more credible and shows the team understands the real provisioning timeline.

**ISSUE 3.2 (HIGH): 30-unit deployment packages by Week 7-8 requires parallel hardware workstream not shown.**
The roadmap is software-only, but "30-unit deployment packages" at Week 7-8 implies hardware integration. If hardware is not available until Week 6 (a common scenario), that leaves only 2 weeks for hardware-software integration testing before Sword.

- **Recommendation:** Add a parallel hardware track (even if high-level) showing when dev hardware arrives, when 30-unit hardware is expected, and where the hardware-software integration window falls. Alternatively, add a dependency callout: "30-unit deployment contingent on hardware availability by Week 6; hardware partner milestone tracked separately."

**ISSUE 3.3 (HIGH): FDA 510(k) submission support in Months 4-6 of Phase 3 is extremely aggressive.**
FDA 510(k) submission for SaMD requires: (1) completed design controls per IEC 62304, (2) risk management file per ISO 14971, (3) software validation and verification evidence, (4) cybersecurity documentation per FDA premarket guidance, and (5) clinical validation data. Compressing this into 3 months while simultaneously maintaining the production software is not feasible with the stated team.

- **Recommendation:** Either extend the FDA timeline to Months 4-10, add dedicated regulatory engineering headcount (at least 1 FTE regulatory affairs specialist), or clarify that the consortium medical device partner owns the 510(k) submission and Veteran Vectors provides software documentation support only.

**ISSUE 3.4 (MEDIUM): IL-5 ATO in Months 6-8 overlapping with FDA submission is a resource conflict.**
Both the ATO package and FDA submission require extensive documentation from the same engineering team. The SSP (System Security Plan) alone for IL-5 is 200+ pages. Running these in parallel with a 5-person team is a staffing conflict.

- **Recommendation:** Stagger these workstreams or identify which consortium partner owns the ATO effort. If the cloud/cyber partner leads the ATO, state that explicitly and remove it as a Veteran Vectors deliverable.

---

## 4. SECURITY / COMPLIANCE

### Strengths
- The security architecture table (Section 8) covers the right categories: encryption at rest/transit, access control, audit logging, supply chain, and regulatory frameworks.
- FIPS 140-2 validated modules, TLS 1.3, CAC/PIV, and CycloneDX SBOM are all correct and current requirements.
- Mentioning Prisma Cloud for continuous monitoring shows awareness of container security requirements.

### Issues and Recommendations

**ISSUE 4.1 (HIGH): FIPS 140-2 should be FIPS 140-3.**
FIPS 140-2 was superseded by FIPS 140-3 as of September 22, 2021. NIST and DoD now require FIPS 140-3 validation for new systems. Citing FIPS 140-2 signals the team may be working from outdated compliance knowledge. While FIPS 140-2 validated modules remain acceptable during their validation period, a new system should target FIPS 140-3.

- **Recommendation:** Update all references to "FIPS 140-3 validated modules (or FIPS 140-2 modules within their active validation period)." This is a small change with significant credibility impact.

**ISSUE 4.2 (HIGH): BLE encryption is mentioned but not specified.**
Section 8 lists "BLE encryption" under Data in Transit, but BLE 4.x encryption (AES-CCM with 128-bit keys) has known vulnerabilities (KNOB attack, BLE pairing weaknesses). For a medical device handling PHI/PII in a military context, the BLE security model needs more detail.

- **Recommendation:** Specify BLE 5.0+ with LE Secure Connections (FIPS-compliant pairing), and note that BLE is used only for short-range sensor-to-edge communication where the threat model is limited to proximity attacks. If the threat model includes adversary proximity (which it does in a combat zone), discuss BLE frequency hopping and the operational security mitigations (e.g., short BLE range, encrypted payloads at the application layer above BLE).

**ISSUE 4.3 (MEDIUM): No mention of NIST SP 800-171 / CMMC.**
As a DoD contractor handling CUI (Controlled Unclassified Information -- which patient health data in a DoD context qualifies as), Veteran Vectors must comply with NIST SP 800-171 and the CMMC framework. This is a table-stakes compliance requirement that is absent from the document.

- **Recommendation:** Add a row to the Security & Compliance table: "CMMC / NIST 800-171: Veteran Vectors maintains CMMC Level 2 compliance; all CUI handling per NIST SP 800-171 Rev 2 controls." If the company does not yet have CMMC certification, flag it as a Phase 3 requirement.

**ISSUE 4.4 (MEDIUM): No mention of HIPAA / 32 CFR Part 199.**
Patient hemodynamic data is Protected Health Information (PHI). While DoD systems operate under 32 CFR Part 199 rather than HIPAA directly, the privacy protections are analogous. The document should address PHI handling.

- **Recommendation:** Add a row: "PHI Protection: Patient data handling compliant with DoD 6025.18-R (DoD Health Information Privacy Regulation) and aligned with HIPAA Security Rule controls."

**ISSUE 4.5 (LOW): No mention of STIG benchmarks for specific components.**
"STIG-hardened containers" is mentioned but which STIGs? Docker STIG? Kubernetes STIG? The DISA STIG for Container Platform?

- **Recommendation:** Specify: "Container hardening per DISA Container Platform SRG and Kubernetes STIG; OS images hardened per applicable DISA STIG (e.g., Ubuntu/RHEL STIG for edge devices)."

---

## 5. RISK COVERAGE

### Strengths
- The risk table identifies the top hardware-dependency risk and proposes a credible mitigation (hardware abstraction layer + simulators).
- The BATDOK and ATAK certification risks are real and appropriately called out.
- ML model fallback to rule-based TCCC scoring is an excellent mitigation.

### Issues and Recommendations

**ISSUE 5.1 (HIGH): Missing risk -- FDA SaMD classification risk.**
The triage classification output (Immediate/Delayed/Minimal/Expectant + recommended interventions) will likely be classified as FDA SaMD Class II, possibly Class III depending on the intended use claims. If the FDA classifies the AI as Class III (life-sustaining/life-supporting), the regulatory burden increases dramatically (PMA instead of 510(k)). This is a major programmatic risk not addressed.

- **Recommendation:** Add risk: "FDA SaMD Classification: Risk that AI triage output is classified as Class III SaMD requiring PMA rather than 510(k). Mitigation: Engage FDA Q-Submission (pre-submission) process in Phase 1 to obtain early classification guidance. Limit intended use claims to 'clinical decision support' (not autonomous diagnosis) to maintain Class II pathway."

**ISSUE 5.2 (HIGH): Missing risk -- Training data availability and quality.**
The model relies on MIMIC-III/IV, JTTR, and PhysioNet data. JTTR access requires formal DUA (Data Use Agreement) with the DoD Joint Trauma System, which can take 3-6 months. MIMIC-III/IV requires PhysioNet credentialed access. Neither dataset contains data from the specific sensor hardware proposed, creating a domain gap between training and deployment data.

- **Recommendation:** Add risk: "Training Data Access: DUA for JTTR may not be executed within prototype timeline. Mitigation: Begin DUA process immediately (Decision Point table); develop initial model on MIMIC/PhysioNet data; validate and fine-tune on JTTR data when available. Domain adaptation techniques to bridge training-deployment sensor gap."

**ISSUE 5.3 (MEDIUM): Missing risk -- Edge compute hardware selection.**
The document does not specify the actual edge compute hardware. If the team selects a device that cannot meet the <50ms inference target, or that has insufficient memory for the model + MQTT broker + local DB + ATAK plugin simultaneously, the architecture fails.

- **Recommendation:** Add risk: "Edge Compute Hardware Performance: Selected edge device may not meet simultaneous compute/memory/power requirements. Mitigation: Performance benchmarking on candidate hardware in Week 2; minimum requirements defined (ARM Cortex-A class, 4GB RAM, 32GB storage); fallback to dedicated inference co-processor if needed."

**ISSUE 5.4 (MEDIUM): Missing risk -- Consortium partner integration.**
The plan assigns all software components to "Veteran Vectors" with only "Device Firmware" assigned to "Hardware Partner." But the Go/No-Go report identifies cloud/cyber, manufacturing, and clinical SME partners. The risk that consortium partners fail to deliver (or fail to integrate) is not addressed.

- **Recommendation:** Add risk: "Consortium Integration: Delays or capability gaps from consortium partners impact software delivery. Mitigation: Formal interface control documents (ICDs) with each partner by Week 2; weekly consortium integration meetings; Veteran Vectors maintains capability to deliver core software independently of partner dependencies."

**ISSUE 5.5 (LOW): Risk impact/likelihood should include residual risk ratings.**
The risk table rates impact and likelihood but does not show residual risk after mitigation. This is standard practice in DoD risk management.

- **Recommendation:** Add a "Residual Risk" column showing the expected risk level after mitigation is applied.

---

## 6. DATA FLOW COMPLETENESS

### Strengths
- The three data flow diagrams (Real-Time Triage, DDIL Sync, Model Update) cover the primary operational scenarios.
- The DDIL sync flow correctly shows connected, disconnected, and reconnection modes with CRDT-based merge.
- The conflict resolution strategy (last-write-wins + clinical priority override) is thoughtful.

### Issues and Recommendations

**ISSUE 6.1 (HIGH): No data flow for multi-casualty / mass casualty scenario.**
The triage flow shows a single sensor-to-edge path. In a mass casualty event (the primary use case for triage classification), a single medic device may monitor 5-10+ casualties simultaneously. How does data flow when multiple BLE sensors are streaming to one edge device? How is triage priority displayed across multiple patients?

- **Recommendation:** Add a "Multi-Casualty Data Flow" diagram showing: multiple sensors -> BLE multiplexing on edge device -> parallel inference -> prioritized triage dashboard. Address BLE connection limits (typical max 7-10 simultaneous BLE connections) and how mesh networking handles overflow.

**ISSUE 6.2 (MEDIUM): Model Update Flow lacks rollback mechanism.**
The canary deploy -> validate -> promote path is good, but there is no rollback path shown. What happens if the canary deployment fails validation? In a medical device context, model rollback is an FDA-auditable event.

- **Recommendation:** Add a rollback path: "Canary Deploy -> Validate -> IF FAIL: Rollback to previous validated model version + alert MLOps team + log event for FDA audit trail. Rollback must complete within 30 seconds with zero patient monitoring interruption."

**ISSUE 6.3 (MEDIUM): No data flow for EHR synchronization.**
Section 2.2 mentions bidirectional EHR sync with TMIP/MHS GENESIS, but no data flow diagram shows this. EHR integration is a major evaluator criterion and deserves its own flow.

- **Recommendation:** Add an "EHR Synchronization Data Flow" diagram showing: Edge patient record -> cloud sync -> FHIR R4 translation -> MHS GENESIS API -> confirmation/conflict resolution. Show the bidirectional path (pulling patient history from EHR to the edge for pre-existing conditions).

**ISSUE 6.4 (LOW): Data flow diagrams should indicate data classification levels.**
For an IL-5 system, evaluators will want to see where data transitions between classification boundaries (e.g., unclassified sensor data vs. CUI patient data vs. IL-5 aggregate data).

- **Recommendation:** Annotate data flow diagrams with data classification labels at each stage (e.g., "CUI//PHII" for patient health data, "U//FOUO" for aggregate non-identified data).

---

## 7. MISSING ELEMENTS

The following items are absent from the document and should be addressed before submission:

**MISSING 7.1 (CRITICAL): Software Test Strategy.**
There is no test plan or test strategy section. For a medical device software system, this is a glaring omission. DIU evaluators and FDA reviewers alike will expect to see:
- Unit test coverage targets (e.g., >90% code coverage for safety-critical modules)
- Integration test approach (edge-to-cloud, sensor-to-BATDOK)
- System test / acceptance test criteria
- Clinical validation test protocol (sensitivity/specificity against labeled trauma data)
- Regression test strategy for model updates

**Recommendation:** Add a Section 7.5 or new Section 11: "Verification & Validation Strategy" covering all test levels and referencing IEC 62304 software testing requirements.

**MISSING 7.2 (HIGH): Configuration Management Plan.**
No mention of software configuration management, version control strategy, branch management, or release engineering. For FDA SaMD, configuration management is a mandatory design control per IEC 62304.

**Recommendation:** Add a subsection under Section 5 addressing: Git branching strategy, release versioning (semantic versioning), software build identification on deployed devices, and traceability from requirements to code to tests.

**MISSING 7.3 (HIGH): Interoperability Testing with BATDOK/ATAK.**
The plan mentions BATDOK and ATAK integration but provides no detail on how interoperability will be validated. BATDOK and ATAK have specific conformance requirements, and TAK Product Center has a plugin certification process.

**Recommendation:** Add detail on: (1) BATDOK conformance testing approach, (2) TAK Product Center plugin certification timeline and requirements, (3) planned interoperability events or testing with government reference implementations.

**MISSING 7.4 (MEDIUM): User Training / Operator Documentation.**
The system will be used by 68W combat medics. There is no mention of user training materials, operator manuals, or IETMs (Interactive Electronic Technical Manuals). These are standard DoD deliverables.

**Recommendation:** Add a line item for user documentation and training materials in Phase 2 deliverables, even if it is a brief operator quick-start guide for the Sword demo.

**MISSING 7.5 (MEDIUM): Accessibility / Section 508 Compliance.**
The cloud analytics dashboard and provider portal are web-based and subject to Section 508 accessibility requirements for DoD systems.

**Recommendation:** Add a note that the provider dashboard will comply with Section 508 / WCAG 2.1 AA standards.

**MISSING 7.6 (MEDIUM): Data Retention and Disposal Policy.**
Patient health data has retention requirements under DoD policy. The document does not address how long data is retained on edge devices, when it is purged, or how device decommissioning handles data sanitization.

**Recommendation:** Add a brief data lifecycle paragraph: retention periods, edge device data purge on cloud sync confirmation, and NIST SP 800-88 media sanitization for device decommissioning.

**MISSING 7.7 (LOW): Performance Requirements / SLAs.**
Beyond the <50ms inference latency target, there are no defined performance requirements: maximum BLE latency, data sync latency, dashboard refresh rate, cloud API response time, system availability targets.

**Recommendation:** Add a Performance Requirements table with quantified targets for each tier.

---

## 8. PROFESSIONAL QUALITY

### Strengths
- The document is well-structured with clear section numbering and consistent formatting.
- Tables are used effectively for cost breakdowns, component descriptions, and risk matrices.
- ASCII architecture diagrams are readable and appropriate for a markdown document.
- The writing is clear, concise, and avoids unnecessary jargon while using correct DoD/medical terminology.
- Cross-references between this document and the White Paper are consistent.

### Issues and Recommendations

**ISSUE 8.1 (MEDIUM): No document control metadata.**
The document lacks version number, revision history, classification marking, and distribution statement. The White Paper includes a distribution statement but this document does not.

- **Recommendation:** Add a document header with: Version (e.g., "v1.0 DRAFT"), Date, Classification (e.g., "CUI" or "UNCLASSIFIED"), Distribution Statement, and Revision History table.

**ISSUE 8.2 (LOW): Section 7 heading says "DATA FLOW DIAGRAMS" but should be more descriptive.**
The data flow section is functional but could benefit from brief narrative descriptions above each diagram explaining the operational scenario depicted.

- **Recommendation:** Add 1-2 sentences of context above each data flow diagram (e.g., "The following diagram depicts the data flow during a typical single-casualty triage event at a Role 1 medical treatment facility...").

**ISSUE 8.3 (LOW): Inconsistent use of "Veteran Vectors" vs. implied consortium ownership.**
The Component Breakdown (Section 2.2) assigns almost everything to "Veteran Vectors" but the overall proposal is from the "Authentic Consortium." Clarify whether Veteran Vectors is the sole software developer or if consortium partners contribute to specific software components.

- **Recommendation:** If all software is Veteran Vectors, state that explicitly: "All software components developed by Veteran Vectors as consortium prime; hardware firmware developed by [Hardware Partner]." This removes ambiguity about consortium roles.

---

## SUMMARY OF PRIORITY RECOMMENDATIONS

### Must-Fix Before Submission (Critical/High)

| # | Issue | Section | Action |
|---|---|---|---|
| 1 | Add Software Test/V&V Strategy | New Section | Add verification & validation section covering all test levels |
| 2 | Fix FIPS 140-2 -> FIPS 140-3 | Section 8 | Update all FIPS references |
| 3 | Add FDA SaMD classification risk | Section 9 | Add risk + Q-Submission mitigation |
| 4 | Add training data availability risk | Section 9 | Add risk + DUA timeline mitigation |
| 5 | Clarify Python/C++ split on edge | Section 2.2 | Specify C++ for inference, Python for dev/test only |
| 6 | Add multi-casualty data flow | Section 7 | New diagram for mass casualty scenario |
| 7 | Increase labor rates or clarify as fully-burdened | Section 6.1 | Add footnote or adjust rates |
| 8 | Increase ATAK/BATDOK developer hours | Section 6.1 | Increase to 1.0 FTE or scope alpha-only |
| 9 | Add CMMC/NIST 800-171 compliance | Section 8 | Add row to compliance table |
| 10 | Add PHI/DoD health privacy compliance | Section 8 | Add row to compliance table |
| 11 | Fix ONNX Runtime vs. TF Lite inconsistency | Section 5.1 | Standardize on one inference runtime |
| 12 | Address GovCloud provisioning timeline reality | Section 4 | Adjust Weeks 1-2 milestones |

### Should-Fix (Medium Priority)

| # | Issue | Section | Action |
|---|---|---|---|
| 13 | Add configuration management plan | Section 5 | New subsection |
| 14 | Add BATDOK/ATAK interoperability test plan | Section 4 or new | Detail conformance testing |
| 15 | Add model rollback mechanism to data flow | Section 7.3 | Update diagram |
| 16 | Add EHR sync data flow diagram | Section 7 | New diagram |
| 17 | Simplify edge database to SQLite-only | Section 2.2, 5.1 | Remove TimescaleDB from edge |
| 18 | Add management reserve to budget | Section 6 | Add 7-10% contingency |
| 19 | Add BLE security detail | Section 8 | Specify BLE 5.0+ security model |
| 20 | Increase Phase 3 budget or clarify partner cost-sharing | Section 6.2 | Adjust to $1.8M-$2.2M or add partner note |
| 21 | Add user training/documentation deliverable | Section 4 | Add to Phase 2 deliverables |
| 22 | Add document control metadata | Header | Version, classification, distribution |

### Nice-to-Have (Low Priority)

| # | Issue | Section | Action |
|---|---|---|---|
| 23 | Add data classification labels to flow diagrams | Section 7 | Annotate CUI/PHII boundaries |
| 24 | Add performance requirements table | New subsection | Quantified targets per tier |
| 25 | Specify applicable DISA STIGs | Section 8 | List specific STIG IDs |
| 26 | Add Section 508 compliance note | Section 5 or 8 | Note for web dashboard |
| 27 | Add residual risk column | Section 9 | Enhance risk table |
| 28 | Add data retention/disposal policy | Section 8 | Brief data lifecycle paragraph |
| 29 | Add narrative context to data flow diagrams | Section 7 | 1-2 sentences per diagram |
| 30 | Defer K3s to Phase 3 | Section 2.2, 5.1 | Simplify prototype deployment |

---

## CONCLUSION

This Software Action Plan is a strong foundation for the DIU PROJ00628 submission. The architecture is sound, the AI/ML strategy is credible, and the DDIL-native approach is the right design philosophy. However, the document needs revision in three key areas before it will be fully competitive:

1. **Compliance completeness:** Add FIPS 140-3, CMMC, PHI protections, and Section 508. Fix the BLE security gap. These are checkbox items that evaluators will scan for.
2. **Programmatic realism:** Adjust labor rates, expand ATAK/BATDOK scoping, add management reserve, and stagger the FDA/ATO timelines to reflect real-world durations.
3. **Missing sections:** A V&V strategy and configuration management plan are mandatory for any medical device software proposal. Their absence is the single largest weakness in the current draft.

With these revisions, the proposal should score well on Technical Feasibility and System Effectiveness -- the two heaviest-weighted evaluation criteria for DIU prototype challenges.

---

*Review prepared for Veteran Vectors / Authentic Consortium internal use. Not for distribution to government evaluators.*
