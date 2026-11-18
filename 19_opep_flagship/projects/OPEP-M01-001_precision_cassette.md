# M01 — Precision cassette and locating demonstrator
RD0 concept specification; no released drawing or machine instruction.

## Engineering question
How much of measured fixture repositioning variation comes from the
location scheme, attachment, operator and measurement system? A removable
cassette should provide repeatable geometry independent of its applied
clamping/thermal interface. Compare a nominal unlocated mounting to
a 3-2-1 constrained locating concept with separate clamping. Ensure thermal
expansion and overconstraint are considered; no force/clamp values chosen.

## First practical work
1. Obtain actual dimensional equipment range/resolution, reference artefacts
   and approved machine/material scope. Inspect stock and standard locators.
2. Design a small training coupon (author-proposed envelope 60 x 40 x 10 mm,
   not final cassette size or machining specification). Choose actual material
   and features with staff. Proposed features: reference planar faces,
   one locating feature, one relief/slot and edge treatment, as appropriate.
   Derive functional dimensions separately from the purchased hardware.
3. Model in real CAD using datums and parameterized features. Compare
   relevant fits and locate without overconstraint. Create drawing and
   inspection plan after actual requirements and measurement resolution.
   Retain native CAD, review PDF, STEP, CAM and revision history.
4. With staff-approved task/process plan, manufacture coupon. Record actual
   process sequence, machine/tool IDs, materials, setup time, actual cycle
   time and dimensions. Keep raw measurements with uncertainty.
5. Establish measurement-system repeatability first, then investigate
   independent removal/reinstallation variation using approved unpowered
   testing. Candidate pilot: three identified artefacts, three repeated
   readings per artefact, one operator, randomized measurement order.
   This is a repeatability screening design only: not a full Gage R&R,
   process capability, or independent-remount study. For later multiple
   consenting operators and independent mounting events use appropriate
   variance-component design; don't count samples as independent mounts.
6. Compare repositioning displacement to the actual sensor-location
   error allocation needed by the relevant module. If precision inadequate,
   redesign before releasing the cassette.

## Required reporting
Tolerances and inspection method must be accepted before production; no
tight tolerance chosen by guess. Document datum A/B/C and functional
critical-to-quality feature dimensions, measured uncertainty and explicit
decision rule. The accompanying Python tool implements a simple conservative
interval screen and pooled within-part repeatability, not a normative
implementation of ISO 14253 or an accredited measurement service.
All sample calculations are synthetic unit tests, not physical results.
