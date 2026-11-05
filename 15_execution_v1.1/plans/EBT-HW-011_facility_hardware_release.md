# EBT-HW-011 — Facility, unpowered hardware and electrical release pathway (WP0/2)

**Status:** PRE-AUTHORIZATION. Reference: [v0.9 Q0](../../14_q0_integrated_v0.9/README.md) and [Q0-010 real-part intake](../../14_q0_integrated_v0.9/docs/EBT-Q0-010_unpowered_intake.md). All machining, equipment and electrical limits must be reviewed *at the actual site*.

## Track A — physical workshop and access (not an electrical lab)

- **Student Workshop:** signed-in course 32080 is **visible**, and its real [onboarding steps](../../14_q0_integrated_v0.9/facility/EBT-G2-012_workshop_onboarding.md) require a **Find Appointment** booking, safety introduction, quiz, uploaded signed safety acknowledgement and, when applicable, official machine risk assessment plus practical introduction. It is a project-based workshop: bring the [bounded EBT mechanical brief](../../14_q0_integrated_v0.9/facility/EBT-G2-012_project_brief.md). Published Nov 5 17:00 and Nov 6 16:00 events were visible on the course page on Nov 5 but are NOT verified vacancies or bookings. Record induction, actual allowed machine/operation and staff permission. Course access is not machine approval.
- **Manufacturing Lab:** independent work outside its allowed arrangements is restricted; do **not** designate it as approved EBT fabrication access. Departmental research/Maskineriet is a distinct institutional route, and MG1000 is required for student Maskineriet.
- **Backup commercial facility:** only after confirming eligibility, mechanical process, access cost, permission for the proposed part and public-data/photo rules. Never infer powered testing from workshop membership.
- **Separate electrical lab:** ELAB enquiry sent Nov 4; no authorized reply as of Nov 5. A member badge or any KTH account is not an approved electrical SOP or permission. If site cannot host the exact scope, search qualified alternatives.

## Track B — part receipt and geometry (unpowered)

Reference candidate: Fischer SK 92 100 SA (nominal 100×100×40 mm, 10 mm profile base) and two Bourns PWR220T-20-10R0F 10 Ω reference heaters (20 W conditional rating at 25°C case; application note 2.8 W free-air example, **not** Q0 limits). **None is confirmed purchased, delivered or inspected.**

Before selecting direct-to-sink vs added adapter: record as-shipped markings/lot/receipt and unmodified photos; verify dimensional tool and actual base/fin/contact geometry, plate necessity, electrical isolation, thermal interface thickness/force and thermal sensor attachment feasibility. Ask authorized staff for permissible machining, fastening and surface-work methods. A catalog 10 mm base does NOT define drillable depth/bolt pattern. Draft and review actual part-specific drawing/assembly bill ONLY after inspection, then seek formal fabrication release.

## Track C — powered bench safety boundary

Named site staff must approve **a real wiring drawing**: isolated current-limited DC source, heater terminal differential V measurement, same-branch I/shunt, conductor and protection ratings, independent stop, fail-safe disconnect, limits and fault/thermal guarding; common-mode/earth/shielding/thermocouple grounding need explicit review. A sample v0.5 net file does not authorize assembly.

Approval requires real part derating vs measured/expected case temperature, PSU and sensor ranges, the site's local rules, human supervision, safe controlled shutdown and incident response. No fixed wattage, power steps, cutoff temperature, fuse size, torque or heat exposure has been inferred in this plan.

## Procurement release discipline

1. **Inspect borrowed equipment first:** avoid duplicating site PSU, DMM, DAQ or sensors.
2. Price each exact SKU + delivery and alternate part; confirm manufacturer datasheet revision; time-stamp quote; verify lead time, material and compatible mount.
3. Keep preliminary v0.5 three-piece **346.58 SEK ex VAT** quote as a historical partial source check only—not the full rig cost. The rest of the BOM remains unpriced; no spending approval implied.
4. Buy only when physical acceptance criteria and site permission for the intended step are confirmed. Separate **mechanical pre-approval procurement** (if justified) from **powered experimental procurement**.

## G2 closeout pack

Actual site authorization (fabrication and powered separately), personnel/induction, receipt/inspected part with mounting assessment, released drawing/BOM, reviewed electrical schematic/SOP, qualified instruments, signed thermal/electrical exposure envelope and controlled archive/rights. Feed these into the existing 23-point register and `EBT-GATE-007`, whose software cannot grant GO. **Until then: HOLD MANUFACTURE / HOLD POWER.**
