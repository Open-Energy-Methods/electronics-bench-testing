"""Runnable synthetic experiment, output and critical stress audits."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from .synthetic import make_dataset,TRUE_BOUNDARY
from .compare import fit_all,fit_case_only_ablation,predict,errors
from .boundary import qualify
from .uncertainty import boundary_prediction_sensitivity


def evaluate(seed:int=20261105,mode:str="ideal")->dict:
    d=make_dataset(seed,mode)
    qualified={name:qualify(d.qualification,name) for name in TRUE_BOUNDARY}
    fitted=fit_all(d.train,qualified)
    ablation=fit_case_only_ablation(d.train)
    holdout=[]
    for e in d.validation:
        for name,f in fitted.items():
            p=predict(f,e,qualified)
            holdout.append({"run":e.run_id,"cooling":e.cooling,"assembly":e.assembly_id,
                            "model":name,**errors(e,p,static=(name=="B0"))})
    sensitivity=boundary_prediction_sensitivity(fitted["B3"],d.validation[1],qualified["FAN"])
    return {
        "boundary_sensitivity_for_forced_holdout":sensitivity,
        "evidence_type":"SYNTHETIC_ONLY_NO_PHYSICAL_MEASUREMENTS",
        "mode":mode,"seed":seed,"truth":d.truth,
        "qualification":{k:{"mean_k_w":v.mean_k_w,"u_k_w":v.u_k_w,
                            "n_independent_runs":v.n_independent_runs,
                            "type":"apparent sink-node resistance, not convection coefficient"}
                         for k,v in qualified.items()},
        "identifiability_ablation_B2_case_only":{
            "parameters":ablation.parameters,
            "optimizer_success":ablation.optimizer_success,
            "training_rmse_c":ablation.train_rmse_c,
            "jacobian_log_condition_number":ablation.condition_number,
            "log_jacobian_singular_values":ablation.jacobian_singular_values,
            "warning":"Local, weighting- and parameterization-dependent condition number."},
        "fitted":{n:{"parameters":v.parameters,"n_parameters":v.n_parameters,
                     "training_observables":v.training_observables,
                     "training_rmse_c":v.train_rmse_c if np.isfinite(v.train_rmse_c) else None,
                     "jacobian_log_condition_number":v.condition_number if np.isfinite(v.condition_number) else None,
                     "jacobian_log_singular_values":v.jacobian_singular_values}
                  for n,v in fitted.items()},
        "holdout":holdout,
        "warning":"No physical testing, instrument calibration, direct semiconductor junction observation or confirmed novelty. Qualification geometry may not transfer."
    }


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",type=Path,
                        default=Path("results/synthetic_model_comparison_v0.4.json"))
    opts=parser.parse_args()
    results={mode:evaluate(mode=mode) for mode in ("ideal","bypass","mismatched")}
    opts.out.parent.mkdir(parents=True,exist_ok=True)
    opts.out.write_text(json.dumps(results,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    for mode,r in results.items():
        print("MODE",mode,"BOUNDARY",r["qualification"])
        for x in r["holdout"]:
            print(x["run"],x["model"],"package_RMSE",x["package_transient_rmse_C"])
    print("SYNTHETIC ONLY. Saved",opts.out)


if __name__=="__main__":
    main()
