# Electronics Bench Testing — controlled programme baseline v1.0

**Status: research planning and verified synthetic feasibility. No physical experiments yet. No KTH institutional approval or accreditation.**

This package converts a series of conversations and the EBT-R01 v0.1 feasibility demonstrator into an **editable, controlled, thesis-equivalent independent research programme**. The programme is living: updates enter through change requests and revisions instead of replacing the whole plan.

Start with:
1. `EBT_Master_Programme_Plan_v1.0.pdf` (readable master programme) or `.docx` (editable), also `.md` for diffable source.
2. `08_project_controls/` (requirements, risks, decisions, tasks, standards, literature, instrument, budget, documents, change requests).
3. `03_campaigns/EBT-Q0/` (pre-test qualification protocol) and `03_campaigns/EBT-R01/` (test plan and 54-row provisional design matrix).
4. `07_source_baseline/EBT_R01_Feasibility_v0.1/` (preserved synthetic model/code/data; never rename as physical test results).
5. `00_governance/CHANGE_CONTROL.md` (how to update without restarting the concept phase).

**Release sequence:** governed plan → pilot authorization and metrology → preregistered experimental protocol → data → holdout analysis → report and open archive → paper pitch/review.

### Current research literature assessment (2026-11-05)

- [EBT-LIT-003 critical full-text assessment v0.3](01_research/EBT-LIT-003_critical_full_text_assessment_v0.3.md) — original full-text reviews where legally retrievable; access-graded records for restricted competitors.
- [14-source evidence matrix](08_project_controls/fulltext_evidence_matrix_v0.3.csv) and [reproducible access/search audit](08_project_controls/literature_search_log_v0.3.csv).
- [EBT-R01 manuscript positioning decision](01_research/EBT-R01_paper_positioning_decision_v0.3.md) — prospective cross-boundary transient temperature validation is a **candidate** contribution, not confirmed novelty.
- **Gate G1 remains open:** the exact methods of several competing papers are access-limited; a formal database-based search is still outstanding. Nothing is authorized for physical testing by this document.

### Verify existing feasibility code

```
cd 07_source_baseline/EBT_R01_Feasibility_v0.1
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pytest -q
python scripts/run_study.py
```

The seven physics/unit tests passed in the authoring environment on 2026-11-05. The generated measurements are synthetic and must be labeled as such.

### Changes

Submit new proposals through `08_project_controls/change_requests.csv` and `06_templates/change_request.md`. Minor adjustments should not reopen the research question. A scientific pivot is permitted, but requires explicit versioning and an impact assessment.

**Independence:** authored as an independent technical study. Facility access, staff approval, coauthorship and journal acceptance are not implied.

### EBT-R01 model and independent boundary qualification (synthetic v0.4)

The [executable model comparison](09_model_comparison/README.md) contains B0 static, B1 one-RC, B2 fixed-boundary two-node and B3 independently boundary-qualified two-node models, a package-only observability ablation, synthetic qualification, stress scenarios, uncertainty formulas and tests.

The [critical methods report](09_model_comparison/docs/EBT-R01_model_comparison_and_boundary_qualification_v0.4.md) documents the transferability failure under mismatched heating/fixture geometries, and why a locally measured apparent sink resistance is not automatically a convection coefficient. No physical experiments, KTH authorization or scientific novelty are claimed.
