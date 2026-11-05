"""Generate a technical PDF from the current reproducible synthetic study."""
from pathlib import Path
import json
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor, white
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'results/metrics.json').read_text())
OUT=ROOT/'docs'/'EBT_R01_Preproposal_Feasibility_v0.1.pdf'
NAVY=HexColor('#132840'); DARK=HexColor('#263a4d'); AQUA=HexColor('#1d7884'); GREY=HexColor('#566371'); PALE=HexColor('#eef3f5'); ORANGE=HexColor('#aa5929')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverEyebrowX',parent=styles['Normal'],fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=AQUA,spaceAfter=10))
styles.add(ParagraphStyle(name='CoverTitleX',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=25,leading=29,textColor=NAVY,spaceAfter=15,alignment=TA_LEFT))
styles.add(ParagraphStyle(name='CoverSubtitleX',parent=styles['Normal'],fontSize=12,leading=18,textColor=GREY,spaceAfter=18))
styles.add(ParagraphStyle(name='Head1X',fontName='Helvetica-Bold',fontSize=15,leading=19,textColor=NAVY,spaceBefore=14,spaceAfter=9,keepWithNext=True))
styles.add(ParagraphStyle(name='Head2X',fontName='Helvetica-Bold',fontSize=10.5,leading=14,textColor=AQUA,spaceBefore=11,spaceAfter=6,keepWithNext=True))
styles.add(ParagraphStyle(name='BodyX',fontName='Helvetica',fontSize=9.3,leading=14,textColor=DARK,spaceAfter=8))
styles.add(ParagraphStyle(name='SmallX',fontName='Helvetica',fontSize=8.4,leading=12,textColor=GREY,spaceAfter=6))
styles.add(ParagraphStyle(name='TinyX',fontName='Helvetica',fontSize=7.5,leading=10.5,textColor=DARK,spaceAfter=3))
styles.add(ParagraphStyle(name='CaptionX',fontName='Helvetica-Oblique',fontSize=8,leading=11,textColor=GREY,spaceAfter=11))
styles.add(ParagraphStyle(name='KPIValueX',fontName='Helvetica-Bold',fontSize=16,leading=20,textColor=NAVY,alignment=TA_CENTER))
styles.add(ParagraphStyle(name='KPILabelX',fontName='Helvetica',fontSize=8,leading=11,textColor=GREY,alignment=TA_CENTER))

P=lambda t,sty='BodyX':Paragraph(t,styles[sty])
S=[]

def heading(t):S.append(P(t,'Head1X'))
def sub(t):S.append(P(t,'Head2X'))
def body(t):S.append(P(t))
def tiny(t):S.append(P(t,'SmallX'))
def bullets(items):
    for t in items:S.append(P('<font color="#1d7884">&#8226;</font>  '+t,'BodyX'))
