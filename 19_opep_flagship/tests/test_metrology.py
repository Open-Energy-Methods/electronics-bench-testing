"""Synthetic unit tests only."""
import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"analysis"))
from metrology import interval_screen,pooled_repeatability,first_pass_yield
class TestScreening(unittest.TestCase):
    def test_inside(self):self.assertEqual(interval_screen(10,.02,9.9,10.1),"INTERVAL_INSIDE")
    def test_overlap(self):self.assertEqual(interval_screen(10.09,.03,9.9,10.1),"INDETERMINATE_OVERLAP")
    def test_outside(self):self.assertEqual(interval_screen(10.2,.02,9.9,10.1),"INTERVAL_OUTSIDE")
    def test_invalid_uncertainty(self):
        with self.assertRaises(ValueError):interval_screen(10,-.1,9.9,10.1)
    def test_repeatability(self):
        r=pooled_repeatability([("A",9),("A",11),("B",19),("B",21)])
        self.assertAlmostEqual(r["within_artifact_sd"],2**.5)
        self.assertEqual(r["degrees_of_freedom"],2)
        self.assertEqual(r["artifact_count"],2)
    def test_single_reading_rejected(self):
        with self.assertRaises(ValueError):pooled_repeatability([("A",10),("B",20),("B",21)])
    def test_yield(self):self.assertAlmostEqual(first_pass_yield(4,5),.8)
    def test_invalid_counts(self):
        with self.assertRaises(ValueError):first_pass_yield(5,4)
if __name__=="__main__":unittest.main()
