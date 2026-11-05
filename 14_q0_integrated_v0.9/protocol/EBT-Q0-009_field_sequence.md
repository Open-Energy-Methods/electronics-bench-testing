# EBT-Q0-009 — Controlled Q0 field sequence for site review

**Rev 0.9 · DRAFT · no approved experimental instructions.**
This describes what to review and record, NOT how to energize equipment.
Do not manufacture or operate from these pages alone.

## Step A — mechanical access and geometry (G2, unpowered)

Record whether the KTH Student Workshop Canvas invitation was accepted and
the safety introduction completed, and precisely which machines/activities
were authorized. **Workshop invitation is not workshop machine approval.**
The Manufacturing Lab has explained that its facilities are restricted to
teaching/department research or approved Maskineriet arrangements; do not
book it as an available independent project machine.

Inspect an actual identified Fischer SK 92 100 SA or approved alternative.
The catalog describes 100×100×40 mm external envelope and nominal **10 mm
base thickness**; neither guarantees a drillable footprint. Obtain a
competent workshop review of fin/base/contact geometry, clamp/fastener
method, surface temperature access, clearances and sensor route. Then
select direct-sink or adapter as a single documented fixture revision.
The 4 mm plate, 97.2 J/K assumed lumped heat capacity and v0.6 spatial
temperature changes are hypothetical inputs, not as-built facts.

**STOP before machining** absent a released drawing, part inspection,
training/permission and responsible staff signoff.

## Step B — powered-site & measurement-chain qualification (G2, no heat yet)

Obtain **separate** written permission and an actual responsible supervisor
for low-voltage electrothermal testing. Inventory the exact isolated PSU,
protective disconnect, DC-rated protection, switching, differential terminal
voltage measurement, branch current/shunt, thermometry, logger, references,
ground/common-mode limitations and ambient/fan measurement. Prepare a site
SOP with approved emergency isolation and operating bounds. A v0.5 net
diagram does NOT replace a reviewed source-specific wiring drawing.

The instrument register must include model, serial, operating range,
calibration or verification evidence, real channel response and clock
synchronization. Do not equate v0.5's **target ≥5 Hz** with achieved accuracy
or the v0.4 assumed 4.84 s mode with a measured fixture response.

**STOP before any energized test** until signed site authority and
safety/derating review are completed. The manufacturer 20 W resistor rating
is at 25°C *case*, not an authorized test setpoint.

## Step C — explicit exploratory Q0 pilot design (G2→G3)

Two previous illustrative alternatives solve different questions:

| Concept | Factors | Planned size | Current decision |
|---|---|---:|---|
| Q0-TP-002 | two unassigned power levels × NAT/FAN × 3 independent remount blocks | 12 | **PROVISIONAL ONLY**; necessary safety envelope absent |
| Q0-007 | two heater identities H1/H2 × source sites A/B × 2 remounts at one cooling/power condition | 8 | **PROVISIONAL ONLY**; screens source/position confounding |

**Neither design is approved.** These are NOT 20 mandatory runs; the
experimenter and site reviewer must choose or restructure a feasible
sequential pilot based on real fixture geometry, thermal speed and power
limits. Power labels P1/P2 remain *unset*. Confirmatory EBT-R01's 54-run
design is a separate planning ceiling to be revisited after pilot variance.

During an eventual authorized Q0 pilot, record predeclared source/site
coordinates, whether surface channel is truly T_PLATE or T_SINK, all
assembly/remount events, electrical terminal V and branch I, ambient,
fan/airflow evidence, timebase and uncertainty. Record every abort and
deviation, not only successful plateaus. Source A and source B thermometry
should remain fixed at documented positions if the geometry supports it.

The Q0 pilot has role \`Q0_PILOT\` and **is never a confirmatory HOLD set**.
Measured input to the heater can be compared with plate energy only after
uncontrolled paths (leads, screws, radiation, supports) are assessed.

## Step D — quantitative Q0 decision / R01 planning (G3)

Only after measured evidence: quantify independent remount variability,
sensor lag, reference suitability, effective samples per plateau, ambient
drift, current/voltage timing covariance and boundary transfer
uncertainties. Predefine sample-size assumptions, stability/abort limits
and source-site equivalence bounds from actual evidence before R01.

If the boundary is not transferable, downgrade B3 to source-position-
conditional or retrospective, or redesign the hardware. Good prediction
fit alone is not identifiable physical convection.

Prepare \`EBT-SPLIT-008\` as a frozen, externally timestamped R01 QUAL/CAL/HOLD
manifest using the canonical data contract. Cross-check \`EBT-GATE-007\`
field identities with the supplied audit; seal each raw record, review the
external timestamp independently and ensure **no HOLD temperature** informs
B0–B3 model fitting, boundary selection, sensor choice or preprocessing.

## Human-controlled release summary

| Stage | Can software mark evidence-complete? | Can software grant approval? | Current |
|---|---|---|---|
| Fabricate a fixture | Structural reference check only | **NO** | HOLD |
| Power Q0 | Structural reference check only | **NO** | HOLD |
| Accept Q0 measured results | After genuine observed, reviewed data | **NO** | NO DATA |
| Begin R01 confirmatory HOLD | Requires verified prereg + measured Q0 | **NO** | HOLD |

A failed/missing item leads to review and documentation, not a software
bypass. The resulting setup may be a workshop fabrication task at one
site and a *different* authorized electrical experiment at another.
