# EBT-Q0-TP-002 · Pre-pilot and acquisition plan v0.2

**Status:** PRELIMINARY / UNPOWERED / NOT SITE-AUTHORIZED. Complements `qualification_protocol_draft.md`. Neither this plan nor the accompanying software permits a powered test.

## Scientific role

Qualify the *measurement method and fixture* before EBT-R01 confirmatory device work. Determine real temperature noise, response speed, baseline drift, mounting repeatability and whether a declared cooling boundary is usable for prospective model predictions.

## Screening design (not yet final)

Pilot envelope: `2 power placeholders × 2 cooling labels × 3 independent assembly/re-mount blocks = 12 candidate runs`.

- Power levels **P1/P2 = TBD in watts**, chosen only after the exact heater, cooling, case-temperature derating, site approval and supplies are verified.
- Cooling **NAT** = passive condition on the *approved defined fixture*; **FAN** = fixture with separately documented fan and measurement of fan behaviour. Not permission to operate a heater without a heatsink.
- Blocks A01/A02/A03 are **distinct physical disassembly/reassembly events**, not three consecutive recordings.
- Within each block, conditions are shuffled reproducibly, but each must return to a predeclared thermal baseline. Randomization may be constrained by setup feasibility; deviations are documented.
- The pilot is **not** the 54-run confirmatory study and is not used as its statistical validation holdout.
- The pilot may be reduced or redesigned after safety and precision reviews.

`python scripts/make_pilot_plan.py --out 03_campaigns/EBT-Q0/pilot_run_plan_v0.2.csv` generates a *planning* matrix without any power in W or device voltage. Do not record executed runs using the planning IDs until released under G2.

## Preflight gate checklist

| Gate item | Required evidence |
|---|---|
| Facility | Active staff-authorized electrical-test permission, site rules and introduction |
| Electrical | Actual approved schematic, independent stop, current limit, verified protection, conductor/shunt ratings, grounding review |
| Mechanical | Drawing, mount/torque instructions, thermal interface control, guarded contact surfaces |
| DUT | Exact traceable part, datasheet revision, ambient/case derating, proposed setpoint bounds |
| Temperature | Sensor reference evidence, channel map, time response and placement uncertainties |
| Electrical metrology | V and I measurement chain, working ranges, reference suitability and power uncertainties |
| DAQ | File paths, clock synchronization, metadata, quality flags, raw immutability, checksum and failed-acquisition behavior |
| Lab sign-off | Approved operating instructions, supervision and shutdown plan |

A missing critical item is **NO-GO**. Never substitute two agreeing uncalibrated meters for a traceable reference.

## Data capture requirements

Raw data are time-indexed **SI-unit CSV** with UTC timestamps or elapsed seconds and the separate run metadata manifest:
`run_id, utc_start, assembly_id, fixture_id, cooling_label, power_label, approved_power_W, heater_part, heater_lot, measured_R_ohm, v_probe_id, i_probe_id, thermometry_ids, sensor_positions_drawing, reference_evidence, ambient_sensor_id, fan_measurement_id, timebase_id, code_commit, site_permission, abort_flag, deviations, raw_sha256`.

No measurements have been made; templates are *proposed schemas*. Do not fill unobserved values with zeros.

## Quality and uncertainty decisions required from pilot

- Determine missing-sample maximum from achievable acquisition reliability.
- Determine timebase and sensor lag relative to measured heating/cooling transient.
- Establish ambient drift and power-stability limits from justified metrological and physical budgets.
- Assess uncertainty in voltage, current, case temperature, sink temperature, ambient, placement and complete remount.
- Define a thermal stabilization algorithm, baseline return criterion and allowed wait time *before* confirmatory campaign.
- Record aborted/over-limit runs in immutable raw archive with reasons and separate eligibility flags.

## Candidate analysis equation (not a validation result)

At a specified steady-state condition `R_th,sink-to-air,apparent=(T_sink−T_amb)/P_heater`. This quantity is sensor-location-specific, includes non-convective heat paths and has uncertainty. Do not equate it to a uniquely observed convection coefficient or use prospective holdout data to estimate it.

## Acceptance and stop decisions

There is no generic fixed **safe wattage**, temperature, allowed hot-surface exposure, current limit, stabilization time or repeatability target in this draft. Set these from the actual device, site and pilot, and obtain signoff before physical execution. Any unexpected rise, limit trip, supply anomaly, cable heating, sensor loss, fan failure or responsible-staff instruction leads to immediate controlled shutdown per the site-approved SOP.

**Evidence needed to enter EBT-R01:** approved Q0 report, accepted equipment/uncertainty record, qualified pilot dataset, justifiable run count and physically independent boundary characterization.
