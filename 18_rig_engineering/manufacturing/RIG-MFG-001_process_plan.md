# RIG-MFG-001 — Manufacture, assembly and inspection

RD0 process allocation; no machine instructions or approved materials yet.

| Item | Preferred manufacturing approach | Required artifact and learning outcome |
|---|---|---|
| RIG-100 modular dock | Buy standard profiles, cut to length if authorized, assemble bolted joints | CAD assembly, cut list, frame inspection, stability/load assessment |
| RIG-200 cassette carrier | CAD/CAM and supervised CNC or manual milling of approved stock | datum scheme, workholding review, machining drawing, first article dimensional report |
| RIG-210 locating hardware | supervised lathe for simple turned locator/spacer if needed | fit/tolerance design, process record, diameter/length measurement |
| RIG-220 brackets | supervised drill/mill only after approved hole schedule | hole-position inspection, deburr, fastener review |
| RIG-230 sensor holder | 3D print unpowered fit-check prototype; final material separately qualified | slicing and print orientation/fit evidence, material and temperature review |
| RIG-300 airflow duct | laser-cut mockup in site-approved material, or suitable sheet fabrication | flat pattern, cutting/assembly tolerance, leakage/flow survey |
| RIG-400 control panel | reviewed electrical enclosure/label pattern; use purchased certified devices where suited | panel layout, cable schedule, protection review |
| RIG-800 guarding | qualified guard materials and inspected detachable structure | hazard-informed design, safe access/handling and boundary impact checks |
| Training coupons | wood/cutter/laser/turning/milling exercises separate from final hot-zone parts | actual machine-specific staff-approved practice and inspected specimens |

## Manufacturing discipline
Develop model-based product structure and drawing list first. Use functional
datums and tolerance chain, not a blanket tight tolerance. Prefer standard
components and minimize custom parts, fasteners and process changes. Document
make/buy/borrow rationale. Perform DFM/DFA review (tool access, tolerances,
tooling, assembly sequence, maintenance), material suitability, workholding,
machine-specific permitted tasks, tool/process approvals and inspection plan.

Release a controlled manufacturing package only at RD3: native CAD, assembly
STEP, part drawings, material/specification, GD&T, surface/edge requirements,
joint review, BOM, process routing, inspection points and revision. CNC CAM
simulation and posted code are NOT machine permission. Obtain shop-specific
postprocessor and tooling review; no generic G-code is approved. First article
inspection: verify datums and critical characteristics with an identified tool,
record measurement uncertainty, NCR and reviewer disposition. Never silently
alter drawing to match a defective part. Record as-built configuration and
re-measure after assembly. The final hot-zone/guard structure needs actual
thermal and electrical review, irrespective of prototype fit.

## Initial drawing register
RIG-GA-100 general arrangement; RIG-MEC-110 frame; RIG-MEC-200 cassette assembly;
RIG-MEC-210 locators; RIG-MEC-220 clamps; RIG-MEC-230 sensor retention;
RIG-MEC-300 duct/air module; RIG-EL-400 system power architecture;
RIG-EL-410 wiring and terminals; RIG-EL-420 protection; RIG-INS-500
instrumentation schematic and channel schedule; RIG-CTL-600 control/state
description; RIG-ENV-700 chamber insertion; RIG-SAF-800 guard/handling.
All detailed drawings remain unreleased. Use interactive FreeCAD/NX/SolidWorks
or other authorized mechanical CAD for reviewed models and drawing views;
KiCad or appropriate electrical CAD for actual circuit/netlist. Use native
CAD/EDA checks, no image-generated manufacturing drawing.
