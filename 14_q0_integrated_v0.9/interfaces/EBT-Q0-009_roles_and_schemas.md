# EBT-Q0-009 — Compatibility contract: stage gates, raw data, roles

**Avoid a new incompatible schema.** The following are the ONE authoritative
machine-readable record types used in this integrated programme:

| Scope | Canonical document | Version | What it can prove |
|---|---|---|---|
| Physical fabricating / powered-site prerequisites | \`12_physical_readiness_v0.7/templates/EBT-GATE-007_record_UNFILLED.json\` | \`EBT-GATE-007-v0.7\` | Declared evidence references only; requires site reviewer |
| R01 prospective partition + external lock | \`13_q0_data_integrity_v0.8/ebt_q0_data.py\` / \`split_lock.json\` | \`EBT-SPLIT-008\` | Declared roles + chronology shape; cannot prove external lock genuineness |
| Per-acquisition metadata | \`13_q0_data_integrity_v0.8/ebt_q0_data.py\` / \`metadata.json\` | \`EBT-RUN-008\` | File content shape, named surface, identities; not physical measurement validity |
| Per-acquisition seal | \`13_q0_data_integrity_v0.8/ebt_q0_data.py\` / \`seal.json\` | \`EBT-SEAL-008\` | Byte equality at verification time; not immutable archival or true timestamp |

## Exactly mapped R01 fields

After real Q0 and before any prospective R01 HOLD acquisition, the
**same** lock and protocol must be represented in both EBT-GATE-007 and
EBT-SPLIT-008. The v0.9 cross-check requires:

| G2/G3 readiness record | R01 split lock |
|---|---|
| \`r01_confirmatory.prereg_lock_utc\` | \`lock_utc\` (compare actual UTC instants) |
| \`r01_confirmatory.prereg_document_sha256\` | \`protocol_sha256\` (equal lowercase hex) |
| \`r01_confirmatory.qualification_ids\` | \`role_run_ids.QUAL\` |
| \`r01_confirmatory.calibration_ids\` | \`role_run_ids.CAL\` |
| \`r01_confirmatory.reserved_holdout_ids\` | \`role_run_ids.HOLD\` |

The split record additionally requires \`external_lock_ref\`. A stated
GitHub link or timestamp is not proof the lock was truly committed before
HOLD results; a reviewer must independently check the authenticated
repository history, content hashes, access chronology and approval record.

Q0_PILOT uses its **own** pilot campaign and never shares the R01
QUAL/CAL/HOLD identity space. An eight-event source/site pilot and a
12-run power/cooling/remount pilot are not mandatory combined designs.

## Temperature and power meaning

- \`t_case_c\` is *accessible heater package surface*, **not junction**.
- \`t_surface_c\` is specified as \`T_PLATE\` or \`T_SINK\` in
  \`temperature_surface\`. Both are possible experimentally; neither
  may be silently converted to the other.
- \`t_ambient_c\` is at a recorded shielded air position, not inferred.
- \`heater_voltage_v\` and \`heater_current_a\` refer to simultaneously
  registered **heater-terminal** electrical quantities. \`V I\` is
  heater electrical dissipation, **not automatically all heat into the
  plate**, and \`R_app=\Delta T/P\` is a sensor-specific experimental
  aggregate, not a unique convection coefficient.
- \`cooling_state\` requires NAT/FAN/OTHER_DOCUMENTED with an actual
  \`cooling_reference_ref\`, not a synthetic effective g.
- A missing/aborted measurement is retained in its raw file and has
  a separate deviation record; it is not silently imputed.

## Important distinction

G2 stage record fields can be populated with arbitrary strings; the
readiness validator does **not** authenticate permissions. Likewise the
v0.8 data validator cannot verify laboratory truth. A structurally
complete record still awaits safety review and independent methodology
signoff. This integration only catches structural inconsistencies.


### Exact timezone contract

The canonical v0.8 `EBT-SPLIT-008.lock_utc` **must be UTC**
(`Z` or `+00:00`), and its checker rejects local offsets such as
`+01:00`. v0.7's gate checker historically accepts timezone-aware
values, including local offsets; the v0.9 compatibility audit normalizes
the **gate value** to UTC before comparing instants. For new records,
prefer UTC `Z` in both to avoid ambiguous cross-references.
