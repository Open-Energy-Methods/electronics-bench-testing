# EBT-MEC-007 — Conditional fixture-architecture decision (PDR supplement)

**STATUS: PROPOSED FOR TECHNICAL REVIEW; NOT APPROVED FOR FABRICATION OR TESTING.** Supplements EBT-MEC-005, EBT-SPAT-006 (draft PR #11), and issue #5.

## Objective

Minimize unidentified heat paths while retaining reproducible A/B heater placements, a stable separately measured cooling state and surface temperature sensors suitable for prospective B0–B3 model assessment. This is a research-method decision, not a cost-only choice.

## Alternative A — DIRECT_TO_SINK_CANDIDATE (preferred for review, not selected for build)

- Mount one reference heater onto an inspected external base surface of the actual SK 92, using a **manufacturer/workshop-approved fastening or clamping approach**; use the same verified mounting method in every A/B test.
- No entire added 4 mm spreader in the primary thermal path. The expected benefit is fewer uncontrolled series interfaces and less added thermal mass.
- Limitations: the actual skin/base surface, screw/load and strain-relief features may make this impossible; bottom-side sensor clearance and contact-pressure repeatability are not currently demonstrated.
- The 10 mm nominal base from the SK 92 series does **not** justify choosing tap depth, hole placement, torque or machining direction.

## Alternative B — ADAPTER_PLATE_CANDIDATE (explicit control or fallback)

- Retain v0.5's **assumed** full-area 100 × 100 × 4 mm plate as an identifiable additional part, with a documented sink-to-plate TIM/contact and heater-to-plate TIM/contact. An as-built drawing must identify which sensors measure T_plate and which directly measure T_sink.
- A wholly isothermal, generic aluminium example (density **assumed** 2700 kg/m³; specific heat **assumed** 900 J/(kg·K)) adds 0.108 kg and **97.2 J/K** nominal lumped heat capacity. This is a *conditional mass/heat capacity calculation*, not a measured dynamic mode; spatial gradients and real material properties are absent.
- If plate use is essential, run a separately qualified comparison against direct-to-sink geometry when possible; don't substitute adapter-plate apparent R for a direct-sink boundary.

## Release criteria

| Requirement | Direct sink | Adapter plate | Evidence status |
|---|---|---|---|
| Verified thermal mating surface | Required on actual part | Required on actual part plus plate | MISSING |
| Manufacturer/workshop-approved pressure and fastening | Required | Required for both interfaces | MISSING |
| Unambiguous source/sensor A and B coordinates | Required | Required, explicitly identify plate vs sink | DESIGN ONLY |
| Independent assembly and mounting history | Required | Required; two contact interfaces | DESIGN ONLY |
| Parasitic wire/fixture heat path assessed | Required | Required | MISSING |
| Actual electrical protection and site permission | Required | Required | NOT GRANTED |
| Qualification-to-target boundary transfer | Physical pilot needed | Physical pilot needed; added interface is model variable | UNVALIDATED |

**Recommended sequence:** obtain/inspect exact sink first → issue a single as-built CAD/thermal-stack decision with explicit fastener loads and sensor accessibility → seek mechanical approval → qualify powered site/instruments independently → execute Q0 pilot only after facility sign-off.

## Gate

Either selection must be justified by observed geometry and approved facility constraints. The existing v0.5 manufacturing HOLD stands. If neither mounting option meets the safety and reproducibility requirements, change the source/fixture hardware rather than force the experiment onto unsuitable geometry.
