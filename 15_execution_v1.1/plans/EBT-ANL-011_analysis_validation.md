# EBT-ANL-011 — Physics, statistical inference and uncertainty plan (WP6/7)

**Status:** analytical pipeline proposed for future **measured** traces. Existing v0.4 B0–B3 and v0.6 2-D results are **SYNTHETIC ONLY**. Do not claim physical validation from current CI.

## Pre-flight reproducibility requirements

Freeze exact source code versions, model equations, time integrator, optimization seeds, dependencies and available parameter bounds. Before any R01 HOLD response, demonstrate independent numerical unit/energy convergence tests, sensitivity/identifiability diagnostics and data-conversion tests on separate synthetic examples. Preregister any allowed model selection and filtering using QUAL/CAL only.

## Measured variable separation and energy

- `T_case`: accessible device case or tab with located attachment, **not junction**.
- `T_plate`: added adapter/plate surface, if present; `T_sink`: exposed heatsink measurement location.
- `T_air`: shielded local approach ambient with declared position.
- `P_elec(t)=V_heater,terminal(t) × I_same_branch(t)` is electrical dissipation for a resistive heater, *not automatically heat entering the sink*. Leads, exposed package, clamping materials, supports, radiation and thermal storage are possible losses.
- Report `R_app=(T_surface−T_amb)/P_elec` only for an explicitly recorded *surface, steady-state criterion and condition*, including heat-path caveats. Never rename R_app as unique physical `1/(hA)` absent defensible calorimetry/boundary identification.
- Distinguish nominal optical/IR thermography (emissivity calibrated if used), contact measurements and inferred internal model temperatures; no JEDEC junction or lifetime conclusions.

## Model registry and comparison

| Model | Meaning | Boundary information / allowed fit |
|---|---|---|
| B0 | static temperature/power relation | fitted from designated CAL conditions only |
| B1 | one-RC lumped transient | CAL-identifiable parameter set and fixed model order rule |
| B2 | fixed-boundary two-node model | fit only CAL and fixed/assumed cooling parameter declared in advance |
| B3 | independently boundary-qualified two-node model | separately measured QUAL boundary, then CAL parameter fit; no HOLD-derived g, offsets, source-position adjustment or sensor tuning |

The v0.6 spatial model is an **assumption-driven counterexample**, not the actual 10 mm finned sink. Use it to design robustness ablations and energy-leak hypotheses. If a sink-injection "boundary" is source/site dependent, report the failure and downgrade B3 to *conditional geometry* or retrospective use. Do not force transferable convection if data do not identify it.

## Uncertainty and estimands

Primary estimand should be a **prospective configuration-level error difference** between preregistered models on wholly unseen assemblies; define metric sign/order and any superiority/equivalence margin using Q0, before R01. Predefine temperature response target (case/sink/plate), prediction horizon, transient time window, stratified cooling/site groups and how aborted runs appear in the denominators.

Quantify:
- V/I standard uncertainties plus contemporaneous covariance: first-order `u_P² ≈ I²u_V² + V²u_I² + 2VI cov(V,I)`; consider time aggregation and uncertainty in instrument bandwidth.
- Temperature differences and cross-channel shared reference effects: `u_ΔT² = u_surface² + u_air² − 2 cov(T_surface,T_air)` under a stated linear approximation.
- Apparent R uncertainty by propagation or Monte Carlo including P–ΔT covariance and geometry/placement/contact variation; do not invent independence of errors.
- Sensor dynamics, power-dependent calibration drift, ambient/fan variation, parameter sensitivity/identifiability and spatial mismatch.
- Report a physically justified uncertainty coverage criterion if possible; if not, explicitly describe missing reference evidence.

## Statistical unit and validation controls

The physical **independent remount/assembly** is the replication cluster; thousands of time samples from one mount are not thousands of independent experimental replicates. Estimate within-run noise separately from between-run and between-remount variance. With enough independent assembly groups, consider hierarchical or cluster-resampled intervals respecting entire remount and held-out configuration groups; otherwise report descriptive effects and wide uncertainty. Do not run ordinary pointwise bootstrap across autocorrelated time samples and claim independent validation.

Report predeclared full-holdout MAE, RMSE, bias, peak/steady error, time-dependent residual structure and prediction interval coverage (if the interval method has been specified in advance). Include uncertainty/variation by cooling, mounting, heater and source position; show both successful and failed transfers. Use no post-hoc exclusion of anomalous HOLD configurations to improve B3 results.

## Decision at G5

- **Accepted with scope:** independent physical HOLD and uncertainty support bounded surface-temperature predictive claims.
- **Conditional/negative:** transparent observed nontransferability, unresolved identifiability, cross-sensor/geometry confounding or weak uncertainty.
- **Rejected for experimental claim:** insufficient evidence, leakage, calibration/rights gap or self-selected holdouts.
- In every case distinguish code verification, measured scientific validation and unmeasured internal junction state. Do not equate software pass with physical validation.
