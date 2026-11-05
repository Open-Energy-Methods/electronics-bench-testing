# EBT-LIT-003 — Critical literature assessment and research-gap review

**Version:** 0.3 · 2026-11-05 · Research work package WP1 / Gate G1  
**Programme:** EBT-PMP-001 v1.0 (unchanged) · EBT-R01 · [Issue #3](https://github.com/Open-Energy-Methods/electronics-bench-testing/issues/3)  
**Status:** **SUBSTANTIVE FULL-TEXT REVIEW WHERE ACCESSIBLE; OPEN ACCESS GAPS REMAIN.** This is a focused critical review, **not** a completed systematic review, exhaustive state-of-the-art search, peer-reviewed paper or confirmed novelty statement.  
**Review scope:** electrothermal thermal-network identification; sensor and junction-temperature observability; cooling-boundary dependence; interface and assembly variability; experimental validation; open reproducibility.

> **Decision summary.** The existing EBT focus is technically relevant but severely overlaps prior research. Parameter identifiability, sensitivity-based experiment design, alternate-interface transient testing, boundary-dependent compact thermal models, sensor-position sensitivity, and interface-resistance variability are **already demonstrated in the literature**. What remains plausible is a *well-controlled, open and prospective* experiment evaluating **transient cross-boundary prediction with independently qualified boundary inputs, independent assembly remounts and a measurement uncertainty budget**. This is a **candidate benchmark/method contribution, not established scientific novelty**. If instrumentation cannot separate heater power, boundary effects and surface-sensor variation, downgrade to a qualified data/method report rather than claim junction-temperature validation.

## 1. Method and evidence policy

### 1.1 Research questions for this review

- **LQ1:** Which of our proposed RQ1–RQ3 components have already been experimentally established?
- **LQ2:** Which published studies actually measure **junction-sensitive** temperatures, accessible surface temperatures, or temperatures estimated only by models?
- **LQ3:** Are boundary conditions measured independently for prospective prediction, fitted in-sample, prescribed in simulation, or partly unreported?
- **LQ4:** How is mounting/interface variance handled: device samples, remounts, repeated traces, ageing or intentionally changed TIMs?
- **LQ5:** Are actual independently held-out *configurations* evaluated, and are their measurement uncertainty and raw data publicly documented?

### 1.2 Search and eligibility

Focused searches were conducted **5 November 2026** using web indexes and publisher/author/institutional pages. Exact query families and access states are recorded in [the search log](../08_project_controls/literature_search_log_v0.3.csv). Reference chaining included key references within Putthong (2026), Zhang et al. (2024), and the 2020 thermal-reproducibility paper. Included sources had original research directly related to a named LQ, prioritizing 2019–2026, with older method standards where necessary. A complete IEEE Xplore, Scopus and Web of Science search was **not** conducted; access-limited sources remain flagged. Do **not** use the term “systematic literature review,” report invented retrieval counts, or infer absence of prior work from missing results.

**Access grades** for the source register:

- **F-PDF:** original scholarly full-text PDF inspected, with methods/results/limitations; no copyrighted PDFs are redistributed.
- **F-HTML:** original full HTML research article inspected, including methods/results (not merely an abstract).
- **T:** original university thesis *summary* manuscript inspected, not automatically every constituent appended article.
- **A:** publisher/author/institutional abstract or bibliographic record only. Method details beyond this record are **unknown**, not absent.
- **R:** external secondary index only; insufficient to settle claims.

A public link labelled “open access” is **not** evidence of actual full-text inspection unless the PDF/html contents were retrieved.

## 2. Findings at a glance — overlap and consequence

| Topic proposed in EBT v1.0 | Relevant existing work | Impact on our claims |
|---|---|---|
| A model fits calibration data but fails prospectively | Putthong et al. (2026) **F-PDF**; Schulz et al. (2026) **A** | **Already known**; no novelty in observing fit-versus-prediction discrepancy. |
| Sensitivity/SVD and better selection of thermal experiments | Putthong et al. (2026) **F-PDF** | **Already done** experimentally; using a randomized factorial alone is not a method invention. |
| Sparse time-domain extraction / time-constant resolution | Zhang et al. (2024) **F-PDF** | **Already done**; avoid rediscovering network identification or noise analysis. |
| Apparent thermal metrics depend on sensor location and fixture | Farkas et al. (2020) **F-HTML** | **Already demonstrated** experimentally and numerically; EBT must define a new decision/use case, not repeat the observation. |
| Thermal-interface variation and mounting pressure matter | Toth-Pal & Nee (2026) **F-HTML**; Wang et al. (2026 issue) **A**; Urabinahatti et al. (2019) **A** | **Not novel**; study repeated *transfer prediction* instead of a generic TIM comparison. |
| Dynamic tests under two interfaces and thermal-network identification | Zhang et al. (2024) **F-PDF**; Farkas et al. (2020) **F-HTML** | **Direct precedent**: a new dual-interface transient test alone is insufficient. |
| Compact model explicitly changes with boundary condition | Ma et al. (2021) **A**; Bahman et al. (2017) citation trail | **Strong precedent**; full-text comparison remains mandatory. |
| Device-level heat input separated from wiring/PCB power | Ress et al. (2026) **F-HTML** | **Already quantified**; heater power must be measured at its own terminals. |
| Experimental spreading-resistance network validation | Cnudde et al. (THERMINIC 2026) **A** | **Possible direct competitor; methods unavailable**; do not claim it fails to cover our gap. |
| Open numerical/physical datasets for thermal transient testing | Ress et al. (2026) **F-HTML**, public dataset link | **Exists**; do not claim the first open thermal benchmark. |
| Thermomechanical package reliability | Bhadoria (2025) **T**; Toth-Pal & Nee (2026) **F-HTML** | Our surface-temperature tests alone cannot justify fatigue/stress/lifetime claims. |

## 3. Full-text critical appraisals

### FT01 — Putthong, Lu & Lee (2026): experimental-design detectability

**Source:** *Efficient Experimental Design Framework for Reliable Parameter Identification of Electro-Thermal Models*. Power Electronics Research and Applications Transactions, published 13 Oct 2026. DOI [10.53941/perat.2026.100014](https://doi.org/10.53941/perat.2026.100014); [original 11-page PDF](https://media.sciltp.com/articles/2610005337/2610005337.pdf). **Access: F-PDF.**

**What the authors actually do (Sections 2–5, especially pp. 2–9):** They formulate a **steady-state** electrothermal model: nonlinear natural-convection self-heating plus linear, symmetric cross-device thermal coupling. A normalized parameter sensitivity matrix is decomposed with SVD. The least-detectable temperature response associated with parameter-change directions is evaluated against a practical temperature threshold. Experimental cases are chosen with a greedy procedure plus exchanges. The authors describe possible modification/recalibration for forced convection or liquid cooling (Sec. 2.1) and explicitly state that their model **does not include thermal dynamics** (Sec. 2.2). Thus the method is not itself a demonstrated transient cross-boundary study.

**Actual test setup (Sec. 5 and Fig. 3):** Four independently controlled **IRFZ44N MOSFETs** with LM358 control electronics act as heat sources. The fitting power range is roughly 2–9 W per MOSFET. OMEGA OM-HL-EH-TC contact thermometry provides steady-state fitting temperatures; a FLIR ONE Pro is **supplementary imaging**, not junction measurement. Two four-case calibration choices (unguided vs criterion-guided) are evaluated against the **same outside-range validation power configuration**. The model is fitted with nonnegative and bounded least squares in SciPy.

**Published result (Sec. 5, Table 1 and Fig. 4):** For the particular experimental comparison, fitting RMSE was **2.161 vs 1.413 °C**, whereas validation RMSE was **28.236 vs 0.462 °C** (unguided/guided). These are the authors' results for their defined case; they are **not** performance guarantees for EBT. Across 1,820 four-case combinations assembled from 16 selected cases, only eight satisfied their criterion, again under the paper's setup and response threshold.

**Critical assessment:** This study is *direct prior art* for information sufficiency, parameter observability and held-out predictive accuracy. It primarily addresses **steady-state input-case selection** for a multi-heat-source arrangement, not experimentally measured transient power-step transfer between physically remounted cooling assemblies. Its one external power-pattern validation case is not the same as multiple independent assembly-level holdouts. However, *lack of discussion in one paper is not evidence nobody has tested the latter*. EBT must not claim novelty in identifiability, SVD, greedy DoE, or out-of-sample temperature prediction.

**Action for EBT:** Record exact sensor detectability from Q0; consider a **pre-experiment sensitivity/detectability audit** before locking levels. Do **not** simply impose the authors' 0.2 °C threshold on our unknown equipment. Compare dynamic experimental designs fairly rather than equating a 54-row factorial with sufficient information.

### FT02 — Zhang, Evgrafov, Zhao, Kalker & de Doncker (2024): transient inversion

**Source:** *A Sparsity-Promoting Time Domain Evaluation Method for Thermal Transient Measurement of Power Semiconductors*. IEEE Transactions on Power Electronics 39(6), 7525–7535, DOI [10.1109/TPEL.2024.3367854](https://doi.org/10.1109/TPEL.2024.3367854); [AAU accepted manuscript PDF](https://vbn.aau.dk/ws/portalfiles/portal/669916831/TPEv1.pdf). **Access: F-PDF.**

**Methods (Secs. II–IV, Figs. 5–7):** A conventional Network Identification by Deconvolution (NID) frequency-domain inverse problem is reformulated as a **regularized time-domain least-squares** problem with sparsity-promoting components. Four simulated three- or five-layer thermal-network examples provide benchmark ground truth. Noise sensitivity is evaluated at varying signal-to-noise ratios. The authors' reported comparison reduces relative **structure-function reconstruction error** on their benchmark from roughly 10% to 1%; do not misquote that as a 1% temperature-prediction error for an arbitrary device.

**Physical demonstration (Sec. IV, Table II and Fig. 7):** A commercial FGA20N120FTD **1200 V/20 A IGBT** with TO-3P package is tested against a temperature-controlled copper reference block, using **dry** and **thermal-grease** interfaces. Heating/sensing currents, IGBT gate bias, and fast sampling are explicitly recorded (reported **30 A heater, 100 mA sensing, 15 V gate, 100 s heat/cool segments, 25 °C coolant and 1 MHz acquisition**). A temperature-sensitive forward voltage is used for junction observation under their qualified method.

**Critical assessment:** This is substantial prior art for **transient** thermal characterization, interface perturbation and alternative Cauer/Foster structure identification. Their key claim is improved **inverse extraction of thermal time constants/structure functions**, not prospective cross-facility model transport with independent boundary measurements. Their own noise study reports sensitivity of the proposed reconstruction to reduced SNR; we must not claim universal superiority.

**Action for EBT:** Keep inverse structure-function extraction as **optional comparative baseline**, not a novel EBT algorithm. Do not equate our proposed low-cost case-temperature logger with the paper's 1 MHz junction-sensitive measurement. If the paper requires junction-time scales beyond our sensors' bandwidth, document that as a **scope mismatch**, not a failed replication.

### FT03 — Farkas, Schweitzer, Sarkany & Rencz (2020): reproducibility across fixtures

**Source:** *On the Reproducibility of Thermal Measurements and of Related Thermal Metrics in Static and Transient Tests of Power Devices*. Energies 13(3), 557, DOI [10.3390/en13030557](https://doi.org/10.3390/en13030557), [publisher HTML](https://www.mdpi.com/1996-1073/13/3/557). **Access: F-HTML.**

**Methods (Secs. 3–8; Tables 2–3):** The paper combines a **finite-element numerical experiment** on a multi-layer IGBT/cold-plate/TIM assembly, comparison of transient dual-interface method (TDIM) with point sensing, and actual package measurements. It explicitly studies external thermocouple placement, TIM conductivity, boundary-condition changes, transient acquisition electrical effects, and fixture/instrument differences. One reported 14-device sample comparison uses seven standard TO-247 HUF75639G3 packages and seven with modified flattened/polished contact surfaces, in higher/lower heat-transfer apparatus. It also compares conventional point-based approaches against TDIM and finite-element references. This is stronger and closer to our sensor-position premise than a generic review.

**Published results:** The measured thermal metrics differed materially with external sensor configuration, surface finish and test installation. The authors report different inferred junction-to-case thermal resistances for different methods and observe sizable inter-setup reproducibility discrepancies; their examples include **up to approximately 26% variation between thermocouple-based laboratory results**. The published percentage is **method/assembly-specific**, not an uncertainty bound that applies to EBT. A dual-interface structure-function analysis can reduce some dependence on selecting an exact physical case sensor reference under its stated assumptions.

**Critical assessment:** **Strong negative novelty evidence** for a paper claiming that “surface sensors can mislead” or that changing TIM/cold-plate conditions distorts apparent thermal resistance. The very premise is established. EBT can still study whether an inexpensive, fully documented measurement protocol gives *prospective* prediction intervals for new assemblies, but must explicitly compare with this work and acknowledge where the simpler method is inferior to TDIM.

**Action for EBT:** Preserve a **sensor-placement sensitivity sub-study** as quality control and a measured covariate, not the manuscript's originality headline. Report case/sink locations and electrical source power rigorously; distinguish apparent sensor-to-ambient metrics from junction-to-case resistance. Evaluate whether fixture/surface effects dominate model differences.

### FT04 — Ress, Farkas, Sarkany & Rencz (2026): power measurement fidelity in GaN

**Source:** *Improved Thermal Transient Testing of Wide Bandgap Devices with Extremely Low Channel Resistance*. Energies 19(11), 2678, DOI [10.3390/en19112678](https://doi.org/10.3390/en19112678), [publisher HTML](https://www.mdpi.com/1996-1073/19/11/2678). **Access: F-HTML.**

**Method (Secs. 2–6):** The authors distinguish thermal-transient measurements aimed at operating temperature from structure reconstruction. With very low channel resistance, external package/PCB/cable resistances can dissipate a significant portion of nominal electrical power outside the actual die. They derive an analytical correction to obtain device-contributed heating rather than using total external terminal power uncritically. The measurements use an **Infineon IGOT60R070D1** GaN GIT-device PCB, multiple voltage taps for two-wire/four-wire comparisons, a thermal tester, deliberately inserted external test resistances and calibrated temperature-sensitive electrical parameters. Sensor calibration was performed at five thermostat conditions from **20 to 60 °C**, according to Sec. 6.2.

**Measured data and reproducibility:** Their experiment distinguishes instrument connections close to the device from those including PCB/wiring paths, and checks corrected thermal descriptors. The Data Availability Statement links a public supporting dataset: [sandorress/wbgmeasurements](https://github.com/sandorress/wbgmeasurements). This invalidates any assertion that EBT would be the first openly released semiconductor thermal-measurement dataset.

**Critical assessment:** For a **resistive Q0 heater**, `V×I` at the *heater terminals* is still necessary but not sufficient to infer a semiconductor junction's own dissipation. For later devices, series-wiring and shunt losses, die versus interconnect heating, and temperature-sensitive calibration become critical. EBT cannot offer a credible internal-junction claim on the basis of surface thermocouples alone.

**Action for EBT:** Implement 4-wire voltage sense at the actual heat-source terminals where appropriate, check instrument common/grounding, quantify any separately heated shunt/control hardware, and publish channel-level measurement geometry. A future MOSFET campaign requires part-specific TSEP calibration or else restrict response variable to measured package/sink temperatures.

### FT05 — Toth-Pal & Nee (2026): KTH mounting variability and lifetime

**Source:** *Operating Lifetime Behavior of Thermal Contact Resistance Between Clip-Attached TO 247 Package and Heat Sink with and Without an Ultra-Thin Interlayer Silver Film*. Energies 19(15), 3493, DOI [10.3390/en19153493](https://doi.org/10.3390/en19153493), [publisher HTML](https://www.mdpi.com/1996-1073/19/15/3493). **Access: F-HTML.** Both authors are affiliated with **KTH EECS**.

**Methods (Secs. 2–3):** A **30-assembly** clip-mounted TO-247 diode/heatsink experiment uses three material groups: **7 no film, 12 with 12.5 µm silver film, 11 with 6 µm film**. Dissipation is around **22 W** from an **18 A diode current**, with package and sink **Pt1000** sensors; the heat sink is coupled to an ice-water bath. Thermal contact resistance is estimated from the temperature difference divided by power at specified sensor locations. Controlled accelerated ageing at **110 °C for 18 weeks**, supplemented by two longer-studied samples, is interpreted using a stated Arrhenius acceleration assumption. The “equivalent operating life” is **conditional on this ageing model**, not proof of in-field endurance for arbitrary equipment. The experiment does not cover vibration, power cycling or humid field conditions.

**Measured results (Table 1; Secs. 3.1 and 3.3):** Initial group means were **1.87 K/W** (no film), **1.48 K/W** (12.5 µm) and **1.72 K/W** (6 µm); ranges and distributions overlap. The authors report a statistically significant average reduction with 12.5 µm film relative to no film, whereas the thinner-film difference was not statistically significant by their test. Individual assembly differences, clip force, surface finish and sensor placement are assessed. Their paper provides **Supplementary Materials** with underlying sample measurements.

**Critical assessment:** This **KTH research directly overlaps EBT's proposed mounting/interface variability**. It is evidence that contacts and attachment are already experimentally studied, at meaningful sample counts. The paper emphasizes **static thermal contact and long-duration ageing**, not the exact proposed EBT prospective transient model transfer under natural/forced cooling and independently characterized boundary inputs. However, we cannot infer that the combination is uniquely unstudied from one paper.

**Action for EBT:** Treat KTH EECS power-electronics packaging as a **potential methodological collaborator**. The approach to KTH should explicitly reference this paper and ask what scientific extension would be useful—not present mounting effects as a new problem. Ensure our eventual physical specimen/sensor geometry and independent assembly count are defensible relative to 30 assemblies already studied elsewhere.

### T01 — Bhadoria (2025): KTH SiC cooling context

**Source:** *Enabling Short-term Over-current Capability for SiC Power Modules and its Application for Power Flow Controllers in HVDC Grids*. KTH doctoral dissertation summary, 2025. [KTH DiVA full summary PDF](https://kth.diva-portal.org/smash/get/diva2%3A1948439/SUMMARY01.pdf). **Access: T (full doctoral thesis summary inspected, not all appended underlying journal publications).**

**Scope (Abstract; Chapters 3–5):** SiC transient over-current thermal constraints are studied using thermal absorbing materials, comparison of top/bottom cooling, microchannel geometries and coupled converter/power-flow-control simulations. COMSOL, PLECS and a scaled-down controller experimental platform are reported in the summary. The thesis has a much different power level and objective from our safe low-voltage bench, but is clear evidence of sophisticated KTH electronics thermal work.

**Critical assessment:** The relevance is institutional and methodological; it does **not** justify claiming that all thermal configurations in the thesis were directly validated at our proposed low-voltage scale. Direct packaging research is a sensible EECS collaboration route.

## 4. Important sources for which original full methods were NOT accessible

The following remain **abstract/record-only** despite targeted searches. We must not populate their missing methods with guesses.

| ID | Original work | Access and securely supported finding | Why still important |
|---|---|---|---|
| A01 | Schulz, Strössner & Grötzbach (2026), *Identifiability of Cauer Thermal Networks*. [Author abstract](https://erickschulz.dev/publications/src/data/publications/identifiability-cauer-thermal-networks/) | **A**. Author reports profile-likelihood assessment of resolvable layers, integrated into PLECS, tested on synthetic and measured examples; accepted by IEEE TPEL. Full methods/manuscript unavailable in this pass. | Direct overlap with layer identification, confidence bounds and prediction of through-power. |
| A02 | Cnudde, Nonneman, Rogiers & De Paepe (2026), *Experimental Validation of a Lumped Parameter Thermal Model for Spreading Resistance in Direct-Cooled Power Electronics*. [UGent institutional record](https://biblio.ugent.be/publication/01M3C8RKZ0XAPQVC4PAPH2Q791) | **A**. University advertises an open PDF, but retrieving the file from the record returned a site error. Only title, authors, publication and institutional metadata verified; detailed apparatus, statistics and validation partitions **unknown**. | Critical to assessing claimed novelty in boundary transfer/spreading-resistance models. |
| A03 | Ma, Guo, Yan et al. (2021), *A Three-Dimensional Boundary-Dependent Compact Thermal Network Model for IGBT Modules in New Energy Vehicles*. [DOI](https://doi.org/10.1109/TIE.2020.2991926) | **A**. Abstract describes FEM-based boundary-dependent compact network, two-step extraction and experimental checks over changing thermal boundaries. The paper appeared in volume 68(6) **2021**, although the DOI includes **2020**; use 2021 as citation year. | The strongest pre-2026 challenge to “first model transfer across cooling boundaries.” |
| A04 | Wang, Zhang & Wang (2026 issue; first online 2025), *Uncertainty Analysis of the Interface Thermal Resistance Between Power Module and Heatsink*. [DOI](https://doi.org/10.1109/TPEL.2025.3610704) | **A**. Abstract covers a six-switch module, dual-interface structure-function tests, thermal cycling, die-to-die TIM variance and PV inverter reliability case study. | Direct uncertainty/mounting precedent. Note online-versus-issue year distinction. |
| A05 | *Guideline for Reproducible SiC MOSFET Thermal Characterization Based on Source-Drain Voltage* (2024), IEEE TIA. [DOI](https://doi.org/10.1109/TIA.2024.3352548) | **A**. Abstract reports TSEP calibration, cooling measurement conditions and validation on four SiC devices. | Essential if we later claim junction T measurement, TSEP reliability or measurement novelty. |
| A06 | Urabinahatti, Ahmad & Narayanan (2019), *Experimental Studies on the Effect of Thermal Interface Material and Mounting Technique on the Thermal Resistance of Device Cooling Arrangement*. [DOI](https://doi.org/10.1109/NPEC47332.2019.9034723) | **A**. Abstract reports experimental comparison of TIMs, clamp/screw techniques and torque, with inferred junction temperature. | Prevents “new interface assembly comparison” claims. |
| A07 | Quitadamo et al. (2022), *A new technique to check the correct mounting of the power module heatsinks*. [DOI](https://doi.org/10.1016/j.microrel.2021.114416) | **A**. Abstract describes intentionally defective heatsink mounting and a measured MOSFET-based test method. | Predictive effect of mounting faults also already addressed. |
| A08 | Bahman, Ma & Blaabjerg (2017), *A Lumped Thermal Model Including Thermal Coupling and Thermal Boundary Conditions for High-Power IGBT Modules*. [DOI](https://doi.org/10.1109/TPEL.2017.2694548) | **A (citation trail)**. Title and established citation via Ma 2021; full original text still to inspect. | Earliest major boundary-aware predecessor in current citation trail. |

**Access note:** A01 and A02 are not “negative results.” Their incomplete access is a **G1 blocker**. KTH library/author-request channels may enable legitimate full-text reading. No publisher PDFs or copyrighted full-text extracts are committed to the repository.

## 5. Critical synthesis by scientific subquestion

### 5.1 RQ1: sensor observability and hidden junction temperature

**Established:** sensor placement, time response, optical emissivity, voltage-sensing TSEP methods, and structural identifiability already matter (FT02, FT03, FT04, A01, A05). Putthong FT01 tests information content against a finite detectable temperature response; Schulz A01 addresses unresolvable thermal network layers.

**What EBT can measure now:** a resistor assembly's **surface**, **sink**, **air** and measured electrical power. Without a separate independently validated junction-sensitive method, a MOSFET's internal `T_junction` is **latent/modelled** and no experiment at our current facility stage can validate it. A synthetic simulation where two models produce nearly identical surface values but different hidden states illustrates **non-identifiability**, not real-world temperature error.

**Recommendation:** move “hidden junction blind spot” to a *motivation/secondary modeling study*. Do **not** headline an empirical junction-temperature accuracy paper unless a legitimate TSEP measurement becomes feasible.

### 5.2 RQ2: prediction transfer across physical cooling boundaries

**Established:** a predictive model's thermal parameters may depend on cooling boundary, and boundary-dependent compact thermal networks exist (A03, A08). FT01 explicitly limits its empirical model to steady-state naturally cooled conditions and notes forced cooling needs new modeling. FT02 demonstrates two thermal interfaces for transient inversion, but its main goal is structural extraction.

**Plausible residual contribution:** compare **steady-state and time-resolved temperature predictions** on held-out *physical* natural/forced cooling and remounted assemblies, using a documented **independently qualified boundary input**, rather than calibrating the boundary on the target run. Include reference baselines, model-complexity penalties, and prediction interval coverage. Evaluate whether gains are meaningful relative to simple fixed-boundary models.

**Hard causal issue:** apparent `R_sa=(T_sink-T_air)/P_heater` from an assembly with other thermal pathways is **not** an intrinsic, transportable convection coefficient. Independent qualification must control heater footprint, fixture, lead losses, orientation, fan behavior and sensor location. A “boundary-aware model” that uses the held-out temperature trace to estimate `R_sa` is **data leakage**, not prospective prediction. If boundary cannot be characterized without the held-out response, declare the analysis retrospective/descriptive.

### 5.3 RQ3: mounting and interface variability

**Established:** physical contact/mounting effects and variability, including replicated assemblies and ageing, are well studied (FT03, FT05, A04, A06, A07). FT05 shows 30 tested assemblies at KTH; three repeated temperature traces from one mount are not the same as three mounts.

**Plausible residual contribution:** quantify **between-remount prediction degradation** and coverage conditional on predeclared mounting procedures and sensor placement. Report mounting assembly as experimental unit and a random/block effect where data support it; do not call a before/after grease comparison new science.

### 5.4 Open-source reproducibility

**Established:** some related real transient measurement data are already publicly released (FT04). Releasing Python code and a Zenodo DOI is good scholarship but **not novelty by itself**.

**Potential added value:** one reproducibility package with complete fixture drawings, instrument reference checks, raw time series, blocked remount metadata, calibration/validation partition manifest, analysis scripts, known failure cases, explicit exact-versus-tolerance numerical reproducibility, and known measurement limitations. That may make a useful **data or methods** publication even if a new model theory is absent—subject to journal suitability and facility release permission.

## 6. Proposed revised positioning (not yet a programme-level change)

**Working title, preferred:**

> **Prospective Cross-Boundary Validation of Compact Thermal Models: An Open Low-Voltage Benchmark with Independent Boundary Measurements and Assembly Variability**

Alternative (only if a qualified junction-observable method becomes available):

> **Measurement-Aware Electrothermal Model Transfer Across Cooling Boundaries: Experimental Validation with Independent Junction-Sensitive References**

### Revised primary research question (provisional)

**When thermal boundary information is measured independently, how accurately do fixed- and boundary-aware compact models predict the *accessible transient temperatures* of physically separate low-voltage cooling assemblies under held-out cooling and remount conditions, and how well do prediction intervals cover the observed variability?**

Research design no longer assumes internal junction temperature is directly observed. MOSFET-specific extension is **conditional** on equipment, safe operation and TSEP feasibility.

### Minimum fair comparison and validation contract

1. **Observable:** primary (T_{case/surface}), (T_{sink}), (T_{amb}), (V_{heater}), (I_{heater}), and time with metrology records. No empirical `Tj` claim without reference.
2. **Baseline models:** B0 stationary empirical surface resistance; B1 one-RC fixed boundary; B2 compact multi-node fixed boundary; B3 multi-node/one-RC with independently supplied external boundary; optional B4 verified spatial model *only if* geometry and airflow inputs warrant it.
3. **Calibration control:** same fitting observations for all competing models; choose complexity and hyperparameters **without** accessing holdout results. Any premeasured boundary characterization must have a **distinct qualification dataset**, cost and uncertainty documented.
4. **Holdouts:** reserve complete *cooling configurations* and independently remounted assembly events before model selection. Avoid random train/test time points from one transient as “independent validation.”
5. **Metrics:** preregistered transient RMSE and bias at specified sensors, peak and late-stage error, uncertainty-normalized residuals, interval coverage, variance components and the price of acquiring boundary inputs. Report all runs including aborts.
6. **Statistics:** use paired error contrasts on independent assembly/configuration units; report effect size with confidence/uncertainty intervals. Do not perform inference treating thousands of within-run timestamps as independent replicates.
7. **Negative results:** if the boundary-aware model offers no material gain, if overparameterized models fail, or if noise prevents junction inference, publish the negative or abstention result rather than redefine the hypothesis afterward.
8. **Decision criterion:** establish a *clinically analogous but engineering-specific* **practical improvement threshold** from instrument precision, expected sensor uncertainty and engineering application *before* confirmatory measurement. No arbitrary 1% goal.

### Consequences for current EBT design

- Keep the **12-run Q0** as a measurement-system pilot, not paper validation.
- Keep the **54-run main envelope** as provisional; use Q0 precision/mount and settling-time evidence for actual power levels and sample size.
- Use the resistor first as a characterized **heat-input artifact**, not a surrogate “junction”.
- Do not derive a calibration value from holdout temperatures and call it an independently available boundary input.
- Maintain a separate G3 MOSFET safe-operating-area and TSEP review. Do not deliberately dissipate arbitrary DC power in a switching MOSFET's linear mode.

## 7. Research-maturity verdict and G1 decision

| Question | Assessment |
|---|---|
| Is electrothermal model validation important? | **Yes.** Clearly supported by multiple original experimental and numerical studies. |
| Is the broad idea new? | **No.** The literature preempts nearly every broad originality claim in the v0.1 motivation. |
| Is there a narrowly differentiated, feasible study? | **Possibly.** A prospective, multi-remount transient boundary-transfer benchmark is narrower and better defined but novelty is **not yet demonstrated**. |
| Is a full systematic literature assessment completed? | **No.** Formal database search and full text for A01–A08 remain outstanding. |
| Is paper submission justified now? | **No.** No physical dataset, qualified reference evidence or defensible confirmed novelty. |
| Can we continue Q0 planning safely? | **Yes, unpowered and subject to site authorization.** |
| Should Issue #3 close? | **No — keep open** until A01/A02/A03/A04 and systematic search/full-text crosswalk are resolved, or explicitly document an approved access-limited scope. |

**Provisional G1 status: PARTIALLY COMPLETE / G1 NOT YET APPROVED.** This review is a substantive advancement, not the final research novelty clearance.

### Priority retrieval to unblock G1

1. Obtain full **Cnudde THERMINIC 2026** PDF from UGent institutional repository through legitimate access; report exact sensor positions, boundary variables, experimental repeats and validation tests.
2. Obtain **Ma et al. 2021** and **Bahman et al. 2017** full methods: this is directly essential for boundary-aware-model originality.
3. Request **Schulz et al. 2026** author-accepted manuscript or publisher version as legally available; inspect sample sensor and through-power prediction design.
4. Obtain full **Wang et al. 2026** and **SiC measurement guideline 2024** before making interface uncertainty or TSEP claims.
5. Conduct documented IEEE Xplore, Scopus/Web of Science and DiVA database screening; duplicate removal and citation chaining.
6. Invite an external researcher to review whether prospective boundary qualification plus remount holdout is sufficiently differentiated.

## 8. References / source locator index

- FT01 Putthong, J., Lu, D. D.-C. & Lee, C.-K. (2026), DOI [10.53941/perat.2026.100014](https://doi.org/10.53941/perat.2026.100014). Full PDF: https://media.sciltp.com/articles/2610005337/2610005337.pdf
- FT02 Zhang, Y., Evgrafov, A., Zhao, S., Kalker, S. & de Doncker, R. W. (2024), DOI [10.1109/TPEL.2024.3367854](https://doi.org/10.1109/TPEL.2024.3367854). Full accepted manuscript: https://vbn.aau.dk/ws/portalfiles/portal/669916831/TPEv1.pdf
- FT03 Farkas, G., Schweitzer, D., Sarkany, Z. & Rencz, M. (2020), DOI [10.3390/en13030557](https://doi.org/10.3390/en13030557). Full HTML: https://www.mdpi.com/1996-1073/13/3/557
- FT04 Ress, S., Farkas, G., Sarkany, Z. & Rencz, M. (2026), DOI [10.3390/en19112678](https://doi.org/10.3390/en19112678). Full HTML: https://www.mdpi.com/1996-1073/19/11/2678
- FT05 Toth-Pal, Z. & Nee, H.-P. (2026), DOI [10.3390/en19153493](https://doi.org/10.3390/en19153493). Full HTML: https://www.mdpi.com/1996-1073/19/15/3493
- T01 Bhadoria, S. (2025), KTH doctoral summary: https://kth.diva-portal.org/smash/get/diva2%3A1948439/SUMMARY01.pdf
- A01 Schulz et al. (2026), accepted-manuscript abstract: https://erickschulz.dev/publications/src/data/publications/identifiability-cauer-thermal-networks/
- A02 Cnudde et al. (2026), UGent institutional record: https://biblio.ugent.be/publication/01M3C8RKZ0XAPQVC4PAPH2Q791
- A03 Ma et al. (2021), DOI [10.1109/TIE.2020.2991926](https://doi.org/10.1109/TIE.2020.2991926)
- A04 Wang, Zhang & Wang, DOI [10.1109/TPEL.2025.3610704](https://doi.org/10.1109/TPEL.2025.3610704)
- A05 SiC MOSFET source–drain thermal guideline (2024), DOI [10.1109/TIA.2024.3352548](https://doi.org/10.1109/TIA.2024.3352548)
- A06 Urabinahatti, Ahmad & Narayanan (2019), DOI [10.1109/NPEC47332.2019.9034723](https://doi.org/10.1109/NPEC47332.2019.9034723)
- A07 Quitadamo et al. (2022), DOI [10.1016/j.microrel.2021.114416](https://doi.org/10.1016/j.microrel.2021.114416)
- A08 Bahman, Ma & Blaabjerg (2017), DOI [10.1109/TPEL.2017.2694548](https://doi.org/10.1109/TPEL.2017.2694548)

**Responsible-publication note:** Cite original sources; no full copyrighted paper PDFs or large verbatim passages are stored. Bibliographic metadata and brief critical paraphrases are stored for research use only. Research questions and hypotheses are *EBT proposals*, not claims from the listed papers.
