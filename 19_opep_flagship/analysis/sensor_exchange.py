"""Draft offline exchange for a sensor time-constant model; no rig control.
Validated structure is NOT qualified physical data or external integration.
"""
from math import isfinite
from dynamics import first_order_sensor

def sensor_replay(record, inputs, initial):
    """inputs: (elapsed seconds, held input in same declared output units).
    Each input is constant over the immediately following interval.
    Returns samples at interval ends; no interpolation outside the declared domain.
    """
    if record.get("schema")!="OPEP-SENSOR-EXCHANGE-003":
        raise ValueError("schema mismatch")
    if record.get("evidence_class")!="SYNTHETIC_REFERENCE":
        raise ValueError("draft adapter accepts synthetic records only")
    if record.get("physical_validation")!="NOT_VALIDATED":
        raise ValueError("invalid synthetic claim")
    for key in ("model_id","model_version","quantity","unit"):
        if not isinstance(record.get(key),str) or not record[key].strip():
            raise ValueError("missing model identity or units")
    tau=record["tau_s"]
    lo,hi=record["input_domain"]
    if not all(isfinite(x) for x in (lo,hi,tau,initial)) or lo>=hi or tau<=0 or not lo<=initial<=hi:
        raise ValueError("invalid model or initial state")
    t,y=0.,initial
    out=[]
    for dt,u in inputs:
        if not isfinite(dt) or dt<=0 or not isfinite(u) or not lo<=u<=hi:
            raise ValueError("invalid time or out-of-domain signal")
        y=first_order_sensor(y,u,tau,dt);t+=dt
        out.append((t,y))
    return out
