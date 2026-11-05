"""Generate plots from deterministic synthetic model benchmark JSON."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"results"/"synthetic_model_comparison_v0.4.json"


def main():
    results=json.loads(REPORT.read_text())
    experiments=["HO-NAT-4W","HO-FAN-5W","HO-NAT-INTERFACE","HO-FAN-INTERFACE"]
    models=["B1","B2","B3"]
    fig,ax=plt.subplots(figsize=(9.2,4.7))
    x=np.arange(len(experiments));width=.24
    for i,m in enumerate(models):
        vals=[next(row["package_transient_rmse_C"] for row in results["ideal"]["holdout"]
                   if row["run"]==exp and row["model"]==m) for exp in experiments]
        ax.bar(x+(i-1)*width,vals,width,label=m)
    ax.set_xticks(x,[v.replace("HO-","").replace("-","\n") for v in experiments])
    ax.set_ylabel("Synthetic package transient RMSE (°C)")
    ax.set_title("Independent boundary qualification helps on cooling holdout (synthetic)")
    ax.legend();ax.grid(axis="y",alpha=.2);fig.tight_layout()
    fig.savefig(ROOT/"figures"/"comparison_holdouts.png",dpi=180);plt.close(fig)

    fig,ax=plt.subplots(figsize=(8.9,4.7))
    for name in ("ideal","bypass","mismatched"):
        v=[next(r["package_transient_rmse_C"] for r in results[name]["holdout"]
                if r["run"]=="HO-FAN-5W" and r["model"]==m) for m in ("B2","B3")]
        ax.plot(["B2 (fixed)","B3 (boundary input)"],v,marker="o",label=name)
    ax.set_ylabel("Synthetic forced-cooling holdout RMSE (°C)")
    ax.set_title("Boundary-aware prediction can fail under model/fixture mismatch")
    ax.grid(alpha=.2);ax.legend();fig.tight_layout()
    fig.savefig(ROOT/"figures"/"boundary_failure_modes.png",dpi=180);plt.close(fig)


if __name__=="__main__":
    main()
