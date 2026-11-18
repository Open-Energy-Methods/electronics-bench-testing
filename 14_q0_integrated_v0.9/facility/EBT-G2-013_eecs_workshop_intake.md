# EBT-G2-013 — EECS Student Workshop physical-intake addendum
Date: 2026-11-19. Status: USER-REPORTED GENERAL ACCESS; task-specific authorization, instrument qualification, machining and power HOLD. Independent research, not a KTH research project. This addendum supplements EBT-Q0-009 and EBT-EXEC-011; it does not supersede their safety, data, or scientific controls.

## New evidence
The researcher reports access to the EECS Student Workshop, Department of Electromagnetics and Plasma Physics. The previously recorded appointment was 18 November 2026, 16:00–17:00; attendance, quiz, signed acknowledgement, duration of access and individual machine permissions have not been explicitly verified. Do not infer course completion from general access.
KTH equipment pages reviewed 2026-11-19:
- https://www.kth.se/emp/student-workshop/verkstan/elektronik-1.686912 — bench PSUs, DMMs, oscilloscopes, generators, soldering, microscope and hot-air station; no normal component inventory.
- https://www.kth.se/emp/student-workshop/verkstan/mekanik-1.686913 — CNC/manual milling/turning require supervisor; booking contact Sharvil Joglekar.
- https://www.kth.se/emp/student-workshop/verkstan/cnc-fras-1.686920 — HAAS Mini Mill listed maximum envelope 406×305×254 mm and 6000 rpm; not a verified workholding/travel guarantee.
- https://www.kth.se/emp/student-workshop/regler-och-sakerhet — induction and signed acknowledgement; no lone work, PPE, no work on live circuits, supervisor help when uncertain. Never modify live circuits. Whether a supervised, isolated, guarded, bounded powered experiment is allowed must be expressly determined by facility staff. If prohibited, use separate authorized site (ELAB or equivalent).
- https://www.kth.se/emp/student-workshop/material-1.686906 — published aluminium 70 SEK/kg, filament 0.7 SEK/g; actual stock, scrap and pricing must be confirmed.
- https://www.kth.se/emp/student-workshop/manualer-och-guider-1.686421 — workshop guide index.

Nine researcher-supplied reference PDFs reviewed; do not redistribute PDFs, photos, serial/license keys or proprietary diagrams without rights. LPKF E44 Getting Started Guide (6 Apr 2020), pp. 2–4, 6, 17–20: single/double copper, no solder mask or plated vias; typically 1.5 mm substrate, 35 µm copper; ≥0.3 mm tracks/spacing recommended where practical, local DRC template and inspection. Prusa Guide v2 pp. 1–3, 5 and troubleshooting pp. 1–6: 0.4 mm nozzle, nominal 0.2 mm profile and 20% infill as starting point only. Zortrax guide pp. 1–3 and ABS/repair guides: M200, nominal 0.19 mm layer and 30% general infill, correct profiles, extraction, warping/calibration; no material temperature/creep qualification. CNC setup Program 1007 (Oct 2020), CNC job guide and Swedish NGC quick guide: documented offsets, workholding, simulation, supervised first run. Sample toolpaths/feeds are NOT EBT machining instructions.

## Facility routing decisions
1. Preferred unpowered assembly and metrology intake: EECS Student Workshop. Confirm task scope with staff; separately verify every machine or supervised activity. For a simple mounting fixture, prefer minimal manual operations over CNC if approved; CNC reserved for demonstrable geometry/flatness need.
2. Candidate powered site: same electronics room ONLY if staff explicitly permit proposed method consistent with no-live-work rule. No direct access to exposed live conductors; all wiring changes de-energized; approved guarded arrangement and independent stop; exact permissible electrical/thermal conditions unknown. If declined, separate site; fabrication can proceed independently once released.
3. Keep direct-to-sink candidate (SK 92 100 SA, nominal 100×100×40 mm and 10 mm base) as v0.7 preferred for review. Two candidate PWR220T-20-10R0F 10 Ω resistors. No setpoints, drilling or fastening coordinates inferred. Optional adapter only if actual geometry requires it; document a new heat path and model boundary.
4. No custom PCB on critical path. Start with reviewed protected instrumentation and qualified off-the-shelf connections. Later prototype passive signal/sensor breakout on E44 if needed, with conservative DRC, explicit creepage/clearance, non-plated via wiring and continuity/isolation inspection. Printed supports outside hot zone; check material temperatures, load and deformation independently.
5. Existing v0.9 Q0 sequence remains authoritative. No acquisition, no substitute synthetic dataset, no R01 holdout changes.

## First visit: evidence, not operation
Use companion intake CSV. Record consultation date, instrument manufacturer/model, serial or approved asset reference, electrical limits/ranges, calibration/verification evidence, availability and borrowing conditions. Ask for calibrated thermometry (case, sink, ambient), DAQ/logger with simultaneous timestamps, actual achieved sampling, sensor attachment, fan/airflow equipment, torque tool and dimensional tools. A scope alone cannot establish long-duration synchronized thermal acquisition. Missing references remain unknown. Ask separately for photo/raw-data rights, no publication of restricted records. Inspect parts only once received; record receipt and lot, dimensions and method, contact/fin geometry and feasible mounting. Never photograph or publish people, lab asset identifiers or access credentials without permission.

## Release and acceptance
- A: general access report retained; actual induction evidence and machine permission recorded, staff-reviewed route selected.
- B: actual part receipt and measurement, selected interface and released drawing + reviewed hardware.
- C: exact powered-site permission and verified instrument chain, site-approved protected schematic/SOP and limits. No automatic GO from this checklist.
- D: canonical G2 record reviewed by named competent humans; only then choose sequential Q0 pilot per Q0-009. Independent remounts and Q0_PILOT tag; QUAL/CAL/HOLD split only for preregistered R01. All missing/aborted runs retained.

No facility consent, procurement, calibration, manufacturing, physical measurement, or safety approval is claimed. Existing G2 23-check inspection register, Q0-010 receipts and instrument manifests, v0.8 data contract and G2/G3 gate logic remain controlling.
