# EBT-R01-TP-001 — physical test campaign (PRE-REGISTERED DRAFT ONLY)

**Scientific objective:** test surface observability, cooling-boundary transfer and mounting variability in a low-voltage semiconductor cooling assembly. This file must be technically completed and approved at G3 before confirmatory acquisition.

**Design envelope:** P1/P2/P3 safe power set points × NAT/PASS/FORCED cooling × A/B mounting interface × rep 1–3 = 54 proposed assembly-runs. Actual nominal watts, component, coolant/air conditions, fixture geometry, thermal-material thickness and torque tolerance, sensor IDs, randomization, interval, stability rule, stop temperature and holdout allocation remain **TBD BY Q0**.

**Preregistered data partitions (proposed):** baseline natural cooling A as primary calibration; test across power with deliberate holdouts; at least one full forced-cooling configuration and B interface/remount events reserved for final evaluation. Avoid training on independent holdout data or using any observations from it to select model order. Store exact split plan as a signed CSV before data acquisition.

**Primary measurements:** synchronized voltage/current, case/sink/ambient surface temperatures, fan tachometer or independently verified cooling boundary input, exact mounting event, raw timestamps. IR camera supplementary only. Do not label case sensor as junction measurement.

**Per-run stages:** identification and preconditioning → protected unpowered checks → instrument zero/reference check → controlled power transient → stabilized hold or predefined duration → safe shutdown → cool-down → file hash and quality record → remount as planned. Any aborted run remains in the raw dataset, with separate status.

**Quality rules to establish in Q0:** missing sample percentage, allowed ambient drift, allowed fan deviation, electrical power stability, saturation flag, sensor detachment, repeatable stabilization, cooldown baseline, independent remount definition, maximum temperature; acceptance criterion and exclusion reasons **before** confirmatory tests.

**Outputs:** raw/clean traces, power and uncertainty budget, per-configuration R_th at explicit surfaces, transient metrics, one-RC/multi-RC comparisons, sensitivity and identifiability diagnostics, full-holdout error and prediction coverage, deviation and limitations analysis.

**Stop/abort:** any facility instruction, loss of supervision, exceeded actual device SOA, temperature/power threshold, suspect wiring, instrument overrange, protection trip, uncontrolled smoke/odor, loose sensor, fan failure. Stop state and cleanup procedures must be approved locally.
