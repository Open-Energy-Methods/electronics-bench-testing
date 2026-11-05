"""Cross-branch integration tests. Passing tests do NOT authorize physical work."""
import csv
import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE/"tools"))
from audit_interfaces import (audit_crosswalk,read_json,run_audit,
                              verify_lock_mapping,GATE_PATH,SPLIT_PATH,RUN_PATH)
sys.path.insert(0,str(ROOT/"12_physical_readiness_v0.7"))
from validate_g2 import evaluate
sys.path.insert(0,str(ROOT/"13_q0_data_integrity_v0.8"))
from ebt_q0_data import check_plan,check_metadata,DataError

class ConsolidatedQ0Tests(unittest.TestCase):
    def test_all_source_modules_and_authority_paths_exist(self):
        for file in (
            "09_model_comparison/research_models/physics.py",
            "10_fixture_v0.5/docs/EBT-PDR-005_engineering_design_review.md",
            "11_spatial_transfer_v0.6/spatial_plate.py",
            "12_physical_readiness_v0.7/validate_g2.py",
            "13_q0_data_integrity_v0.8/ebt_q0_data.py",
            "14_q0_integrated_v0.9/protocol/EBT-Q0-009_field_sequence.md",
            "08_project_controls/facility_access_tracker.csv"):
            self.assertTrue((ROOT/file).is_file(),file)

    def test_crosswalk_has_valid_unique_sources(self):
        data=audit_crosswalk()
        self.assertGreaterEqual(len(data),10)
        ids=[r["item_id"] for r in data]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertTrue(all(r["physical_gate"] for r in data))

    def test_intentionally_blank_g2_and_split_and_run_stay_blocked(self):
        gate=read_json(GATE_PATH)
        r=evaluate(gate)
        self.assertTrue(all(x["status"]=="BLOCKED" for x in r["status_by_stage"].values()))
        split=read_json(SPLIT_PATH)
        with self.assertRaises((DataError,ValueError,KeyError,TypeError)):
            check_plan(split)
        with self.assertRaises((DataError,ValueError,KeyError,TypeError)):
            check_metadata(read_json(RUN_PATH))

    def test_expected_audit_status_is_not_permission(self):
        report=run_audit()
        self.assertEqual(report["project_status"],"BLOCKED_NEEDS_PHYSICAL_EVIDENCE")
        self.assertEqual(report["physical_test_observations_count"],0)
        self.assertTrue(report["software_never_grants_fabrication_or_power_authority"])
        self.assertTrue(report["declared_r01_cross_record_discrepancies"])

    def make_test_records(self):
        """In-memory shape test; not a real registration or evidence record."""
        gate=read_json(GATE_PATH)
        g=gate["r01_confirmatory"]
        g["prereg_lock_utc"]="2026-11-05T12:00:00Z"
        g["prereg_document_sha256"]="a"*64
        g["qualification_ids"]=["QUAL-001","QUAL-002"]
        g["calibration_ids"]=["CAL-001"]
        g["reserved_holdout_ids"]=["HOLD-001"]
        plan={"schema_version":"EBT-SPLIT-008","study_kind":"R01",
              "lock_utc":"2026-11-05T13:00:00+01:00",
              "protocol_sha256":"a"*64,
              "external_lock_ref":"https://example.org/unverified-external-lock",
              "role_run_ids":{"QUAL":["QUAL-002","QUAL-001"],
                              "CAL":["CAL-001"],"HOLD":["HOLD-001"]}}
        return gate,plan

    def test_filled_consistent_mapping_is_not_approval(self):
        gate,plan=self.make_test_records()
        self.assertEqual(verify_lock_mapping(gate,plan),[])
        self.assertEqual(evaluate(gate)["status_by_stage"]["powered_q0"]["status"],"BLOCKED")

    def test_cross_record_time_and_hash_mismatch(self):
        gate,plan=self.make_test_records()
        plan["lock_utc"]="2026-11-05T11:00:00Z"
        plan["protocol_sha256"]="b"*64
        issues=verify_lock_mapping(gate,plan)
        self.assertIn("LOCK_INSTANT_MISMATCH",issues)
        self.assertIn("PROTOCOL_SHA256_MISMATCH",issues)

    def test_cross_record_role_mismatch(self):
        gate,plan=self.make_test_records()
        gate["r01_confirmatory"]["reserved_holdout_ids"]=["HOLD-999"]
        issues=verify_lock_mapping(gate,plan)
        self.assertIn("ROLE_PARTITION_MISMATCH_HOLD",issues)

    def test_r01_plan_must_not_be_q0_pilot(self):
        gate,plan=self.make_test_records()
        plan["study_kind"]="Q0_PILOT"
        plan["role_run_ids"]={"Q0_PILOT":["PILOT-001"]}
        self.assertIn("EXPECTED_R01_SPLIT_NOT_Q0_PILOT",verify_lock_mapping(gate,plan))

    def test_10mm_profile_mfr_is_not_4mm_plate_spec(self):
        with (ROOT/"12_physical_readiness_v0.7/evidence/EBT-MEC-007_source_grades.csv").open(newline="",encoding="utf-8") as f:
            data={r["evidence_id"]:r for r in csv.DictReader(f)}
        self.assertEqual(data["GEOM-003"]["value"],"10")
        self.assertEqual(data["GEOM-003"]["grade"],"MANUFACTURER_FAMILY_PROFILE")
        self.assertEqual(data["GEOM-004"]["value"],"4")
        self.assertEqual(data["GEOM-004"]["grade"],"UNVERIFIED_DESIGN_ASSUMPTION")
        self.assertEqual(data["GEOM-003"]["manufacturing_permission"],"NO")

    def test_spatial_synthetic_result_not_physical(self):
        d=read_json(ROOT/"11_spatial_transfer_v0.6/results/conditional_spatial_transfer_v0.6.json")
        self.assertEqual(d["evidence_class"],"SYNTHETIC_ASSUMPTION_DRIVEN_PREDESIGN")
        self.assertTrue(d["power_is_not_authorized_setpoint"])
        self.assertEqual(len(d["scenarios"]),4)
        self.assertLess(d["scenarios"][0]["co_moving_relative_difference"],1e-10)
        self.assertGreater(d["scenarios"][1]["co_moving_relative_difference"],.1)

    def test_old_pilot_and_new_crossover_both_provisional(self):
        content=(HERE/"protocol/EBT-Q0-009_field_sequence.md").read_text(encoding="utf-8")
        for needle in ("12","8","54","PROVISIONAL","HOLD","NOT 20"):
            self.assertIn(needle,content)

    def test_facility_approvals_not_inferred(self):
        with (ROOT/"08_project_controls/facility_access_tracker.csv").open(newline="",encoding="utf-8-sig") as f:
            rows={r["facility_id"]:r for r in csv.DictReader(f)}
        self.assertIn("Canvas invitation",rows["FAC-02"]["email_status"])
        self.assertIn("Independent projects",rows["FAC-03"]["facility_decision"])
        self.assertIn("Awaiting response",rows["FAC-01"]["facility_decision"])

if __name__=="__main__":
    unittest.main()
