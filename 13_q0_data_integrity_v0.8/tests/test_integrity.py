"""Adversarial synthetic data tests. No physical EBT measurement is generated."""
from __future__ import annotations
import copy
import json
import tempfile
import unittest
from pathlib import Path
from ebt_q0_data import (
    RAW_FIELDS, DataError, check_metadata, check_plan, inspect_campaign,
    inspect_raw, inspect_run, load_json, seal_run
)

RAW_HEADER=",".join(RAW_FIELDS)+"\n"
RAW_VALID=(RAW_HEADER+
           "0,0,0,24,24,24,RUN\n"
           "1,1,0.1,24.1,24.02,24,RUN\n"
           "2,1,0.1,24.2,24.04,24,RUN\n")
LOCK="2026-11-05T12:00:00Z"
ACQUIRED="2026-11-05T13:00:00Z"

def metadata(run_id="QUAL-001",role="QUAL",assembly="ASSEMBLY-001",
             event="MOUNT-001",evidence="SYNTHETIC_DEMO"):
    return dict(
      schema_version="EBT-RUN-008",run_id=run_id,role=role,
      evidence_class=evidence,assembly_id=assembly,mount_event_id=event,
      heater_id="HEATER-001",site_id="SITE-A",
      fixture_revision="CONCEPT-008",temperature_surface="T_PLATE",
      cooling_state="NAT", cooling_reference_ref="DEMO-NO-COOLING-EVIDENCE",
      heater_part_ref="DEMO-CANDIDATE", heating_envelope_ref="DEMO-UNAPPROVED",
      electrical_wiring_ref="DEMO-WIRING",
      sensor_map_ref="DEMO-SENSOR-MAP",reference_evidence_ref="DEMO-REFERENCES",
      timebase_ref="DEMO-TIMEBASE",facility_permission_ref="DEMO-NO-PERMISSION",
      protocol_ref="DEMO-NON-AUTHORIZED",acquired_utc=ACQUIRED,
      review_status="NOT_VALIDATED",synthetic_disclosure=True)

def plan(parts=None,kind="R01"):
    if parts is None:
        parts={"QUAL":["QUAL-001"],"CAL":["CAL-001"],"HOLD":["HOLD-001"]}
    return dict(schema_version="EBT-SPLIT-008",study_kind=kind,
       lock_utc=LOCK,protocol_sha256="f"*64,
       external_lock_ref="https://github.com/test/synthetic-fixture/commit/"+"a"*40,
       role_run_ids=parts)

def save_json(path,obj):
    Path(path).write_text(json.dumps(obj,indent=2)+"\n",encoding="utf-8")