def table(headers, rows, widths=None, font=8):
    content=[[P(str(x),'TinyX') for x in headers]]+[[P(str(x),'TinyX') for x in row] for row in rows]
    if widths is None: widths=[(174*mm)/len(headers)]*len(headers)
    t=Table(content,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('BOX',(0,0),(-1,-1),0.35,HexColor('#cbd7de')),
                           ('INNERGRID',(0,0),(-1,-1),0.24,HexColor('#dbe2e8')),
                           ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
                           ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    S.append(t);S.append(Spacer(1,8))
def fig(name,caption,width=170*mm):
    from PIL import Image as PILImage
    with PILImage.open(ROOT/'figures'/name) as raw:
        w,h=raw.size
    im=Image(str(ROOT/'figures'/name),width=width,height=h*width/w)
    S.append(im);S.append(P(caption,'CaptionX'))
def page():S.append(PageBreak())

S.append(Spacer(1,32*mm))
S.append(P('OPEN ELECTROTHERMAL BENCH  /  EBT-R01','CoverEyebrowX'))
S.append(P('When Surface Temperatures Mislead','CoverTitleX'))
S.append(P('Computational feasibility study for measurement observability and cross-boundary validation of compact electrothermal models','CoverSubtitleX'))
S.append(HRFlowable(width='100%',thickness=1.6,color=AQUA,spaceBefore=5,spaceAfter=17))
S.append(P('<b>Independent research programme</b>  |  November 5, 2026  |  Draft v0.1','BodyX'))
S.append(P('<b>Researcher:</b> Abhijith Sivaprasadan  |  ORCID 0000-0003-0299-5745','BodyX'))
S.append(P('<font color="#aa5929"><b>STATUS: SYNTHETIC RESULTS ONLY.</b></font> No physical measurements, equipment calibration, institutional approval, KTH sponsorship, or experimental validation has occurred. The numerical results demonstrate problem feasibility and software verification, not the thermal behaviour of any real MOSFET.','BodyX'))
S.append(Spacer(1,18*mm))
S.append(P('Purpose of this dossier','Head2X'))
body('Establish a credible, testable research problem before contacting KTH: working code, a physical conservation model, independently held-out numerical scenarios, a targeted literature assessment, an instrumented bench concept and explicit research/approval gates.')
S.append(Spacer(1,22*mm))
tiny('Companion reproducibility package: source code, seven automated tests, synthetic CSV outputs, figures, metrics, study protocol and bibliography. Code MIT; original documentation and generated synthetic data CC BY 4.0.')
page()

heading('Executive technical summary')
body('The proposed paper studies a measurement-design problem: can package and heatsink sensors adequately constrain the internal temperatures predicted by compact electrothermal models, and can a model identified under one thermal boundary predict a different cooling or interface configuration? The present numerical benchmark is deliberately small and transparent. It is a method-shakedown, not evidence of novelty or hardware accuracy.')
S.append(Spacer(1,2*mm))
metrics=[
    (f"{DATA['max_alternate_case_diff_C']:.3f} °C",'maximum difference between two synthetic case-temperature traces'),
    (f"{DATA['max_alternate_junction_diff_C']:.2f} °C",'maximum hidden junction-temperature difference for those same models'),
    (f"{DATA['forced_fixed_rmse_C']:.2f} °C",'forced-convection holdout RMSE: fixed-boundary 1RC model'),
    (f"{DATA['forced_boundary_aware_rmse_C']:.2f} °C",'same holdout RMSE: 1RC with independently supplied synthetic boundary R')
]
rows=[]
for v,label in metrics: rows.append([P(v,'KPIValueX'),P(label,'KPILabelX')])
t=Table(rows,colWidths=[40*mm,130*mm],rowHeights=[24*mm]*4)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('LINEBELOW',(0,0),(-1,-2),0.7,white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),8)]));S.append(t)
S.append(Spacer(1,9*mm))
sub('What these numbers establish')
bullets(['A pair of <b>synthetically defined</b> assemblies can have similar externally observable temperatures but different internal states.',
         'An unchanged boundary model may fail on a different cooling configuration even when its original fit is respectable.',
         'Updating a boundary resistance known independently by construction can materially improve a synthetic holdout; this is <b>not</b> a verified real-world measurement strategy.',
         'The benchmark verifies equations and proposes where physical instrumentation will be needed. It does <b>not</b> establish junction-temperature accuracy for a physical device.'])
sub('Primary research risk')
body('Theoretical identifiability and thermal model validation are extensively covered in prior work. Scientific novelty remains unproven. The most promising differentiated output would be a properly controlled open experimental benchmark that quantifies cross-assembly transfer, measurement observability and uncertainty together.')
page()

heading('1. Physical model and numerical verification')
body('The synthetic model consists of three energy-storing nodes: internal junction j, sensor-accessible package p and heat sink s. The heat path includes junction-to-package Rjp, package-to-sink Rps and sink-to-ambient Rsa; input power P is applied at j. All node heat capacities and resistances are positive.')
S.append(P('<b>Governing balances</b>','Head2X'))
for eq in ['Cj dTj/dt = P - (Tj - Tp)/Rjp',
           'Cp dTp/dt = (Tj - Tp)/Rjp - (Tp - Ts)/Rps',
           'Cs dTs/dt = (Tp - Ts)/Rps - (Ts - Ta)/Rsa']:
    S.append(P(eq,'BodyX'))
