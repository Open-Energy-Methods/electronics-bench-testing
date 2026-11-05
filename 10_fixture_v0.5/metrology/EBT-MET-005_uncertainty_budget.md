# EBT-MET-005 — Measurement, timebase and uncertainty design (Rev 0.5)

**NO REAL UNCERTAINTY ESTIMATES EXIST**: the v0.4 synthetic 0.07 °C and 1% power assumptions are numerical, not specifications achieved by hardware. This file gives equations and evidence needed for an actual budget.

## 1. Trace the two electric measurements

Heater electrical dissipated power: \(P(t)=V_{H}(t)I_H(t)\), voltage sensed **across the actual heater terminals**, current in the same branch. For a time-aligned point, under first-order uncertainty propagation:

\[u^2(P)=I^2u^2(V)+V^2u^2(I)+2VI\,\mathrm{Cov}(V,I).\]

Independently characterize lead, fuse, shunt, relay, amplifier and terminal losses **outside the heater**. If `I` is obtained by `V_shunt/R_shunt`, include shunt reference resistance and its heating/temperature coefficient. Check measurement time offsets and bandwidth. Unknown correlation is not automatically zero.

## 2. Apparent resistance is a sensor-defined aggregate

\[R_{app}=\Delta T/P=(T_{plate}-T_{amb})/P.\]

\[u^2(\Delta T)=u^2(T_{plate})+u^2(T_{amb})-2\,\mathrm{Cov}(T_{plate},T_{amb}),\]

\[u^2(R_{app}) = u^2(\Delta T)/P^2 + (\Delta T)^2u^2(P)/P^4 - 2\Delta T\,\mathrm{Cov}(\Delta T,P)/P^3.\]

The plateau mean's standard uncertainty cannot assume each 5 Hz sample is independent: autocorrelation and baseline drift require effective sample-size/blocked estimation. Additional Type B terms: sensor contact, placement, calibration/ref, logger cold junction compensation, fan variation, ambient radiation, lead/fixture loss and sink gradients. General traceability needs an actual reference chain and any relevant calibration documents.

## 3. Time response and sampling

The 4.84-second mode is an **assumed synthetic** fastest mode; measured finite-body modes may be faster or slower. A provisional planning target is **at least 5 Hz synchronous logging** on package/sink channels, with verified sensor time-constant and analog filtering appropriate to that mode. At 5 Hz ~24 samples/mode, but sampling alone does not bypass thermocouple attachment lag or anti-aliasing concerns. **If measured sensor 63% step time is of the same order as the mode**, no meaningful fast-mode identification should be claimed. Choose actual rate from pilot and report effective uncertainty/lag; higher rate can degrade cold-junction noise on some DAQ modules.

Supplier warning: NI notes that ordinary wide-range analog inputs are unsuitable for µV-level raw thermocouple measurement; use qualified temperature channels with cold-junction compensation and actual configured scan speed. NI-9213 16-channel example supports high-speed configurations up to nominal 75 S/s all-channel versus 1 S/s high-resolution mode, but its higher speed comes with a different uncertainty budget; no lab possession is implied. Sources: https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000x5LbCAI&l=en-US and https://download.ni.com/support/manuals/374916a_02.pdf.

## 4. Gate Q0 measured evidence sheet

Record **instrument model and serial**, calibration/verification provenance, ambient and case/sink sensor type, mounting and repositioning, physical reference, as-found offsets, usable range, logged sampling interval/jitter, 90% rise lag, thermal-gradient effects and any missing sample. No fitted uncertainty interval may be labelled 95% physical coverage without actual replicate coverage evidence.

## 5. Recommended verification tests (NOT conducted)

- No-power zero and stability drift, including electrical reference readings.
- Two temperature references covering intended range (site-approved method); assess both systematic and repeated error.
- Controlled, bounded electrical input with a verified reference branch to cross-check voltage-current product; actual values chosen only by authorized lab.
- Temperature sensor relocation/rebonding sensitivity, heater-site A versus B, ambient plume contamination.
- Synchronization check for rapidly varying logged heater power; preservation of raw timestamps and abort flags.

**Do not adopt the v0.4 synthetic noise numbers as a laboratory capability claim.**
