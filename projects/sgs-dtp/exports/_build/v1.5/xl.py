"""Đọc thẳng XML của file .xlsx (không dùng openpyxl để khỏi mất gì). Dùng chung cho các script phân tích."""
import re, zipfile
from lxml import etree

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
RNS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
def q(t): return "{%s}%s" % (NS, t)

def col_no(s):
    n = 0
    for ch in s: n = n * 26 + ord(ch) - 64
    return n
def col_name(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26); s = chr(65 + r) + s
    return s
def split_ref(ref):
    m = re.match(r"([A-Z]+)(\d+)$", ref); return col_no(m.group(1)), int(m.group(2))

class Book:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        self.names = self.z.namelist()
        wb = etree.fromstring(self.z.read("xl/workbook.xml"))
        rels = {r.get("Id"): r.get("Target") for r in etree.fromstring(self.z.read("xl/_rels/workbook.xml.rels"))}
        self.sheets = []      # (name, path, state)
        for s in wb.find(q("sheets")):
            t = rels[s.get("{%s}id" % RNS)]
            self.sheets.append((s.get("name"), t.lstrip("/") if t.startswith("/") else "xl/" + t, s.get("state")))
        self.wb = wb
        sst = etree.fromstring(self.z.read("xl/sharedStrings.xml")) if "xl/sharedStrings.xml" in self.names else None
        self.si = sst.findall(q("si")) if sst is not None else []
        self.strings = ["".join(t.text or "" for t in si.iter(q("t")) if t.getparent().tag != q("rPh")) for si in self.si]
        self.st = etree.fromstring(self.z.read("xl/styles.xml"))
        self.fonts = self.st.find(q("fonts")); self.fills = self.st.find(q("fills")); self.borders = self.st.find(q("borders"))
        self.xfs = self.st.find(q("cellXfs"))
        self._roots = {}
    def root(self, name):
        if name not in self._roots:
            path = next(p for n, p, _ in self.sheets if n == name)
            self._roots[name] = etree.fromstring(self.z.read(path))
        return self._roots[name]
    def cells(self, name):
        """{(col,row): (value, style, formula, type)}"""
        out = {}
        for c in self.root(name).iter(q("c")):
            v = c.find(q("v")); f = c.find(q("f")); t = c.get("t")
            if t == "s" and v is not None: val = self.strings[int(v.text)]
            elif t == "inlineStr": val = "".join(x.text or "" for x in c.iter(q("t")))
            else: val = v.text if v is not None else None
            out[split_ref(c.get("r"))] = (val, c.get("s", "0"), (f.text if f is not None else None), t)
        return out
    def formula_cells(self, name):
        """{(col,row)} của mọi ô có công thức, kể cả ô dùng công thức chia sẻ (thẻ <f> không có chữ)."""
        return {split_ref(c.get("r")) for c in self.root(name).iter(q("c")) if c.find(q("f")) is not None}
    def merges(self, name):
        out = []
        for m in self.root(name).iter(q("mergeCell")):
            a, _, b = m.get("ref").partition(":")
            (c1, r1), (c2, r2) = split_ref(a), split_ref(b or a)
            out.append((c1, r1, c2, r2))
        return out
    def font(self, s):
        f = self.fonts[int(self.xfs[int(s)].get("fontId", "0"))]
        g = lambda t: (f.find(q(t)).get("val") if f.find(q(t)) is not None else None)
        col = f.find(q("color"))
        return dict(name=g("name"), sz=g("sz"), b=f.find(q("b")) is not None, i=f.find(q("i")) is not None,
                    u=f.find(q("u")) is not None, color=dict(col.attrib) if col is not None else None)
    def fill(self, s):
        pf = self.fills[int(self.xfs[int(s)].get("fillId", "0"))].find(q("patternFill"))
        if pf is None or pf.get("patternType") in (None, "none"): return None
        fg = pf.find(q("fgColor")); return dict(fg.attrib) if fg is not None else {"pattern": pf.get("patternType")}
    def xf(self, s): return self.xfs[int(s)]
