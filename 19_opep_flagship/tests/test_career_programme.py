"""Structural quality tests for public roadmap; no physical authorization."""
import csv, unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=R/"career"
def rows(p):
    with p.open(encoding="utf-8",newline="") as f:
        items=list(csv.DictReader(f))
    if any(None in x or any(v is None for v in x.values()) for x in items):
        raise ValueError(f"Malformed CSV {p.name}")
    return items
class CareerProgrammeTests(unittest.TestCase):
    def test_roles_map_to_campaigns(self):
        c=rows(D/"OPEP-CAM-004_campaign_registry.csv")
        r=rows(D/"OPEP-JOB-004_public_role_matrix.csv")
        ids={x["id"] for x in c}
        self.assertEqual(len(r),28)
        self.assertEqual(len({x["id"] for x in r}),28)
        self.assertEqual(len(c),12)
        self.assertEqual(len(ids),12)
        for x in r:
            self.assertTrue(set(x["campaign_ids"].split(";")) <= ids)
            self.assertTrue(x["public_source"].startswith("https://"))
    def test_campaigns_resolve_to_existing_modules(self):
        m={x["id"] for x in rows(R/"OPEP-MOD-001_modules.csv")}
        for c in rows(D/"OPEP-CAM-004_campaign_registry.csv"):
            self.assertTrue(set(c["module_ids"].split(";"))<=m)
            self.assertIn(c["state"],("PLANNED","CONDITIONAL","START_AFTER_TASK_APPROVAL"))
    def test_verification_template_is_unfilled(self):
        r=rows(D/"OPEP-DVPR-004_UNFILLED.csv")
        self.assertEqual(len(r),12)
        self.assertEqual({x["campaign"] for x in r},{f"C{i:02}" for i in range(1,13)})
        for x in r:
            self.assertEqual(x["disposition"],"PLANNED")
            for key in ("procedure_ref","acceptance_limit_ref","facility_authorization_ref",
                "as_built_ref","instrument_reference_ref","actual_evidence_ref","uncertainty_ref","review_ref"):
                self.assertEqual(x[key],"")
    def test_machine_inventory_scope_distinct(self):
        r=rows(D/"OPEP-FAC-004_machine_opportunity.csv")
        self.assertEqual(len(r),25)
        self.assertEqual(len({x["id"] for x in r}),25)
        for x in r:
            self.assertTrue(x["limitation"])
            self.assertIn(x["evidence_status"],("PUBLIC_LISTED","PUBLIC_GUIDE_2020","USER_REPORTED_NOT_INSPECTED","SURVEY_REQUIRED"))
        self.assertIn("NOT load calibration",next(x["limitation"] for x in r if x["id"]=="F08"))
    def test_non_nuclear_and_heating_scope(self):
        t=(D/"OPEP-ENG-004_structural_thermal_quality.md").read_text()
        for marker in ("No boiling","radioactive material","No deliberate crack initiation","not an improvised heater"):
            self.assertIn(marker,t)
        t=(D/"OPEP-PROC-004_makerspace_requests.md").read_text()
        self.assertIn("No Stockholm Makerspace board or funding",t)
        self.assertIn("No public student equipment allowance",t)
if __name__=="__main__":unittest.main()
