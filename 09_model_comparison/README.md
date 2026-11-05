# EBT-R01 model-comparison and boundary-transfer audit v0.4

**Computational feasibility / synthetic-only.** Not physical device measurements, semiconductor junction temperatures, qualified calibrations, laboratory authorization, validated novelty or experimental performance.

## Execute

From this subdirectory (Python 3.11+, NumPy, SciPy and Matplotlib):

```sh
python -m pip install -r ../07_source_baseline/EBT_R01_Feasibility_v0.1/requirements.txt
python -m unittest discover -s tests -p 'test_*.py' -v
python -m research_models.run --out results/synthetic_model_comparison_v0.4.json
python -m scripts.robustness_scan
python -m scripts.plot_comparison
```

The model explicitly separates:
- **TRAIN:** two natural-cooling surface/sink thermal traces with measured synthetic power
- **QUAL:** four disjoint sink-only heat-injection runs per cooling boundary
- **HOLDOUT:** four distinct mounting/cooling events, never used by the fit or qualification routine

B0 is static only; B1 fits a case-only one-RC model; B2 fits fixed-boundary two-node case/sink RC; B3 uses independently qualified natural/forced apparent sink boundary input and fits a three-parameter two-node RC. A case-only B2 ablation audits local Jacobian conditioning. Synthetic counterexamples include package-to-air bypass and a deliberately mismatched boundary qualification fixture.

**Important:** Although B3 can be predictive when the boundary is transferable, its extra qualification data incur a real measurement cost. Apparent sink-to-air resistance is **not** an identified convection coefficient. The report describes model error, sensor bandwidth, power metrology, observation leakage, uncertain boundary transport and required Q0 evidence.

[Read the critical model and boundary-method report](docs/EBT-R01_model_comparison_and_boundary_qualification_v0.4.md).

All input powers, heat capacities, resistances, noise and operating times are *assumed synthetic values*, not an approved powered test envelope. The previous v0.1 source baseline remains intact.

## Generated numerical output snapshots checked into version control

- [`results/synthetic_model_comparison_v0.4.json`](results/synthetic_model_comparison_v0.4.json) and [`results/synthetic_noise_seed_robustness_v0.4.json`](results/synthetic_noise_seed_robustness_v0.4.json)
- [`figures/comparison_holdouts.png`](figures/comparison_holdouts.png) and [`figures/boundary_failure_modes.png`](figures/boundary_failure_modes.png)
- [Generation provenance and integrity hashes](GENERATED_OUTPUT_PROVENANCE.md), [`SOURCE_OUTPUT_SHA256.json`](SOURCE_OUTPUT_SHA256.json)

**These are stored synthetic outputs**, regenerated data can differ at floating-point or plot-byte level between environments. Do not present them as measured validation.
