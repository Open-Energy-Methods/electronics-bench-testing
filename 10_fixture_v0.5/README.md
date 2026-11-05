# EBT v0.5 — Preliminary Design Review (PDR)

**Status: DESIGN FOR REVIEW — NOT BUILD RELEASED — NEVER SITE AUTHORIZATION.** This project remains independent, with synthetic-only numerical evidence and no real energized test.

This controlled package turns the earlier conceptual hardware list into a **traceable preliminary engineering proposal**. It does **not** claim that equipment is purchased, calibrated, assembled, safe at any proposed operating voltage/power, or that the selected mechanics are machinable without review.

## Assets

- [PDR and hard blockers](docs/EBT-PDR-005_engineering_design_review.md)
- [Test modes and boundary-transfer qualification](docs/EBT-MET-005_boundary_transfer_qualification.md)
- [Fabrication and dimensional drawing notes](docs/EBT-MEC-005_manufacturing_review.md)
- [Plan view, SVG](drawings/EBT-MEC-005_plan.svg), [section view, SVG](drawings/EBT-MEC-005_section.svg), [editable DXF, review geometry only](cad/EBT-MEC-005_layout_NOT_FOR_MANUFACTURE.dxf)
- [Electrical measurement circuit, SVG](drawings/EBT-EL-005_measurement_schematic.svg) plus [net connectivity](electrical/EBT-EL-005_nets.csv) and [electrical interface design review](electrical/EBT-EL-005_schematic_review.md)
- [Channels and metrological checks](metrology/EBT-MET-005_channels.csv), [uncertainty model](metrology/EBT-MET-005_uncertainty_budget.md)
- [Line-item sourced preliminary BOM](procurement/EBT-BOM-005.csv), [pricing evidence](procurement/EBT-BOM-005_sources.md), [budget XLSX](procurement/EBT-BOM-005_budget.xlsx)
- [Evidence and release gates](docs/EBT-PDR-005_evidence_register.csv)
- [Programmatic review tests](tests/test_pdr_integrity.py).

## Chosen base hardware — not approved for use

- **Two candidate identical heater parts**: Bourns `PWR220T-20-10R0F`, 10 Ω ±1%, TO-220. Datasheet case-based power rating is **not** a safe test setpoint. Manufacturer drawing: package 10.1 mm width, 14.6 mm body height, Ø3.6 mm package hole, 5.08 mm lead pitch (PWR220T-20 datasheet Rev. 06/25).
- **One candidate cooling extrusion**: Fischer Elektronik `SK 92 100 SA`, nominal externally 100 × 100 × 40 mm. Distributor thermal-resistance figures depend on unspecified test flow/orientation: **never substitute them for a measured independent boundary input**.
- **Proposed interposer/spreader**: 100 × 100 × 4 mm aluminium plate, material, flatness, contact surface, mounting, fastener length, screw clearance, heat bypass and exact matching to extrusion **TBD**. Dimension is a *design assumption*, not a purchased manufacturing drawing.

## Validity of source claims

The source links and price snapshots were checked on **2026-11-05**. The BOM deliberately separates **source-verified priced rows** from unquoted, site-borrowed or unqualified requirements. Partial quoted cost is *not* an all-in price. An upstream v1.0 baseline manifest is historical and remains unchanged.

The CAD/DXF layout has **design-intent coordinates** and MUST NOT be machined until a reviewed manufacturer profile, actual part dimensions, threading, tolerances, clearance and thermal interface design are incorporated into a released drawing. The electrical diagram has explicit topology, but protective components and instrument input ratings still require qualified site selection and review.
