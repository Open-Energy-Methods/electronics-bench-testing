# EBT-Q0-007 — Source–site crossover pilot and prospective data firewall

**Rev 0.7 | DRAFT SCIENTIFIC METHOD ONLY | NO POWER LEVELS OR RUNS AUTHORIZED.** Extends (does not supersede) Q0-TP-002's provisional 12-run P1/P2 × cooling × remount planning envelope.

## Scientific separation

- Q0 physical pilot is for method development, surface thermometry, lag, mounting repeatability and selection of uncertainty/equivalence bounds; **all Q0 readings are exploratory** and cannot be relabeled as later blind validation.
- QUAL: independent reference-heating/plate-sink boundary experiments with distinct acquisition IDs and raw hashes. The measurement is apparent R(sensor, heat site, thermal stack, airflow state); not intrinsic convection coefficient.
- CAL: designated model-training temperature histories, not taken from QUAL or prospective HOLD trace values.
- HOLD: complete unseen assembly/remount and cooling configurations, reserved **before acquisition** for confirmatory R01. No HOLD temperature is available to select boundaries, filtering, sensors or model parameters.

## Pilot question and test pairing

The initial diagnostic tests the ability to separate **heat source identity** from **position** and **mount event**. For one eventually approved source power and one measured cooling state, an **illustrative crossed design** is:

| Heater identity | Source at site A | Source at site B |
|---|---|---|
| H1 | two independent full remount events | two independent full remount events |
| H2 | two independent full remount events | two independent full remount events |

This yields **8 hypothetical mounting events** in a single cooling state, **not eight performed runs, not a final powered protocol**, and two remounts per cell are only a screening choice—not necessarily statistically sufficient. Feasibility/safety may require a smaller pilot or an entirely revised source/fixing strategy. Repeat cooling/power levels only after a new safety and precision assessment.

Across each event, if geometry permits, preserve sensor positions A and B on the *same defined physical surface*, log both simultaneously, and report both fixed-A and co-moving site A/B apparent resistance. If a probe is physically relocated, it becomes an explicit sensor-remount event and must be separately identified.

## Dataset identifiers and acquisition integrity

For every prospective physical event store UTC start/end, raw data SHA-256, immutable acquisition log (including aborted events), fixture revision, heat-source identity/lot, assembly_id, mounting-event_id, site coordinates, actual T_case, T_sink and (if applicable) T_plate sensor references, ambient, fan/airflow, V_heater at heater terminals, branch I, supply/interlock status and deviations.

- Never mix QUAL/CAL/HOLD run IDs; never assign a physical event to two sets.
- Register R01 dataset partitions, model versions, threshold and predeclared exclusions **with cryptographic hash and timezone-aware UTC** before examining first HOLD outcome.
- Distinguish synthetic MODEL datasets from real PHYSICAL run records in file paths and metadata.
- Independent remount events (not the count of 5 Hz samples) are the statistical unit for mount transfer variability.
- Q0 estimates whether an equivalence band and measured uncertainty allow a credible test. Do not choose the tolerance after viewing held-out R01 data.

## Research failure gates

**FAIL-TRANSFER**: position-matched boundary has unexplained mismatch or yields unacceptable prospective prediction at independent sites/assemblies; downgrade B3 to position-specific or retrospective.

**FAIL-METROLOGY**: temperature lag, timebase errors, incomplete uncertainty or unresolved common-mode prevent validation. Do not cite synthetic 0.07°C or 5 Hz as achieved capabilities.

**FAIL-MECHANICS**: contact geometry, clamp load, sensor routing or adapter/sink thermal path cannot be documented repeatably.

**FAIL-AUTHORITY**: no explicitly authorized powered laboratory and site safety review. Student Workshop access/Canvas is only a potential mechanical fabrication route.

## Structural readiness checker

The v0.7 offline gate validator has three independent sections: fabrication evidence, powered Q0 evidence and future R01 registration. Each can be BLOCKED, or DOCUMENTS_PRESENT_HUMAN_REVIEW_REQUIRED. It never grants a GO and does not validate the truth of self-supplied references. Empty manifest remains intentionally blocked. Scientific evidence requires actual inspection and signed site documents.
