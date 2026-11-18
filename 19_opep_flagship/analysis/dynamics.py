"""Analytical reference models, not physical rig validation.
SI units exclusively. No operating limits or safety approval.
"""
from math import exp, pi, sqrt, log10, isfinite
from cmath import exp as cexp

def _positive(*values):
    if any(not isfinite(v) or v <= 0 for v in values):
        raise ValueError("positive finite values required")

def beam_frequency(length_m, elastic_pa, inertia_m4, density_kg_m3,
                   area_m2, mode=1, support="cantilever"):
    """Uniform undamped slender Euler-Bernoulli beam, ideal end conditions."""
    _positive(length_m, elastic_pa, inertia_m4, density_kg_m3, area_m2)
    if type(mode) is not int or mode < 1:
        raise ValueError("positive integer mode required")
    if support == "cantilever":
        roots = (1.875104068711961, 4.694091132974175, 7.854757438237613,
                 10.99554073487547, 14.13716839104647)
        if mode > len(roots):
            raise ValueError("reference limited to five modes")
        beta = roots[mode-1]
    elif support == "simply_supported":
        beta = mode*pi
    else:
        raise ValueError("unsupported ideal boundary")
    return beta**2/(2*pi*length_m**2)*sqrt(elastic_pa*inertia_m4/(density_kg_m3*area_m2))

def sdof_accelerance(frequency_hz, mass_kg, stiffness_n_m, damping_ns_m):
    """Complex A/F (m/s² per N), convention exp(+i omega t)."""
    _positive(mass_kg, stiffness_n_m)
    if not isfinite(frequency_hz) or frequency_hz < 0 or not isfinite(damping_ns_m) or damping_ns_m < 0:
        raise ValueError("invalid frequency or damping")
    w = 2*pi*frequency_hz
    z = stiffness_n_m-mass_kg*w*w+1j*w*damping_ns_m
    if z == 0:
        raise ValueError("undamped resonance singularity")
    return -w*w/z

def duct_mode(length_m, sound_speed_m_s, mode=1, ends="open_open"):
    """Ideal lossless 1D uniform duct, no end correction or flow."""
    _positive(length_m,sound_speed_m_s)
    if type(mode) is not int or mode < 1:
        raise ValueError("positive integer mode required")
    if ends in ("open_open","closed_closed"):
        return mode*sound_speed_m_s/(2*length_m)
    if ends=="open_closed":
        return (2*mode-1)*sound_speed_m_s/(4*length_m)
    raise ValueError("unsupported acoustic boundary")

def sound_pressure_level(rms_pa, reference_pa=20e-6):
    """Unweighted SPL for calibrated RMS sound pressure only; not sound power."""
    _positive(rms_pa, reference_pa)
    return 20*log10(rms_pa/reference_pa)

def first_order_sensor(initial, held_input, tau_s, dt_s):
    """Exact zero-order-hold solution of tau dy/dt + y = u."""
    _positive(tau_s)
    if any(not isfinite(v) for v in (initial,held_input,dt_s)) or dt_s<0:
        raise ValueError("invalid input or elapsed time")
    return held_input+(initial-held_input)*exp(-dt_s/tau_s)

def modal_assurance(a,b):
    """MAC for matched complex mode DOFs, no mode selection or weighting."""
    if len(a)!=len(b) or not a:
        raise ValueError("matched nonempty DOFs required")
    a,b=[complex(x) for x in a],[complex(x) for x in b]
    if any(not isfinite(x.real) or not isfinite(x.imag) for x in a+b):
        raise ValueError("finite modes required")
    aa,bb=sum(abs(x)**2 for x in a),sum(abs(x)**2 for x in b)
    if aa==0 or bb==0:
        raise ValueError("zero mode norm")
    return min(1.0,abs(sum(x.conjugate()*y for x,y in zip(a,b)))**2/(aa*bb))
