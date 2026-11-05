# EBT-MEC-005 — Mechanical review record, Rev. 0.5

**Technical status: CONCEPT DRAWING, NOT A MANUFACTURING RELEASE.** The generated DXF is **editable geometry** for reviewing clearance and instrumentation positions, not an inspection-passed production drawing.

## Evidence-backed input dimensions

- Bourns PWR220T-20 nominal package: 10.1 mm body width; 14.6 mm body height; 4.0 mm nominal depth; Ø3.6 mm package through-hole; 5.08 mm terminal pitch. The manufacturer drawing gives general ±0.38 mm dimensional tolerance unless otherwise noted. Original datasheet Rev. 06/25, page 2: https://www.bourns.com/docs/product-datasheets/pwr220t-20.pdf
- Fischer SK 92 100 SA catalog external width × length × height: 100 × 100 × 40 mm. **This does not certify a drillable 100 × 100 mm flat area on the underside.** Source: https://se.farnell.com/fischer-elektronik/sk-92-100-sa/heat-sink-100mm-1-4-c-w/dp/4621580

## Proposed review coordinate system

- Origin plate horizontal centre (0,0), +X right and +Y up from plan view.
- Provisional plate envelope ±50 mm square, 4 mm thickness. Not specified material grade or tolerance.
- Two device body centres: D1=(-25,0), D2=(+25,0). Each has a nominal 10.1×14.6 mm rectangle. Package-hole centres at (-25,+4.8) and (+25,+4.8) because 14.6/2−2.5=4.8 mm. **Do not automatically drill/tap these coordinates.** Actual hole-to-mating geometry depends on package, mount direction, mechanical clamp, underside plate face and cable exit.
- Proposed sensor **placement targets only**: T-CASE1=(-25,-3), T-CASE2=(+25,-3) on package faces; T-PLATE1=(-25,-17), T-PLATE2=(+25,-17) on plate/near sink; T-PLATE-FAR=(0,+32). Ambient sensor is **not on the plate**.
- Proposed 20×30 mm keep-out each device, conceptual. Must not be interpreted as exact clamp clearance.

## Remaining design blockers

1. Confirm actual flat base of sink, fin location, base thickness, surface roughness, machine drilling allowance and manufacturer's thermal assumptions.
2. Select whether mounting through an intermediate plate is scientifically acceptable; the extra TIM/contact resistance may defeat the intended boundary identification. Design a direct-sink comparison to quantify this or remove plate.
3. Define profile-specific and package-specific fasteners, calibrated torque, clip geometry, electrical isolation and force distribution. No torque value is yet approved.
4. Obtain exact sensor bead and adhesive/pad geometry, strain relief, routing and per-channel temperature lag.
5. Draw a mechanical section with true stack dimensions once real heat sink/screw data exist; current section only has published external dimensions and explicitly assumed adapter-plate thickness.
6. Verify air path, fan stand-off/guard and fan mounting with a separate drawing. Fan placement is not fixed by v0.5.
7. Address removal/reinstallation damage and **independent assembly ID** and mount-history requirements.

**Manufacturing release checklist:** ☐ approved vendor parts ☐ confirmed heatsink cross-section ☐ measured actual parts ☐ hole dimensions/tolerances ☐ defined joining force/torque ☐ sensor fixation validation ☐ isolation/clearances ☐ fixture heat-bypass assessment ☐ machining permission ☐ issue-signed release.
