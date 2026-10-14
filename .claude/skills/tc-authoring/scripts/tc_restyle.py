#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đưa một file test case về MỘT phông, MỘT bảng màu (references/format.md §4 · tc_palette.py).

    python tc_restyle.py in.xlsx --out out.xlsx \\
        [--copy-style "*!F11>W11,X11"] [--rename-header "Chờ text=Open question"] [--fix-summary] \\
        [--change "02/10/2026|1.1|Tất cả sheet|M|Một màu, một phông|FB-016"]

Làm trên XML (cần lxml) nên giữ nguyên logo, dropdown, công thức, độ rộng cột. Việc script làm:
  1. Mọi kiểu ô của mọi sheet: phông và cỡ chữ chuẩn; bỏ nghiêng, gạch chân; giữ đậm, gạch ngang,
     chỉ số trên/dưới.
  2. Mọi ô có nền → một màu nền tiêu đề, chữ trắng. Ô không nền → một màu chữ.
     Nền trắng và nền "màu cửa sổ" coi như không nền. Nền của dòng còn câu hỏi mở được giữ.
  3. Đường kẻ về một màu (tự động).
  4. Bỏ định dạng có điều kiện tô màu ngoài bảng màu.
  5. Sheet TC: tô ô Open question (và ô Expected result nếu trống) ở dòng còn câu hỏi mở,
     bỏ tô ở dòng đã hết câu hỏi.
  6. Chữ định dạng riêng từng đoạn trong một ô (rich text): từng đoạn về phông, cỡ chuẩn,
     màu chữ theo kiểu của ô chứa nó.

Tuỳ chọn:
  --copy-style     chép kiểu của một ô sang các ô khác, vd "Login!F11>W11,X11"; sheet "*" = mọi sheet TC
  --rename-header  đổi tên một cột ở hàng tiêu đề của mọi sheet TC, vd "Chờ text=Open question"
  --fix-summary    khối tổng kết của mọi sheet TC: vùng đếm bắt đầu ở dòng dữ liệu đầu và phủ tới dòng cuối
  --change         thêm một dòng Record of change ở trang bìa: ngày|version|mục|A/D/M|mô tả|tham chiếu
                   (lặp lại tuỳ chọn để thêm nhiều dòng)

