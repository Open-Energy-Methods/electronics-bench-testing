"""RD0 spatial reservation model, NOT a manufacturing release.
CadQuery/OpenCascade solids, mm. All dimensions are author-proposed layout
reservations; fit, profiles, guards, fasteners and load capacity unverified.
"""
from pathlib import Path
import argparse
import cadquery as cq
import json

# x, y, z, dx, dy, dz: lower-left corner and envelope size in mm
DOCK = (600, 450, 400)
CELL = (300, 250, 160)
# Separate removable carrier; actual profile sections and parts are not selected.
FRAME = [
    ('base_front', (0,0,0,600,30,30)), ('base_rear',(0,420,0,600,30,30)),
    ('base_left',(0,30,0,30,390,30)), ('base_right',(570,30,0,30,390,30)),
    ('post_FL',(0,0,30,30,30,340)), ('post_FR',(570,0,30,30,30,340)),
    ('post_RL',(0,420,30,30,30,340)), ('post_RR',(570,420,30,30,30,340)),
    ('top_front',(0,0,370,600,30,30)), ('top_rear',(0,420,370,600,30,30)),
    ('top_left',(0,30,370,30,390,30)), ('top_right',(570,30,370,30,390,30)),
    ('deck_envelope',(30,30,30,540,390,10)),
    ('rear_utility_panel_reservation',(350,390,40,220,30,300)),
]
CARRIER = [
    ('cassette_floor_reservation',(0,0,0,300,250,8)),
    ('DUT_sink_catalog_envelope',(100,75,8,100,100,40)),
    ('DUT_mount_interface_reservation',(100,75,48,100,100,12)),
    ('optional_duct_reservation',(0,75,8,100,100,100)),
    ('sensor_support_reservation',(95,10,8,110,10,125)),
    ('harness_interface_reservation',(240,10,8,40,40,50)),
]
# This is a spatial partition, not a final cable, guard or duct geometry.
UTILITIES=[('external_DAQ_patch_panel_reservation',(375,315,40,170,60,120)),
           ('external_control_panel_reservation',(375,75,40,170,200,100))]
COLORS={'frame':(.55,.60,.64),'carrier':(.68,.73,.77),'DUT':(.15,.19,.23),
        'air':(.22,.56,.69),'sensor':(.85,.59,.20),'utility':(.31,.38,.45)}

def box(v):
    x,y,z,dx,dy,dz=v
    return cq.Workplane('XY').box(dx,dy,dz,centered=(False,False,False)).translate((x,y,z)).val()

def translated(v,origin):
    return tuple(v[i]+origin[i] for i in range(3))+v[3:]

def carrier_parts(forced=True):
    return [(n,v) for n,v in CARRIER if forced or n!='optional_duct_reservation']

def solid_check(parts, bounds):
    items=[(n,box(v)) for n,v in parts]
    for n,s in items:
        b=s.BoundingBox()
        assert s.isValid() and s.Volume()>0, n
        assert min(b.xmin,b.ymin,b.zmin)>=-1e-6, n
        assert b.xmax<=bounds[0]+1e-6 and b.ymax<=bounds[1]+1e-6 and b.zmax<=bounds[2]+1e-6,n
    largest=0.0
    for i,(a,s) in enumerate(items):
        for b,t in items[i+1:]:
            # Faces may touch; positive-volume penetration is not permitted.
            v=s.intersect(t).Volume()
            largest=max(largest,v)
            assert v<1e-6, (a,b,v)
    return {'solid_count':len(items),'max_positive_overlap_mm3':largest,
            'reservation_bounds_mm':bounds,'status':'RD0_GEOMETRY_ONLY'}

def color(n):
    if n.startswith('DUT'):return COLORS['DUT']
    if 'duct' in n:return COLORS['air']
    if 'sensor' in n or 'harness' in n:return COLORS['sensor']
    if 'panel' in n:return COLORS['utility']
    if 'cassette' in n:return COLORS['carrier']
    return COLORS['frame']

def export(parts, name, out):
    assy=cq.Assembly(name=name)
    for n,v in parts:assy.add(box(v),name=n,color=cq.Color(*color(n)))
    assy.save(str(out/(name+'.step')))

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=Path('.'));a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    results={}
    for forced in (False,True):
        label='FORCED' if forced else 'NAT'
        cell=carrier_parts(forced)
        dock=FRAME+UTILITIES+[(n,translated(v,(40,100,40))) for n,v in cell]
        for name,parts,bounds in [('RIG200_'+label+'_CELL_RD0',cell,CELL),('RIG100_'+label+'_DOCK_RD0',dock,DOCK)]:
            results[name]=solid_check(parts,bounds);export(parts,name,a.out)
    (a.out/'geometry_audit.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
if __name__=='__main__':main()
