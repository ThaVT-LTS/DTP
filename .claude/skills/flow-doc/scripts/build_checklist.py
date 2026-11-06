# Flow checklist (Excel) tied to the flow Word files: one row per "Step n", UC ID (v6.x), wave from the Plan,
# known open bugs, Pass/Fail for the customer. Rows outside the current round are greyed and locked.
# Usage: python -I build_checklist.py <checklist-map.json> <specs dir> <UC xlsx> <Plan xlsx> <bugs.md> <out.xlsx>
import json, re, sys, os
from collections import defaultdict
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image as XLImage

MAP, SPECS, UCX, PLANX, BUGS, OUT = sys.argv[1:7]
M = json.load(open(MAP, encoding='utf8'))
ROUND = M.get('round', 1)

uc = {}
for r in openpyxl.load_workbook(UCX, read_only=True, data_only=True)['P1 Use Cases'].iter_rows(min_row=2, values_only=True):
    if r[1]: uc[str(r[1]).strip()] = {'name': str(r[2] or ''), 'actor': str(r[3] or ''), 'portal': str(r[4] or '')}
plan = {}
for r in openpyxl.load_workbook(PLANX, read_only=True, data_only=True)['Plan by UC'].iter_rows(values_only=True):
    if r[0] and re.match(r'^[A-Z]{2,4}-\d', str(r[0])):
        plan[str(r[0]).strip()] = {'wave': int(r[3]) if str(r[3]).isdigit() else None, 'status': str(r[10] or '')}
mod_wave = defaultdict(set)
for k, v in plan.items():
    if v['wave']: mod_wave[k.split('-')[0]].add(v['wave'])
def wave_of(u):
    if u in plan and plan[u]['wave']: return plan[u]['wave']
    w = mod_wave.get(u.split('-')[0]); return min(w) if w else M.get('module_wave', {}).get(u.split('-')[0])

bugs = {}
for line in open(BUGS, encoding='utf8'):
    c = [x.strip() for x in line.split('|')]
    if len(c) > 13 and re.match(r'^[A-Z]{2}-BUG-\d+$', c[2]) and not re.search(r'Verified|Closed|Removed', c[5]):
        bugs.setdefault(c[2], {'area': c[1], 'status': c[5], 'title': c[13]})
def friendly(s):
    if s.startswith('Fixed'): return 'Fixed, being verified'
    if s == 'Blocked': return 'Cannot be checked on the test environment'
    return 'Being fixed'
uc_bugs = defaultdict(list)
for code, ucs in M['bugs'].items():
    if code in bugs:
        for u in ucs: uc_bugs[u].append(code)

def ren(s, table):
    for a, b in table.items(): s = re.sub(r'\b' + re.escape(a) + r'\b', b, s)
    return s

rows, flows = [], []
for fl in M['flows']:
    S = json.load(open(os.path.join(SPECS, fl['spec']), encoding='utf8'))
    word = os.path.basename(S['out']); seq = S.get('seq', [len(flows) + 1, len(M['flows'])])
    if len(S['steps']) != len(fl['steps']): raise SystemExit(f"{fl['spec']}: {len(S['steps'])} steps, map has {len(fl['steps'])}")
    flows.append({'code': fl['code'], 'title': S['title'], 'word': word, 'n': len(S['steps']), 'blocked': S.get('blocked', [])})
    for i, (st, mp) in enumerate(zip(S['steps'], fl['steps']), 1):
        for u in mp['uc']:
            if u not in uc: raise SystemExit(f'unknown UC {u} in {fl["code"]} step {i}')
        w = mp.get('wave') or wave_of(mp['uc'][0])
        kb = sorted({b for u in mp['uc'] for b in uc_bugs.get(u, [])})
        rows.append({'id': f"{fl['code']}-S{i:02d}", 'flow': f"{fl['code']} · {S['title']}", 'word': word, 'step': i, 'wave': w,
                     'who': mp.get('who') or ren(st['who'], M.get('who_rename', {})), 'where': ren(st['where'], M.get('where_rename', {})),
                     'what': mp.get('what', st['what']) + (f" (Same as {mp['same']}: test it once.)" if mp.get('same') else ''), 'result': mp.get('result', st['result']), 'uc': mp['uc'], 'shots': len(st.get('shots', [])), 'bugs': kb,
                     'issues': [M['issue_text'][b] for b in kb if b in M.get('issue_text', {})],
                     'blocked': [a for a, ids in M.get('blocked_steps', {}).items() if f"{fl['code']}-S{i:02d}" in ids]})

