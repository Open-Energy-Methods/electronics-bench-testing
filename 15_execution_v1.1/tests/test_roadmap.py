"""Adversarial plan-integrity tests; no physical authorization ever given."""
import copy, json, sys, unittest
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE/"tools"))
from check_roadmap import audit,read_plan,validate_dependencies,validate_gates,SNAP

class RoadmapChecks(unittest.TestCase):
    def setUp(self):
        self.rows=read_plan()
        self.gates=json.loads(SNAP.read_text(encoding="utf-8"))
    def test_real_plan_has_all_gates_and_files(self):
        x=audit()
        self.assertEqual(x["gate_count"],7)
        self.assertGreaterEqual(x["task_count"],30)
        self.assertFalse(x["physical_permission_granted_by_software"])
    def test_duplicate_task_rejected(self):
        rows=copy.deepcopy(self.rows)+[copy.deepcopy(self.rows[0])]
        with self.assertRaisesRegex(ValueError,"Duplicate task"):
            validate_dependencies(rows)
    def test_unknown_dependency_rejected(self):
        rows=copy.deepcopy(self.rows)
        rows[2]["depends_on"]="E-999"
        with self.assertRaisesRegex(ValueError,"Unknown prerequisite"):
            validate_dependencies(rows)
    def test_cycle_rejected(self):
        rows=copy.deepcopy(self.rows)
        rows[0]["depends_on"]="E-002"
        with self.assertRaisesRegex(ValueError,"cycle"):
            validate_dependencies(rows)
    def test_no_false_physical_completed_task(self):
        rows=copy.deepcopy(self.rows)
        rows[14]["status"]="COMPLETE"
        with self.assertRaisesRegex(ValueError,"cannot award physical completion"):
            validate_dependencies(rows)
    def test_empty_acceptance_rejected(self):
        rows=copy.deepcopy(self.rows)
        rows[2]["acceptance_evidence"]=""
        with self.assertRaisesRegex(ValueError,"Incomplete acceptance"):
            validate_dependencies(rows)
    def test_explicit_physical_approval_flag_rejected(self):
        g=copy.deepcopy(self.gates)
        g["powered_q0_site_permission_confirmed"]=True
        with self.assertRaisesRegex(ValueError,"must be false"):
            validate_gates(g)
    def test_false_gate_approval_rejected(self):
        g=copy.deepcopy(self.gates)
        g["gate_status"]["G2"]["status"]="APPROVED"
        with self.assertRaisesRegex(ValueError,"False physical gate"):
            validate_gates(g)
    def test_physical_safety_not_inferred_from_docs(self):
        r=audit()
        self.assertEqual(r["status"],"PLAN_STRUCTURALLY_CONSISTENT_PHYSICAL_GATES_BLOCKED")
        self.assertFalse(r["physical_data_validated_by_software"])
    def test_candidate_pilot_and_54_r01_not_executed(self):
        p=(HERE/"plans/EBT-MET-011_metrology_and_pilot.md").read_text()
        r=(HERE/"plans/EBT-R01-011_design_and_acquisition.md").read_text()
        self.assertIn("NOT cumulative",p)
        self.assertIn("54 proposed",r)
        self.assertIn("Q0_PILOT",r)
        self.assertIn("HOLD",r)
    def test_cooling_factor_collision_recorded(self):
        p=(HERE/"plans/EBT-R01-011_design_and_acquisition.md").read_text()
        self.assertIn("NAT/PASS/FORCED",p)
        self.assertIn("OTHER_DOCUMENTED",p)
        self.assertIn("heater position",p)
    def test_no_live_power_level_assigned(self):
        p=(HERE/"plans/EBT-HW-011_facility_hardware_release.md").read_text()
        self.assertIn("No fixed wattage",p)
        self.assertIn("HOLD",p)
if __name__=="__main__":unittest.main()
