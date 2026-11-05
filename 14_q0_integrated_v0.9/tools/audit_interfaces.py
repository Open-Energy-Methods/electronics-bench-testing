"""EBT-Q0-009 cross-interface compatibility audit, WITHOUT site approval.

Merges semantic connections among v0.7 structural stage gates, v0.8 R01
split locks, and the source inventory. The authoritative record formats
remain v0.7 EBT-GATE-007 and v0.8 EBT-SPLIT-008 / EBT-RUN-008.
No field or combination of fields returns "SAFE" or "AUTHORIZED".
"""
from __future__ import annotations
import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "12_physical_readiness_v0.7"))
sys.path.insert(0, str(ROOT / "13_q0_data_integrity_v0.8"))
from validate_g2 import evaluate as evaluate_stage_gate
from ebt_q0_data import check_plan, check_metadata, utc_datetime, DataError

GATE_PATH = ROOT / "12_physical_readiness_v0.7/templates/EBT-GATE-007_record_UNFILLED.json"
SPLIT_PATH = HERE / "templates/EBT-SPLIT-009_R01_UNFILLED.json"
RUN_PATH = HERE / "templates/EBT-RUN-009_PHYSICAL_UNFILLED.json"
CROSSWALK_PATH = HERE / "interfaces/EBT-Q0-009_crosswalk.csv"
R01_FIELDS = {
    "prereg_document_sha256": "protocol_sha256",
    "qualification_ids": "QUAL",
    "calibration_ids": "CAL",
    "reserved_holdout_ids": "HOLD",
}

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def audit_crosswalk(path=CROSSWALK_PATH):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))
    ids = [r["item_id"] for r in records]
    if len(ids) != len(set(ids)) or len(records)<10:
        raise ValueError("crosswalk must have >=10 uniquely identified entries")
    absent = []
    for entry in records:
        for name in ("authoritative_source", "related_source"):
            path = (ROOT / entry[name]).resolve()
            if ROOT not in path.parents or not path.is_file():
                absent.append(f"{entry['item_id']}: {name}: {entry[name]}")
        if not entry["physical_gate"] or not entry["current_resolution"]:
            absent.append(f"{entry['item_id']}: resolution or gate missing")
    if absent:
        raise ValueError("crosswalk broken: " + "; ".join(absent))
    return records

def verify_lock_mapping(gate, plan):
    """Return issues; this is not proof of historical preregistration."""
    issues = []
    try:
        check_plan(plan)
    except (DataError, KeyError, TypeError, ValueError) as exc:
        return ["SPLIT_INVALID_OR_UNFILLED: " + str(exc)]
    if plan["study_kind"] != "R01":
        return ["EXPECTED_R01_SPLIT_NOT_Q0_PILOT"]
    g = gate.get("r01_confirmatory", {})
    try:
        lhs = utc_datetime(g.get("prereg_lock_utc"))
        rhs = utc_datetime(plan.get("lock_utc"))
        if lhs != rhs:
            issues.append("LOCK_INSTANT_MISMATCH")
    except (DataError, TypeError, KeyError):
        issues.append("GATE_PREREG_LOCK_MISSING_OR_INVALID")
    sha = g.get("prereg_document_sha256")
    if not isinstance(sha, str) or sha != plan.get("protocol_sha256"):
        issues.append("PROTOCOL_SHA256_MISMATCH")
    for gate_field, role in list(R01_FIELDS.items())[1:]:
        ids = g.get(gate_field)
        source = plan["role_run_ids"].get(role)
        if not isinstance(ids, list) or set(ids) != set(source) or len(ids) != len(set(ids)):
            issues.append("ROLE_PARTITION_MISMATCH_" + role)
    return issues

def run_audit(gate_path=GATE_PATH,split_path=SPLIT_PATH):
    audit_crosswalk()
    gate = read_json(gate_path)
    split = read_json(split_path)
    template_run = read_json(RUN_PATH)
    # Templates MUST be invalid for acquisition: they are deliberately unfilled.
    template_run_invalid = False
    try:
        check_metadata(template_run)
    except (DataError, KeyError, ValueError, TypeError):
        template_run_invalid = True
    stage = evaluate_stage_gate(gate)
    mismatch = verify_lock_mapping(gate,split)
    is_blocked = any(x["status"] == "BLOCKED" for x in stage["status_by_stage"].values())
    return {
      "report_class": "REVIEW_OF_RECORD_STRUCTURES_NOT_PHYSICAL_EVIDENCE",
      "integration_revision": "EBT-Q0-009-v0.9",
      "physical_test_observations_count": 0,
      "run_metadata_template_invalid_until_populated": template_run_invalid,
      "g2_g3": {k:v["status"] for k,v in stage["status_by_stage"].items()},
      "declared_r01_cross_record_discrepancies": mismatch,
      "unfilled_templates_intentionally_blocked": is_blocked,
      "project_status": "BLOCKED_NEEDS_PHYSICAL_EVIDENCE" if is_blocked or mismatch
                        else "STRUCTURAL_RECORDS_PRESENT_HUMAN_REVIEW_REQUIRED",
      "software_never_grants_fabrication_or_power_authority": True,
      "external_preregistration_and_permission_refs_not_authenticated": True
    }

def main():
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument("--gate",type=Path,default=GATE_PATH)
    pa.add_argument("--split",type=Path,default=SPLIT_PATH)
    pa.add_argument("--json-out",type=Path,default=None)
    args=pa.parse_args()
    report=run_audit(args.gate,args.split)
    output=json.dumps(report,indent=2,sort_keys=True)+"\n"
    print(output,end="")
    if args.json_out:
        args.json_out.write_text(output,encoding="utf-8")
    # 0 = successfully audited, not pass/physical authorization
    return 0

if __name__=="__main__":
    raise SystemExit(main())
