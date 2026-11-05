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
