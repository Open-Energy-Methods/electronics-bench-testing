# EBT-EXEC-011 — Remaining research, engineering and publication programme (v1.1)

**Planning revision:** 2026-11-05 · **Governed by:** [EBT-PMP-001 v1.0](../EBT_Master_Programme_Plan_v1.0.md) and [change control](../00_governance/CHANGE_CONTROL.md).
**Scientific objective unchanged:** surface observability, independent cooling-boundary transfer and mounting variability. **Status:** a proposed **execution plan**, not a new research claim, site SOP, fabrication drawing or proof of experiments.

## One entry point for all remaining work

This package continues from [the merged Q0 v0.9 engineering authority](../14_q0_integrated_v0.9/README.md) and [Q0-010 unpowered component intake](../14_q0_integrated_v0.9/docs/EBT-Q0-010_unpowered_intake.md). These remain authoritative for hardware details and real instrument evidence. The v0.1–v0.8 source models/data are preserved. This file defines *future work*, not measured results.

| Gate | Exact deliverable needed to leave gate | Current evidence / disposition | Cannot be bypassed by |
|---|---|---|---|
| G0 · Programme | reviewed controlled plan, change and decision register | baseline prepared; internal acceptance still to record | a GitHub merge alone |
| G1 · Differentiation | graded competing-source matrix, claim-level gap and fallback framing, dated independent research review where feasible | partial source assessment; **OPEN** | publication enthusiasm |
| G2 · Safety/site/fixture | actual inspected part, competent machining approval, separately permitted powered site, signed local SOP/electrical limits, reference instruments | catalog and unfilled templates only; **HOLD** | KTH workshop Canvas invitation or passing CI |
| G3 · Q0 and R01 lock | physically measured pilot, uncertainty, suitable boundaries, independent remount variance, site-approved DOE, external preregistration and partitions | no Q0 measurements; **HOLD** | synthetic noise/cooling simulations |
| G4 · Data | authorized complete acquisition, immutable originals and aborts, distinct independent mounts, reviewable rights | no EBT physical data; **HOLD** | number of raw files or time samples |
| G5 · Inference | verified B0–B3 implementations, predeclared prospective HOLD comparisons and uncertainties, negative-case assessment | numerical V&V only; **HOLD physical validation** | low synthetic RMSE |
| G6 · Dissemination | traceable raw-to-result reproduction, appropriate authorship/permissions, paper vs methods benchmark vs technical-report decision, separate archival DOI | preliminary release checklist; **HOLD** | a Zenodo record alone |

**G1 and remote numerical work can proceed while G2 is blocked.** G3 follows *actual* G2 authorization and Q0. G4–G6 depend on real data if an experimental paper is claimed. A non-experimental technical report remains a defensible fallback with properly labelled scope.

## Detailed work packages

1. [WP0/1 — governance and novelty-clearance](plans/EBT-LIT-011_governance_and_novelty.md)
2. [WP0/2 — facility access, procurement and mechanical/electrical design release](plans/EBT-HW-011_facility_hardware_release.md)
3. [WP3 — metrology and executable Q0 qualification proposal](plans/EBT-MET-011_metrology_and_pilot.md)
4. [WP4/5 — R01 experiment and prospective preregistration](plans/EBT-R01-011_design_and_acquisition.md)
5. [WP6/7 — models, statistics, uncertainty, independent validation](plans/EBT-ANL-011_analysis_validation.md)
6. [WP8/9 — research publication, open archive, portfolio](plans/EBT-PUB-011_open_release.md)
7. [Constraints, spend, risk, time and no-lab fallback](plans/EBT-OPS-011_schedule_budget_contingencies.md)

[Machine-readable dependency worklist](controls/EBT-EXEC-011_dependencies.csv) lists exact prerequisites, owners and evidence; [gate snapshot](controls/EBT-EXEC-011_gate_snapshot.json) is explicitly **UNVERIFIED / NO-GO** for the physical stages. The [offline checker](tools/check_roadmap.py) checks only plan structure and blocked-state consistency, never safety authority.

## Scientific interface decisions that must be resolved *before* physical R01

- **Mount identities:** one mount event may have multiple power/cooling runs. A distinct remount is a documented teardown/reassembly, a **new mount_event_id and assembly_id**; samples and repeated runs are not independent remount replicates. Updated in canonical v0.8 data checker and regression tests.
- **Cooling:** old provisional R01 labels `NAT/PASS/FORCED` must NOT automatically map to v0.8 `NAT/FAN/OTHER_DOCUMENTED`. In particular, what `PASS` differs from `NAT` must be physically defined, or one level removed; forced-air is only FAN if a fan is actually controlled/measured.
- **A/B:** Q0 source sites A/B describe heater *position*. Original R01 interface A/B describes a *thermal attachment/interface treatment*. These are not interchangeable factors. Assign independent field names.
- **B0–B3:** no fitted parameter, boundary coefficient, model order, sensor layout or exclusion threshold may be selected using HOLD temperature outcomes.
- **Quantities:** heater-terminal `V×I` is not identical to heat deposited into an optional plate; `T_case` is not junction; `T_plate` is not `T_sink`; apparent Rth is not a unique convective coefficient.

## Operating discipline

Review the [dependency register](controls/EBT-EXEC-011_dependencies.csv) each week. Close a task only with actual path(s), named responsible human review where needed, date, and acceptance evidence. The default for unobserved equipment, permissions, calibration and outcomes is **BLOCKED** or **NOT STARTED**. Timelines below are conditional windows, not promised dates. Even a complete software validator never gives GO for fabrication or energization.
