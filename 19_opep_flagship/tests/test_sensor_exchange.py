import json,sys,unittest,math
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/"analysis"))
from sensor_exchange import sensor_replay
class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.r=json.loads((R/"digital_twin/synthetic_sensor_exchange.json").read_text())
    def test_exact_replay(self):
        t,y=sensor_replay(self.r,[(1,310),(1,310)],300)[-1]
        self.assertEqual(t,2)
        self.assertAlmostEqual(y,310-10/math.e)
    def test_reject_outside_domain(self):
        with self.assertRaises(ValueError):sensor_replay(self.r,[(1,500)],300)
    def test_reject_real_unqualified_record(self):
        self.r["evidence_class"]="PHYSICAL"
        with self.assertRaises(ValueError):sensor_replay(self.r,[(1,310)],300)
    def test_reject_false_validation(self):
        self.r["physical_validation"]="VALIDATED"
        with self.assertRaises(ValueError):sensor_replay(self.r,[(1,310)],300)
    def test_reject_nonpositive_step(self):
        with self.assertRaises(ValueError):sensor_replay(self.r,[(0,310)],300)
if __name__=="__main__":unittest.main()
