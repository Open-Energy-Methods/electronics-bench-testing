"""Validate EBT-EXEC-011 dependency and gate snapshot; NEVER authorizes a test."""
from __future__ import annotations
import csv, json, re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parents[1]
CSV=HERE/"controls/EBT-EXEC-011_dependencies.csv"
SNAP=HERE/"controls/EBT-EXEC-011_gate_snapshot.json"
GATES={f"G{i}" for i in range(7)}
STATUS={"PLANNED","IN_PROGRESS","BLOCKED","CONDITIONAL"}
NEEDED={"task_id","gate","work_package","task","depends_on","status",
        "owner","acceptance_evidence","timing"}
PARTS=[
 "plans/EBT-LIT-011_governance_and_novelty.md",
 "plans/EBT-HW-011_facility_hardware_release.md",
 "plans/EBT-MET-011_metrology_and_pilot.md",
 "plans/EBT-R01-011_design_and_acquisition.md",
 "plans/EBT-ANL-011_analysis_validation.md",
 "plans/EBT-PUB-011_open_release.md",
 "plans/EBT-OPS-011_schedule_budget_contingencies.md",
 "controls/EBT-EXEC-011_decision_queue.csv",
 "controls/EBT-EXEC-011_gate_snapshot.json",
 "controls/EBT-EXEC-011_dependencies.csv",
]

def read_plan(path=CSV):
    with Path(path).open(encoding="utf-8-sig",newline="") as file:
        dr=csv.DictReader(file)
        if dr.fieldnames is None or set(dr.fieldnames)!=NEEDED:
            raise ValueError("Wrong task register schema")
        return list(dr)

def validate_dependencies(rows):
    if len(rows)<30:
        raise ValueError("Incomplete future workplan: expected at least 30 task records")
    ids=[r["task_id"] for r in rows]
    if len(ids)!=len(set(ids)):
        raise ValueError("Duplicate task IDs")
    tasks={r["task_id"]:r for r in rows}
    incoming={}
    for id,r in tasks.items():
        if re.fullmatch(r"E-\d{3}",id) is None:
            raise ValueError("Malformed task ID")
        if r["gate"] not in GATES:
            raise ValueError(f"Unrecognized gate at {id}")
        if r["status"] not in STATUS:
            raise ValueError(f"Invalid task status {id}; plans cannot award physical completion")
        if not all(r.get(k) for k in ("task","owner","acceptance_evidence","timing")):
            raise ValueError(f"Incomplete acceptance/ownership {id}")
        deps=[x.strip() for x in r["depends_on"].split(";") if x.strip()]
        if len(deps)!=len(set(deps)) or id in deps:
            raise ValueError(f"Repeated/self dependency {id}")
        if any(x not in tasks for x in deps):
            raise ValueError(f"Unknown prerequisite at {id}")
        incoming[id]=set(deps)
    # Detect cycles deterministically with topological sorting.
    remaining={k:set(v) for k,v in incoming.items()}
    order=[]
    while remaining:
        ready=sorted(k for k,v in remaining.items() if not v)
        if not ready:raise ValueError("Dependency cycle")
        for item in ready:
            order.append(item)
            del remaining[item]
        for v in remaining.values():
            v.difference_update(ready)
    return order

def validate_gates(snap):
    if snap.get("schema_version")!="EBT-EXEC-011-GATES-1":
        raise ValueError("Gate schema incompatible")
    status=snap.get("gate_status")
    if not isinstance(status,dict) or set(status)!=GATES:
        raise ValueError("Missing G0–G6")
    for g,r in status.items():
        if not isinstance(r,dict) or not r.get("status"):
            raise ValueError(f"Missing recorded status {g}")
        if r.get("actual_authority_ref") is not None:
            # This particular dated planning snapshot has NO approvals.
            raise ValueError(f"Unsupported authority reference in planning snapshot: {g}")
    for key in ("hardware_fabrication_permission_confirmed",
                "powered_q0_site_permission_confirmed",
                "independent_r01_holdout_executed",
                "automatic_safety_release_permitted"):
        if snap.get(key) is not False:
            raise ValueError(f"No confirmed physical evidence: {key} must be false")
    if snap.get("no_physical_ebt_measurements_confirmed_as_of_date") is not True:
        raise ValueError("Historical evidence scope changed without review")
    for g in ("G2","G3","G4","G5","G6"):
        if status[g]["status"].startswith(("APPROVED","PASSED","COMPLETE")):
            raise ValueError(f"False physical gate claim: {g}")
    return True

def audit():
    rows=read_plan()
    sequence=validate_dependencies(rows)
    snap=json.loads(SNAP.read_text(encoding="utf-8"))
    validate_gates(snap)
    missing=[part for part in PARTS if not (HERE/part).is_file()]
    if missing:raise ValueError("Missing planned document(s): "+", ".join(missing))
    return {
      "audit_class":"FUTURE_PLANNING_DEPENDENCY_CONSISTENCY_ONLY",
      "task_count":len(rows),
      "gate_count":len(snap["gate_status"]),
      "task_status_counts":dict(sorted(Counter(r["status"] for r in rows).items())),
      "independently_reproducible_dependency_order":sequence,
      "physical_permission_granted_by_software":False,
      "physical_data_validated_by_software":False,
      "status":"PLAN_STRUCTURALLY_CONSISTENT_PHYSICAL_GATES_BLOCKED"
    }

if __name__=="__main__":
    import argparse
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(audit(),indent=2))