ONLY = M.get('only_round', False)
SHOW_ISSUES = M.get('show_issues', False)  # QA lead 06/11: no bug list for the customer
if ONLY:
    rows = [r for r in rows if r['wave'] == ROUND]
    flows = [f for f in flows if any(r['id'].startswith(f['code'] + '-') for r in rows)]
    uc = {u: d for u, d in uc.items() if wave_of(u) == ROUND}
covered = defaultdict(list)
for r in rows:
    for u in r['uc']: covered[u].append(r['id'])

F = 'Arial'
def font(**k): return Font(name=F, size=k.pop('size', 10), **k)
H_FILL = PatternFill('solid', fgColor='1B2730'); GREY = PatternFill('solid', fgColor='EEEEEE'); IN_FILL = PatternFill('solid', fgColor='FFF8E1')
thin = Side(style='thin', color='C8CED3'); BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical='top'); CENTER = Alignment(horizontal='center', vertical='top', wrap_text=True)
def header(ws, row, names, widths):
    for j, (n, w) in enumerate(zip(names, widths), 1):
        c = ws.cell(row, j, n); c.font = font(bold=True, color='FFFFFF'); c.fill = H_FILL; c.alignment = CENTER; c.border = BORDER
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = ws.cell(row + 1, 3)

wb = openpyxl.Workbook()
# ---- Start here
ws = wb.active; ws.title = 'Start here'; ws.column_dimensions['A'].width = 3; ws.column_dimensions['B'].width = 120
lines = [(f'SGS Digital Trust Platform – Flow checklist (Phase 1 · Wave {ROUND})' if ONLY else 'SGS Digital Trust Platform – Flow checklist (Phase 1)', font(bold=True, size=16)),
         (f'Use case list v6.5 · Detailed Plan v3.0 · This round: Wave {ROUND}', font(size=11, color='697077')), ('', None),
         ('How to use', font(bold=True, size=12)),
         (f"1. Keep this file in the same folder as the flow documents listed below and the mind map ({M.get('mindmap', '00_DTP_Happy_Path_MindMap.html')}).", font()),
         ('2. In the sheet "Checklist", each row is one step of a flow document. "Step" is the step number in that document; click the flow name to open it.', font()),
         ('3. Follow the step as shown in the document, then pick your result: Pass, Fail, Blocked (could not try it) or Not tested. Write what you saw in "Comments".', font()),
         ((f'4. This checklist covers Wave {ROUND} only. Flows and steps of later waves are not listed: please do not test or comment on them yet. A step marked "Same as …" repeats an earlier step: test it once.' if ONLY else f'4. Only rows of Wave {ROUND} are open for testing in this round (white rows). Grey rows belong to a later wave: please do not test or comment on them yet.'), font(bold=True)),
         ('5. "Blocked (needs SGS)" marks a part that can only be checked on the SGS environment (Microsoft Entra sign-in, SGS email, malware scan); see the sheet "Not tested yet (blocked)".', font()),
         (M.get('portal_note', ''), font(italic=True)),
         ('6. "UC ID" refers to the SGS DTP Use Case List v6.5. The sheet "UC coverage" shows which step covers each use case' + (f' of Wave {ROUND}.' if ONLY else '.'), font()), ('', None),
         ('Waves', font(bold=True, size=12)),
         ('Wave 1 – Customer onboarding and set-up, scopes, frameworks, workspaces and evidence collection.', font()),
         ('Wave 2 – Bulk upload and audit request (NirmatAI), certification records, training.', font()),
         ('Wave 3 – Consulting and Gap Analysis, Marketplace, home pages, audit views and data retention.', font()), ('', None),
         ('Flow documents', font(bold=True, size=12))]
