# EBT-CAD-020 — Drawing register and evidence grades

| ID | Format | Role | State | Changes required before G2 physical release |
|---|---|---|---|---|
| EBT-EL-020 | KiCad .kicad_sch | Functional review of protected DC heater measurement and separate fan | PRE-DESIGN | Real switch/pinouts/protection/wire/DAQ isolation, KiCad/ERC and competent engineer review |
| EBT-EL-020-NET | CSV | Pin-to-net connectivity ledger | SOFTWARE STRUCTURE | Export actual KiCad netlist, independently reconcile |
| EBT-MEC-020 | OpenSCAD .scad | Nominal simplified sink and two alternative heater sites | REPRESENTATIVE MODEL | Real sink extrusion cross-section, heater body and mounting envelope |
| EBT-MEC-020-STEP | CadQuery .py to STEP | Multi-solid CAD review for FreeCAD | REPRESENTATIVE MODEL | As-built measurement + release fasteners/clamp and actual CAD constraints |
| EBT-MEC-020-DXF | ezdxf .py to DXF | Nominal plan/section/underside review sheet | NOT FOR MANUFACTURE | Actual certified dimensions, GD&T, mount pattern, fastener material, surface finish, tolerance |
| EBT-MET-020 | CSV | Instrumentation to electrical drawing crosswalk | UNINSPECTED | Approved serials, references, sensor placements, logger isolation and permission |

**Catalog-qualified nominal:** Fischer SK 92 100 SA nominal length/width 100 mm,
total height 40 mm and base thickness 10 mm. No actual part inspection done.
**Assumed:** optional 100x100x4 mm plate; representative 11-fin geometry;
TO-220 body thickness and placement/lead stubs; sensor markers and size.

The CAD and KiCad files are NOT evidence of a safe or functioning test rig.
This register is not a release checklist for manufacturing or wiring.

**Rev A review alignment:** heater marker centres in the DXF underside view are matched to the provisional CAD x=±25 mm layout; surface sensors NEAR1/NEAR2/FAR are visually labelled as non-manufacturing *proposals*. No hole location or verified thermometric attachment is implied.
