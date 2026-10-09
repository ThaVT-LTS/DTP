#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So một file TC người dùng đã sửa tay với bản gốc: từng ô theo TVP_ID, case bỏ, case thêm, thứ tự, và định dạng sau khi lưu.

    python compare_edit.py <bản gốc.xlsx> <bản đã sửa.xlsx> <sheet> [--out so-sanh.md] [--json so-sanh.json]

Dùng mỗi khi người dùng gửi lại file TC đã sửa, để biết chính xác họ đổi gì trước khi làm tiếp
(`rules/feedback.md` rule 1: ghi nhận trước khi sửa). Chỉ đọc, không ghi vào file .xlsx.

Phần nội dung so theo TVP_ID của <sheet>. Phần định dạng kiểm cả file đã sửa:
phông khác Times New Roman 10, chữ dạng tổ hợp (chưa NFC), ô bắt đầu bằng - + = @ thiếu dấu nháy đơn,
màu nền ngoài bảng màu, công thức ra lỗi (#REF!…), dòng TC thiếu TVP_ID hoặc UC, ô Open question tô lệch.
"""
import argparse
import difflib
import json
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flat import COLS, flat  # noqa: E402
from xl import Book, col_name, q  # noqa: E402

FONT, SIZE = "Times New Roman", 10.0
FILLS_OK = {"00B0F0", "FBE9E7"}                # nền tiêu đề, nền dòng còn câu hỏi mở
OPEN_FILL = "FBE9E7"
START = ("-", "+", "=", "@")
TC_FIRST_ROW = 13
FIELDS = ["I", "II", "III", "IV", "Pri", "Name", "Pre", "Step", "Exp", "OQ", "UC"]
LABEL = {"I": "Classification I", "II": "Classification II", "III": "Classification III", "IV": "Classification IV",
         "Pri": "Priority", "Name": "Test case name", "Pre": "Pre-condition", "Step": "Step", "Exp": "Expected result",
         "OQ": "Open question", "UC": "UC"}


def nfc(s):
    return unicodedata.normalize("NFC", str(s if s is not None else ""))


def clean(s):
    """Dạng NFC, bỏ khoảng trắng cuối dòng, bỏ dòng trống đầu và cuối ô."""
    s = nfc(s).replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in s.split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def md(s):
    s = clean(s).replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
    return s if s else "(trống)"


def fill_key(book, s):
    f = book.fill(s)
    if not f:
        return None
    if f.get("rgb"):
        return f["rgb"][-6:].upper()
    if "theme" in f:
        return {"0": "trắng (theme 0)"}.get(f["theme"], "theme %s" % f["theme"])
    if "indexed" in f:
        return {"5": "vàng (indexed 5)"}.get(f["indexed"], "indexed %s" % f["indexed"])
    return "khác"


def cell_ranges(refs):
    """['H56','H57','H58','K62'] → 'H56 → H58, K62' (gom các ô liền nhau trong một cột)."""
    by_col = OrderedDict()
    for r in refs:
        col = "".join(ch for ch in r if ch.isalpha())
        by_col.setdefault(col, []).append(int("".join(ch for ch in r if ch.isdigit())))
    out = []
    for col, rows in by_col.items():
        rows = sorted(set(rows))
        i = 0
        while i < len(rows):
            j = i
            while j + 1 < len(rows) and rows[j + 1] == rows[j] + 1:
                j += 1
            out.append("%s%d" % (col, rows[i]) if i == j else "%s%d → %s%d" % (col, rows[i], col, rows[j]))
            i = j + 1
    return ", ".join(out)


def compare_content(a_rows, b_rows):
    a = OrderedDict((r["ID"], r) for r in a_rows)
    b = OrderedDict((r["ID"], r) for r in b_rows)
    res = {"n_a": len(a_rows), "n_b": len(b_rows)}
    res["removed"] = [dict(id=i, **{k: clean(a[i].get(k)) for k in FIELDS}) for i in a if i not in b]
    res["added"] = [dict(id=i, row=b[i]["row"], **{k: clean(b[i].get(k)) for k in FIELDS}) for i in b if i not in a]
    changed = []
    for i, r in b.items():
        if i not in a:
            continue
        diffs = [(k, clean(a[i].get(k)), clean(r.get(k))) for k in FIELDS if clean(a[i].get(k)) != clean(r.get(k))]
        space = [k for k in FIELDS if nfc(a[i].get(k)) != nfc(r.get(k)) and clean(a[i].get(k)) == clean(r.get(k))]
        if diffs or space:
            changed.append({"id": i, "row": r["row"], "no": r["No"], "diffs": diffs, "space_only": space})
    res["changed"] = changed
    ia = [i for i in a if i in b]
    ib = [i for i in b if i in a]
    moves = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ia, ib, autojunk=False).get_opcodes():
        if tag == "insert":
            moves.extend(ib[j1:j2])
    grp = {c["id"] for c in changed if any(k in ("I", "II", "III") for k, _, _ in c["diffs"])}
    moved = []
    for i in moves:
        k = ib.index(i)
        around = ib[max(0, k - 1):k + 3]
        # difflib chỉ ra một trong hai TC đổi chỗ cho nhau; TC nào đổi nhóm thì đó mới là TC được chuyển
        who = next((x for x in around if x in grp), i)
        moved.append({"id": who, "row": b[who]["row"], "order": around})
    res["moved"] = moved
    res["dup_ids"] = sorted(i for i, n in Counter(r["ID"] for r in b_rows).items() if n > 1 and i)
    nos = [str(r["No"]) for r in b_rows]
    res["no_ok"] = nos == [str(k) for k in range(1, len(b_rows) + 1)]
    res["no_id"] = [r["row"] for r in b_rows if not nfc(r["ID"]).strip()]
    res["no_uc"] = [r["ID"] for r in b_rows if not nfc(r["UC"]).strip()]
    res["empty_exp"] = [r["ID"] for r in b_rows if not nfc(r["Exp"]).strip()]
    res["with_oq"] = sum(1 for r in b_rows if nfc(r["OQ"]).strip())
    return res


def check_format(book, tc_sheets):
    out = {"font": {}, "nfc": {}, "quote": {}, "fill": {}, "errors": {}, "oq_fill": {}}
    for name, _, _ in book.sheets:
        cells = book.cells(name)
        has_f = book.formula_cells(name)
        font, form, quote, errs = [], [], [], []
        fills = {}
        for (c, r), (val, s, f, t) in sorted(cells.items(), key=lambda x: (x[0][1], x[0][0])):
            ref = "%s%d" % (col_name(c), r)
            fo = book.font(s)
            if fo["name"] != FONT or float(fo["sz"] or 0) != SIZE:
                font.append(ref)
            if isinstance(val, str) and (c, r) not in has_f:
                if nfc(val) != val:
                    form.append(ref)
                if t in ("s", "inlineStr", "str") and val.lstrip()[:1] in START and book.xf(s).get("quotePrefix") != "1":
                    quote.append(ref)
            if t == "e" or ((c, r) in has_f and isinstance(val, str) and val.startswith("#")):
                errs.append((ref, val))
            fk = fill_key(book, s)
            if fk and fk not in FILLS_OK:
                fills.setdefault(fk, []).append(ref)
        out["font"][name], out["nfc"][name], out["quote"][name] = font, form, quote
        out["errors"][name], out["fill"][name] = errs, fills
        if name in tc_sheets:
            wrong = []
            last = max((r for (c, r), v in cells.items() if c == COLS["ID"] and v[0]), default=TC_FIRST_ROW)
            for r in range(TC_FIRST_ROW, last + 1):
                oq = cells.get((COLS["OQ"], r))
                if oq is None:
                    continue
                has = bool(nfc(oq[0]).strip())
                pink = fill_key(book, oq[1]) == OPEN_FILL
                if has != pink:
                    wrong.append(("%s%d" % (col_name(COLS["OQ"]), r), "có câu hỏi, chưa tô" if has else "hết câu hỏi, còn tô"))
            out["oq_fill"][name] = wrong
    return out


def main():
    ap = argparse.ArgumentParser(description="So file TC đã sửa tay với bản gốc.")
    ap.add_argument("goc")
    ap.add_argument("da_sua")
    ap.add_argument("sheet")
    ap.add_argument("--tc-sheets", default="Login,Scopes,Users,Profile", help="các sheet TC, để kiểm ô Open question")
    ap.add_argument("--out", help="ghi bảng so sánh dạng markdown")
    ap.add_argument("--json", help="ghi kết quả dạng json")
    a = ap.parse_args()

    A, B = Book(a.goc), Book(a.da_sua)
    names = [n for n, _, _ in B.sheets]
    res = compare_content(flat(A, a.sheet), flat(B, a.sheet))
    other = {}
    for n in names:
        if n == a.sheet or n not in [x for x, _, _ in A.sheets]:
            continue
        ca, cb = A.cells(n), B.cells(n)
        fa, fb = A.formula_cells(n), B.formula_cells(n)
        other[n] = sorted("%s%d" % (col_name(c), r) for (c, r) in set(ca) | set(cb)
                          if (c, r) not in fa and (c, r) not in fb
                          and nfc(ca.get((c, r), (None,))[0]) != nfc(cb.get((c, r), (None,))[0]))
    fmt = check_format(B, [s for s in a.tc_sheets.split(",") if s in names])
    res["other_sheets"] = other
    res["format"] = fmt

    L = []
    w = L.append
    w("### Nội dung sheet %s" % a.sheet)
    w("")
    w("| | Bản gốc | Bản đã sửa |")
    w("|---|---|---|")
    w("| Số TC | %d | %d |" % (res["n_a"], res["n_b"]))
    w("| TC đổi chữ | | %d |" % sum(1 for c in res["changed"] if c["diffs"]))
    w("| TC bỏ | | %d |" % len(res["removed"]))
    w("| TC thêm | | %d |" % len(res["added"]))
    w("| TC đổi chỗ | | %d |" % len(res["moved"]))
    w("| TC còn câu hỏi mở | | %d |" % res["with_oq"])
    w("| TC để trống Expected | | %d%s |" % (len(res["empty_exp"]), (": " + ", ".join(res["empty_exp"])) if 0 < len(res["empty_exp"]) <= 12 else ""))
    w("")
    if res["changed"]:
        w("| TC | Dòng | Cột | Trước | Sau |")
        w("|---|---|---|---|---|")
        for c in res["changed"]:
            for k, old, new in c["diffs"]:
                w("| %s | %s | %s | %s | %s |" % (c["id"], c["row"], LABEL[k], md(old), md(new)))
        w("")
    sp = [c for c in res["changed"] if c["space_only"]]
    if sp:
        w("Chỉ khác khoảng trắng ở đầu, cuối ô: " + "; ".join("%s (%s)" % (c["id"], ", ".join(LABEL[k] for k in c["space_only"])) for c in sp) + ".")
        w("")
    for title, key in (("TC bỏ", "removed"), ("TC thêm", "added")):
        if res[key]:
            w("**%s**" % title)
            w("")
            w("| TC | Khu vực ▸ nhóm ▸ case | Tên case | Expected | Open question |")
            w("|---|---|---|---|---|")
            for r in res[key]:
                w("| %s | %s ▸ %s ▸ %s | %s | %s | %s |" % (r["id"], md(r["II"]), md(r["III"]), md(r["IV"]), md(r["Name"]), md(r["Exp"]), md(r["OQ"])))
            w("")
    if res["moved"]:
        w("**TC đổi chỗ:** " + "; ".join("%s nay ở dòng %s (thứ tự mới: %s)" % (m["id"], m["row"], " → ".join(m["order"])) for m in res["moved"]) + ".")
        w("")
    notes = []
    if res["dup_ids"]:
        notes.append("TVP_ID trùng: %s" % ", ".join(res["dup_ids"]))
    if not res["no_ok"]:
        notes.append("cột No. không liền mạch từ 1")
    if res["no_id"]:
        notes.append("dòng thiếu TVP_ID: %s" % ", ".join(str(x) for x in res["no_id"]))
    if res["no_uc"]:
        notes.append("TC thiếu UC: %s" % ", ".join(res["no_uc"]))
    w("Kiểm nhanh: " + ("; ".join(notes) if notes else "TVP_ID không trùng, cột No. liền mạch, không dòng nào thiếu TVP_ID hay UC") + ".")
    w("")
    ch = {n: v for n, v in other.items() if v}
    w("Sheet khác: " + ("; ".join("%s đổi %d ô (%s)" % (n, len(v), cell_ranges(v[:30])) for n, v in ch.items()) if ch else "không ô nào đổi nội dung (không tính ô công thức)") + ".")
    w("")
    w("### Định dạng của bản đã sửa")
    w("")
    w("| Kiểm | Kết quả |")
    w("|---|---|")

    def per_sheet(d, fmt_item=lambda v: "%d ô (%s)" % (len(v), cell_ranges(v))):
        parts = ["%s: %s" % (n, fmt_item(v)) for n, v in d.items() if v]
        return "; ".join(parts) if parts else "không có"

    w("| Ô khác %s %g | %s |" % (FONT, SIZE, per_sheet(fmt["font"])))
    w("| Ô có chữ dạng tổ hợp (chưa NFC) | %s |" % per_sheet(fmt["nfc"]))
    w("| Ô bắt đầu bằng - + = @ thiếu dấu nháy đơn | %s |" % per_sheet(fmt["quote"]))
    fills = []
    for n, d in fmt["fill"].items():
        for k, v in d.items():
            rows = sorted({int("".join(ch for ch in x if ch.isdigit())) for x in v})
            fills.append("%s: nền %s ở %d ô, dòng %s" % (n, k, len(v), ", ".join(str(x) for x in rows)))
    w("| Màu nền ngoài bảng màu | %s |" % ("; ".join(fills) if fills else "không có"))
    w("| Công thức ra lỗi | %s |" % per_sheet(fmt["errors"], lambda v: "%d ô, vd %s = %s" % (len(v), v[0][0], v[0][1])))
    w("| Ô Open question tô lệch | %s |" % per_sheet(fmt["oq_fill"], lambda v: ", ".join("%s (%s)" % x for x in v)))
    text = "\n".join(L) + "\n"
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, encoding="utf-8", newline="\n")
        print("→", a.out)
    else:
        sys.stdout.write(text)
    if a.json:
        Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
