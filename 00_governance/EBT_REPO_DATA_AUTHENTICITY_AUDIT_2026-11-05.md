# EBT repository boilerplate, representative-data and evidence audit

**Checked against:** Open-Energy-Methods/electronics-bench-testing `main`, 5 November 2026; GitHub recursive tree returned **96 tracked blobs**. Read original v1.0 package, v0.4 model package, selected current v0.2/v0.3/v0.4 GitHub files and source registers. Binary exports and every scholarly full text are **not separately revalidated byte-for-byte** by this audit.

**Interpretation:** Severity here means *danger if incorrectly advertised as a verified engineering result*, not a claim that the underlying code or documents are poor quality. Most high flags are deliberately labeled drafts/simulations, so their very existence is appropriate. No physical experiment, calibrated electronics lab measurement or authorized energized procedure appears in this repository.

## Core conclusions

1. The entire `07_source_baseline/EBT_R01_Feasibility_v0.1/data/synthetic/` dataset and its plots/metrics are simulated. A passing numerical test means software behavior under assumed physics, not laboratory validation.
2. The `09_model_comparison/` B0-B3 models are genuine executable software, but the data generator creates all training, qualification, validation, noise, constants, and stress cases. 25 random seeds do not equal 25 physical remounts.
3. `09_model_comparison/results/` and `figures/` each hold `.gitkeep` on GitHub, while the separate supplied v0.4 ZIP contains the generated JSON and PNG. The scientific result figures are not committed on `main` as generated artifacts.
4. All 54 rows of `03_campaigns/EBT-R01/provisional_run_matrix.csv` say `NOT AUTHORIZED` / `No measured data`, and the watts, execution order and training/holdout split are TBD. The Q0 12-row pilot exists only as a generator/plan.
5. `08_project_controls/equipment_register.csv` has eight uninspected instrument entries and no model/serial/calibration identity; hardware and electrical diagrams are predesign, not construction or safety approvals.
6. Source register and control artifacts include deliberate placeholders, incomplete scholarly access, historical QA counts and an import-specific rather than current-HEAD SHA-256 manifest.
7. Genuine work: the models, tests, published literature synthesis and documented facility correspondence/status. None should be presented as measured electrothermal hardware validation.

## Generated artifacts present in the v0.4 ZIP but absent from the tracked GitHub tree

- `09_model_comparison/results/synthetic_model_comparison_v0.4.json`
- `09_model_comparison/results/synthetic_noise_seed_robustness_v0.4.json`
- `09_model_comparison/figures/comparison_holdouts.png`
- `09_model_comparison/figures/boundary_failure_modes.png`

These four source paths should be treated as **not committed** as of this audit; the files can be regenerated and have already existed in a separate archive.

## Full 96-file inventory

