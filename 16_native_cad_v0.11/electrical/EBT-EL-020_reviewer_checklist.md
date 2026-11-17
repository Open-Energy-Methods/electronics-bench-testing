# EBT-EL-020 — KiCad native review and electrical release checklist

**Status:** PRE-DESIGN. The editable KiCad file is a connection-level
research topology with self-embedded symbolic function blocks. It is
NOT a finished circuit board, safe wiring diagram, or electrical approval.
It must be opened in a suitable KiCad version and reviewed by a competent
electrical laboratory engineer before releasing any physical wiring.

## Editor/import review

- [ ] KiCad can open the .kicad_sch without parser warnings.
- [ ] All 15 functional review symbols and 14 nets render legibly on A3.
- [ ] All 35 schematic pins have their intended labels; inspect pin-to-wire
      endpoints and label angle; export KiCad-native netlist and compare
      to EBT-EL-020_net_connections.csv.
- [ ] Run KiCad ERC and save the actual report; don't suppress violations
      merely to obtain a green check.
- [ ] Replace review symbols with real part-specific symbols and actual
      connector pinouts **only after** hardware selection and site review.

## Physical circuit approval

- [ ] Actual PSU model and available isolation/source current limiting.
- [ ] Actual source disconnect S0 and independent stop design; rated
      under real DC interrupt/current/voltage fault cases.
- [ ] F1/F2 correct DC interrupt capacity, protection response, and
      wire gauge/material under fault and sustained current.
- [ ] S1 identified manufacturer part: verified mechanical center OFF,
      break-before-make, DC load breaking, contact welding and misposition
      behavior; ensure that H1 and H2 cannot energize simultaneously.
- [ ] RSH1 actual calibrated shunt (Kelvin sense, resistance vs temperature,
      I2R heating, isolation, overload and protection).
- [ ] V1/V2/VI true differential or appropriately isolated analog inputs
      with checked common-mode ratings; no dangerous chassis/earth
      reference or inadvertent grounds.
- [ ] Fan supply isolation, fan F2/control, actual tach signal compatibility,
      separate fan test and state records.
- [ ] Real T_CASE/T_PLATE/T_SINK/T_AMB sensing chain; grounded thermocouple
      junctions and logger common-mode reviewed, actual sensor locations
      documented, calibration and lag verified.
- [ ] Site approved overtemperature/fault isolation including protective
      disconnection independent of software-controlled limits.
- [ ] Competent facility sign-off, authorized room/trained operator, user SOP,
      expected case derating, actual wiring inspection before any energization.

**Neither 20 W at 25 degC case nor 2.8 W free air is an approved setpoint.**
The diagram does not specify absolute heater power/current/voltage limits.
