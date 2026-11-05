# EBT v0.6 — Spatial boundary-transfer sensitivity

**Status: CONDITIONAL SYNTHETIC PREDESIGN. No real heatsink measured, no calibration, no manufacturing approval, no energized work authorization.** This supplements v0.5 without changing EBT-PMP-001 v1.0 or replacing B0–B3.

- spatial_plate.py: numerical steady finite-volume plate model (not a real finned heatsink).
- run_sensitivity.py: normalized 1 W hypothetical source/position, boundary asymmetry, bypass and footprint comparisons.
- tests/test_spatial.py: seven physics/numerical integrity checks.
- docs/EBT-SPAT-006_review.md: method, numbers, design decisions and transferability gates.
- results/conditional_spatial_transfer_v0.6.json: synthetic-only precomputed summary, reproducible via runner.

Execute from this directory after installing requirements: python -m unittest discover -s tests -p 'test_*.py' -v; python run_sensitivity.py. All numerical inputs are assumptions, not measured component properties.
