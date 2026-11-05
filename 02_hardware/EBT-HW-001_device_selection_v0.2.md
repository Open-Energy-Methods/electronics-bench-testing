# EBT-HW-001 · Device and heater selection review (v0.2)

**Status:** candidate design, NOT a purchase order, authorized electrical test, or final DUT selection. 2026-11-05. Programme baseline: EBT-PMP-001 v1.0.

## Decision

Use a **datasheet-defined TO-220-compatible resistive reference heater** for EBT-Q0. Keep the semiconductor device as a separate EBT-R01 **Gate G3** selection. A resistor permits direct control and measurement of dissipated heat without confusing MOSFET switching losses or deliberate DC linear-mode stresses with thermal contact resistance. It is a *reference-heater assembly*, not a semiconductor junction and not an interchangeable validation target for all internal device thermal mechanisms.

## Candidate reference heaters (manufacturer documentation)

**H-01: Bourns PWR220T-20 family**, provisional 10 Ω / ±1% option, ordering example `PWR220T-20-10R0F` (availability and exact suffix not yet verified). Thick-film TO-220 form, insulated backplate; quoted **20 W at 25 °C CASE** and nominal **6.5 °C/W internal thermal resistance**. Datasheet lists case-temperature derating and 10 Ω as a standard value. Manufacturer sources:
- https://www.bourns.com/products/resistors/details/high-power-resistors/pwr220t-20__
- https://www.bourns.com/docs/product-datasheets/pwr220t-20.pdf
- https://www.bourns.com/products/resistors/high-power-resistors

**H-02: Vishay Sfernice LTO 30 family**, nominal 10 Ω option, precise part number TBD. Thick-film TO-220-style, ceramic direct mounting. Published **30 W at 25 °C case when heatsink-mounted**; specified torque in manufacturer's datasheet: **1 N·m** for this device family, which must not be transferred to the Bourns part without checking its mounting guidance. Sources:
- https://www.vishay.com/en/product/50049/
- https://www.vishay.com/docs/50049/lto30.pdf

**Selection note:** Bourns gives a convenient isolated mounting plate and a thermal-resistance specification, but must be verified for selected mechanical stack and heatsink. A published 20 W or 30 W rating does **not** authorize operation at that power in air or on an arbitrary heatsink. The Bourns product family overview indicates only ~2–3.5 W in free air for related configurations, with product-specific conditions. All setpoints shall be determined from the actual manufacturer's derating curve, thermal conditions, measured component resistance, available heat sink, protective limits and host-lab approval.

## Illustrative calculations, NOT pilot setpoints

For an **ideal** 10 Ω resistor, `P=V²/R`, `I=V/R`; 2 W corresponds to approximately 4.47 V and 0.447 A, and 5 W to approximately 7.07 V and 0.707 A. These figures are for engineering sizing only and do not establish safety in free air or under a particular fixture. Verify true resistance at operating temperature; acquire synchronous `V_heater(t)` and `I_heater(t)`; power delivered to wiring or a separate control component is **not** heater dissipation.

## Why MOSFETs are not the Q0 heat source

A low-RDS(on) MOSFET driven fully on typically develops low conduction heat unless substantial current flows. Intentionally using its **linear region** to generate controllable watts can trigger localized thermal instability even when an overall power estimate seems safe. Manufacturer guidance:
- Infineon, *Designing with power MOSFETs*, safe-operating-area and thermal-stability sections: https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf
- Nexperia, AN50006, *Power MOSFETs in linear mode*: https://assets.nexperia.com/documents/application-note/AN50006.pdf

**Reject any MOSFET for linear-dissipation experimentation until** the exact part's DC/pulsed SOA, case derating, linear-mode thermal-stability guidance, gate-drive control, protections, mounting, and temperature-estimation approach have been technically reviewed. Ratings such as `79 W (Tcase)` or a high absolute-current rating do NOT establish a safe DC linear-mode operating point. An attractive older part (FQP30N06L) is marked obsolete by DigiKey as of this screening, so it is not selected.

## Purchase-release gate

1. Facility confirms **powered low-voltage experiments** are allowed; fabrication workshops may forbid them.
2. Verify exact orderable part, distributor availability, price, and manufacturer revision.
3. Establish mechanical dimensional stack, screw/insulator, torque and interface; make no assumptions across heater families.
4. Obtain independently verified electrical limits and temperature stop conditions for **every** proposed configuration, including loss of airflow.
5. Record supply current-limit, interruption method, fuse/lead derating, wiring, grounding and human supervision.
6. Place order **only after** checking existing equipment and current budget.

## Scientific boundary

Q0 measured quantities are `T_package_surface`, `T_sink`, `T_ambient`, and `P_heater` with their uncertainties. Internal film temperature is neither a directly observed MOSFET junction nor a calibrated reference. Do not infer MOSFET junction thermal resistance from heater measurements.
