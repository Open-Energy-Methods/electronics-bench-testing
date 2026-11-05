# EBT-Q0-009 — Consolidated Q0 engineering review package (v0.9)

**Document control:** 5 November 2026 · independent EBT project · research predesign only.

**GATE STATUS: HOLD for machining; HOLD for energized testing; NO PHYSICAL RESULTS.**
This is a single navigation, specification and audit entry point into the
existing v0.5–v0.8 modules. The package is NOT a facility-approved laboratory
SOP, released drawing, installation design or certified instrument record.

## Canonical source-of-truth order

1. **Safety and local authority:** actual signed facility permissions, site SOP,
   equipment specifications, competent mechanical/electrical review and KTH
   training are REQUIRED but **NOT PRESENT**. No repository file overrides these.
2. **G2 fabrication and powered-stage evidence:** the v0.7
   [23-check inspection register](../12_physical_readiness_v0.7/facility/EBT-G2-007_inspection_register.csv)
   and [unfilled structural gate record](../12_physical_readiness_v0.7/templates/EBT-GATE-007_record_UNFILLED.json).
   Its validator can flag missing documents but never grants GO.
3. **Mechanical architecture:** [v0.7 physical decision](../12_physical_readiness_v0.7/docs/EBT-MEC-007_fixture_architecture_decision.md)
   supersedes v0.5's *assumed requirement* for a 4 mm adapter, **not** the v0.5
   concept drawings. Direct-to-sink is the preferred candidate for REVIEW,
   subject to real component inspection. Any v0.5 toolpath remains unreleased.
4. **Model evidence:** v0.4 B0–B3 model definitions and
   [v0.6 conditional 2-D plate sensitivity](../11_spatial_transfer_v0.6/README.md).
   The former defines numerical comparisons; the latter illustrates how
   source/sensor locations and unmodelled heat paths may confound apparent
   resistance. Neither defines an actual sink convection coefficient.
5. **Pilot methods:** [EBT-Q0-009 field sequence](protocol/EBT-Q0-009_field_sequence.md)
   is the CURRENT Q0 draft. Earlier Q0-TP-002's **12-run power/cooling/remount**
   matrix and Q0-007's **8-event source/site crossover** are alternative
   feasibility sketches, not two simultaneous required campaigns.
6. **Data identities and preregistration:** the
   [v0.8 EBT-RUN-008 / EBT-SPLIT-008 data contract](../13_q0_data_integrity_v0.8/docs/EBT-DAT-008_acquisition_contract.md)
   is authoritative for raw rows, run metadata, role partitions and hashes.
   The [mapping](interfaces/EBT-Q0-009_roles_and_schemas.md) connects it to
   G2/G3's v0.7 structural gate record without creating a competing schema.
7. **Current external status:** the [facility tracker](../08_project_controls/facility_access_tracker.csv)
   records Student Workshop Canvas invitation and Manufacturing Lab restrictions.
   Neither authorizes Q0 electrical testing; ELAB is still unconfirmed.

## Review and execution preparation

- [EBT-Q0-009 integrated laboratory sequence](protocol/EBT-Q0-009_field_sequence.md)
- [Conflict and interface review](docs/EBT-Q0-009_integration_review.md)
- [Evidence still required](docs/EBT-Q0-009_open_evidence.md)
- [Machine-readable mapping](interfaces/EBT-Q0-009_crosswalk.csv)
- [v0.7↔v0.8 dataset/lock contract](interfaces/EBT-Q0-009_roles_and_schemas.md)
- [Unfilled R01 plan template](templates/EBT-SPLIT-009_R01_UNFILLED.json)
  and [unfilled future physical-run metadata](templates/EBT-RUN-009_PHYSICAL_UNFILLED.json).
  These are intentionally **invalid for acquisition** until real entries and site approval exist.
- [Offline interface audit](tools/audit_interfaces.py), with automated tests.

## Offline verification

From repository root, Python 3.11+:

\`\`\`bash
python -m unittest discover -s 14_q0_integrated_v0.9/tests -p 'test_*.py' -v
python 14_q0_integrated_v0.9/tools/audit_interfaces.py
\`\`\`

An expected outcome is **BLOCKED_NEEDS_PHYSICAL_EVIDENCE**; this is not CI
failure. Numerical and data-contract tests live in their source modules and
must also pass. No real sample files or operating voltages are included.

### Project research integrity

Always separate \(T_{\rm case}\), \(T_{\rm plate}\), \(T_{\rm sink}\) and ambient;
never convert apparent \(R_{\rm app}=\Delta T/P_{\rm heater}\) into intrinsic
convection without a justified energy-path model. Keep QUAL, CAL and unseen
HOLD data disjoint; Q0 pilot remains exploratory. No safe current, voltage,
power, sample rate, fan duty or statistical equivalence margin is prescribed
by these unqualified documents. The later MOSFET remains a separate SOA-gated
research article, not an electrically interchangeable heater.
