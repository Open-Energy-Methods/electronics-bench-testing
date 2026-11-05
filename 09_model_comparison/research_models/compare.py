"""Fitted benchmark candidates B0-B3; strict calibration/qualification split.

Assumes controlled constant ambient and run-specific fixed cooling. All model
parameters are empirical/effective; fitted network components are not proven
uniquely identifiable physical resistances or semiconductor junctions.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.optimize import least_squares
from .physics import TwoNode, rc1, solve
from .boundary import BoundaryEstimate

@dataclass(frozen=True)
class Experiment:
    run_id: str
    category: str
    assembly_id: str
    cooling: str
    time_s: np.ndarray
    power_w: np.ndarray
    measured_c: np.ndarray
    ambient_c: float

    def __post_init__(self) -> None:
        if self.measured_c.shape != (len(self.time_s), 2):
            raise ValueError("measured case and sink required")

@dataclass(frozen=True)
class ModelFit:
    name: str
    parameters: tuple[float, ...]
    train_rmse_c: float
    jacobian_singular_values: tuple[float, ...]
    condition_number: float
    n_parameters: int
    training_observables: str
    optimizer_success: bool = True


def _fit(kind: str, experiments: list[Experiment],
         boundary: dict[str, BoundaryEstimate] | None) -> ModelFit:
    if not experiments or any(x.category != "train" or x.cooling != "NAT" for x in experiments):
        raise ValueError("fit accepts explicitly labeled NAT calibration runs only")
    if kind == "B1":
        initial, lower, upper = [3,75], [0.1,1], [20,2000]
    elif kind in ("B2","B2_CASE_ONLY"):
        initial, lower, upper = [0.5,12,65,2.8], [0.05,0.5,1,0.2], [5,500,1000,12]
    elif kind == "B3":
        if not boundary or "NAT" not in boundary:
            raise ValueError("B3 requires independent NAT boundary qualification")
        initial, lower, upper = [0.5,12,65], [0.05,0.5,1], [5,500,1000]
    else:
        raise ValueError(kind)
    b_nat = None if boundary is None else boundary.get("NAT")
    weights = np.array([0.10,0.10])

    def predictions(par: np.ndarray, exp: Experiment) -> np.ndarray:
        if kind == "B1":
            return rc1(exp.time_s,exp.power_w,par[0],par[1],exp.ambient_c)[:,None]
        rsa = par[3] if kind in ("B2","B2_CASE_ONLY") else b_nat.mean_k_w
        model = TwoNode(r_ps=par[0],c_p=par[1],c_s=par[2],r_sa=rsa)
        return solve(model,exp.time_s,exp.power_w,ambient_c=exp.ambient_c)

    def residual(lp: np.ndarray) -> np.ndarray:
        par = np.exp(lp)
        items=[]
        for e in experiments:
            predicted=predictions(par,e)
            obs=e.measured_c[:,:1] if kind in ("B1","B2_CASE_ONLY") else e.measured_c
            items.append(((predicted[:,:obs.shape[1]]-obs)/weights[:obs.shape[1]]).ravel())
        return np.concatenate(items)

    fit=least_squares(residual,np.log(initial),bounds=(np.log(lower),np.log(upper)),
                     x_scale="jac",max_nfev=120,xtol=1e-10,ftol=1e-10,gtol=1e-10)
    if not fit.success and fit.optimality > 1e-3 and kind != "B2_CASE_ONLY":
        raise RuntimeError("optimizer did not converge")
    res=residual(fit.x)
    sv=np.linalg.svd(fit.jac,full_matrices=False,compute_uv=False)
    cond=float(sv[0]/sv[-1]) if sv[-1]>1e-12 else float("inf")
    return ModelFit(kind,tuple(float(x) for x in np.exp(fit.x)),
                    float(np.sqrt(np.mean((res*.10)**2))),
                    tuple(float(x) for x in sv),cond,len(initial),
                    "package only" if kind in ("B1","B2_CASE_ONLY") else "package + sink",bool(fit.success))


def fit_case_only_ablation(training: list[Experiment]) -> ModelFit:
    """Identifiability diagnostic, not proof of recovered internal parameters."""
    return _fit("B2_CASE_ONLY",training,None)


def fit_all(training: list[Experiment], boundary: dict[str,BoundaryEstimate]) -> dict[str,ModelFit]:
    """No validation argument is accepted: structural prevention of response leakage."""
    if not training or any(x.category!="train" for x in training):
        raise ValueError("training must be labelled train")
    ratios=[]
    for e in training:
        powered=np.where(e.power_w>0)[0]
        if len(powered)<8: raise ValueError("insufficient powered plateau")
        tail=powered[-max(5,int(len(powered)*.2)):]
        ratios.append(float(np.mean((e.measured_c[tail,0]-e.ambient_c)/e.power_w[tail])))
    b0=ModelFit("B0",(float(np.mean(ratios)),),float("nan"),(),float("nan"),1,
                "package late-power plateau")
    return {"B0":b0,"B1":_fit("B1",training,None),"B2":_fit("B2",training,None),
            "B3":_fit("B3",training,boundary)}


def predict(fit: ModelFit,exp: Experiment,
            boundary: dict[str,BoundaryEstimate]|None=None) -> np.ndarray:
    """No observed temperature enters the forecast calculation."""
    par=fit.parameters
    if fit.name=="B0":
        case=exp.ambient_c+par[0]*exp.power_w
        return np.column_stack([case,np.full(len(case),np.nan)])
    if fit.name=="B1":
        case=rc1(exp.time_s,exp.power_w,par[0],par[1],exp.ambient_c)
        return np.column_stack([case,np.full(len(case),np.nan)])
    if fit.name in ("B2","B2_CASE_ONLY","B3"):
        if fit.name=="B3":
            if not boundary or exp.cooling not in boundary:
                raise ValueError("no independent boundary input for requested cooling condition")
            rsa=boundary[exp.cooling].mean_k_w
        else:
            rsa=par[3]
        return solve(TwoNode(r_ps=par[0],c_p=par[1],c_s=par[2],r_sa=rsa),
                     exp.time_s,exp.power_w,ambient_c=exp.ambient_c)
    raise ValueError(fit.name)


def errors(exp:Experiment,pred:np.ndarray,*,static:bool=False)->dict[str,float|None]:
    """Within-run errors descriptive; time samples are NOT independent n."""
    outcome={}
    powered=np.where(exp.power_w>0)[0]
    tail=powered[-max(5,int(.2*len(powered))):]
    for label,j in (("package",0),("sink",1)):
        if np.all(np.isnan(pred[:,j])):
            outcome[f"{label}_transient_rmse_C"]=None
            outcome[f"{label}_late_bias_C"]=None
        else:
            d=pred[:,j]-exp.measured_c[:,j]
            outcome[f"{label}_transient_rmse_C"]=None if static else float(np.sqrt(np.mean(d**2)))
            outcome[f"{label}_late_bias_C"]=float(np.mean(d[tail]))
    return outcome
