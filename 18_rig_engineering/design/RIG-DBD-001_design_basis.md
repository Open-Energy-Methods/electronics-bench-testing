# RIG-DBD-001 — Engineering design basis and calculation work

RD0 — design hypotheses; no approved operating envelope.

## Mechanical
Allocate distinct stable base, removable cell, locating reference planes A/B/C,
and accessible clamping. Use standard aluminium profiles/stock where appropriate;
avoid machining commercial heatsinks without validated mounting data. Calculate
frame loads, dead weight, equipment shelf load, overturning under credible cable
pull, support deflection, joint slip, thermal expansion, lifting and fastener
capacity after actual parts and usage are known. Use accurate supplier CAD and
section properties; validate FEA against a simple analytical beam or frame model
and measured deflection. Do not treat bonded ideal FEA as joint qualification.

Initial analytical benchmark for a simply supported beam with central mass:
delta = F L^3/(48 E I), Mmax = FL/4, sigma=Mmax c/I. These assumptions are NOT a
real extruded-frame joint model. Use actual supplier I and yield data and user
load case. Model support and instrumentation deflection relative to sensor
position and remount uncertainty, not arbitrary cosmetic stiffness.

For thermal expansion, deltaL=alpha L deltaT, then assess locating and clamp
compliance. Select fits and GD&T from functional tolerance budgets: location
repeatability, contact face parallelism, locating pin hole distance and datum
alignment. Define a measurable tolerance only once measurement resolution and
fabrication capability are verified. Do not blanket-apply general tolerances.

## Thermal/air
Control-volume energy: P_terminal = Q_storage + Q_air + Q_support + Q_leads
+ Q_radiation + other losses. Include all relevant masses. For steady duct
screening Q_air≈rho cp Vdot deltaT with density, humidity, flow and measurement
assumptions. Fan free-air rated flow is not duct flow. Establish a fan/system
curve measurement plan, inlet velocity uniformity, recirculation and thermal
loss check. Estimate duct pressure loss using Darcy–Weisbach plus fittings
only when geometry/flow regime are known. Use CFD for design sensitivity,
mesh verification and actual boundary conditions, not to assert measured flow.

For chamber service, record door and access dimensions, usable swept volume,
shelf permissible load, feedthroughs, permitted powered loads, air speed,
temperature bounds and uniformity under relevant loaded state. Do not assume
the chamber can reject DUT heat or that temperature setpoint is measured
ambient. Condensation and dew point require review for all transitions.

## Electrical
Source power is measured across DUT terminal voltage and same branch current.
One source at a time in first cassette. Select shunt and analog front end by
range, self heating, uncertainty, common-mode and isolation; coordinate
actual protective devices with prospective DC fault current, wire ratings and
thermal derating. Independent protective shutdown shall not rely on the DAQ
or host computer. Exact thresholds and components remain unset until reviewed.
Scope bandwidth/sample rate/probe ratings follow actual transient target.
Start with resistive DUT only; separate semiconductor phase needs DC/pulse SOA,
appropriate gate/control circuit, switching transient and protection review.

## Design calculation deliverables
Mechanical: load cases, stability, profile deflection, joints/fasteners,
tolerance stack, thermal expansion. Thermal: heat-loss budget, duct pressure,
fan operating point, chamber loading and uncertainty. Electrical: wiring
diagram, electrical power/energy and fault assessment, shunt and sensor
range/uncertainty, independent shutdown concept. Instrumentation: I/O list,
sampling and timing, traceable calibration, logger design, uncertainty.
Models must have units, provenance, bounded assumptions, independent formula
checks and measured qualification later. No numerical scenario authorizes
equipment operation.
