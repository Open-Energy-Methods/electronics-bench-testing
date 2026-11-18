# OPEP Engineering campaigns: method, evidence, and scope
RD0 design extension | 2026-11-18. No powered or manufacturing release.

## C01 / C11 — modular precision interface and manufacturing validation
Keep the one-box requirement. The physical envelope and plate size remain TBD
until the actual KTH storage box is measured. <8 kg is a provisional carry target.
Actual box interior/taper/lid and component masses control. No common high-load/pressure platform.
First article: a removable low-load datum cassette and small machined
coupon. Obtain staff approval for material and process, survey reference
artefacts and dimensional measurement tools. Derive GD&T and a tolerance
stack from the required remount uncertainty. Compare conventional cut/mill/
drill operations with CNC (where justified); turned locators or spacers;
laser-cut templates and cold fit-check prints. Independent measurements,
first article, process traveller, NCR, rework approval and as-built CAD.
Use PFMEA, control plan and fit-for-purpose MSA, not automatic PPAP approval.
A small supervised batch is a descriptive learning study: cycle/setup/
inspection time, first-pass yield, material losses and actual cost. No
process capability index without enough stable observations and qualified MSA.

## C02 / C03 — structural integrity and mechanically validated FEA
Create a second work product: benign elastic structural coupon and compact
bolted support bracket, not a pressure boundary, lifting accessory or
nuclear component. Use actual stock geometry/material data and the available
approved fixture. Drawings specify datums, tolerance and inspection features.
Analytical checks: Euler–Bernoulli beam deflection, second moment of area,
nominal bending stress, stiffness and linear thermal expansion. Compare
to independently implemented solid and/or beam models in ANSYS Mechanical;
Abaqus, CalculiX or Code_Aster are alternatives. Record elements, mesh,
boundary conditions, reactions, deflection, stress evaluation location,
singularity treatment and convergence. Then consider contact, joint slip,
preload sensitivity, material/geometry nonlinearities only when justified.
A concentrated point force or ideal fixed end without sensitivity is not a
validated joint model.

Define allowable load and measurement range from qualified stand/fixture
and actual material; no universal load is assigned. Use a separate approved
bounded loading setup, retained loads, reference force and displacement or
strain chain. No shop press or calibrated universal testing machine is confirmed at EECS.
Any fabrication press, if present, is NOT a calibrated test machine.
Stop short of yield/failure in baseline. Predeclare observable deflection/
strain and uncertainty, blind prediction and independent installation
holdouts. Quantify fixture stiffness, gauge placement/temperature, preload,
repeatability and material uncertainty. If no authorized loading chain exists,
prepare analysis only and pursue external supervised testing.

Mechanical-integrity extension: thermal expansion/stress with approved
passive or externally heated sample, model stress concentration, fatigue
cycle counting and fatigue damage using source-traceable material curves
within their domain. Nonlinear material and creep/lifing/crack-growth
methods can be computational studies with public benchmark data and clear
limits. No deliberate crack initiation, destructive loads, heated pressure
vessels or physical lifetime claims. Destructive tensile/fatigue/fracture/
seismic/shock tests are external specialist-lab activities.
ASME BPVC, EN 1993, EN 13001, relevant ISO GPS and ASME V&V 10 are
candidate scope/education references; select provision and edition from
actual intended use, obtain legal full texts, document assumptions, obtain
competent review. No pressure-code or nuclear code qualification.

## C04 / C05 — vibration/acoustic/damping qualification analogue
Extend modal beam/plate study by testing independently mounted configurations
and support influence. Force/acceleration FRF requires force measurement,
response conditioning, synchronized acquisition, anti-alias checks, hit
quality, window and uncertainty. Basic MEMS or workshop audio is frequency
screening only; distinguish qualitative results from traceable mode/damping/
sound measurements. Ideal acoustic duct, low-level approved source and
calibrated microphone when available; measure ambient background, geometry,
calibration and network timing; no sound-power claims from room recordings.
A passive bounded spring/damper analogue can illustrate stiffness,
damping/hysteresis and frequency response, not qualification of a vehicle
damper. High-load or repetitive powered excitation only in a qualified lab.
Guarded commercial fan/tach as optional order and blade-passing study.
No fabricated high-speed rotor, induced imbalance, uncontrolled shock
or unqualified shaker. Use COMSOL/ANSYS modal, harmonic and pressure
acoustics if licensed; coupled vibroacoustics only after the submodels pass.

