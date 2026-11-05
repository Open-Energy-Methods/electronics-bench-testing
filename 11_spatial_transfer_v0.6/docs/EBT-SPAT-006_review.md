# EBT-SPAT-006 — Conditional 2-D plate and apparent-boundary transfer review

**5 November 2026 | Rev. 0.6 | COMPUTATIONAL ONLY | NO FABRICATION OR POWERED TEST APPROVAL**

## Falsifiable engineering question

At the two proposed source coordinates A=(-25,0) mm and B=(+25,0) mm, does the independently qualified apparent boundary remain comparable when the source and/or the sensor are moved? v0.5 proposes near-plate sensor coordinates (-25,-17) and (+25,-17) mm. These are still only design targets.

## Defined model, not measured apparatus

A 100×100×4 mm square plate, conductivity **assumed** 180 W/(m K), satisfies a conservative cell-centred 2-D finite-volume balance of the steady equation:

    -k*t*Laplacian(T_plate - T_air) + g(x,y)*(T_plate - T_air) = q''(x,y)

Insulated lateral edges; positive distributed effective vertical loss g. The assumed g field is not a measured convection coefficient or actual heatsink fin representation. Input is normalized to **1 W for mathematics only; it is NOT a permitted bench power**. TO-220 nominal body 10.1×14.6 mm is used as a **hypothetical heat-input footprint**, not a measured mating/contact face. The alternative 6×6 mm footprint is entirely hypothetical. A nominal bypass fraction simulates some terminal electrical power NOT reaching the plate, with no attempt to identify the real bypass mechanism. Rapp is the *particular plate sensor's* temperature rise divided by *terminal* power, not a universal Rsa.

**Omissions:** actual Fischer extrusion, convection and fin direction, plate/TIM contact, force and screws, package internals/junction, lead convection, thermal radiation, real instrument response, dynamics and timebase. Do not use the outputs as a hardware rating, sensor specification, prospective validation claim or B3 model parameter.

## Executed illustrative cases

| Assumptions | Rapp at A with source A | Rapp at B with source B | Co-moving A/B difference | Fixed sensor A when source moves to B |
|---|---:|---:|---:|---:|
| Uniform g = 60 W m^-2 K^-1 | 1.8619 K/W | 1.8619 K/W | 0% | 17.38% difference |
| Left/right g = 40/100 W m^-2 K^-1 | 1.7310 K/W | 1.5260 K/W | 12.59% | 24.61% difference |
| Asymmetric g, hypothetical 20% plate bypass | 1.3848 K/W | 1.2208 K/W | 12.59% | 24.61% difference |
| Asymmetric g, hypothetical 6×6 mm footprint | 1.7266 K/W | 1.5215 K/W | 12.63% | 24.42% difference |

Rounded from generated JSON. The bypass test reduces reported apparent resistance without changing g: this exposes a confounding heat path, not enhanced cooling. The footprint result is restricted to this assumed plate conductance and loss field.

## Scientific and mechanical decisions

1. **Keep source-site and sensor-site identities distinct.** Record actual coordinates, sensor attachment side (plate versus sink), device footprint, assembly ID, remount, orientation and time for each independent run. Co-moving and fixed-location sensor comparisons are different estimands.
2. Maintain near-A and near-B thermometry, if technically feasible. Simultaneously measuring both when source A or B operates is more informative than a single relocated probe; consider far-plate/actual-sink temperatures only after their surface definition is verified.
3. Before blind validation, preregister a same-source physical reversal A→B and an independent sensor remount. Confounders include source identity, location, fixture conduction, nonuniform airflow and heat bypass. Do not infer unique g(x,y) or a transferable boundary from a good fit.
4. Set an equivalence band and Type A/Type B uncertainty using **real** instrument data and assembly-block variation before looking at held-out data. Individual fast time samples do not represent independent remount replicates.
5. If actual apparent resistance or model errors are nonportable across source locations, flag **FAIL-TRANSFER** and restrict B3 to position-specific or retrospective application. No target validation temperatures may be used to choose its prospective boundary.
6. No fixture release: obtain manufacturer sink extrusion drawing, real mating dimensions, contact resistance strategy, heater ratings/mount torque and site-approved electrical and DAQ protection first.

## Reproducibility

Seven automated tests cover input power conservation, energy rejection, symmetry, bypass linearity, invalid geometry, grid convergence and explicit synthetic classification. Run under the new CI job. Numerical verification **does not close** EBT issues #4, #5, #6 or #9, and it is not evidence of a fabricated or validated rig.
