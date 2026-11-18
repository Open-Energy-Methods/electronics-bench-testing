# RIG-SEMP-001 — Systems engineering management plan

Revision RD0, 2026-11-18. Tailored systems engineering process informed by
ISO/IEC/IEEE 15288:2023 and NASA Systems Engineering Handbook. These are
method references, not a compliance or certification declaration.

## Life cycle and review gates

| Gate | Entry | Required outputs and acceptance |
|---|---|---|
| RD0 concept | need and constraints | stakeholder needs, scope, candidate architecture, unknowns register |
| RD1 SRR | facility survey and stakeholder needs | measurable requirements, intended use, operational scenarios, standards scope, verification crosswalk, allocated functions |
| RD2 PDR | accepted RD1 | trade study and rationale, preliminary CAD envelope and loads, interface control, hazard analysis, instrumentation and cost estimates; review preliminary geometry |
| RD3 CDR | closed PDR actions, physical parts and calibrated equipment known | part-specific manufacturing drawings with GD&T, bill of materials, calculations, reviewed CAD/EDA netlists, wiring/guard/thermal protection review, inspection and test procedures; competent facility authorization |
| RD4 manufacturing readiness and acceptance | approved CDR, task-specific machine authorization | supervised manufacture, inspection, as-built drawing changes, unpowered acceptance and nonconformance register |
| RD5 TRR | RD4 acceptance, actual powered-site authority | actual safe limits, signed protection/function review, emergency procedure, calibration evidence, approved commissioning steps, responsible staff |
| RD6 acceptance | approved controlled commissioning | signed acceptance results, unresolved residual risks and operation boundaries, configuration baseline, training, maintenance and calibration intervals |

Use V-model relationships: requirements ↔ system acceptance; architecture ↔
integration verification; subsystem specification ↔ subsystem tests;
drawings ↔ dimensional and assembly inspection. Rig verification asks
whether specified functions work; scientific validation asks whether the
rig is suitable for independent boundary transfer and surface-temperature
research. Validation cannot be replaced by a geometric CAD check.

## Intended use and use cases
U01: mount/remove a reference resistive DUT at documented coordinates.
U02: conduct natural-convection and controlled forced-air experiments.
U03: transport only the eligible removable cell into a thermal chamber,
with external equipment and approved chamber feedthroughs.
U04: observe electrical waveforms, heat-input and temperature responses.
U05: repeat a physical remount without changing unrelated configuration.
U06: isolate energy, maintain hardware, export traceable test records.
U07: extend to a qualified semiconductor DUT only via a separate change review.
Explicit exclusions: mains design, battery testing, pressure systems,
high-energy switching and automated unattended operation in the first phase.

## Configuration discipline
Use hierarchy RIG-100 structural/platform, 200 DUT cassette, 300 air module,
400 electric/protection, 500 measurement, 600 control/data, 700 chamber
interface, 800 guarding/handling. Each subsystem owns numbered drawings,
parts and interfaces. Track revision, author, reviewer, date, status and
source grades. Native CAD/EDA source is authoritative; STEP/PDF/DXF are
derivatives. Control drawing revisions, part revisions, software hashes,
calibration records, NCRs, engineering change requests and as-built
configuration. A new physical configuration must map to existing EBT
fixture_revision, assembly_id, mount_event_id and run_id contracts.

Owner is independent researcher. Facility staff are potential reviewers only
if they consent; no individual is assigned or represented as endorsing this
work. Review actions need explicit closure evidence. Avoid scope creep:
a learning exercise is not a reason to add unnecessary manufacturing operations.
