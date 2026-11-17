# EBT-CAD-020 | Native CAD / EDA engineering package v0.11

Status: PRE-DESIGN A, 17 November 2026. NOT FOR MANUFACTURE OR ENERGIZED TESTING.

This is professional editable engineering source, NOT a generated decorative image.
The native KiCad schematic uses embedded EBT review symbols, and mechanical
architecture uses OpenSCAD and CadQuery, with STEP and DXF exports.

## Documents

- electrical/EBT-EL-020.kicad_sch — editable KiCad A3 schematic, 15 functional review symbols; 14 nets and 35 pin members. These are not actual manufacturer connector pinouts or released protective device ratings.
- electrical/EBT-EL-020_net_connections.csv — labelled pin-to-net review ledger.
- mechanical/EBT-MEC-020_assembly.scad — editable OpenSCAD parametric rig geometry; adapter=true selects OPTIONAL 4 mm plate.
- mechanical/EBT-MEC-020_cadquery.py — named CadQuery assembly and STEP exporter for FreeCAD/CAD review.
- mechanical/EBT-MEC-020_drawing.py — editable engineering drawing generator (ezdxf; DXF R2010).

## Circuit intent

Heater circuit: isolated, qualified bench DC source (TBD) -> DC-rated disconnect S0
(TBD) -> protection F1 (TBD) -> DC-rated break-before-make center-OFF
selector S1 (TBD) -> ONE Bourns PWR220T-20-10R0F candidate at a time ->
four-wire shunt RSH1 (TBD) -> PSU return. V1/V2 are differential
measurements of the heater *terminals*, VI measures Kelvin shunt voltage.
A separate fan supply, F2, fan control and tachometer are shown
without a shared electrical-earth assumption. Temperature logger
connections remain unselected due to actual sensor/ground/isolation unknowns.

**This is a KiCad editable review schematic, not a safe wiring instruction.**
None of the protective devices, physical PSU, wire ratings, common mode
or stop logic have been selected. Native KiCad ERC and competent site review
must be completed prior to any electrical design release. S1 has a
functional review symbol only; switching safety or break-before-make is NOT
validated by this drawing.

## Mechanical scope

Fischer SK 92 100 SA nominal 100x100x40 mm and 10 mm base.
Fins are *surrogate* (11 simplified fins); this is not a verified
manufacturer extrusion section. Approximate TO-220 face placeholders
are shown at x=-25 and +25 mm; these are candidate positions only,
not hole coordinates. Heater-body Z, fin widths, any screw/torque,
clamp geometry and TIM are unverified. Both heater solids appearing
in a model does NOT authorize simultaneous energization.

DIRECT model = no adapter. OPTIONAL model = assumed 100x100x4 mm
additional aluminium plate; currently not a physically qualified part.
Actual sensor meanings T_CASE, T_PLATE and T_SINK must remain distinct.

## How to open or regenerate

KiCad Schematic Editor: open electrical/EBT-EL-020.kicad_sch.
OpenSCAD: open mechanical/EBT-MEC-020_assembly.scad.
CadQuery 2.x / CQ-editor: execute the Python assembly generator to
export direct and adapter STEP files, which FreeCAD can also import.
ezdxf: execute the drawing generator to export an R2010 DXF review sheet.

Commands (from this folder):

    python -m unittest discover -s tests -p 'test_*.py' -v
    python mechanical/EBT-MEC-020_cadquery.py --out build/
    python mechanical/EBT-MEC-020_drawing.py --out build/EBT-MEC-020_review.dxf
    openscad -o build/EBT-MEC-020_direct.stl mechanical/EBT-MEC-020_assembly.scad
    openscad -o build/EBT-MEC-020_adapter.stl -D 'adapter=true' mechanical/EBT-MEC-020_assembly.scad

Static source checks demonstrate file structure, syntax and
source-ledger consistency. A separate native KiCad CLI export check is
required to prove the editor can read and export the schematic; even
then, ERC deviations remain for real electrical design review and no
code or export can establish site safety or
manufacturer tolerances. STEP and DXF preview exports were independently
generated in a CAD environment and visually reviewed.

## Remaining G2 physical blockers

Workshop machine-specific training and task permission; actual sink
inspection and valid contact geometry; approved mechanical drawings,
fasteners and insulation; electrical lab site approval, actual PSU,
DC interruption, shunt references, temperature logger calibration,
hardware independent shutdown and signed operating limits.

There is NO physical measurement, certified wiring, manufacturing
release or powered-testing authorization in this package. The
scientific boundary-transfer and holdout studies remain blocked.
