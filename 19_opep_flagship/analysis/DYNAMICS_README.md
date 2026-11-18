# Analytical dynamics verification examples
All examples are synthetic and independent of actual rig hardware.
- Uniform beam reference for modal FEA: ideal cantilever or simply supported.
  Actual joint compliance, shear, rotary inertia, accelerometer loading and
  dimensions may invalidate the idealization. No predicted actual frequency.
- Linear SDOF complex accelerance benchmark for harmonic response; no assumed
  constant damping for all physical modes.
- Ideal lossless duct modes for pressure-acoustic solver checks; no end
  corrections or thermoviscous loss, uniform sound speed, no mean flow.
- SPL conversion requires calibrated pressure in Pa RMS; no raw microphone
  counts or uncalibrated phone audio. No IEC meter conformity or sound power.
- Exact first-order zero-order-hold sensor replay; independent sensor step
  tests needed before importing a physical time constant into ThermoTwin-F.
- MAC compares identical measured and calculated DOFs; not a frequency or
  damping comparison.
Run `python -m unittest discover -s 19_opep_flagship/tests -p 'test_*.py' -v`.
The next implementation should add measured multichannel FRF processing,
timebase verification and model-parameter provenance with real references.
