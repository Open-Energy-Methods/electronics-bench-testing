# Open science, data custody and publication gates — v0.1

## Reproducibility tiers

**A: Analysis-only** - reproduce synthetic outputs now; later reproduce raw-to-figure pipeline with actual permitted measurements and documented environments. Highest immediate availability.

**B: Low-cost physical comparison** - a separate reduced setup with clear measurement limitations and no claim of equivalent accuracy. Release only after safe methods are validated.

**C: Full qualified physical replication** - exact rig drawings, component identifiers, thermal/electrical calibration records where shareable, sensor locations, full runs, deviations, acceptance criteria and uncertainty analysis.

## Data separation

Use disjoint folders `data/synthetic/` and, only after approved physical tests, `data/experimental/raw/` and `data/experimental/processed/`. Synthetic CSV headers deliberately use `synthetic_*`. The former must never be relabeled as instrument records. Raw physical data is immutable and hashed; processed data must retain a script lineage to raw inputs.

## Publication routes

- GitHub: living source, issues, literature tracking and methods. Mark the research state and institutional independence accurately.
- Zenodo: versioned archived source/data release with DOI after reproducibility tests, permission checks and technical review. Citation metadata should point to an immutable release.
- arXiv: optional scholarly manuscript if editorial scope and research depth qualify. No automatic acceptance or peer review implied.
- Conference/journal: select only after confirmed differentiated contribution, independent physical results and sufficient statistical analysis.
- LinkedIn: publish verified plots, a methodological takeaway, failure/limitations and the exact GitHub/Zenodo link **after** review. Avoid misleading headlines about accuracy or device qualifications.

## Permissions and authorship

Explicit approval is required for publishing KTH-facility photos, instrument certificates, restricted laboratory manuals or proprietary fixture information. Using facilities does not establish KTH institutional authorship or endorsement. Discuss possible KTH collaborator roles, data rights, authorship policy and manuscript review **before** joint experiments.

## Open releases

Software MIT; original text/data CC BY 4.0; external standards/papers are only linked, not redistributed. The reproducibility pipeline should be independently run using pinned dependencies and verified against the output JSON/CSV hashes. CI could later run pytest and artifact checks once the GitHub repository is established.