TOP = 0
LOGOS = [M['logo']] if isinstance(M.get('logo'), str) else M.get('logo', [])
if LOGOS:  # logos side by side above the title
    from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker
    from openpyxl.drawing.xdr import XDRPositiveSize2D
    from openpyxl.utils.units import pixels_to_EMU
    x = 0
    for lg in LOGOS:
        f = lg['file'] if isinstance(lg, dict) else lg; sc = lg.get('scale', 1) if isinstance(lg, dict) else 1
        img = XLImage(os.path.join(os.path.dirname(MAP), f)); h = round(46 * sc); w = round(h * img.width / img.height); img.height, img.width = h, w
        img.anchor = OneCellAnchor(_from=AnchorMarker(col=1, colOff=pixels_to_EMU(x), row=0, rowOff=pixels_to_EMU(4 + (46 - h) // 2)), ext=XDRPositiveSize2D(pixels_to_EMU(w), pixels_to_EMU(h)))
        ws.add_image(img); x += w + 28
    ws.row_dimensions[1].height = 42; TOP = 2
for i, (t, f) in enumerate(lines, 1 + TOP):
    c = ws.cell(i, 2, t)
    if f: c.font = f
    c.alignment = Alignment(wrap_text=True)
r0 = len(lines) + 1 + TOP
for k, fl in enumerate(flows):
    c = ws.cell(r0 + k, 2, f"{fl['code']} · {fl['title']} ({fl['n']} steps) – {fl['word']}"); c.hyperlink = fl['word']; c.font = font(color='C05000', underline='single')
ws.sheet_view.showGridLines = False

# ---- Checklist
ck = wb.create_sheet('Checklist')
cols = ['ID', 'Flow (click to open)', 'Step', 'Wave', 'In this round', 'Sign in as', 'Where', 'What to do', 'What you should see', 'UC ID (v6.5)', 'Screenshots', *(['Known issue (being fixed)'] if SHOW_ISSUES else []), 'Blocked (needs SGS)', 'Your result', 'Comments', 'Tested by', 'Date tested']
RC = cols.index('Your result') + 1; RL = get_column_letter(RC)
header(ck, 1, cols, [9, 30, 6, 6, 8, 18, 30, 40, 40, 16, 8] + ([34] if SHOW_ISSUES else []) + [26, 13, 36, 14, 12])
dv = DataValidation(type='list', formula1='"Pass,Fail,Blocked,Not tested"', allow_blank=True); ck.add_data_validation(dv)
for i, r in enumerate(rows, 2):
    inr = r['wave'] == ROUND
    vals = [r['id'], r['flow'], r['step'], f"Wave {r['wave']}", 'Yes' if inr else 'No', r['who'], r['where'], r['what'], r['result'],
            ', '.join(r['uc']), r['shots'], *([chr(10).join('• ' + x for x in r['issues']) or '—'] if SHOW_ISSUES else []), chr(10).join(r['blocked']) or '—', None if inr else 'Not in this round', None, None, None]
    for j, v in enumerate(vals, 1):
        c = ck.cell(i, j, v); c.border = BORDER; c.alignment = CENTER if j in (1, 3, 4, 5, 11, RC) else WRAP
        c.font = font(color='000000' if inr else '8A9297')
        if not inr: c.fill = GREY
        elif j >= RC: c.fill = IN_FILL; c.protection = Protection(locked=False)
    ck.cell(i, 2).hyperlink = r['word']; ck.cell(i, 2).font = font(color='C05000' if inr else '8A9297', underline='single')
    if inr: dv.add(ck.cell(i, RC))
    ck.cell(i, len(cols)).number_format = 'dd mmm yyyy'
last = len(rows) + 1
for txt, color in (('Pass', 'C6EFCE'), ('Fail', 'FFC7CE'), ('Blocked', 'FFEB9C')):
    ck.conditional_formatting.add(f'{RL}2:{RL}{last}', FormulaRule(formula=[f'${RL}2="{txt}"'], fill=PatternFill('solid', fgColor=color)))
ck.auto_filter.ref = f'A1:{get_column_letter(len(cols))}{last}'
ck.protection.sheet = True; ck.protection.autoFilter = False; ck.protection.sort = False; ck.protection.formatColumns = False; ck.protection.formatRows = False

# ---- Summary
sm = wb.create_sheet('Summary', 1)
sm['A1'] = 'Progress (updates automatically)'; sm['A1'].font = font(bold=True, size=14)
header(sm, 3, ['Flow', 'Document', 'Steps', f'In Wave {ROUND}', 'Pass', 'Fail', 'Blocked', 'Not tested', 'Progress'], [44, 38, 8, 10, 8, 8, 9, 11, 10])
sm.freeze_panes = None
R = f'Checklist!$A$2:$A${last}'
for k, fl in enumerate(flows, 4):
    a = f'"{fl["code"]}-*"'
    vals = [f"{fl['code']} · {fl['title']}", fl['word'], f'=COUNTIF({R},{a})',
            f'=COUNTIFS({R},{a},Checklist!$E$2:$E${last},"Yes")']
    for col, res in zip('EFG', ('Pass', 'Fail', 'Blocked')):
        vals.append(f'=COUNTIFS({R},{a},Checklist!${RL}$2:${RL}${last},"{res}")')
    vals.append(f'=D{k}-SUM(E{k}:G{k})'); vals.append(f'=IF(D{k}=0,"—",SUM(E{k}:G{k})/D{k})')
    for j, v in enumerate(vals, 1):
        c = sm.cell(k, j, v); c.font = font(); c.border = BORDER; c.alignment = WRAP if j < 3 else CENTER
    sm.cell(k, 2).hyperlink = fl['word']; sm.cell(k, 2).font = font(color='C05000', underline='single'); sm.cell(k, 9).number_format = '0%'
t = 4 + len(flows)
sm.cell(t, 1, 'Total').font = font(bold=True)
for j in range(3, 9):
    L = get_column_letter(j); c = sm.cell(t, j, f'=SUM({L}4:{L}{t-1})'); c.font = font(bold=True); c.alignment = CENTER; c.border = BORDER
c = sm.cell(t, 9, f'=IF(D{t}=0,"—",SUM(E{t}:G{t})/D{t})'); c.number_format = '0%'; c.font = font(bold=True); c.alignment = CENTER; c.border = BORDER

# ---- UC coverage
uv = wb.create_sheet('UC coverage')
header(uv, 1, ['UC ID', 'Use case', 'Actor(s)', 'Portal', 'Wave', 'Covered by step', 'Note'], [10, 44, 26, 10, 7, 26, 48])
for i, (u, d) in enumerate(uc.items(), 2):
    w = wave_of(u); note = ''
    if not covered[u]: note = 'Not part of the happy-path flows; tested by the QA team.'
    vals = [u, d['name'], d['actor'], d['portal'], f'Wave {w}' if w else '—', ', '.join(covered[u]) or '—', note]
    for j, v in enumerate(vals, 1):
        c = uv.cell(i, j, v); c.font = font(color='000000' if w == ROUND else '5F6B72'); c.border = BORDER; c.alignment = CENTER if j in (1, 4, 5) else WRAP
uv.auto_filter.ref = f'A1:G{len(uc)+1}'

# ---- Not tested yet (blocked)
bk = wb.create_sheet('Not tested yet (blocked)')
header(bk, 1, ['Area', 'Flow', 'Not tested', 'Why it is blocked', 'Check on the SGS environment', 'Steps'], [24, 30, 34, 44, 40, 20])
bi = 2
for fl in flows:
    for bl in fl['blocked']:
        mapped = [x for x in M.get('blocked_steps', {}).get(bl[0], []) if x.startswith(fl['code'] + '-')]
        ids = sorted(x for x in mapped if any(r['id'] == x for r in rows))
        if mapped and not ids: continue  # only steps of a later wave
        for j, v in enumerate([bl[0], f"{fl['code']} · {fl['title']}", bl[1], bl[2], bl[3], ', '.join(ids) or 'Whole flow'], 1):
            c = bk.cell(bi, j, v); c.font = font(bold=(j == 1), color='B42318' if j == 1 else '000000'); c.border = BORDER; c.alignment = WRAP
            if j == 1: c.fill = PatternFill('solid', fgColor='FCE8E8')
        bi += 1
bk.auto_filter.ref = f'A1:F{max(bi - 1, 1)}'
used = sorted({b for r in rows for b in r['bugs']})

for s in wb.worksheets: s.sheet_view.zoomScale = 100
wb.save(OUT)
inr = sum(1 for r in rows if r['wave'] == ROUND)
print(json.dumps({'rows': len(rows), 'in_round': inr, 'by_flow': {f['code']: sum(1 for r in rows if r['id'].startswith(f['code']) and r['wave'] == ROUND) for f in flows},
                  'uc_total': len(uc), 'uc_covered': sum(1 for u in uc if covered[u]), 'known_issues': len(used),
                  'not_in_plan': [u for u in uc if u not in plan]}, ensure_ascii=False))