body('Constants: Rjp = 0.75 K/W, Rps = 0.45 K/W, Rsa = 3.00 K/W; Cj = 0.60 J/K, Cp = 9.0 J/K, Cs = 70 J/K; Ta = 24 °C. A 5 W step runs for 750 s, then power is removed. A 5 s sampled exact zero-order-hold propagator eliminates dependence on a numerical ODE time step at sampling boundaries.')
fig('01_three_node_response.png','Figure 1. All lines are generated by the numerical model. The junction trace is a simulated hidden state, not a measurement.')
sub('Verification activities passed')
body('Seven automated tests verify zero-power ambient equilibrium, analytical steady-state limit, passive temperature ordering, grid-invariant sampled solution, approximate energy conservation, the single-RC steady-state formula and cooling response to changed thermal boundary. The total relative discrete energy-balance residual is '+f"{DATA['energy_balance_relative_residual']:.2e}"+' at a 1 s integration grid. This is a solver/implementation check only.')
page()

heading('2. Identifiability counterexample')
body('We compare two otherwise identical synthetic systems: A with Rjp = 0.75 K/W, and B with Rjp = 1.50 K/W. Both have the same input power, ambient temperature, case/sink resistances and capacities. The package is assumed to be the instrumented observable; the junction is inaccessible to a surface thermometer.')
fig('02_surface_blind_spot.png','Figure 2. Both package-temperature trajectories closely overlap, whereas the modelled internal junction trajectories diverge.')
body('Across the prescribed time history, the maximum package discrepancy is '+f"<b>{DATA['max_alternate_case_diff_C']:.3f} °C</b>"+' while the maximum junction difference is '+f"<b>{DATA['max_alternate_junction_diff_C']:.2f} °C</b>"+'. The synthetic measurement-noise standard deviation is assumed to be 0.15 °C. Hence the maximum package change is smaller than a single assumed noise standard deviation, even though internal temperature differs by several degrees. This does not prove global parameter non-identifiability or define a detection probability: those require a formal likelihood, noise-correlation and power analysis.')
sub('Implication for instrument selection')
body('A package thermocouple and thermal camera both measure surface quantities. Agreement between them cannot, by itself, validate junction temperature. Future experiment designs need either a qualified junction-sensitive electrical measurement, an externally constrained inner thermal path, or an explicitly bounded junction uncertainty. This limitation must appear in all claims.')
page()

heading('3. Holdout prediction under changed cooling')
body('A single first-order RC model is fitted only to a synthetic noisy package temperature measured during 5 W natural cooling. Independent synthetic cases are reserved for evaluation: a 3 W power change, forced convection (Rsa = 0.90 K/W) and a changed interface (Rps = 1.00 K/W). The 0.15 °C sensor-noise assumption is used for all nominal noisy traces.')
fig('03_boundary_transfer.png','Figure 3. In this synthetic holdout, an unchanged lumped thermal boundary overpredicts temperatures under forced convection. Supplying an independently known boundary R improves predictions.')
table(['Test condition','Evaluation model','RMSE (°C)'],[
    ('5 W natural (calibration)','fixed 1RC',f"{DATA['train_rmse_C']:.3f}"),
    ('3 W natural (holdout)','fixed 1RC',f"{DATA['same_boundary_3W_rmse_C']:.3f}"),
    ('5 W forced (holdout)','fixed 1RC',f"{DATA['forced_fixed_rmse_C']:.3f}"),
    ('5 W forced (same holdout)','boundary-aware 1RC',f"{DATA['forced_boundary_aware_rmse_C']:.3f}"),
    ('5 W modified interface (holdout)','unadapted fixed 1RC',f"{DATA['interface_unmodelled_rmse_C']:.3f}")
], [50*mm,84*mm,36*mm])
body('The boundary-aware model changes an independently supplied Rsa input, not a parameter inferred from held-out case temperatures. That is a necessary anti-leakage condition, but in hardware Rsa will itself require measurement and uncertainty. These results demonstrate a feasible research methodology, not comparative accuracy of actual physical models.')
page()

