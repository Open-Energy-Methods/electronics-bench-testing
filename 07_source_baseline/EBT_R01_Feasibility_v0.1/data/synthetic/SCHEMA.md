# Schema for synthetic demo CSV files

Every filename and temperature field is explicitly tagged `synthetic` in order to prevent accidental confusion with physical data.

- `time_s`: elapsed seconds on a 5-second, UTC-independent synthetic test grid.
- `power_W`: programmed ideal dissipated watts for the *interval starting at this time sample*. The last sample is conventionally unused by the state propagator; at t=750 s power steps to zero.
- `synthetic_*_true_C`: precisely simulated model states (not experimentally known truth).
- `synthetic_*_measured_C`: simulated sensor data with independent zero-mean Gaussian noise, sigma=0.15 degrees C, RNG seed 20261105. This is a *design assumption*, not a device specification.
- `model_*_C`: predictions from the calibrated 1RC model (single-case training) or its boundary-aware variant.
- `model_boundary_updated_C`: uses forced cooling `Rsa` supplied from the synthetic scenario configuration, not fitted to held-out package data.

All temperature units are deg C, thermal resistances are K/W, time is s, and device power is W. No real device datasheet, calibration certificate or measurements were used.
