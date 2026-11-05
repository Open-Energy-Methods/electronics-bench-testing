"""EBT v0.6: conditional steady 2D plate finite-volume sensitivity.
Every result is SYNTHETIC. No finned sink, TIM, package junction or physical
instrument is represented. A normalized 1 W input is NOT an operating setpoint.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

@dataclass(frozen=True)
class Plate:
    side_m: float = .100
    thickness_m: float = .004
    conductivity_w_mk: float = 180.
    cells: int = 41

    def validate(self):
        if self.cells < 9 or self.cells % 2 == 0:
            raise ValueError("cells must be odd >= 9")
        if any(not np.isfinite(v) or v <= 0 for v in
               (self.side_m, self.thickness_m, self.conductivity_w_mk)):
            raise ValueError("plate parameters must be positive finite")

@dataclass(frozen=True)
class Source:
    x_m: float
    y_m: float = 0.
    width_m: float = .0101
    height_m: float = .0146
    power_w: float = 1.
    plate_fraction: float = 1.

    def validate(self, plate):
        values=(self.x_m,self.y_m,self.width_m,self.height_m,
                self.power_w,self.plate_fraction)
        if not all(np.isfinite(x) for x in values):
            raise ValueError("source must be finite")
        if min(self.width_m,self.height_m,self.power_w) <= 0:
            raise ValueError("positive footprint and power required")
        if not 0 < self.plate_fraction <= 1:
            raise ValueError("plate_fraction must be (0,1]")
        if (abs(self.x_m)+self.width_m/2 > plate.side_m/2 or
            abs(self.y_m)+self.height_m/2 > plate.side_m/2):
            raise ValueError("footprint exceeds proposed plate")

def loss_field(plate, left_w_m2k, right_w_m2k=None):
    """Spatial effective plate loss; not a qualified convective coefficient."""
    plate.validate()
    right=left_w_m2k if right_w_m2k is None else right_w_m2k
    if not all(np.isfinite(x) and x>0 for x in (left_w_m2k,right)):
        raise ValueError("g must be positive finite")
    x=(np.arange(plate.cells)+.5)*plate.side_m/plate.cells-plate.side_m/2
    return np.where(x[:,None]<0,left_w_m2k,right)*np.ones((plate.cells,plate.cells))

def source_map(plate, source):
    """Rectangle-cell overlap apportions unit power without grid input loss."""
    plate.validate();source.validate(plate)
    d=plate.side_m/plate.cells
    lo=np.arange(plate.cells)*d-plate.side_m/2;hi=lo+d
    def overlap(center,width):
        return np.maximum(0,np.minimum(hi,center+width/2)-np.maximum(lo,center-width/2))
    area=np.outer(overlap(source.x_m,source.width_m),overlap(source.y_m,source.height_m))
    if area.sum()<=0:raise ValueError("empty footprint")
    return source.power_w*source.plate_fraction*area/area.sum()

def solve_plate(plate, source, g_w_m2k):
    """-k*t*laplacian(theta)+g*theta=q, insulated lateral edges."""
    plate.validate();source.validate(plate)
    n=plate.cells
    g=np.asarray(g_w_m2k,float)
    if g.shape!=(n,n) or not np.all(np.isfinite(g)) or np.any(g<=0):
        raise ValueError("invalid effective loss field")
    d=plate.side_m/n;c=plate.conductivity_w_mk*plate.thickness_m
    diag=(g*d*d).ravel().copy()
    rows=list(range(n*n));cols=rows.copy();values=[]
    off=[]
    for ix in range(n):
        for iy in range(n):
            i=ix*n+iy
            diag[i]+=c*((ix>0)+(ix<n-1)+(iy>0)+(iy<n-1))
            if ix<n-1:off.append((i,i+n,-c))
            if iy<n-1:off.append((i,i+1,-c))
    values=diag.tolist()
    for i,j,v in off:
        rows.extend((i,j));cols.extend((j,i));values.extend((v,v))
    A=coo_matrix((values,(rows,cols)),shape=(n*n,n*n)).tocsr()
    return spsolve(A,source_map(plate,source).ravel()).reshape(n,n)

def sample(plate,rise_k,x_m,y_m):
    """Bilinear interpolation: measured quantity is T_plate, not T_sink."""
    plate.validate();n=plate.cells
    if np.shape(rise_k)!=(n,n):raise ValueError("field shape")
    d=plate.side_m/n
    fx=(x_m+plate.side_m/2)/d-.5
    fy=(y_m+plate.side_m/2)/d-.5
    if min(fx,fy)<0 or max(fx,fy)>n-1:raise ValueError("sensor outside grid")
    ix=min(n-2,int(np.floor(fx)));iy=min(n-2,int(np.floor(fy)))
    sx=fx-ix;sy=fy-iy;t=np.asarray(rise_k)
    return float((1-sx)*(1-sy)*t[ix,iy]+sx*(1-sy)*t[ix+1,iy]
                +(1-sx)*sy*t[ix,iy+1]+sx*sy*t[ix+1,iy+1])

def inspect(plate,src,g,positions):
    t=solve_plate(plate,src,g)
    qin=src.power_w*src.plate_fraction
    qout=float(np.sum(g*t)*(plate.side_m/plate.cells)**2)
    return {
        "apparent_r_k_w_by_sensor":{name:sample(plate,t,*pos)/src.power_w for name,pos in positions.items()},
        "input_to_plate_w":qin,"computed_loss_w":qout,
        "energy_relative_residual":abs(qout-qin)/qin,
        "model_label":"SYNTHETIC_CONDITIONAL_STEADY_PLATE_NOT_PHYSICAL_VALIDATION"
    }
