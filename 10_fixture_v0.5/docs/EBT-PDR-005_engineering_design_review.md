# EBT-PDR-005 — Physical test rig preliminary design review, Rev. 0.5

**Date:** 2026-11-05. **Release:** research predesign only, **NOT APPROVED FOR FABRICATION OR ENERGIZED TESTING**. Parent EBT-PMP-001 v1.0 and Issue #5; independent prospective boundary-transfer test Issue #9.

## 1. Requirement and method

The project must test whether the *apparent* sink-to-ambient boundary from a reference heat source is adequate for **prospective** surface-temperature predictions from an independently heated package. This is not a junction-temperature measurement. Model parameters and boundary input must not be estimated using reserved target temperature traces. The research design is contingent on legitimate facility access and equipment.

**Physical subassemblies:** A100 100×100×40 mm catalog heatsink candidate, P100 100×100×4 mm candidate aluminium interface plate, two relocatable 10 Ω TO-220 thick-film heaters with individually identified mounting footprints, surface/near/far/air thermometry, optional separately supplied fan, approved isolated current-limited bench supply and instrumented voltage/current measurement. The proposed plate may itself introduce unmeasured spreading/interface resistance: that is a risk to characterize, **not** a presumed negligible element.

## 2. Mechanical concept and status

Heatsink candidate: **Fischer SK 92 100 SA**, actual external envelope 100×100×40 mm per distributor; the claimed 1.4 °C/W nominal listing cannot be extrapolated to arbitrary natural/forced airflow. Prior to machining obtain manufacturer's extrusion cross-section/flat contact-face dimensions and review its base material thickness, fin channels, direction, thermal gradient, allowed holes and finish.

Plate candidate: **100×100×4 mm aluminium** — deliberately a provisional stock geometry, NOT an ordered or verified part. Origin at plate centre. H1 site x=−25 mm, y=0 mm; H2 site x=+25 mm, y=0 mm. Package hole centres x=−25,+25 mm, y=+4.8 mm *only* under the drawing's package-body-centred convention derived from the nominal Bourns 14.6 mm body and 2.5 mm top-hole offset. This absolute positioning and all tap/drill/slot dimensions are **UNRELEASED**. Package body about 10.1 mm wide ×14.6 mm tall, and mounting hole Ø3.6 mm; M3 screw, flatness and torque must be verified. Respect sensor attachment clearance and insulated leads. Adhesive or Kapton on unknown surfaces is not a qualified mounting method by itself.

**Sampling places, coordinate proposals, not drilling instructions:** K-CASE1 (H1 package face near x−25,y−3), K-CASE2 (H2 face x+25,y−3); K-SINK1 (x−25,y−17), K-SINK2 (x+25,y−17) on plate or a verified sink thermometric pad; K-SINKFAR (0,+32) optional; K-AIR shielded >several cm away at **site-defined** position. The exact meaning of “sink” versus “plate” temperature must be decided after geometry inspection. If a sensor measures **plate** temperature, label it `T_plate`, not `T_sink` and do not silently treat the plate as an isothermal sink.

**Reference architecture:** Study different heater **positions** as independent factor; do not assume that H2 on the right is the same boundary as H1 on the left. A stronger geometry equivalence test is to mount and energize one characterized heater **sequentially at the same physical site** as the later target, with independent recorded assembly/reassembly and measurement history. Do **not** energize both heaters in one “single-source” qualification run. Include swapping H1/H2 sites to separate heat-source identity from position effects. The later MOSFET is a separate gated test article with SOA and TSEP requirements.

## 3. Electrical/DAQ topology

The [vector electrical schematic](../drawings/EBT-EL-005_measurement_schematic.svg) and [connectivity ledger](../electrical/EBT-EL-005_nets.csv) are **reviewable predesigns**. They identify the isolated PSU, independent disconnect, approved protective device, center-off source selector, Kelvin voltage taps on each heater, current transducer/shunt, differential instrumentation and separately powered fan. The drawing contains **no final protective-device ratings or terminal catalog numbers**: these require actual equipment choice and a competent facility sign-off.

Ground/earth is intentionally not hard-bonded on the draft. Never attach ordinary earth-referenced oscilloscope ground to an unknown high-side or shunt node. Confirm any sensor bead-to-case galvanic connection and the DAQ input common-mode/isolation limits. Current transducer/shunt dissipation is not heater dissipation. A firmware power-limit or software shutoff cannot replace approved independent hardware interruption.

## 4. Metrology planning values are *targets*, not instrument performance

- Primary heater voltage: **measured across actual two heater terminals** by an appropriately rated differential or isolated measurement.
- Heater branch current: contemporaneous measurement; if using a shunt, record four-wire resistance, self-heating and uncertainty.
- Contact/plate/sink/ambient sensors: minimum three channels + an additional heat-source-position or far-field channel strongly recommended; channel maps preserve actual physical reference locations.
- Time sampling: **hypothesis** of fast mode near 4.84 s from synthetic modeling; a 20 s sample interval cannot resolve it. A provisional testability **target** is 5 Hz or better for temperature channels *only if physical sensor response time and DAQ accuracy permit*. A module rated for 75 S/s in one setting does not guarantee sensor-attached temperature bandwidth or acceptable accuracy. Pilot must measure actual lag before locking sample rate; if it is too slow, explicitly restrict the analysis to slow modes.
- No default sensor accuracy of 0.07°C/0.15°C is assumed as qualified. Use actual calibration/reference evidence and Type A/Type B uncertainties with correlations.

## 5. Required document releases

| ID | Deliverable | Status | Go/no-go evidence |
|---|---|---|---|
| EBT-MEC-005 | Manufacturer-anchored dimensioned fixture drawing | **PDR ONLY** | manufacturer sink drawing, measured part footprint, drill/tap and torque review, tolerances, no hot-surface exposure |
| EBT-EL-005 | Circuit schematic, wiring, protection and DAQ grounding | **PDR ONLY** | exact PSU & protective ratings, instrument isolation, site supervisor review |
| EBT-MET-005 | Measurement chain and uncertainty | **PDR ONLY** | actual instruments, qualified references, sensor lag and timestamp checks |
| EBT-BOM-005 | Bill of materials | **PARTIAL PRICE EVIDENCE** | supplier confirmed price/stock and procurement signoff |
| EBT-Q0-BND | Boundary qualification / transfer test | **PROTOCOL ONLY** | separate qualified boundary input, controlled heat paths and holdout registration |
| Lab authority | Permission to power and machine | **NOT GRANTED** | host staff acceptance and applicable training |

**Verdict: RED / HOLD at release-to-fabrication and release-to-power.** Preparatory 2D CAD, documentation and code reviews may proceed. No drilling, soldering, thermal cycling or energized bench work is approved by this PDR.
