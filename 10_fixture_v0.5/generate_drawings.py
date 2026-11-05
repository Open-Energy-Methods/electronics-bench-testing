#!/usr/bin/env python3
"""Create design-review SVG / DXF. NOT released fabrication files."""
from pathlib import Path
import math
import svgwrite as sw
import ezdxf
ROOT=Path(__file__).resolve().parent
DRAW=ROOT/'drawings'; CAD=ROOT/'cad'
DRAW.mkdir(exist_ok=True);CAD.mkdir(exist_ok=True)
FONT='DejaVu Sans,Arial,sans-serif'
INK='#202f3e'; MUTED='#5b7186'; BLUE='#1c779f'; AMBER='#b66c15'; RED='#bf3d38'; GREEN='#237460'
def setup(fname,w,h,title,sub):
 d=sw.Drawing(str(DRAW/fname),size=(str(w),str(h)),viewBox=f'0 0 {w} {h}')
 d.add(d.rect(insert=(0,0),size=(w,h),fill='#f8fafb'))
 d.add(d.rect(insert=(0,0),size=(w,72),fill=INK))
 d.add(d.text(title,insert=(28,32),font_size=23,fill='white',font_family=FONT,font_weight='bold'))
 d.add(d.text(sub,insert=(28,55),font_size=12,fill='#d0e2e9',font_family=FONT))
 return d
def txt(d,x,y,s,size=13,color=INK,weight='normal'):
 d.add(d.text(str(s),insert=(x,y),font_size=size,fill=color,font_family=FONT,font_weight=weight))
def line(d,x1,y1,x2,y2,color=MUTED,width=1.5,dash=None):
 kw={'start':(x1,y1),'end':(x2,y2),'stroke':color,'stroke_width':width}
 if dash:kw['stroke_dasharray']=dash
 d.add(d.line(**kw))
def dim(d,x1,y1,x2,y2,text,labelOffset=0):
 line(d,x1,y1,x2,y2,BLUE,1.4)
 ang=math.atan2(y2-y1,x2-x1)
 for x,y,flip in ((x1,y1,1),(x2,y2,-1)):
  a=ang if flip==1 else ang+math.pi
  p=[(x,y),(x+11*math.cos(a+.38),y+11*math.sin(a+.38)),(x+11*math.cos(a-.38),y+11*math.sin(a-.38))]
  d.add(d.polygon(p,fill=BLUE))
 txt(d,(x1+x2)/2-35+labelOffset,(y1+y2)/2-10,text,12,BLUE,'bold')

