"""Screening calculations only; not accredited measurement or normative conformity.
All lengths and uncertainties supplied by caller in consistent units.
"""
from collections import defaultdict
from math import isfinite,sqrt
from statistics import mean
def interval_screen(value,expanded_u,lower,upper):
    """Conservative interval containment; agreed decision rule required."""
    if not all(isfinite(x) for x in (value,expanded_u,lower,upper)) or expanded_u<0 or lower>=upper:
        raise ValueError("invalid measurement, uncertainty or specification")
    lo,hi=value-expanded_u,value+expanded_u
    if lo>=lower and hi<=upper:return "INTERVAL_INSIDE"
    if hi<lower or lo>upper:return "INTERVAL_OUTSIDE"
    return "INDETERMINATE_OVERLAP"
def pooled_repeatability(records):
    """Pool within-artifact sample variance; not full Gage R&R.
    records: iterable of (artifact_id, measurement) from one defined method.
    """
    groups=defaultdict(list)
    for identity,v in records:
        if not isinstance(identity,str) or not identity.strip() or not isfinite(v):
            raise ValueError("invalid observation")
        groups[identity].append(v)
    if len(groups)<2 or any(len(x)<2 for x in groups.values()):
        raise ValueError("need >=2 artifacts with >=2 readings each")
    dof=sum(len(x)-1 for x in groups.values())
    ss=sum(sum((v-mean(x))**2 for v in x) for x in groups.values())
    return {"artifact_count":len(groups),"reading_count":sum(map(len,groups.values())),
            "degrees_of_freedom":dof,"within_artifact_sd":sqrt(ss/dof),
            "method":"POOLED_REPEATABILITY_ONLY_NOT_FULL_GRR"}
def first_pass_yield(accepted_first_pass,attempted):
    """Learning lot descriptive proportion, not process capability."""
    if type(accepted_first_pass) is not int or type(attempted) is not int or not 0<=accepted_first_pass<=attempted or attempted<=0:
        raise ValueError("invalid counts")
    return accepted_first_pass/attempted
