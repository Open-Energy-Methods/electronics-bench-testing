# Change log

## 1.0 — 2026-11-05
- Established programme charter and fixed initial research direction without locking future technical revisions.
- Retained EBT-R01 v0.1 feasibility source and seven passing tests.
- Defined Q0, MET-001 and R01 campaigns, 54-row *provisional* design, cross-boundary holdouts, stage gates, standards/novelty limits, safety and metrology policies.
- Added machine-readable requirements, risk, standards, literature, instrument, budget, access, decision, change and work registers; editable document templates.
- No facility authorization, physical measurement, peer-reviewed finding or KTH affiliation claimed.

## Work package v0.2 — 2026-11-05 (PR candidate; not a replacement for PMP v1.0)
- Screened TO-220 reference heater candidates and documented conditional power/derating and separate semiconductor SOA gates.
- Added unpowered protected-bench block architecture, sensor placement and grounding hazards; a complete approved schematic is still outstanding.
- Prepared preliminary 12-row Q0 pilot planning design (P1/P2 remain undefined) with three automated checks and CI workflow.
- Added targeted prior-art differentiation matrix; no full systematic review or novel-paper claim yet.
- Updated facility-access tracker with Mykola Ivchenko's Student Workshop eligibility response; Canvas/induction and energized ELAB permission remain pending.

## Research work package v0.3 — 2026-11-05
- Completed source-graded **critical full-text literature pass**: five primary full-text research articles and the KTH doctoral-thesis summary; eight additional abstract/record-only sources with explicit access blockers.
- Added EBT-LIT-003 critical review, 14-record evidence matrix, dated search/access audit and guarded research-gap decision.
- Revised proposed manuscript emphasis toward **prospective transient boundary-transfer assessment**, with independently acquired boundary inputs, true remount holdouts, and accessible measured surface temperatures. The master plan v1.0 remains unchanged.
- Research novelty is **not established**; G1 remains open pending full-text competition review, broader scholarly database screening and external methodological critique.
- Added offline literature register checks for provenance and source-grade consistency.

## Model work package v0.4 — 2026-11-05
- Developed runnable B0/B1/B2/B3 synthetic model comparisons and package-only identifiability ablation, retaining unmodified v0.1 baseline.
- Distinguished natural-cooling training, separate sink-injection boundary qualification and entire held-out cooling/remount scenarios; tested deliberate validation-response corruption.
- Tested energy balance, exact-ZOH solver, error propagation with covariance, measurement-information asymmetry and boundary transport counterexamples.
- Exposed 4.84-second synthetic fast mode under-sampling at 20-second measurement interval, and failures caused by parallel heat paths and mismatched boundary geometry.
- Report remains **synthetic only**. No actual physical tests, calibrated boundaries, qualified junction temperatures or novelty determination.

## Engineering work package v0.5 — 2026-11-05
- Produced unpowered preliminary mechanical plan/section and editable design-coordinate DXF, with manufacturer-versus-assumed dimensions explicitly separated; **not manufacturing released**.
- Produced the heater-selector/current-measurement preliminary electrical topology, connection-level net ledger, detailed grounding and protection blockers, and channel/uncertainty requirements; **not an approved circuit**.
- Quoted exact Bourns PWR220T-20-10R0F (x2) and Fischer SK 92 100 SA (x1) from Swedish distributor snapshots; **346.58 SEK ex VAT covers only these three pieces**; the other 14 BOM lines remain unpriced or site-dependent.
- Archived v0.4 synthetic JSON/PNG output snapshots with hashes; baseline v0.1 remains unchanged. Preserved whole-repository boilerplate/representative-data audit and created current source hierarchy. Historic v1.0 manifest and QA report are retained as snapshots, not current summaries.
- Added six offline integrity tests to GitHub Actions, covering data classification, no false calibration claims, circuit net coverage, vector geometry and partial BOM arithmetic.
- Formal G1 novelty, G2 energized facility authorization, G3 physical experiment and hardware manufacturing release remain blocked.

## Spatial model work package v0.6 — 2026-11-05 (integrated from PR #11)
- Added hypothetical 2-D steady plate source/sensor transfer tests with numerical conservation/symmetry/record checks. Spatial heat loss coefficients, 1 W normalization and effective transfer differences remain synthetic, never manufacturer or physical validation.

## Physical readiness v0.7 — 2026-11-05 (integrated from PR #12)
- Added source-graded SK 92 manufacturer-family base thickness (nominal 10 mm) and conditional direct-to-sink versus assumed 4 mm adapter plate architecture; 97.2 J/K plate value only under generic assumed aluminium properties.
- Added 23-point inspection register, separate workshop/powered authority, blank G2-G3 gate, Q0 source/site pilot alternative, and explicit no-permission software checks.

## Acquisition integrity v0.8 — 2026-11-05 (integrated from PR #13)
- Added prospective raw CSV/metadata contract, create-once SHA-256 sealing, retained aborts/quality flags, source/cooling and remount identities, and partition/lock validation with synthetic-only test generator. External pre-registration chronology and physical provenance are not authenticated by code.
- Updated facility correspondence status for Student Workshop invitation and Manufacturing Lab restrictions; powered ELAB access still absent.

## Unified Q0 v0.9 — 2026-11-05 (integration review)
- Consolidated PRs #11–#13 with all source-code modules preserved and eight distinct GitHub Actions jobs.
- Established 14_q0_integrated_v0.9 as the single Q0 review entry point; reconciled 12-run vs 8-event **alternative** pilot sketches and \`T_plate\` vs \`T_sink\` sensor labels.
- Defined exact v0.7 EBT-GATE-007 ↔ v0.8 EBT-SPLIT-008 lock/hash/role mapping; added cross-module integrity checks and intentionally incomplete future-acquisition templates.
- Remaining G1 novelty, G2 machining/power authority, G3 real metrology, Q0 physical pilot and R01 validation remain **HOLD / NOT COMPLETED**.

## Catalog/source & unpowered intake Q0-010 — 2026-11-05 (limited remote stage)
- Reviewed exact Bourns 10R0F datasheet and 2025 resistor thermal-management application note; distinguished 20 W at 25°C case from 2.8 W without heatsink. Neither is an EBT operating limit.
- Cross-checked catalog thermal resistance inconsistency for SK 92 100 SA (Farnell, TME, DigiKey); expressly rejected fitting distributor figures as a measured cooling boundary.
- Added **unfilled** part receiving and instrument inspection records with four guardrail tests. No received parts, real measurements, booked workshop introduction, authorized powered lab or physical test are claimed.
