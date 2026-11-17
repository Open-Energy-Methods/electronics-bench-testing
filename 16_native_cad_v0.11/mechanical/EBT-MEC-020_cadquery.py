"""EBT-MEC-020: parametric editable STEP assembly generator (CadQuery 2.x).

Manufacturer nominal sink envelope 100x100x40 and nominal base 10mm.
Fin pitch/thickness, heater body thickness/contacts and optional plate geometry
are REPRESENTATIONAL NOT MANUFACTURING RELEASES. No holes/torques/current limits.
"""
from pathlib import Path
import argparse
import cadquery as cq

SINK_X=SINK_Y=100.0
SINK_TOTAL_Z=40.0
SINK_BASE_Z=10.0
SURROGATE_FIN_N=11
SURROGATE_FIN_THICKNESS=2.2
PLATE_Z=4.0  # optional, not procured
HEATER_FACE_X=10.1
HEATER_FACE_Y=14.6
HEATER_BODY_Z=4.0  # invented clearance surrogate
HEATER_SITES_X=(-25.,25.)

def block(x,y,z,center):
    return cq.Workplane("XY").box(x,y,z).translate(center).val()

def assembly(adapter=False):
    assy=cq.Assembly(name="EBT-MEC-020_ADAPTER" if adapter else "EBT-MEC-020_DIRECT")
    assy.add(block(100,100,SINK_BASE_Z,(0,0,5)),name="sink_nominal_base",
             color=cq.Color(.42,.51,.57))
    for i in range(SURROGATE_FIN_N):
        x=-50+(i+.5)*100/SURROGATE_FIN_N
        assy.add(block(SURROGATE_FIN_THICKNESS,100,30,(x,0,25)),
                 name=f"fin_SURROGATE_{i+1:02d}",color=cq.Color(.42,.51,.57))
    if adapter:
        assy.add(block(100,100,PLATE_Z,(0,0,-2)),
                 name="plate_OPTIONAL_ASSUMED",color=cq.Color(.83,.54,.29))
    z=-PLATE_Z-HEATER_BODY_Z/2 if adapter else -HEATER_BODY_Z/2
    for i,x in enumerate(HEATER_SITES_X,1):
        assy.add(block(HEATER_FACE_X,HEATER_FACE_Y,HEATER_BODY_Z,(x,0,z)),
                 name=f"heater_site_{i}_NOT_SIMULTANEOUS",color=cq.Color(.18,.20,.23))
    return assy

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out",default=".",type=Path)
    out=p.parse_args().out;out.mkdir(parents=True,exist_ok=True)
    for adapter in (False,True):
        name="EBT-MEC-020_adapter_OPTIONAL.step" if adapter else "EBT-MEC-020_direct_CONCEPT.step"
        assembly(adapter).save(str(out/name))
        print(f"Created {out/name} - NOT FOR MANUFACTURE")

if __name__=="__main__":main()
