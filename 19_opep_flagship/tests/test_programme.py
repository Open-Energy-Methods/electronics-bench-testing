"""Structural requirements and module checks. Does not establish rig acceptance."""
import csv,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def rows(path):
    with (ROOT/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
class TestProgramme(unittest.TestCase):
    def test_modules_unique_and_not_accepted(self):
        r=rows("19_opep_flagship/OPEP-MOD-001_modules.csv")
        self.assertEqual({x["id"] for x in r},{f"M{i:02d}" for i in range(1,16)})
        self.assertEqual(len(r),15)
        self.assertTrue(all(x["state"] in ("PLANNED","CONDITIONAL") for x in r))
    def test_requirements_unique_and_open(self):
        r=rows("18_rig_engineering/verification/RIG-REQ-001_requirements.csv")
        self.assertEqual(len(r),28)
        self.assertEqual(len({x["requirement_id"] for x in r}),28)
        self.assertTrue(all(x["status"]=="OPEN" for x in r))
    def test_risk_references_resolve(self):
        ids={x["requirement_id"] for x in rows("18_rig_engineering/verification/RIG-REQ-001_requirements.csv")}
        hazards=rows("18_rig_engineering/safety/RIG-HAZ-001_hazard_register.csv")
        self.assertEqual(len(hazards),14)
        for h in hazards:
            self.assertTrue(set(h["req_ids"].split(";"))<=ids)
            self.assertEqual(h["state"],"OPEN")
    def test_standards_not_certification(self):
        r=rows("19_opep_flagship/OPEP-STD-001_extensions.csv")
        self.assertEqual(len(r),16)
        self.assertTrue(all(x["disposition"]=="PUBLIC_SCOPE_CHECKED" for x in r))
    def test_no_real_inspections_in_example(self):
        r=rows("19_opep_flagship/templates/first_article_UNFILLED.csv")
        self.assertEqual(len(r),0)
if __name__=="__main__":unittest.main()
