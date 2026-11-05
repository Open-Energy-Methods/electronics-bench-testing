# Open Electrothermal Bench — EBT-R01 computational feasibility study

**Status:** v0.1, 2026-11-05 — **synthetic model and pre-registration draft only**. No physical measurements have been conducted. Independent research, not an approved KTH project, a thesis submitted for academic credit, or an accredited test laboratory.

## The research problem

A package-surface temperature curve may look correct while the internal junction temperature remains poorly determined. At the same time, a compact model calibrated for one cooling boundary condition can fail when the airflow or interface changes. This repository quantifies those risks with a transparent energy-conserving three-node synthetic system, then translates the findings into a proposed physical experiment.

**Provisional paper topic:** *When Surface Temperatures Mislead: Measurement Observability and Cross-Boundary Validation of Compact Thermal Models for Power-Electronics Cooling.* This is not a novelty claim: related parameter-identifiability, thermal transient, and experimental-design research already exists (see `docs/literature_gap_matrix.md`).

## What is actually completed

- Deterministic three-node thermal-network solver using exact zero-order-hold state propagation.
- Seven automated physics/solver checks (equilibrium, energy balance, grid invariance, thermal ordering, thermal boundary response, first-order solution).
- Synthetic package, sink and hidden-junction temperatures; simulated package measurement noise (0.15 degrees C standard deviation).
- One-RC calibration on **only one 5 W natural-cooling case**, plus independent synthetic 3 W, forced-cooling, and altered-interface test cases.
- Numerical demonstration that two distinct hidden junction-to-package resistances can have similar measured package temperatures but different internal junction temperatures.
- Four generated figures, CSV datasets, JSON metrics and SHA-256 hashes.
- Pre-experiment design, metrology requirements, publication gates, literature screening and project safety exclusions.

## Reproduce (Python 3.11+)

```bash
python -m venv .venv
# activate the virtual environment for your OS
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pytest -q
python scripts/run_study.py
```

Outputs: `data/synthetic/`, `results/` and `figures/`. Use `results/SHA256SUMS.json` for tabular-data integrity. The script is deterministic with fixed seed `20261105` and intentionally overwrites its own synthetic outputs. **Never mix actual measurements into `data/synthetic/`.**

### Model and assumptions

Junction `j`, observed package `p`, and sink `s` are connected by thermal resistances `Rjp`, `Rps`, `Rsa`, and carry thermal capacitances `Cj`, `Cp`, `Cs`. Constant electrical dissipation is injected at the junction. Ambient temperature, resistances and capacities are fixed within a simulated case; radiation, lateral spreading, sensor loading, T-dependent properties, contact-pressure variability, airflow turbulence and device electrical dynamics are omitted. Therefore the benchmark is deliberately *not* an accurate model of a particular MOSFET or physical rig.

State equations:

```text
Cj dTj/dt = P - (Tj - Tp)/Rjp
Cp dTp/dt = (Tj - Tp)/Rjp - (Tp - Ts)/Rps
Cs dTs/dt = (Tp - Ts)/Rps - (Ts - Ta)/Rsa
```

All capacities are positive; all resistances are positive. The model conserves energy subject to the numerical integration of sink-to-ambient heat flow.

### Synthetic parameter values

`Rjp=0.75 K/W`, `Rps=0.45 K/W`, `Rsa=3.0 K/W`, `Cj=0.6 J/K`, `Cp=9 J/K`, `Cs=70 J/K`, `Ta=24 °C`. The alternative hidden-junction model uses `Rjp=1.50 K/W`. These are illustrative parameters, **not calibrated or extracted from a device datasheet**.

### How to interpret results

- A nominal package noise of 0.15 degrees C is **assumed** for the simulation, not a claim about a real sensor.
- `forced_boundary_aware_rmse_C` uses the forced-cooling `Rsa` **provided as an independent synthetic boundary input**. It is not secretly estimated from the held-out forced-cooling temperature traces.
- The three-node generator is the synthetic reference; it is not an empirical ground truth. Its good energy conservation validates the math implementation, not physics of any real package.
- The study currently demonstrates a **problem formulation and model/code verification**, not a peer-reviewed scientific result or physical thermal validation.

## Documents

- `docs/research_concept.md` — questions, hypotheses, study design, go/no-go decision, pilot implications.
- `docs/literature_gap_matrix.md` — relevant literature, prior art overlap, and claim boundaries.
- `docs/experimental_protocol_draft.md` — controlled, safe, hardware-stage test campaign plan.
- `docs/standards_applicability.md` — references without claiming standards compliance.
- `docs/publication_and_data_plan.md` — reproducibility levels, preservation, publication/permissions.

## Research governance and publication status

No experimental data has been collected. No equipment has been calibrated. No person or KTH group has agreed to supervise, authorize the use of laboratory facilities, coauthor, or review this project. All physical experiments require the host facility's authorization and a signed safety/test readiness review. We will not use a package surface sensor to claim direct junction temperature measurements.

Software code: MIT license (`LICENSE`). Original project documentation and generated synthetic datasets: CC BY 4.0 (see `DATA-LICENSE.md`). External linked literature and standards retain their own copyright.

**Independent researcher:** Abhijith Sivaprasadan · ORCID [0000-0003-0299-5745](https://orcid.org/0000-0003-0299-5745).
