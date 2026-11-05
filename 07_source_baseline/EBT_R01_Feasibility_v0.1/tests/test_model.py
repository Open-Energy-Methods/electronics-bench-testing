import numpy as np
from dataclasses import replace
from ebt.model import ThermalSystem, response, single_rc_response, power_schedule, relative_energy_residual


def test_zero_power_stays_at_ambient():
    s=ThermalSystem(); t=np.arange(0,400,2)
    assert np.allclose(response(s,t,np.zeros_like(t)) ,s.t_amb)


def test_steady_state_exact():
    s=ThermalSystem(); t=np.arange(0,8001,5.)
    out=response(s,t,np.full(t.shape,4.))[-1]-s.t_amb
    assert np.allclose(out,s.steady_rise(4.),atol=1e-7)


def test_temperatures_order_and_physics():
    s=ThermalSystem(); t=np.arange(0,1101,5.)
    y=response(s,t,power_schedule(t)); mask=(t>0)&(t<750)
    assert np.all(y[mask,0]>y[mask,1]) and np.all(y[mask,1]>y[mask,2])
    assert y[-1,0]<y[np.argmin(abs(t-745)),0]


def test_time_grid_invariance_at_common_points():
    s=ThermalSystem(); coarse=np.arange(0,1101,5.)
    fine=np.arange(0,1101,1.)
    assert np.max(abs(response(s,coarse,power_schedule(coarse))-response(s,fine,power_schedule(fine))[::5]))<1e-10


def test_conservation_law_approximation():
    s=ThermalSystem(); t=np.arange(0,1201,1.)
    assert relative_energy_residual(s,t,power_schedule(t),response(s,t,power_schedule(t))) <2e-4


def test_single_rc_analytical_steady():
    t=np.arange(0,5001,10.)
    y=single_rc_response(t,np.full(t.shape,4.),2.8,30.)
    assert abs(y[-1]-(24+4*2.8))<1e-8


def test_boundary_change_cools():
    a=ThermalSystem(); b=replace(a,r_sa=0.90)
    t=np.arange(0,1201,5.); p=power_schedule(t)
    assert response(b,t,p)[100,1]<response(a,t,p)[100,1]
