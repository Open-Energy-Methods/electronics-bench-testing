# RD0 packaging models — first electrothermal application only
Run `python rig_layout.py --out build` with CadQuery 2.x.
Four neutral STEP assemblies can be generated for natural and forced
convection: dock and detachable cell. Local CadQuery/OpenCascade checks of
the individual solids, envelope containment and positive-volume overlaps
are recorded in geometry_audit.json. They do not establish manufacturability,
clearance under movement, strength, thermal suitability or any chamber fit.
The 600 x 450 x 400 mm dock and 300 x 250 x 160 mm cell are preliminary
packaging reservations only. The block primitives are deliberately not
manufactured profiles, detailed components, fastening or actual duct walls.
No drilling, slot geometry, hot-zone material, safety guard or wiring is
released. Generate exact supplier CAD and reviewed functional manufacturing
drawings only after RD1/RD2 actual equipment and part inspection.
