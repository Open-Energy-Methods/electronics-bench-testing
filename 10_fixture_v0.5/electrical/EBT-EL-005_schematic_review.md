# EBT-EL-005 — Draft electrical measurement topology

**Connection-level conceptual topology, pending real device/catalog selections, electrical engineering review and site authorization.** The corresponding [SVG schematic](../drawings/EBT-EL-005_measurement_schematic.svg) and [nets](EBT-EL-005_nets.csv) are the intended source of topology review. Do not wire using this draft without a signed controlled drawing.

## Source and load path (one DC source heater at a time)

`PSU_P` → `S0` manual power interrupt → `F1` appropriately rated protective device → `S1` *rated break-before-make, centre-off* source selector → one of two 10 Ω heaters `H1` or `H2` → `ISENSE` approved four-terminal shunt or verified current transducer → `PSU_N`. The unselected heater positive lead is **open**; both heaters may share the current-return bus only after isolated-circuit analysis. Selector failure/stuck/misposition must be assessed. No working mains wires or batteries are part of the test source.

**Separate measurement taps:** `V_H1` across *H1 lead terminals*, `V_H2` across H2. The selected voltage channel times the branch current gives nominal electrical dissipation *in the heater terminals*; exclude shunt/cable/S0/F1 losses. The analog input's common-mode, isolation, bandwidth, reference ground, thermal and lead loading are **unverified**.

**Fan:** separately powered low-voltage circuit with independent protection and fan-off state, not electrically shared with the heater measurement return unless instrument/host design explicitly permits. Record tachometer and actual airflow if available. `PWM%` is not a measured convection coefficient.

## Protective design hold points

- `PSU`: manufacturer/model, voltage/current and isolation/overvoltage/overtemperature limits **TBD**.
- `S0`: actual interrupt rating under DC load, independent reachable emergency off, wiring, signage **TBD**.
- `F1`: fuse/protection type, DC interrupt capability, trip characteristic and rating **TBD**, based on host risk analysis.
- `S1`: switch actual rated DC breaking current, center-off and break-before-make contact design **TBD**.
- `ISENSE`: exact sensor; low-side shunt means possible ground offset. Differential acquisition must not tie node `SHUNT_TOP` to earth inadvertently; dissipated shunt power is separate from heater power.
- `AIN1/AIN2`: true differential/high-common-mode qualified acquisition or isolated channels. No oscilloscope alligator earth clip across arbitrarily floating nodes.
- `TCASE/TSINK/TAMB`: check thermocouple galvanic contact; grounded junctions must not short source rails through logger common.

**No approved voltage, current, power, fuse, wire-gauge, torque or thermal shutdown value is provided.** Do not use the Bourns 20 W at 25 °C *case* rating as a setpoint. Detailed manufacturer mounting, actual case temperature derating and every alternative airflow/heat-loss path must be signed at G2.
