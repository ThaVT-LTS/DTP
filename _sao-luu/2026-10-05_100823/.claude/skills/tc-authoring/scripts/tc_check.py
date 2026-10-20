#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra file test case trước khi bàn giao.

    python tc_check.py TestCase.xlsx [--uc uc_list.txt] [--sheets Login,Scopes] [--lang en]

Báo lỗi (mã thoát 1):
  - TC thiếu UC_ID, hoặc TVP_ID trùng, hoặc thiếu Expected mà không khai ở cột Open question
  - Priority / Result không thuộc danh sách hợp lệ
  - Kết quả mong đợi mơ hồ ("hoạt động bình thường", "hiển thị đúng", "thành công", "works normally", "as expected"…)
  - Khu vực (Classification II) có nhóm Thành công / Success mà thiếu nhóm Không thành công / Failure
  - UC trong danh sách mà chưa có TC nào (khi truyền --uc)
  - Ô có nội dung sai phông / cỡ chữ, hoặc dùng màu nền / màu chữ ngoài bảng màu (mọi sheet)
  - Ô chữ của bảng TC (Classification B–E, Name, Pre-condition, Step, Expected, Open question) không xuống dòng,
    không căn giữa theo chiều dọc hoặc không căn trái (rule 19)
  - Ô Open question có chữ mà không tô màu, hoặc tô màu mà không còn câu hỏi (rule 13, 23)
Cảnh báo: ô Open question có phần không phải câu hỏi (không có dấu "?") (rule 23);
  dòng còn ký tự ngoài bảng chữ Latin (không tính dấu câu như · — ←) mà không khai ở cột Open question;
  với --lang en: ô còn chữ tiếng Việt, trừ cột Open question và sheet Cần xác nhận.
