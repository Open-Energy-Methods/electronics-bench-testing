"""EBT v0.8 evidence-aware raw-data validation. NOT a laboratory safety system.

No real EBT measurements are contained in this package. Hashing checks file
identity, NOT calibration, truthful acquisition, or chronological preregistration.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path

RAW_FIELDS = ("elapsed_s", "heater_voltage_v", "heater_current_a",
              "t_case_c", "t_surface_c", "t_ambient_c", "event_flag")
ROLES = {"Q0_PILOT", "QUAL", "CAL", "HOLD"}
CLASSES = {"SYNTHETIC_DEMO", "PHYSICAL_UNVERIFIED"}
METADATA_FIELDS = (
    "schema_version", "run_id", "role", "evidence_class",
    "assembly_id", "mount_event_id", "heater_id", "site_id",
    "fixture_revision", "temperature_surface", "cooling_state",
    "cooling_reference_ref", "heater_part_ref", "heating_envelope_ref",
    "electrical_wiring_ref", "sensor_map_ref",
    "reference_evidence_ref", "timebase_ref", "facility_permission_ref",
    "protocol_ref", "acquired_utc", "review_status")
ID = re.compile(r"^[A-Z][A-Z0-9_-]{2,63}$")
HEX = re.compile(r"^[0-9a-f]{64}$")
PLACEHOLDERS = {"", "tbd", "pending", "not granted", "unknown", "n/a", "none",
                "uninspected", "placeholder", "not authorized", "demo_only",
                "synthetic", "draft", "example"}

class DataError(ValueError):
    pass

def require(condition, message):
    if not condition:
        raise DataError(message)

def sha256(raw):
    return hashlib.sha256(raw).hexdigest()

def nonplaceholder(value):
    return isinstance(value, str) and value.strip().lower() not in PLACEHOLDERS and bool(value.strip())

def utc_datetime(value):
    require(isinstance(value, str) and (value.endswith("Z") or value.endswith("+00:00")),
            "timestamp must be explicit UTC Z or +00:00")
    try:
        t = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise DataError(f"invalid UTC datetime: {value}") from exc
    require(t.utcoffset() is not None and t.utcoffset().total_seconds() == 0,
            "timestamp is not UTC")
    return t

def no_duplicate_keys(pairs):
    data = {}
    for key, val in pairs:
        require(key not in data, f"duplicate JSON key: {key}")
        data[key] = val
    return data

def load_json(path):
    return json.loads(Path(path).read_bytes(), object_pairs_hook=no_duplicate_keys)

def check_metadata(meta):
    require(isinstance(meta, dict), "metadata must be object")
    require(set(METADATA_FIELDS).issubset(meta), "missing metadata: " +
            ", ".join(sorted(set(METADATA_FIELDS) - set(meta))))
    require(meta["schema_version"] == "EBT-RUN-008", "wrong run schema")
    for key in ("run_id", "assembly_id", "mount_event_id", "heater_id", "site_id"):
        require(isinstance(meta[key], str) and ID.fullmatch(meta[key]) is not None,
                f"invalid {key}")
    require(meta["role"] in ROLES, "unknown dataset role")
    require(meta["evidence_class"] in CLASSES, "unknown evidence class")
    require(meta["temperature_surface"] in {"T_PLATE", "T_SINK"},
            "surface sensor must be unambiguously T_PLATE or T_SINK")
    require(meta["cooling_state"] in {"NAT", "FAN", "OTHER_DOCUMENTED"},
            "cooling_state must be NAT, FAN or OTHER_DOCUMENTED")
    require(meta["review_status"] == "NOT_VALIDATED",
            "automated Q0 ingestion never awards validated status")
    utc_datetime(meta["acquired_utc"])
    for k in ("fixture_revision", "sensor_map_ref", "reference_evidence_ref",
              "cooling_reference_ref", "heater_part_ref",
              "heating_envelope_ref", "electrical_wiring_ref",
              "timebase_ref", "facility_permission_ref", "protocol_ref"):
        require(nonplaceholder(meta[k]), f"missing/placeholder {k}")
    if meta["evidence_class"] == "PHYSICAL_UNVERIFIED":
        for k in ("sensor_map_ref", "reference_evidence_ref", "timebase_ref",
                  "cooling_reference_ref", "heater_part_ref",
                  "heating_envelope_ref", "electrical_wiring_ref",
                  "facility_permission_ref", "protocol_ref"):
            require(not meta[k].upper().startswith(("DEMO", "EXAMPLE", "SYNTHETIC", "TBD")),
                    f"physical metadata may not use demo reference: {k}")
    else:
        require(meta.get("synthetic_disclosure") is True,
                "SYNTHETIC_DEMO must explicitly disclose synthetic provenance")
    return True

def inspect_raw(raw_bytes):
    require(raw_bytes, "empty raw CSV")
    try:
        text = raw_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise DataError("raw CSV must be UTF-8") from exc
    reader = csv.DictReader(io.StringIO(text, newline=""))
    require(reader.fieldnames is not None and tuple(reader.fieldnames) == RAW_FIELDS,
            "exact raw CSV header required: " + ",".join(RAW_FIELDS))
    n = 0
    prev = -math.inf
    issues = []
    aborts = 0
    for n, row in enumerate(reader, start=1):
        require(None not in row and all(isinstance(v, str) for v in row.values()),
                f"malformed CSV row {n}")
        flag = row["event_flag"]
        require(flag in {"RUN", "ABORT", "QUALITY_FLAG"},
                f"row {n}: invalid event_flag")
        t = numeric(row["elapsed_s"], f"row {n} elapsed_s", allow_blank=False)
        require(t >= 0 and t > prev, f"row {n}: time not strictly increasing")
        prev = t
        if flag == "ABORT":
            aborts += 1
        for col in RAW_FIELDS[1:-1]:
            v = numeric(row[col], f"row {n} {col}", allow_blank=True)
            if v is None:
                issues.append(f"row {n}: missing {col}")
            elif col in {"heater_voltage_v", "heater_current_a"} and v < 0:
                issues.append(f"row {n}: negative heater electrical input {col}")
        if flag == "QUALITY_FLAG":
            issues.append(f"row {n}: explicit QUALITY_FLAG")
        if flag == "ABORT":
            issues.append(f"row {n}: ABORT retained, not silently excluded")
    require(n >= 2, "at least two time-indexed raw rows required")
    return {"rows": n, "aborted_samples": aborts, "quality_issues": issues,
            "analysis_status": "REVIEW_REQUIRED" if issues else "STRUCTURALLY_COMPLETE_UNVERIFIED"}

def numeric(value, field, *, allow_blank):
    if allow_blank and value == "":
        return None
    try:
        f = float(value)
    except (ValueError, TypeError) as exc:
        raise DataError(f"not numeric: {field}") from exc
    require(math.isfinite(f), f"non-finite: {field}")
    return f

def inspect_run(path, *, sealed=True):
    root = Path(path)
    meta_path = root / "metadata.json"
    raw_path = root / "raw.csv"
    meta = load_json(meta_path)
    check_metadata(meta)
    require(root.name == meta["run_id"], "run directory and metadata ID mismatch")
    raw_bytes = raw_path.read_bytes()
    qc = inspect_raw(raw_bytes)
    if qc["aborted_samples"] > 0 or any(
        "QUALITY_FLAG" in issue for issue in qc["quality_issues"]
    ):
        require(nonplaceholder(meta.get("deviation_log_ref")),
                "aborts/QUALITY_FLAG rows need deviation_log_ref")
    info = {"run_id": meta["run_id"], "role": meta["role"],
            "evidence_class": meta["evidence_class"],
            "raw_sha256": sha256(raw_bytes),
            "metadata_sha256": sha256(meta_path.read_bytes()),
            **qc, "physical_measurement_claim": False,
            "human_review_required": True}
    if sealed:
        seal = load_json(root / "seal.json")
        require(seal.get("schema_version") == "EBT-SEAL-008", "wrong seal schema")
        require(seal.get("run_id") == meta["run_id"], "seal run mismatch")
        require(seal.get("raw_sha256") == info["raw_sha256"], "raw CSV hash mismatch")
        require(seal.get("metadata_sha256") == info["metadata_sha256"], "metadata hash mismatch")
        utc_datetime(seal.get("sealed_utc"))
        info["sealed"] = True
    else:
        info["sealed"] = False
    return info

def seal_run(path):
    root = Path(path)
    info = inspect_run(root, sealed=False)
    obj = {"schema_version": "EBT-SEAL-008", "run_id": info["run_id"],
           "raw_sha256": info["raw_sha256"],
           "metadata_sha256": info["metadata_sha256"],
           "sealed_utc": datetime.now(timezone.utc).isoformat(),
           "scope": "FILE_INTEGRITY_ONLY_NOT_ACQUISITION_AUTHENTICITY"}
    with (root / "seal.json").open("x", encoding="utf-8") as handle:
        json.dump(obj, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return inspect_run(root)

def check_plan(plan):
    require(isinstance(plan, dict) and plan.get("schema_version") == "EBT-SPLIT-008",
            "wrong plan schema")
    require(plan.get("study_kind") in {"Q0_PILOT", "R01"}, "study kind")
    lock = utc_datetime(plan.get("lock_utc"))
    require(isinstance(plan.get("protocol_sha256"), str) and HEX.fullmatch(plan["protocol_sha256"]),
            "valid protocol sha256 required")
    require(nonplaceholder(plan.get("external_lock_ref")) and not
            plan["external_lock_ref"].upper().startswith(("DEMO", "EXAMPLE", "TBD")),
            "externally verifiable preregistration lock reference required")
    parts = plan.get("role_run_ids")
    require(isinstance(parts, dict), "role_run_ids dictionary required")
    expected = {"Q0_PILOT"} if plan["study_kind"] == "Q0_PILOT" else {"QUAL", "CAL", "HOLD"}
    require(set(parts) == expected, "incorrect role partition keys")
    ids = []
    for role, run_ids in parts.items():
        require(isinstance(run_ids, list) and len(run_ids) >= 1,
                f"{role}: nonempty list required")
        for run_id in run_ids:
            require(isinstance(run_id, str) and ID.fullmatch(run_id), "invalid run ID in plan")
            ids.append(run_id)
    require(len(ids) == len(set(ids)), "overlapping or repeated run IDs across partitions")
    return lock, {rid: role for role, group in parts.items() for rid in group}

def inspect_campaign(folder):
    root = Path(folder)
    lock, roles = check_plan(load_json(root / "split_lock.json"))
    data_root = root / "runs"
    require(data_root.is_dir(), "runs directory missing")
    run_dirs = sorted(x for x in data_root.iterdir() if x.is_dir())
    recorded = set()
    reports = []
    assemblies = {"QUAL": set(), "CAL": set(), "HOLD": set(), "Q0_PILOT": set()}
    events = set()
    evidence_classes = set()
    for d in run_dirs:
        require(d.name in roles, f"unregistered run folder {d.name}")
        info = inspect_run(d)
        meta = load_json(d / "metadata.json")
        require(meta["role"] == roles[d.name], "role mismatch against locked plan")
        require(utc_datetime(meta["acquired_utc"]) >= lock, "run acquired before declared lock")
        require(meta["mount_event_id"] not in events, "reused mount_event_id")
        events.add(meta["mount_event_id"])
        assemblies[meta["role"]].add(meta["assembly_id"])
        evidence_classes.add(meta["evidence_class"])
        recorded.add(d.name)
        reports.append(info)
    require(len(evidence_classes) <= 1, "cannot mix physical and demo runs in a campaign")
    if "HOLD" in assemblies:
        require(not assemblies["HOLD"].intersection(assemblies["CAL"] |
                                                   assemblies["QUAL"]),
                "HOLD assembly overlaps qualification or calibration")
    return {"report_kind": "EVIDENCE_INTEGRITY_AUDIT_NOT_PHYSICAL_VALIDATION",
            "planned_run_count": len(roles), "recorded_run_count": len(recorded),
            "missing_planned_runs": sorted(set(roles) - recorded),
            "checks_do_not_prove_preregistration_timing": True,
            "checks_do_not_grant_facility_authorization": True,
            "runs": reports,
            "status": "REVIEW_REQUIRED" if recorded else "NO_ACQUISITION_RECORDS",
            "external_lock_ref_unverified_by_software": True}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    for cmd in ("seal", "run", "campaign"):
        sub.add_parser(cmd).add_argument("directory", type=Path)
    args = ap.parse_args()
    try:
        result = {"seal": seal_run, "run": inspect_run, "campaign": inspect_campaign}[args.command](args.directory)
    except (DataError, OSError, KeyError, json.JSONDecodeError) as exc:
        ap.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
