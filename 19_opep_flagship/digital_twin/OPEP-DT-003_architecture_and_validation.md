# OPEP-DT-003 — Rig-specific digital twin and closed-loop V&V
Rev 0.2 | 2026-11-18 | RD0 proposal and synthetic reference implementation.

## Intended uses and maturity
The OPEP model represents the actual modular rig and its installed test cell,
not an industrial gas turbine. Stage D0: parameterized design model and
analytical checks; D1: verified solver models tied to inspected geometry;
D2: offline calibrated and independently validated model in a bounded domain;
D3: one-way synchronized measurement replay/operational shadow with stale-data
and configuration checks; D4: live digital twin only after justified,
tested asset-data synchronization and proper operating controls. No D2–D4
claim now; no control command to actual rig from twin or ThermoTwin-F.
The existing EBT raw/data split contract stays unchanged.

## High-fidelity and reduced-order hierarchy
1. Native mechanical CAD and inspection -> as-built CAD revision, mass,
   sensor coordinates, contact surfaces and uncertainty.
2. FEA: static stiffness and modal frequencies, then damping/FRF or prestress
   only if demanded; verified beam reference and mesh convergence; actual
   support compliance, sensor loading and connection properties.
3. CFD/CHT: cold flow pressure loss first, then approved heat addition,
   conjugate heat transfer, density properties and energy conservation.
   Check boundary conditions and independent measured inlet/flow/temperature;
   refine grids/time steps, monitor conservation/iteration and model-form
   sensitivity. No industrial Mach/pressure similarity asserted.
4. Acoustics: 1D ideal duct modes, then pressure acoustics and structural-acoustic
   coupling only if single-physics validation supports need. COMSOL
   Acoustics/Structural Mechanics modules (if licensed), ANSYS or open-source
   solver alternatives. Archive native model and tool versions if permitted;
   record boundary conditions, material sources, mesh, solver settings and
   exports. No proprietary solver has been run or licence confirmed.
5. Circuit/sensor dynamics: SPICE/reference RC, electrical measurement chain,
   thermal sensor response, anti-aliasing and time/phase alignment.
6. Reduced-order representation: physically identifiable parameters, units,
   operating domain, model versions and uncertainty. Use separately fitted
   ROM and independent validation; report extrapolation refusal. A fit to
   high-fidelity model is reduction verification, not physical validation.

## V&V with uncertainty
Code verification: analytical limits and independent unit checks; solution
verification: refinement and iterative/time integration error estimates,
minimum three systematic levels where suitable; document nonsmooth or
non-asymptotic convergence, do not blindly apply GCI. Record numerical
uncertainty, inputs, model discrepancy and measurement uncertainty separately.
Validation: freeze geometry/configuration, model version, quantity, prediction
and acceptance metric before unsealing HOLD. Use independent physical
assembly/source/operating-condition holdouts; no timestamp-level random split.
Parameter fitting and method selection use CAL only. A new revision informed
by old HOLD requires new independently collected prospective holdouts.
Report residuals and combined uncertainty only when assumptions/independence
or covariance are justified; no universal percent error pass threshold.
Every model release includes calibration provenance, validation domain,
known limitations and acceptance evidence or explicit NOT_VALIDATED state.

## Digital thread and replay
Native CAD/EDA -> BOM/material lot/process records -> inspected as-built
assembly -> instrument IDs and calibration -> synchronized raw data with
UTC origin and per-channel sample-time reference -> immutable manifest/hash ->
processing code/version -> model registry and frozen prediction -> holdout
comparison -> engineering change -> next as-built revision. Preserve aborted
runs, calibration versions, missing data and actual uncertainty. Separate
real acquisition from numerical/synthetic. Optional high-rate vibration/
acoustic streams are separate from EBT-RUN-008; no silent modification
of EBT required fields. A run manifest links module/configuration, coordinate
system, instrument evidence, sample rates, channel units/timebase, raw paths
and hashes, role, environment, model version and permitted rights.
For D3 align clocks, handle missing/stale/out-of-domain data, expose measured
vs predicted vs estimated values with uncertainty, and replay first.
A twin prediction is not a protection device.

## ThermoTwin-F interface
Create a versioned machine-readable parameter exchange, not a claim that the
small rig matches full-size turbines: measured sensor lag/time constants,
calibrated channel noise/uncertainty, applicable low-Mach component-loss
coefficients with geometry/Re/Mach and fit range, and validated reduced
thermal/structural/acoustic properties when relevant. Turbine use of these
parameters is illustrative or separately validated; no direct scaling without
similarity justification. First test offline sensor-response replay and
virtual alarms. Later consider SIL and isolated bench HIL with independently
approved I/O; FMI Model Exchange or Co-Simulation is a candidate long-term
interoperability route, not an implemented FMU. Physical rig keeps independent
shutdown. No cross-repo source changes or integration test completed here.

## Release artifacts
Model card, source code/native solver project, mesh/refinement report,
as-built geometry provenance, input and calibration data, frozen predictions,
untouched holdout data, validation and uncertainty report, scripts regenerating
figures, machine-readable parameter export, software environment, archive
hashes and rights. ISO 23247 manufacturing twin framework is a reference
architecture; ASME V&V 10/20 methodology reference; full text/applicability
review pending. See matrix and standards register.
