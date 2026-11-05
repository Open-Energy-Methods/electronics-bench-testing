"""Execute deliberately conditional plate-transfer sensitivity. NO lab data."""
from __future__ import annotations
import json
from pathlib import Path
from spatial_plate import Plate, Source, loss_field, inspect

POSITIONS={"A_near_plate":(-.025,-.017),"B_near_plate":(.025,-.017),"far_plate":(0,.032)}

def make_results():
    p=Plate()
    scenarios=[
        ("symmetric_effective_loss",60.,60.,1.,.0101,.0146),
        ("asymmetric_effective_loss",40.,100.,1.,.0101,.0146),
        ("asymmetric_with_20pct_plate_bypass",40.,100.,.8,.0101,.0146),
        ("asymmetric_narrower_heat_footprint",40.,100.,1.,.006,.006),
    ]
    results=[]
    for name,gl,gr,f,w,h in scenarios:
        g=loss_field(p,gl,gr)
        obs={site:inspect(p,Source(x_m=x,width_m=w,height_m=h,plate_fraction=f),g,POSITIONS)
             for site,x in (("A",-.025),("B",.025))}
        aa=obs["A"]["apparent_r_k_w_by_sensor"]["A_near_plate"]
        bb=obs["B"]["apparent_r_k_w_by_sensor"]["B_near_plate"]
        ba=obs["B"]["apparent_r_k_w_by_sensor"]["A_near_plate"]
        results.append({
            "scenario":name,"assumed_g_left_right_w_m2k":[gl,gr],
            "assumed_plate_fraction":f,"assumed_heat_footprint_m":[w,h],
            "r_app_A_to_A_k_w":aa,"r_app_B_to_B_k_w":bb,"r_app_B_to_A_k_w":ba,
            "co_moving_relative_difference":abs(aa-bb)/((aa+bb)/2),
            "fixed_A_sensor_source_swap_relative_difference":abs(aa-ba)/aa,
            "maximum_energy_relative_residual":max(x["energy_relative_residual"] for x in obs.values())
        })
    return {
        "evidence_class":"SYNTHETIC_ASSUMPTION_DRIVEN_PREDESIGN",
        "revision":"v0.6",
        "normalized_power_w":1.,"power_is_not_authorized_setpoint":True,
        "assumed_plate_m":[p.side_m,p.side_m,p.thickness_m],
        "assumed_k_w_mk":p.conductivity_w_mk,"cells_per_side":p.cells,
        "not_modelled":["real fin profile","TIM","contact mechanics","true convection field",
                       "case/junction dynamics","electrical heat bypass mechanism"],
        "sensor_positions_m":{name:list(xy) for name,xy in POSITIONS.items()},
        "scenarios":results
    }

if __name__=="__main__":
    import argparse
    pa=argparse.ArgumentParser()
    pa.add_argument("--out",default="results/conditional_spatial_transfer_v0.6.json")
    args=pa.parse_args()
    path=Path(args.out);path.parent.mkdir(parents=True,exist_ok=True)
    data=make_results()
    path.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    for c in data["scenarios"]:
        print(c["scenario"],"A",round(c["r_app_A_to_A_k_w"],4),"B",round(c["r_app_B_to_B_k_w"],4),
              "co-moving %",round(100*c["co_moving_relative_difference"],2),
              "fixed-A %",round(100*c["fixed_A_sensor_source_swap_relative_difference"],2))
