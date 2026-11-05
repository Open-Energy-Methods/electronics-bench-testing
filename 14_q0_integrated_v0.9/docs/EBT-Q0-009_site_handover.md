# EBT-Q0-009 — Laboratory / workshop handover sheet

**Author:** independent EBT project researcher. **Issued:** 5 November 2026.
**Document state:** PRE-APPROVAL REVIEW. **Do not operate or machine from this document.**
**Request:** assess whether the proposed low-voltage thermal fixture can be
fabricated, instrumented and tested safely in an authorized laboratory.
No KTH sponsorship, facility permission or actual physical results are asserted.

## Proposed experiment and what it is NOT

The aim is to test whether a boundary measured independently using a
reference heat source predicts future *accessible package/surface*
temperatures when heater site, attachment and cooling change. Numerical
B0–B3 comparisons and synthetic 2-D spatial counterexamples already
exist. The physical experiment is **not** a direct semiconductor-junction
temperature measurement and is **not** a JEDEC compliance test.

**Candidate reference materials (not purchased/approved):**
Fischer SK 92 100 SA black anodized extruded sink, nominal 100 × 100 ×
40 mm with 10 mm base; two Bourns PWR220T-20-10R0F 10 Ω power-resistor
candidates, assessed one heat source at a time. A 100 × 100 × 4 mm added
Al plate is a *proposed alternative*, not required or physically
verified. No drilling pattern, mounting torque, TIM stack, power level,
fuse rating, fan spacing or temperature abort value is released.

## Stage A — Mechanical-only review (no energization)

Use the actual received component, manufacturer drawing and
[mechanical source grades](../12_physical_readiness_v0.7/evidence/EBT-MEC-007_source_grades.csv).
Inspect mating surface/fin orientation, allowed fastening, heater contact
patch, surface sensor locations, electrical insulation and cable strain.
Compare directly mounting a heater to a qualified sink surface against
an extra plate; explicitly record all extra thermal interfaces.

**Recorded by qualified facility staff (currently BLANK):**
- Facility and machinery/room: ____________________________
- Induction and permission reference: ____________________
- Actual part identification / inspection reference: _______
- Selected revision and mounting process: _________________
- As-built mechanical drawing and approval: _______________
- Machine operator / reviewer and date: ___________________

Until these are real and reviewed, G2 fabrication = **HOLD**.

## Stage B — Electrical site review (no energization)

A separately authorized electrical laboratory must verify the
connection-level [v0.5 topology](../10_fixture_v0.5/electrical/EBT-EL-005_schematic_review.md)
against actual PSU, DC protection, terminal voltage acquisition,
branch-current measurement, measurement common-mode/isolation and
thermocouple grounding. A software limit does not replace the site's
independent hardware shutdown and documented procedure.

**Recorded by responsible laboratory staff (currently BLANK):**
- Approved room / site permission and supervisor: __________
- Induction / controlled access: ___________________________
- Actual PSU and metrology models/serials: _________________
- Approved schematic/revision/isolation review: ____________
- Approved DC protection and hardware cutoff: _____________
- Approved *site-specific* voltage/current/power/temp limits: _______
- Controlled thermal guarding and emergency response SOP: _________
- Sign-off / date: ________________________________________

Until real approval exists, powered Q0 = **HOLD**. The 20 W resistor
catalog rating at 25°C *case* is not a valid experiment setpoint.

## Stage C — Metrology and data readiness

Use the [23-point inspection register](../12_physical_readiness_v0.7/facility/EBT-G2-007_inspection_register.csv)
with instrument reference documents, sensor-bead attachment, measured
sensor lag/timebase, synchronized heater-terminal V/I, defined
T_CASE vs T_PLATE/T_SINK, shielded ambient, measured cooling state and
real independent remount ID. Do not assume 5 Hz logging is achieved
or adequate before the real sensor response is verified.

The [v0.8 acquisition contract](../13_q0_data_integrity_v0.8/docs/EBT-DAT-008_acquisition_contract.md)
defines \`EBT-RUN-008\`, \`EBT-SPLIT-008\`, raw byte hashes and
QUAL/CAL/HOLD identities. Preserve missing/aborted samples and a
separate deviation log; never fill real measurement fields from
synthetic example files.

## Stage D — Q0 pilot selection and review

The [controlled Q0 field sequence](../protocol/EBT-Q0-009_field_sequence.md)
lists two *alternative*, not cumulative, pilot screens:
- 12 proposed power/cooling/remount runs with **P1/P2 still unset**.
- 8 proposed heater-identity/site/remount events at one approved
  condition, if geometry allows.

Which conditions and how many runs are feasible must be decided **after**
mechanical, electrical and metrology review. Independent source/sensor
positions and uncertainty margins must be documented before any blind
confirmatory R01 holdout design. All Q0 data are exploratory.

**Research approval record (currently BLANK):**
- Selected/modified pilot protocol, version and justification: __________
- Real uncertainty/precision evidence and qualified instruments: _______
- Approved data archive location and public-data permissions: __________
- Qualified supervisor/method reviewer and date: ______________________

## Explicit dispositions

- **REVIEW-ONLY:** This packet can be circulated to authorized staff.
- **NO-GO MANUFACTURE:** No approved as-built drawing/machine permission.
- **NO-GO POWER:** No authorized energized site, wiring or operating envelope.
- **NO CONFIRMATORY DATA:** No Q0 pilot or R01 physical temperature records.
- **NO AUTOMATIC GO:** GitHub CI and schema checks never grant permission.

The documented G2/G3 authorizing parties remain the actual facility and
competent reviewers, not the research repository or its author.
