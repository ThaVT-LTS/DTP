#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm bản v1.5 ở mức XML, so với bản v1.4.

    python verify_v15.py <v1.4.xlsx> <v1.5.xlsx> <scopes_v15.json>
"""
import hashlib
import json
import re
import sys
import unicodedata
import zipfile
from collections import Counter

from pathlib import Path  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lxml import etree  # noqa: E402
from xl import Book, NS, q, col_name, col_no, split_ref  # noqa: E402

FONT, SIZE = "Times New Roman", 10.0
FILLS_OK = {"00B0F0", "FBE9E7"}
FONTCOL_OK = {"363A45", "B8362B", "FFFFFF", "000000"}
START = ("-", "+", "=", "@")
TC_SHEETS = ["Login", "Scopes", "Users", "Profile"]

errors, notes = [], []


def err(msg):
    errors.append(msg)


def rgb(el):
    if el is None:
        return None
    v = el.get("rgb")
    return v[-6:].upper() if v else ("indexed:%s" % el.get("indexed") if el.get("indexed") else ("theme:%s" % el.get("theme") if el.get("theme") else None))


def used_styles(book, name):
    root = book.root(name)
    out = Counter()
    for c in root.iter(q("c")):
        out[int(c.get("s", "0"))] += 1
    for col in root.iter(q("col")):
        out[int(col.get("style", "0"))] += 1
    for row in root.iter(q("row")):
        if row.get("s"):
            out[int(row.get("s"))] += 1
    return out


def main():
    old_p, new_p, rows_p = sys.argv[1:4]
    old, new = Book(old_p), Book(new_p)
    data = json.load(open(rows_p, encoding="utf-8"))
    rows = data["rows"]

    # ---------------- gói zip
    zo, zn = zipfile.ZipFile(old_p), zipfile.ZipFile(new_p)
    if zn.testzip() is not None:
        err("zip hỏng")
    if sorted(zo.namelist()) != sorted(zn.namelist()):
        err("danh sách phần trong zip khác bản v1.4: %s" % (set(zo.namelist()) ^ set(zn.namelist())))
    same, diff = [], []
    for n in zo.namelist():
        (same if hashlib.md5(zo.read(n)).hexdigest() == hashlib.md5(zn.read(n)).hexdigest() else diff).append(n)
    notes.append("phần không đổi: %d · phần đổi: %s" % (len(same), sorted(diff)))
    for n in zn.namelist():
        if n.endswith(".xml") or n.endswith(".rels"):
            try:
                etree.fromstring(zn.read(n))
            except Exception as e:
                err("XML lỗi ở %s: %s" % (n, e))
    for n in ("xl/media/image1.png", "xl/drawings/drawing1.xml", "xl/theme/theme1.xml", "[Content_Types].xml", "xl/_rels/workbook.xml.rels"):
        if n in diff:
            err("phần %s bị đổi" % n)

    # ---------------- 1. phông, màu: mọi kiểu ô đang được dùng ở mọi sheet
    for name, _, _ in new.sheets:
        for s, n in sorted(used_styles(new, name).items()):
            xf = new.xfs[s]
            f = new.fonts[int(xf.get("fontId", "0"))]
            fname = f.find(q("name")).get("val")
            sz = float(f.find(q("sz")).get("val"))
            if fname != FONT or sz != SIZE:
                err("%s · kiểu ô %d (%d chỗ) phông %s %g" % (name, s, n, fname, sz))
            if f.find(q("i")) is not None or f.find(q("u")) is not None or f.find(q("strike")) is not None:
                err("%s · kiểu ô %d chữ nghiêng / gạch" % (name, s))
            fc = rgb(f.find(q("color")))
            if fc and not fc.startswith("indexed:65") and fc not in FONTCOL_OK:
                err("%s · kiểu ô %d màu chữ %s" % (name, s, fc))
            pf = new.fills[int(xf.get("fillId", "0"))].find(q("patternFill"))
            if pf is not None and pf.get("patternType") not in (None, "none"):
                bg = rgb(pf.find(q("fgColor")))
                if bg not in FILLS_OK:
                    err("%s · kiểu ô %d (%d chỗ) nền %s" % (name, s, n, bg))
    sst = etree.fromstring(zn.read("xl/sharedStrings.xml"))
    if sst.findall(".//" + q("rPr")):
        err("sharedStrings có đoạn chữ định dạng riêng")
    si = sst.findall(q("si"))
    texts = ["".join(t.text or "" for t in s.iter(q("t"))) for s in si]
    if len(set(texts)) != len(texts):
        err("sharedStrings có chuỗi trùng")
    if int(sst.get("uniqueCount")) != len(si):
        err("uniqueCount lệch")
    bad_nfc = [t for t in texts if unicodedata.normalize("NFC", t) != t]
    if bad_nfc:
        err("%d chuỗi chưa ở dạng NFC" % len(bad_nfc))
    refs = Counter()
    for name, _, _ in new.sheets:
        for c in new.root(name).iter(q("c")):
            if c.get("t") == "s":
                refs[int(c.find(q("v")).text)] += 1
    if max(refs) >= len(si) or len(refs) != len(si) or sum(refs.values()) != int(sst.get("count")):
        err("sharedStrings: chỉ số / count lệch (max %d, dùng %d/%d, count %s vs %d)" % (max(refs), len(refs), len(si), sst.get("count"), sum(refs.values())))

    # ---------------- 5. dấu nháy đơn đầu ô
    nq = Counter()
    for name, _, _ in new.sheets:
        for (c, r), (val, s, f, t) in new.cells(name).items():
            if f is not None or not isinstance(val, str) or t not in ("s", "inlineStr", "str"):
                continue
            quoted = new.xfs[int(s)].get("quotePrefix") == "1"
            if val.lstrip()[:1] in START:
                nq[name] += 1
                if not quoted:
                    err("%s!%s%d bắt đầu bằng %r mà không có quotePrefix" % (name, col_name(c), r, val[:1]))
            elif quoted:
                err("%s!%s%d có quotePrefix thừa" % (name, col_name(c), r))
    notes.append("ô có dấu nháy đơn: %s (tổng %d)" % (dict(nq), sum(nq.values())))

    # ---------------- Scopes: nội dung đúng bảng phẳng
    cells = new.cells("Scopes")
    merges = new.merges("Scopes")
    anchor = {}
    for c1, r1, c2, r2 in merges:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                anchor[(c, r)] = (c1, r1)
    COLS = {"I": 2, "II": 3, "III": 4, "IV": 5, "Pri": 6, "Name": 8, "Pre": 9, "Step": 10, "Exp": 11, "OQ": 23, "UC": 24}

    def val(c, r):
        a = anchor.get((c, r), (c, r))
        v = cells.get(a, (None,))[0]
        return v if v is not None else ""

    first, last = 13, 13 + len(rows) - 1
    for i, rec in enumerate(rows):
        r = first + i
        if str(cells[(1, r)][0]) != str(i + 1):
            err("Scopes!A%d No. = %r" % (r, cells[(1, r)][0]))
        if cells[(7, r)][0] != "Scope_%03d" % (i + 1):
            err("Scopes!G%d TVP_ID = %r" % (r, cells[(7, r)][0]))
        for k, c in COLS.items():
            if val(c, r) != rec[k]:
                err("Scopes!%s%d khác bảng phẳng: %r ≠ %r" % (col_name(c), r, val(c, r)[:60], rec[k][:60]))
        for c in range(12, 23):
            if cells.get((c, r), (None,))[0] not in (None, ""):
                err("Scopes!%s%d có giá trị ngoài dự kiến" % (col_name(c), r))
        if not rec["UC"]:
            err("Scopes dòng %d thiếu UC" % r)
        if not rec["Exp"] and not rec["OQ"]:
            err("Scopes dòng %d không có Expected lẫn Open question" % r)
        if rec["Pri"] not in ("High", "Medium", "Low"):
            err("Scopes dòng %d Priority %r" % (r, rec["Pri"]))
        for k in ("Name", "Pre", "Step", "Exp", "OQ", "I", "II", "III", "IV"):
            if "{{" in rec[k] or "}}" in rec[k]:
                err("Scopes dòng %d cột %s còn {{…}}" % (r, k))
        if not rec["Pre"].startswith("Đăng nhập "):
            err("Scopes dòng %d Pre-condition không mở đầu bằng dòng đăng nhập: %r" % (r, rec["Pre"][:40]))
        if not re.match(r"1\. ", rec["Step"]):
            err("Scopes dòng %d Step không bắt đầu bằng '1. '" % r)
    extra = [r for (c, r) in cells if r > last and cells[(c, r)][0] not in (None, "")]
    if extra:
        err("Scopes còn ô có nội dung sau dòng %d: %s" % (last, sorted(set(extra))[:5]))
    max_row = max(r for (c, r) in cells)
    if max_row != last:
        err("Scopes dòng cuối trong XML = %d, chờ %d" % (max_row, last))
    # gộp ô: cụm con nằm trong cụm cha, không chồng nhau
    seen = set()
    for c1, r1, c2, r2 in merges:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if (c, r) in seen:
                    err("gộp ô chồng nhau tại %s%d" % (col_name(c), r))
                seen.add((c, r))
        if r1 >= first and c1 == c2 and c1 in (3, 4, 5):
            pa = anchor.get((c1 - 1, r1)), anchor.get((c1 - 1, r2))
            parent = [m for m in merges if m[0] == c1 - 1 and m[1] <= r1 and m[3] >= r2]
            if not parent and r1 != r2:
                # cha không gộp → mọi dòng của cụm con phải cùng ô cha (không thể, vì cha một dòng)
                err("cụm %s%d:%s%d vượt ranh giới cụm cha" % (col_name(c1), r1, col_name(c2), r2))
        if r1 >= first and r2 > last:
            err("gộp ô vượt quá vùng dữ liệu: %s%d:%s%d" % (col_name(c1), r1, col_name(c2), r2))
    # ô trong cụm gộp (không phải ô neo) phải trống
    for (c, r), a in anchor.items():
        if (c, r) != a and cells.get((c, r), (None,))[0] not in (None, ""):
            err("ô %s%d nằm trong cụm gộp mà có giá trị" % (col_name(c), r))
    # nhóm kết quả: Không thành công đứng trước Thành công trong cùng khu vực; khu vực có Thành công phải có Không thành công
    area = {}
    for rec in rows:
        area.setdefault((rec["I"], rec["II"]), []).append(rec["III"])
    for k, seq in area.items():
        groups = [g for i, g in enumerate(seq) if i == 0 or seq[i - 1] != g]
        if len(groups) != len(set(groups)):
            err("khu vực %s: nhóm III không liền nhau: %s" % (k[1], groups))
        if "Thành công" in groups and "Không thành công" not in groups:
            err("khu vực %s có Thành công mà thiếu Không thành công" % k[1])
        if "Thành công" in groups and "Không thành công" in groups and groups.index("Không thành công") > groups.index("Thành công"):
            err("khu vực %s: Thành công đứng trước Không thành công (khác cách của bản v1.4)" % k[1])
        if "Kiểm tra dữ liệu" in groups:
            err("khu vực %s còn nhóm Kiểm tra dữ liệu" % k[1])
    # kiểu ô vùng dữ liệu của Scopes
    sty = Counter()
    for (c, r), v in cells.items():
        if first <= r <= last:
            sty[(col_name(c) if c > 5 else "B-E" if c > 1 else "A", v[1])] += 1
    notes.append("Scopes kiểu ô vùng dữ liệu: %s" % sorted(sty.items(), key=lambda x: (len(x[0][0]), x[0])))
    # ô Open question / Expected trống: tô đúng
    for i, rec in enumerate(rows):
        r = first + i
        w = new.fill(cells[(23, r)][1])
        k = new.fill(cells[(11, r)][1])
        if bool(rec["OQ"]) != (w is not None):
            err("Scopes!W%d tô nền không khớp câu hỏi mở" % r)
        if (bool(rec["OQ"]) and not rec["Exp"]) != (k is not None):
            err("Scopes!K%d tô nền không khớp (Expected trống + có câu hỏi)" % r)
    # công thức khối tổng kết, vùng dropdown
    root = new.root("Scopes")
    for c in root.iter(q("c")):
        f = c.find(q("f"))
        if f is not None and f.text:
            for m in re.finditer(r"\$([A-Z]+)\$(\d+):\$([A-Z]+)\$(\d+)", f.text):
                if (int(m.group(2)), int(m.group(4))) != (first, last):
                    err("Scopes!%s công thức %s không phủ đúng %d–%d" % (c.get("r"), f.text, first, last))
    xml = zn.read(next(p for n, p, _ in new.sheets if n == "Scopes")).decode("utf-8")
    sq = re.findall(r"<xm:sqref>([^<]+)</xm:sqref>", xml)
    if sorted(sq) != sorted(["F13:F%d" % last, "M13:M%d R13:R%d" % (last, last)]):
        err("Scopes vùng dropdown: %s" % sq)
    hts = {int(r.get("r")): r for r in root.iter(q("row"))}
    for r in range(first, last + 1):
        if hts[r].get("customHeight") != "1" or not hts[r].get("ht"):
            err("Scopes dòng %d thiếu chiều cao" % r)

    # ---------------- các sheet khác: nội dung không đổi
    allowed = {("Users", "W13"), ("Cần xác nhận", "D2"), ("Cần xác nhận", "E20")}
    for name in ("Login", "Users", "Profile", "Cần xác nhận"):
        a, b = old.cells(name), new.cells(name)
        for k in sorted(set(a) | set(b), key=lambda x: (x[1], x[0])):
            va = a.get(k, (None, None, None, None))
            vb = b.get(k, (None, None, None, None))
            ref = "%s%d" % (col_name(k[0]), k[1])
            if (va[0] or "") != (vb[0] or "") or (va[2] or "") != (vb[2] or ""):
                if (name, ref) in allowed:
                    notes.append("%s!%s: %r → %r" % (name, ref, va[0], vb[0]))
                else:
                    err("%s!%s đổi nội dung: %r → %r" % (name, ref, str(va[0])[:60], str(vb[0])[:60]))
        if old.merges(name) != new.merges(name):
            err("%s đổi gộp ô" % name)
        ra, rb = old.root(name), new.root(name)
        ha = {r.get("r"): (r.get("ht"), r.get("customHeight")) for r in ra.iter(q("row"))}
        hb = {r.get("r"): (r.get("ht"), r.get("customHeight")) for r in rb.iter(q("row"))}
        if ha != hb:
            err("%s đổi chiều cao dòng" % name)
        ca = [dict(c.attrib) for c in ra.iter(q("col"))]
        cb = [dict(c.attrib) for c in rb.iter(q("col"))]
        if ca != cb:
            err("%s đổi định nghĩa cột" % name)
    # Cover: chỉ thêm dòng Record of change và ô Version
    a, b = old.cells("Cover"), new.cells("Cover")
    for k in sorted(set(a) | set(b), key=lambda x: (x[1], x[0])):
        va, vb = a.get(k, (None,))[0], b.get(k, (None,))[0]
        if (va or "") != (vb or ""):
            notes.append("Cover!%s%d: %r → %r" % (col_name(k[0]), k[1], va, vb))
            if not (k[1] in (17, 18, 19) or (col_name(k[0]), k[1]) == ("G", 6)):
                err("Cover!%s%d đổi ngoài dự kiến" % (col_name(k[0]), k[1]))

    # ---------------- Test_Report
    rep = new.cells("Test_Report")
    r = 4
    expect = []
    for name in TC_SHEETS:
        cc = new.cells(name)
        mm = new.merges(name)
        anc = {}
        for c1, r1, c2, r2 in mm:
            for rr in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    anc[(c, rr)] = (c1, r1)
        seq = []
        for rr in sorted({k[1] for k in cc if k[1] >= 13}):
            if not cc.get((7, rr), (None,))[0]:
                continue
            g = lambda c: cc.get(anc.get((c, rr), (c, rr)), (None,))[0] or ""   # noqa: E731
            seq.append((g(2), g(3), rr))
        pairs = []
        for i_, ii, rr in seq:
            if pairs and pairs[-1][0] == i_ and pairs[-1][1] == ii and pairs[-1][3] == rr - 1:
                pairs[-1] = (i_, ii, pairs[-1][2], rr)
            else:
                pairs.append((i_, ii, rr, rr))
        expect.append((name, pairs, len(seq)))
    total_all = 0
    for name, pairs, n in expect:
        b0 = r
        for k, (i_, ii, a_, b_) in enumerate(pairs):
            if (rep.get((3, r), (None,))[0], rep.get((4, r), (None,))[0]) != (i_, ii):
                err("Test_Report dòng %d: %r / %r ≠ %r / %r" % (r, rep.get((3, r), (None,))[0], rep.get((4, r), (None,))[0], i_, ii))
            if k == 0 and rep.get((2, r), (None,))[0] != name:
                err("Test_Report dòng %d thiếu tên sheet %s" % (r, name))
            f = rep[(13, r)][2]
            want = "COUNTA('%s'!$G$%d:$G$%d)-SUM(H%d:L%d)" % (name, a_, b_, r, r)
            if f != want:
                err("Test_Report!M%d công thức %r ≠ %r" % (r, f, want))
            for col in (7, 13, 16, 22):                    # Total, Not execute của hai vòng
                if float(rep[(col, r)][0]) != b_ - a_ + 1:
                    err("Test_Report!%s%d giá trị đã lưu %s ≠ %d" % (col_name(col), r, rep[(col, r)][0], b_ - a_ + 1))
            r += 1
        if rep.get((3, r), (None,))[0] != "Total":
            err("Test_Report dòng %d chờ dòng Total của %s" % (r, name))
        if float(rep[(7, r)][0]) != n:
            err("Test_Report!G%d tổng %s đã lưu %s ≠ %d" % (r, name, rep[(7, r)][0], n))
        total_all += n
        r += 1
    if rep.get((2, r), (None,))[0] != "Total" or float(rep[(7, r)][0]) != total_all:
        err("Test_Report dòng tổng cuối (%d): %r, %r ≠ %d" % (r, rep.get((2, r), (None,))[0], rep.get((7, r), (None,))[0], total_all))
    notes.append("Test_Report: %s · tổng %d TC · dòng tổng %d" % ({n: c for n, _, c in expect}, total_all, r))
    for (c, rr), v in rep.items():
        if v[2] is not None and v[0] is None:
            err("Test_Report!%s%d công thức chưa có giá trị đã lưu" % (col_name(c), rr))
    sc = new.cells("Scopes")
    for ref in ("L4", "R4", "L6", "R6"):
        c, rr = split_ref(ref)
        if float(sc[(c, rr)][0]) != len(rows):
            err("Scopes!%s giá trị đã lưu %s ≠ %d" % (ref, sc[(c, rr)][0], len(rows)))

    wbx = zn.read("xl/workbook.xml").decode("utf-8")
    if 'fullCalcOnLoad="1"' not in wbx:
        err("workbook thiếu fullCalcOnLoad")

    print("\n".join("· " + n for n in notes))
    print("\n%d lỗi" % len(errors))
    for e in errors[:80]:
        print("LỖI:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
