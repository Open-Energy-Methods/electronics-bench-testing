# OPEP-PKG-002 — Pack-away platform and process-air extension
2026-11-18 | Proposed RD0 design amendment | NO manufacturing or powered release.

## Storage constraint and architecture
Stockholm Makerspace permits one approved SmartStore Classic 31 or Home 31
member box for active lab-access members. Classic 31 published external size
500 x 390 x 260 mm; Bauhaus lists internal 400 x 307 x 221 mm. Actual
taper, rib/clip/lid geometry and permissible mass must be measured.
Sources:
https://wiki.makerspace.se/Medlemsf%C3%B6rvaring
https://www.bauhaus.se/forvaringslada-smartstore-classic-31l-med-lock

Proposed packed envelope 380 x 285 x 200 mm; baseplate target 350 x 250 mm;
longest single component 380 mm (orientation-dependent); packed user-owned
active module + common hardware target <=8 kg; setup <=15 min, pack <=10 min
after safe cooldown/disconnection. These targets are author choices to
review, not measured fit or performance. Mutually exclusive modules can be
stored elsewhere; do not assume ten modules fit in one box. Borrow shared
instruments on-site; do not store them, lithium cells or prohibited materials
in the box. Box is storage only, never an operating enclosure.

Supersede the earlier fixed 600 x 450 x 400 mm dock as the physical design
baseline. Retain existing RD0 CAD as historical packaging exploration.
Evaluate detachable short extrusions, common datum carrier plate, demountable
posts/guard and separate module-specific utility panels. Require controlled
pack configuration, part list, actual fit with lid, mass and carry assessment,
assembled stability, repeatability across unpack/setup and time logs.
Exact plate thickness, structural alloy, fastener patterns, tolerance and
operating footprint await RD1/RD2 survey. Do not promise current STEP fits.

## Proposed M11 — process-air / turbine-physics analogue
Separate M11 from M06 electronic cooling. Start with open-to-atmosphere
low-energy cold airflow and interchangeable nonrotating test passages, then
only if separately authorized use a suitable commercially manufactured
process-air source/heater with reviewed electrical, thermal, airflow and
emergency protection. No conversion of consumer space heater or heat gun
into duct, no pressurized hot air, pressure vessel, combustion or custom
high-speed rotor in this baseline. Shared compressed air is not experiment
approval. Keep hot components away from storage box and polymers; cooldown
before storing. Approved heater and bench limits are TBD.

Engineering questions: duct/reducer pressure loss, distribution and mixing,
temperature sensor response, transient temperature transport, heated-air
energy balance, and CFD/measurement comparison. Instrument chain:
up/downstream temperatures, differential pressure, actual mass/volume flow,
synchronized acquisition and independently measured input power. Evaluate
heat losses, density, uncertainty and sensor response. Use Reynolds/Mach
and Prandtl similarity where applicable; ambient low-speed flows cannot
validate high-Mach/high-pressure turbine performance. An electric heater is
an external heat-addition surrogate, not combustion or an operating turbine.
A digital turbine model can consume characterized component data or use
hardware-in-the-loop emulated signals; distinguish simulation from measured
performance. Later guarded commercial fan characterization may be considered
separately after review; genuine rotating turbomachinery requires another facility.

## Makerspace capability and questions
Public list records electronics bench DMM, scope, function generator, supplies,
thermal camera, PCB work, 3D scanning, metal lathe/mill, surface plate,
compressed-air plant and convection oven. It does not establish calibrated
flow/pressure sensors, a process-air heater, chamber suitability or authorization.
References:
https://wiki.makerspace.se/doc/electronics-ebd1c6a868
https://wiki.makerspace.se/doc/maskiner-och-inventarier-8991ffd97b
https://wiki.makerspace.se/doc/general-rules-english-710a7afe49
https://www.makerspace.se/kontakta-oss

Ask board whether personal noncommercial supervised/intermittent heated-air
bench work is acceptable, designated area, applicable electrical/thermal/
ventilation/fire restrictions, suitable existing heater/blower or donated
surplus, permissible sources, thermocouples/DAQ, pressure/flow instruments,
probe isolation and calibration, training, storage and permission for
photographs/public documentation. No funding, procurement or equipment
availability inferred. No email sent by this change.

## Acceptance planning
SRR: inspect exact box and tools and facility scope; PDR: actual packaging
trade, collision and stability review; CDR: approved individual component
geometry, materials, wiring and safety; RD4: unpowered fit/pack verification;
RD5/6: actual approved module-specific readiness and acceptance. No physical
gate closed. M11 is a candidate, not an authorized experimental module.
