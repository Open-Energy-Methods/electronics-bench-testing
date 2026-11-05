"""Exact-ZOH passive 2-node heater/sink energy-balance model.

All values and inputs are synthetic and not device ratings or approved setpoints.
Model temperatures are accessible package/sink nodes, NOT semiconductor junction.
Internal package-to-ambient leak is optional to test model inadequacy.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.linalg import expm

@dataclass(frozen=True)
class TwoNode:
    r_ps: float = 0.48
    r_sa: float = 2.8
    c_p: float = 12.0
    c_s: float = 65.0
    r_pa: float | None = None

    def check(self) -> None:
        for label in ("r_ps", "r_sa", "c_p", "c_s"):
            value = getattr(self, label)
            if not np.isfinite(value) or value <= 0:
                raise ValueError(f"{label} must be finite, positive")
        if self.r_pa is not None and (not np.isfinite(self.r_pa) or self.r_pa <= 0):
            raise ValueError("r_pa must be finite, positive or None")


def matrices(m: TwoNode) -> tuple[np.ndarray, np.ndarray]:
    m.check()
    gps, gsa = 1 / m.r_ps, 1 / m.r_sa
    gpa = 0 if m.r_pa is None else 1 / m.r_pa
    a = np.array([[-(gps + gpa) / m.c_p, gps / m.c_p],
                  [gps / m.c_s, -(gps + gsa) / m.c_s]], float)
    b = np.array([[1 / m.c_p, 0], [0, 1 / m.c_s]], float)
    return a, b


def solve(m: TwoNode, time_s: np.ndarray, package_w: np.ndarray,
          sink_w: np.ndarray | None = None, ambient_c: float = 24) -> np.ndarray:
    """Return [Tpackage,T_sink] with zero-initial rise and constant ambient.

    Inputs are zero-order-held on [t[i],t[i+1]); t[-1] power is ignored.
    Any boundary change must be represented as a separate fixed-boundary run.
    """
    t = np.asarray(time_s, float)
    q_p = np.asarray(package_w, float)
    q_s = np.zeros_like(q_p) if sink_w is None else np.asarray(sink_w, float)
    if t.ndim != 1 or len(t) < 2 or not np.all(np.isfinite(t)) or np.any(np.diff(t) <= 0):
        raise ValueError("time must be finite and strictly increasing")
    if q_p.shape != t.shape or q_s.shape != t.shape or not np.all(np.isfinite(q_p)) or not np.all(np.isfinite(q_s)):
        raise ValueError("inputs must be finite arrays with time shape")
    if not np.isfinite(ambient_c):
        raise ValueError("ambient must be finite")
    a, b = matrices(m)
    equilibrium = -np.linalg.solve(a, b)
    transitions = {}
    x = np.zeros(2)
    out = np.empty((len(t), 2), float)
    out[0] = ambient_c
    for i, dt in enumerate(np.diff(t)):
        if dt not in transitions:
            transitions[dt] = expm(a * dt)
        q = np.array([q_p[i], q_s[i]])
        eq = equilibrium @ q
        x = eq + transitions[dt] @ (x - eq)
        out[i + 1] = ambient_c + x
    return out


def rc1(time_s: np.ndarray, power_w: np.ndarray, r_th: float, c_th: float,
        ambient_c: float = 24) -> np.ndarray:
    t = np.asarray(time_s, float)
    p = np.asarray(power_w, float)
    if r_th <= 0 or c_th <= 0 or not np.isfinite(r_th + c_th):
        raise ValueError("R and C positive finite")
    if len(t) < 2 or p.shape != t.shape or np.any(np.diff(t) <= 0):
        raise ValueError("bad time/input")
    out = np.zeros(len(t))
    for i, dt in enumerate(np.diff(t)):
        decay = np.exp(-dt / (r_th * c_th))
        out[i+1] = out[i] * decay + r_th * p[i] * (1-decay)
    return out + ambient_c


def total_energy_j(m: TwoNode, temperature_c: np.ndarray, ambient_c: float) -> np.ndarray:
    y = np.asarray(temperature_c) - ambient_c
    return m.c_p * y[:, 0] + m.c_s * y[:, 1]


def energy_residual(m: TwoNode, t: np.ndarray, qp: np.ndarray, qs: np.ndarray,
                    temps: np.ndarray, ambient_c: float = 24) -> float:
    """Relative integrated law; trapezoid approximates heat rejection."""
    energy = total_energy_j(m, temps, ambient_c)
    rise = temps - ambient_c
    q_out = rise[:, 1] / m.r_sa + (0 if m.r_pa is None else rise[:, 0] / m.r_pa)
    dt = np.diff(t)
    residual = np.diff(energy) - (qp[:-1] + qs[:-1]) * dt + 0.5 * (q_out[:-1] + q_out[1:]) * dt
    return float(np.sum(np.abs(residual)) / max(1e-12, np.sum(np.abs((qp[:-1] + qs[:-1]) * dt))))
