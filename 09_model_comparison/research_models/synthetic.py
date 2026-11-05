"""Disjoint synthetic training/qualification/validation experiments.

All numbers, noise/uncertainty values and heat-transfer coefficients are
illustrative and in NO way authorize operation at the stated wattages.
"""
from __future__ import annotations
from dataclasses import dataclass,replace
import numpy as np
from .physics import TwoNode,solve
from .boundary import QualRecord
from .compare import Experiment

SEED=20261105
AMBIENT_C=24.0
TRUE_BOUNDARY={"NAT":2.8,"FAN":0.95}

@dataclass(frozen=True)
class Dataset:
    train:list[Experiment]
    qualification:list[QualRecord]
    validation:list[Experiment]
    truth:dict[str,float]


def _input(time:np.ndarray,w:float,end:float)->np.ndarray:
    return np.where(time<end,w,0.)


def make_dataset(seed:int=SEED,mode:str="ideal")->Dataset:
    """Synthetic stress scenarios ideal, bypass, mismatched qualification geometry."""
    if mode not in {"ideal","bypass","mismatched"}:
        raise ValueError(mode)
    rng=np.random.default_rng(seed)
    time=np.arange(0,1001,20.,dtype=float)
    qt=np.arange(0,2201,25.,dtype=float)
    rpa=8.5 if mode=="bypass" else None
    base=TwoNode(r_pa=rpa)
    qualification=[]
    for cooling,rsa in TRUE_BOUNDARY.items():
        qual_r=rsa*4 if mode=="mismatched" and cooling=="FAN" else rsa
        for i in range(4):
            q=_input(qt,4.,1850.)
            y=solve(replace(base,r_sa=qual_r),qt,np.zeros_like(q),
                    sink_w=q,ambient_c=AMBIENT_C)
            plateau=(qt>=1600)&(qt<=1850)
            ts=float(np.mean(y[plateau,1])+rng.normal(0,.055))
            ta=float(AMBIENT_C+rng.normal(0,.04))
            p=float(4*(1+rng.normal(0,.006)))
            qualification.append(QualRecord(f"Q-{cooling}-{i+1}",cooling,ts,ta,p))

    def run(run_id:str,category:str,cooling:str,pw:float,rps:float,assembly:str)->Experiment:
        p=_input(time,pw,600.)
        truth=solve(replace(base,r_sa=TRUE_BOUNDARY[cooling],r_ps=rps),
                    time,p,ambient_c=AMBIENT_C)
        measured=truth+rng.normal(0,.07,(1,2))+rng.normal(0,.09,truth.shape)
        return Experiment(run_id,category,assembly,cooling,time.copy(),p,measured,AMBIENT_C)

    train=[run("CAL-NAT-3W","train","NAT",3.,.48,"TR-A"),
           run("CAL-NAT-5W","train","NAT",5.,.48,"TR-A")]
    validation=[run("HO-NAT-4W","validate","NAT",4.,.50,"HO-01"),
                run("HO-FAN-5W","validate","FAN",5.,.50,"HO-02"),
                run("HO-NAT-INTERFACE","validate","NAT",5.,.78,"HO-03"),
                run("HO-FAN-INTERFACE","validate","FAN",4.,.78,"HO-04")]
    return Dataset(train,qualification,validation,{
        "truth_rsa_nat_k_w":2.8,"truth_rsa_fan_k_w":.95,
        "truth_rps_train_k_w":.48,"truth_rps_new_interface_k_w":.78,
        "rpa_bypass_k_w":rpa if rpa else 0.0,
        "qualification_mismatch_factor":4.0 if mode=="mismatched" else 1.0})
