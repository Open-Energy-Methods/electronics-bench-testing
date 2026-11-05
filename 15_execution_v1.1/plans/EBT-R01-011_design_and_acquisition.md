# EBT-R01-011 — Confirmatory design, data partitions and acquisition (WP4–5)

**Status:** PRE-REGISTERED-DRAFT ONLY. This is a forward execution specification, not a locked experiment, data, or permission to power hardware. Baseline: [EBT-R01-TP-001](../../03_campaigns/EBT-R01/main_test_plan_draft.md) and [54-row matrix](../../03_campaigns/EBT-R01/provisional_run_matrix.csv).

## Design under review, not silently approved

The original 3 power placeholders P1/P2/P3 × 3 cooling labels NAT/PASS/FORCED × 2 interface levels A/B × 3 physically independent remount repetitions = **54 proposed assembly-runs**. None of these power levels, material treatments, fan conditions, positions or permutations has been physically approved. The *actual* run count and design must be justified with Q0 observed variances and resources. The initial 54 should not become an arbitrary mandatory count.

### Factor reconciliation work required before G3

1. **Cooling conditions:** Q0 data schema only allows `NAT`, `FAN`, `OTHER_DOCUMENTED`; the baseline matrix's `NAT`, `PASS`, `FORCED` represent a different proposed experimental vocabulary. Define what the *physical* NAT/PASS distinction is, including actual sink contact, orientation, fan presence/absence and ambient, before claiming they are three distinct boundaries. Only map FORCED to `FAN` if controlled/measured fan cooling is present. If PASS cannot be differentiated, reduce or rename the factor *before lock* with a change record.
2. **Interface vs location:** baseline `interface_level A/B` describes a mounting/interface treatment; Q0 crossover `source_site A/B` describes a *heater position*. Make independent columns, record exact physical geometry and do not swap their meanings. If a source is moved and remounted, log a new mounting event.
3. **Power levels:** select only after actual resistor part, case-temperature derating, supply, attachment and local stop limits have been reviewed and approved. `20 W` at 25°C case from Bourns is not the permissible Q0 or R01 setpoint.
4. **Replications:** one independent remount is a physical teardown and reassembly. Runs that share a single mount event but change power/fan are repeated measures; do not count them as independent mounting replicates. Treat run order, conditioning and cooldown as correlated within mount.
5. **Semiconductor extension:** a future MOSFET is a separate DUT/phase, not interchangeable with the reference heater; part-specific DC/pulsed SOA, linear-mode suitability and electrical measurement justification are mandatory.

## R01 partition roles and locking

**Q0_PILOT** stays a separate exploratory dataset. **QUAL** is independent cooling-boundary characterization; **CAL** is model parameter fitting; **HOLD** is prospective out-of-configuration evaluation. The `EBT-SPLIT-008` format requires all three registered roles, non-overlapping run IDs, and holdout assemblies disjoint from QUAL/CAL. Mount event identities cannot be reused across different roles. A single unchanged physical mount can contribute several different acquisition runs *within the same role*, if the protocol permits.

The G3 preregistration packet shall contain:
- final exact heater/sink/fixture revision and sensor map; physical treatment definitions, permitted site + time windows;
- study design and randomization unit, anticipated independent assembly events, explicit cooling/site/interface assignment, conditioning/thermal baseline return and planned acquisition lengths;
- observed Q0 covariance/variance components, primary error metric, pre-set equivalence or improvement margin and sample-size/precision analysis;
- model candidates/frozen versions, hyperparameter and order-selection rule based exclusively on QUAL/CAL, and how independent boundary measurements enter B3;
- list of HOLD *entire independent assembly/configuration IDs* plus handling of missing/aborted/repeated acquisitions;
- calibration and QC criteria, analysis exclusions and escalation/stop decisions fixed *before* any HOLD response is inspected;
- externally verifiable preregistration reference and protocol SHA-256; independent reviewer verification of actual publication/commit time;
- record-level UTC lock instant `Z` or `+00:00`, plus consistent v0.7 gate record and human sign-off.

A hash and locally declared time by themselves do not prove prospective registration. Do not expose protected facility staff/records in a public lock without permission.

## Operational flow once separately authorized

- Inspect real signed site SOP, supervision, permitted heater/fixture revision, zero/reference checks, protective cutoff and actual raw-archive space **before each** acquisition.
- Record each run's metadata in canonical `EBT-RUN-008`: unique run ID, stable mount identity for unchanged physical mounting, cooling reference, `T_PLATE/T_SINK` meaning, UTC start, actual measured V/I and temperatures, deviation reference and raw/seal hashes. **No prespecified safe wattage is provided here.**
- Record deliberate shutdowns, aborts, samples missing due to logger faults, out-of-limit events and loss of supervision as raw records, not deleted failures.
- Save original raw bytes before transforming data. Seal the raw file and metadata and independently verify. Never reseal edited raw records under their old ID.
- Maintain clean role separation and blinded HOLD. Do not use HOLD trace shape even to choose sensor lag filter, ambient correction, boundary estimator or model architecture.
- Final G4 report lists attempted / successfully acquired / excluded / abandoned by *run and independent assembly*, and reasons, including data rights and unresolved metrological limitations.

## Scientific decision outcomes

**Proceed to G5** only when Q0/G3 approvals, independent HOLD and real uncertainty evidence are complete. **Restrict claim** if some boundary conditions not physically distinguishable or precision too low; **report negative transfer** if B3 performs worse; **stop/redesign** if G2 safety or source-location repeatability fails. A reduced study requires prospective amendment, not after-the-fact relabelling of the 54-row planning table.
