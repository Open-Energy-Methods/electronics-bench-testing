# EBT v0.8 — Q0 raw acquisition integrity and data firewall

**Status: software-only, NOT site authorization, NOT measured thermal evidence.**
No test rig, instrument calibration, approved power or physical data is supplied.
This package is independent of draft PR #11 (spatial synthetic analysis) and draft
PR #12 (physical readiness). It builds on main v0.5 and complements Q0-TP-002.

## Rationale

A future physical campaign needs an audit trail before any values are fitted
to B0–B3. A single ambiguous sensor name, remount identity, unexpected raw
edit, or reused holdout assembly can compromise the core paper claim.

This package defines and checks:

1. **Per-run records** at \`runs/RUN-ID/raw.csv\` (raw UTF-8 samples),
   \`metadata.json\` (sensor surface, part, mounting event, permission and
   timebase references), \`seal.json\` (SHA-256 hashes of raw and metadata).
2. **Acquisition quality**: exact columns, elapsed time strictly increasing,
   finite numeric readings, quality flags and retained aborts. Missing sensor
   values are flagged; no imputation or silent removal.
3. **Roles**: Q0_PILOT must remain exploratory. Confirmatory R01 requires
   separate QUAL, CAL and HOLD registration, non-overlapping run IDs and
   disjoint held-out assembly IDs from calibration/qualification.
4. **Partition lock**: \`split_lock.json\` declares UTC lock time, protocol
   hash, planned run IDs/roles and an external lock reference. The code checks
   shapes/declared chronology but **cannot verify that a claimed Git commit
   existed before data were inspected**. Independent verification is mandatory.
5. **Physical vs synthetic provenance**: SYNTHETIC_DEMO and
   PHYSICAL_UNVERIFIED must never share the same campaign. Even structurally
   complete physical records are not certified by this software.

## Commands (Python 3.11+, standard library only)

From this directory:

\`\`\`bash
python -m unittest discover -s tests -p 'test_*.py' -v
python demo.py                         # creates synthetic test data only, in a temporary directory
python demo.py --out /tmp/ebt-demo     # optional preserved demo; explicitly synthetic
python ebt_q0_data.py run /tmp/ebt-demo/runs/QUAL-001
python ebt_q0_data.py campaign /tmp/ebt-demo
\`\`\`

To validate a future authorized run, an operator (not this tool) first creates
\`metadata.json\` and \`raw.csv\` from actual instruments, then invokes
\`python ebt_q0_data.py seal <run_dir>\`. Sealing is **create-only**: it refuses
to overwrite an existing seal. A reviewer independently verifies the raw
hash, metadata, calibration records and site approval.

### Required raw CSV fields

\`\`\`csv
elapsed_s,heater_voltage_v,heater_current_a,t_case_c,t_surface_c,t_ambient_c,event_flag
\`\`\`

The last field allows RUN, ABORT, QUALITY_FLAG. Case/surface/ambient
values are labelled degC; electrical inputs V/A; elapsed seconds.
\`t_surface_c\` is T_PLATE or T_SINK as recorded in metadata. Voltage is
across heater terminals, current in the same branch. An aborted row may
contain blank readings; the file remains sealed but analysis readiness
becomes REVIEW_REQUIRED. A candidate sensor rate is not a measured
bandwidth or guarantee of timestamp synchronization.

### Limits and operational conditions

**No authorized experiment is implied.** File checks neither certify
calibration nor prove the permission references are genuine. SHA-256
does not establish an external trustworthy timestamp, protect against
deliberate replacement of an entire dataset, or validate sensor placement.
A manifest that merely *claims* it was locked before data cannot
constitute third-party pre-registration. Preserve an external dated
commit/registered protocol and have an independent reviewer check it.
Do not put sensitive staff or facility documents in the public repository
without explicit permission. No physical input to this validator may
replace the actual safety review, mechanical release or site SOP.

The 12-run Q0 matrix and 54-run R01 matrix remain **provisional** and are
not manufactured experiment logs.