## C06 / C07 — atmospheric flow and non-nuclear thermal-hydraulic analogue
Use a separate cold-flow module with removable reducer, diffuser, duct or
nonrotating passage. CFD and experiment compare pressure drop vs actual
flow, density, local temperature, boundary effects and uncertainty; record
Re, Mach and geometric similarity. Compare geometry A and B within measured
domain, not a full-scale turbine efficiency claim. Optional commercial low
heat addition after permission. Device selection depends on validated
heat/flow need and all-in cost for source, flow, protection, instrumentation,
guard, ventilation and installation. Do not adapt a room heater, hot-air
rework tool, oven or heat gun into an improvised duct. Do not use compressed
air to feed an improvised heater.

Candidate separate wet-area cold water open-reservoir circuit (commercial
appropriately rated pump and components, low stored energy, spill control,
no electrical exposure, no blocked-flow or pressurized test). Specimens:
commercial heat exchanger, pipe fittings, simple flow routing and valves,
if staff agree. No boiling, steam generation, pressurized gas/liquid vessels,
liquid metal, radioactive material, fuel or reactor experiment. Warm-water
heat exchanger project only under a separately reviewed setup and approved
source, not an improvised heater. Record P&ID, component data, actual mass
flow and pressure differential, thermal reference and leak/energy balance.
Validate pump/loop pressure-loss curves, thermal inertia and UA (if
temperature and flow contrast sufficient), mass/energy residual and
transient control using CFD/ROM and independent configurations. Non-nuclear
analogue supports fluid systems, thermal hydraulics and V&V methods only.
Two-phase boiling, sCO2, high temperature or pressure research may be
computational with public data or conducted only in qualified external labs.

## C08 / C10 — electronics, metrology and industrial automation
Use listed bench equipment for approved low-energy reference RC/filter
boards, signal conditioning and sensor-interface design. Native KiCad
schematic/netlist/PCB, reviewed part ratings and approved fabrication
method. Record real scope traces, differential/grounding constraints,
voltage/current reference, DAQ timebase, bandwidth, noise and uncertainty.
Investigate instrumentation amplifier and strain bridge if actual gauges/
references available, thermocouple/RTD chain, sensor lag and sample timing.
Use serial/Modbus or simulated industrial fieldbus if justified and
authorized; not a live plant interface. Test event log, first-out, stale data,
fault indications and manual reset in software first. No safety function
relies on the host. Build maintenance and calibration schedule, independent
protection assessment and documented commissioning/pass-off with actual
acceptance criteria. Derive site/ambient correction with experimentally
measured environmental dependence and held-out data; do not claim full-scale
turbine pass-off. ThermoTwin-F offline replay requires bounded parameter
provenance; OPEP twin separately follows actual as-built state.

## C09 / C12 — assurance and additional shop skills
DVP&R, requirements ID, SRR/PDR/CDR/TRR, evidence readiness/TRL with stated
reference framework, DFMEA and PFMEA, nonconformance/change tracking, and
scope-specific procedures. Civil/industrial nuclear analogues focus on
seismic modal methods, component traceability, design-basis calculations,
independent review, configuration control and test evidence, never nuclear
safety sign-off. Study public nuclear codes/standards with scope/version
review, not copyrighted extracts. Visual inspection and reversible low-risk
inspection methods only after permission; no radiography. Welded/formed,
plasma-cut or powder-coated training coupons only if approved and genuinely
useful; not load-bearing/pressurized service. Capture qualified staff
feedback; avoid hazards, chemical processing or excess fabrication solely to
claim machine coverage. Scan-to-CAD/as-built comparison is a screening
study unless scanner calibrated and uncertainty defensible.

## Deliverable and promotion
Each physical project outputs native CAD/EDA/simulation, drawing/BOM and
revision, process record, as-built checks, raw source/manifest and reference
IDs, analytical and numerical verification, predeclared validation and
uncertainty, results with failure analysis, rework/change and new holdout
where changed, checklists and reproducible report. Track owner, reviewer,
authority and date. No missing evidence becomes PASS through software.
