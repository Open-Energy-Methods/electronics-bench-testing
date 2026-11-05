# EBT-MET-011 — Measurement assurance and Q0 pilot plan (WP3)

**Prerequisite:** G2 approved physical equipment and powered site; this plan is NOT an executable electrical SOP. Q0 is a **metrology/feasibility pilot**, never the 54-run confirmatory study.

## Traceable electrical–thermal measurement chain

| Measurand | Acquisition mechanism needing inspection | Error sources to quantify from real references |
|---|---|---|
| Heater electrical input | Differential terminal voltage across the *actual heater* and time-aligned same-branch current | voltage/current reference errors, offsets, quantization, source ripple, shunt heating, probe common-mode, simultaneity and `cov(V,I)` |
| Package surface | Attached case thermometry (not junction) | contact perturbation, spatial placement, lag, attachment reapplication, device gradients, calibration/verification limits |
| T_plate / T_sink | Surface-specific sensor map with physically inspected attachment | gradients, package/sink/plate interface, position tolerance, fin conduction; never relabel plate as sink |
| Ambient | Shielded and documented air sensor | plume/radiation bias, room drift and approach air definition |
| Cooling boundary | Defined fan speed/airflow/geometry, orientation and site surroundings | fan tach uncertainty, entrainment, recirculation, inlet gradients, alternate bypass paths |
| Time | Shared or aligned acquisition clock and event log | channel skew, missing samples, timestamp monotonicity and filter phase lag |
| Independent mounting | Actual teardown, cleaning/TIM controls and separate assembly+mount_event IDs | between-remount variability; not inflated by many time samples |

**Electrical loss note:** `P_heater(t)=V_terminal(t)I_branch(t)` is not automatically the heat into plate/sink; leads, supports, radiation, interface and stored heat remain distinct terms. Any inferred sink-to-air resistance is location/power/geometry conditional.

## Sequence — software preparation before energization

- Inspect real instrument model/serials, calibration/reference suitability, channel ranges, grounding and readout units. The source v0.8 `EBT-RUN-008` metadata contract is authoritative. Abort and missing readings are recorded; do not impute them.
- Prepare **site-reviewed** zero/offset, wiring isolation, protection, shutdown, sensor-contact and independent V/I timing checks. No power on until site approval and local operating procedure.
- Determine usable sample interval from *measured* sensor/mount response and logger capabilities. The prior 5 Hz target and 4.84s synthetic mode are not achieved specifications.
- Record a justification for temperature and power uncertainty that includes correlated errors and between-mount scatter; do not assert traceability without genuine instrument/reference evidence.

## Q0 screening choice: two illustrative alternatives, NOT cumulative

- **PILOT-A:** provisional 2 **unset** power levels × 2 defined cooling states × 3 independent **physical** assembly/remount blocks = 12 run observations. Four treatment traces *within one unchanged mount* may share its mount_event ID and are repeated measures, not 4 independent mounting samples.
- **PILOT-B:** provisional 2 heater identities × 2 physically distinct source sites × 2 independent mounts = 8 event observations at one approved nominal cooling/power configuration, if geometry supports the crossover.
- **Decision:** site reviewer selects/adapts A or B, or stages the studies in a controlled amendment, using actual fixture constraints and attainable precision. No assumption that 12+8=20 required experiments. Fixed sensor coordinates and their physical measured surface are logged.

## Pilot output and G3 trigger

Prepare a Q0 data report with: observed channel noise, response lag, baseline/ambient drift, power stability, fan state, independent remount variance, abort/sensor-loss rate, uncertainty components/covariance, energy-path plausibility and physical source/site boundary transfer evidence. A separate independent review decides if B3 boundary use is physically defensible. Negative findings must remain visible.

**Only after real Q0:** choose study power levels and geometry, set minimum effect/equivalence margin, determine independent assembly count with a defensible precision/power criterion, choose randomization and stopping, and decide whether to freeze R01. If no physical or metrological precision adequate, report Q0 limitations and revise the experiment or use a technical-report fallback. Q0 output cannot be treated as a held-out R01 validation dataset.
