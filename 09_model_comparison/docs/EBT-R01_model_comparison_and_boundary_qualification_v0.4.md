# EBT-R01-MDL-001 — Model comparison and independent boundary-identification audit

**Version 0.4 · 5 November 2026 · EBT-R01 / EBT-PMP-001 v1.0**  
**ALL RESULTS SYNTHETIC.** No physical experiment, KTH laboratory authorization, calibration traceability, measured semiconductor junction temperature, identified real device properties or confirmed publication novelty.

## Decision

The previous v0.1 boundary-aware simulation directly supplied the known synthetic true cooling resistance. This is an optimistic proof of concept, not independent identification. Version 0.4 separates **(1) natural-cooling training**, **(2) independent synthetic sink-heater boundary qualification**, and **(3) withheld cooling and remount runs**. It examines both favorable and adverse boundary-transfer cases.

**B3 is retained as a conditional comparator, not selected as a validated superior physical model.** An extra boundary input can improve predictive temperature error if its heat path and geometry are transferable. An independently measured but *nonrepresentative* boundary can make predictions substantially worse.

## 1. Thermal network and observation contract

The model has package/surface and sink states. It is **not a junction-temperature model**. For package temperature Tp, sink temperature Ts, ambient Ta, package heating Pp and optional independent sink heating Ps:

$$
C_p\dot{T}_p=P_p-\frac{T_p-T_s}{R_{ps}}-\frac{T_p-T_a}{R_{pa}},\qquad
C_s\dot{T}_s=P_s+\frac{T_p-T_s}{R_{ps}}-\frac{T_s-T_a}{R_{sa}}.
$$

The main series two-node models omit the package-to-air Rpa path. A deliberate synthetic failure case adds Rpa=8.5 K/W. Source inputs are zero-order held and integrated by an exact sampled matrix exponential. Resistance and capacitance are constrained positive.

Actual package and sink temperatures would be *location-dependent contact measurements*. Uniform node temperatures, linear heat transfer and negligible sensor mass/lag are model simplifications, **not verified properties of a real assembly**.

### Model inventory and fair information accounting

| Model | Structure and fitted parameters | Training data | Validation availability |
|---|---|---|---|
| **B0** | Static apparent case-to-ambient resistance; 1 parameter | Late-powered natural-cooling case response and power | **Late powered bias only**; cannot score as transient model |
| **B1** | One-node fixed-boundary RC; 2 parameters | Natural-cooling case sensor and power | Target power and ambient; predicts case |
| **B2** | Two-node fixed-boundary RC; 4 fitted parameters (Rps, Cp, Cs, Rsa) | Same natural-cooling package **and sink** traces as B3 | Target power and ambient, **no target boundary information** |
| **B3** | Two-node boundary-qualified RC; 3 fitted parameters (Rps, Cp, Cs) | Same B2 traces **plus a separate natural-cooling boundary qualifier** | Target power, ambient **and separately qualified target-cooling boundary** |
| **B2 case-only ablation** | Two-node fixed network with 4 parameters | Package-only sensor, no sink channel | Conditioning diagnostic only, not a primary accuracy comparator |

**Information asymmetry is unavoidable:** B3 receives *additional measurements* that B2 does not. A positive B3 result is evidence for the conditional value of that input, not proof of a better optimizer or new circuit theory. Real comparisons must disclose equipment time, qualification measurements, reference quality and uncertainty budget. Fitting code structurally rejects records not marked as training; a test changes withheld temperatures by 1000°C and verifies that forecasts are unchanged.

## 2. Actual boundary-identification method to qualify during Q0

A separate, metrologically reviewable heater would inject heat into a defined sink location with the **package-side source off**, ideally on the identical proposed sink, guard and airflow geometry. The operator would record the heater's own synchronized voltage and current, sink and shielded ambient temperature, sensor coordinates and fan/tach state. The reference heat source requires a separate site-reviewed **electrical schematic, protection, qualification and safe operating range**. This document is NOT a wiring diagram or energized-test authorization.

For an independently recorded steady plateaulike period:

$$
P_{\mathrm{inj}}(t)=V_{\mathrm{heater}}(t)I_{\mathrm{heater}}(t),\qquad
R_{\mathrm{app}}=\frac{\overline{T_s}-\overline{T_a}}{\overline{P_{\mathrm{inj}}}}.
$$

**This is apparent sink-point-to-air resistance in the qualification geometry, not measured convection coefficient h, not a universal heat-sink property, and not necessarily the true branch Rsa.** A package-to-air bypass gives, only for this special linear two-path steady model:

$$
R_{\mathrm{app}}=\left(\frac{1}{R_{sa}}+\frac{1}{R_{ps}+R_{pa}}\right)^{-1}.
$$

