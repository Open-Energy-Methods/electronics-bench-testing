# M12/M13 — Structural dynamics, acoustics and vibroacoustics
Concept 0.2 | 2026-11-18 | Proposed methods only; no test authorization.

## Scientific progression
V01: passive beam/coupon with defined support condition. CAD and measured
as-built length, section, mass and support; analytical Euler–Bernoulli
reference, FEA eigenfrequency and mesh studies; low-amplitude staff-approved
excitation. Compare first modes; quantify sensor mass, clamp compliance,
orientation, repeat installation and temperature. No machining or excitation
from this document alone.
V02: instrumented impact hammer plus accelerometer(s) and simultaneous
force/response channels, if available and reviewed. Record unprocessed
time histories, force/acceleration units, calibration, anti-aliasing,
window, averaging, impact quality, clipping, double hits, frequency resolution
and coherence. Define H1 accelerance FRF from cross/auto spectra with stated
conjugation; convert to mobility/displacement only with defensible frequency
band and units. Unmeasured tap response is a qualitative spectrum, NOT FRF.
Modal damping by appropriate curve fit or ringdown on isolated modes; report
method and uncertainty. Compare mode shapes using MAC only with matched DOFs,
normalization and sufficient sensor coverage; do not fit HOLD resonances.
V03: cold, passive duct with interchangeable length/end condition; use a
commercial low-level acoustic source (reviewed) and microphone chain.
Predict longitudinal modes with ideal one-dimensional acoustics; assess
end correction, wall/room effects, actual temperature/speed of sound.
Record fixed geometry, source and microphone coordinates, calibration
before/after, noise background, sample rate and frequency response.
Report sound pressure at stated positions and bandwidth. Ordinary workshop
recordings are not free-field sound-power tests; phone/uncalibrated microphone
only qualitative frequency content, never calibrated dB SPL.
V04: guarded commercial fan on separately approved mounting, with tach
reference, synchronized pressure/accelerometer/microphone channels. Track
rotational orders, blade-passing tones, structural resonances and background.
No custom high-speed rotor, deliberate overspeed, imbalance or unsafe faults.
V05: coupled vibroacoustic transfer only after structural and acoustic
sub-models independently qualify. Compare pressure/acceleration phase and
frequency response; distinguish structural-borne and airborne paths.
Flow-induced noise or heated air adds a separate environment and risk review.

## Facility and instrumentation survey
Ask Makerspace/KTH about impact hammer, IEPE or other compatible conditioned
accelerometers, simultaneous sampling DAQ, signal conditioner, shaker or
approved speaker, acoustic measurement microphones, sound calibrator,
tachometer, quiet room and background noise restrictions. Confirm channel
ranges, bandwidth, clock skew, anti-alias filtering, sensor mass and traceable
reference/calibration; scope channels alone do not establish those properties.
Respect noise exposure and adjacent members; safe excitation/level defined by
site. No availability inferred. Portable beam/duct and sensor adapters may
share box; shaker, DAQ, sound reference and stand remain facility equipment.

## V&V acceptance
Before independent HOLD define primary modes/frequency range, comparison
metrics, tolerance justified by intended use, measurement uncertainty,
sample/replicate plan and analysis method. Use disjoint remounts/configurations,
not random FFT bins. Frequency error, FRF complex discrepancy/coherence,
damping, MAC and localized pressure spectra have different interpretations.
A low fitted error does not prove predictive validation. Retain negative
results; update only with CAL; new version requires fresh prospective HOLD.
