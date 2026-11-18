# M02 / M10 — Manufacturing process and digital quality demonstrator

Use the M01 coupon as the first product with controlled design-to-production
flow. Select only meaningful supervised tasks. Turning: locator/spacer or
separate coupon. Milling/CNC: carrier or dimensional artefact. Drill/cutting:
approved bracket. Laser: approved flat pattern/cool-zone mockup, measured kerf
and fit. FDM: separate unpowered fit prototype, check anisotropy and dimensional
variation. Woodworking: training mockup/coupon, NOT a hot-zone structure.

## Production engineering
Product breakdown -> make/buy/borrow -> drawing and BOM -> process plan with
equipment and safe setup reviewed by shop -> inspection plan -> actual first
article -> deviation review -> repeat lot if justified. Ask for actual machine
capabilities and use the shop's postprocessor/official training. No generic
feeds/speeds/G-code or permission assumed. Record actual operator time,
machine time, setup, changeover, inspection, rework, scrap and purchased costs.
Report first-pass yield as accepted first-pass units / attempted units,
with denominators and actual observed counts. For small learning lots, report
individual measurements and uncertainty, not Cp/Cpk or certified machine
capability. Capability metrics require stable process, adequate sampling and
appropriate distribution/model and measurement-system quality.

## Digital thread
Part ID and revision; material lot; as-designed CAD and released drawing;
operation ID; machine and approved method revision; inspection instrument,
reference and uncertainty; feature ID; observed value; disposition; NCR;
rework instruction and acceptance authority; corresponding rig assembly.
A new part revision must not silently change a locked EBT configuration.
Maintain nonconformance and engineering-change records; corrections are
traceable, not erased. Protect private information and facility rights.
