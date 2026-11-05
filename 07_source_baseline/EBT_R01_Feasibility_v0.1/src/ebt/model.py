"""Transparent three-node transient thermal model for *synthetic* feasibility testing.

Nothing in this module is a measurement of a real semiconductor.
Temperatures are in kelvin differences (deg C offsets numerically identical),
power in W, heat capacities J/K and thermal resistances K/W.
"""
from dataclasses import dataclass, replace
import numpy as np
from scipy.linalg import expm

@dataclass(frozen=True)
class ThermalSystem:
    r_jp: float = 0.75    # junction -> observed package, K/W
    r_ps: float = 0.45    # package -> sink, K/W
    r_sa: float = 3.00    # sink -> ambient, K/W
    c_j: float = 0.60    # junction node, J/K
    c_p: float = 9.00    # package node, J/K
    c_s: float = 70.0    # heatsink node, J/K
    t_amb: float = 24.0 # ambient deg C

    def checked(self):
        for x in ('r_jp','r_ps','r_sa','c_j','c_p','c_s'):
            if getattr(self,x)<=0:
                raise ValueError(f'{x} must be > 0')
        return self

    def matrices(self):
        self.checked()
        g1,g2,g3 = 1/self.r_jp,1/self.r_ps,1/self.r_sa
        conductance=np.array([[-g1,g1,0], [g1,-g1-g2,g2], [0,g2,-g2-g3]],dtype=float)
        capacity=np.array([self.c_j,self.c_p,self.c_s])
        A=conductance/capacity[:,None]
        b=np.array([1/self.c_j,0,0],float)
        return A,b

    def steady_rise(self,power):
        return np.array([power*(self.r_jp+self.r_ps+self.r_sa),
                         power*(self.r_ps+self.r_sa), power*self.r_sa])


def response(system: ThermalSystem, time, power, initial=None):
    """Exact zero-order-hold response to power(time[i]) over [time[i],time[i+1]).

    power can be an array sampled at each time or a scalar.  The final
    power sample is conventionally unused because there is no following interval.
    """
    t=np.asarray(time,float)
    if t.ndim!=1 or len(t)<2 or np.any(np.diff(t)<=0):
        raise ValueError('time must be increasing and have >=2 samples')
    P=np.full(t.shape, float(power)) if np.isscalar(power) else np.asarray(power,float)
    if P.shape!=t.shape or not np.all(np.isfinite(P)):
        raise ValueError('power shape/values invalid')
    A,b=system.matrices()
    x=np.zeros(3) if initial is None else np.asarray(initial,float).copy()
    out=np.empty((len(t),3),float)
    out[0]=x
    cache={}
    # steady x = -A^{-1} b * P => no numerical time-stepping ambiguity
    coeff=-np.linalg.solve(A,b)
    for i,dt in enumerate(np.diff(t)):
        step=cache.get(float(dt))
        if step is None:
            step=expm(A*dt)
            cache[float(dt)]=step
        eq=coeff*P[i]
        x=eq+step@(x-eq)
        out[i+1]=x
    return out+system.t_amb


def power_schedule(time,watts=5.0,pulse_end=750.):
    return np.where(np.asarray(time,float)<pulse_end,float(watts),0.)


def single_rc_response(time,power,r_th,c_th,t_amb=24.0,initial_rise=0):
    """Exact first-order lumped response, assuming fixed R and C."""
    t=np.asarray(time,float); P=np.asarray(power,float)
    if r_th<=0 or c_th<=0: raise ValueError('R,C must be positive')
    if P.shape!=t.shape: raise ValueError('power/time mismatch')
    y=np.empty(len(t)); y[0]=initial_rise
    for i,dt in enumerate(np.diff(t)):
        a=np.exp(-dt/(r_th*c_th))
        y[i+1]=a*y[i]+r_th*P[i]*(1-a)
    return y+t_amb


def relative_energy_residual(system,time,power,temperatures):
    """Energy balance using interval integrals; exact for piecewise constant P
    up to trapezoidal integration error in external convection flux."""
    t=np.asarray(time,float); P=np.asarray(power,float)
    x=np.asarray(temperatures,float)-system.t_amb
    capacity=np.array([system.c_j,system.c_p,system.c_s])
    total_energy=x@capacity
    gain=np.diff(t)*P[:-1]
    outward=np.diff(t)/system.r_sa*(x[:-1,2]+x[1:,2])/2
    delta=np.diff(total_energy)
    denom=max(float(np.sum(np.abs(gain))),1e-12)
    return float(np.sum(np.abs(delta-(gain-outward)))/denom)
