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

## Subsequent draft research/engineering branches (not merged)

- Draft PR #11: proposed v0.6 conditional spatial model; synthetic-only sensitivity, not manufacturer geometry validation.
- Draft PR #12: proposed v0.7 physical readiness checklist and conditional fixture architecture, with unapproved real access.
- Draft v0.8: \`13_q0_data_integrity_v0.8/\` adds prospective RAW DATA **schema and software verification only**, not a measured experimental campaign.
- Facility correspondence on 5 Nov 2026: Student Workshop Canvas invitation sent (induction yet to be completed); KTH Manufacturing Lab declined casual independent-project access under current policy (MG1000/Maskineriet for enrolled students and formal funded research are described pathways); ELAB authority is unverified.