The separate sink heater changes heat-flow distribution from actual package heating. Independent files alone do not demonstrate transportability. A pilot must challenge geometry, lead loss and sink-gradient differences **before the prospective model-validation holdout**. No boundary may be back-fitted from a held-out package or sink trace if the result is called prospective prediction.

### Proposed qualification chronology

1. Obtain facility authorization for powered testing, complete its induction and full electrical safety/grounding/thermal-stop review; Student Workshop fixture access does not authorize energized work.
2. Identify actual heater part, case derating, sink, mounting, guard and safety limits; create dimensioned mechanical and connection-level electrical drawings.
3. Inspect sensors, electrical instruments and reference evidence; establish the actual heater terminal voltage measurement, branch current, heat-leak paths, thermometry reference, timebase, contact position, sensor lag and airflow measurement.
4. Collect separate, timestamped and hashed sink-injection qualification sessions for each NAT/FAN cooling configuration. Consider at least two facility-approved power levels to examine thermal nonlinearity; no actual watts or durations are authorized by this draft.
5. Define plateau using a predeclared slope/drift criterion grounded in measured reference uncertainty and actual thermal time scales, not a fixed arbitrary waiting period.
6. In Q0 only, compare package- and sink-side heating temperature maps to establish whether a single scalar boundary can be transported between them, and whether apparent resistance depends on source location or power.
7. Lock the boundary coefficients, uncertainties, model source, calibration data, model-selection rules and complete remount/cooling holdout allocation *before* any confirmatory acquisition.
8. If geometry/power transfer fails, **do not claim B3 blind prediction**: revise the model and qualification or downgrade the analysis to retrospective description.

### Uncertainty

For measured P=VI:

$$
u^2(P)=I^2u^2(V)+V^2u^2(I)+2VI\operatorname{cov}(V,I).
$$

For an apparent resistance (Ts−Ta)/P:

$$
u^2(R_{\mathrm{app}})\approx
\frac{u^2(T_s)+u^2(T_a)-2\operatorname{cov}(T_s,T_a)}{P^2}
+\frac{(T_s-T_a)^2u^2(P)}{P^4}.
$$

The synthetic implementation aggregates four independent simulated qualification-run averages for each cooling state, adds an assumed **0.07°C standard uncertainty per temperature reference** and an assumed **1% relative electrical power standard uncertainty**, and uses the between-run scatter rather than assuming every timestamp is an independent replicate. Common reference uncertainty does not decrease with run count.

A local finite-difference sensitivity to boundary resistance estimates the small-signal effect of that assumed measurement uncertainty on predicted package/sink temperatures. **This is not a calibrated model prediction interval**: fitted-parameter covariance, geometric discrepancy, sensor placement, shared biases, nonlinear airflow and between-remount variation remain outside this narrow calculation.

## 3. Runnable synthetic design

Illustrative truth uses Rps=0.48 K/W, Cp=12 J/K, Cs=65 J/K, NAT Rsa=2.8 K/W, FAN Rsa=0.95 K/W, ambient=24°C, sample interval=20s, independently randomized temperature noise=0.09°C per reading plus 0.07°C per run offset. These numbers—including simulated heating powers of 3, 4 and 5 W—**do not specify actual safe device powers**.

The fit uses two natural-cooling traces on one assembly. Four future temperature responses are withheld: natural unchanged interface, forced unchanged interface, natural changed interface and forced changed interface, each assigned a distinct *synthetic* assembly ID. Interface change alters Rps to 0.78 K/W; fitted model parameters are not adjusted after viewing it.

The scenarios are:

- **Ideal:** correct series thermal network and transferable independently qualified NAT/FAN boundary.
- **Bypass:** unmodeled package-to-air Rpa=8.5 K/W, meaning sink-injection apparent resistance is not the physical Rsa branch.
- **Mismatched:** deliberately extreme *negative control*: the forced-cooling qualification assembly has four times the target forced-cooling sink-to-ambient resistance. This is a logical stress test, not a typical measured fixture offset.

### Primary single-seed result — withheld forced-cooling package-transient RMSE

| Synthetic mode | B1 fixed 1RC | B2 fixed 2-node | B3 qualified-boundary 2-node |
|---|---:|---:|---:|
| **Ideal** | 5.526°C | 5.489°C | **0.188°C** |
| **Bypass** | 3.599°C | 3.591°C | **0.477°C** |
| **Mismatched boundary** | 5.526°C | **5.489°C** | 7.774°C |

With a changed interface under forced cooling, B3 still has 0.976°C package RMSE in the ideal scenario. A cooling-boundary update does not identify the unobserved interface change.

In the bypass scenario, natural-cooling qualification estimates apparent 2.153 ± 0.035 K/W despite the synthetic **physical** sink-air branch being 2.8 K/W. The reported ± quantity is an *assumed synthetic standard uncertainty*, **not an accuracy or calibrated 95% bound**. This is a strong counterexample to equating prediction utility with identification of physical parameters.

