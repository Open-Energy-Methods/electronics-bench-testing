"""Structural regression tests: KTH Canvas source is not machine permission."""
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class G2CanvasAccessTests(unittest.TestCase):
    def setUp(self):
        self.r=json.loads((ROOT/"EBT-G2-012_access_record_UNFILLED.json").read_text(encoding="utf-8"))
    def test_course_access_not_equated_with_machine_access(self):
        self.assertTrue(self.r["course_access_confirmed_by_browser_read"])
        self.assertFalse(self.r["machining_approval"])
        self.assertFalse(self.r["powered_test_approval"])
        self.assertIsNone(self.r["introduction_attended_evidence_ref"])
    def test_no_booking_asserted_from_schedule(self):
        self.assertEqual(len(self.r["session_listing_not_availability"]),2)
        self.assertTrue(all(not s["booking_confirmed"] for s in self.r["session_listing_not_availability"]))
        self.assertIsNone(self.r["introduction_booking_ref"])
    def test_all_official_safety_activities_are_unverified(self):
        for key in ("post_introduction_quiz_completion_ref","safety_acknowledgement_submission_ref",
                    "project_based_eligibility_confirmed_by_staff"):
            self.assertIsNone(self.r[key])
        for key in ("machine_specific_risk_assessment_refs",
                    "machine_specific_practical_introduction_refs",
                    "task_specific_machine_authorization_refs"):
            self.assertFalse(self.r[key])
    def test_no_machining_operating_instructions_released(self):
        s=(ROOT/"EBT-G2-012_project_brief.md").read_text(encoding="utf-8")
        self.assertIn("unpowered",s.lower())
        self.assertIn("No machining drawing",s)
        self.assertIn("no energizing power resistors",s)
    def test_course_document_requires_canvas_appointment_and_machine_training(self):
        s=(ROOT/"EBT-G2-012_workshop_onboarding.md").read_text(encoding="utf-8")
        for token in ("Find Appointment","post-introduction quiz","safety acknowledgement",
                      "risk assessment PDF","practical introduction","NOT"):
            self.assertIn(token,s)
if __name__=="__main__": unittest.main()