heading('4. Cross-case model performance')
fig('04_case_metrics.png','Figure 4. Errors compare model outputs with simulated noisy package data only; held-out scenarios remain excluded from calibration.')
sub('Interpretation and limitations')
bullets(['Calibration RMSE is '+f"{DATA['train_rmse_C']:.3f} °C"+', greater than the 0.15 °C injected noise scale: there is structural mismatch between a one-state compact model and a three-node system.',
         'The forced-convection error changes substantially with boundary information. This alone is not novel; it motivates independent boundary characterization and fair comparisons.',
         'Modified interface behavior remains inadequately modeled: an airflow-only correction does not resolve mounting/thermal-contact changes.',
         'The synthetic truth model has fixed linear parameters, deterministic power delivery, known ambient and independent Gaussian sensor noise. Real devices introduce nonlinearity, measurement lag, contact variation, airflow uncertainty and electrical loss dynamics.'])
sub('Evidence required to upgrade to a paper')
body('The physical campaign must predefine held-out hardware configurations; independently characterize boundary and mounting conditions; evaluate a qualified temperature measurement system; document variation across genuine remounts; and report predictive performance with uncertainty and limits. A specific narrow contribution must survive a full-paper literature review.')
page()

heading('5. Draft experimental campaign (not authorized)')
body('Use an appropriately rated low-voltage MOSFET assembly and a separate resistive reference heater. Provide a repeatable mechanical mount, appropriate heat sink, controlled source, measured dissipation, ambient reference, at least package and sink temperature sensors, and synchronized data acquisition. An internal junction-temperature reference is conditional on technical feasibility and suitable calibration. Do not equate case temperature with junction temperature.')
table(['Factor','Candidate structure','Reason'],[
 ('Input dissipation','3 safely qualified levels','Estimate load dependence and boundary transfer'),
 ('Cooling','3 regimes, monitored','Separate natural and forced boundary conditions'),
 ('Thermal interface','2 defined assembly configurations','Quantify contact/assembly sensitivity'),
 ('Replicates','3 independent remounts per configuration','Estimate assembly repeatability'),
 ('Initial envelope','54 candidate independent runs','Pilot must confirm statistical precision and time budget'),
 ('Withheld validation','Entire cooling/mounting configurations','Prevent time-series leakage from correlated samples')
],[40*mm,51*mm,79*mm])
sub('Laboratory prerequisites')
bullets(['Written facility permission for energized testing; do not perform energized tests in manufacturing-only workshops.',
         'Approved schematic, current/voltage/safe operating area review, current limit, protection and emergency shutdown.',
         'Sensor and instrument identification with calibration evidence/qualified verification, synchronized timestamps, uncertainty budget.',
         'A written operator procedure with temperature stop limits, supervised test scope and failed-run preservation.',
         'Permission for publishing allowed photographs, manufacturer information and non-confidential facility records.'])
sub('Pilot go/no-go criteria')
body('Proceed to a main campaign only when the chosen circuit is demonstrably safe under expected worst-case conditions, sensor lag and repeatability are quantified, test time is feasible, the intended boundary can be measured independently, and the research objective is not already fully resolved by accessible literature.')
page()

heading('6. Relevant prior art and novelty controls')
table(['Source','Existing contribution','What we must NOT claim'],[
  ('Putthong et al. (2026), DOI 10.53941/perat.2026.100014','SVD/information-sufficient design and held-out predictions on electrothermal MOSFET models','Novelty of experiment design or out-of-sample assessment alone'),
  ('Schulz et al. (2026), IEEE TPEL, accepted','Resolvable Cauer network layers, profile likelihood','Discovery of Cauer non-identifiability'),
  ('Zhang et al. (2024), DOI 10.1109/TPEL.2024.3367854','Regularized transient thermal parameter identification','Novelty of sparse thermal identification'),
  ('Ress et al. (2026), DOI 10.3390/en19112678','Improved thermal transient measurements for wide-bandgap devices','New thermal transient measurement concept absent comparison'),
  ('Bhadoria (2025), KTH PhD thesis','SiC cooling, microchannels, thermal and overcurrent response','Novel SiC cooling comparison'),
  ('Cnudde et al. (2026), THERMINIC','Experimental lumped spreading-resistance model validation','Novelty of lumped electronics thermal validation alone')
],[43*mm,65*mm,62*mm])
body('<b>Current defensible positioning:</b> an open protocol and benchmark studying the joint measurement/transfer/uncertainty problem in a specific accessible cooling assembly. This is a <b>potential contribution</b>, not a verified gap. Full-text review, systematic citation search and independent scholarly feedback are required before using words such as "novel" in an abstract.')
sub('Technical framework references')
body('ISO/IEC 17025:2017 provides laboratory competence principles (no accreditation claimed). JCGM 100:2008 and its 2026 amendment provide an uncertainty framework. ASME V&V 20-2009 (R2021) offers concepts for specified validation points in CFD and heat transfer. JEDEC JESD51 methods may be applicable to device-level thermal measurement, but no JEDEC procedure has been performed here.')
page()

