"""Q0-010 catalog/actual-part separation and blank physical intake tests."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    return json.loads((ROOT/"inspection"/name).read_text(encoding="utf-8"))
class RealReceiptIntakeTests(unittest.TestCase):
    def test_components_not_marked_physically_inspected(self):
        d=load("EBT-Q0-010_unfilled_component_receipt.json")
        self.assertEqual(d["actual_measurement_count"],0)
        self.assertTrue(d["manufacturer_values_are_not_observations"])
        self.assertEqual(d["evidence_class"],"UNFILLED_ACTUAL_RECEIPT_REQUIRED")
        self.assertEqual(len(d["parts"]),3)
        for p in d["parts"]:
            self.assertEqual(p["disposition"],"NOT_INSPECTED")
            self.assertIsNone(p["receipt_ref"])
            self.assertIsNone(p["photo_sha256"])
            self.assertIsNone(p["reviewer"])
    def test_catalog_geometries_never_measured_in_template(self):
        sink=load("EBT-Q0-010_unfilled_component_receipt.json")["parts"][0]
        self.assertEqual(sink["nominal_mm"]["base"],10)
        self.assertEqual(sink["manufacturer_dimensional_tolerances"],"NOT_PROVIDED")
        self.assertTrue(all(v is None for v in sink["measured_mm"].values()))
        self.assertIsNone(sink["fastening_permission_ref"])
    def test_heater_rating_is_conditional_not_setpoint(self):
        d=load("EBT-Q0-010_unfilled_component_receipt.json")
        self.assertEqual({p["id"] for p in d["parts"]},{"HSK-001","HEAT-001","HEAT-002"})
        for p in d["parts"][1:]:
            self.assertEqual(p["nominal_resistance_ohm"],10)
            self.assertEqual(p["tolerance_percent"],1)
            self.assertEqual(p["case_rating_w_at_25c"],20)
            self.assertEqual(p["free_air_example_w"],2.8)
            self.assertIsNone(p["measured_resistance_ohm"])
            self.assertIsNone(p["reference_evidence_ref"])
    def test_instrument_evidence_all_absent(self):
        d=load("EBT-Q0-010_unfilled_instrument_inventory.json")
        self.assertEqual(d["status"] if "status" in d else d["evidence_class"],"UNFILLED_LAB_INSPECTION_REQUIRED")
        self.assertIsNone(d["site_permission_ref"])
        self.assertEqual(len(d["instruments"]),6)
        for i in d["instruments"]:
            self.assertIsNone(i["actual_model"])
            self.assertIsNone(i["serial"])
            self.assertIsNone(i["calibration_or_reference_ref"])
if __name__=="__main__":
    unittest.main()
