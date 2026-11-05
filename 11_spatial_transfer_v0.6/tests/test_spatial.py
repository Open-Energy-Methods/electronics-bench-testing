"""Numerical unit checks, not physical verification or safe-to-operate tests."""
import unittest
import numpy as np
from spatial_plate import Plate,Source,loss_field,source_map,solve_plate,sample
from run_sensitivity import make_results

class SpatialTests(unittest.TestCase):
    def setUp(self):self.p=Plate(cells=21)

    def test_source_energy(self):
        for f in (1.,.8):
            q=source_map(self.p,Source(x_m=-.025,plate_fraction=f))
            self.assertAlmostEqual(q.sum(),f,places=12)
            self.assertGreaterEqual(q.min(),0)

    def test_steady_energy_balance(self):
        src=Source(x_m=-.025,plate_fraction=.8)
        g=loss_field(self.p,40,100)
        t=solve_plate(self.p,src,g)
        self.assertAlmostEqual(float(np.sum(g*t)*(self.p.side_m/self.p.cells)**2),.8,places=9)
        self.assertGreater(t.min(),0)

    def test_symmetric_mirror(self):
        g=loss_field(self.p,60)
        a=solve_plate(self.p,Source(x_m=-.025),g)
        b=solve_plate(self.p,Source(x_m=.025),g)
        self.assertTrue(np.allclose(a,b[::-1,:],rtol=0,atol=1e-12))
        self.assertAlmostEqual(sample(self.p,a,-.025,-.017),sample(self.p,b,.025,-.017),places=10)

    def test_bypass_linearity(self):
        g=loss_field(self.p,40,100)
        a=solve_plate(self.p,Source(x_m=-.025),g)
        b=solve_plate(self.p,Source(x_m=-.025,plate_fraction=.8),g)
        self.assertTrue(np.allclose(b,.8*a,rtol=1e-10))

    def test_invalid_input(self):
        g=loss_field(self.p,60)
        with self.assertRaises(ValueError):solve_plate(self.p,Source(x_m=.05),g)
        with self.assertRaises(ValueError):solve_plate(self.p,Source(x_m=0,plate_fraction=1.2),g)
        with self.assertRaises(ValueError):solve_plate(self.p,Source(x_m=0),-g)
        with self.assertRaises(ValueError):sample(self.p,np.zeros((21,21)),.05,0)
        with self.assertRaises(ValueError):Plate(cells=8).validate()

    def test_grid_refinement(self):
        values=[]
        for n in (21,41,61):
            p=Plate(cells=n)
            t=solve_plate(p,Source(x_m=-.025),loss_field(p,40,100))
            values.append(sample(p,t,-.025,-.017))
        self.assertLess(abs(values[1]-values[2])/abs(values[2]),.015)
        self.assertLess(abs(values[0]-values[2])/abs(values[2]),.04)

    def test_scenarios_and_data_authenticity(self):
        d=make_results()
        self.assertEqual(d["evidence_class"],"SYNTHETIC_ASSUMPTION_DRIVEN_PREDESIGN")
        self.assertTrue(d["power_is_not_authorized_setpoint"])
        self.assertEqual(len(d["scenarios"]),4)
        self.assertLess(d["scenarios"][0]["co_moving_relative_difference"],1e-10)
        self.assertGreater(d["scenarios"][0]["fixed_A_sensor_source_swap_relative_difference"],.01)
        self.assertGreater(d["scenarios"][1]["co_moving_relative_difference"],.01)


    def test_committed_results_are_reproducible(self):
        import json
        from pathlib import Path
        stored=json.loads((Path(__file__).resolve().parents[1]/
                           "results/conditional_spatial_transfer_v0.6.json").read_text(encoding="utf-8"))
        recomputed=make_results()
        self.assertEqual(stored["evidence_class"],recomputed["evidence_class"])
        self.assertEqual(stored["not_modelled"],recomputed["not_modelled"])
        self.assertEqual(len(stored["scenarios"]),len(recomputed["scenarios"]))
        for saved,actual in zip(stored["scenarios"],recomputed["scenarios"]):
            self.assertEqual(saved["scenario"],actual["scenario"])
            for k in ("r_app_A_to_A_k_w","r_app_B_to_B_k_w","r_app_B_to_A_k_w",
                      "co_moving_relative_difference",
                      "fixed_A_sensor_source_swap_relative_difference",
                      "maximum_energy_relative_residual"):
                self.assertAlmostEqual(saved[k],actual[k],delta=1e-7)

if __name__=="__main__":unittest.main()
