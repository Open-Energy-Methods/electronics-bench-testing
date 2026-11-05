# EBT-DAT-008 — Acquisition record contract and review gates

**Rev v0.8 · specification of prospective data structures, not completed experiments.**

## Data provenance states

- `SYNTHETIC_DEMO`: generated CSV exercises parsing, integrity and negative tests.
  No real temperature observations, no permitted operating conditions and no
  claim of an independently measured thermal boundary.
- `PHYSICAL_UNVERIFIED`: operator-entered physical observations whose
  claimed instrument, location, permission and provenance references
  **still require a human reviewer**. This is not a declaration of accuracy.
- There is deliberately **no automatic PHYSICAL_VALIDATED state**.
  Calibration, uncertainty and operational approvals are separate evidence.

## Records and roles

Run directory name and metadata run_id must match. The `mount_event_id`
identifies **one physical mounting event**, not one measurement run. Several
different run IDs may correctly reuse the SAME mount_event_id when electrical
power or fan conditions change **without any physical disassembly/remount**.
Every physical remount requires a NEW mount_event_id and a NEW assembly_id.
A mount_event_id cannot change roles, assembly IDs or fixture revision within
one campaign. The count of time samples or runs does not establish the
number of statistically independent remounts. `assembly_id` identifies
a documented physical assembly. Each run declares `site_id`, `heater_id`,
`temperature_surface` (exactly T_PLATE or T_SINK), fixture revision,
sensor map, reference evidence, facility permission, protocol, timebase,
acquisition UTC and review state. The raw CSV's surface column must not
be inferred to refer to a sink when it measured an added adapter plate.

`QUAL` supplies prospective boundary information from separate experiments.
`CAL` supplies designated model-fitting measurements.
`HOLD` reserves full independent assemblies/remounts for evaluation only.
`Q0_PILOT` provides exploratory metrology/mounting evidence and must never
be silently promoted to R01 confirmatory HOLD.

## Seal and preregistration integrity

Hashes are computed over **raw bytes** of the CSV and metadata JSON.
The seal is created once and rechecked before use. A changed raw record
must not be silently fixed; retain the original, issue a new record ID,
record the deviation and review both versions. The lock file includes a
protocol SHA-256, planned role/run IDs, UTC locking time and an external
evidence ref; software checking the local timestamp is **not proof** it
predated acquisition.

Before R01 physical validation, an independent reviewer should verify:
1. the protocol commit or trusted timestamp was published before HOLD data,
2. the external manifest SHA-256 matches the actual registered protocol,
3. the cold-start calibration and boundary-qualification files do not overlap
   reserved HOLD assemblies or IDs,
4. no target HOLD response was opened or used during model selection,
5. any abort, sensor loss or instrument discrepancy is preserved as an
   auditable quality flag rather than removed.

## Remaining gaps (not filled with representative numbers)

Actual samples, fan/airflow, thermocouple lag, instrument calibration,
site power envelope and laboratory permissions remain unavailable.
The data contract does not yet implement missing-channel interpolation,
covariance estimation, synchronized DAQ acquisition, signal-processing
filters, sample-size calculation or model fitting. Those require verified
equipment and real Q0 results. DO NOT overstate a passed parser test as
thermal research validation.

## Additional mandatory experimental configuration references

Each run now declares `cooling_state` (NAT, FAN or OTHER_DOCUMENTED) and
`cooling_reference_ref` with actual airflow/fan/setup provenance once physical
data are acquired. `heater_part_ref`, `heating_envelope_ref` and
`electrical_wiring_ref` identify the inspected device and site-reviewed
electrical envelope. These are **references**, not invented numeric ratings.
An ABORT or QUALITY_FLAG record requires `deviation_log_ref`; even an abort
with missing thermometry is retained and cannot silently become accepted data.
