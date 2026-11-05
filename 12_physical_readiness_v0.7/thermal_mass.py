"""Conditional thermal-mass comparison, NOT real fixture thermodynamics.

The density and specific heat are assumed generic aluminium values, not an
SK92 certificate or calorimetric measurement. Fully isothermal plate
capacitance is only an illustrative upper-level lumped bookkeeping estimate.
"""
from __future__ import annotations
import json
from dataclasses import dataclass
from math import isfinite

@dataclass(frozen=True)
class AssumedPlate:
    width_m: float = .100
    length_m: float = .100
    thickness_m: float = .004
    density_kg_m3: float = 2700.0
    specific_heat_j_kgk: float = 900.0

    def quantities(self):
        dims=(self.width_m,self.length_m,self.thickness_m,
              self.density_kg_m3,self.specific_heat_j_kgk)
        if any(not isfinite(x) or x<=0 for x in dims):
            raise ValueError("all assumed dimensions and properties must be finite positive")
        vol=self.width_m*self.length_m*self.thickness_m
        mass=vol*self.density_kg_m3
        return {
          "evidence_grade":"ILLUSTRATIVE_ALUMINIUM_ASSUMPTIONS_NOT_REAL_PART_PROPERTIES",
          "volume_m3":vol,"mass_kg":mass,
          "fully_lumped_heat_capacity_j_per_k":mass*self.specific_heat_j_kgk,
          "not_included":["real sink fins and base","contact resistance","temperature gradients",
                          "fasteners","TIM","sensor mass","airflow and radiation"],
          "not_a_predicted_time_constant":True
        }

if __name__=="__main__":
    print(json.dumps(AssumedPlate().quantities(),indent=2,sort_keys=True))
