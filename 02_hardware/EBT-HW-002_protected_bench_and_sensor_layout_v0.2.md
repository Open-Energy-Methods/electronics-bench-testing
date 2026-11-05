# EBT-HW-002 · Protected bench architecture and sensor placement (v0.2)

**DESIGN-REVIEW DRAFT — UNENERGIZED.** This is a functional block architecture, **not** a wiring-approved electrical schematic. Actual connector pinouts, fuse ratings, switch ratings, schematic/netlist, protective earth assessment and interlocks remain to be engineered and approved by the host facility. Do not build or energize from this document alone.

## Functional electrical architecture

```text
  Qualified isolated/current-limited DC bench PSU
       +                                      -
       |                                      |
       |  facility-approved disconnect       |
       +-- [manual stop / fuse or protection]|
       |                                      |
       |    +----- Kelvin V+ -----------------+-- to differential V sense (+) [at heater terminal]
       |    |                                 |
       +----+---- [REFERENCE HEATER] ---------+-----[CURRENT SENSOR / SHUNT]---  PSU return
                  TO-220 resistive                   (sense arrangement documented)
                   |
           Mechanical stack: device face / interface / heat sink / fixture

  Temperature measurement (independent logger if possible)
     TC-1: package FRONT/CENTER designated measurement point
     TC-2: sink near mounting location, fixed offset defined in drawing
     TC-3: ambient air, radiation-shielded and out of exhaust stream
     Optional TC-4: sink far-field / back surface for gradient assessment

  Optional forced cooling: independently supplied fan, measured tachometer,
  same ambient definition; never assume fan PWM is a measured convection coefficient.
```

**Drawing caveat:** The displayed return/shunt placement is illustrative. A dedicated full schematic must define all four-wire sense points and current-path nodes unambiguously before construction. `P_heater(t)=V_heater(t) × I_heater(t)` only if voltage is measured **at the heater terminals** and current is the heater branch current; otherwise resistive wiring/control losses contaminate the estimate.

## Critical grounding / instrument safety decisions

1. Never assume oscilloscope ground clips are floating or isolated. Bench scopes may reference protective earth, and clipping ground to an arbitrary circuit node can short the node or defeat current sensing. The approved drawing must specify isolated/differential measurement or a safe instrument arrangement.
2. Prefer battery-independent or isolated thermometry where practical; verify whether thermocouple junctions are electrically connected to heater metal, sink or logger common.
3. Do not use a mains-fed bare/open heater; only an appropriately approved isolated DC laboratory source.
4. Include a reachable independent power-off means and an approved current-limited output. The host site defines supervision, emergency procedures, guards and allowable run duration.
5. Disallow work at KTH Student Workshop involving **energized circuits** unless its rules are explicitly changed by an authorized responsible person. Use it for unpowered fabrication only.

## Thermal sensor placement and traceability

- `T_CASE_FRONT`: identify the fixed package surface point in a dimensioned drawing; record attachment medium, sensor-bead size, mounting pressure, response time and whether the sensor perturbs cooling.
- `T_SINK_NEAR`: specify a reproducible position and depth relative to the mounting hole and heat-source footprint; record sink material and geometry.
- `T_AIR_AMBIENT`: shield from radiation and place outside the thermal plume / fan outlet; record location and air movement.
- Optional IR thermography: record emissivity treatment and reference spot; do not use uncorrected IR temperature as a substitute for junction temperature.
- Synchronize channels and document clock offsets; capture independent supply voltage/current and a no-power reference.

## Boundary characterization, the paper's central measurement problem

The physical `R_sink-to-ambient = (T_sink - T_air) / P` is an **apparent** steady-state quantity based on a defined sink sensor; it is not automatically a device-independent convection coefficient. Heat from leads, radiation, fixture conduction and nonuniform sink temperature must be considered. A fitted `R_sa` from a holdout temperature trace constitutes **information leakage** if later called a prospective prediction. A defensible predictive boundary is premeasured using separate qualification runs or an independently characterized boundary method and its uncertainty; the preregistration specifies what is allowed.

## Open drawing deliverables before Gate G2

- `EBT-HW-002-SCH-01`: complete connection-level schematic and fused/stop path with instrument earth references.
- `EBT-HW-002-MEC-01`: dimensioned sensor/mount/heat-sink layout and permissible interface configurations.
- `EBT-HW-002-SFT-01`: acquired channel-to-file mapping, unit conversion, timebase, failed-channel behavior and emergency logging.
- `EBT-HW-002-RISK-01`: protective limits specific to actual components, actual site and observed failure modes.

**Acceptance:** physical build only after signed/recorded facility authorization, competent electrical review, documented safe envelope and qualified references.
