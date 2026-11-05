"""Generate formulas and source-backed PDR procurement workbook with artifact_tool."""
from __future__ import annotations
import csv
from pathlib import Path
from artifact_tool import Workbook,SpreadsheetFile
ROOT=Path(__file__).resolve().parent
rows=list(csv.DictReader((ROOT/'EBT-BOM-005.csv').open(encoding='utf-8',newline='')))
wb=Workbook.create(); s=wb.worksheets.add('BOM and Costs'); e=wb.worksheets.add('Evidence Rules')
headers=['Item','Category','Requirement / item','Exact / proposed MPN','Qty','Unit','Unit SEK ex VAT','Ext SEK ex VAT','Status','Source URL','Hold / release blocker']
s.get_range('A1:K1').values=[headers]
value_rows=[]
for r in rows:
 try:cost=float(r['unit_price_sek_exvat'])
 except:cost=None
 value_rows.append([r['item_id'],r['category'],r['description'],r['manufacturer_part'],int(r['qty']),r['unit'],cost,None,r['status'],r['source_url'],r['purchase_gate']])
s.get_range(f'A2:K{1+len(rows)}').values=value_rows
for n in range(2,2+len(rows)):
 s.get_range(f'H{n}').formulas=[[f'=IF(G{n}="","",E{n}*G{n})']]
end=1+len(rows)
s.get_range('M1:N1').values=[['Cost summary','SEK / number']]
s.get_range('M2:N2').values=[['VAT example factor',0.25]]
s.get_range('M3').values=[['Quoted items ex VAT (partial)']]
s.get_range('N3').formulas=[[f'=SUM(H2:H{end})']]
s.get_range('M4').values=[['Count priced BOM lines']]
s.get_range('N4').formulas=[[f'=COUNT(G2:G{end})']]
s.get_range('M5').values=[['Count unpriced BOM lines']]
s.get_range('N5').formulas=[[f'=COUNTA(A2:A{end})-N4']]
s.get_range('M6').values=[['Quote partial incl illustrative VAT']]
s.get_range('N6').formulas=[['=N3*(1+N2)']]
s.get_range('M8:N8').values=[['Important','PARTIAL QUOTES ONLY']]
s.get_range('M9:N9').values=[['Site items uninspected','No procurement authorization']]
s.get_range('M10:N10').values=[['2026-11-05','Prices require checkout review']]
s.get_range('M11:N11').values=[['Do not infer','Full rig cost or safe power']]
# Give columns sensible sizes and styled regions
s.get_range('A1:K1').format={'fill':'#163448','font':{'bold':True,'color':'#FFFFFF'},'row_height':31}
s.get_range('M1:N1').format={'fill':'#163448','font':{'bold':True,'color':'#FFFFFF'},'row_height':31}
widths={'A':12,'B':16,'C':40,'D':31,'E':9,'F':9,'G':18,'H':20,'I':29,'J':45,'K':45,'M':36,'N':24}
for k,w in widths.items(): s.get_range(f'{k}:{k}').format.column_width=w
s.get_range(f'A2:K{end}').format.wrap_text=True
s.get_range(f'A2:K{end}').format.row_height=56
s.get_range(f'G2:H{end}').set_number_format('#,##0.00 "kr"')
s.get_range('N2').set_number_format('0%')
s.get_range('N3').set_number_format('#,##0.00 "kr"')
s.get_range('N6').set_number_format('#,##0.00 "kr"')
s.get_range('M8:N8').format={'fill':'#FFF1E6','font':{'bold':True,'color':'#9A3D19'}}
s.freeze_panes.freeze_rows(1)
# evidence worksheet uses explicit facts, no estimates disguised as quotes
records=[
['Source / assumption','Status','Source or constraint'],
['Bourns PWR220T-20-10R0F', 'Maker part + Farnell price checked, NOT ORDERED', 'https://se.farnell.com/en-SE/c/passive-components/resistors-fixed-value/through-hole-resistors?brand=bourns&resistance=10ohm'],
['Fischer SK 92 100 SA','Maker part + Farnell price checked, NOT ORDERED','https://se.farnell.com/fischer-elektronik/sk-92-100-sa/heat-sink-100mm-1-4-c-w/dp/4621580'],
['Aluminium adapter plate 100 x 100 x 4','DESIGN ASSUMPTION ONLY', 'Actual sink base/contact geometry not verified; do not machine'],
['Temperature sensors / RTDs','SITE EQUIPMENT UNKNOWN','No calibration or sensor lag evidence; do not assume vendor accuracy achieved'],
['NI 9213','OPTIONAL EXAMPLE ONLY','https://www.ni.com/en-us/shop/model/ni-9213.html'],
['Complete project cost','NOT AVAILABLE','No site equipment list and 14 BOM lines not priced'],
['Energized work','NOT AUTHORIZED','Physical laboratory permission / induction / safe limits pending'],
['Manufacturer rating','NOT A TEST SETPOINT','20 W only at manufacturer-defined 25C case rating'],
['Farnell price tax basis','EX VAT','Confirmed from Swedish listings, actual checkout must be checked']
]
e.get_range(f'A1:C{len(records)}').values=records
e.get_range('A1:C1').format={'fill':'#163448','font':{'bold':True,'color':'#FFFFFF'},'row_height':30}
for col,w in {'A':34,'B':35,'C':70}.items():e.get_range(f'{col}:{col}').format.column_width=w
e.get_range(f'A2:C{len(records)}').format.wrap_text=True
e.get_range(f'A2:C{len(records)}').format.row_height=48
e.freeze_panes.freeze_rows(1)
# Inspect and export
print(wb.inspect({'kind':'table','range':'BOM and Costs!M1:N6','include':'values,formulas','table_max_rows':7,'table_max_cols':2}).ndjson[:1300])
p=ROOT/'EBT-BOM-005_budget.xlsx';SpreadsheetFile.export_xlsx(wb).save(str(p))
print('Wrote',p,p.stat().st_size)
