# RIG-SYS-001 — System architecture trade study

## Alternatives
A: minimal open fixture with bench instruments. Low cost/complexity but limited
repeatable interfaces, cable control and chamber relocation.
B: modular external control/measurement dock with removable DUT cassette,
interchangeable cooling, repeatable mounting datums and defined chamber interface.
C: integrated stand/enclosure with permanently installed electronics and duct.
Good operator organization but harder service, chamber relocation and cost.

Screening matrix: 1 poor / 5 strong; weights and scores are **author judgments**,
not measured data, safety decisions or objective lifecycle cost. Hard exclusions
(site approval, no interference with chamber, protection/measurement suitability)
override every score.

| Criterion | Weight | A | B | C | rationale |
|---|---:|---:|---:|---:|---|
| Configuration repeatability | 25 | 2 | 5 | 4 | common cassette and datums |
| Chamber flexibility | 20 | 3 | 5 | 2 | only permitted passive/test cell moved |
| Serviceability | 15 | 4 | 5 | 2 | separable replaceable modules |
| Learning/technical scope | 15 | 2 | 5 | 5 | interfaces, DFM, controls, qualification |
| Cost/effort | 15 | 5 | 3 | 1 | use available bench equipment |
| Footprint and storage | 10 | 5 | 3 | 2 | modular but less compact |
| Weighted total (/5) | 100 | 3.25 | 4.50 | 2.80 | provisional selection B |

Sensitivity: shifting emphasis from repeatability to cost by 25 percentage
points changes A by +0.75, B by -0.50 and C by -0.75; A and B then tie at
4.00. Choice B therefore depends on value of reproducibility and modular
engineering, not on a claim it is universally optimal. Re-score using
observed costs, workspace capacity and real access at RD1.

## Allocated functions
100 platform: stable footprint, cable routes, removable panel, lifting/handling
assessment. 200 cassette: kinematic or quasi-kinematic locating scheme
(3-2-1 locating candidate), independently controlled clamping, thermal contact
and replaceable DUT and sensor mounts; locate without overconstraint.
300 air module: modular fan, upstream conditioning, duct, temperature/velocity
survey, diagnostic fan state; removable for NAT to avoid artificial blockage.
400 electrical: approved external supply, separable harness, verified protective
interrupt and independent thermal shutdown; no custom mains wiring.
500 measurement: external DMM/DAQ, isolated/differential probe selection,
thermometry/reference network, timebase and actual sensor attachment.
600 control: human supervision and independent protection; logger, setpoint
workflow, state/event history, configuration manifest; no software-based safety
claim or automatic restart.
700 chamber interface: remove only approved cell, map feedthroughs and ambient
reference, require load, temperature uniformity, gradients, condensation,
material, airflow and control-response assessment.
800 containment: guard against inadvertent hot surface/contact, fan ingress,
strain and loose objects; material and clearances depend on hazard review.

## Design constraints
Keep high heat and electrical utilities away from plastic/enclosure prototypes;
no wood or 3D-printed polymer as thermal/electrical protection without specific
material qualification. Do not use scope ground clips as isolated probes.
The measured DUT boundary shall not be arbitrarily changed by the carrier,
guard or duct; parasitic conduction and airflow effects must be evaluated.
Natural convection and forced air are separate documented configurations;
chamber insertion introduces an additional boundary, not equivalent to room air.

## Design baseline
Provisional external dock 600 × 450 mm footprint, 400 mm reserved structural
height; removable cell envelope 300 × 250 × 160 mm for layout evaluation only.
No actual chamber fit is asserted. A separate equipment shelf/utility region
is spatial reservation; actual instruments remain outside the chamber. Do not
size frame or mounting fasteners from envelope alone. The layout dimensions
are author-selected hypotheses to be reduced if survey requires.
