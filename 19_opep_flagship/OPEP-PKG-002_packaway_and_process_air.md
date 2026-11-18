# OPEP-PKG-002 — Pack-away platform and process-air extension
2026-11-18 | Proposed RD0 design amendment | NO manufacturing or powered release.

## Storage constraint and architecture
The researcher requires a single storage box at KTH EECS Student Workshop.
Actual box internal dimensions, opening, lid clearance, permissible mass,
labelling and storage duration remain unverified. The former 31 L SmartStore
assumption came from a different facility and is withdrawn.
Earlier 380 x 285 x 200 mm packed / 350 x 250 mm plate dimensions are historical
design hypotheses and NOT current dimensional requirements. Freeze dimensions
only after measuring the actual box. Retain provisional setup <=15 min,
pack <=10 min after safe cooldown/disconnection and <=8 kg carry target,
subject to actual facility and handling review. Borrow instruments with
permission; storage box is not an operating enclosure.

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
high-speed rotor in this baseline. Compressed-air availability is unverified at this facility; no pressurized experiment is authorized. Keep hot components away from storage box and polymers; cooldown
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

## KTH EECS Student Workshop capability and questions
Use KTH public inventory and local Canvas course 32080; see career/OPEP-FAC-004_machine_opportunity.csv and career/OPEP-PROC-004_makerspace_requests.md.
KTH lists electronics equipment, 3D printers, laser, PCB mill, CNC/manual
milling, turning and carpentry; actual models and permissions still require
survey. A thermal chamber has been user-reported but is not publicly verified.
Ask Mykola Ivchenko about project scope and equipment needs and Alicia
Carredano Robertsson about safety/heat/noise/flow testing. Record missing
equipment on the Student Workshop Needs list. ELAB is a separate facility.
No funding, equipment purchase or test authorization assumed.

## Acceptance planning
SRR: inspect exact box and tools and facility scope; PDR: actual packaging
trade, collision and stability review; CDR: approved individual component
geometry, materials, wiring and safety; RD4: unpowered fit/pack verification;
RD5/6: actual approved module-specific readiness and acceptance. No physical
gate closed. M11 is a candidate, not an authorized experimental module.