def mech_plan():
 d=setup('EBT-MEC-005_plan.svg',1250,845,'EBT-MEC-005  |  Plan view — preliminary','Rev 0.5 • units mm • design intent only • NOT FOR MANUFACTURE')
 s=5;ox,oy=355,430
 X=lambda x:ox+x*s;Y=lambda y:oy-y*s
 d.add(d.rect(insert=(X(-50),Y(50)),size=(100*s,100*s),fill='#e0edf2',stroke=INK,stroke_width=2))
 # assumed plate and heat sink plan
 for v in range(-40,50,10):
  line(d,X(v),Y(-50),X(v),Y(50),'#d0dfe4',.7)
  line(d,X(-50),Y(v),X(50),Y(v),'#d0dfe4',.7)
 for i,x in enumerate((-25,25),1):
  cx,cy=X(x),Y(0)
  d.add(d.rect(insert=(cx-10.1*s/2,cy-14.6*s/2),size=(10.1*s,14.6*s),fill='#fdebd5',stroke=AMBER,stroke_width=2))
  hx,hy=X(x),Y(4.8)
  d.add(d.circle(center=(hx,hy),r=3.6*s/2,fill='white',stroke=RED,stroke_width=2))
  d.add(d.rect(insert=(cx-10*s,cy-15*s),size=(20*s,30*s),fill='none',stroke=RED,stroke_dasharray='7,5',stroke_width=1))
  txt(d,cx-14,cy-6,f'H{i}',16,INK,'bold')
  txt(d,cx-20,cy+57,f'K-CASE{i}',11,AMBER)
  for xx,yy,label in [(x,-3,'CASE'),(x,-17,'PLATE')]:
   px,py=X(xx),Y(yy)
   d.add(d.circle(center=(px,py),r=5,fill=GREEN,stroke='white',stroke_width=1.5))
  txt(d,cx-35,Y(-17)+20,f'K-PLATE{i}',11,GREEN)
 d.add(d.circle(center=(X(0),Y(32)),r=6,fill=GREEN,stroke='white',stroke_width=1.5))
 txt(d,X(0)+12,Y(32)+4,'K-PLATE-FAR (optional)',11,GREEN)
 line(d,X(-50),Y(53),X(50),Y(53),BLUE,1)
 dim(d,X(-50),Y(59),X(50),Y(59),'100 mm envelope')
 dim(d,X(-59),Y(-50),X(-59),Y(50),'100 mm')
 dim(d,X(-25),Y(-42),X(25),Y(-42),'50 mm nominal site pitch')
 line(d,ox,Y(-50),ox,Y(50),MUTED,1,'5,5')
 line(d,X(-50),oy,X(50),oy,MUTED,1,'5,5')
 txt(d,ox+8,oy-6,'0,0',11,MUTED)
 d.add(d.rect(insert=(693,92),size=(527,670),fill='white',stroke='#d8e3ea',stroke_width=1.5,rx=12))
 info=[('SOURCE VERIFIED','SK 92 100 SA external envelope: 100 × 100 × 40 mm.'),('SOURCE VERIFIED','Bourns heater body: 10.1 × 14.6 mm; hole Ø3.6.'),('DESIGN ASSUMPTION','Aluminium adapter plate: 100 × 100 × 4 mm.'),('DESIGN ASSUMPTION','Two nominal sites: x = −25 and +25 mm, y = 0.'),('DESIGN ASSUMPTION','Package hole centre y = +4.8 mm in drawn orientation.'),('MISSING CRITICAL','Real extrusion flat base, fins, tap depth & clearance.'),('MISSING CRITICAL','Fastener, torque, interface material and insulation.'),('MISSING CRITICAL','Mounting-pad tolerances and sensor attachment geometry.'),('SCIENTIFIC WARNING','Both sites are NOT automatically thermally equivalent.'),('SCIENTIFIC WARNING','K-PLATE is not measured sink temperature by definition.')]
 yy=130
 for head,body in info:
  c=GREEN if head=='SOURCE VERIFIED' else AMBER if head=='DESIGN ASSUMPTION' else RED
  txt(d,718,yy,head,12,c,'bold');yy+=21
  txt(d,718,yy,body,12,INK);yy+=34
 txt(d,28,813,'Use editable DXF for geometry review only — all drill/tap operations blocked pending manufacturer section and host approval.',13,RED,'bold')
 d.save()
 # geometry DXF from same params, no cross-section drilling or toolpaths
 dwg=ezdxf.new('R2013'); dwg.header['$INSUNITS']=4
 for n,color in [('PLATE_ASSUMED',8),('DEVICE_ASSUMED',2),('KEEP_OUT',1),('SENSOR_TARGET',3),('TEXT',7)]:dwg.layers.new(name=n,dxfattribs={'color':color})
 ms=dwg.modelspace()
 ms.add_lwpolyline([(-50,-50),(50,-50),(50,50),(-50,50)],close=True,dxfattribs={'layer':'PLATE_ASSUMED'})
 for i,x in enumerate((-25,25),1):
  ms.add_lwpolyline([(x-10.1/2,-14.6/2),(x+10.1/2,-14.6/2),(x+10.1/2,14.6/2),(x-10.1/2,14.6/2)],close=True,dxfattribs={'layer':'DEVICE_ASSUMED'})
  ms.add_circle((x,4.8),radius=1.8,dxfattribs={'layer':'DEVICE_ASSUMED'})
  ms.add_lwpolyline([(x-10,-15),(x+10,-15),(x+10,15),(x-10,15)],close=True,dxfattribs={'layer':'KEEP_OUT'})
  ms.add_text(f'HEATER {i} PROVISIONAL',dxfattribs={'height':2.4,'insert':(x-13,-23),'layer':'TEXT'})
  for xx,yy in [(x,-3),(x,-17)]:ms.add_circle((xx,yy),radius=1,dxfattribs={'layer':'SENSOR_TARGET'})
 ms.add_circle((0,32),radius=1,dxfattribs={'layer':'SENSOR_TARGET'})
 ms.add_text('DESIGN REVIEW ONLY / DO NOT MACHINE',dxfattribs={'height':3.8,'insert':(-48,-58),'layer':'TEXT'})
 ms.add_text('MM  SK92-100-SA ENVELOPE ASSUMED',dxfattribs={'height':3,'insert':(-48,56),'layer':'TEXT'})
 dwg.saveas(CAD/'EBT-MEC-005_layout_NOT_FOR_MANUFACTURE.dxf')

