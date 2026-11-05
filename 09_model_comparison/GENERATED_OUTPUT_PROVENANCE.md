# v0.4 checked numerical output snapshot (not measurements)

This directory adds the **already-generated v0.4 synthetic JSON metrics and PNG plots** to version control; it does **not** add any physical experiment. Source code generating the data remains `09_model_comparison/research_models/run.py` and scripts under `scripts/`.

- All outputs tagged `SYNTHETIC_ONLY_NO_PHYSICAL_MEASUREMENTS` (except plots carrying matching synthetic captions).
- These snapshots were generated in the original 2026-11-05 authoring environment (Python 3.13 / installed numerical stack); cross-environment floating-point differences mean byte-for-byte regenerated data or matplotlib PNGs need not match. Numerical tests use scientifically stated tolerances.
- `SOURCE_OUTPUT_SHA256.json` verifies the exact *archived output snapshot*, not reproducibility after rerunning code with different library versions.
- **No new numerical inference is made by committing the files.** The v0.4 report remains the scientific source for interpretation and its limitations.
