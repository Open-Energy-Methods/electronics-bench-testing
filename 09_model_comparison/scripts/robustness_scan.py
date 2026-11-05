"""Descriptive sensitivity to synthetic sensor-noise seeds, NOT hardware replicates."""
from pathlib import Path
import json
import numpy as np
from research_models.run import evaluate


def run(n=25):
    output={}
    for mode in ("ideal","bypass","mismatched"):
        improvement=[]
        condition=[]
        for seed in range(20261105,20261105+n):
            r=evaluate(seed,mode)
            row=lambda model: next(x for x in r["holdout"] if x["run"]=="HO-FAN-5W" and x["model"]==model)
            improvement.append(row("B2")["package_transient_rmse_C"]-row("B3")["package_transient_rmse_C"])
            condition.append(r["identifiability_ablation_B2_case_only"]["jacobian_log_condition_number"])
        output[mode]={
            "seed_start":20261105,
            "n_independent_synthetic_noise_seeds":n,
            "median_B2_minus_B3_RMSE_C":float(np.median(improvement)),
            "q05_B2_minus_B3_RMSE_C":float(np.quantile(improvement,.05)),
            "q95_B2_minus_B3_RMSE_C":float(np.quantile(improvement,.95)),
            "number_B3_lower_error":int(np.sum(np.asarray(improvement)>0)),
            "median_package_only_B2_Jacobian_condition":float(np.median(condition))
        }
    return {"evidence_type":"SYNTHETIC_ONLY",
            "warning":"Noise seeds are NOT physical remounts; quantiles are not experimental confidence intervals.",
            "summary":output}


if __name__=="__main__":
    output=run()
    path=Path("results/synthetic_noise_seed_robustness_v0.4.json")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))