Phông của kiểu Normal (fonts[0]) được giữ nguyên: bảng tính đo độ rộng cột theo phông này,
đổi nó thì mọi cột co giãn theo. Mọi ô — kể cả ô chưa định dạng — vẫn dùng phông chuẩn.
Chạy lại nhiều lần cho cùng một file không đổi thêm gì.
"""
from __future__ import annotations

import argparse
import copy
import re
import sys
from collections import Counter
from pathlib import Path

from lxml import etree

from tc_add_sheet import (RNS, X14, Package, SharedStrings, Sheet, Styles, TcLayout, _cell, _sig, add_change,
                          fix_summary_ranges, mark_open_rows, norm, q, rgb_of, split_ref, utf8_console)
from tc_palette import FONT, HEAD_FILL, HEAD_FONT, OPEN_FILL, OPEN_FONT, PALETTE_FILL, PALETTE_FONT, SIZE, TEXT


# ----------------------------------------------------------------------------- kiểu ô
def fill_kind(fill) -> str:
    """'none' = không nền · 'open' = nền dòng câu hỏi mở · 'head' = mọi nền khác."""
    pf = fill.find(q("patternFill"))
    if pf is None or pf.get("patternType") in (None, "none"):
        return "none"
    fg = pf.find(q("fgColor"))
    if fg is None:
        return "head"
    rgb = rgb_of(fg)
    if rgb:
        return "none" if rgb == "FFFFFF" else "open" if rgb == OPEN_FILL else "head"
    if fg.get("indexed") in ("1", "9", "65"):                       # trắng, hoặc màu nền cửa sổ
        return "none"
    if fg.get("theme") == "0" and float(fg.get("tint") or 0) == 0:  # màu sáng 1 của theme = trắng
        return "none"
    return "head"


KEEP_TAGS = ("b", "strike", "vertAlign")      # đậm, gạch ngang, chỉ số trên/dưới: mang nghĩa, giữ lại


def make_font(src, rgb: str, tag: str = "font"):
    """Phông chuẩn với màu `rgb`, giữ đậm / gạch ngang / chỉ số trên-dưới của `src`.
    tag="font" cho kiểu ô (tên phông ở <name>), tag="rPr" cho một đoạn chữ (tên phông ở <rFont>)."""
    f = etree.Element(q(tag))
    for e in src:
        if etree.QName(e).localname in KEEP_TAGS and e.get("val", "1") not in ("0", "false"):
            f.append(copy.deepcopy(e))
    etree.SubElement(f, q("sz")).set("val", str(SIZE))
    etree.SubElement(f, q("color")).set("rgb", "FF" + rgb)
    etree.SubElement(f, q("name" if tag == "font" else "rFont")).set("val", FONT)
    return f


def normalize(st: Styles) -> Counter:
    """Sửa tại chỗ mọi kiểu ô (cellXfs). Chỉ thêm phông và nền mới, không xoá định nghĩa cũ,
    nên chỉ số kiểu trong các sheet không đổi."""
    kinds = [fill_kind(f) for f in st.fills]
    sources = list(st.fonts)
    colors = [rgb_of(f.find(q("color"))) for f in sources]
    fill_of = {"none": 0, "head": st.fill_id(HEAD_FILL), "open": st.fill_id(OPEN_FILL)}
    n = Counter()
    for xf in list(st.xfs):
        fid, lid = int(xf.get("fontId", "0")), int(xf.get("fillId", "0"))
        kind = kinds[lid] if lid < len(kinds) else "none"
        if kind == "none":
            rgb = TEXT
        elif kind == "head":
            rgb = HEAD_FONT
        else:                                    # ô Expected result tô nền giữ màu chữ thường
            rgb = colors[fid] if colors[fid] in (TEXT, OPEN_FONT) else OPEN_FONT
        font = st.add(st.fonts, make_font(sources[fid], rgb))
        fill = fill_of[kind]
        if font != fid:
            n["kiểu ô đổi phông hoặc màu chữ"] += 1
            xf.set("fontId", str(font))
            st.changed = True
        if fill != lid:
            n["kiểu ô đổi nền"] += 1
            xf.set("fillId", str(fill))
            st.changed = True
        xf.set("applyFont", "1")
        if kind != "none":
            xf.set("applyFill", "1")
    borders = st.root.find(q("borders"))
    if borders is not None:
        for col in borders.iter(q("color")):
            if dict(col.attrib) != {"auto": "1"}:
                col.attrib.clear()
                col.set("auto", "1")
                n["đường kẻ đổi màu"] += 1
                st.changed = True
    return n


# ----------------------------------------------------------------------------- chữ định dạng từng đoạn
def fix_runs(text_el, rgb: str) -> int:
    """Một chuỗi (<si> hoặc <is>): từng đoạn có định dạng riêng về phông, cỡ chuẩn và màu `rgb`.
    Đoạn không có định dạng riêng thì vốn đã theo kiểu của ô. Trả về số đoạn đã sửa."""
    n = 0
    for run in text_el.findall(q("r")):
        old = run.find(q("rPr"))
        if old is None:
            continue
        new = make_font(old, rgb, "rPr")
        if _sig(new) != _sig(old):
            run.replace(old, new)
            n += 1
    return n


def normalize_runs(roots, sst: SharedStrings, st: Styles) -> int:
    """Chữ định dạng riêng từng đoạn trong một ô đè lên phông của kiểu ô, nên phải sửa riêng.
    Màu chữ của đoạn lấy theo kiểu của ô chứa nó; một chuỗi dùng ở hai ô khác màu chữ thì tách làm hai."""
    n = 0
    uses: dict[int, dict[str, list]] = {}
    for root in roots:
        for cel in root.iter(q("c")):
            rgb = st.font_rgb(cel.get("s", "0")) or TEXT
            if cel.get("t") == "s":
                v = cel.find(q("v"))
                if v is not None and v.text and sst.items[int(v.text)].find(q("r")) is not None:
                    uses.setdefault(int(v.text), {}).setdefault(rgb, []).append(v)
            elif cel.get("t") == "inlineStr":
                txt = cel.find(q("is"))
                if txt is not None:
                    n += fix_runs(txt, rgb)
    for i, by_rgb in uses.items():
        for k, (rgb, refs) in enumerate(sorted(by_rgb.items(), key=lambda kv: -len(kv[1]))):
            j = i if k == 0 else sst.clone(i)
            for v in refs:
                v.text = str(j)
            n += fix_runs(sst.items[j], rgb)
    return n


# ----------------------------------------------------------------------------- định dạng có điều kiện
def drop_cf(sheet_root, st_root) -> int:
    """Bỏ quy tắc định dạng có điều kiện tô màu ngoài bảng màu. Trả về số quy tắc đã bỏ."""
    ok = PALETTE_FILL | PALETTE_FONT
    dxfs = st_root.find(q("dxfs"))
    n = 0

    def off(el) -> bool:
        cols = [rgb_of(c) for tag in ("fgColor", "bgColor", "color") for c in el.iter(q(tag))]
        return any(c and c not in ok for c in cols)

    for cf in list(sheet_root.iter(q("conditionalFormatting"))):
        for rule in list(cf.findall(q("cfRule"))):
            i = rule.get("dxfId")
            dxf = dxfs[int(i)] if i is not None and dxfs is not None and int(i) < len(dxfs) else None
            if off(rule) or (dxf is not None and off(dxf)):
                cf.remove(rule)
                n += 1
        if not cf.findall(q("cfRule")):
            cf.getparent().remove(cf)
    for cf in list(sheet_root.iter(f"{{{X14}}}conditionalFormatting")):
        if off(cf):
            n += len(cf.findall(f"{{{X14}}}cfRule"))
            box = cf.getparent()
            box.remove(cf)
            if len(box) == 0:                                   # x14:conditionalFormattings rỗng → bỏ cả <ext>
                ext = box.getparent()
                ext.getparent().remove(ext)
    ext_lst = sheet_root.find(q("extLst"))
    if ext_lst is not None and len(ext_lst) == 0:
        sheet_root.remove(ext_lst)
    return n


# ----------------------------------------------------------------------------- main
def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description="Đưa file test case về một phông, một bảng màu.")
    ap.add_argument("book")
    ap.add_argument("--out", required=True)
    ap.add_argument("--copy-style", action="append", default=[], metavar='"Sheet!F11>W11,X11"')
    ap.add_argument("--rename-header", action="append", default=[], metavar='"Tên cũ=Tên mới"')
    ap.add_argument("--fix-summary", action="store_true",
                    help="khối tổng kết của sheet TC: vùng đếm bắt đầu ở dòng dữ liệu đầu, phủ tới dòng cuối")
    ap.add_argument("--change", action="append", default=[], metavar='"ngày|version|mục|A/D/M|mô tả|tham chiếu"',
                    help="một dòng Record of change; lặp lại tuỳ chọn để thêm nhiều dòng")
    a = ap.parse_args()

    pkg = Package(Path(a.book))
    wb = pkg.xml("xl/workbook.xml")
    rels = pkg.xml("xl/_rels/workbook.xml.rels")
    target = {r.get("Id"): r.get("Target") for r in rels}

    def part(kind, default):
        return next(("xl/" + r.get("Target").lstrip("/").replace("xl/", "", 1) for r in rels
                     if r.get("Type").endswith("/" + kind)), default)

    sst_name, st_name = part("sharedStrings", "xl/sharedStrings.xml"), part("styles", "xl/styles.xml")
    sst_root, st_root = pkg.xml(sst_name), pkg.xml(st_name)
    sst, st = SharedStrings(sst_root), Styles(st_root)

    sheets = []                                     # (tên, đường dẫn, root, bố cục TC hoặc None)
    for s in wb.find(q("sheets")).findall(q("sheet")):
        t = target[s.get(f"{{{RNS}}}id")]
        path = t.lstrip("/") if t.startswith("/") else "xl/" + t
        root = pkg.xml(path)
        lay = None
        if root.find(q("sheetData")) is not None:
            sh = Sheet(root, sst)
            if sh.find_text("No."):
                try:
                    lay = TcLayout(sh)
                except SystemExit:
                    lay = None
        sheets.append((s.get("name"), path, root, lay))
    tc_names = [n for n, _, _, lay in sheets if lay]
    by_name = {n: root for n, _, root, _ in sheets}

    # 1–3. kiểu ô
    stats = normalize(st)

    # 4. định dạng có điều kiện
    n_cf = sum(drop_cf(root, st_root) for _, _, root, _ in sheets)

    # chép kiểu ô
    n_copy = 0
    for spec in a.copy_style:
        m = re.match(r"^(.+)!([A-Z]+\d+)>([A-Z0-9,\s]+)$", spec.strip())
        if not m:
            raise SystemExit(f"--copy-style sai cú pháp: {spec}")
        names = tc_names if m.group(1) == "*" else [m.group(1)]
        for name in names:
            if name not in by_name:
                raise SystemExit(f"--copy-style: không có sheet '{name}'")
            root = by_name[name]
            src = _cell(root, *split_ref(m.group(2))).get("s")
            if src is None:
                raise SystemExit(f"--copy-style: ô {name}!{m.group(2)} chưa có kiểu")
            for ref in re.split(r"[,\s]+", m.group(3).strip()):
                cel = _cell(root, *split_ref(ref))
                if cel.get("s") != src:
                    cel.set("s", src)
                    n_copy += 1

    # đổi tên cột ở hàng tiêu đề
    n_ren = 0
    for spec in a.rename_header:
        old, _, new = spec.partition("=")
        if not new:
            raise SystemExit(f"--rename-header sai cú pháp: {spec}")
        for name, _, root, lay in sheets:
            if not lay:
                continue
            sh = Sheet(root, sst)
            for (c, r), cel in sh.cells.items():
                if r in (lay.hdr1, lay.hdr2) and norm(sh.value(c, r) or "") == norm(old):
                    for ch in list(cel):
                        cel.remove(ch)
                    cel.set("t", "s")
                    etree.SubElement(cel, q("v")).text = str(sst.get(new.strip()))
                    n_ren += 1

    # 5. dòng còn câu hỏi mở
    opened = {}
    for name, _, root, lay in sheets:
        if lay:
            opened[name] = mark_open_rows(root, sst, st)

    # khối tổng kết
    fixed = {}
    if a.fix_summary:
        for name, _, root, lay in sheets:
            if lay:
                k = fix_summary_ranges(root, lay, lay.data_start, lay.data_end)
                if k:
                    fixed[name] = k

    if a.change:
        cover = next((root for _, _, root, _ in sheets
                      if root.find(q("sheetData")) is not None and Sheet(root, sst).find_text("Effective Date")), None)
        if cover is None:
            raise SystemExit("Không tìm thấy bảng Record of change")
        for line in a.change:
            r = add_change(cover, sst, line.split("|"), st)
            print(f"Trang bìa: thêm dòng Record of change ở hàng {r}")

    # 6. chữ định dạng từng đoạn — làm sau cùng, khi kiểu của mọi ô đã chốt
    n_runs = normalize_runs([root for _, _, root, _ in sheets if root.find(q("sheetData")) is not None], sst, st)

    for _, path, root, _ in sheets:
        pkg.put(path, root)
    sst.finish()
    pkg.put(sst_name, sst_root)
    pkg.put(st_name, st_root)
    pkg.save(Path(a.out))

    print(f"{len(sheets)} sheet → {a.out} · phông {FONT} {SIZE} · nền tiêu đề {HEAD_FILL}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if n_cf:
        print(f"  quy tắc định dạng có điều kiện đã bỏ: {n_cf}")
    if n_copy:
        print(f"  ô được chép kiểu: {n_copy}")
    if n_ren:
        print(f"  ô tiêu đề đổi tên: {n_ren}")
    if n_runs:
        print(f"  đoạn chữ định dạng riêng đã sửa: {n_runs}")
    for name, (n_open, n_changed) in opened.items():
        print(f"  {name}: {n_open} dòng còn câu hỏi mở · {n_changed} ô đổi trạng thái tô")
    for name, k in fixed.items():
        print(f"  {name}: {k} công thức tổng kết được sửa vùng đếm")
    print("Chạy tc_check.py trước khi bàn giao.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
