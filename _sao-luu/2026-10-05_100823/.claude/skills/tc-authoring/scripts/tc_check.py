#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra file test case trước khi bàn giao.

    python tc_check.py TestCase.xlsx [--uc uc_list.txt] [--sheets Login,Scopes]

Báo lỗi (mã thoát 1):
  - TC thiếu UC_ID, hoặc TVP_ID trùng, hoặc thiếu Expected mà không khai ở cột Open question
  - Priority / Result không thuộc danh sách hợp lệ
  - Kết quả mong đợi mơ hồ ("hoạt động bình thường", "hiển thị đúng", "thành công"…)
  - Khoá {{...}} không có trong sheet _Data hoặc _Labels
  - Khu vực (Classification II) có thao tác ghi dữ liệu mà thiếu nhóm Không thành công
  - UC trong danh sách mà chưa có TC nào (khi truyền --uc)
  - Ô có nội dung sai phông / cỡ chữ, hoặc dùng màu nền / màu chữ ngoài bảng màu (mọi sheet)
Cảnh báo: dòng còn ký tự ngoài bảng chữ Latin mà không khai ở cột Open question.
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
import openpyxl

DATA_ROW = 13
C_NO, C_I, C_II, C_III, C_IV = 1, 2, 3, 4, 5
C_PRI, C_TVP, C_NAME, C_PRE, C_STEP, C_EXP = 6, 7, 8, 9, 10, 11
C_R1, C_R2, C_WAIT, C_UC = 13, 18, 23, 24

PRI_OK = {"High", "Medium", "Low"}
RES_OK = {"Passed", "Failed", "Pending", "Blocked", "NA", "Not execute"}
VAGUE = ["hoạt động bình thường", "hiển thị đúng", "thành công", "bình thường",
         "đúng như mong đợi", "ok", "chính xác"]
NON_LATIN = re.compile(r"[^\x00-\x7FÀ-ỹ\s]")
KEY = re.compile(r"\{\{[^}]+\}\}")
SYS_SHEETS = {"Cover", "Hướng dẫn", "_Data", "_Labels", "_Patterns", "_Nav",
              "_Effects", "Test_Report", "Đối chiếu nhãn", "Cần xác nhận"}


FONT, SIZE = "Times New Roman", 10
PALETTE_FILL = {"17324D", "EAE7E1", "FBE9E7"}          # references/format.md §4
PALETTE_FONT = {"FFFFFF", "B8362B", "000000"}


def _rgb(color):
    """Trả mã RGB 6 ký tự, hoặc None khi là màu mặc định / theme."""
    if color is None or getattr(color, "type", None) != "rgb":
        return None
    v = color.rgb
    if not isinstance(v, str) or v in ("00000000",):
        return None
    return v[-6:].upper()


def check_format(ws, errors):
    """Mọi ô có nội dung: đúng phông, đúng cỡ, màu thuộc bảng màu. Gộp lỗi theo sheet."""
    bad = {"phông": [], "cỡ chữ": [], "màu nền": [], "màu chữ": []}
    for row in ws.iter_rows():
        for c in row:
            if c.value is None or str(c.value).strip() == "":
                continue
            f = c.font
            if (f.name or "") != FONT:
                bad["phông"].append(f"{c.coordinate}={f.name}")
            if f.size is not None and float(f.size) != SIZE:
                bad["cỡ chữ"].append(f"{c.coordinate}={f.size:g}")
            fc = _rgb(f.color)
            if fc and fc not in PALETTE_FONT:
                bad["màu chữ"].append(f"{c.coordinate}={fc}")
            if c.fill is not None and c.fill.fill_type:
                bg = _rgb(c.fill.fgColor)
                if bg and bg not in PALETTE_FILL:
                    bad["màu nền"].append(f"{c.coordinate}={bg}")
    for kind, cells in bad.items():
        if cells:
            more = f" … (+{len(cells) - 5})" if len(cells) > 5 else ""
            errors.append(f"{ws.title} · {len(cells)} ô sai {kind}: {', '.join(cells[:5])}{more}")


