# EBT-Q0-010 — Real hardware intake and unpowered inspection

**Issued:** 5 November 2026. **Status:** catalog verified; physical receipt and instruments NOT inspected. **DO NOT MACHINE OR ENERGIZE.** This is a supplement to the [v0.9 Q0 authority](../README.md), not a new physical protocol.

## Exact reference components

| ID | Catalog specification | What it DOES NOT verify |
|---|---|---|
| HSK-001 Fischer SK 92 100 SA | Nominal 100 × 100 × 40 mm black-anodized sink; 10 mm base | Actual flat face, tapping depth, tolerances, allowed mounting pressure or airflow resistance |
| HEAT-001 and HEAT-002 Bourns PWR220T-20-10R0F | 10 Ω ±1% TO-220 resistor; family 20 W at **25°C case** and 6.5 K/W internal element-to-case | Real mounting contact, actual heater dissipation inside plate, safe operating power or electrical insulation |
| Bourns PWR220T-20 family | Manufacturer application note gives **2.8 W without heatsink** | Not an approved experimental power setting |

**Catalog Rth conflict:** For the exact SK 92 100 SA, public distributor listings quote *different* nominal cooling figures: Farnell **1.4 K/W**, TME **2.15 K/W** and DigiKey **1.25 K/W**. Do not treat these as directly comparable tests, average them, or assume any is an experimentally qualified boundary. The test method, airflow and orientation require verification.

**Primary sources:** 
- Fischer exact SKU datasheet: https://www.fischerelektronik.de/web_fischer/en_GB/VA/SK92100SA/datasheet.xhtml
- Farnell exact SK 92 SKU: https://se.farnell.com/fischer-elektronik/sk-92-100-sa/heat-sink-100mm-1-4-c-w/dp/4621580
- TME exact SK 92 SKU: https://www.tme.eu/en/details/sk_92_100_sa/heatsinks/fischer-elektronik/sk-92-100-sa/
- DigiKey SK 92 SKU: https://www.digikey.com/en/products/detail/fischer-elektronik/SK-92-100-SA/25835076
- Bourns series datasheet: https://www.bourns.com/docs/product-datasheets/pwr220t-20.pdf
- Bourns thermal management note (Oct 2025): https://bourns.com/docs/technical-documents/technical-library/fixed-resistors/application-notes/bourns_considerations_for_effective_resistor_thermal_management_appnote.pdf?sfvrsn=134229f6_11
- Exact 10R0F: https://www.digikey.se/en/products/detail/bourns-inc/PWR220T-20-10R0F/2192706

## FIRST REQUIRED PHYSICAL ACTIONS — only after receiving hardware

1. Assign distinct receipt IDs HSK-001 / HEAT-001 / HEAT-002; record original order and delivery record, actual device marking, batch and raw photographs with SHA-256. **Do not substitute catalog images.**
2. Have a trained workshop reviewer inspect the as-received SK92 and record measured length, width, height, base thickness and a *flatness/mountability* observation. No manufacturing tolerances or hole-depth values are released from the catalog.
3. Inspect each heater's leads, body and intended heat-transfer face for damage. Use a **disconnected, unpowered** part. Record the actual source-side mounting/insulation plan, not a vendor photo.
4. If suitable calibrated/reference-verified DMM equipment exists, measure the individual *unpowered* terminal resistance and record DMM serial, lead compensation, temperature and expanded measurement uncertainty. A 10 Ω ±1% catalog tolerance is not proof that an unreferenced DMM reading is valid.
5. Fill the two machine-readable intake templates under `inspection/`. They are deliberately **blank** and are not simulated observations.
6. Separately obtain electrical laboratory site permission and inspect PSU, branch-current and terminal-voltage measurement, thermometry references, common-mode/grounding, actual sampling lag and source interruption. Only qualified site staff may approve protection values and operating limits.

## Readiness as checked on 5 November 2026

- Student Workshop Canvas invitation: **issued**; introduction/machine permission not verified.
- Manufacturing Lab: independent activities restricted by departmental policy; **not an available workshop**.
- ELAB: email inquiry sent 4 November; **no authorization reply found**.
- Part receipt and instrument inspection: **none evidenced**.
- G2 machine release, electrical operating envelope and physical Q0: **HOLD**.

An actual inspection can be reported as evidence only once signed/traceable
records, genuine reference documents, and real part photos are provided.
Passing JSON structure checks or catalog evidence never grants machine or
power authorization. No purchase or booking was made in this update.