def mech_section():
 d=setup('EBT-MEC-005_section.svg',1200,715,'EBT-MEC-005  |  Concept section — NOT dimensioned for manufacture','Nominal only • actual extrusion fin cross section not retrieved • thermal bypass unquantified')
 # Render heat sink fins conceptual under plate, not actual profile
 d.add(d.rect(insert=(175,325),size=(645,43),fill='#b8c9d0',stroke=INK,stroke_width=2))
 for x in range(175,820,34):
  d.add(d.rect(insert=(x,368),size=(16,148),fill='#93b2bd',stroke='#637f89',stroke_width=1))
 txt(d,185,542,'Heatsink SK 92 100 SA: known external 100 × 100 × 40 mm; fin outline symbolic',14,INK)
 d.add(d.rect(insert=(175,287),size=(645,32),fill='#ebc99a',stroke=AMBER,stroke_width=2))
 txt(d,845,309,'Adapter plate: 4 mm ASSUMED',13,AMBER)
 d.add(d.rect(insert=(175,319),size=(645,6),fill='#c7a376',stroke=AMBER,stroke_dasharray='4,3'))
 txt(d,845,340,'Plate/sink interface: TBD',13,AMBER)
 for x in (280,650):
  d.add(d.rect(insert=(x-42,198),size=(84,82),fill='#f5dec3',stroke=AMBER,stroke_width=2))
  d.add(d.rect(insert=(x-42,280),size=(84,6),fill='#c7a376',stroke=AMBER))
  d.add(d.circle(center=(x,215),r=11,fill='white',stroke=RED,stroke_width=2))
  d.add(d.circle(center=(x+24,227),r=5,fill=GREEN,stroke='white',stroke_width=1))
  line(d,x+24,227,x+60,170,GREEN,1.3)
  txt(d,x+56,167,'K-CASE',12,GREEN)
 txt(d,236,184,'H1 10 Ω',14,INK);txt(d,608,184,'H2 10 Ω',14,INK)
 txt(d,175,577,'Sensor near plate/sink interface may observe plate, not sink. Characterize real interface and gradients.',14,RED,'bold')
 txt(d,175,606,'Not to scale: heater bodies intentionally exaggerated; drawn stack is conceptual only.',13,MUTED)
 d.add(d.rect(insert=(160,635),size=(955,53),fill='#fceeee',stroke='#f1b3b3',rx=7))
 txt(d,183,669,'RELEASE HOLD: actual sink base thickness, contact plane, fasteners, TIM and electrical isolation not validated.',15,RED,'bold')
 d.save()

def elec_sch():
 d=setup('EBT-EL-005_measurement_schematic.svg',1380,900,'EBT-EL-005  |  Preliminary connection-level topology','Isolated bench DC supply, only one heater at a time • protective ratings not selected • DO NOT WIRE')
 # DC source and positive chain
 def box(x,y,w,h,l1,l2=''):
  d.add(d.rect(insert=(x,y),size=(w,h),rx=7,fill='white',stroke=INK,stroke_width=2))
  txt(d,x+13,y+27,l1,14,INK,'bold')
  if l2:txt(d,x+13,y+47,l2,11,MUTED)
 box(35,190,165,93,'PSU','isolated/current-limit')
 box(260,190,128,93,'S0 / STOP','rated DC open')
 box(450,190,122,93,'F1','DC fuse TBD')
 box(640,190,160,93,'S1','centre OFF/BBM')
 line(d,200,235,260,235,BLUE,3);line(d,388,235,450,235,BLUE,3);line(d,572,235,640,235,BLUE,3)
 line(d,800,216,858,216,BLUE,2.5);line(d,858,216,858,149,BLUE,2.5);line(d,858,149,900,149,BLUE,2.5)
 line(d,800,257,858,257,BLUE,2.5);line(d,858,257,858,365,BLUE,2.5);line(d,858,365,900,365,BLUE,2.5)
 box(900,111,173,81,'H1 / 10 Ω','Bourns TO-220')
 box(900,325,173,81,'H2 / 10 Ω','Bourns TO-220')
 # returns to shunt and negative
 line(d,1073,153,1115,153,INK,2.5);line(d,1115,153,1115,466,INK,2.5)
 line(d,1073,367,1115,367,INK,2.5)
 box(945,452,164,73,'I-SENSE','4-wire shunt TBD')
 line(d,1115,466,1109,466,INK,2.5)
 line(d,945,490,212,490,INK,2.5);line(d,212,490,212,270,INK,2.5);line(d,212,270,200,270,INK,2.5)
 txt(d,35,329,'Only H1 or H2 energized',15,RED,'bold')
 txt(d,35,348,'Switch type/rating not approved.',12,RED)
 # Kelvin channels
 for y,label in [(151,'V_H1 differential'),(367,'V_H2 differential')]:
  line(d,914,y-35,914,y-47,GREEN,1.8)
  line(d,1059,y-35,1059,y-47,GREEN,1.8)
  txt(d,925,y-54,label+' (Kelvin)',12,GREEN,'bold')
 box(740,535,310,74,'DA / VOLTAGE CHANNELS','isolated true differential required')
 line(d,914,109,914,105,GREEN,1.6)
 txt(d,790,631,'NOT ordinary scope earth clips',13,RED,'bold')
 box(740,667,310,75,'TEMP LOGGER','Tcase1/2 Tplate1/2 Tamb')
 box(1091,667,237,75,'FAN (separate PSU)','tach/airflow TBD')
 d.add(d.rect(insert=(28,764),size=(1317,103),fill='#fceeee',stroke='#e6a4a4',rx=6))
 txt(d,51,798,'DRAWING IS A TOPOLOGY REVIEW — NOT A SITE-APPROVED ELECTRICAL SCHEMATIC',20,RED,'bold')
 txt(d,51,828,'PSU/S0/F1/S1/shunt wire gauge, protection ratings, DAQ earth/isolation and interlocks are TBD.',14,INK)
 txt(d,51,850,'Read electrical/EBT-EL-005_nets.csv for exact intended net names. Fan supply/ground remains separate.',13,INK)
 txt(d,50,83,'Power path (blue) • branch return (black) • measurement taps (green)',12,MUTED)
 d.save()

if __name__=='__main__':
 mech_plan();mech_section();elec_sch()
 print('Generated 3 SVG design-review drawings + editable DXF')
