# ELECTRONICS BENCH TESTING
## Master Research, Engineering & Test Programme Plan

**Controlled baseline:** EBT-PMP-001 / Revision 1.0 / 05 November 2026  
**Status:** ACTIVE PLANNING BASELINE — research proposal and physical test procedures remain preliminary.  
**Principal researcher:** Abhijith Sivaprasadan · ORCID 0000-0003-0299-5745  
**Research identity:** Open Electrothermal Bench (working title)  
**Institutional status:** Independent research. Not a KTH-sponsored or degree-awarding thesis; no laboratory accreditation or physical testing authorization is asserted.  
**Companion baseline:** EBT-R01 computational feasibility package v0.1 (retained unmodified in `07_source_baseline/`).

## Contents

- [1. Executive mandate and project boundaries](#s1)
- [2. Scientific thesis definition](#s2)
- [3. Existing verified baseline and evidence maturity](#s3)
- [4. Literature review and standards research plan](#s4)
- [5. Engineering requirements and traceability](#s5)
- [6. Physical bench system architecture](#s6)
- [7. Test campaign plan](#s7)
- [8. Design of experiments and statistical analysis plan](#s8)
- [9. Verification, validation and model governance](#s9)
- [10. Measurement uncertainty and calibration policy](#s10)
- [11. Safety, facility governance and ethics](#s11)
- [12. Data architecture and open reproducibility](#s12)
- [13. Work breakdown structure (WBS) and ownership](#s13)
- [14. Schedule, constraints and dependencies](#s14)
- [15. Budget, procurement and equipment strategy](#s15)
- [16. Risk management and contingency](#s16)
- [17. Stage-gate governance: measurable readiness](#s17)
- [18. Scientific manuscript strategy](#s18)
- [19. Outreach and professional translation](#s19)
- [20. Configuration and change management](#s20)
- [21. Next 14-day execution order](#s21)
- [22. Core references and provenance](#s22)

> **Decision:** This document defines the programme. New observations, facility constraints and literature findings shall be handled through controlled revisions and change requests. Work should now advance along the plan rather than repeatedly redefine the entire project.

# 1. Executive mandate and project boundaries {#s1}

## 1.1 Mission

Develop and publicly document a **thesis-level, reproducible engineering investigation** of the measurement and prediction of electrothermal behaviour in power-electronic cooling assemblies. Produce credible experimental evidence, transparent numerical models, explicit uncertainty accounting, and a journal- or conference-submittable manuscript if the evidence and contribution support it. Build a demonstrable career portfolio in thermal electronics, power electronics test and validation, reliability and computational heat transfer.

## 1.2 End-state definition

A successful programme delivers: (a) a controlled research question and documented prior-art gap; (b) a qualified measurement system and safe, permitted experimental rig; (c) a physical dataset with genuinely independent runs and held-out conditions; (d) reproducible models with numerical verification; (e) calibrated/verified measurement evidence and explicit uncertainty; (f) a defensible comparative analysis; (g) an open research release with raw-to-figure reproduction; and (h) a complete scientific manuscript and employer-facing case study. **Peer-reviewed acceptance is a stretch outcome, not guaranteed.**

## 1.3 Programmes, campaigns and hierarchy

| Identifier | Work item | Position | Evidence product |
|---|---|---|---|
| EBT-P | Programme management and research quality | Governing baseline | Master plan, requirements, controlled decisions |
| EBT-Q0 | Laboratory capability and safe bench qualification | Mandatory enabling campaign | Equipment inventory, test-site permission, pilot, uncertainties |
| EBT-MET-001 | Measurement assurance | Cross-cutting campaign | Reference chain, verification/calibration records, uncertainty budgets |
| EBT-R01 | Primary flagship study: electrothermal model transfer | Thesis-equivalent research | Open benchmark, comparisons, report, manuscript |
| EBT-R02+ | Future studies (converters / packaging / reliability) | Not committed | Require separate concept and resource approval |

## 1.4 Fixed scope and explicit exclusions

**In scope:** low-voltage isolated DC heating and MOSFET operation within verified datasheet safe operating area; resistive control heater; safe cooling assemblies; contact and supplementary IR surface thermometry; electrical loss measurement; repeatable mechanical fixture; measured environmental conditions; compact thermal network and optional spatial simulation; analysis reproducibility and independent holdouts.

**Not initially in scope:** mains-connected experiments, high-energy batteries, high-voltage converters, destructive device stress, unattended energized experiments, full reliability/lifetime qualification, thermal shock or TVAC testing, JEDEC compliance claims, proprietary KTH facility documentation, formal ISO/IEC 17025 accreditation, or direct semiconductor junction-temperature measurement absent a validated junction-sensitive method.

**Crucial boundary:** measured package/case temperature is **not** measured junction temperature. Inferring an unobserved internal state requires a model with quantified uncertainty or an independently validated junction-sensitive method.

# 2. Scientific thesis definition {#s2}

## 2.1 Working title and problem statement

**Working paper title:** *When Surface Temperatures Mislead: Observability and Cross-Boundary Validation of Compact Electrothermal Models for Low-Voltage Power-Electronics Cooling.*

**Problem:** A thermal model may match an observed package temperature without identifying the internal thermal pathway, and a model identified under one cooling or mounting condition may be unreliable when transferred to another. The literature already recognizes parameter non-identifiability and thermal-transient measurement problems; the programme must therefore investigate a specific open, independently checkable experiment and assess whether it adds sufficiently differentiated evidence or methodology.

## 2.2 Research questions and hypotheses

| ID | Research question | Predeclared testable hypothesis | Primary evidence |
|---|---|---|---|
| RQ1 / H1 | Which surface/boundary measurements discriminate alternative internal thermal pathways? | Package-only signals can be insufficient to distinguish materially different hidden thermal states within the measurement uncertainty. | Model sensitivity, profile likelihood / identifiability analysis; junction-sensitive comparison only if qualified |
| RQ2 / H2 | Does an independently characterized cooling boundary improve prediction transfer? | Boundary-aware predictions improve over a fixed-boundary baseline on complete held-out cooling configurations. | Separate physical cooling condition; holdout prediction error and uncertainty |
| RQ3 / H3 | How much variation arises from remounting and interface changes? | Assembly variability materially contributes to measured thermal behaviour and predictive error. | Independent reassemblies, randomized/blocked tests, variance components |

These are **hypotheses** rather than conclusions. Direction may change through a documented scientific change request if new literature or pilot feasibility invalidates the premise. A null or negative result is acceptable if adequately measured and interpreted.

## 2.3 Claimed and unclaimed contribution

**Plausible contribution to test:** a low-voltage, open, uncertainty-qualified benchmark that combines (i) measurement observability, (ii) independent cooling-boundary transfer, (iii) mechanical reassembly variation, and (iv) transparent holdout evaluation within one controlled experimental framework. Methodological novelty is not established.

**Do not claim:** first use of Cauer networks; first observation of parameter identifiability limits; original use of SVD/DoE; direct junction thermal validation from a case sensor; compliance with JEDEC standards; device reliability/lifetime qualification; external peer review; KTH affiliation or sponsorship.

## 2.4 Research novelty decision

The core manuscript may be framed as (A) a methodological experimental paper, (B) an open benchmark/data-plus-validation paper, or (C) a technical report if novelty/measurement depth is inadequate. **Gate G1** requires a full-text comparison against directly competing papers and explicit statement of what is not already established. This is a gate for *claims and manuscript strategy*, not a reason to stop safe preliminary analytical work.

# 3. Existing verified baseline and evidence maturity {#s3}

The prior EBT-R01 v0.1 repository is the computational feasibility baseline and must not be quietly overwritten. It contains a three-node energy-conserving synthetic thermal-network model, seven automated tests, fixed-seed outputs, case-only fitting, an independent synthetic forced-cooling holdout, CSV/JSON outputs and four figures. Tests were re-run on 05 November 2026 and passed 7/7.

| Evidence class | Current status | Permitted language |
|---|---|---|
| Synthetic model / code | Implemented and automated tests pass | ‘Numerically verified synthetic demonstration’ |
| Synthetic example | Assumed 0.15°C package noise; example junction difference approximately 3.75°C vs package difference approximately 0.104°C | ‘Model-defined illustrative case, not hardware evidence’ |
| Synthetic holdout | Fixed-boundary RMSE approximately 6.79°C; supplied-boundary example approximately 0.57°C | ‘Model-to-model result with independently specified synthetic boundary’ |
| Instrument and test rig | No facility inspection or permission documented | ‘Planned’ |
| Experimental dataset | None yet | Never describe synthetic data as measurement |
| External scientific novelty | Not established | ‘Candidate contribution under review’ |
| Academic collaboration / publication | Not established | ‘Independent, proposed’ |

Numerical code passing energy conservation and convergence checks does **not** verify the physical model. The headline synthetic values should only appear with qualifiers and provenance. The reference is `07_source_baseline/EBT_R01_Feasibility_v0.1/`.

# 4. Literature review and standards research plan {#s4}

## 4.1 Targeted prior-art landscape

The v0.1 scoping review identifies direct overlap with Putthong, Lu & Lee (2026; information sufficiency and experiment design), Schulz et al. (2026; Cauer thermal-network identifiability), Zhang et al. (2024; thermal transient estimation), Cnudde et al. (2026; experimental thermal model validation), and KTH semiconductor cooling research. **These references have not all been screened in full text.** The master literature register records retrieval, verification, overlap and implications; review status shall be upgraded only after reading actual papers.

## 4.2 Review protocol

Search IEEE Xplore, Scopus/Web of Science when accessible, KTH DiVA, publisher sites and relevant conference proceedings. Keep search date, database, query, inclusion/exclusion, DOI, title, methodology, DUT, sensors, boundary methods, raw data availability, uncertainty method, holdout design, limitations and direct overlap. Use backward/forward citation screening. Summarize at least 15–25 central papers before choosing a manuscript-specific novelty claim; this is a **planning target** and not proof of completeness. Record non-public full-text access as ‘not obtained’ rather than inventing details.

## 4.3 Normative reference policy

The standard names below identify relevant source documents. They are **not blanket legal requirements**, evidence of acquired normative text, or claims of conformity. Obtain official applicable editions, check scope, and register whether each procedure is ‘informative’, ‘adapted’, ‘fully applied’, or ‘not applicable’ before testing. Do not redistribute copyrighted standards.

| Reference | Intended use | Applicability decision |
|---|---|---|
| ISO/IEC 17025:2017 | Competence, records, traceability and quality principles | Informative independent-lab framework; not accredited |
| JCGM 100:2008 + Amendment 1:2026; JCGM 101:2008 | Type A/B uncertainties, propagation and Monte Carlo checks | Core methodological guidance |
| ASME V&V 20-2009 (R2021) | Validation-point uncertainty framing for CFD/heat-transfer simulation | Methodological reference; formal application subject to actual numerical study |
| JEDEC JESD51 family; JESD51-14 if applicable | Semiconductor thermal characterization, junction-to-case terminology, qualified methods | Scope review required; not compliant by default |
| IEC 61010-1:2010 + AMD1:2016 | Safety context for laboratory/measurement equipment | Equipment scope reference, not new-equipment certification by project |
| IPC-2152 | PCB current carrying and conductor-temperature rise, if project includes designed PCB | Conditional, not applicable to initial fixture absent PCB design |

# 5. Engineering requirements and traceability {#s5}

Each requirement receives a unique identifier and verification method in `08_project_controls/requirements_register.csv`. Requirement status is NOT assumed satisfied because text exists. Demonstration = data/script; Inspection = documented observation; Analysis = derivation/review; Test = approved empirical test.

**Priority requirement families:** publication integrity; user/operator safety; metrological suitability; independent repeatability; traceable DUT and fixture definition; data provenance; numerical correctness; predictive holdout; limitations; independent reproducibility. The traceability register connects each RQ and claimed finding to a measurement, analysis and release artifact.

## 5.1 Quantitative acceptance criteria: how they will be set

Do not prematurely set ‘model must be within 5%’ or ‘temperature calibration ±0.2°C’. During EBT-Q0, use pilot measurements and design margins to justify electrical power uncertainty, steady-state definition, timestamp alignment, thermal stability and minimum detectable effects. These criteria are to be **approved and preregistered before confirmatory data acquisition**. Analytical pipeline tests may have deterministic numeric tolerances now; empirical acceptance limits require actual instrument ranges and DUT design.

# 6. Physical bench system architecture {#s6}

## 6.1 Functional block chain

Isolated current-limited DC source → protection / disconnect → DUT electrical measurement → qualified low-voltage resistive heater or MOSFET assembly → heat sink / interface / defined airflow → ambient. Parallel instrumentation records synchronized voltage and current, package/case and sink temperatures, ambient temperature and fan conditions. Raw acquisition files are copied to immutable custody storage; scripted processing creates calibrated quantities, uncertainty estimates and model comparisons.

## 6.2 Hardware and measurement specification

| Subsystem | Required design evidence | Must be decided from actual equipment |
|---|---|---|
| Source/protection | voltage/current limits, energy/power margins, fuse/limit/switch-off, wiring capacity | supply model, isolated output, current limit and safe set points |
| Resistive reference heater | rating and geometry, contact mechanics and temperature limits | actual resistor/fixture and surface measurement locations |
| MOSFET DUT | manufacturer part and datasheet, SOA, on-resistance and losses, package mounting | operating point, pulse/waveform, thermal margin |
| Electrical metrology | four-wire/sense where appropriate, current shunt/probe, synchronized V·I | accuracy, bandwidth, reference status |
| Thermal metrology | defined sensor positions, attachment/lag, reference ambient | thermocouple/RTD type, logger and calibration chain |
| IR imaging (optional) | emissivity/reference target, spatial calibration, reflected-temperature control | instrument and method availability |
| Cooling and interface | heater/heat-sink geometry, torque/mount record, fan boundary | fan monitoring and boundary characterization |
| Data system | timestamp, acquisition metadata, failure detection, backup | logging hardware/software and permitted interfaces |

No hardware purchase is authorized by this plan. The preliminary bill of materials is a procurement planning document until facility inventory, costs, and protection design are known.

## 6.3 Physical temperature terminology

Define `T_case,measured` as temperature at an explicitly documented sensor location; `T_sink` at a marked sink location; `T_ambient` at a position shielded from direct fixture heating; and `T_junction,inferred` as a model quantity only. If a validated temperature-sensitive electrical parameter or equivalent qualified method becomes feasible, create a separate protocol and uncertainty study before introducing observed junction estimates.

# 7. Test campaign plan {#s7}

## 7.1 EBT-Q0: bench commissioning and pilot

**Q0-A:** facility authorization, safety induction, bench reservation rules, allowed heat loads and public-data permissions; sign off site-specific rules. **Q0-B:** inventory equipment by manufacturer/model/serial, operating condition, calibration evidence, and suitable measurement ranges. **Q0-C:** unpowered wiring inspection, continuity and polarity check, protective components. **Q0-D:** verify temperature channels over the intended range against acceptable reference with error/uncertainty statement; electrical channels against suitably qualified references. **Q0-E:** run protected resistive-heater pilot; measure temperature rise and dissipation; characterize sensor lag, ambient drift and safe stopping. **Q0-F:** perform at least three *independent* assembly/measurement cycles if feasible and estimate variance before locking main design.

Completion evidence: authorized rig description, controlled schematic, instrument register, reference-chain records, safety approval, pilot run files, uncertainty estimate, risk reassessment, preliminary sample-size calculation, and revised campaign acceptance criteria. If the facility forbids energized tests, EBT-Q0 cannot be passed there.

## 7.2 EBT-MET-001: measurement assurance

Maintain channel-specific measurement equations, corrections, dependencies and uncertainty sources. Basic equation for dissipated electrical power under quasi-DC conditions is `P = V·I`, with appropriate correlated voltage/current uncertainty treatment. For switching waveforms, synchronized `P_avg = mean(v(t)·i(t))` replaces `mean(v)·mean(i)` where necessary. Estimate Type A repeatability and Type B calibration/accuracy components and report expanded uncertainty with declared coverage factor and assumptions. Prevent invalid ‘traceability’ claims: agreement between unknown meters is only a comparison.

Each thermocouple channel needs sensor ID, connection type, cold-junction handling, placement photo/drawing, temperature range, reference evidence, sample interval and time response. A contact-reference comparison is not by itself a complete thermal-camera radiometric calibration.

## 7.3 EBT-R01: main physical experiment

**Planning envelope only:** 3 approved dissipated-power levels (P1–P3); 3 cooling configurations (NAT, PASS, FORCED); 2 mounting/interface configurations (A, B); and 3 independent remounts per configuration → **54 candidate runs**. The companion `03_campaigns/EBT-R01/provisional_run_matrix.csv` enumerates the factorial. Exact wattages, randomization, repeated-measures structure, stabilization and number of runs are TBD after pilot and design-efficiency analysis. This is **not authorization to run**.

Run phases: precondition/cool-down to controlled baseline; unpowered inspection; instrument self-check; powered thermal rise; fixed-duration or stability-based hold (criterion preregistered); safe switch-off; monitored cool-down; independent reassembly. Record failed/aborted tests without deletion. No analysis-informed cherry-picking.

**Predictive split:** calibration data, diagnostic exploration data and sealed confirmatory holdout data must be partitioned at the assembly/configuration level, not using random time points from the same transient. A baseline model may use only natural-cooling reference assemblies; at least one entire forced-cooling condition and one reassembly/interface condition remain sequestered for the primary transfer claims. The final split is committed before confirmatory acquisition, and any changes are documented.

**Primary response set:** temperature versus time for package/sink/ambient, directly measured dissipated power, steady-state normalized temperature rise, model prediction errors on independent cases, confidence/prediction interval coverage, measurement uncertainty and remount variance. **Secondary:** time constants, simulated heat-balance residual, compute cost and sensor-position sensitivity.

## 7.4 Incomplete equipment / no junction measurement fallback

If no junction-sensitive reference is feasible, RQ1 is a model-identifiability and surface-observability study, not experimentally measured junction accuracy. If variable cooling is unavailable, prioritize a rigorously replicated interface/mounting dataset with a narrower manuscript. If no powered bench is permitted, continue computational development and publish only a computational report; do **not** claim a completed experimental thesis or submit a paper predicated on hardware validation.

# 8. Design of experiments and statistical analysis plan {#s8}

## 8.1 Experimental unit and replication

The independent experimental unit is a distinct assembly/remount under an independently executed thermal cycle as defined in the protocol. High-frequency timestamps within one cycle are repeated observations, not independent replicates. Where a heatsink and fixture are shared, treat any block effects appropriately. Randomize or block configuration order according to practical cooldown and tool-change requirements; preserve ordering to diagnose drift.

## 8.2 Pilot-driven sizing and stopping

Estimate effective temperature noise, remount standard deviation, ambient drift, stabilized thermal resistance variability and run duration. Choose run count based on the smallest industrially meaningful detectable difference and target confidence/precision, with explicit assumptions. A minimum of three replicates is a pilot planning default, not a universal statistically adequate sample size. Define temperature/power trip criteria, facility stop rules, failure classifications and missing-data thresholds before confirmatory testing.

## 8.3 Analysis strategy

Use (a) physical inspection and sensor plausibility; (b) clean, audit-preserving data transformation; (c) direct thermal/electrical measurements and uncertainty; (d) parsimonious analytical baseline; (e) candidate multi-node RC models selected by predeclared rules; (f) optional 3D conduction or CFD with mesh/time-step verification and measured boundaries; (g) held-out RMSE/MAE/bias and interval coverage; (h) grouped uncertainty and sensitivity analysis. Report effect sizes and uncertainty rather than relying on p-values alone. For model complexity, document identifiability and penalize unnecessary parameters.

# 9. Verification, validation and model governance {#s9}

The model and test facility must be audited independently. The existing synthetic model has seven passing solver tests, but requires additional parameter sensitivity, robustness, missing data, uncertainty propagation and boundary-estimation tests prior to a publishable pipeline.

**Verification questions:** Are equations correctly implemented? Are units and energy balance correct? Are results independent of integration resolution within declared tolerances? Are input data and reported plots reproducible bitwise or within numeric tolerance? **Validation questions:** Does the model accurately predict **measured variables at specified conditions** when uncertainty is considered? Is the comparison genuinely independent of parameter fitting? What changed under a new cooling configuration?

Do not present one ‘percent accurate’ value as universal validation. State the variable, surface location, operating condition, sample, uncertainty and validation range. Spatial simulations cannot be described as verified until mesh/convergence and appropriate boundary checks have been performed.

# 10. Measurement uncertainty and calibration policy {#s10}

## 10.1 Instrument status vocabulary

**Unverified:** existence/function only. **Functionally checked:** behavior assessed but no adequate reference chain. **Verified for intended use:** compared against defined limits using a suitable measurement method/reference. **Calibrated in-house:** a documented comparison with a qualified reference, measurement equation, uncertainty and traceability chain, within defined range. **Externally calibrated:** calibration evidence from competent provider with scope confirmed. **Out of service:** unsuitable for release measurements.

## 10.2 Uncertainty-budget structure

For each measurand record quantity, formula, measurement range, Type A observations, Type B source, probability/distribution, standard uncertainty, sensitivity coefficient, correlation/covariance, combined standard uncertainty, coverage method, expanded uncertainty, validity range and reference documents. For thermal resistance `R_th=(T_surface-T_amb)/P`, include shared ambient sensor correlations and power uncertainty. For time constants include synchronized sampling, sensor lag and model form uncertainty. Separately address *model discrepancy*, which is not automatically included in the sensor uncertainty budget.

## 10.3 Calibration decision logic

Use a device only where its expected uncertainty is adequate for the declared effect size. Seek existing certificates from the host where allowed; do not alter shared instruments. Costly external calibration is a resource decision following a measurement capability assessment. An accredited certificate is not a prerequisite for every exploratory measurement, but formal claims of traceability require supporting evidence.

# 11. Safety, facility governance and ethics {#s11}

## 11.1 Permission gates

No energized work unless facility personnel explicitly authorize the specific experiment and operator; complete local induction, assess supervision requirements and restrictions, and approve the control schematic, heat load and stop conditions. Fabrication permissions do not imply powered-test permissions. Confirm risk ownership and emergency procedures before first power-up. A personal access card does not substitute for equipment authorization.

## 11.2 Main hazards and controls

Electrical shorts/incorrect wiring (isolated low-voltage current-limited supply, protection, continuity/polarity check, quick disconnect); burns and ignition (component rating, nonflammable mounting, contact guards, surface temperature limits, monitoring); stored capacitor energy (discharge path and verification), ESD and component damage (ESD controls); rotating fan (guarding); solder fumes (suitable ventilation); tool hazards (machine induction); unattended tests (prohibited initially); documentation/data leak (redact IDs and KTH facility-sensitive material). No high-voltage, mains-connected or high-energy-battery circuit in scope.

## 11.3 Research integrity

Keep original observations, failed tests and deviations. No backdating, fabricated measurements, hidden data exclusions or after-the-fact ‘pre-registration’. Record AI-supported drafting or coding according to venue policy; the researcher is responsible for technical accuracy and attribution. The independent programme cannot claim KTH supervision, accreditation, university degree credit, institutional funding or laboratory endorsement without explicit authorization.

# 12. Data architecture and open reproducibility {#s12}

## 12.1 Data custody and separation

Retain `data/synthetic/` as a separate clearly labeled class. Once tests are approved, store `data/experimental/raw/` immutable with cryptographic hashes and capture metadata; store corrections and derived results in `processed/` with script identifiers and quality flags. Never store private identity numbers or restricted KTH documents in the public repository. Maintain a private custody register for laboratory certificate locations if publication permission is absent.

## 12.2 Reproduction tiers

**A — analysis-only:** download public release and reproduce figures/statistics with pinned Python environment and no instruments. **B — lower-cost physical replication:** reproduce a reduced safe experiment with explicitly larger uncertainties, not a claim of metrological equivalence. **C — full laboratory replication:** use specified fixture, instruments/ref status, documented mount conditions, risk review and repeat the qualified campaign.

**Release gate:** a clean checkout passes tests, reproduces plots/statistics within declared tolerance, checks data hashes, documents dependencies, links findings to raw input and has a second-person reproduction review where feasible.

## 12.3 GitHub and Zenodo

GitHub is the living collaboration/review record. A **tagged, immutable release** is archived to Zenodo after data/publishing permissions and independent reproduction check. `CITATION.cff`, a license, data dictionary, README and DOI metadata must match the released version. arXiv is optional for a qualified manuscript and does not substitute for peer review. LinkedIn is a **post-publication technical explanation**, not an evidentiary source.

# 13. Work breakdown structure (WBS) and ownership {#s13}

| WBS | Work package | Core activities | Exit evidence |
|---|---|---|---|
| WP0 | Governance | requirements, risk, decisions, versioning, facilities | controlled baseline and review logs |
| WP1 | Scholarly review | reproducible search, full texts, novelty matrix | gap assessment accepted / scope controlled |
| WP2 | Architecture and safety | circuit, protection, CAD fixture, hazard log | approved drawing, local lab permission |
| WP3 | Metrology and commissioning | instrument qualification, uncertainty, pilot | EBT-Q0 evidence and go/no-go |
| WP4 | DOE/preregistration | sample sizing, run order, holds, acceptance | test plan v1.0 approved before confirmatory tests |
| WP5 | Experimental execution | acquisition, remounts, deviations, backups | quality-controlled real dataset |
| WP6 | Modeling | RC and optional spatial models, numerical V&V | verified source + model registry |
| WP7 | Statistical validation | holdout inference, uncertainty, limits | analysis notebook and results review |
| WP8 | Scholarly publication | paper, figures, supplementary, reviewer feedback | manuscript readiness assessment |
| WP9 | Open release and career communication | DOI, tutorial, portfolio, LinkedIn | independently reproducible release |

**Accountability:** independent researcher owns and signs all project decisions. Any facility officer, reviewer, or future academic collaborator may sign only for the domain they have explicitly agreed to review. No named person is assigned duties without consent.

# 14. Schedule, constraints and dependencies {#s14}

The schedule is **relative to gate completion**, with a current planning window from November 2026 into mid-2027. Physical work is front-loaded only if facility approval is received; laboratory permissions and experimental reliability override schedule. The Ladok re-registration certificate documents course registration through **11 January 2027**; it does not itself guarantee laboratory access through that date or February 2027.

| Window | Priority work | Critical decision |
|---|---|---|
| Nov 2026 (weeks 1–4) | controlled baseline, literature review, facility responses, Q0 rig proposal | G0 programme baseline |
| Late Nov–Dec 2026 (weeks 3–8) | equipment inspection, component selection, sensor assessment, Q0 pilot | G1 scientific differentiation; G2 safety/equipment feasibility |
| Dec 2026–Jan 2027 (weeks 7–12) | pilot-driven DOE lock and authorized physical acquisition | G3 protocol approval; G4 dataset adequacy |
| Jan–Mar 2027 (weeks 10–20) | modeling, uncertainty, validation and counterchecks | G5 validated claim review |
| Mar–May 2027 (weeks 18–28) | thesis-equivalent manuscript, replication audit, archival release | G6 publication readiness |

If access is delayed, move physical windows and use parallel time for literature, code verification, sensitivity studies and instrument-selection calculations. If no lab is available, invoke the recorded **computational-only fallback**; never quietly substitute simulated data for experimental claims.

# 15. Budget, procurement and equipment strategy {#s15}

**Buy last, qualify first.** Primary facility option: KTH ELAB, pending approval. Backup: Stockholm Makerspace only after confirming permitted energized tests, instrument availability, facility rules and actual access economics. Current screenshot indicates a 750 SEK two-month starter package (200 SEK base + 550 SEK access); treat rates as quoted at time of inquiry, not a long-term guaranteed price.

| Budget class | Strategy | Authorization status |
|---|---|---|
| Facility membership | use approved university access first; reserve paid backup | pending access replies |
| Consumables | resistors, MOSFETs, heatsink, TIM, wires, connectors, protective elements | itemize after circuit and inventory |
| Thermal measurements | use available verified logger/sensors; buy only missing measurement functions | pending inventory |
| Precision and calibration | preferentially use suitably qualified references in host lab; external calibration only if warranted | pending uncertainty budget |
| Fabrication | CAD and student/community workshop subject to permission | pending induction |
| Archival and dissemination | GitHub + Zenodo; manuscript venue fees/format assessed later | no spend committed |

Maintain a bill of materials with vendor, currency, unit cost, alternate part, risk, lead time, available-on-site flag and purchase approval. A budget forecast is not a purchase order.

# 16. Risk management and contingency {#s16}

Risks are recorded with owner, likelihood (1–5), consequence (1–5), score, mitigation, trigger and contingency in `08_project_controls/risk_register.csv`. The leading risks are (R-01) lack of lab permission, (R-02) insufficient measurement quality, (R-03) junction observability/overclaim, (R-04) no publishable novelty, (R-05) insufficient independent replicate count, (R-06) fixture/contact variation, (R-07) test overheat or wiring hazard, (R-08) schedule compression, (R-09) publication/data permissions, (R-10) collaborator/authorship ambiguity.

Risk review occurs at every gate and after incidents or substantive design changes. Safety stop rules take precedence over publication ambition.

# 17. Stage-gate governance: measurable readiness {#s17}

| Gate | Name | Non-negotiable evidence | Current status |
|---|---|---|---|
| G0 | Controlled project baseline | charter, WBS, RQs, initial risks, source model retained, change-control procedure | **Baseline produced; internal acceptance pending** |
| G1 | Research differentiation | full-text prior-art matrix; novelty/benchmark framing and overlap transparently reviewed | OPEN |
| G2 | Lab readiness | site permission, induction, electrical/thermal hazard controls, actual instruments characterized | OPEN |
| G3 | Confirmatory protocol lock | pilot results; uncertainty and sample-size justification; preregistered matrix/holdout, procedures and stop rules | OPEN |
| G4 | Experimental data sufficiency | independent raw records, quality flags, logs, repeats and documented deviations | OPEN |
| G5 | Scientific validation review | numerical verification, held-out prediction with uncertainty, limitations and negative outcomes | OPEN |
| G6 | Release/manuscript readiness | external critical review where feasible, independent reproduction, rights approval, DOI-ready materials | OPEN |

**Go/conditional/no-go:** at each gate document reviewer, evidence links, decision, conditions and follow-up actions. Physical test authorization requires G2 **and** the approved local test procedure, not merely a checked project-management box.

# 18. Scientific manuscript strategy {#s18}

## 18.1 Target manuscript structure

Title and structured abstract; introduction and literature gap; theory and observability; experimental facility and traceability; predeclared DOE and held-out cases; analytical/RC and spatial models; numerical verification; raw-data reduction; uncertainty quantification; experimental results; out-of-sample prediction analysis; sensitivity; threats to validity and limitations; conclusions; data/code availability and appendix.

## 18.2 Publication decision hierarchy

1. **Journal/conference research paper** only if differentiated contribution, adequate measured evidence and reviewer feedback support the claim. Potential families: electronics thermal management, packaging, experimental metrology, power electronics; exact venue fit/restrictions checked when manuscript is mature.
2. **Open benchmark/methods paper** if high-quality reproducible dataset and method are valuable but methodological novelty limited.
3. **Citable Zenodo technical report** if a research paper cannot be honestly supported. It remains a strong engineering portfolio outcome.

No submission to arXiv or a peer-reviewed venue will imply acceptance. Do not rush deadlines or claim authorship on behalf of KTH researchers. Maintain an authorship and affiliation agreement before collaboration or shared data collection.

# 19. Outreach and professional translation {#s19}

Do not approach KTH with empty promises or a generic request to use tools. **Outreach packet** must include this scope, one-page concept note, verified v0.1 code, explicit prior-art overlap, practical apparatus/equipment list, proposed measurement plan, preliminary cost/risk estimate and the precise technical feedback sought. A first methods discussion can occur before the full experiment, but any assertion of empirical findings requires data.

**Career portfolio outputs:** schematic with safety basis; fixture CAD; calibration/verification matrix; trial-to-result traceability; thermal-model comparison; uncertainty budget; reproducible figures; lessons learned; a clear statement of what the researcher personally designed, verified and operated. Publication-related LinkedIn posts must link to an actual public release, show real (not simulated-as-real) results and distinguish system predictions from measurements.

# 20. Configuration and change management {#s20}

## 20.1 Baseline concept

Revision 1.0 is a **controlled, living baseline**, not a frozen research conclusion. The work has identified research questions and methods to pursue, but scientific revisions are allowed. Future updates should be additive or focused replacements tied to a change request—not total rewrites of the project history.

| Change class | Example | Action |
|---|---|---|
| Editorial patch 1.0.x | typo, broken link, reference formatting, clarification without technical effect | direct edit + CHANGELOG + peer self-review |
| Minor 1.x | sensor method, sample design, apparatus or new work package within thesis objective | change request + impact assessment + affected documents updated |
| Major 2.0 | change central research question or scientific endpoint | formal decision and superseding baseline; preserve old version |
| Confirmatory test-plan amendment | any modification after G3 protocol lock | dated amendment with reason; distinguish exploratory from confirmatory data |

## 20.2 Required change request (CR)

Every technical CR contains CR ID, origin, date, documents impacted, current/proposed baseline, motivation, impact on safety/cost/schedule/measurement/reproducibility/publication, proposed verification, decision, decision date and effective revision. Record alternatives rejected. Keep raw measurements intact even if analysis rules change; use versioned processors and regenerate results.

## 20.3 Working cadence

Weekly: update project board, blocker list, spending and equipment requests. At each completed work package: review generated artifacts and references. At every gate: sign decision record and freeze the relevant test-plan revision. Monthly: assess research novelty and facility constraints without reopening the whole programme. Publication release: tag, archive, reproduce and verify metadata.

# 21. Next 14-day execution order {#s21}

| Order | Concrete task | Output / definition of done |
|---|---|---|
| 1 | Accept EBT-PMP-001 v1.0 baseline and repository folder structure | decision D-001 recorded; no substantive editing without CR |
| 2 | Log pending responses to existing KTH enquiries | access tracker updated with dates and owners |
| 3 | Review central 2024–2026 papers and complete detailed overlap comparison | at least first 8 full-text entries with evidence status, unresolved points listed |
| 4 | Select two candidate DUTs and one resistive reference heater from datasheets | component selection matrix with safe voltage/current/temperature bounds |
| 5 | Draft electrical block diagram, protection and sensor map | reviewed unpowered drawing and preliminary hazard assessment |
| 6 | Prepare equipment inventory survey for ELAB / alternate space | measurement requirements / required references ready before site visit |
| 7 | Extend synthetic benchmark with sensitivity, noise and model identifiability tests | automated tests and plots with explicit simulation labels |
| 8 | Write one-page KTH research pitch *but do not send automatically* | claims limited to actual reviewed technical evidence |

This sequence is intended to stop conceptual drift. Workstreams can run in parallel. The facility decision (KTH first, paid backup only if justified) remains an implementation choice, not a recurring debate about the scientific thesis.

# 22. Core references and provenance {#s22}

**Standards / metrology (primary source URLs):**

- [S01] ISO/IEC 17025:2017, ISO official catalogue: https://www.iso.org/standard/66912.html
- [S02] JCGM guides, BIPM: https://www.bipm.org/en/committees/jc/jcgm/publications
- [S03] ASME V&V 20-2009 (R2021), ASME catalogue: https://www.asme.org/codes-standards/find-codes-standards/standard-for-verification-and-validation-in-computational-fluid-dynamics-and-heat-transfer
- [S04] IEC 61010-1:2010 + AMD1:2016, IEC official publication: https://webstore.iec.ch/en/publication/4279
- [S05] IPC-2152, official IPC table of contents: https://www.ipc.org/TOC/IPC-2152.pdf
- [S06] JESD51-14 method background (not full standard), IEEE STHERM 2011: https://doi.org/10.1109/STHERM.2011.5767204
- [S07] Zenodo GitHub archival integration: https://help.zenodo.org/docs/github/enable-repository/

**Direct prior-art and KTH context (screening-stage, full texts pending where noted):**

- [P01] Putthong, Lu & Lee (2026), DOI https://doi.org/10.53941/perat.2026.100014
- [P02] Schulz, Strössner & Grötzbach (2026), author publication note: https://erickschulz.dev/publications/src/data/publications/identifiability-cauer-thermal-networks/
- [P03] Zhang et al. (2024), DOI https://doi.org/10.1109/TPEL.2024.3367854
- [P04] Ress et al. (2026), DOI https://doi.org/10.3390/en19112678
- [P05] Bhadoria (2025), KTH DiVA institutional record: https://kth.diva-portal.org/smash/person.jsf?pid=authority-person%3A105216
- [P06] Cnudde et al. (2026), Ghent institutional record: https://biblio.ugent.be/publication/01M3C8RKZ0XAPQVC4PAPH2Q791

**Internal provenance:** EBT-R01 feasibility v0.1 ZIP, generated 05 Nov 2026, with experimental protocol draft, targeted literature table, synthetic data, code, seven tests, and explicit nonphysical disclaimers. External references are cited as source records; their normative or full-text contents have not been reproduced.

# Appendix A — Gate decisions and unanswered choices

The following choices have **defined owners and triggers**; they are not reasons to delay the programme baseline. AC-01 exact DUT (trigger: datasheet + facility inventory). AC-02 allowed electrical levels (trigger: safety review). AC-03 instrument/reference suitability (trigger: bench inspection). AC-04 sensor geometry and junction-sensitive method (trigger: Q0 feasibility). AC-05 effective sample size/run order (trigger: pilot variance). AC-06 public data/photo rights (trigger: facility approval). AC-07 manuscript differentiation (trigger: full-text review). AC-08 KTH research contact date (trigger: working evidence package + sufficiently bounded claim).

# Appendix B — Document index and naming

`EBT-PMP-001`: this master plan. `EBT-REQ-001`: requirements register. `EBT-RSK-001`: risk register. `EBT-STD-001`: standards matrix. `EBT-LIT-001`: literature matrix. `EBT-Q0-TP-001`: pilot protocol. `EBT-MET-001-REG`: instrument register. `EBT-R01-TP-001`: primary research test plan. `EBT-R01-DAT-001`: raw experimental dataset manifest (not yet existent). `EBT-R01-RPT-001`: technical report (future). `EBT-PUB-001`: publication and release plan. `EBT-CR-###`: change requests. `EBT-DEC-###`: decision records.

# Appendix C — Definitions of done

**Baseline complete:** controlled documents are internally consistent, registers have unique IDs and owners, source model passes tests. **Bench ready:** actual authorization, electrical schematic, equipment and metrology suitability, safety stop rules and recorded readiness signoff. **Experiment complete:** all raw files immutable and hashed, quality/exclusions logged, independent runs documented. **Research complete:** held-out predictions, uncertainties, sensitivity and limitations reviewed. **Open release complete:** independent recreation from clean checkout, DOI metadata, licensing and permission checks. **Career output complete:** technically accurate one-page case study and LinkedIn material linking to actual evidence.