"""
from __future__ import annotations
import argparse, re, sys, unicodedata
from pathlib import Path
import openpyxl

DATA_ROW = 13
C_NO, C_I, C_II, C_III, C_IV = 1, 2, 3, 4, 5
C_PRI, C_TVP, C_NAME, C_PRE, C_STEP, C_EXP = 6, 7, 8, 9, 10, 11
C_R1, C_R2, C_WAIT, C_UC = 13, 18, 23, 24

PRI_OK = {"High", "Medium", "Low"}
RES_OK = {"Passed", "Failed", "Pending", "Blocked", "NA", "Not execute"}
VAGUE = ["hoạt động bình thường", "hiển thị đúng", "thành công", "bình thường",
         "đúng như mong đợi", "ok", "chính xác",
         "works normally", "works correctly", "work correctly", "works as expected", "as expected",
         "displays correctly", "displayed correctly", "display correctly",
         "successfully", "success", "correctly", "properly", "normally"]
NON_LATIN = re.compile(r"[^\x00-\x7FÀ-ỹ\s·—–…‹›←→↑↓“”‘’•×]")   # dấu câu thường gặp không tính
VI_CHARS = re.compile(r"[ăâđêôơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]", re.I)
SYS_SHEETS = {"Cover", "Hướng dẫn", "_Patterns", "_Nav",
              "_Effects", "Test_Report", "Đối chiếu nhãn", "Cần xác nhận", "Phân quyền"}
Q_SHEET = "Cần xác nhận"   # sheet câu hỏi: viết theo ngôn ngữ câu hỏi, --lang en không kiểm


FONT, SIZE = "Times New Roman", 10
PALETTE_FILL = {"00B0F0", "FBE9E7"}                    # references/format.md §4, theo file TC mẫu
PALETTE_FONT = {"363A45", "B8362B", "000000"}


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


ALIGN_COLS = (C_I, C_II, C_III, C_IV, C_NAME, C_PRE, C_STEP, C_EXP, C_WAIT)
OPEN_FILL = "FBE9E7"


def check_align(ws, errors):
    """rule 19: ô chữ của bảng TC xuống dòng, căn giữa dọc, căn trái (ô trống của cụm gộp cũng tính)."""
    last = max((r for r in range(DATA_ROW, ws.max_row + 1) if ws.cell(r, C_TVP).value), default=0)
    inner = set()    # ô nằm trong cụm gộp mà không phải ô neo: Excel lấy căn lề của ô neo
    for m in ws.merged_cells.ranges:
        for row in ws.iter_rows(min_row=m.min_row, max_row=m.max_row, min_col=m.min_col, max_col=m.max_col):
            for c in row:
                if (c.row, c.column) != (m.min_row, m.min_col):
                    inner.add((c.row, c.column))
    bad = []
    for r in range(DATA_ROW, last + 1):
        for col in ALIGN_COLS:
            c = ws.cell(r, col)
            if (r, col) in inner or (col == C_WAIT and not c.value):
                continue
            a = c.alignment
            if not (a.wrap_text and a.vertical == "center" and a.horizontal == "left"):
                bad.append(c.coordinate)
    if bad:
        more = f" … (+{len(bad) - 5})" if len(bad) > 5 else ""
        errors.append(f"{ws.title} · {len(bad)} ô chưa xuống dòng / căn giữa dọc / căn trái: {', '.join(bad[:5])}{more}")


def check_open_question(ws, r, tvp, where, errors, warns):
    """rule 13, 23: câu hỏi đã có trả lời thì xoá và bỏ tô; mỗi phần của ô là một câu hỏi thật."""
    c = ws.cell(r, C_WAIT)
    text = str(c.value or "").strip()
    filled = c.fill is not None and c.fill.fill_type and _rgb(c.fill.fgColor) == OPEN_FILL
    if text and not filled:
        errors.append(f"{where} · {tvp} còn câu hỏi ở Open question mà ô không tô màu")
    if filled and not text:
        errors.append(f"{where} · {tvp} đã hết câu hỏi mà ô Open question vẫn tô màu")
    if text:
        parts = [p.strip() for p in re.split(r"→\s*Q-[\w-]+(?:[,;]\s*Q-[\w-]+)*\s*[;,]?", text) if p.strip()]
        if not any("?" in p for p in parts) or any("?" not in p for p in parts):
            warns.append(f"{where} · {tvp} Open question có phần không phải câu hỏi (thiếu dấu ?): {text[:60]}")


OPEN_SCREEN = re.compile(r"(?i)(\bmở\s+(màn|trang)|\bvào\s+(màn|trang)|\bopen(ed)?\s+(the\s+)?[\w ]{0,30}screen|\bgo\s+to\b)")


def check_sheet(ws, errors, warns):
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
        check_open_question(ws, r, tvp, where, errors, warns)
        pre = str(ws.cell(r, C_PRE).value or "")
        if OPEN_SCREEN.search(pre):
            warns.append(f"{where} · {tvp} Pre-condition ghi mở màn hình; việc mở màn đang test là Step 1 (rule 14)")
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
        if re.search(r"\bsuccess", joined) and not re.search(r"\bfailure", joined):
            errors.append(f"{ws.title} · khu vực '{area}' có nhóm Success nhưng thiếu Failure")
    return ucs


def check_lang_en(ws, warns):
    """--lang en: ô còn chữ tiếng Việt, trừ cột Open question của sheet TC và sheet câu hỏi."""
    if ws.title == Q_SHEET:
        return
    tc_sheet = ws.title not in SYS_SHEETS
    cells = []
    for row in ws.iter_rows():
        for c in row:
            if not isinstance(c.value, str) or (tc_sheet and c.column == C_WAIT):
                continue
            if VI_CHARS.search(unicodedata.normalize("NFC", c.value)):
                cells.append(c.coordinate)
    if cells:
        more = f" … (+{len(cells) - 5})" if len(cells) > 5 else ""
        warns.append(f"{ws.title} · {len(cells)} ô còn chữ tiếng Việt: {', '.join(cells[:5])}{more}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Kiểm tra file test case.")
    ap.add_argument("xlsx")
    ap.add_argument("--uc", help="file danh sách UC, mỗi dòng một mã")
    ap.add_argument("--sheets", help="chỉ kiểm các sheet này, phân tách bằng dấu phẩy")
    ap.add_argument("--lang", choices=["en"], help="en: file TC viết tiếng Anh, cảnh báo ô còn chữ tiếng Việt")
    a = ap.parse_args()

    wb = openpyxl.load_workbook(Path(a.xlsx), data_only=True)
    only = set(a.sheets.split(",")) if a.sheets else None

    errors, warns, ucs = [], [], set()
    n = 0
    for ws in wb.worksheets:
        if not only or ws.title in only:
            check_format(ws, errors)
            if a.lang == "en":
                check_lang_en(ws, warns)
        if ws.title in SYS_SHEETS:
            continue
        if only and ws.title not in only:
            continue
        n += 1
        check_align(ws, errors)
        ucs |= check_sheet(ws, errors, warns)

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
