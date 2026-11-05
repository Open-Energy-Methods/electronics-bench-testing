"""Offline evidence-integrity checks for EBT v0.5 PDR: NOT a safe-to-operate test."""
import csv
from decimal import Decimal
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]

def rows(rel):
 with (ROOT/rel).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

class PDRTests(unittest.TestCase):
 def test_priced_bom_totals_and_missing_quotes_remain_unpriced(self):
  items=rows('procurement/EBT-BOM-005.csv')
  self.assertEqual(len(items),16)
  self.assertEqual(len({x['item_id'] for x in items}),16)
  prices=[x for x in items if x['unit_price_sek_exvat']]
  self.assertEqual({x['item_id'] for x in prices},{'BOM-001','BOM-002'})
  total=Decimal('0')
  for x in items:
   if x['unit_price_sek_exvat']:
    value=Decimal(x['unit_price_sek_exvat'])*Decimal(x['qty'])
    self.assertEqual(value,Decimal(x['extended_price_sek_exvat']))
    self.assertTrue(x['source_url'].startswith('https://'))
    total+=value
   else:
    self.assertEqual(x['extended_price_sek_exvat'],'')
  self.assertEqual(total,Decimal('346.58'))
  self.assertEqual(len(items)-len(prices),14)

 def test_no_fabrication_promise_or_power_setpoint(self):
  docs=[
   'README.md','docs/EBT-PDR-005_engineering_design_review.md',
   'docs/EBT-MEC-005_manufacturing_review.md','electrical/EBT-EL-005_schematic_review.md'
  ]
  for doc in docs:
   t=(ROOT/doc).read_text(encoding='utf-8').upper()
   self.assertTrue(any(s in t for s in ('NOT','HOLD','UNRELEASED')))
   self.assertTrue(any(s in t for s in ('AUTHORIZ','APPROV','MANUFACT')))

 def test_sensor_channels_no_fake_calibration_results(self):
  channels=rows('metrology/EBT-MET-005_channels.csv')
  self.assertGreaterEqual(len(channels),10)
  ids={x['channel_id'] for x in channels}
  self.assertTrue({'EL_VH1','EL_VH2','EL_I','TH_CASE1','TH_CASE2','TH_NEAR1','TH_NEAR2','TH_AMB'} <= ids)
  for r in channels:
   self.assertEqual(r['actual_accuracy'],'')
   self.assertEqual(r['actual_rate_Hz'],'')
   self.assertNotIn('VERIFIED',r['status'].replace('UNVERIFIED',''))

 def test_electrical_nets_unique_and_source_branches(self):
  nets=rows('electrical/EBT-EL-005_nets.csv')
  names=[x['net_id'] for x in nets]
  self.assertTrue({'H1_POS','H2_POS','V_H1_PLUS','V_H1_MINUS','V_H2_PLUS','V_H2_MINUS','I_PLUS','I_MINUS'}<=set(names))
  self.assertEqual(len(names)-names.count('H_RET')+1,len(set(names)))
  self.assertTrue(all(x['status']=='DESIGN_NOT_AUTHORIZED' for x in nets))
  self.assertTrue(any(x['member_1']=='S1.A' for x in nets))
  self.assertTrue(any(x['member_1']=='S1.B' for x in nets))

 def test_schematic_and_plan_vectors_are_valid(self):
  for p in (ROOT/'drawings').glob('*.svg'):
   ET.parse(p)
   self.assertGreater(p.stat().st_size,3500)
  paths=[x.name for x in (ROOT/'drawings').glob('*.svg')]
  self.assertEqual(len(paths),3)
  dxf=(ROOT/'cad/EBT-MEC-005_layout_NOT_FOR_MANUFACTURE.dxf').read_text(encoding='ascii')
  self.assertIn('PLATE_ASSUMED',dxf)
  self.assertIn('DO NOT MACHINE',dxf)
  self.assertIn('SENSOR_TARGET',dxf)

 def test_evidence_register_labelled_instead_of_made_up(self):
  entries=rows('docs/EBT-PDR-005_evidence_register.csv')
  self.assertGreaterEqual(len(entries),10)
  classes={r['classification'] for r in entries}
  self.assertTrue({'SOURCE_SPECIFICATION','PRICE_SNAPSHOT','DESIGN_ASSUMPTION','NOT_EXISTING'}<=classes)
  self.assertTrue(all(r['release_blocker'] for r in entries))

if __name__=='__main__':unittest.main()
