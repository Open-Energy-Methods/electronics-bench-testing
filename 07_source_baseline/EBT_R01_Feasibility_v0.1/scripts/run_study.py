#!/usr/bin/env python3
"""Execute an entirely synthetic bench feasibility case study.

This script DOES NOT analyse experimental measurements and should not be cited
as evidence of real hardware model accuracy.
"""
from pathlib import Path
import json, sys, hashlib
from dataclasses import replace
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from ebt.model import ThermalSystem,response,power_schedule,single_rc_response,relative_energy_residual

RNG=np.random.default_rng(20261105)
sys0=ThermalSystem()
t=np.arange(0.,1201.,5.)
p5=power_schedule(t,5.,750.)
p3=power_schedule(t,3.,750.)
obs_sd=0.15


def noisy(reference):
    return reference+RNG.normal(0,obs_sd,len(reference))

# Complete case/sink data and inaccessible internal junction state are all SYNTHETIC.
train_ref=response(sys0,t,p5)
train_meas_case=noisy(train_ref[:,1])
train_meas_sink=noisy(train_ref[:,2])
cal_ref3=response(sys0,t,p3)
val_meas3=noisy(cal_ref3[:,1])
forced=replace(sys0,r_sa=0.90)
forced_truth=response(forced,t,p5)
forced_case=noisy(forced_truth[:,1])
interface=replace(sys0,r_ps=1.00)
interface_truth=response(interface,t,p5)
interface_case=noisy(interface_truth[:,1])

# Only calibrate using baseline case time-series, never using held-out conditions.
def predicted(params,power):
    r,c=np.exp(params)
    return single_rc_response(t,power,r,c,sys0.t_amb)
fit=least_squares(lambda lp: (predicted(lp,p5)-train_meas_case)/obs_sd,
                  x0=np.log([3.4,60.]),bounds=(np.log([0.1,0.1]),np.log([25,2000])),max_nfev=700)
r_fit,c_fit=np.exp(fit.x)

train_pred=predicted(fit.x,p5)
val_pred3=predicted(fit.x,p3)
forced_fixed=predicted(fit.x,p5)
# Independent cooling resistance of each configuration is supplied as a known
# *synthetic boundary input*, not estimated from held-out temperature data.
r_bdy=r_fit-sys0.r_sa+forced.r_sa
if r_bdy<=0: raise RuntimeError('Unphysical boundary-corrected thermal R')
forced_bdy=single_rc_response(t,p5,r_bdy,c_fit,sys0.t_amb)
int_fixed=predicted(fit.x,p5)

# JUNCTION BLIND SPOT: two networks with different inner junction/package R.
# Both generate almost the same accessible package signal (and can be missed
# by low-bandwidth case sensors), but hidden Tj strongly differs.
alt=replace(sys0,r_jp=1.50)
alt_response=response(alt,t,p5)
max_case_difference=float(np.max(abs(alt_response[:,1]-train_ref[:,1])))
max_junction_difference=float(np.max(abs(alt_response[:,0]-train_ref[:,0])))
max_sink_difference=float(np.max(abs(alt_response[:,2]-train_ref[:,2])))

# Scaled finite-difference sensitivity of accessible temperature sensors
# to log(r_jp). Dimension is degrees C per 1 log unit.
h=0.01
plus=response(replace(sys0,r_jp=sys0.r_jp*np.exp(h)),t,p5)
minus=response(replace(sys0,r_jp=sys0.r_jp*np.exp(-h)),t,p5)
sens=(plus-minus)/(2*h)
sens_case=np.max(abs(sens[:,1]))
sens_junction=np.max(abs(sens[:,0]))

rmse=lambda observed,predicted: float(np.sqrt(np.mean((np.asarray(observed)-np.asarray(predicted))**2)))
results={
 'disclaimer':'ALL RESPONSES AND OBSERVATIONS ARE SYNTHETIC. NO PHYSICAL VALIDATION.',
 'seed':20261105,
 'sensor_noise_std_C':obs_sd,
 'power_W':5.0,
 'pulse_end_s':750.0,
 'time_step_s':5.0,
 'calibration_case':'baseline natural cooling; one 5 W pulse; package-only noisy sensor',
 'validation_cases':['3 W natural cooling', '5 W forced convection r_sa=0.9 K/W', '5 W altered interface r_ps=1.0 K/W'],
 'true_parameters':sys0.__dict__,
 'alternate_hidden_r_jp_K_per_W':alt.r_jp,
 'lumped_fitted_R_K_per_W':float(r_fit),
 'lumped_fitted_C_J_per_K':float(c_fit),
 'boundary_aware_R_K_per_W':float(r_bdy),
 'train_rmse_C':rmse(train_meas_case,train_pred),
 'same_boundary_3W_rmse_C':rmse(val_meas3,val_pred3),
 'forced_fixed_rmse_C':rmse(forced_case,forced_fixed),
 'forced_boundary_aware_rmse_C':rmse(forced_case,forced_bdy),
 'interface_unmodelled_rmse_C':rmse(interface_case,int_fixed),
 'max_alternate_case_diff_C':max_case_difference,
 'max_alternate_junction_diff_C':max_junction_difference,
 'max_alternate_sink_diff_C':max_sink_difference,
 'case_Rjp_log_sensitivity_max_C':float(sens_case),
 'junction_Rjp_log_sensitivity_max_C':float(sens_junction),
 'energy_balance_relative_residual':relative_energy_residual(sys0,np.arange(0,1201,1.),power_schedule(np.arange(0,1201,1.)),response(sys0,np.arange(0,1201,1.),power_schedule(np.arange(0,1201,1.))))
}

