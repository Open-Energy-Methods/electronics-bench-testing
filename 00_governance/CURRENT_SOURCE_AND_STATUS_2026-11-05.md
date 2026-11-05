# Current status, source hierarchy and nonphysical evidence policy (2026-11-05)

**No real EBT electrothermal experiments have been performed.** `07_source_baseline/` is historical v0.1 with model-generated datasets, figures and synthetic results. `09_model_comparison/` is v0.4 synthetic numerical work; it is not laboratory data. The new `10_fixture_v0.5/` is an **unapproved engineering preliminary design**, not a manufactured or approved rig. No instrument calibration, real boundary coefficient, safe setpoints or qualified physical model predictive accuracy are reported.

## Precedence for future readers

1. **Programme baseline (unchanged):** `EBT_Master_Programme_Plan_v1.0.md` and historical PDF/DOCX, archive retained for provenance.
2. **Current scientific/novelty limits:** `01_research/EBT-LIT-003_critical_full_text_assessment_v0.3.md` and `EBT-R01_paper_positioning_decision_v0.3.md`; G1 still open.
3. **Current numerical benchmark:** `09_model_comparison/` B0–B3 synthetic models. Checked figure/result snapshots are generated program outputs and cannot substitute for physical validation.
4. **Current proposed rig:** `10_fixture_v0.5/` design documents and drawings **not for manufacture/test**; G2 and G3 still open.
5. **Physical pilot and campaign:** `03_campaigns/` pre-registration drafts; never interpret blank/12-row/54-row planning tables as executed runs.
6. **Historical import helpers:** `GITHUB_IMPORT.md`, `00_governance/RELEASE_MANIFEST_SHA256.json` (historical import package hashes) and `08_project_controls/qa_report.json` (baseline QA snapshot) are **not current operational status reports**.

## Classification and status vocabulary

- `SOURCE_SPECIFICATION`: manufacturer or verified reseller published dimensions, part/price as of stated retrieval date; **not product measured**.
- `DESIGN_ASSUMPTION`: chosen geometry, sample rate or circuit topology; **not manufacturer-released**.
- `SYNTHETIC_ONLY`: generated numerical data/figures and fitting metrics, not physical replication.
- `REVIEWED_LITERATURE`: actual source-method assessment, varying from full text to abstract; **not experimental EBT evidence or novelty clearance**.
- `UNKNOWN_UNINSPECTED`: laboratory/equipment status not independently verified.
- `PDR_ONLY`: explicit engineering proposal, do not manufacture or energize.
- `PHYSICAL_VERIFIED`: **zero records** at current project date.

## Manifest and QA scope

The historic 65-entry `00_governance/RELEASE_MANIFEST_SHA256.json` refers to the v1.0 import package and was never a live mirror of GitHub's evolving tree. Likewise `08_project_controls/qa_report.json` contains historical baseline counts. **Do not update their old numerical claims to falsely imply they reverify current files**. For a current GitHub tree snapshot use the actual Git commit plus `git ls-tree` or GitHub tree API; for output file integrity use the v0.4 results SHA file generated from the current checked outputs.

## Work-status rule

A successful GitHub numerical CI check demonstrates **source/software verification**, not calibrated instruments, safety authorization, physical heat-transfer model validation or scientific novelty. Publish a figure only with its numerical/physical evidence class in the caption.

## Current integrated Q0 review status — v0.9 (5 November 2026)

The **current** Q0 documentation index is [14_q0_integrated_v0.9/README.md](../14_q0_integrated_v0.9/README.md).
It reconciles the following preserved independent work packages:

- \`11_spatial_transfer_v0.6/\` — conditional **synthetic plate** spatial analysis, not a measured Fischer SK 92 thermohydraulic/thermal network.
- \`12_physical_readiness_v0.7/\` — nominal **10 mm** heatsink-family base specification, unfilled physical inspection/permission gates, direct/adapter decision candidate. No authorized machining.
- \`13_q0_data_integrity_v0.8/\` — future physical data schema and **synthetic demonstration** of data checks; all actual thermometry, calibration and timestamps unverified.
- \`14_q0_integrated_v0.9/\` — unique Q0 index, physical review sequence and cross-record compatibility audit; NOT a site-approved operational SOP.

**Original source baseline and earlier drawings remain preserved and unreleased.**
Under the integrated contract, the 12-run screening plan and the 8-event
source/site crossover are alternative research pilots. No blanket 20-run
experimental authorization is implied, nor is the 54-row R01 design executed.
Passing CI establishes parser/method verification only, not physical validity.
## Future execution workplan (minor implementation revision v1.1)

[EBT-EXEC-011](../15_execution_v1.1/README.md) extends G0–G6 stages from the **unchanged** v1.0 master programme; planning records are not physical evidence. The dated [gate snapshot](../15_execution_v1.1/controls/EBT-EXEC-011_gate_snapshot.json) makes explicit that all physical authority and R01 experimental gates are blocked or unvalidated as of 2026-11-05. The [37-task register](../15_execution_v1.1/controls/EBT-EXEC-011_dependencies.csv) is a future work dependency map, not an executed-work claim. Q0-010 remains unpowered intake, and the v0.9 Q0 authority is unchanged.
