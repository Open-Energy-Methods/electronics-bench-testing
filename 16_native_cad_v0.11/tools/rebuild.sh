# EBT CAD 0.11 local generation examples; not a safety approval
# Optional local rebuilding (only with the installed engineering applications)

# OpenSCAD is an editable parametric 3-D CAD project:
openscad -o EBT-MEC-020_direct.stl -D 'adapter=false' mechanical/EBT-MEC-020_assembly.scad
openscad -o EBT-MEC-020_adapter.stl -D 'adapter=true' mechanical/EBT-MEC-020_assembly.scad

# Professional neutral STEP assembly (editable source is CadQuery Python):
python mechanical/EBT-MEC-020_cadquery.py --out build/

# Review drawing is proper R2010 DXF, not a raster image:
python mechanical/EBT-MEC-020_drawing.py --out build/EBT-MEC-020_concept_review.dxf

# Open editable schematic directly in KiCad Schematic Editor:
# electrical/EBT-EL-020.kicad_sch
# (Optional) kicad-cli sch export svg -o build/kicad-svg electrical/EBT-EL-020.kicad_sch
# (Optional) kicad-cli sch erc -o build/EBT-EL-020_ERC.txt electrical/EBT-EL-020.kicad_sch
