# OPEP-SE-001 — Flagship architecture and implementation sequence
Rev 0.1 | 2026-11-18 | proposal, no physical release.

## System boundary
A shared product/fixture and documentation baseline underlies distinct
work areas: (1) engineering design and simulation, (2) external authorized
manufacturing, (3) clean dimensional inspection, (4) approved experimental
test station, (5) external thermal chamber and any later specialist
test facility. Never machine, laser-cut or create conductive debris on
the electronics measurement station. Separate wet experiments, mechanical
load/rotating modules and electronics. Only use a common base where actual
load/temperature/electrical/service demands are compatible.

## Shared interfaces
- I-MECH: coordinate frame A/B/C, documented footprint and attachment, mass,
  loads/moments, stiffness and thermal-contact requirements, removal clearance.
  Define exact datums, port pattern and fits only after SRR/PDR inspection.
- I-ELEC: module-specific approved external power and disconnect, connector/
  harness ratings, earth/isolation review and hazard-specific protection.
  No universal unqualified power connector or common floating ground.
- I-MET: channel ID, quantity, units, sensor position, range, bandwidth,
  calibration, uncertainty, timebase and acquisition format; optional signals
  separate from EBT required raw records.
- I-DATA: module ID, hardware revision, measurement setup, test procedure
  revision, operator, raw paths/hashes, deviations and provenance.
- I-ENV: temperature/humidity/airflow or other environment, fixture material
  qualification, safe transport, actual conditions and limits.
- I-SAFE: module-specific hazard review and restrictions with independent
  protective functions; no authorization inherited from a previous module.

A removable cassette can be shared between low-load experiments if validated.
A future loading frame may need a completely different stand. Chamber test
requires actual door/shelf/heat load/feedthrough approval. No facility use
rights asserted for an equipment list.

## Phased execution and exit evidence
P0: RD0 and module registry; user survey and official machine introductions.
P1: M01 common interface prototype and M02 supervised manufacturing coupons;
    documented dimensions and repeatability. RD1/RD2 then RD3 approval
    before actual production. Compare as-built to drawing and record NCRs.
P2: M05 measurement chain, M04 electronics reference experiments and M09
    software-only control/data verification; real circuits only after review.
P3: EBT-RIG-001 first electrothermal rig commissioning. RD4 unpowered
    inspection, RD5 readiness with site-approved procedure, RD6 acceptance.
P4: M06 Q0 electrothermal scientific experiments; M07 airflow and M08 chamber
    qualification as separate planned and approved conditions. No R01 lock
    until Q0 and uncertainties actually support the experimental design.
P5: M03 separate structural fixture (only when approved load instrumentation
    and suitable bounded loading are available), further electronics/control
    modules, and production improvement. M10 links actual manufacturing and
    test data to digital product/quality records throughout.
P6: publish versioned dossiers and data; choose technical report vs research
    paper based on real evidence. Continue module-by-module instead of
    requiring every module to complete for the first release.

## Review method
Tailored systems V-model based on public ISO/IEC/IEEE 15288:2023 scope
and NASA handbook: stakeholder needs -> requirements -> interfaces ->
subsystem design -> production -> inspection -> integration -> acceptance.
Use SRR/PDR/CDR/TRR as adapted review names, not a NASA affiliation.
Design alternatives must consider function, maintenance, cost, risk,
manufacturability and actual capability. Derive acceptance limits from use,
measurement capability, tolerance budgets and verified hardware. No claim
that generic standards have been fully applied before their text and scope
are reviewed.

## Engineering release management
Document IDs, revisions, BOM, approved source files, process routing, test
records, equipment and calibration IDs, engineering change requests, NCR,
approved deviations, as-built revision and spare/maintenance records.
Module maturity: PLANNED -> DESIGN_REVIEW -> RELEASED_FOR_SPECIFIC_BUILD ->
BUILT_UNVERIFIED -> ACCEPTED_FOR_BOUNDED_USE. Only named human reviewers and
actual evidence can authorize physical stages. Software checks report
structural consistency only. RD6 never grants unrestricted operation.

## Parallel M11–M15 path
M12 passive structural modes and M13 low-level acoustic resonance may start after
module-specific review and suitable references; no energized thermal rig is needed
for the first beam. M11 starts with cold atmospheric flow. M14 is developed
continuously from analytical verification through as-built models and separately
held-out validation. M15 starts with offline replay; no direct command path
from the virtual turbine or twin to physical protection. The one-box target
remains, using one active physical module at a time and external lab instruments.
See OPEP-DT-003 for model/experiment release rules and cross-domain priorities.

## Career-informed execution crosswalk (004)
For actual portfolio delivery follow [campaigns C01–C12](career/OPEP-CAM-004_campaign_registry.csv).
Prioritize approved precision manufacture and first article, elastic structural
FEA evidence and modal measurement, reference electronics and cold-flow
experiments. Develop cold open-liquid thermal hydraulics only with a separate
approved wet area and equipment. Defer process heating, externally qualified
shock/fatigue and hazardous test domains. The campaign DVP&R and real acceptance
references augment, not replace, EBT and RD0–RD6 gates. No private application
history or employment guarantees are part of the public programme.