heading('7. Reproduction, open data and publication path')
sub('Deliverable package already available')
body('The accompanying archive contains a physics solver, exact sampled propagator, 7 executable tests, reproducible simulation script, generated CSV results, integrity hashes, four plots, scope/governance documents, draft physical test procedure and an explicit literature-gap tracker. All provided data are synthetic and are labeled as such at file and column level.')
body('<b>Reproduction commands:</b> create a Python environment; install requirements; install the project editable; run <font face="Courier">python -m pytest -q</font> followed by <font face="Courier">python scripts/run_study.py</font>. The random seed is fixed at 20261105. Verify expected JSON results in <font face="Courier">results/metrics.json</font>. The synthetic CSV and JSON outputs are hashed in <font face="Courier">results/SHA256SUMS.json</font>.')
sub('Next phases')
table(['Gate','Evidence needed'],[
 ('G1: Scientific gap','Full-text literature matrix and bounded contribution reviewed by a researcher'),
 ('G2: Physical feasibility','Authorized lab, supported device, qualified sensors and power system'),
 ('G3: Pilot','Observed repeatability, verified safety envelope and realistic runtime'),
 ('G4: Primary experiment','Replicated measured data, blind holdouts and uncertainty analysis'),
 ('G5: Paper readiness','External methodological critique, clean reproduction, scientific interpretation'),
 ('G6: Public release','Permissions, GitHub, Zenodo DOI, honest technical post; scholarly venue if merited')
],[40*mm,130*mm])
sub('KTH contact after tangible progress')
body('The current package is enough to support a serious <b>methodology discussion</b>, but not yet a publication proposal based on empirical findings. The most valuable next evidence is an independently characterized benchtop data set that demonstrates where surface-only observations succeed or fail. Collaboration cannot be assumed: authorship, supervision, permissions and data rights must be agreed explicitly.')
sub('Reference links (selected)')
for txt in [
 'Putthong et al. (2026): https://doi.org/10.53941/perat.2026.100014',
 'Schulz et al. (2026): https://erickschulz.dev/publications/src/data/publications/identifiability-cauer-thermal-networks/',
 'Zhang et al. (2024): https://doi.org/10.1109/TPEL.2024.3367854',
 'Ress et al. (2026): https://doi.org/10.3390/en19112678',
 'JCGM guides: https://www.bipm.org/en/committees/jc/jcgm/publications',
 'ASME V&V 20: https://www.asme.org/codes-standards/find-codes-standards/standard-for-verification-and-validation-in-computational-fluid-dynamics-and-heat-transfer',
 'ISO 17025: https://www.iso.org/standard/66912.html'
]:S.append(P(txt,'TinyX'))

def footer(canvas,doc):
    canvas.saveState()
    w,h=A4
    canvas.setStrokeColor(HexColor('#dbe3e8'))
    canvas.line(19*mm,17*mm,w-19*mm,17*mm)
    canvas.setFont('Helvetica',8);canvas.setFillColor(GREY)
    canvas.drawString(19*mm,12*mm,'EBT-R01  |  independent synthetic feasibility study  |  NOT experimental validation')
    canvas.drawRightString(w-19*mm,12*mm,f'{doc.page}')
    canvas.restoreState()

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=19*mm,leftMargin=19*mm,topMargin=19*mm,bottomMargin=23*mm,title='EBT-R01 When Surface Temperatures Mislead - Synthetic Feasibility',author='Abhijith Sivaprasadan',subject='Open Electrothermal Bench pre-proposal and numerical feasibility, not experimental')
doc.build(S,onFirstPage=footer,onLaterPages=footer)
print(OUT)