for p in [ROOT/'data/synthetic',ROOT/'results',ROOT/'figures']:
    p.mkdir(parents=True,exist_ok=True)
df=pd.DataFrame({'time_s':t, 'power_W':p5,
                 'synthetic_junction_true_C':train_ref[:,0],
                 'synthetic_package_true_C':train_ref[:,1],
                 'synthetic_heatsink_true_C':train_ref[:,2],
                 'synthetic_package_measured_C':train_meas_case,
                 'synthetic_heatsink_measured_C':train_meas_sink,
                 'synthetic_package_alt_inner_R_C':alt_response[:,1],
                 'synthetic_junction_alt_inner_R_C':alt_response[:,0],
                 'model_single_rc_package_C':train_pred})
df.to_csv(ROOT/'data/synthetic'/'baseline_synthetic.csv',index=False,float_format='%.9f')
val=pd.DataFrame({'time_s':t,'power_W':p5,'synthetic_forced_case_true_C':forced_truth[:,1],
                  'synthetic_forced_case_measured_C':forced_case,
                  'model_fixed_boundary_C':forced_fixed,
                  'model_boundary_updated_C':forced_bdy,
                  'synthetic_modified_interface_case_true_C':interface_truth[:,1],
                  'synthetic_modified_interface_case_measured_C':interface_case,
                  'model_unmodelled_interface_C':int_fixed,
                  'synthetic_3W_package_measured_C':val_meas3,'model_3W_package_C':val_pred3})
val.to_csv(ROOT/'data/synthetic'/'heldout_synthetic.csv',index=False,float_format='%.9f')
(ROOT/'results'/'metrics.json').write_text(json.dumps(results,indent=2)+'\n')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.dpi':130,'savefig.dpi':170})
fig,ax=plt.subplots(figsize=(9.5,4.1))
ax.plot(t,train_ref[:,0],label='Junction (hidden state, synthetic)',linewidth=2)
ax.plot(t,train_ref[:,1],label='Package (synthetic)',linewidth=2)
ax.plot(t,train_ref[:,2],label='Heatsink (synthetic)',linewidth=2)
ax.axvline(750,color='gray',linestyle=':',label='Power turned off')
ax.set(xlabel='Time (s)',ylabel='Temperature (°C)',title='Three-node energy-conserving thermal model - synthetic commissioning case')
ax.grid(alpha=.22);ax.legend(ncol=2,fontsize=8)
fig.tight_layout();fig.savefig(ROOT/'figures'/'01_three_node_response.png');plt.close(fig)

fig,ax=plt.subplots(figsize=(9.5,4.1))
ax.plot(t,train_ref[:,1],label='Package case A',linewidth=2)
ax.plot(t,alt_response[:,1],label='Package case B (different hidden Rjp)',linewidth=2,linestyle='--')
ax.plot(t,train_ref[:,0],label='Internal junction A',linewidth=1.7)
ax.plot(t,alt_response[:,0],label='Internal junction B',linewidth=1.7,linestyle='--')
ax.set(xlabel='Time (s)',ylabel='Temperature (°C)',title='Synthetic identifiability counterexample: similar surface, different junction')
ax.grid(alpha=.22);ax.legend(fontsize=8,ncol=2)
fig.tight_layout();fig.savefig(ROOT/'figures'/'02_surface_blind_spot.png');plt.close(fig)

fig,ax=plt.subplots(figsize=(9.5,4.1))
ax.plot(t,forced_truth[:,1],label='Held-out forced-cooling truth (synthetic)',linewidth=2)
ax.plot(t,forced_fixed,label='1RC fitted at natural cooling, unchanged',linestyle='--')
ax.plot(t,forced_bdy,label='1RC using independent boundary R input',linestyle='-.')
ax.set(xlabel='Time (s)',ylabel='Package temperature (°C)',title='Synthetic model transfer: natural cooling -> forced cooling')
ax.grid(alpha=.22);ax.legend(fontsize=8)
fig.tight_layout();fig.savefig(ROOT/'figures'/'03_boundary_transfer.png');plt.close(fig)

fig,ax=plt.subplots(figsize=(8.5,4.4))
labels=['Calibration\n5 W, natural','Held-out\n3 W, natural','Held-out\n5 W, forced\nfixed boundary','Held-out\n5 W, forced\nupdated boundary','Held-out\n5 W, interface\nnot updated']
vals=[results['train_rmse_C'],results['same_boundary_3W_rmse_C'],results['forced_fixed_rmse_C'],results['forced_boundary_aware_rmse_C'],results['interface_unmodelled_rmse_C']]
ax.bar(range(len(labels)),vals,color=['#415a77','#778da9','#bf5d50','#5b957b','#bf5d50'])
ax.set_xticks(range(len(labels)),labels,fontsize=8)
ax.set(ylabel='RMSE against synthetic noisy package sensor (°C)',title='Synthetic feasibility outcomes: in-sample fit vs held-out scenarios')
ax.grid(axis='y',alpha=.15)
for i,v in enumerate(vals): ax.text(i,v+max(vals)*.015,f'{v:.2f}',ha='center',fontsize=9)
ax.set_ylim(0,max(vals)*1.22);fig.tight_layout();fig.savefig(ROOT/'figures'/'04_case_metrics.png');plt.close(fig)

# Data and figure checksum manifest; stable under repeated seeded execution.
paths=[ROOT/'data/synthetic'/'baseline_synthetic.csv',ROOT/'data/synthetic'/'heldout_synthetic.csv',ROOT/'results'/'metrics.json']
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
(ROOT/'results'/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(results,indent=2))
