#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng SGS-DTP_TestCase1_v1.5.xlsx từ bản v1.4, làm thẳng trên XML (không lưu bằng openpyxl).

    python build_v15.py --book v1.4.xlsx --rows scopes_v15.json --out v1.5.xlsx [--measure measure_v1.5.json]

Cách chạy cả chuỗi: xem README.md cùng thư mục.

Việc làm:
  1. Mọi kiểu ô đang dùng phông khác Times New Roman 10 → Times New Roman 10 (kiểu Normal giữ nguyên, để độ rộng cột không đổi).
  2. Sheet Scopes: dựng lại vùng dữ liệu từ bảng phẳng; No. 1…N, TVP_ID Scope_001…; gộp ô 4 cột Classification;
     kiểu ô lấy từ chính sheet (ô neo, ô giữa, ô cuối của cụm gộp), bỏ nền tô tay.
  3. Dòng còn câu hỏi mở: tô ô Open question, và ô Expected result khi trống.
  4. Mọi sheet: ô văn bản bắt đầu bằng - + = @ → kiểu ô có quotePrefix (dấu nháy đơn ở đầu khi sửa ô).
  5. Test_Report dựng lại theo các sheet TC; sheet Cần xác nhận, Users: sửa chỗ trỏ tới TC của Scopes; Cover: thêm dòng Record of change.
  6. Bảng chuỗi dùng chung dựng lại gọn, mọi chuỗi về dạng dựng sẵn (NFC).
  7. --measure: chiều cao dòng và giá trị công thức do LibreOffice tính (lo_measure.py) được ghi vào file.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

# Thư viện làm thẳng trên XML (tc_add_sheet.py, tc_palette.py): mặc định lấy ở .claude/skills/tc-authoring/scripts
# của thư mục qa-pipeline; đổi chỗ thì đặt biến môi trường TC_LIB.
HERE = Path(__file__).resolve().parent
LIB = os.environ.get("TC_LIB") or str(HERE.parents[4] / ".claude" / "skills" / "tc-authoring" / "scripts")
sys.path.insert(0, LIB)
from lxml import etree  # noqa: E402

import tc_add_sheet as T  # noqa: E402
from tc_add_sheet import q, col_letter, split_ref  # noqa: E402
from tc_palette import FONT, OPEN_FILL, TEXT  # noqa: E402

NS = T.NS
FORMULA_START = ("-", "+", "=", "@")


def nfc(s):
    return unicodedata.normalize("NFC", s)


# ----------------------------------------------------------------------------- 1. phông
def fix_fonts(st: T.Styles) -> list[int]:
    """Kiểu ô nào dùng phông không phải Times New Roman 10 thì chuyển sang phông chữ thường của file (cùng màu chữ dữ liệu)."""
    def ok(font):
        name = font.find(q("name"))
        sz = font.find(q("sz"))
        return (name is not None and name.get("val") == FONT and sz is not None and float(sz.get("val")) == 10.0)

    target = None
    for i, f in enumerate(st.fonts):
        if ok(f) and f.find(q("b")) is None and T.rgb_of(f.find(q("color"))) == TEXT:
            target = i
            break
    if target is None:
        raise SystemExit("styles.xml không có phông Times New Roman 10 màu chữ dữ liệu")
    changed = []
    for i, xf in enumerate(st.xfs):
        f = st.fonts[int(xf.get("fontId", "0"))]
        if not ok(f):
            xf.set("fontId", str(target))
            xf.set("applyFont", "1")
            changed.append(i)
    if changed:
        st.changed = True
    return changed


def quote_variant(st: T.Styles, s: str) -> str:
    key = ("quote", str(s))
    if key not in st._cache:
        xf = st.xfs[int(s)]
        if xf.get("quotePrefix") == "1":
            st._cache[key] = str(s)
        else:
            new = copy.deepcopy(xf)
            new.set("quotePrefix", "1")
            st._cache[key] = str(st.add(st.xfs, new))
    return st._cache[key]


