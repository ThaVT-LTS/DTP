"""v0.1_Phase1 -> v0.2_Phase1: chuyển dấu [Phase 2] ở tên case sang cột V (Remark Round 2). FB-071.
Sửa thẳng XML, giữ logo, dropdown, công thức."""
import zipfile, re, sys, html, unicodedata
SRC, OUT = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(SRC)
sst = z.read('xl/sharedStrings.xml').decode('utf8')
sis = re.findall(r'<si>.*?</si>|<si/>', sst, re.S)
def si_text(x): return html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', x, re.S)))
texts = [si_text(x) for x in sis]
new_si = []
def add(t):
    t = unicodedata.normalize('NFC', t)
    new_si.append('<si><t xml:space="preserve">%s</t></si>' % html.escape(t, quote=False))
    return len(sis) + len(new_si) - 1
P2 = add('Phase 2')
log = []
TC_SHEETS = range(3, 25)
files = {}
for i in TC_SHEETS:
    name = 'xl/worksheets/sheet%d.xml' % i
    s = z.read(name).decode('utf8')
    rows_hit = []
    def fix_h(m):
        r = int(m.group(1)); attrs = m.group(2); idx = int(m.group(3))
        t = texts[idx]
        if r >= 13 and t.lstrip().startswith('[Phase 2]'):
            nt = re.sub(r'^\s*\[Phase 2\]\s*', '', t)
            rows_hit.append((r, t, nt))
            return '<c r="H%d"%s><v>%d</v></c>' % (r, attrs, add(nt))
        return m.group(0)
    s = re.sub(r'<c r="H(\d+)"([^>]*\bt="s"[^>]*)><v>(\d+)</v></c>', fix_h, s)
    for r, old, new in rows_hit:
        pat = re.compile(r'<c r="V%d"( s="\d+")?\s*/>' % r)
        if pat.search(s):
            s = pat.sub(lambda m: '<c r="V%d"%s t="s"><v>%d</v></c>' % (r, m.group(1) or '', P2), s, 1)
        else:
            mv = re.search(r'<c r="V%d"[^>]*>.*?</c>' % r, s)
            raise SystemExit('V%d sheet%d có sẵn nội dung hoặc thiếu ô: %s' % (r, i, mv.group(0) if mv else 'không có ô'))
        log.append((i, r, old, new))
    files[name] = s
# Cover: Version + một dòng Record of change sau dòng 49
c = z.read('xl/worksheets/sheet1.xml').decode('utf8')
assert texts[12].strip() == 'Version 0.1', texts[12]
c = c.replace('<c r="G6" s="7" t="s"><v>12</v></c>', '<c r="G6" s="7" t="s"><v>%d</v></c>' % add('Version 0.2'), 1)
def shift(m):
    col, row = m.group(1), int(m.group(2))
    return '%s%d' % (col, row + 1 if row >= 50 else row)
head, body, tail = re.split(r'(<sheetData>.*</sheetData>)', c, flags=re.S)
body = re.sub(r'<row r="(\d+)"', lambda m: '<row r="%d"' % (int(m.group(1)) + 1 if int(m.group(1)) >= 50 else int(m.group(1))), body)
body = re.sub(r'(?<=<c r=")([A-Z]+)(\d+)', shift, body)
tail = re.sub(r'(?<=ref=")([A-Z]+)(\d+)', shift, tail)
r48 = re.search(r'<row r="48"[ >].*?</row>', body, re.S).group(0)
r49 = re.search(r'<row r="49"[ >].*?</row>', body, re.S).group(0)
st48 = re.findall(r'<c r="([B-G])48" s="(\d+)"', r48); st49 = dict(re.findall(r'<c r="([B-G])49" s="(\d+)"', r49))
r49n = r49
for col, s48 in st48: r49n = r49n.replace('<c r="%s49" s="%s"' % (col, st49[col]), '<c r="%s49" s="%s"' % (col, s48))
vals = {'B': '14/10/2026', 'C': '0.2', 'D': 'Tất cả sheet TC', 'E': 'M', 'F': 'Chuyển dấu Phase 2 từ tên case sang cột Remark (V) của Round 2: %d case' % len(log), 'G': 'FB-071'}
cells = ''.join('<c r="%s50" s="%s" t="s"><v>%d</v></c>' % (col, st49[col], add(vals[col])) for col in 'BCDEFG')
new50 = '<row r="50" ht="15.75" customHeight="1">%s</row>' % cells
body = body.replace(r49, r49n + new50, 1)
files['xl/worksheets/sheet1.xml'] = head + body + tail
# sharedStrings
allsi = sis + new_si
cnt = re.search(r'count="(\d+)"', sst)
start = sst.index('<si'); end = sst.rindex('</sst>')
newsst = sst[:start] + ''.join(allsi) + sst[end:]
newsst = re.sub(r'uniqueCount="\d+"', 'uniqueCount="%d"' % len(allsi), newsst, 1)
if cnt: newsst = newsst.replace('count="%s"' % cnt.group(1), 'count="%d"' % (int(cnt.group(1)) + len(new_si) + len(log) + 6), 1)
files['xl/sharedStrings.xml'] = newsst
out = zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED)
for it in z.infolist():
    data = files[it.filename].encode('utf8') if it.filename in files else z.read(it.filename)
    out.writestr(it, data)
out.close()
for i, r, old, new in log: print('sheet%d' % i, r, '|', old[:70], '->', new[:60])
print('Tổng', len(log))
