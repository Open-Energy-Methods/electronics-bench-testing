import unittest
from dataclasses import replace
import numpy as np
from research_models.physics import TwoNode,solve,energy_residual,rc1
from research_models.boundary import QualRecord,qualify
from research_models.synthetic import make_dataset
from research_models.compare import fit_all,predict,fit_case_only_ablation
from research_models.uncertainty import power_standard_uncertainty,apparent_r_standard_uncertainty,boundary_prediction_sensitivity

class Physics(unittest.TestCase):
    def test_zero_input_and_positive_dynamics(self):
        t=np.arange(0,1001,10.)
        y=solve(TwoNode(),t,np.zeros_like(t))
        self.assertTrue(np.allclose(y,24))
        p=np.full(len(t),3.)
        z=solve(TwoNode(),t,p)
        self.assertTrue(np.all(z[1:,0]>z[1:,1]))

    def test_steady_series_solution(self):
        m=TwoNode(); t=np.arange(0,20001,40.)
        y=solve(m,t,np.full(len(t),3.))
        self.assertAlmostEqual(y[-1,1],24+3*m.r_sa,places=5)
        self.assertAlmostEqual(y[-1,0],24+3*(m.r_ps+m.r_sa),places=5)

    def test_energy_balance(self):
        m=TwoNode(r_pa=8.5)
        t=np.arange(0,1001,1.);qp=np.where(t<600.,3.,0.);qs=np.zeros_like(qp)
        y=solve(m,t,qp,qs)
        self.assertLess(energy_residual(m,t,qp,qs,y),2e-4)

    def test_time_grid_invariance(self):
        m=TwoNode();t=np.arange(0,1001,20.);tf=np.arange(0,1001,5.)
        p=np.where(t<600,4.,0.);pf=np.where(tf<600,4.,0.)
        self.assertTrue(np.allclose(solve(m,t,p),solve(m,tf,pf)[::4],atol=1e-10))

    def test_reject_bad_physics(self):
        t=np.arange(10.)
        with self.assertRaises(ValueError):solve(TwoNode(r_sa=-1),t,np.ones_like(t))
        with self.assertRaises(ValueError):solve(TwoNode(),t,np.ones(5))
        with self.assertRaises(ValueError):rc1(t,np.ones_like(t),0,2)

    def test_boundary_qualified_from_independent_sink_runs(self):
        d=make_dataset()
        f=qualify(d.qualification,"FAN")
        n=qualify(d.qualification,"NAT")
        self.assertEqual(f.n_independent_runs,4)
        self.assertLess(abs(n.mean_k_w-2.8),.12)
        self.assertLess(abs(f.mean_k_w-.95),.12)
        self.assertGreater(f.u_k_w,0)

    def test_package_only_reduces_identifiability(self):
        d=make_dataset();case_only=fit_case_only_ablation(d.train)
        q={name:qualify(d.qualification,name) for name in ("NAT","FAN")}
        full=fit_all(d.train,q)["B2"]
        self.assertGreater(case_only.condition_number,full.condition_number)

    def test_common_uncertainty_not_shrunk_by_repeats(self):
        r=[QualRecord(str(i),"NAT",34,24,4) for i in range(100)]
        estimate=qualify(r,"NAT")
        self.assertGreater(estimate.u_k_w,.02)

    def test_holdout_temperature_is_not_fitting_input(self):
        d=make_dataset()
        q={name:qualify(d.qualification,name) for name in ("NAT","FAN")}
        fits=fit_all(d.train,q)
        e=d.validation[1]
        tampered=replace(e,measured_c=e.measured_c+1000.)
        self.assertTrue(np.array_equal(predict(fits["B3"],e,q),predict(fits["B3"],tampered,q)))

    def test_independent_boundary_required(self):
        d=make_dataset()
        q={name:qualify(d.qualification,name) for name in ("NAT","FAN")}
        fit=fit_all(d.train,q)
        with self.assertRaises(ValueError):predict(fit["B3"],d.validation[1],{"NAT":q["NAT"]})
        self.assertEqual(set(fit),{"B0","B1","B2","B3"})

    def test_uncertainty_propagation(self):
        self.assertAlmostEqual(power_standard_uncertainty(4.0,.5,.01,.02),np.hypot(.5*.01,4*.02))
        self.assertAlmostEqual(apparent_r_standard_uncertainty(34,24,4,.08,.06,.04),
                               np.hypot(.1/4,10*.04/16))
        with self.assertRaises(ValueError):power_standard_uncertainty(4,1,.1,.1,cov_vi=1)

    def test_boundary_sensitivity_to_reference_uncertainty(self):
        d=make_dataset()
        q={name:qualify(d.qualification,name) for name in ("NAT","FAN")}
        f=fit_all(d.train,q)
        u=boundary_prediction_sensitivity(f["B3"],d.validation[1],q["FAN"])
        self.assertGreater(u["max_package_C_per_K_W"],0)
        self.assertGreater(u["one_sigma_package_C"],0)

    def test_static_B0_suppresses_transient_rmse(self):
        from research_models.compare import errors
        d=make_dataset()
        q={name:qualify(d.qualification,name) for name in ("NAT","FAN")}
        p=predict(fit_all(d.train,q)["B0"],d.validation[0],q)
        self.assertIsNone(errors(d.validation[0],p,static=True)["package_transient_rmse_C"])

    def test_b0_has_no_false_transient_prediction(self):
        d=make_dataset()
        q={name:qualify(d.qualification,name) for name in ("NAT","FAN")}
        p=predict(fit_all(d.train,q)["B0"],d.validation[0],q)
        self.assertTrue(np.all(np.isnan(p[:,1])))

if __name__=="__main__":
    unittest.main()
