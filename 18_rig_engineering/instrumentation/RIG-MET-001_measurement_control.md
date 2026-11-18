# RIG-MET-001 — Instrumentation and controls architecture

The rig is a measurement system, not just a powered fixture. The actual
laboratory instruments are to be surveyed before selection. Use purchased
commercial lab equipment where qualified; no custom mains implementation.
 
| Tag | Measurement | Intended instruments, actual model TBD |
|---|---|---|
| E-101 | DUT terminal differential V | suitable isolated/differential DAQ or DMM; approved probes for scope |
| E-102 | same branch I | calibrated current instrument or Kelvin shunt with suitable differential readout |
| E-103 | transient V/I | scope + correctly rated differential/isolated probes, bandwidth/attenuation verified |
| T-201 | accessible DUT case | contact thermometry, no internal junction assertion |
| T-202/T-203 | near-source surface, physically T_PLATE or T_SINK | thermometry with documented datum/attachment/lag |
| T-204 | far surface | optional, same surface definition |
| T-205 | local ambient | shielded sensor at verified approach position |
| T-206 | duct inlet/outlet | optional pair, differential uncertainty and flow mixing |
| F-301 | air velocity/flow | actual appropriate calibrated instrument, traverse/geometry |
| N-301 | fan speed | actual qualified tach interface, NOT direct flow inference |
| C-701 | chamber data | setpoint and independent loaded ambient reading separate |
| S-401 | protection/isolated state feedback | read-only status from independently reviewed protective chain |

Measurement planning: choose sensor range, resolution, bandwidth and timing
from actual pilot response; scope is for transients, DAQ for synchronized
long-duration records. Verify probe grounding, common-mode, input loading,
attenuation, offset, actual timestamp skew and acquisition anti-aliasing.
Never defeat protective earth or attach grounded scope clips to arbitrary
floating nodes. Use documented reference instruments and serials/certificates
where permitted. Temperature calibration should cover intended operating
range and installed chain, not just sensor vendor tolerance.
 
Uncertainty: u(P)^2 = I^2 u(V)^2 + V^2 u(I)^2 + 2VI cov(V,I).
For temperature difference use covariance of common references; apparent R
propagation includes covariance of power and temperature. Include attachment
repeatability, airflow nonuniformity, timing, offset and instrument drift.
Type A covariance and between-mount scatter require real repeated results.
Do not assume measured terminal power all enters sink.

Functional control states: ISOLATED, IDLE, PRECHECK, READY, RUN, CONTROLLED_STOP,
FAULT_LATCHED. Transitions require site-approved interlocks/authority; a fault
requires safe isolation independent of software; manual reset is not restart.
Host control can request operation but cannot be the protective device.
Record alarms, first-out cause, operator acknowledgement, actual stop status,
sensor dropout and configuration changes. Define actual hazard-based states
and thresholds at RD3/RD5, not here. No unattended or automatic commissioning.
 
Acceptance work uses dummy/simulated signals before hardware integration;
only a competent reviewer authorizes real tests, including fault response.
Raw acquisition exports retain existing EBT-RUN-008 schema for required
columns and metadata. Add a version-controlled companion channel map and
separate optional high-rate waveform/airflow archive; no silent reinterpretation
of raw columns. Q0 P/R data remain exploratory; R01 independent roles remain.
