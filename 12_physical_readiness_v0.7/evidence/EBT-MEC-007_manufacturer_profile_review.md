# EBT-MEC-007 — Reviewed manufacturer-family geometry and evidence boundary

**5 November 2026 | v0.7 | Supplier-source assessment only | NOT A MANUFACTURING DRAWING**

## New verified external evidence

The [Fischer Elektronik SK 92 series profile sheet](https://cdn.soselectronic.com/productdata/43/5c/5f09af37/sk-92-150-sa.pdf) depicts a 100 mm wide and 40 mm high extrusion with **10 mm nominal base thickness**; its length choices include 100 mm. The 2022 document is *family-level profile information*, not a signed as-received inspection of the exact SKU.

The [SK 92 100 SA listing](https://www.tme.eu/en/details/sk_92_100_sa/heatsinks/fischer-elektronik/sk-92-100-sa/) independently identifies a 100 × 100 × 40 mm black-anodized part and quotes base thickness 10 mm. It does not establish surface flatness, hole positions, permissible tap depth, fin taper, surface finish suitability or an isolated electrical contact.

The [Bourns PWR220T-20 Rev 06/25 datasheet](https://www.bourns.com/docs/product-datasheets/pwr220t-20.pdf), p. 2, provides nominal width 10.1 mm, body height 14.6 mm and Ø3.6 mm through-hole. The package drawing has a stepped section. **Do not assume the full 10.1 × 14.6 mm rectangle is a certified flat thermal mating patch.** Its isolated backplate feature does not replace a system-level electrical leakage/grounding assessment. The 20 W rating is specified at 25°C *case*, not a bench setpoint.

## The corrected interpretation of v0.5

The v0.5 preliminary section previously treated the inner heatsink base section as unknown. The **nominal manufacturer-family base thickness is now documented as 10 mm**. This reduces one information gap; it does **not** release any proposed drilling coordinate or permit a powered test.

The v0.5 100 × 100 × 4 mm added plate remains an *assumed optional part*, not a manufacturer-shipped component. It adds a further contact interface and a potentially material transient thermal capacity. Distinguish ambient-side sink base from the optional plate sensor in each report.

## Specific real-world evidence still missing

1. Actual received part identity (SKU/lot), measured fin/base profile, mating face dimensions/roughness and usable mounting side. Fin geometry in the small catalog sketch is not enough for tap/drill planning.
2. Manufacturer or qualified workshop's accepted approach for blind holes, clamp loading and mechanical finish—no released tapping depth, torque or fastener grade exists.
3. Thermal contact interface material/thickness, electrical clearance, leakage and lead-routing review.
4. Sensor adhesive/attachment compatibility, true measurement footprint and whether available surfaces can host A and B thermometers without altering conduction.
5. Actual calibrated or at least reference-verified temperature/electrical instruments and approved facility.

**Review decision:** evaluate DIRECT_TO_SINK_CANDIDATE first because it eliminates an otherwise uncontrolled full-area interposer. The ADAPTER_PLATE_CANDIDATE is retained explicitly as an alternative research condition, not silently treated as part of the heatsink.

**No drawing is to be manufactured, no source powered and no catalog thermal resistance treated as measured boundary.**
