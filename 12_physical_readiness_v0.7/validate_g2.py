"""EBT-GATE-007: evidence COMPLETENESS checks, never site authorization.

No connected laboratory or instrument is inspected by this software. Even a
complete record returns HUMAN_REVIEW_REQUIRED rather than SAFE or GO.
Standard library only; do not substitute strings for authentic signed records.
"""
from __future__ import annotations
import argparse
import json
import re
from datetime import datetime
from pathlib import Path

STAGES = {
    "fabrication": (
        "manufacturer_profile_ref",
        "actual_part_inspection_ref",
        "approved_mechanical_drawing_ref",
        "mounting_and_torque_review_ref",
        "thermal_interface_review_ref",
        "workshop_induction_ref",
        "workshop_permission_ref",
    ),
    "powered_q0": (
        "electrical_lab_permission_ref",
        "lab_induction_ref",
        "responsible_supervisor",
        "approved_schematic_ref",
        "psu_model_and_serial_ref",
        "dc_protection_review_ref",
        "independent_shutdown_verification_ref",
        "isolation_and_grounding_review_ref",
        "temperature_reference_chain_ref",
        "voltage_current_reference_chain_ref",
        "sensor_lag_verification_ref",
        "timebase_verification_ref",
        "bounded_power_envelope_ref",
        "risk_review_ref",
    ),
    "r01_confirmatory": (
        "q0_measured_report_ref",
        "measured_uncertainty_budget_ref",
        "preregistered_model_protocol_ref",
        "prereg_lock_utc",
        "prereg_document_sha256",
    ),
}
BAD = {"", "tbd", "todo", "unknown", "n/a", "none", "uninspected",
       "not granted", "not authorized", "not authorised", "placeholder", "example",
       "synthetic", "not started", "pending", "draft"}
STAGE_NAMES = tuple(STAGES)

def evidence_present(value):
    return (isinstance(value, str) and bool(value.strip()) and
            value.strip().lower() not in BAD and
            not value.strip().upper().startswith(("TBD", "TODO", "UNKNOWN", "DEMO_", "EXAMPLE_")))

def _ids(values):
    return isinstance(values,list) and bool(values) and all(
        isinstance(v,str) and re.fullmatch(r"[A-Z][A-Z0-9_-]{2,63}",v)
        for v in values) and len(values)==len(set(values))

def _timestamp(value):
    if not evidence_present(value):
        return False
    try:
        parsed=datetime.fromisoformat(value.replace("Z","+00:00"))
        return parsed.tzinfo is not None and parsed.utcoffset() is not None
    except (ValueError,TypeError,OverflowError):
        return False

def evaluate(record):
    """Structural eligibility only. Never calls this 'safe' or 'approved'."""
    if not isinstance(record,dict):
        raise ValueError("expected JSON object")
    if record.get("schema_version") != "EBT-GATE-007-v0.7":
        raise ValueError("incorrect schema_version")
    review={}
    for stage,fields in STAGES.items():
        data=record.get(stage)
        if not isinstance(data,dict):
            data={}
        missing=[f"{stage}.{f}" for f in fields if not evidence_present(data.get(f))]
        if stage=="fabrication" and data.get("fixture_strategy") not in ("DIRECT_TO_SINK_CANDIDATE","ADAPTER_PLATE_CANDIDATE"):
            missing.append("fabrication.fixture_strategy_validated_selection")
        if stage=="r01_confirmatory":
            if not _timestamp(data.get("prereg_lock_utc")):
                missing.append("r01_confirmatory.prereg_lock_utc_timezone")
            h=data.get("prereg_document_sha256")
            if not isinstance(h,str) or not re.fullmatch(r"[0-9a-f]{64}",h):
                missing.append("r01_confirmatory.prereg_document_sha256_hex")
            names=("qualification_ids","calibration_ids","reserved_holdout_ids")
            groups=[data.get(n) for n in names]
            for name,group in zip(names,groups):
                if not _ids(group):
                    missing.append(f"r01_confirmatory.{name}_unique_nonempty")
            if all(_ids(v) for v in groups):
                ids=[v for group in groups for v in group]
                if len(ids)!=len(set(ids)):
                    missing.append("r01_confirmatory.dataset_partitions_disjoint")
        review[stage]={
          "status":"BLOCKED" if missing else "DOCUMENTS_PRESENT_HUMAN_REVIEW_REQUIRED",
          "missing_evidence_or_invalid_fields":sorted(set(missing)),
          "human_review_is_mandatory":True,
          "is_authorization":False,
        }
    return {
        "report_kind":"STRUCTURAL_EVIDENCE_COMPLETENESS_ONLY",
        "software_grants_no_access_and_approves_no_power_or_fabrication":True,
        "status_by_stage":review,
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record",type=Path)
    args=parser.parse_args()
    try:
        result=evaluate(json.loads(args.record.read_text(encoding="utf-8")))
    except (OSError,json.JSONDecodeError,ValueError) as ex:
        parser.error(str(ex))
    print(json.dumps(result,indent=2,sort_keys=True))
    return 2 if any(s["status"]=="BLOCKED" for s in result["status_by_stage"].values()) else 0

if __name__=="__main__":
    raise SystemExit(main())
