# EBT-MET-005 — Independent boundary-transfer qualification protocol (DESIGN ONLY)

**No powered work authorized.** This protocol is the engineering realization of Issue #9 and v0.4's falsifiable boundary-transfer problem.

## Different questions that must not be conflated

1. **Apparent sensor-to-air resistance:** \(R_{app}=(\overline{T}_{plate}-\overline{T}_{air})/\overline{P}_{heater}\) from a separately qualified source at a fixed position, in a defined airflow and ambient. This is **not** the total thermal network branch \(R_{sa}\) unless the identified lumped model and heat paths warrant that equivalence.
2. **Location transferability:** whether an apparent boundary from source at position A predicts temperatures when an equivalent heater is placed at B. Source spatial footprint and plate conduction matter.
3. **Technology transferability:** whether the resistive heater's boundary can predict surface temperatures from a MOSFET package with potentially different heat deposition and internal paths. This requires independently established device power and additional R01 approvals.

## Proposed dataset identities (each with immutable hashed raw logs)

- `QUAL-SITE-A`: sink/plate/reference heater only; qualify independent boundary before model target; multiple power and airflow conditions **within a site-approved safe envelope**; record plate/site/sink sensor locations, orientation, fan speeds, ambient and input power.
- `CAL-HEAT-A`: model calibration for designated heater at A with boundary state; data available for fitting B0–B3 only under preregistration.
- `TRANSFER-HEAT-B`: different source position B and full remount, same physical sink and orientation; **true holdout**, with no B-model input fitted from its temperatures.
- `QUAL-REPOSITIONED`: separately characterize whether relocation A→B changes apparent boundary (before unsealing `TRANSFER-HEAT-B`, or from prior pilot-only data). If relocation changes it, use position-specific qualified models or declare boundary transfer invalid.
- `HOLD-COOLING`: entire unseen cooling condition with independently measured fan/airflow and a separate `QUAL` dataset; no temperature trace from the target case is used to choose the B3 boundary value.

Chronological acquisition records must prove that qualification was completed **before** holdout observations were inspected. A new remount must have a new `assembly_id`, and a sensor-remount must be disclosed even if the heater remained attached. Pilot data do not count as confirmatory held-out evidence.

## Statistical test & failure gates

- Before data, define equivalence band \(\delta_R\) from instrument uncertainty plus acceptable application prediction degradation. Do **not** choose after seeing data.
- Compare mean `R_app` and paired temperature-response error over **independent mount/session blocks**, not time samples as independent replicates. Report position effect and its uncertainty.
- Evaluate B2 (fixed-boundary), B3 (prequalified-boundary) and a diagnostic oracle-B3 *only on synthetic studies*; an oracle physically inferred from target temperatures is forbidden as a prospective model.
- `FAIL-TRANSFER`: A and B have materially different apparent resistance for the planned predictive purpose; B3 becomes position-conditional or retrospective.
- `FAIL-IDENT`: sensor lag and 1–5 Hz or actual acquisition accuracy cannot identify the intended dynamic modes; simplify model or narrow time scope.
- `FAIL-METROLOGY`: missing uncertainty chain, unstable supply, input power not at source terminals, unexplained heat paths, incomplete data acquisition or failed interlock → no confirmatory run.
- `FAIL-REPRO`: independent remount variance greater than the predicted effect → increase replicates or downgrade claim; do not cherry-pick stable samples.

## Explicit resource requirements

Multiple accurate contact temperature channels, verified reference for each, simultaneous or timestamp-correlated heater V(t) and I(t), independently qualified device/plate heat input position, documented fan/ambient state, actual supply protection, independent supervised safety shutdown, manufacturer's thermal limits and dedicated lab permission.

**Q0 must demonstrate** an operational protocol with measured uncertainties and approved holdout logic. This document alone is not a calibration report, site SOP or approval to power the test rig.
