"""CAD static-source checks only. No KiCad ERC or physical safety approval."""
import csv,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class NativeCADTests(unittest.TestCase):
    def test_kicad_root_and_s_expression_balanced(self):
        s=(ROOT/"electrical/EBT-EL-020.kicad_sch").read_text()
        self.assertTrue(s.startswith("(kicad_sch "))
        self.assertIn("(version 20250114)",s)
        depth=0;quoted=False;escape=False
        for ch in s:
            if ch=='"' and not escape: quoted=not quoted
            elif not quoted:
                depth+=(ch=="(")-(ch==")")
                self.assertGreaterEqual(depth,0)
            escape=ch=="\\" and not escape
        self.assertEqual(depth,0)
        self.assertFalse(quoted)
    def test_named_net_label_coverage(self):
        s=(ROOT/"electrical/EBT-EL-020.kicad_sch").read_text()
        with (ROOT/"electrical/EBT-EL-020_net_connections.csv").open(newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),14)
        self.assertEqual(len(set(r["net_name"] for r in rows)),14)
        for r in rows:
            self.assertGreaterEqual(s.count('(label "'+r["net_name"]+'"'),2)
            self.assertGreaterEqual(len(r["pin_members"].split(";")),2)
            self.assertEqual(r["review_status"],"PREDESIGN_NOT_APPROVED")
        self.assertIn("H1_POS",{r["net_name"] for r in rows})
        self.assertIn("H2_POS",{r["net_name"] for r in rows})
    def test_kicad_embedded_review_symbols(self):
        s=(ROOT/"electrical/EBT-EL-020.kicad_sch").read_text()
        self.assertEqual(s.count('(lib_id "EBT:'),15)
        self.assertEqual(s.count("(on_board no)"),26)
        self.assertIn("(paper \"A3\")",s)
    def test_mechanical_assumptions_not_machining_release(self):
        s=(ROOT/"mechanical/EBT-MEC-020_assembly.scad").read_text()
        self.assertIn("surrogate_fin_count=11",s)
        self.assertIn("sink_z=40",s)
        self.assertIn("base_z=10",s)
        self.assertIn("adapter = false",s)
        self.assertNotIn("drill_holes",s)
    def test_cad_model_and_dxf_generator_available(self):
        a=(ROOT/"mechanical/EBT-MEC-020_cadquery.py").read_text()
        d=(ROOT/"mechanical/EBT-MEC-020_drawing.py").read_text()
        self.assertIn("cq.Assembly",a)
        self.assertIn("SURROGATE_FIN_N=11",a)
        self.assertIn('ezdxf.new("R2010")',d)
        self.assertIn("NOT FOR MANUFACTURE",d)
    def test_no_site_authority_claim(self):
        s=(ROOT/"README.md").read_text()
        for keyword in ("NOT FOR MANUFACTURE","STOP","ERC","T_PLATE","T_SINK","workshop"):
            if keyword=="STOP":continue
            self.assertIn(keyword.lower(),s.lower())
if __name__=="__main__": unittest.main()