class DataChecks(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/"runs").mkdir()
        save_json(self.root/"split_lock.json",plan())

    def make_run(self,run_id="QUAL-001",role="QUAL",assembly="ASSEMBLY-001",
                 event="MOUNT-001",raw=RAW_VALID,evidence="SYNTHETIC_DEMO",
                 sealed=True):
        folder=self.root/"runs"/run_id
        folder.mkdir()
        meta=metadata(run_id,role,assembly,event,evidence)
        if evidence=="PHYSICAL_UNVERIFIED":
            # Test-only invented references; validator does not assess their authenticity.
            for k in ("sensor_map_ref","reference_evidence_ref","timebase_ref",
                      "cooling_reference_ref","heater_part_ref",
                      "heating_envelope_ref","electrical_wiring_ref",
                      "facility_permission_ref","protocol_ref"):
                meta[k]="REF-TEST-SHAPE-NOT-REAL"
            meta.pop("synthetic_disclosure")
        save_json(folder/"metadata.json",meta)
        (folder/"raw.csv").write_text(raw,encoding="utf-8")
        if sealed:
            seal_run(folder)
        return folder

    def test_unacquired_plan_does_not_claim_data(self):
        r=inspect_campaign(self.root)
        self.assertEqual(r["recorded_run_count"],0)
        self.assertEqual(r["status"],"NO_ACQUISITION_RECORDS")
        self.assertTrue(r["checks_do_not_grant_facility_authorization"])

    def test_seal_and_inspect_valid_synthetic_example(self):
        run=self.make_run()
        info=inspect_run(run)
        self.assertEqual(info["evidence_class"],"SYNTHETIC_DEMO")
        self.assertEqual(info["rows"],3)
        self.assertEqual(info["quality_issues"],[])
        self.assertFalse(info["physical_measurement_claim"])
        self.assertTrue(info["human_review_required"])
        self.assertEqual(inspect_campaign(self.root)["recorded_run_count"],1)

    def test_seal_is_create_only(self):
        run=self.make_run()
        with self.assertRaises(FileExistsError):
            seal_run(run)

    def test_raw_tamper_is_rejected(self):
        run=self.make_run()
        with (run/"raw.csv").open("a",encoding="utf-8") as f:
            f.write("3,1,0.1,24.3,24.05,24,RUN\n")
        with self.assertRaisesRegex(DataError,"raw CSV hash mismatch"):
            inspect_run(run)

    def test_metadata_tamper_is_rejected(self):
        run=self.make_run()
        m=load_json(run/"metadata.json")
        m["heater_id"]="HEATER-NEW"
        save_json(run/"metadata.json",m)
        with self.assertRaisesRegex(DataError,"metadata hash mismatch"):
            inspect_run(run)

    def test_duplicate_json_keys_rejected(self):
        p=self.root/"double.json"
        p.write_text('{"schema_version":"X","schema_version":"Y"}',encoding="utf-8")
        with self.assertRaisesRegex(DataError,"duplicate JSON"):
            load_json(p)

    def test_csv_header_and_time_order(self):
        with self.assertRaisesRegex(DataError,"exact raw CSV header"):
            inspect_raw(b"wrong,header\n1,2\n")
        bad=RAW_HEADER+"0,0,0,24,24,24,RUN\n0,0,0,24,24,24,RUN\n"
        with self.assertRaisesRegex(DataError,"not strictly increasing"):
            inspect_raw(bad.encode())

    def test_nonfinite_and_negative_heater_are_flagged_or_rejected(self):
        with self.assertRaisesRegex(DataError,"non-finite"):
            inspect_raw((RAW_HEADER+"0,0,0,24,24,24,RUN\n1,nan,0.1,24,24,24,RUN\n").encode())
        raw=RAW_HEADER+"0,0,0,24,24,24,RUN\n1,-1,0.1,24,24,24,RUN\n"
        self.assertTrue(inspect_raw(raw.encode())["quality_issues"])

    def test_abort_missing_sensor_is_preserved_not_imputed(self):
        raw=RAW_HEADER+"0,0,0,24,24,24,RUN\n1,1,0.1,,24.1,24,ABORT\n"
        x=inspect_raw(raw.encode())
        self.assertEqual(x["aborted_samples"],1)
        self.assertIn("row 2: missing t_case_c",x["quality_issues"])
        self.assertEqual(x["analysis_status"],"REVIEW_REQUIRED")

    def test_metadata_rejects_ambiguous_thermometry(self):
        m=metadata()
        m["temperature_surface"]="T_SINK_OR_PLATE"
        with self.assertRaisesRegex(DataError,"unambiguously"):
            check_metadata(m)

    def test_physical_run_rejects_demo_permission_placeholder(self):
        m=metadata(evidence="PHYSICAL_UNVERIFIED")
        with self.assertRaises(DataError):
            check_metadata(m)

    def test_cooling_state_and_electrical_chain_are_required(self):
        m=metadata()
        m["cooling_state"]="UNCONTROLLED"
        with self.assertRaisesRegex(DataError,"cooling_state"):
            check_metadata(m)
        m=metadata()
        m["heating_envelope_ref"]="TBD"
        with self.assertRaisesRegex(DataError,"heating_envelope_ref"):
            check_metadata(m)
        m=metadata()
        m.pop("electrical_wiring_ref")
        with self.assertRaisesRegex(DataError,"missing metadata"):
            check_metadata(m)

    def test_abort_requires_deviation_log_and_preserves_raw(self):
        raw=(RAW_HEADER+"0,0,0,24,24,24,RUN\n"+
             "1,1,0.1,,24.2,24,ABORT\n")
        run=self.make_run(raw=raw,sealed=False)
        with self.assertRaisesRegex(DataError,"deviation_log_ref"):
            seal_run(run)
        m=load_json(run/"metadata.json")
        m["deviation_log_ref"]="DEMO-ABORT-REASON-RETAINED"
        save_json(run/"metadata.json",m)
        info=seal_run(run)
        self.assertEqual(info["aborted_samples"],1)
        self.assertEqual(info["analysis_status"],"REVIEW_REQUIRED")
        self.assertTrue(any("missing t_case_c" in s for s in info["quality_issues"]))

    def test_duplicate_and_overlapping_plan_ids(self):
        p=plan({"QUAL":["QUAL-001"],"CAL":["QUAL-001"],"HOLD":["HOLD-001"]})
        with self.assertRaisesRegex(DataError,"overlapping"):
            check_plan(p)

    def test_unverified_plan_lock_timestamp_rejected(self):
        p=plan()
        p["lock_utc"]="2026-11-05T12:00:00"
        with self.assertRaisesRegex(DataError,"explicit UTC"):
            check_plan(p)
        p=plan()
        p["protocol_sha256"]="deadbeef"
        with self.assertRaisesRegex(DataError,"sha256"):
            check_plan(p)

    def test_role_mismatch_against_plan_rejected(self):
        self.make_run(role="CAL")
        with self.assertRaisesRegex(DataError,"role mismatch"):
            inspect_campaign(self.root)

    def test_acquisition_before_lock_rejected(self):
        run=self.make_run(sealed=False)
        m=load_json(run/"metadata.json")
        m["acquired_utc"]="2026-11-04T12:00:00Z"
        save_json(run/"metadata.json",m)
        seal_run(run)
        with self.assertRaisesRegex(DataError,"before declared lock"):
            inspect_campaign(self.root)

    def test_independent_mount_event_identity(self):
        self.make_run()
        self.make_run("CAL-001","CAL","ASSEMBLY-002","MOUNT-001")
        with self.assertRaisesRegex(DataError,"reused mount_event_id"):
            inspect_campaign(self.root)

    def test_holdout_assembly_overlap_rejected(self):
        self.make_run()
        self.make_run("HOLD-001","HOLD","ASSEMBLY-001","MOUNT-002")
        with self.assertRaisesRegex(DataError,"HOLD assembly overlaps"):
            inspect_campaign(self.root)

    def test_mixed_demonstration_and_physical_is_forbidden(self):
        self.make_run()
        self.make_run("CAL-001","CAL","ASSEMBLY-002","MOUNT-002",
                      evidence="PHYSICAL_UNVERIFIED")
        with self.assertRaisesRegex(DataError,"cannot mix"):
            inspect_campaign(self.root)

    def test_future_planned_holdout_not_falsely_completed(self):
        self.make_run()
        report=inspect_campaign(self.root)
        self.assertEqual(report["missing_planned_runs"],["CAL-001","HOLD-001"])
        self.assertTrue(report["checks_do_not_prove_preregistration_timing"])
        self.assertTrue(report["external_lock_ref_unverified_by_software"])

if __name__=="__main__":
    unittest.main()