| Exact repository path | Classification | Presentation risk | What is real versus representative / missing | Appropriate action |
|---|---|---|---|---|
| `.github/workflows/ebt-ci.yml` | REAL_NUMERICAL_CI | Low | Genuine code checks; does not perform/verify hardware experiments | Keep as numerical and planning verification |
| `.gitignore` | GENUINE_INFRASTRUCTURE_POLICY | Low | Real project operational metadata, not a measured dataset | No physical-evidence claim |
| `00_governance/CHANGELOG.md` | REAL_CHANGE_LOG | Low | Genuine record of documentary/code change, not physical results | Keep revised and dated |
| `00_governance/CHANGE_CONTROL.md` | PROJECT_GOVERNANCE | Low | Actual process and change policy; future approval fields remain contingent | Maintain evidence links |
| `00_governance/RELEASE_MANIFEST_SHA256.json` | HISTORICAL_IMPORT_MANIFEST | High | Lists 65 files excluding itself from initial import; not a current main-branch integrity manifest | Preserve as v1.0 archive, create revisioned manifest for current release/tag |
| `00_governance/SOURCE_ARCHIVE_PROVENANCE.md` | REAL_ARCHIVE_PROVENANCE | Low | Source archive checksums provenance for initial v1.0 | Preserve as archive metadata |
| `01_research/EBT-LIT-002_targeted_gap_review_v0.2.md` | NON_SYSTEMATIC_PRELIMINARY_LITERATURE | Medium | Focused prior-art comparison, not full systematic review | Treat v0.3 as more recent |
| `01_research/EBT-LIT-003_critical_full_text_assessment_v0.3.md` | MIXED_FULLTEXT_AND_ABSTRACT_EVIDENCE | High | Five full-text papers + one thesis summary; critical competitors abstract/record only | Do not say full systematic review or novelty established |
| `01_research/EBT-R01_paper_positioning_decision_v0.3.md` | PROVISIONAL_PUBLICATION_DECISION | Medium | Paper title and model contract proposed; no confirmed novelty or physical evidence | Keep G1 open and choose final framing only after evidence |
| `01_research/one_page_pitch_draft.md` | SUPERSEDED_RESEARCH_PITCH | High | Early pitch centered on hidden-junction observability; later scope focuses measured accessible temperatures | Rewrite only after G1, label original historical internal draft |
| `02_hardware/DEVICE_CANDIDATES_v0.2.csv` | CANDIDATE_OR_REQUIREMENT_REGISTER | High | Candidate families/instrument needs, not purchased/inspected actual assets | Verify exact part number, stocks, datasheet and real instrument inventory |
| `02_hardware/EBT-HW-001_device_selection_v0.2.md` | CANDIDATE_HARDWARE_PREDESIGN | High | Example nominal 10 ohm parts and 2/5 W sizing examples not authorized setpoints | Select manufacturer ordering codes and approved operating envelope |
| `02_hardware/EBT-HW-002_protected_bench_and_sensor_layout_v0.2.md` | ILLUSTRATIVE_BLOCK_SCHEMATIC | Critical | Conceptual connections and sensor locations; not a netlist or rated build drawing | Generate and review complete electrical/mechanical drawings before energizing |
| `02_hardware/INSTRUMENT_MINIMUM_v0.2.csv` | CANDIDATE_OR_REQUIREMENT_REGISTER | High | Candidate families/instrument needs, not purchased/inspected actual assets | Verify exact part number, stocks, datasheet and real instrument inventory |
| `03_campaigns/EBT-Q0/pilot_plan_v0.2.md` | UNAPPROVED_QUALIFICATION_PLAN | High | 12 hypothetical pilot rows or Q0 description; no device-specific limits or physical readings | Authorize site and verify devices/DAQ before execution |
| `03_campaigns/EBT-Q0/qualification_protocol_draft.md` | UNAPPROVED_QUALIFICATION_PLAN | High | 12 hypothetical pilot rows or Q0 description; no device-specific limits or physical readings | Authorize site and verify devices/DAQ before execution |
| `03_campaigns/EBT-R01/main_test_plan_draft.md` | UNAPPROVED_MAIN_TEST_DRAFT | High | Treatment levels, timing, safety, sample size and thresholds remain undefined | Finalize after Q0 with host-lab signoff |
| `03_campaigns/EBT-R01/provisional_run_matrix.csv` | 54_UNEXECUTED_PLANNED_RUNS | Critical | 54 planning rows: every watt/run order/split TBD, all NOT AUTHORIZED, all No measured data | Do not call them 54 tests; freeze actual levels and holdouts after approved pilot |
| `05_publication/linked_in_post_outline.md` | PUBLICATION_SCAFFOLD | Medium | Unwritten example structure; no verified result photo, actual plot or DOI | Do not publish as research achievement |
| `05_publication/release_checklist.md` | UNSATISFIED_RELEASE_CHECKLIST | High | Unchecked release gates, not a release approval | Complete before data or paper release |
| `06_templates/change_request.md` | INTENTIONALLY_BLANK_TEMPLATE | Medium | Blank change request, run log, gate review or instrument assurance form | Populate only when real evidence exists; do not replace with fabricated samples |
| `06_templates/equipment_verification_form.md` | INTENTIONALLY_BLANK_TEMPLATE | Medium | Blank change request, run log, gate review or instrument assurance form | Populate only when real evidence exists; do not replace with fabricated samples |
| `06_templates/gate_review.md` | INTENTIONALLY_BLANK_TEMPLATE | Medium | Blank change request, run log, gate review or instrument assurance form | Populate only when real evidence exists; do not replace with fabricated samples |
| `06_templates/run_record_template.md` | INTENTIONALLY_BLANK_TEMPLATE | Medium | Blank change request, run log, gate review or instrument assurance form | Populate only when real evidence exists; do not replace with fabricated samples |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/.github/workflows/ci.yml` | NUMERICAL_TEST_OR_LEGACY_CI | Low | Actual validation of code assertions, not experiments; nested workflow not root-active | Keep code tests; do not equate with physical validation |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/.gitignore` | ARCHIVED_SOURCE_METADATA | Low | Licensing, citation, package declarations or metadata for earlier synthetic baseline | Keep immutable archival context |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/CITATION.cff` | ARCHIVED_SOURCE_METADATA | Low | Licensing, citation, package declarations or metadata for earlier synthetic baseline | Keep immutable archival context |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/DATA-LICENSE.md` | ARCHIVED_SOURCE_METADATA | Low | Licensing, citation, package declarations or metadata for earlier synthetic baseline | Keep immutable archival context |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/LICENSE` | ARCHIVED_SOURCE_METADATA | Low | Licensing, citation, package declarations or metadata for earlier synthetic baseline | Keep immutable archival context |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/README.md` | PROVENANCE_DOCUMENT | Low | Explains explicitly synthetic v0.1 model and data columns | Retain disclaimers |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/data/synthetic/SCHEMA.md` | PROVENANCE_DOCUMENT | Low | Explains explicitly synthetic v0.1 model and data columns | Retain disclaimers |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/data/synthetic/baseline_synthetic.csv` | SYNTHETIC_DATA | Critical | Numeric histories and noisy sensors generated from assumed thermal circuits, not measured | Keep data/synthetic path, preserve seed, never describe as real instrument data |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/data/synthetic/heldout_synthetic.csv` | SYNTHETIC_DATA | Critical | Numeric histories and noisy sensors generated from assumed thermal circuits, not measured | Keep data/synthetic path, preserve seed, never describe as real instrument data |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/docs/EBT_R01_Preproposal_Feasibility_v0.1.pdf` | HISTORICAL_SYNTHETIC_REPORT | High | Illustrative preproposal with simulated findings, not a peer-reviewed report | Retain archival label; link newer v0.4 work |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/docs/experimental_protocol_draft.md` | LEGACY_DRAFT_METHODOLOGY | High | Historical research/experiment proposal includes future activities and idealized parameters | Mark historical; use v0.3/v0.4 current methodology for planning |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/docs/literature_gap_matrix.md` | HISTORICAL_RESEARCH_SUPPORT | Medium | Existing literature/standards/readiness/publication discussion; some incomplete or superseded | Cross-link current status, do not present proposed steps as done |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/docs/publication_and_data_plan.md` | HISTORICAL_RESEARCH_SUPPORT | Medium | Existing literature/standards/readiness/publication discussion; some incomplete or superseded | Cross-link current status, do not present proposed steps as done |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/docs/readiness_checklist.md` | HISTORICAL_RESEARCH_SUPPORT | Medium | Existing literature/standards/readiness/publication discussion; some incomplete or superseded | Cross-link current status, do not present proposed steps as done |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/docs/research_concept.md` | LEGACY_DRAFT_METHODOLOGY | High | Historical research/experiment proposal includes future activities and idealized parameters | Mark historical; use v0.3/v0.4 current methodology for planning |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/docs/standards_applicability.md` | HISTORICAL_RESEARCH_SUPPORT | Medium | Existing literature/standards/readiness/publication discussion; some incomplete or superseded | Cross-link current status, do not present proposed steps as done |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/figures/01_three_node_response.png` | SYNTHETIC_FIGURE | High | Visuals come from generated model signals | Keep figure captions explicitly synthetic |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/figures/02_surface_blind_spot.png` | SYNTHETIC_FIGURE | High | Visuals come from generated model signals | Keep figure captions explicitly synthetic |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/figures/03_boundary_transfer.png` | SYNTHETIC_FIGURE | High | Visuals come from generated model signals | Keep figure captions explicitly synthetic |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/figures/04_case_metrics.png` | SYNTHETIC_FIGURE | High | Visuals come from generated model signals | Keep figure captions explicitly synthetic |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/pyproject.toml` | ARCHIVED_SOURCE_METADATA | Low | Licensing, citation, package declarations or metadata for earlier synthetic baseline | Keep immutable archival context |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/requirements.txt` | ARCHIVED_SOURCE_METADATA | Low | Licensing, citation, package declarations or metadata for earlier synthetic baseline | Keep immutable archival context |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/results/SHA256SUMS.json` | SYNTHETIC_RESULT_OR_INTEGRITY | High | Numerical metrics or synthetic-output file hashes; physically unvalidated | Retain explicit simulated provenance and regenerate from code |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/results/metrics.json` | SYNTHETIC_RESULT_OR_INTEGRITY | High | Numerical metrics or synthetic-output file hashes; physically unvalidated | Retain explicit simulated provenance and regenerate from code |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/scripts/make_report.py` | EXECUTABLE_SYNTHETIC_MODEL | Medium | Genuine executable code whose parameters/noise/power histories are assumptions | Preserve tests and provenance, no device property claims |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/scripts/run_study.py` | EXECUTABLE_SYNTHETIC_MODEL | Medium | Genuine executable code whose parameters/noise/power histories are assumptions | Preserve tests and provenance, no device property claims |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/scripts/verify_reproduction.py` | EXECUTABLE_SYNTHETIC_MODEL | Medium | Genuine executable code whose parameters/noise/power histories are assumptions | Preserve tests and provenance, no device property claims |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/src/ebt/__init__.py` | EXECUTABLE_SYNTHETIC_MODEL | Medium | Genuine executable code whose parameters/noise/power histories are assumptions | Preserve tests and provenance, no device property claims |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/src/ebt/model.py` | EXECUTABLE_SYNTHETIC_MODEL | Medium | Genuine executable code whose parameters/noise/power histories are assumptions | Preserve tests and provenance, no device property claims |
| `07_source_baseline/EBT_R01_Feasibility_v0.1/tests/test_model.py` | NUMERICAL_TEST_OR_LEGACY_CI | Low | Actual validation of code assertions, not experiments; nested workflow not root-active | Keep code tests; do not equate with physical validation |
| `08_project_controls/budget_and_procurement.csv` | NONCOMMITTED_ESTIMATED_BUDGET | High | 7 of 8 prices TBD; lone SEK 750 backup is user-provided indicative quote, not live verified price | Supplier quote and facility inventory before approval |
| `08_project_controls/change_requests.csv` | EMPTY_CONTROL_REGISTER | Medium | Column headers only; no accepted changes recorded | Use for future approved scope changes |
| `08_project_controls/decision_log.csv` | REAL_DECISIONS_CONDITIONAL_EXECUTION | Low | Real recorded scope/safety rules with scientific decisions provisional | Retain provenance and gates |
| `08_project_controls/equipment_register.csv` | ENTIRELY_UNINSPECTED_INSTRUMENTS | Critical | All 8 models/serial numbers and reference records TBD, status Uninspected | Survey actual lab and enter serial/range/reference evidence |
| `08_project_controls/execution_board.csv` | PLANNED_WORK_TRACKER | Medium | Future deadlines and status estimates; not evidence of finished tasks | Synchronize with GitHub issues and actual deliverables |
| `08_project_controls/facility_access_tracker.csv` | ACCESS_REQUEST_TRACKER_NOT_SITE_APPROVAL | High | Records requests; Student Workshop Canvas invite path described, not powered-lab authorization | Update on actual induction/card/access and ELAB response |
| `08_project_controls/fulltext_evidence_matrix_v0.3.csv` | MIXED_SOURCE_EVIDENCE | Medium | Actual paper metadata and reviews plus abstract-only records / unknown details | Use full-text access grades, avoid presenting abstract-only as read |
| `08_project_controls/literature_register.csv` | MIXED_SOURCE_EVIDENCE | Medium | Actual paper metadata and reviews plus abstract-only records / unknown details | Use full-text access grades, avoid presenting abstract-only as read |
| `08_project_controls/literature_search_log_v0.3.csv` | PARTIAL_SEARCH_AUDIT | Medium | Real access log but systematic index search explicitly not done | Complete IEEE/Scopus/WoS search with date/query/result trail |
| `08_project_controls/qa_report.json` | HISTORICAL_QA_SNAPSHOT | High | Frozen initial v1.0 counts (7 literature, 10 tasks, 7 tests), not a current 96-file audit | Label snapshot as-of and generate a new CI-backed live status report |
| `08_project_controls/requirements_register.csv` | VERIFICATION_PENDING | High | Many requirements marked Open/Draft/Partially met; evidence docs not proof of physical verification | Use actual test and signed records to close |
| `08_project_controls/risk_register.csv` | JUDGMENT_BASED_RISK_SCORES | Medium | Likelihood and impact scores are management estimates, not statistically derived risk frequencies | Review once lab and component details known |
| `08_project_controls/standards_matrix.csv` | REFERENCE_ONLY_NO_COMPLIANCE | High | Standards applicability and methodology listed; no compliance/certification established | Get standards and document applicability; no compliance badge |
| `09_model_comparison/README.md` | SIMULATION_METHODS_REPORT | High | Numerical results and conditional boundary qualification with illustrative parameters | Keep explicit synthetic-only header and caveats |
| `09_model_comparison/docs/EBT-R01_model_comparison_and_boundary_qualification_v0.4.md` | SIMULATION_METHODS_REPORT | High | Numerical results and conditional boundary qualification with illustrative parameters | Keep explicit synthetic-only header and caveats |
| `09_model_comparison/figures/.gitkeep` | EMPTY_DIRECTORY_PLACEHOLDER | High | No generated v0.4 figures or JSON results are committed in these folders | Regenerate and commit labeled synthetic artifacts or clearly state outputs are generated on demand |
| `09_model_comparison/research_models/__init__.py` | CODE_PACKAGE_SUPPORT | Low | Package structure, no empirical dataset | No action |
| `09_model_comparison/research_models/boundary.py` | REAL_ALGORITHM_ASSUMED_INPUTS | High | Executable boundary and uncertainty propagation but input errors/geometry are hypothetical | Qualify actual instrument covariance/geometry before any measured claim |
| `09_model_comparison/research_models/compare.py` | REAL_MODEL_SIMULATED_EVIDENCE | High | Actual physics/fit code; model structure and temperature histories not empirically established | Retain simulation tags, test model discrepancy and real observable limits |
| `09_model_comparison/research_models/physics.py` | REAL_MODEL_SIMULATED_EVIDENCE | High | Actual physics/fit code; model structure and temperature histories not empirically established | Retain simulation tags, test model discrepancy and real observable limits |
| `09_model_comparison/research_models/run.py` | REAL_MODEL_SIMULATED_EVIDENCE | High | Actual physics/fit code; model structure and temperature histories not empirically established | Retain simulation tags, test model discrepancy and real observable limits |
| `09_model_comparison/research_models/synthetic.py` | SYNTHETIC_EXPERIMENT_GENERATOR | Critical | Fabricates training, qualification, validation, 4 apparent-replicate runs and stress scenarios | Keep distinct from real experimental inputs; label 4 runs as simulated independent records |
| `09_model_comparison/research_models/uncertainty.py` | REAL_ALGORITHM_ASSUMED_INPUTS | High | Executable boundary and uncertainty propagation but input errors/geometry are hypothetical | Qualify actual instrument covariance/geometry before any measured claim |
| `09_model_comparison/results/.gitkeep` | EMPTY_DIRECTORY_PLACEHOLDER | High | No generated v0.4 figures or JSON results are committed in these folders | Regenerate and commit labeled synthetic artifacts or clearly state outputs are generated on demand |
| `09_model_comparison/scripts/__init__.py` | SYNTHETIC_GENERATION_TOOL | Medium | Produces figures or robustness metrics from synthetic scenarios | Publish generated outputs with provenance or explicit regenerate instructions |
| `09_model_comparison/scripts/plot_comparison.py` | SYNTHETIC_GENERATION_TOOL | Medium | Produces figures or robustness metrics from synthetic scenarios | Publish generated outputs with provenance or explicit regenerate instructions |
| `09_model_comparison/scripts/robustness_scan.py` | SYNTHETIC_GENERATION_TOOL | Medium | Produces figures or robustness metrics from synthetic scenarios | Publish generated outputs with provenance or explicit regenerate instructions |
| `09_model_comparison/tests/test_physics.py` | REAL_MODEL_SIMULATED_EVIDENCE | High | Actual physics/fit code; model structure and temperature histories not empirically established | Retain simulation tags, test model discrepancy and real observable limits |
| `09_model_comparison/tests/test_stress_scenarios.py` | NUMERICAL_UNIT_TEST | Low | Actual code tests; passing does not validate field measurement method | Keep coverage distinction |
| `CITATION.cff` | SOFTWARE_CITATION_METADATA | Low | Metadata for software planning baseline only, no paper or DOI | Avoid calling it a scientific publication |
| `CONTRIBUTING.md` | GENUINE_INFRASTRUCTURE_POLICY | Low | Real project operational metadata, not a measured dataset | No physical-evidence claim |
| `DATA-LICENSE.md` | GENUINE_INFRASTRUCTURE_POLICY | Low | Real project operational metadata, not a measured dataset | No physical-evidence claim |
| `EBT_Master_Programme_Plan_v1.0.docx` | DETAILED_PLAN_NOT_VALIDATED_RESULT | High | Substantive research plan with illustrative evidence and prospective protocol, not measurements | Keep dated v1.0 snapshot, label planned vs done |
| `EBT_Master_Programme_Plan_v1.0.md` | DETAILED_PLAN_NOT_VALIDATED_RESULT | High | Substantive research plan with illustrative evidence and prospective protocol, not measurements | Keep dated v1.0 snapshot, label planned vs done |
| `EBT_Master_Programme_Plan_v1.0.pdf` | DETAILED_PLAN_NOT_VALIDATED_RESULT | High | Substantive research plan with illustrative evidence and prospective protocol, not measurements | Keep dated v1.0 snapshot, label planned vs done |
| `GITHUB_IMPORT.md` | SUPERSEDED_BOOTSTRAP_INSTRUCTIONS | Medium | Instructions still tell reader to create and import an empty repository already created | Move to archival migration notes or replace with current developer onboarding |
| `LICENSE` | GENUINE_INFRASTRUCTURE_POLICY | Low | Real project operational metadata, not a measured dataset | No physical-evidence claim |
| `README.md` | RESEARCH_STATUS_README | Medium | Real project index; methods, synthetic outputs, draft gates; not experimental proof | Ensure status and generated-output availability are current |
| `SAFETY_AND_PROVENANCE.md` | GENUINE_INFRASTRUCTURE_POLICY | Low | Real project operational metadata, not a measured dataset | No physical-evidence claim |
| `scripts/make_pilot_plan.py` | REAL_PLANNING_SOFTWARE | Low | Working program/checks for procedural fixtures, but no real run data | Keep distinct from physical validation |
| `tests/test_literature_evidence.py` | REAL_PLANNING_SOFTWARE | Low | Working program/checks for procedural fixtures, but no real run data | Keep distinct from physical validation |
| `tests/test_pilot_plan.py` | REAL_PLANNING_SOFTWARE | Low | Working program/checks for procedural fixtures, but no real run data | Keep distinct from physical validation |

## Recommended remediation order

**P0 — accuracy and reproducibility (do first):** explicitly mark v0.4 generated figures/results as derived synthetic artifacts, commit them or add release verification/links; replace misleading claims of uploaded figures. Keep original v0.1 synthetic archive intact. Clearly say that the 54-run schedule is unexecuted and Q0 data are absent.

**P1 — avoid stale or misleading records:** label `qa_report.json` and `RELEASE_MANIFEST_SHA256.json` historical snapshots (not current status); retire `GITHUB_IMPORT.md` instructions; update current README/navigation and older internal pitch to point to v0.3 paper framing. Do not silently overwrite archived research baselines.

**P2 — replace engineering boilerplate with real evidence after authorization:** inspected instrument inventory, reference-grade uncertainty, exact component order numbers and site permission, a connection-level approved schematic, dimensioned fixture/sensor drawings, a costed BoM and actual Q0 pilot observations.

**P3 — research maturity:** obtain inaccessible competing full texts and a reproducible index search before claiming novelty; use real physically independent training/qualification/holdout campaigns before paper-grade empirical prediction claims.

### Exact wording for public materials

> *Electronics Bench Testing is an independent, open-source electrothermal research programme. It currently includes working, numerically verified compact thermal models; a documented critical literature assessment; synthetic experimental-design and boundary-transfer benchmarks; and preliminary laboratory/fixture protocols. Physical bench construction, instrument qualification and experimental validation remain pending. Numerical examples and hypothetical instrument values must not be read as real electronics measurements.*
