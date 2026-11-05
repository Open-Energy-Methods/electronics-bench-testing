# EBT-R01-TP-001 — Draft physical test protocol (not approved for execution)

Document state: **PRELIMINARY / NOT AUTHORISED / NO ENERGISED TESTING**. Revision 0.1, 2026-11-05.

## Test article and rig

- Select a MOSFET with manufacturer datasheet and SOA (safe operating area) covering the proposed current, voltage, pulse duration and junction temperature. Do not use unqualified switching waveforms or assume that junction temperature equals package temperature.
- Separate reference resistive heater for initial rig commissioning; mount using controlled fixture and traceable contact/torque approach where possible.
- Low-voltage isolated laboratory DC source with current limit, external protection, accessible switch-off and an approved bench configuration.
- Directly measure voltage across DUT dissipative path and current with suitable measurement geometry. Compute P(t)=V(t)I(t), not just PSU display output; where waveform variation matters, use synchronized acquisition.
- Record case, heat sink and ambient temperature. Map sensor positions on drawing and state sensor attachment and thermal mass. A thermal camera is a supplemental, emissivity-dependent surface tool, not a direct junction sensor.
- Optional electrical junction-temperature observable must be independently validated before claims about internal junction temperature.

## Facility and safety prerequisites

The host laboratory must allow powered experimentation and give explicit authorization. Student Workshop fabrication facilities may not permit energized circuits. Complete host induction, safety review, PPE and supervision requirements. Maximum input energy, resistor wattage, cable capacity, thermal runaway/short protections and stop thresholds must be specified *after* actual components and instruments are known.

## Proposed pilot stages

| Stage | Objective | Release condition |
|---|---|---|
| Q0 dry inspection | traceable inventory, visual inspection, wiring continuity and polarity, no power | all parts identified, safe schematic reviewed |
| Q1 sensor verification | compare each sensing channel with qualified reference at relevant temperatures | channel corrections, uncertainty budget and valid range defined |
| Q2 resistive baseline | establish electrical-power and thermal response on protected heater | safe thermal limits and energy balance recorded |
| Q3 MOSFET preliminary | controlled safe device dissipative run | voltage/current limits and temperature stop criteria demonstrated |
| Q4 repeatability | independent reassemblies in same baseline condition | repeatability/measurement variance quantified |
| Q5 main matrix | randomized/blocked across cooling/interface conditions | pre-registered holdout preserved, deviations logged |

## Pilot test matrix — provisional only

Factors: three **approved** dissipated-power set points, three airflow/heat-sink regimes, two interface/attachment conditions, three independent assembly replicates (54 candidate runs). Details and sample size will be revised based on a pilot precision analysis, measurement stabilization, and access constraints. Ambient temperature and fan speed are recorded, not assumed constant. No proposed power set point is authorized by this document.

Holdout design: withhold entire airflow/fixture configurations or remounts from model fitting. Never tune model choice or numerical uncertainty coverage on reserved validation runs. Set temporal measurement interval based on measured sensor response time and fastest relevant physical transient. Capture preheat, thermal rise, hold and cool-down and define an objective stabilization criterion before collecting results.

## Metadata for every run

`run_id`, `utc_time`, `operator`, `site_authorization`, `dut_model`, `dut_serial`, `mount_id`, `assembly_sequence`, `interface_material`, `mount_torque`, `heatsink_id`, `fan_pwm`, `ambient_temperature`, `sensor_ids`, `sensor_positions`, `calibration_records`, `sampling_frequency`, `power_limits`, `stop_rules`, `software_revision`, `raw_data_file_sha256`, `observed_deviations`, `acceptance_status`.

## Calibration / measurement assurance

- Verify reference calibrations are current within required ranges; record certificates and correction factors only where permissions allow.
- An unknown multimeter is not a calibration standard. Two agreeing uncalibrated instruments do not create metrological traceability.
- For low-cost replication, clearly declare higher expected uncertainty and do not equate it with the qualified main campaign.

## Data acceptance and exclusions

Establish limits for missing samples, supply saturation, thermal-limit trips, fan malfunction, sensor detachments and ambient excursions in an approved preregistration. Archive *all* runs including aborted tests and deviations, with original unmodified source files. Exclusions must be justified without inspecting desired model outcomes.

## Model quality and paper evaluation

Report power delivery, instrument repeatability, time offset, temperature reference positions, heat-loss assumptions, and uncertainty. Comparisons must specify what is actually measured; do not validate `Tjunction` with case sensor alone. Use blinded/held-out evaluation and prediction intervals.
