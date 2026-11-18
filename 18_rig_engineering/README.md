# EBT-RIG-001 — Modular electrothermal engineering test rig

**Baseline:** RD0 / preliminary system definition, 18 November 2026.
**Project status:** proposed engineering architecture, not a released rig.
**Purpose:** develop a reusable industrial-style laboratory platform, then use
it for EBT Q0/R01. Rig engineering and scientific validation are separate
work packages with separate acceptance evidence. Existing Q0 data contracts,
numerical models and safety gates remain in force.

The researcher reports access to measurement/instrumentation, oscilloscopes,
laser cutters, a thermal chamber, 3D printers, drilling machines, lathes,
cutters, woodworking and CNC machinery. This is a user-reported capability
list, not inspected models, completed machine training, available booking,
or permission for the proposed powered test. Obtain specific authority.

This rig is the first application of the broader [OPEP flagship programme](../19_opep_flagship/README.md). The candidate standards list below is a screening queue; selected official scope pages independently checked on 18 November are recorded in [OPEP-STD-001](../19_opep_flagship/OPEP-STD-001_extensions.csv). Full text, editions and applicability remain to be reviewed for actual equipment.

The [native CadQuery layout source and local geometry audit](cad/README.md) document four preliminary dock/cell packaging models, not manufacturing CAD.

## System baseline and controlled documents

| Document | Purpose |
|---|---|
| [RIG-SEMP-001](design/RIG-SEMP-001_systems_engineering.md) | Life cycle, requirements, design reviews, configuration management |
| [RIG-SYS-001](design/RIG-SYS-001_architecture_trade.md) | Architecture options, functional decomposition, provisional baseline |
| [RIG-DBD-001](design/RIG-DBD-001_design_basis.md) | Mechanical, thermal, electrical and measurement design basis |
| [RIG-ICD-001](design/RIG-ICD-001_interfaces.csv) | Mechanical, electrical, measurement and data interfaces |
| [RIG-REQ-001](verification/RIG-REQ-001_requirements.csv) | System requirements and verification traceability |
| [RIG-STD-001](safety/RIG-STD-001_standards.csv) | Applicability screening, not certification |
| [RIG-HAZ-001](safety/RIG-HAZ-001_hazard_register.csv) | Initial risk review, no residual-risk acceptance |
| [RIG-MFG-001](manufacturing/RIG-MFG-001_process_plan.md) | DFM/DFA, manufacturing and inspection |
| [RIG-MET-001](instrumentation/RIG-MET-001_measurement_control.md) | Measurement architecture, DAQ and control requirements |
| [RIG-VVP-001](verification/RIG-VVP-001_verification_plan.md) | Test and commissioning sequence, FAT/SAT-like records |
| [RIG-EDU-001](learning/RIG-EDU-001_training_and_report.md) | Skills acquisition, actual evidence, report chapters |
| [RIG-COST-001](manufacturing/RIG-COST-001_cost_and_make_buy.csv) | Make/buy/borrow and cost scope |
| [RIG-SURVEY-001](facility/RIG-SURVEY-001_capability_inventory.csv) | Real facility survey to fill in privately |

## Current packaging amendment

[OPEP-PKG-002](../19_opep_flagship/OPEP-PKG-002_packaway_and_process_air.md) introduces a one-box portable design target. Existing RD0 STEP layouts are historical space reservations, not the current physical design. Actual pack verification and modular redesign remain open.

## Separate design gates

RD0 system definition; RD1 system requirements review (SRR); RD2 preliminary
design review (PDR); RD3 critical design review (CDR); RD4 fabrication and
unpowered acceptance; RD5 test readiness review; RD6 controlled commissioning
and rig acceptance. All RD1–RD6 remain open. RD0 is author-prepared,
not externally accepted. RD6 is necessary but not sufficient for EBT G3:
actual permission, metrology and scientific Q0 evidence are still mandatory.

**Do not use the superseded PR #19 or the locally supplied Rev A concept sheets
as manufacturing documents.** The modular rig replaces the previous
heater-on-sink concept at SYSTEM level. The prior Fischer/Bourns parts may
still be considered for the first removable cassette; no parts are received
or chosen for procurement by this architecture decision.

CAD layout dimensions are provisional space reservations, not certified
extrusion geometry, mounting-hole locations, safety clearances or actual
thermal chamber capacity. Source geometry, equipment models, operating
limits, guards, interlocks, protective devices and manufacturing release
require inspection and competent review. No physical work is asserted.
