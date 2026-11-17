"""EBT-MEC-020: generate ASCII DXF REV A for engineering review, NOT manufacture."""
from pathlib import Path
import argparse
import ezdxf
from ezdxf.enums import TextEntityAlignment

def create(path):
    doc=ezdxf.new("R2010"); doc.units=4
    m=doc.modelspace()
    for name,color in [("OUTLINE",7),("REVIEW_TEXT",3),
                       ("DIM_NOMINAL",4),("UNVERIFIED",1),("FRAME",8)]:
        doc.layers.new(name,dxfattribs={"color":color})
    def line(x1,y1,x2,y2,layer="OUTLINE"):
        m.add_line((x1,y1),(x2,y2),dxfattribs={"layer":layer})
    def rect(x,y,w,h,layer="OUTLINE"):
        m.add_lwpolyline([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],close=True,
                         dxfattribs={"layer":layer})
    def txt(s,x,y,h=3,layer="REVIEW_TEXT"):
        m.add_text(s,dxfattribs={"layer":layer,"height":h}).set_placement(
          (x,y),align=TextEntityAlignment.LEFT)
    rect(0,0,420,297,"FRAME");rect(7,7,406,283,"FRAME")
    txt("EBT-MEC-020 | Concept review drawing, dimensions mm",14,280,6)
    txt("NOT FOR MANUFACTURE - no drill/fastener design or power release",14,268,3.4,"UNVERIFIED")
    txt("A. TOP / NOMINAL SINK ENVELOPE",22,243,4)
    rect(24,116,100,100)
    for i in range(11):
        x=24+(i+.5)*100/11
        line(x,116,x,216,"UNVERIFIED")
    txt("FIN COUNT/PITCH UNVERIFIED",24,110,2.5,"UNVERIFIED")
    line(24,116,24,100,"DIM_NOMINAL")
    line(124,116,124,100,"DIM_NOMINAL")
    line(24,103,124,103,"DIM_NOMINAL")
    txt("100 NOM",62,96,2.7,"DIM_NOMINAL")
    line(24,116,10,116,"DIM_NOMINAL")
    line(24,216,10,216,"DIM_NOMINAL")
    line(13,116,13,216,"DIM_NOMINAL")
    txt("100 NOM",9,165,2.7,"DIM_NOMINAL")
    txt("B. SECTION / BASE & SURROGATE FINS",148,243,4)
    rect(149,170,100,10)
    for i in range(11):
        x=149+(i+.5)*100/11
        rect(x-1.1,180,2.2,30,"UNVERIFIED")
    line(254,170,267,170,"DIM_NOMINAL")
    line(254,180,267,180,"DIM_NOMINAL")
    line(263,170,263,180,"DIM_NOMINAL")
    txt("10 BASE",268,176,2.5,"DIM_NOMINAL")
    line(254,170,290,170,"DIM_NOMINAL")
    line(254,210,290,210,"DIM_NOMINAL")
    line(284,170,284,210,"DIM_NOMINAL")
    txt("40 TOTAL",292,190,2.4,"DIM_NOMINAL")
    txt("Heater contact face / thickness not verified",149,160,2.8,"UNVERIFIED")
    txt("C. UNDERSIDE HEATER SITES",277,231,4)
    rect(293,105,100,100)
    rect(311,148,10.1,14.6,"UNVERIFIED")
    rect(361,148,10.1,14.6,"UNVERIFIED")
    txt("H1",310,167,3);txt("H2",361,167,3)
    txt("SITE CENTRES: x=-25/+25 (unreleased)",280,95,2.7,"UNVERIFIED")
    txt("Direct sink: no plate; adapter: OPTIONAL 4 mm",19,76,3.1)
    txt("TO-220 placement is predesign, not hole coordinates",19,68,2.8,"UNVERIFIED")
    txt("No junction-temperature measurements claimed",19,60,2.8)
    txt("Fin shape, screws, TIM, isolation & fan omitted",19,51,2.8,"UNVERIFIED")
    rect(11,11,398,29,"FRAME")
    txt("Open Energy Methods | Q0 Rev PRE-DESIGN A | 2026-11-17",17,29,3.5)
    txt("Fischer SK92 nominal 100x100x40, 10 base; VERIFY AS-RECEIVED",17,21,2.8)
    txt("G2 HOLD / NOT RELEASED FOR FABRICATION OR POWER",17,14,2.8,"UNVERIFIED")
    doc.saveas(path)

def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument("--out",type=Path,default=Path("EBT-MEC-020_concept_review.dxf"))
    args=a.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True)
    create(args.out);print("Created",args.out)
if __name__=="__main__":main()
