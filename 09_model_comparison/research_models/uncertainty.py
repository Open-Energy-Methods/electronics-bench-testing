"""Local sensitivity and measurement variance propagation (synthetic assumptions).

No full confidence interval coverage is claimed. Only specified Type B terms
are propagated; model discrepancy and parameter covariance remain separate.
"""
from __future__ import annotations
import numpy as np
from .physics import TwoNode, solve
from .compare import Experiment, ModelFit
from .boundary import BoundaryEstimate


def power_standard_uncertainty(v: float, i: float, u_v: float, u_i: float, cov_vi: float = 0.) -> float:
    if u_v < 0 or u_i < 0 or abs(cov_vi) > u_v * u_i + 1e-15:
        raise ValueError("invalid V-I standard uncertainty/covariance")
    variance = (i*u_v)**2 + (v*u_i)**2 + 2*v*i*cov_vi
    if variance < 0:
        raise ValueError("negative power variance")
    return float(np.sqrt(variance))


def apparent_r_standard_uncertainty(ts: float, ta: float, p: float, u_ts: float, u_ta: float,
                                    u_p: float, cov_t: float = 0.) -> float:
    if p <= 0 or any(x < 0 for x in (u_ts,u_ta,u_p)) or abs(cov_t) > u_ts*u_ta+1e-15:
        raise ValueError("invalid thermal boundary uncertainty inputs")
    variance = (u_ts**2+u_ta**2-2*cov_t)/p**2 + ((ts-ta)*u_p/p**2)**2
    return float(np.sqrt(max(variance, 0.)))


def boundary_prediction_sensitivity(fit: ModelFit, e: Experiment, b: BoundaryEstimate,
                                    rel_step: float = 1e-3) -> dict[str,float]:
    """Local perturbation only; excludes fit covariance and structural discrepancy."""
    if fit.name != "B3":
        raise ValueError("B3 only")
    if rel_step <= 0 or rel_step >= .5:
        raise ValueError("step must be positive small")
    rps, cp, cs = fit.parameters
    yplus = solve(TwoNode(r_ps=rps,r_sa=b.mean_k_w*(1+rel_step),c_p=cp,c_s=cs),
                  e.time_s,e.power_w,ambient_c=e.ambient_c)
    yminus = solve(TwoNode(r_ps=rps,r_sa=b.mean_k_w*(1-rel_step),c_p=cp,c_s=cs),
                   e.time_s,e.power_w,ambient_c=e.ambient_c)
    dydr = (yplus-yminus)/(2*rel_step*b.mean_k_w)
    return {"max_package_C_per_K_W":float(np.max(np.abs(dydr[:,0]))),
            "max_sink_C_per_K_W":float(np.max(np.abs(dydr[:,1]))),
            "one_sigma_package_C":float(np.max(np.abs(dydr[:,0]))*b.u_k_w),
            "one_sigma_sink_C":float(np.max(np.abs(dydr[:,1]))*b.u_k_w)}