def collect_keys(wb) -> set[str]:
    keys = set()
    for name in ("_Data", "_Labels"):
        if name in wb.sheetnames:
            for row in wb[name].iter_rows(values_only=True):
                for v in row:
                    if isinstance(v, str):
                        keys.update(KEY.findall(v))
    return keys


def check_sheet(ws, keys, errors, warns):
    seen, ucs = set(), set()
    cur_ii = None
    areas = {}
    for r in range(DATA_ROW, ws.max_row + 1):
        tvp = ws.cell(r, C_TVP).value
        if not tvp:
            continue
        where = f"{ws.title}!{r}"
        if tvp in seen:
            errors.append(f"{where} · TVP_ID trùng: {tvp}")
        seen.add(tvp)

        if ws.cell(r, C_II).value:
            cur_ii = ws.cell(r, C_II).value
        areas.setdefault(cur_ii, set()).add(str(ws.cell(r, C_III).value or ""))

        uc = ws.cell(r, C_UC).value
        if not uc:
            errors.append(f"{where} · {tvp} thiếu UC")
        else:
            ucs.add(str(uc).strip())

        pri = ws.cell(r, C_PRI).value
        if pri and pri not in PRI_OK:
            errors.append(f"{where} · Priority không hợp lệ: {pri}")
        for col, lbl in ((C_R1, "Round 1"), (C_R2, "Round 2")):
            v = ws.cell(r, col).value
            if v and v not in RES_OK:
                errors.append(f"{where} · {lbl} Result không hợp lệ: {v}")

        exp = (ws.cell(r, C_EXP).value or "").strip()
        wait = (ws.cell(r, C_WAIT).value or "").strip()
        if not exp and not wait:
            errors.append(f"{where} · {tvp} không có Expected và cũng không khai Open question")
        if exp:
            low = exp.lower()
            for w in VAGUE:
                if re.search(r"(^|[\s\-•])" + re.escape(w) + r"\s*$", low):
                    errors.append(f"{where} · {tvp} kết quả mong đợi mơ hồ: '{w}'")
                    break
        for cell in (C_PRE, C_STEP, C_EXP):
            txt = ws.cell(r, cell).value
            if isinstance(txt, str):
                for k in KEY.findall(txt):
                    if keys and k not in keys:
                        errors.append(f"{where} · khoá {k} chưa khai trong _Data/_Labels")
        if not wait:
            joined = " ".join(str(ws.cell(r, c).value or "") for c in (C_NAME, C_PRE, C_STEP, C_EXP))
            if NON_LATIN.search(joined):
                warns.append(f"{where} · {tvp} còn ký tự ngoài bảng chữ Latin mà không khai Open question")

    for area, lv3 in areas.items():
        if not area:
            continue
        joined = " ".join(lv3).lower()
        if "thành công" in joined and "không thành công" not in joined:
            errors.append(f"{ws.title} · khu vực '{area}' có nhóm Thành công nhưng thiếu Không thành công")
    return ucs


def main() -> int:
    ap = argparse.ArgumentParser(description="Kiểm tra file test case.")
    ap.add_argument("xlsx")
    ap.add_argument("--uc", help="file danh sách UC, mỗi dòng một mã")
    ap.add_argument("--sheets", help="chỉ kiểm các sheet này, phân tách bằng dấu phẩy")
    a = ap.parse_args()

    wb = openpyxl.load_workbook(Path(a.xlsx), data_only=True)
    keys = collect_keys(wb)
    only = set(a.sheets.split(",")) if a.sheets else None

    errors, warns, ucs = [], [], set()
    n = 0
    for ws in wb.worksheets:
        if not only or ws.title in only:
            check_format(ws, errors)
        if ws.title in SYS_SHEETS:
            continue
        if only and ws.title not in only:
            continue
        n += 1
        ucs |= check_sheet(ws, keys, errors, warns)

    if a.uc:
        want = {l.strip() for l in Path(a.uc).read_text(encoding="utf-8").splitlines() if l.strip()}
        for u in sorted(want - ucs):
            errors.append(f"UC chưa có TC nào: {u}")

    print(f"{n} sheet · {len(ucs)} UC được phủ · {len(errors)} lỗi · {len(warns)} cảnh báo")
    for e in errors:
        print("LỖI: " + e)
    for w in warns:
        print("Cảnh báo: " + w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
