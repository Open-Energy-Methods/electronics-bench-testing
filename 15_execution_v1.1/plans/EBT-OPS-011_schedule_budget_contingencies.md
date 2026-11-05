# EBT-OPS-011 — Dependency-driven schedule, cost controls and fallbacks (WP0–9)

**Planning date:** 5 November 2026. The original master plan's November 2026–May 2027 window is **conditional**, not a promise. User-reported KTH autumn course registration ends 11 January 2027; it does **not** guarantee workshop or powered site access until that date.

## Relative timeboxes anchored to evidence, not arbitrary appointments

| Phase | Work possible without a powered lab | Prerequisite for next physical phase | Timing rule |
|---|---|---|---|
| Now / first working week | accept Student Workshop Canvas invitation/book introduction; inspect facility replies; grade critical prior art; get real-item vendor/fixture and metrology checklist ready | no machining or energization from account registration alone | immediately, no implied actual booking |
| While G2 pending | review exact bill of materials, drafting alternatives, numerical V&V, risk and research gap | signed physical machine permission, separate electrical site approval, actual instrument inventory | duration facility-dependent |
| Once machines authorized | inspect real sink/resistors; get staff feedback on contact/mount; release dimensioned as-built fabrication plan if allowed | task-specific machine approval and reviewed drawing | only after receipt and induction |
| Once energized site authorized | instrument reference checks, reviewed protection, approved local operating limits and SOP | competent signoff on actual test conditions | no universal safe voltage/current/power |
| Only after G2 complete | exploratory Q0 data acquisition, uncertainty characterization, pilot redesign if needed | measured Q0 report and independent review | may need several legitimate remounts/sessions |
| Only after G3 lock | R01 independent QUAL/CAL/HOLD planned campaign and complete raw archive | explicit external timestamp, registered holdout groups and signed protocol | physically measured session times determine duration |
| After G4 | model and statistical evaluation, blind final HOLD once, uncertainty/limitations | actual measured dataset and QA coverage | do not select data by pleasing conclusions |
| After G5 | manuscript, open release, reproducibility and DOI | rights and G6 technical review | only after permitted materials mature |

## Budget strategy (SEK)

Current exact prior preliminary quote: **346.58 SEK excluding VAT** for two Bourns resistor candidates and one Fischer sink at 5 November 2026; it excludes all other BOM lines, shipment, tax and facilities. Historical community space quote **750 SEK starter package** was user-supplied earlier and is *not* a verified live price. All expected additional spend—TIM, mount hardware, guarding, metrology, external references, machine time, replacement devices, publishing—is **TBD**. No purchase order or budget approval has been issued.

**Financial gate:** verify equipment already available under actual site authorization; price exact SKU and alternatives; compute all-in quote including VAT and travel; compare with authorized project capacity; do not buy a measurement system with unknown reference suitability. Freeze only a **preliminary cost forecast** before inspection; procurement is deliberately deferred until physical architecture/site rules are clear.

## Material decision branches

- **No powered lab access:** keep simulated study explicitly computational; consider a computational validation/measurement-design technical report; do not publish synthetic data as physical.
- **Manufacturing facility denies task:** pursue a qualified external maker/fabricator with released drawings; do not drill hypothetical SK92 geometry.
- **Only limited temperature/electrical reference equipment:** narrow claim to observed surface quantities/feasible transients; request a traceable reference or stop physical validation claims.
- **No viable 3-level cooling factor:** document site physics, revise preregistration **before** HOLD using controlled change; don't artificially label two identical cooling states.
- **High spatial/source-site mismatch:** report lack of transfer, revise B3 as position-specific and retain negative data.
- **Excessive mounting variance:** estimate cluster-level variability, improve fixture control or report large uncertainty; don't inflate n by counting timestamps.
- **Insufficient originality:** target open benchmark/methodology or technical report, with direct source evidence.
- **License/data restrictions:** do not publish site calibration certificates/photos/raw data unless expressly allowed; either obtain rights, release independently reproduced permitted outputs, or restrict public claim scope.

## Weekly project control

Review [dependency register](../controls/EBT-EXEC-011_dependencies.csv), actual permissions, engineering risks, open issues, spend, staff decision/ref dates, critical blockers and next real action. Assign only owner = independent researcher until external personnel agree. Use G0–G6 evidence register and CR policy; maintain honest **BLOCKED** even if numerical CI passes.
