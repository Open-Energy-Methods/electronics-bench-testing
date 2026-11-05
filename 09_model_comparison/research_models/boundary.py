"""Independent sink-heater effective-boundary qualification and uncertainty.

This is a synthetic qualification algorithm. The estimated K/W quantity is
apparent resistance at a specified sink sensor and heater geometry, not a
universal convective coefficient or an identified physical r_sa in general.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class QualRecord:
    run_id: str
    cooling: str
    sink_plateau_c: float
    ambient_plateau_c: float
    measured_power_w: float

    @property
    def apparent_r(self) -> float:
        if self.measured_power_w <= 0:
            raise ValueError("positive measured heater power required")
        return (self.sink_plateau_c - self.ambient_plateau_c) / self.measured_power_w

@dataclass(frozen=True)
class BoundaryEstimate:
    cooling: str
    mean_k_w: float
    u_k_w: float
    n_independent_runs: int
    method: str = "independent-sink-injection-apparent"


def qualify(records: list[QualRecord], cooling: str, *,
            u_temp_sink_c: float = 0.07, u_temp_ambient_c: float = 0.07,
            relative_power_u: float = 0.01,
            covariance_temp_c2: float = 0.0) -> BoundaryEstimate:
    """Use independent run averages. Common bias does not shrink with run n."""
    data = [x for x in records if x.cooling == cooling]
    if len(data) < 2:
        raise ValueError("at least 2 independent qualification sessions needed")
    if u_temp_sink_c < 0 or u_temp_ambient_c < 0 or relative_power_u < 0:
        raise ValueError("invalid uncertainty")
    var_temp = u_temp_sink_c**2 + u_temp_ambient_c**2 - 2 * covariance_temp_c2
    if var_temp < 0:
        raise ValueError("temperature covariance inconsistent")
    rs = np.asarray([x.apparent_r for x in data], float)
    if not np.all(np.isfinite(rs)) or np.any(rs <= 0):
        raise ValueError("thermal resistance must be positive and finite")
    r_bar = float(np.mean(rs))
    u_type_a = float(np.std(rs, ddof=1) / np.sqrt(len(rs)))
    p_bar = float(np.mean([x.measured_power_w for x in data]))
    u_common = np.sqrt(var_temp / p_bar**2 + (r_bar * relative_power_u)**2)
    return BoundaryEstimate(cooling, r_bar, float(np.hypot(u_type_a, u_common)), len(data))
