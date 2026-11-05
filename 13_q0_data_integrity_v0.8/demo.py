"""Generate ONLY simulated CSV to exercise structural checks, never thermal truth."""
from __future__ import annotations
import argparse
import json
import tempfile
from pathlib import Path
from ebt_q0_data import seal_run, inspect_campaign, RAW_FIELDS

def create_demo(directory):
    from datetime import datetime, timezone
    base=Path(directory)
    base.mkdir(parents=True,exist_ok=True)
    (base/"runs").mkdir(exist_ok=True)
    role_ids={"QUAL":["QUAL-001"],"CAL":["CAL-001"],"HOLD":["HOLD-001"]}
    lock={
        "schema_version":"EBT-SPLIT-008","study_kind":"R01",
        "lock_utc":"2026-11-05T12:00:00Z",
        "protocol_sha256":"f"*64,
        # Deliberately unusable dummy reference for software demonstration.
        "external_lock_ref":"https://github.com/test/synthetic-fixture/commit/"+"a"*40,
        "role_run_ids":role_ids,"demonstration_only":True}
    (base/"split_lock.json").write_text(json.dumps(lock,indent=2)+"\n",encoding="utf-8")
    folder=base/"runs"/"QUAL-001"
    folder.mkdir()
    meta={
        "schema_version":"EBT-RUN-008","run_id":"QUAL-001","role":"QUAL",
        "evidence_class":"SYNTHETIC_DEMO","synthetic_disclosure":True,
        "assembly_id":"ASSEMBLY-001","mount_event_id":"MOUNT-001",
        "heater_id":"HEATER-001","site_id":"SITE-A",
        "fixture_revision":"NOT_A_REAL_FIXTURE",
        "temperature_surface":"T_PLATE",
        "cooling_state":"NAT",
        "cooling_reference_ref":"DEMO-NOT-MEASURED",
        "heater_part_ref":"DEMO-HEATER-CANDIDATE",
        "heating_envelope_ref":"DEMO-NO-APPROVED-POWER",
        "electrical_wiring_ref":"DEMO-NOT-APPROVED-WIRING",
        "sensor_map_ref":"DEMO-SENSOR-MAP",
        "reference_evidence_ref":"DEMO-NOT-CALIBRATED",
        "timebase_ref":"DEMO-TIMEBASE",
        "facility_permission_ref":"DEMO-NO-PERMISSION",
        "protocol_ref":"DEMO-NON-AUTHORIZED",
        "acquired_utc":"2026-11-05T13:00:00Z","review_status":"NOT_VALIDATED"}
    (folder/"metadata.json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")
    (folder/"raw.csv").write_text(",".join(RAW_FIELDS)+"\n"+
       "0,0,0,24,24,24,RUN\n"+
       "1,1,0.1,24.1,24.02,24,RUN\n"+
       "2,1,0.1,24.2,24.04,24,RUN\n",encoding="utf-8")
    seal_run(folder)
    return inspect_campaign(base)

if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out",type=Path,help="Temporary demo destination (optional)")
    args=ap.parse_args()
    if args.out is None:
        with tempfile.TemporaryDirectory() as d:
            print(json.dumps(create_demo(d),indent=2))
    else:
        print(json.dumps(create_demo(args.out),indent=2))
