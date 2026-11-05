# EBT-R01 · Paper positioning and Gate G1 decision

**Controlled working decision:** EBT-R01-DEC-003 / revision 0.3 / 2026-11-05  
**Based on:** [EBT-LIT-003](EBT-LIT-003_critical_full_text_assessment_v0.3.md); [evidence matrix](../08_project_controls/fulltext_evidence_matrix_v0.3.csv); [search log](../08_project_controls/literature_search_log_v0.3.csv).  
**State:** **provisional / G1 PARTIALLY COMPLETE.** Not approval to execute physical tests or a claim of scientific novelty.

## 1. Decision: tighten contribution without changing EBT-PMP-001 v1.0

Retain the overall research programme but **reframe the flagship paper around a prospective benchmark**. A basic model-fit exercise, comparison of cooling methods, MOSFET heatsink experiment, sensor-placement caution, remount test or thermal-interface study individually would duplicate published work. Specifically:

- **Putthong et al. 2026:** already demonstrate SVD/detectability-driven case choice and severe calibration-versus-validation divergence in a **steady-state** four-MOSFET test;
- **Zhang et al. 2024:** already experimentally compare transient inverse thermal structure methods under **dry/TIM** interfaces;
- **Farkas et al. 2020:** explicitly examine thermal-metric reproducibility, external sensors, TIMs and cooling apparatus;
- **Ma et al. 2021** and **Bahman et al. 2017:** boundary-conditioned compact-network modeling predates EBT;
- **Toth-Pal & Nee 2026 (KTH):** already quantify interface-thermal variability over 30 packaged assemblies;
- **Ress et al. 2026:** already correct for external series power and publish supporting thermal-measurement data.

**Research hypothesis to evaluate, NOT claim as original:** a compact boundary-aware transient model, given **boundary information measured without using holdout temperatures**, may yield better *prospective* surface-temperature prediction and calibrated intervals on fully withheld cooling conditions and remounted assemblies than a fair fixed-boundary model.

This specific combination remains only *potentially differentiable*. Full Cnudde and Ma methods could preempt much of it; a publishable paper requires scientific value beyond openly uploading a model.

## 2. Proposed central paper

**Provisional title:** *Prospective Cross-Boundary Validation of Compact Thermal Models: An Open Low-Voltage Benchmark with Independent Boundary Measurements and Assembly Variability.*

**Target research type:** experimental benchmark + methods evaluation; a data/method paper if the novelty of model comparison is insufficient. *Not* a novel numerical inversion theory paper.

**Primary dependent variables:** observed and reference-qualified heater-package/sink surface temperatures and measured electrical dissipation; internal MOSFET junction temperature remains **unobserved** unless a separate qualified reference is built.

**Important choice:** the Q0 reference heater is a non-semiconductor thermal source. It can validate **fixture/method predictions at its measured surfaces**, not semiconductor junction-temperature predictions, package mechanical stresses or lifetime.

## 3. Proposed comparators (fixed BEFORE confirmatory results)

| Label | Model | Permitted inputs | Principal limitation |
|---|---|---|---|
| B0 | static apparent thermal-resistance baseline | calibration P and temperatures; holdout measured P only | no transient shape prediction; benchmark only late-stage temperatures |
| B1 | one-node first-order RC, fixed cooling boundary | fitting configuration temperature traces, measured P and ambient | ignores known boundary change |
| B2 | 2–3 node constrained passive RC, fixed boundary | same fitting cases as B1 | risk of weakly identifiable parameters |
| B3 | boundary-aware passive network | same fitting cases plus **separately qualified** boundary characteristic and its uncertainty, *acquired before target holdout* | additional boundary measurement time/cost; must not fit holdout response |
| B4 (optional) | verified spatial conduction / CHT model | known independent geometry and cooling information; mesh study | justified only with adequate parameters and computing; not essential |

**Fairness rule:** model comparisons must report (i) training data accessible, (ii) independent boundary measurements each receives, (iii) fit parameter count, (iv) whether selection used holdout feedback, and (v) operational complexity. A B3 advantage cannot be interpreted as a better algorithm if it simply received more relevant *target-specific* information.

## 4. Confirmatory experiment and statistical unit

**Q0 pilot:** 12 proposed planning-only runs; two *unassigned* power levels, natural/forced labels, three independent remount events. These runs establish precision, time constants, achievable temperature gradients, needed replication and safety limits. They are **not the confirmatory holdout**.

**R01 planning envelope:** 54 proposed runs (3 allowable power settings x 3 cooling conditions x 2 interface conditions x 3 independent assemblies) is **not** a guaranteed adequately powered design. The pilot may require changing the number of assemblies, conditions or runs.

**Preregistration:** define what is training, what is validation and what may be tuned, before any confirmatory measurement. Reserve entire cooling conditions or complete new mounting events. Account for nested repeated temperature samples within an assembly; the independent observational unit is the **mount/session under controlled configuration**, not each logger timestamp.

**Metrology:** Q0 must establish uncertainty in heater-branch electrical power, contact and ambient temperatures, position perturbation, logging timebase and sensor lag, thermal baseline drift, fan/flow state and repeated assembly effects. No qualified reference means no metrologically traceable instrument claim.

## 5. Paper decision and falsifiable outcomes

**Outcome A — positive:** B3 materially improves predeclared held-out surface temperatures and interval coverage relative to B1/B2, even after allowing for boundary-measurement cost and assembly variance. Report model-specific conditions and effect size; do not generalize to all power electronics.

**Outcome B — null:** B3 provides little or no practical improvement after measurement uncertainty. Publish why: boundary sensing noisy, model too simple, natural/forced physics nontransferable, or fitting overparameterized.

**Outcome C — negative:** richer model predicts worse; or unmeasured lead losses/reassembly effects dominate. Publish a measurement and model-failure benchmark if qualified.

**Outcome D — no qualified boundary:** boundary estimates require target holdout output. Treat as retrospective characterization, **do not advertise prediction transfer**.

**Outcome E — no powered testing:** computational feasibility remains a synthetic methods demonstration, **not an experimental paper**.

## 6. G1 closure conditions

G1 remains **open** until all of the following are resolved and recorded:

1. Legitimate full text and method comparisons for **Cnudde 2026**, **Ma 2021**, **Bahman 2017**, **Wang online 2025/issue 2026**, and **Schulz 2026** if accessible; otherwise document precise access failures and obtain independent critical review acknowledging the uncertainty.
2. Reproducible database query and citation screening, without falsely calling the present focused review comprehensive.
3. An explicit side-by-side novelty/overlap table comparing same *observable, model input, holdout unit, boundary knowledge and uncertainty*.
4. At least one technically qualified independent reviewer evaluates the contribution statement.
5. Manuscript target chosen according to evidence: rigorous experimental research paper **versus** methods/data note **versus** open qualification report.

**Physical G2/G3 safety gates are separate** and cannot be replaced by G1.

## 7. KTH outreach decision

A research discussion becomes more credible once G1 reaches a defensible limited decision and Q0 has actual hardware/instrument evidence. An early methods critique can be sought without claiming a complete paper: show the literature overlap and ask directly if the prospective benchmark would add useful knowledge. Mention the **2026 KTH paper by Toth-Pal and Nee** explicitly rather than approaching the department as if thermo-electronic packaging were new there.

**Version control:** document future source additions and amendments in review/decision revisions; never silently overwrite the v1.0 baseline or relabel synthetic data as measured data.
