# RIG-VVP-001 — Verification, test readiness and acceptance

RD0 proposed V&V sequence. All actual tests, dates, results and approvals are absent.
Verification methods map to RIG-REQ-001. Acceptance is not software CI.
 
| Step | Review/verification object | Acceptance evidence |
|---|---|---|
| V01 | design inputs and facility capability | SRR disposition, approved intended use and operating environment |
| V02 | calculation and digital layout | PDR trade, independent checks, interface and load/tolerance review |
| V03 | final drawing and electrical package | CDR signed release, BOM and component ratings; actual CAD/EDA review |
| V04 | manufactured part inspection | first article, verified critical dimensions, NCR closure |
| V05 | unpowered assembly | configuration, stable load/handling, repeat cassette installation, cable/access checks |
| V06 | device and instrument inspection | actual instrument serials, calibration/verification and wiring checks by competent staff |
| V07 | cold functional simulation | simulated data/timebase, state transitions, lost sensor/event preservation; no heater energy |
| V08 | readiness review | site permission, reviewed protection, guard, emergency procedure, approved test plan/limits |
| V09 | controlled powered commissioning | supervised site-approved staged test; fault and stop validation by qualified personnel |
| V10 | thermal/airflow qualification | observed no-load/loaded flow, environmental mapping, heat-path and uncertainty review |
| V11 | measurement qualification | documented reference comparison, lag, synchronization, repeatability, uncertainty |
| V12 | rig acceptance | requirement-by-requirement verified evidence or approved restriction, as-built baseline, operator training |
 
Use factory-acceptance-style unpowered checks and site-acceptance-style
installed verification adapted to a research rig (not certified FAT/SAT).
No operation until separate site review. Each real test record must contain:
test ID, requirement IDs, procedure revision, rig and instrument configuration,
operator and reviewer, approved conditions, acceptance criterion established
before execution, actual observations and uncertainty, result, deviations,
evidence path, NCR/retest disposition, and signed review date.

A qualified team must define safe methods for no-load/loaded chamber,
fault scenarios and protective shutdown tests; do not deliberately induce
hazardous faults or energize from this plan. No test becomes "passed"
because of a synthetic signal or example report. RD6 acceptance restricts
use to verified conditions. Scientific Q0 begins under separate EBT gate
and does not retroactively establish rig acceptance or a transferable boundary.
