"""Offline integrity tests only. No rig operation or lab permission claimed."""
from __future__ import annotations
import copy
import csv
import json
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE))
from validate_g2 import evaluate,evidence_present

def template():
    return json.loads((HERE/"templates/EBT-GATE-007_record_UNFILLED.json").read_text(encoding="utf-8"))

class ReadinessTests(unittest.TestCase):
    def test_unfilled_template_is_blocked_not_authorized(self):
        r=evaluate(template())
        self.assertTrue(r["software_grants_no_access_and_approves_no_power_or_fabrication"])
        self.assertTrue(all(v["status"]=="BLOCKED" for v in r["status_by_stage"].values()))
        self.assertTrue(all(not v["is_authorization"] for v in r["status_by_stage"].values()))

    def test_fabrication_profile_not_equivalent_to_measured_parts(self):
        r=evaluate(template())["status_by_stage"]["fabrication"]
        self.assertIn("fabrication.actual_part_inspection_ref",r["missing_evidence_or_invalid_fields"])

    def test_fake_placeholders_not_evidence(self):
        for word in ("TBD","UNKNOWN","PENDING","placeholder","not granted","DEMO_fake",""):
            # PENDING is not acceptable although case-insensitively.
            self.assertFalse(evidence_present(word),word)

    def test_no_approval_from_self_asserted_complete_record(self):
        d=template()
        for stage in ("fabrication","powered_q0","r01_confirmatory"):
            for name,value in d[stage].items():
                if value is None: d[stage][name]="RECORD_REF_FOR_STRUCTURE_TEST"
        d["fabrication"]["fixture_strategy"]="DIRECT_TO_SINK_CANDIDATE"
        d["r01_confirmatory"].update({
           "prereg_lock_utc":"2026-11-05T12:00:00+01:00",
           "prereg_document_sha256":"a"*64,
           "qualification_ids":["QUAL-001"],"calibration_ids":["CAL-001"],
           "reserved_holdout_ids":["HOLD-001"]
        })
        r=evaluate(d)
        self.assertTrue(all(v["status"]=="DOCUMENTS_PRESENT_HUMAN_REVIEW_REQUIRED"
                            for v in r["status_by_stage"].values()))
        self.assertTrue(all(not v["is_authorization"] for v in r["status_by_stage"].values()))

    def test_invalid_fixture_choice_remains_blocked(self):
        d=template()
        d["fabrication"]["fixture_strategy"]="MACHINED_AND_APPROVED"
        self.assertIn("fabrication.fixture_strategy_validated_selection",
                      evaluate(d)["status_by_stage"]["fabrication"]["missing_evidence_or_invalid_fields"])

    def test_overlapping_prereg_dataset_ids_rejected(self):
        d=template()
        d["r01_confirmatory"].update({
           "qualification_ids":["QUAL-001"],"calibration_ids":["QUAL-001"],
           "reserved_holdout_ids":["HOLD-001"]
        })
        self.assertIn("r01_confirmatory.dataset_partitions_disjoint",
                      evaluate(d)["status_by_stage"]["r01_confirmatory"]["missing_evidence_or_invalid_fields"])

    def test_prereg_requires_timezone_and_sha256(self):
        d=template()
        d["r01_confirmatory"]["prereg_lock_utc"]="2026-11-05T12:00:00"
        d["r01_confirmatory"]["prereg_document_sha256"]="deadbeef"
        missing=evaluate(d)["status_by_stage"]["r01_confirmatory"]["missing_evidence_or_invalid_fields"]
        self.assertIn("r01_confirmatory.prereg_lock_utc_timezone",missing)
        self.assertIn("r01_confirmatory.prereg_document_sha256_hex",missing)

    def test_profile_has_mfr_family_grade_and_not_machining_approval(self):
        with (HERE/"evidence/EBT-MEC-007_source_grades.csv").open(newline="",encoding="utf-8") as f:
            records=list(csv.DictReader(f))
        indexed={r["evidence_id"]:r for r in records}
        self.assertEqual(indexed["GEOM-003"]["value"],"10")
        self.assertEqual(indexed["GEOM-003"]["grade"],"MANUFACTURER_FAMILY_PROFILE")
        self.assertEqual(indexed["GEOM-004"]["grade"],"UNVERIFIED_DESIGN_ASSUMPTION")
        self.assertTrue(all(r["manufacturing_permission"]=="NO" for r in records))
        self.assertEqual(len(records),len(indexed))

    def test_inspection_checklist_not_falsely_completed(self):
        with (HERE/"facility/EBT-G2-007_inspection_register.csv").open(newline="",encoding="utf-8") as f:
            records=list(csv.DictReader(f))
        self.assertGreaterEqual(len(records),18)
        self.assertEqual(len(records),len({r["check_id"] for r in records}))
        self.assertTrue(all(r["status"] in ("NOT_INSPECTED","SOURCE_ONLY_PENDING_PHYSICAL_CHECK") for r in records))
        self.assertTrue(all(not r["actual_evidence_ref"] for r in records))

    def test_no_power_settings_or_approvals_in_template(self):
        text=(HERE/"templates/EBT-GATE-007_record_UNFILLED.json").read_text(encoding="utf-8")
        self.assertNotIn('"approved_power_w"',text)
        self.assertIn('"document_status": "NOT_AUTHORIZED"',text)
        self.assertNotIn("FABRICATION_APPROVED",text)
        

    def test_assumed_plate_mass_and_scaling(self):
        from thermal_mass import AssumedPlate
        a=AssumedPlate().quantities()
        self.assertAlmostEqual(a["mass_kg"],0.108,places=10)
        self.assertAlmostEqual(a["fully_lumped_heat_capacity_j_per_k"],97.2,places=10)
        self.assertEqual(a["evidence_grade"],"ILLUSTRATIVE_ALUMINIUM_ASSUMPTIONS_NOT_REAL_PART_PROPERTIES")
        self.assertAlmostEqual(AssumedPlate(thickness_m=.002).quantities()
                               ["fully_lumped_heat_capacity_j_per_k"],48.6,places=9)
        self.assertTrue(a["not_a_predicted_time_constant"])
        with self.assertRaises(ValueError):
            AssumedPlate(thickness_m=0).quantities()

    def test_stack_drawing_is_explicitly_not_manufacturing_release(self):
        import xml.etree.ElementTree as ET
        p=HERE/"drawings/EBT-MEC-007_stacks_NOT_FOR_MANUFACTURE.svg"
        tree=ET.parse(p)
        root=tree.getroot()
        self.assertTrue(root.tag.endswith("svg"))
        content=p.read_text(encoding="utf-8")
        for token in ("NOT FOR MANUFACTURE","10 mm","4 mm","DIRECT","ADAPTER"):
            self.assertIn(token,content)

if __name__=="__main__":
    unittest.main()