### Twenty-five synthetic noise seeds

Positive Δ means B3 lower RMSE than B2 on the forced, unchanged-interface holdout.

| Case | Median Δ RMSE(B2)−RMSE(B3) | 5–95% seed quantiles | Seed outcomes favoring B3 |
|---|---:|---:|---:|
| Ideal | +5.434°C | +5.203 to +5.544°C | 25/25 |
| Bypass | +3.270°C | +3.027 to +3.480°C | 25/25 |
| Mismatched | −2.337°C | −2.403 to −2.291°C | 0/25 |

These quantiles represent synthetic noise perturbations with otherwise fixed assumptions, **not experiment-to-experiment variability, statistical confidence intervals or evidence of real hardware significance**.

### Sensor information and dynamic-resolution warning

The assumed network has approximate natural-cooling thermal modes of **4.84s and 216.52s**, yet the synthetic logger samples every **20s**; the fastest mode is seriously undersampled. In one example, the log-parameter B2 Jacobian condition number is **44 with both package and sink sensors**, versus **approximately 9,667 with package-only data**. This does not prove physical uniqueness even with both channels. Under bypass, B3's Cp fit reaches the enforced lower bound while the local Jacobian condition exceeds 800. Good temperature RMSE can coincide with nonphysical parameter recovery or structural misspecification.

**Q0 implication:** before picking sampling rate or fitting internal nodes, establish sensor response and actual observable time constants. Faster logging cannot recover physical transients hidden by sensor lag.

## 4. Threats to scientific validity

- **Model-data leakage:** target-response temperatures used to set the boundary or model order invalidate prospective claims.
- **Boundary transport:** qualification heat source geometry, sink gradients, screws/leads/PCB heat paths, ambient radiation and fan fields can make a scalar sink-to-air resistance nonportable.
- **Power fidelity:** PSU-level V×I can include shunt, wire and electronics dissipation rather than heat injected at the intended thermal node.
- **Temperature fidelity:** mounting pressure, bead thermal mass, electrical probe ground and sensor offsets can distort inferred time constants; no current metrology budget has been verified.
- **Data information:** B3's extra instrument data and additional qualification effort must be costed before attributing an advantage to mathematical model structure.
- **Parameter nonidentifiability:** a low RMSE and a finite local Jacobian condition do not prove unique thermal path properties. Future profile-likelihood/multistart and nonlinear spatial checks may be needed.
- **Pseudoreplication:** each true physical remount is the experimental unit, not a thousand dependent logger samples; simulated noise seeds are not physical remounts.
- **Uncertainty undercoverage:** small u(Rapp) excludes huge potential structural geometry mismatch and correlated sensor errors.
- **Research novelty:** boundary-dependent compact models, measurement-position effects, interface variation and identifiability have been published already. Formal G1 literature screening and external review remain pending.

## 5. Gate decisions and execution

**G1 / novelty:** OPEN; see EBT-LIT-003 and the unresolved Ma, Cnudde, Bahman and Schulz methods. Relevant earlier work includes Rose & Menzel (2022), [DOI 10.1002/gamm.202200010](https://doi.org/10.1002/gamm.202200010); Ma et al. (2021), [DOI 10.1109/TIE.2020.2991926](https://doi.org/10.1109/TIE.2020.2991926); Putthong et al. (2026), [DOI 10.53941/perat.2026.100014](https://doi.org/10.53941/perat.2026.100014).

**G2 / powered Q0:** NOT AUTHORIZED; site permission, exact component suitability, calibrated/verified instrument chain, appropriate electrical protection, complete drawings and supervisory conditions remain unknown.

**G3 / experiment lock:** NOT READY; the physical pilot must determine model time scales, accepted reference uncertainty, external heat-loss fraction, actual boundary compatibility, safe power settings and statistical replicates.

**Next unpowered design action:** add and critically review a dimensioned *separate sink-injection qualification port* plus sensor-location map on the same intended sink assembly. If the geometry cannot be made representative and uncertainty cannot be assessed, B3 is **not** eligible for claims of prospective boundary prediction.

## 6. Reproduce

Change into the 09_model_comparison directory and install NumPy/SciPy/Matplotlib using the existing project requirements file.

- Run all 16 new physics/identifiability/leakage/uncertainty/stress checks with the Python unittest test discovery.
- Run the synthetic comparison module to generate a JSON report for ideal, bypass and mismatched scenarios.
- Run the 25-seed synthetic robustness module and the plotting module for two generated PNG charts.

The source and tests in this directory are intended to remain versioned with future experimental evidence. Numerical results should be checked with tolerances across numerical-library versions rather than byte-equality. **No measured data or human-signoff state has changed.**