def unquote_variant(st: T.Styles, s: str) -> str:
    key = ("unquote", str(s))
    if key not in st._cache:
        xf = st.xfs[int(s)]
        if xf.get("quotePrefix") != "1":
            st._cache[key] = str(s)
        else:
            new = copy.deepcopy(xf)
            del new.attrib["quotePrefix"]
            st._cache[key] = str(st.add(st.xfs, new))
    return st._cache[key]


# ----------------------------------------------------------------------------- 2. dựng lại vùng dữ liệu
def plain_style(st: T.Styles, s: str) -> bool:
    """Kiểu ô 'gốc' của vùng dữ liệu: không nền, không quotePrefix, chữ màu dữ liệu."""
    xf = st.xfs[int(s)]
    if xf.get("quotePrefix") == "1":
        return False
    pf = st.fills[int(xf.get("fillId", "0"))].find(q("patternFill"))
    if pf is not None and pf.get("patternType") not in (None, "none"):
        return False
    return st.font_rgb(s) in (TEXT, None)


def data_styles(tpl: T.Sheet, lay: T.TcLayout, st: T.Styles) -> dict:
    """{(cột, loại): kiểu ô} lấy theo đa số trong vùng dữ liệu của sheet. Loại: plain | single | first | inner | last."""
    pos = {}
    for c1, r1, c2, r2 in tpl.merges:
        if c1 == c2 and c1 in lay.cls and r1 >= lay.data_start and r2 > r1:
            for r in range(r1, r2 + 1):
                pos[(c1, r)] = "first" if r == r1 else ("last" if r == r2 else "inner")
    cnt: dict[tuple[int, str], Counter] = {}
    for r in range(lay.data_start, lay.data_end + 1):
        for c in range(1, lay.last_col + 1):
            s = tpl.style(c, r)
            if s is None or not plain_style(st, s):
                continue
            kind = pos.get((c, r), "single") if c in lay.cls else "plain"
            cnt.setdefault((c, kind), Counter())[s] += 1
    out = {k: v.most_common(1)[0][0] for k, v in cnt.items()}
    # Bốn cột Classification cùng một kiểu ô đơn thì coi là một họ: ô neo, ô giữa, ô cuối lấy theo đa số của cả bốn cột
    # (cột ít cụm gộp, hoặc cụm do người dùng gộp tay, sẽ không kéo theo kiểu lệch).
    singles = {out[(c, "single")] for c in lay.cls if (c, "single") in out}
    if len(singles) == 1:
        for kind in ("first", "inner", "last"):
            pool = Counter()
            for c in lay.cls:
                pool.update(cnt.get((c, kind), Counter()))
            if pool:
                best = pool.most_common(1)[0][0]
                for c in lay.cls:
                    out[(c, kind)] = best
    for c in lay.cls:                                   # cột Classification thiếu loại nào thì mượn loại gần nhất
        out.setdefault((c, "single"), out.get((c, "first")))
        out.setdefault((c, "first"), out[(c, "single")])
        out.setdefault((c, "last"), out[(c, "single")])
        out.setdefault((c, "inner"), out[(c, "last")])
    return out


