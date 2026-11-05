# EBT-Q0-009 — Cross-branch independent-interface audit (author review)

**Review date: 5 November 2026. Scope:** PR #11 v0.6, PR #12 v0.7,
PR #13 v0.8 against v0.5 \`main\`. This is a **documentation/software
integration review**, not independent academic peer review or a safety
certification.

## Conflicts and reconciled decisions

| ID | Pre-integration discrepancy or failure risk | Final contract | Residual uncertainty |
|---|---|---|---|
| INT-01 | Three branches each appended a different CI job, README and changelog from the same v0.5 ancestor. | All source modules and four baseline jobs retained; single composite workflow and top-level authority index. | Verify combined CI after integration. |
| INT-02 | v0.5 assumed a 4 mm interposer; v0.7 considered direct-to-sink and a nominal 10 mm SK 92 base. | Direct is first design-review candidate; adapter is explicit alternative/control. No part selected for machining. | Actual flat face, surface, fastening, tolerance, TIM, electrical isolation remain unverified. |
| INT-03 | v0.6 assumed uniformly thin 4 mm plate with 2-D effective loss; could be mistaken for actual Fischer sink model. | v0.6 is strictly synthetic counterexample, not structural, thermal or manufacturing verification of v0.7's 10 mm extrusion. | Actual conduction, three-dimensional fin field and bypass unknown. |
| INT-04 | v0.5/v0.7 sensors named near “sink” but might be on added plate. | Source-specific \`temperature_surface=T_PLATE|T_SINK\` in v0.8, plus mandatory physical sensor map. Never silently rename \`T_plate\` to \`T_sink\`. | Sensor attachment/lag/positions require inspection. |
| INT-05 | Q0-TP-002 proposed 12-power/cooling/remount cases, Q0-007 proposed 8-source/site/remount events. | Two alternative pilot screening schemes, not cumulative 20-run mandate, not R01's 54-row test. | G2 power/safety and pilot precision determine executable design. |
| INT-06 | v0.7 G2/G3 record and v0.8 R01 split use different lock fields and dataset-role names. | Explicit 1:1 crosswalk; compare UTC lock instants, protocol SHA-256 and QUAL/CAL/HOLD role IDs. | Blank records invalid by design; external timestamp not software-verified. |
| INT-07 | v0.8 raw file hash might look like physical provenance or pre-registration proof. | SHA-256 is byte-level integrity only; software cannot prove true acquisition, calibration, scope of permission or chronological sealing. | Independent reviewer and trusted external lock remain mandatory. |
| INT-08 | v0.8 stores heater-terminal V/I while v0.6 boundary model assumes plate heat input. | Do not equate electrical terminal \(P=VI\) with all heat entering plate; distinguish heater dissipation and unmodelled parasitic pathways. | Requires actual energy-loss assessment before physical \(R_{\rm app}\). |
| INT-09 | Student Workshop Canvas access and Manufacturing Lab response could be mistaken for lab authority. | Student Workshop invitation only for possible fabrication intro; Manufacturing Lab independent access restricted; ELAB powered authority unverified. | Confirm booking/training, named powered site/supervisor and permission. |
| INT-10 | v0.4 synthetic instrument noise, v0.5 5 Hz target and v0.6 1 W normalized input could harden into physical limits. | **All three remain numerical/planning assumptions**; physical thresholds are blank until site inspection. | Q0 metrology/safety program required. |

## Review checklist

- [x] Preserve master EBT-PMP-001 v1.0 and baseline v0.1 without changing scientific intent.
- [x] Retain source notebooks/models, v0.4 B0–B3 and v0.6 conditional results with honest evidence labels.
- [x] Retain v0.7 geometry/authorization inspection register and v0.8 data/partition code.
- [x] Resolve shared GitHub workflow/docs and specify one current Q0 authority index.
- [x] Programmatically test cross-module record mapping and missing-evidence gates.
- [ ] Physical heatsink identification, manufacturer-approved mounting and real sensor coordinates.
- [ ] Signed workshop machining release and **separate** powered-site permission.
- [ ] Instrument calibration/verification, timebase and sensor-lag measurement.
- [ ] Completed measured Q0 and independently registered R01 HOLD.

**Decision: ACCEPT SOFTWARE/DOCUMENTATION INTEGRATION subject to combined CI.
Maintain G2/G3 HOLD.** This decision cannot be interpreted as fabrication
approval, energized authorization, data qualification or novelty clearance.


## Integration CI correction — timestamp normalization

The first combined CI run exposed three failing integration tests caused
by using a Stockholm `+01:00` timestamp in the **v0.8 split**. This is
not an accepted `EBT-SPLIT-008` format. The corrected contract keeps
that split's strict UTC `Z/+00:00` requirement; it converts a valid
timezone-aware **v0.7 gate** instant to UTC for equality comparison.
A negative test now confirms a local-offset split is rejected. The
original failed CI run is retained in GitHub Actions for auditability.