def est_height(texts: dict[int, str], widths: dict[int, float]) -> float:
    """Ước lượng chiều cao dòng (pt) khi chưa có số đo của LibreOffice: 13.5 pt mỗi dòng chữ + 8.1."""
    lines = 2
    for c, t in texts.items():
        if not t:
            continue
        per = max(8, int(widths.get(c, 10) * 1.12))
        n = sum(max(1, -(-len(seg) // per)) for seg in t.split("\n"))
        lines = max(lines, n)
    return round(13.5 * lines + 8.1, 2)


def rebuild_tc_sheet(root, sst: T.SharedStrings, st: T.Styles, rows: list[dict], id_fmt: str):
    """Thay vùng dữ liệu của sheet TC bằng `rows` (bảng phẳng). Trả về (lay, first, last)."""
    tpl = T.Sheet(root, sst)
    lay = T.TcLayout(tpl)
    styles = data_styles(tpl, lay, st)
    widths = T.col_widths(root)
    sd = root.find(q("sheetData"))
    tail = []
    trow = tpl.rows.get(lay.data_start)
    for cel in trow.findall(q("c")):
        c, _ = split_ref(cel.get("r"))
        if c > lay.last_col:
            tail.append((c, cel.get("s")))
    for row in list(sd.findall(q("row"))):
        if int(row.get("r")) >= lay.data_start:
            sd.remove(row)
    first = lay.data_start
    last = first + len(rows) - 1
    C = lay.cols
    field_of = {C["priority"]: "Pri", C["test case name/ test view point"]: "Name", C["pre-condition"]: "Pre",
                C["step"]: "Step", C["expected result"]: "Exp", lay.c_wait: "OQ", lay.c_uc: "UC"}
    keys = ["I", "II", "III", "IV"]
    runs = T.class_runs(rows)
    run_at = {}
    for level, rr in runs.items():
        for a, b in rr:
            for i in range(a, b + 1):
                run_at[(level, i)] = (a, b)

    for i, rec in enumerate(rows):
        r = first + i
        row_el = etree.SubElement(sd, q("row"))
        row_el.set("r", str(r))
        texts = {c: rec.get(f, "") for c, f in field_of.items()}
        for level, key in enumerate(keys):
            a, b = run_at[(level, i)]
            if a == b:
                texts[lay.cls[level]] = rec[key]
        row_el.set("ht", str(est_height(texts, widths)))
        row_el.set("customHeight", "1")
        for c in range(1, lay.last_col + 1):
            val = None
            kind = "plain"
            if c == lay.col_no:
                val = i + 1
            elif c in lay.cls:
                level = lay.cls.index(c)
                a, b = run_at[(level, i)]
                kind = "single" if a == b else ("first" if i == a else ("last" if i == b else "inner"))
                if i == a:
                    val = rec[keys[level]] or None
            elif c == C["tvp_id"]:
                val = id_fmt % (i + 1)
            elif c in field_of:
                val = rec.get(field_of[c], "") or None
            cel = etree.SubElement(row_el, q("c"))
            cel.set("r", f"{col_letter(c)}{r}")
            cel.set("s", styles[(c, kind)])
            if val is None:
                continue
            if isinstance(val, int):
                etree.SubElement(cel, q("v")).text = str(val)
            else:
                cel.set("t", "s")
                etree.SubElement(cel, q("v")).text = str(sst.get(val))
        for c, s in tail:
            cel = etree.SubElement(row_el, q("c"))
            cel.set("r", f"{col_letter(c)}{r}")
            if s is not None:
                cel.set("s", s)

    T.fix_summary_ranges(root, lay, first, last, exact=True)

    mc = root.find(q("mergeCells"))
    for m in list(mc.findall(q("mergeCell"))):
        if T.Sheet._rng(m.get("ref"))[1] >= lay.data_start:
            mc.remove(m)
    for level, rr in runs.items():
        c = lay.cls[level]
        for a, b in rr:
            if b > a:
                etree.SubElement(mc, q("mergeCell")).set("ref", f"{col_letter(c)}{first + a}:{col_letter(c)}{first + b}")
    mc.set("count", str(len(mc.findall(q("mergeCell")))))

    sv = root.find(q("sheetViews"))
    if sv is not None:
        for v in sv.findall(q("sheetView")):
            v.attrib.pop("topLeftCell", None)
            for sel in v.findall(q("selection")):
                sel.set("activeCell", f"A{first}")
                sel.set("sqref", f"A{first}")
    dim = root.find(q("dimension"))
    if dim is not None:
        dim.set("ref", f"A1:{col_letter(max([lay.last_col] + [c for c, _ in tail]))}{last}")

    def fit(sqref: str) -> str:
        out = []
        for tok in sqref.split():
            m = re.match(r"([A-Z]+)(\d+):([A-Z]+)(\d+)$", tok)
            if m and int(m.group(2)) == lay.data_start:
                tok = f"{m.group(1)}{m.group(2)}:{m.group(3)}{last}"
            out.append(tok)
        return " ".join(out)

    for dv in root.iter(f"{{{T.X14}}}dataValidation"):
        sq = dv.find(f"{{{T.XM}}}sqref")
        if sq is not None and sq.text:
            sq.text = fit(sq.text)
    for dv in root.iter(q("dataValidation")):
        if dv.get("sqref"):
            dv.set("sqref", fit(dv.get("sqref")))
    return lay, first, last


# ----------------------------------------------------------------------------- 4. dấu nháy đơn đầu ô
def cell_text(cel, sst: T.SharedStrings):
    t = cel.get("t")
    if cel.find(q("f")) is not None:
        return None
    if t == "s":
        v = cel.find(q("v"))
        return sst.text(int(v.text)) if v is not None else None
    if t == "inlineStr":
        return "".join(x.text or "" for x in cel.iter(q("t")))
    if t == "str":
        v = cel.find(q("v"))
        return v.text if v is not None else None
    return None


def apply_quote_prefix(root, sst: T.SharedStrings, st: T.Styles) -> tuple[int, int]:
    """Ô văn bản bắt đầu bằng - + = @ phải có quotePrefix; ô khác thì bỏ quotePrefix thừa. Trả về (số ô cần, số ô đổi kiểu)."""
    need = changed = 0
    for cel in root.iter(q("c")):
        txt = cell_text(cel, sst)
        s = cel.get("s", "0")
        if txt and txt.lstrip()[:1] in FORMULA_START:
            need += 1
            new = quote_variant(st, s)
        else:
            new = unquote_variant(st, s) if txt is not None or cel.find(q("v")) is None else s
        if new != s:
            cel.set("s", new)
            changed += 1
    return need, changed


# ----------------------------------------------------------------------------- 5. chỗ trỏ sang TC của Scopes
def set_text(cel, sst: T.SharedStrings, text: str):
    for ch in list(cel):
        cel.remove(ch)
    cel.set("t", "s")
    etree.SubElement(cel, q("v")).text = str(sst.get(text))


def wrap_variant(st: T.Styles, s: str) -> str:
    key = ("wrap", str(s))
    if key not in st._cache:
        xf = copy.deepcopy(st.xfs[int(s)])
        al = xf.find(q("alignment"))
        if al is None:
            al = etree.Element(q("alignment"))
            xf.insert(0, al)
        al.set("wrapText", "1")
        if not al.get("vertical"):
            al.set("vertical", "top")
        xf.set("applyAlignment", "1")
        st._cache[key] = str(st.add(st.xfs, xf))
    return st._cache[key]


# ----------------------------------------------------------------------------- 6. bảng chuỗi
def compact_sst(pkg: T.Package, sheet_paths: list[str], roots: dict, sst_name: str, old: T.SharedStrings):
    """Dựng lại sharedStrings: chỉ giữ chuỗi còn được dùng, không trùng, dạng NFC."""
    new_root = etree.Element(q("sst"), nsmap={None: NS})
    index: dict[str, int] = {}
    total = 0
    not_nfc = 0
    for p in sheet_paths:
        root = roots[p]
        for cel in root.iter(q("c")):
            if cel.get("t") != "s":
                continue
            v = cel.find(q("v"))
            if v is None:
                continue
            raw = old.text(int(v.text))
            text = nfc(raw)
            not_nfc += raw != text
            if text not in index:
                si = etree.SubElement(new_root, q("si"))
                t = etree.SubElement(si, q("t"))
                t.text = text
                if text != text.strip() or "\n" in text or "  " in text:
                    t.set(T.XML_SPACE, "preserve")
                index[text] = len(index)
            v.text = str(index[text])
            total += 1
    new_root.set("count", str(total))
    new_root.set("uniqueCount", str(len(index)))
    pkg.put(sst_name, new_root)
    return len(index), total, not_nfc


# ----------------------------------------------------------------------------- main
def main() -> int:
    T.utf8_console()
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--rows", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--measure", help="kết quả của lo_measure.py: chiều cao dòng và giá trị công thức")
    ap.add_argument("--log", help="ghi tóm tắt việc đã làm ra file JSON")
    a = ap.parse_args()

    data = json.load(open(a.rows, encoding="utf-8"))
    rows = data["rows"]
    pkg = T.Package(Path(a.book))
    wb = pkg.xml("xl/workbook.xml")
    rels = pkg.xml("xl/_rels/workbook.xml.rels")
    rid_target = {r.get("Id"): r.get("Target") for r in rels}

    def path_of(sheet_el):
        t = rid_target[sheet_el.get(f"{{{T.RNS}}}id")]
        return t.lstrip("/") if t.startswith("/") else "xl/" + t

    sheets_el = wb.find(q("sheets"))
    by_name = {s.get("name"): s for s in sheets_el.findall(q("sheet"))}
    order = [s.get("name") for s in sheets_el.findall(q("sheet"))]
    paths = {n: path_of(by_name[n]) for n in order}
    roots = {paths[n]: pkg.xml(paths[n]) for n in order}
    R = lambda name: roots[paths[name]]                                     # noqa: E731
    sst_name = "xl/sharedStrings.xml"
    sst_root = pkg.xml(sst_name)
    sst = T.SharedStrings(sst_root)
    st_root = pkg.xml("xl/styles.xml")
    st = T.Styles(st_root)
    info = {}

    # 1. phông
    info["xf_doi_phong"] = fix_fonts(st)

    # 2. Scopes
    lay, first, last = rebuild_tc_sheet(R("Scopes"), sst, st, rows, "Scope_%03d")
    info["scopes"] = dict(rows=len(rows), first=first, last=last)

    # 3. dòng còn câu hỏi mở (mọi sheet TC, để kiểu ô nhất quán)
    tc_sheets = []
    for n in order:
        shx = T.Sheet(R(n), sst)
        if n != "Test_Report" and shx.find_text("No.") and shx.find_text("TVP_ID"):
            tc_sheets.append(n)
    info["open_rows"] = {}
    for n in tc_sheets:
        n_open, n_changed = T.mark_open_rows(R(n), sst, st)
        info["open_rows"][n] = (n_open, n_changed)

    # 5a. Test_Report
    books = [(n, T.Sheet(R(n), sst)) for n in tc_sheets]
    info["report_last_row"] = T.rebuild_report(R("Test_Report"), sst, books)

    # 5b. chỗ trỏ sang TC của Scopes ở sheet khác
    by_src = {r["src"]: r["id"] for r in rows if r["src"]}
    def new_id(v14_row):                                                    # noqa: E306
        return by_src[v14_row]
    refs = []
    qsh = T.Sheet(R("Cần xác nhận"), sst)
    for (c, r), cel in sorted(qsh.cells.items(), key=lambda x: (x[0][1], x[0][0])):
        v = qsh.value(c, r)
        if not isinstance(v, str):
            continue
        new = v
        if v.strip() == "Scopes Scope_021, Scope_025, Scope_131":           # Q-S-28: 3 case tạo scope (dòng 37, 38, 39 của v1.4)
            new = "Scopes " + ", ".join(new_id(x) for x in (37, 38, 39))
        if "(Scopes TC_110: Users ở mục Administration)" in v:
            new = v.replace("Scopes TC_110", "Scopes " + new_id(129))
        if new != v:
            set_text(cel, sst, new)
            refs.append(("Cần xác nhận", f"{col_letter(c)}{r}", v, new))
    ush = T.Sheet(R("Users"), sst)
    for (c, r), cel in sorted(ush.cells.items(), key=lambda x: (x[0][1], x[0][0])):
        v = ush.value(c, r)
        if isinstance(v, str) and "(Scopes TC_110)" in v:
            new = v.replace("Scopes TC_110", "Scopes " + new_id(129))
            set_text(cel, sst, new)
            refs.append(("Users", f"{col_letter(c)}{r}", v, new))
    info["refs"] = refs
    if len(refs) != 3:
        raise SystemExit("Chỗ trỏ sang TC của Scopes: chờ 3 chỗ, thấy %d: %s" % (len(refs), refs))

    # 5c. Cover
    cover = R("Cover")
    changes = [
        ["07/10/2026", "1.4", "Scopes", "M",
         "Hanna viết lại khu vực Điều hướng và Danh sách scope (No. 1–67)", "FB-042 → FB-046"],
        ["07/10/2026", "1.5", "Scopes", "M",
         "Viết lại từ Chi tiết scope trở xuống theo cách viết của bản 1.4; thêm case biên cho Evidence coverage, Coverage; "
         "đánh lại No. và TVP_ID", "FB-042 → FB-048"],
        ["07/10/2026", "1.5", "Tất cả sheet", "M",
         "Mọi ô Times New Roman 10; ô bắt đầu bằng dấu - có dấu nháy đơn ở đầu", "FB-016, FB-049"],
    ]
    info["cover_rows"] = [T.add_change(cover, sst, ch, st) for ch in changes]
    csh = T.Sheet(cover, sst)
    c0, r0 = csh.find_text("Effective Date")
    wcol = T.col_widths(cover)
    r = r0 + 1
    while csh.value(c0, r):
        need = 1
        for k in (2, 4, 5):                                                  # Change Item, Change description, Reference
            cel = csh.cells.get((c0 + k, r))
            txt = csh.value(c0 + k, r)
            if cel is None or not isinstance(txt, str):
                continue
            cel.set("s", wrap_variant(st, cel.get("s", "0")))
            per = max(6, int(wcol.get(c0 + k, 10) * 1.12))
            need = max(need, sum(max(1, -(-len(seg) // per)) for seg in txt.split("\n")))
        row_el = csh.rows[r]
        if need > 1:
            row_el.set("ht", str(round(12.75 * need + 3, 2)))
            row_el.set("customHeight", "1")
        r += 1

    # 4. dấu nháy đơn (sau khi mọi kiểu ô đã yên)
    info["quote"] = {}
    for n in order:
        info["quote"][n] = apply_quote_prefix(R(n), sst, st)

    # 7. số đo của LibreOffice
    if a.measure:
        m = json.load(open(a.measure, encoding="utf-8"))
        for n, hs in m.get("heights", {}).items():
            sd = R(n).find(q("sheetData"))
            rowmap = {int(x.get("r")): x for x in sd.findall(q("row"))}
            for rn, h in hs.items():
                rowmap[int(rn)].set("ht", str(h))
                rowmap[int(rn)].set("customHeight", "1")
        n_val = 0
        for n, vals in m.get("values", {}).items():
            cells = {c.get("r"): c for c in R(n).iter(q("c"))}
            for ref, val in vals.items():
                cel = cells.get(ref)
                if cel is None or cel.find(q("f")) is None:
                    continue
                for v in cel.findall(q("v")):
                    cel.remove(v)
                cel.attrib.pop("t", None)
                etree.SubElement(cel, q("v")).text = repr(val) if isinstance(val, float) and not float(val).is_integer() else str(int(val))
                n_val += 1
        info["measure"] = dict(values=n_val, heights={n: len(h) for n, h in m.get("heights", {}).items()})

    # workbook: mở ở sheet Scopes, tính lại công thức khi mở
    bv = wb.find(q("bookViews"))
    if bv is not None:
        for v in bv.findall(q("workbookView")):
            v.set("activeTab", str(order.index("Scopes")))
    for n in order:
        for v in R(n).iter(q("sheetView")):
            if n == "Scopes":
                v.set("tabSelected", "1")
            else:
                v.attrib.pop("tabSelected", None)
    cp = wb.find(q("calcPr"))
    if cp is None:
        cp = etree.SubElement(wb, q("calcPr"))
    cp.set("fullCalcOnLoad", "1")

    # 6. bảng chuỗi
    sheet_paths = [paths[n] for n in order]
    info["sst"] = compact_sst(pkg, sheet_paths, roots, sst_name, sst)

    for p, root in roots.items():
        pkg.put(p, root)
    pkg.put("xl/styles.xml", st_root)
    pkg.put("xl/workbook.xml", wb)
    pkg.save(Path(a.out))
    if a.log:
        json.dump(info, open(a.log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(info, ensure_ascii=False)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
