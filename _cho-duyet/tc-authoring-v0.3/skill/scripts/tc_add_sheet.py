#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thêm một sheet test case vào FILE MẪU của dự án, nhân bản định dạng của một sheet TC đã có.

Làm thẳng trên XML của file .xlsx nên mọi thứ khác được giữ nguyên: logo, dropdown
(data validation x14), theme, các sheet khác. Không dùng openpyxl để lưu file mẫu:
openpyxl làm rơi ảnh và phần mở rộng x14 (dropdown Priority/Result). Cần thư viện lxml.

    python tc_add_sheet.py --book SGS-DTP_TestCase.xlsx --like Login --sheet Scopes \\
        --data scopes.tsv --function "SCP-L0001_Quản lý scope" \\
        --screen "Scopes · Customer Portal" --creator "<tên>" --created 01/10/2026 \\
        --source "Figma … · prototype …" --report Test_Report \\
        --change "01/10/2026|1.0|Login, Scopes|A|Tạo mới|UC List v2.1" --out out.xlsx

Dữ liệu TSV giống tc_build_xlsx.py: I, II, III, IV, Pri, Name, Pre, Step, Expected, UC, Wait.
Cột cha lặp ở mọi dòng; script gộp ô bốn cột Classification theo rule 20 của rules/tc-authoring.md.

Định dạng lấy từ sheet mẫu (--like), không đặt cứng trong script:
  - khối thông tin, khối tổng kết vòng test, hai hàng tiêu đề: chép nguyên, chỉ thay giá trị;
  - ô dữ liệu: style của cột tương ứng trong sheet mẫu; ô Classification phân biệt ô giữa cụm
    gộp (không viền dưới) và ô cuối cụm (có viền dưới) đúng như sheet mẫu;
  - độ rộng cột, cài đặt trang, dropdown: chép từ sheet mẫu, chỉ nới vùng áp dụng;
  - công thức của khối tổng kết: chép từ sheet mẫu, vùng đếm đặt lại đúng vùng dữ liệu của sheet mới;
  - dòng còn câu hỏi mở: tô ô Open question (và ô Expected result nếu trống) theo tc_palette.py.

File mẫu phải đã đúng một phông, một bảng màu (chạy tc_restyle.py một lần cho file mẫu).
"""
from __future__ import annotations

import argparse
import copy
import csv
import re
import sys
import uuid
import zipfile
from collections import Counter
from pathlib import Path

from lxml import etree

from tc_palette import OPEN_FILL, OPEN_FONT, TEXT

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
RNS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PNS = "http://schemas.openxmlformats.org/package/2006/relationships"
CTNS = "http://schemas.openxmlformats.org/package/2006/content-types"
X14 = "http://schemas.microsoft.com/office/spreadsheetml/2009/9/main"
XM = "http://schemas.microsoft.com/office/excel/2006/main"
XR = "http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
WS_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"
WS_CT = "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"

INFO_LABELS = {"function name": "function", "screen name": "screen", "creator": "creator",
               "created date": "created", "reference": "source"}


def q(tag: str) -> str:
    return f"{{{NS}}}{tag}"


def col_letter(n: int) -> str:
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def col_index(s: str) -> int:
    n = 0
    for ch in s:
        n = n * 26 + ord(ch) - 64
    return n


def split_ref(ref: str) -> tuple[int, int]:
    m = re.match(r"([A-Z]+)(\d+)$", ref)
    return col_index(m.group(1)), int(m.group(2))


def norm(text) -> str:
    """So khớp nhãn tiêu đề: bỏ xuống dòng, khoảng trắng thừa, không phân biệt hoa thường."""
    return " ".join(str(text).split()).lower()


def guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def to_bytes(root) -> bytes:
    return (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            + etree.tostring(root, encoding="UTF-8"))


# ----------------------------------------------------------------------------- gói xlsx
class Package:
    def __init__(self, path: Path):
        with zipfile.ZipFile(path) as z:
            self.names = z.namelist()
            self.data = {n: z.read(n) for n in self.names}

    def xml(self, name):
        return etree.fromstring(self.data[name])

    def put(self, name, root_or_bytes, after: str | None = None):
        b = root_or_bytes if isinstance(root_or_bytes, bytes) else to_bytes(root_or_bytes)
        if name not in self.data:
            idx = self.names.index(after) + 1 if after in self.names else len(self.names)
            self.names.insert(idx, name)
        self.data[name] = b

    def save(self, path: Path):
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for n in self.names:
                z.writestr(n, self.data[n])


class SharedStrings:
    def __init__(self, root):
        self.root = root
        self.items = root.findall(q("si"))
        self.index: dict[str, int] = {}
        for i, si in enumerate(self.items):
            self.index.setdefault(self.text(i), i)
        self.new_refs = 0

    def text(self, i: int) -> str:
        return "".join(t.text or "" for t in self.items[i].iter(q("t")))

    def get(self, text: str) -> int:
        self.new_refs += 1
        if text in self.index:
            return self.index[text]
        si = etree.SubElement(self.root, q("si"))
        t = etree.SubElement(si, q("t"))
        t.text = text
        if text != text.strip() or "\n" in text or "  " in text:
            t.set(XML_SPACE, "preserve")
        self.items.append(si)
        self.index[text] = len(self.items) - 1
        return self.index[text]

    def clone(self, i: int) -> int:
        """Bản sao của chuỗi `i` (giữ nguyên định dạng từng đoạn) — dùng khi hai ô cần cùng chữ nhưng khác định dạng."""
        si = copy.deepcopy(self.items[i])
        self.root.append(si)
        self.items.append(si)
        return len(self.items) - 1

    def finish(self):
        self.root.set("uniqueCount", str(len(self.items)))
        self.root.set("count", str(int(self.root.get("count", len(self.items))) + self.new_refs))


# ----------------------------------------------------------------------------- đọc sheet
class Sheet:
    """Đọc nhanh một worksheet: giá trị ô (đã giải shared string), style, gộp ô."""

    def __init__(self, root, sst: SharedStrings):
        self.root = root
        self.sst = sst
        sd = root.find(q("sheetData"))                       # sheet biểu đồ không có sheetData
        self.rows = {int(r.get("r")): r for r in sd.findall(q("row"))} if sd is not None else {}
        self.cells: dict[tuple[int, int], etree._Element] = {}
        for rn, row in self.rows.items():
            for c in row.findall(q("c")):
                self.cells[split_ref(c.get("r"))] = c
        mc = root.find(q("mergeCells"))
        self.merges = [self._rng(m.get("ref")) for m in mc.findall(q("mergeCell"))] if mc is not None else []

    @staticmethod
    def _rng(ref):
        a, b = ref.split(":")
        (c1, r1), (c2, r2) = split_ref(a), split_ref(b)
        return c1, r1, c2, r2

    def value(self, col, row):
        c = self.cells.get((col, row))
        if c is None:
            return None
        t = c.get("t")
        if t == "s":
            v = c.find(q("v"))
            return self.sst.text(int(v.text)) if v is not None else None
        if t == "inlineStr":
            return "".join(x.text or "" for x in c.iter(q("t")))
        v = c.find(q("v"))
        return v.text if v is not None else None

    def style(self, col, row):
        c = self.cells.get((col, row))
        return c.get("s") if c is not None else None

    def merged_value(self, col, row):
        """Giá trị nhìn thấy ở (col,row): nếu nằm trong vùng gộp thì lấy ô neo."""
        for c1, r1, c2, r2 in self.merges:
            if c1 <= col <= c2 and r1 <= row <= r2:
                return self.value(c1, r1)
        return self.value(col, row)

    def find_text(self, text, rows=None):
        text = norm(text)
        for (c, r) in sorted(self.cells):
            if rows and r not in rows:
                continue
            v = self.value(c, r)
            if isinstance(v, str) and norm(v) == text:
                return c, r
        return None


class TcLayout:
    """Bố cục một sheet TC theo mẫu FEEC: khối thông tin, khối tổng kết, 2 hàng tiêu đề, vùng dữ liệu."""

    def __init__(self, sh: Sheet):
        hit = sh.find_text("No.")
        if not hit:
            raise SystemExit("Sheet mẫu không có ô tiêu đề 'No.'")
        self.col_no, self.hdr2 = hit
        self.hdr1 = self.hdr2 - 1
        self.data_start = self.hdr2 + 1
        cols = {}
        for c in range(1, 60):
            for r in (self.hdr1, self.hdr2):
                v = sh.value(c, r)
                if isinstance(v, str) and v.strip():
                    key = norm(v)
                    if key == "result":
                        cols.setdefault("result1" if "result1" not in cols else "result2", c)
                    else:
                        cols.setdefault(key, c)
        need = ["i", "ii", "iii", "iv", "priority", "tvp_id", "test case name/ test view point",
                "pre-condition", "step", "expected result", "result1"]
        miss = [k for k in need if k not in cols]
        if miss:
            raise SystemExit("Sheet mẫu thiếu cột: " + ", ".join(miss))
        self.cols = cols
        self.cls = [cols["i"], cols["ii"], cols["iii"], cols["iv"]]
        self.c_wait = cols.get("open question") or cols.get("chờ text")   # tên cũ: Chờ text
        self.c_uc = cols.get("uc")
        self.last_col = max(cols.values())
        self.info = {}
        for (c, r) in sorted(sh.cells):
            if r >= self.hdr1:
                continue
            v = sh.value(c, r)
            if isinstance(v, str) and norm(v) in INFO_LABELS:
                self.info[INFO_LABELS[norm(v)]] = (c + 1, r)
        tvp = cols["tvp_id"]
        rows = [r for r in sh.rows if r >= self.data_start and sh.value(tvp, r)]
        self.data_end = max(rows) if rows else self.data_start


# ----------------------------------------------------------------------------- styles.xml
KEEP = object()


def _sig(el):
    """Chữ ký của một phần tử XML (tên, thuộc tính, con) để biết hai định nghĩa có trùng nhau không."""
    return (etree.QName(el).localname, tuple(sorted(el.attrib.items())), tuple(_sig(c) for c in el))


def rgb_of(color_el):
    """Mã RGB 6 ký tự của một phần tử màu; None khi không phải mã RGB (theme, indexed, tự động)."""
    if color_el is None:
        return None
    v = color_el.get("rgb")
    return v[-6:].upper() if v else None


def set_font_color(font, rgb: str):
    for c in font.findall(q("color")):
        font.remove(c)
    col = etree.Element(q("color"))
    col.set("rgb", "FF" + rgb)
    name = font.find(q("name"))
    if name is not None:
        name.addprevious(col)
    else:
        font.append(col)


class Styles:
    """styles.xml — tìm hoặc tạo biến thể của một kiểu ô (đổi nền, đổi màu chữ), không đụng kiểu gốc."""

    def __init__(self, root):
        self.root = root
        self.fonts = root.find(q("fonts"))
        self.fills = root.find(q("fills"))
        self.xfs = root.find(q("cellXfs"))
        self.changed = False
        self._cache: dict[tuple, str] = {}

    def add(self, parent, el) -> int:
        sig = _sig(el)
        for i, e in enumerate(parent):
            if _sig(e) == sig:
                return i
        parent.append(el)
        parent.set("count", str(len(parent)))
        self.changed = True
        return len(parent) - 1

    def fill_id(self, rgb) -> int:
        """Chỉ số của nền đặc màu `rgb`; None nghĩa là không nền."""
        if rgb is None:
            return 0
        f = etree.Element(q("fill"))
        pf = etree.SubElement(f, q("patternFill"))
        pf.set("patternType", "solid")
        etree.SubElement(pf, q("fgColor")).set("rgb", "FF" + rgb)
        etree.SubElement(pf, q("bgColor")).set("rgb", "FF" + rgb)
        return self.add(self.fills, f)

    def fill_rgb(self, s):
        xf = self.xfs[int(s)]
        pf = self.fills[int(xf.get("fillId", "0"))].find(q("patternFill"))
        if pf is None or pf.get("patternType") != "solid":
            return None
        return rgb_of(pf.find(q("fgColor")))

    def is_open(self, s) -> bool:
        return self.fill_rgb(s) == OPEN_FILL

    def font_rgb(self, s):
        """Màu chữ (mã RGB) của kiểu ô `s`; None khi kiểu đó không đặt màu RGB."""
        return rgb_of(self.fonts[int(self.xfs[int(s)].get("fontId", "0"))].find(q("color")))

    def variant(self, s, fill=KEEP, font_rgb=KEEP) -> str:
        """Chỉ số kiểu ô giống kiểu `s` nhưng đổi nền và/hoặc màu chữ. Trùng kiểu đã có thì dùng lại."""
        key = (str(s), "keep" if fill is KEEP else fill, "keep" if font_rgb is KEEP else font_rgb)
        if key not in self._cache:
            xf = copy.deepcopy(self.xfs[int(s)])
            if fill is not KEEP:
                xf.set("fillId", str(self.fill_id(fill)))
                xf.set("applyFill", "1")
            if font_rgb is not KEEP:
                font = copy.deepcopy(self.fonts[int(xf.get("fontId", "0"))])
                set_font_color(font, font_rgb)
                xf.set("fontId", str(self.add(self.fonts, font)))
                xf.set("applyFont", "1")
            self._cache[key] = str(self.add(self.xfs, xf))
        return self._cache[key]

    def like(self, s, ref) -> str:
        """Chỉ số kiểu ô giống kiểu `s` (giữ viền, nền, phông) nhưng căn lề và định dạng số theo kiểu `ref`."""
        key = ("like", str(s), str(ref))
        if key not in self._cache:
            xf = copy.deepcopy(self.xfs[int(s)])
            rf = self.xfs[int(ref)]
            for al in xf.findall(q("alignment")):
                xf.remove(al)
            al = rf.find(q("alignment"))
            if al is not None:
                xf.insert(0, copy.deepcopy(al))
                xf.set("applyAlignment", "1")
            else:
                xf.attrib.pop("applyAlignment", None)
            xf.set("numFmtId", rf.get("numFmtId", "0"))
            self._cache[key] = str(self.add(self.xfs, xf))
        return self._cache[key]


def mark_open_rows(sheet_root, sst, styles: Styles) -> tuple[int, int]:
    """Tô ô Open question (và ô Expected result nếu trống) ở dòng còn câu hỏi mở;
    bỏ tô ở dòng đã hết câu hỏi. Trả về (số dòng còn câu hỏi mở, số ô đổi kiểu)."""
    sh = Sheet(sheet_root, sst)
    lay = TcLayout(sh)
    if not lay.c_wait:
        return 0, 0
    c_exp = lay.cols["expected result"]
    n_open = n_changed = 0
    for r in range(lay.data_start, lay.data_end + 1):
        if not sh.value(lay.cols["tvp_id"], r):
            continue
        wait = (sh.value(lay.c_wait, r) or "").strip()
        exp = (sh.value(c_exp, r) or "").strip()
        n_open += bool(wait)
        for c, on, font in ((lay.c_wait, bool(wait), OPEN_FONT), (c_exp, bool(wait) and not exp, KEEP)):
            cel = sh.cells.get((c, r))
            if cel is None:
                continue
            s = cel.get("s", "0")
            if on:
                new = styles.variant(s, fill=OPEN_FILL, font_rgb=font)
            elif styles.is_open(s):
                new = styles.variant(s, fill=None, font_rgb=TEXT)
            else:
                new = s
            if new != s:
                cel.set("s", new)
                n_changed += 1
    return n_open, n_changed


# ----------------------------------------------------------------------------- khối tổng kết
RANGE = re.compile(r"(\$?)([A-Z]{1,3})(\$?)(\d+):(\$?)([A-Z]{1,3})(\$?)(\d+)")


def fix_summary_ranges(sheet_root, lay: TcLayout, first: int, last: int, exact: bool = False) -> int:
    """Khối tổng kết phía trên bảng: mọi vùng đếm trên cột TVP_ID / Result phải bắt đầu ở dòng dữ liệu đầu
    và phủ tới dòng dữ liệu cuối.
      exact=True   sheet mới dựng: đặt đúng vùng dữ liệu `first`–`last`;
      exact=False  sheet có sẵn: chỉ kéo dòng đầu về `first`, và nới dòng cuối khi nó chưa tới `last`.
    Sheet có công thức bị sửa thì xoá giá trị đã lưu của mọi công thức trong khối, để bảng tính tính lại khi mở.
    Trả về số công thức đã sửa."""
    C = lay.cols
    data_cols = {col_letter(C["tvp_id"]), col_letter(C["result1"])}
    if "result2" in C:
        data_cols.add(col_letter(C["result2"]))

    def rep(m):
        d1, c1, d2, r1, d3, c2, d4, r2 = m.groups()
        if c1 != c2 or c1 not in data_cols or int(r1) <= lay.hdr2:
            return m.group(0)
        if exact:
            return f"${c1}${first}:${c2}${last}"
        return f"{d1}{c1}{d2}{first}:{d3}{c2}{d4}{max(int(r2), last)}"

    cells = [cel for row in sheet_root.find(q("sheetData")).findall(q("row")) if int(row.get("r")) < lay.hdr1
             for cel in row.findall(q("c")) if cel.find(q("f")) is not None]
    n = 0
    for cel in cells:
        f = cel.find(q("f"))
        new = RANGE.sub(rep, f.text) if f.text else f.text
        if new != f.text:
            f.text = new
            n += 1
    if n or exact:
        for cel in cells:
            v = cel.find(q("v"))
            if v is not None:
                cel.remove(v)
            if cel.get("t") in ("e", "str", "n", "b"):
                del cel.attrib["t"]
    return n


# ----------------------------------------------------------------------------- dữ liệu
def read_tsv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for r in rows:
        for k, v in list(r.items()):
            r[k] = (v or "").replace("\\n", "\n").strip()
    return rows


def uc_label(uc: str) -> str:
    if not uc or uc.startswith("UC-") or uc.startswith("["):
        return uc
    return "UC-" + uc


def class_runs(rows: list[dict]) -> dict[int, list[tuple[int, int]]]:
    """Cụm dòng liền nhau cùng giá trị cho 4 cấp, cụm con không vượt cụm cha. Trả về chỉ số dòng 0-based."""
    keys = ["I", "II", "III", "IV"]
    out = {}
    parent = [(0, len(rows) - 1)]
    for level, k in enumerate(keys):
        runs = []
        for a, b in parent:
            s = a
            for i in range(a + 1, b + 2):
                if i == b + 1 or rows[i][k] != rows[s][k]:
                    runs.append((s, i - 1))
                    s = i
        out[level] = runs
        parent = runs
    return out


def est_height(texts: dict[int, str], widths: dict[int, float], min_h: float) -> float:
    lines = 1
    for c, t in texts.items():
        if not t:
            continue
        per = max(1, int(widths.get(c, 10) * 1.15))
        n = sum(max(1, -(-len(seg) // per)) for seg in t.split("\n"))
        lines = max(lines, n)
    return max(min_h, round(13.5 * lines + 6, 2))


def col_widths(root) -> dict[int, float]:
    out = {}
    cols = root.find(q("cols"))
    if cols is None:
        return out
    for c in cols.findall(q("col")):
        for i in range(int(c.get("min")), min(int(c.get("max")), 200) + 1):
            out[i] = float(c.get("width", 9))
    return out


# ----------------------------------------------------------------------------- dựng sheet mới
def build_sheet(tpl_root, sst: SharedStrings, rows: list[dict], meta: dict, book: Styles | None = None) -> tuple:
    tpl = Sheet(tpl_root, sst)
    lay = TcLayout(tpl)
    new = copy.deepcopy(tpl_root)
    sd = new.find(q("sheetData"))
    for row in list(sd.findall(q("row"))):
        if int(row.get("r")) >= lay.data_start:
            sd.remove(row)
    first = lay.data_start
    last = first + len(rows) - 1

    # --- style của vùng dữ liệu, lấy từ sheet mẫu
    in_merge = {}
    for c1, r1, c2, r2 in tpl.merges:
        if c1 == c2 and c1 in lay.cls and r1 >= lay.data_start and r2 > r1:
            for r in range(r1, r2 + 1):
                in_merge[(c1, r)] = "last" if r == r2 else "inner"
    styles: dict[tuple[int, str], Counter] = {}
    for r in range(lay.data_start, lay.data_end + 1):
        for c in range(1, lay.last_col + 1):
            s = tpl.style(c, r)
            if s is None:
                continue
            if book is not None and book.is_open(s):         # ô đang tô ở sheet mẫu → lấy kiểu chưa tô
                s = book.variant(s, fill=None, font_rgb=TEXT)
            kind = in_merge.get((c, r), "single") if c in lay.cls else "plain"
            styles.setdefault((c, kind), Counter())[s] += 1

    def style_for(c, kind):
        for k in ([kind] + (["last", "single", "inner"] if kind != "plain" else []) + ["plain"]):
            if (c, k) in styles:
                return styles[(c, k)].most_common(1)[0][0]
        return tpl.style(c, lay.data_start) or "0"

    tail = []  # ô ngoài bảng ở dòng dữ liệu đầu của mẫu (giữ nguyên để giống mẫu)
    trow = tpl.rows.get(lay.data_start)
    if trow is not None:
        for cel in trow.findall(q("c")):
            c, _ = split_ref(cel.get("r"))
            if c > lay.last_col:
                tail.append((c, cel.get("s")))
    row_attrs = {k: v for k, v in (trow.attrib.items() if trow is not None else []) if k not in ("r", "ht", "spans")}
    min_h = float(trow.get("ht", 15)) if trow is not None else 15.0
    widths = col_widths(tpl_root)

    # --- giá trị theo cột
    C = lay.cols
    field_of = {C["priority"]: "Pri", C["test case name/ test view point"]: "Name",
                C["pre-condition"]: "Pre", C["step"]: "Step", C["expected result"]: "Expected"}
    if lay.c_wait:
        field_of[lay.c_wait] = "Wait"
    runs = class_runs(rows)
    run_at = {}  # (level, rowidx) -> (start, end)
    for level, rr in runs.items():
        for a, b in rr:
            for i in range(a, b + 1):
                run_at[(level, i)] = (a, b)

    for i, rec in enumerate(rows):
        r = first + i
        row_el = etree.SubElement(sd, q("row"))
        row_el.set("r", str(r))
        texts = {c: rec.get(f, "") for c, f in field_of.items()}
        for level, key in enumerate(["I", "II", "III", "IV"]):
            a_, b_ = run_at[(level, i)]
            if a_ == b_:                       # ô không gộp thì chữ của nó quyết định chiều cao dòng
                texts[lay.cls[level]] = rec[key]
        for k, v in row_attrs.items():
            row_el.set(k, v)
        row_el.set("ht", str(est_height(texts, widths, min_h)))
        row_el.set("customHeight", "1")
        for c in range(1, lay.last_col + 1):
            val = None
            if c == lay.col_no:
                kind, val = "plain", i + 1
            elif c in lay.cls:
                level = lay.cls.index(c)
                a, b = run_at[(level, i)]
                kind = "single" if a == b else ("last" if i == b else "inner")
                if i == a:
                    val = rec[["I", "II", "III", "IV"][level]] or None
            elif c == C["tvp_id"]:
                kind, val = "plain", "TC_%03d" % (i + 1)
            elif c == lay.c_uc:
                kind, val = "plain", uc_label(rec.get("UC", "")) or None
            elif c in field_of:
                kind, val = "plain", rec.get(field_of[c], "") or None
            else:
                kind = "plain"
            cel = etree.SubElement(row_el, q("c"))
            cel.set("r", f"{col_letter(c)}{r}")
            cel.set("s", style_for(c, kind))
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

    # --- khối thông tin
    for key, (c, r) in lay.info.items():
        val = meta.get(key)
        if val is None:
            continue
        cel = _cell(new, c, r)
        for ch in list(cel):
            cel.remove(ch)
        cel.set("t", "s")
        etree.SubElement(cel, q("v")).text = str(sst.get(val))

    # --- công thức tổng kết: mọi vùng trên cột TVP_ID / Result về đúng vùng dữ liệu mới
    fix_summary_ranges(new, lay, first, last, exact=True)

    # --- gộp ô
    mc = new.find(q("mergeCells"))
    if mc is None:
        mc = etree.SubElement(new, q("mergeCells"))
    for m in list(mc.findall(q("mergeCell"))):
        if Sheet._rng(m.get("ref"))[1] >= lay.data_start:
            mc.remove(m)
    for level, rr in runs.items():
        c = lay.cls[level]
        for a, b in rr:
            if b > a:
                etree.SubElement(mc, q("mergeCell")).set(
                    "ref", f"{col_letter(c)}{first + a}:{col_letter(c)}{first + b}")
    mc.set("count", str(len(mc.findall(q("mergeCell")))))

    # --- khung nhìn: mở ở đầu sheet
    sv = new.find(q("sheetViews"))
    if sv is not None:
        for v in sv.findall(q("sheetView")):
            v.attrib.pop("topLeftCell", None)
            v.set("tabSelected", "1")
            for sel in v.findall(q("selection")):
                sel.set("activeCell", f"A{first}")
                sel.set("sqref", f"A{first}")
    dim = new.find(q("dimension"))
    if dim is not None:
        dim.set("ref", f"A1:{col_letter(max(lay.last_col, max([c for c, _ in tail], default=0)))}{last}")

    # --- dropdown và định dạng có điều kiện: chép từ mẫu, nới vùng dữ liệu, cấp id mới
    def widen(sqref: str) -> str:
        out = []
        for tok in sqref.split():
            m = re.match(r"([A-Z]+)(\d+):([A-Z]+)(\d+)$", tok)
            if m and int(m.group(2)) == lay.data_start:
                end = max(int(m.group(4)), last)
                tok = f"{m.group(1)}{m.group(2)}:{m.group(3)}{end}"
            out.append(tok)
        return " ".join(out)

    for dv in new.iter(f"{{{X14}}}dataValidation"):
        sq = dv.find(f"{{{XM}}}sqref")
        if sq is not None and sq.text:
            sq.text = widen(sq.text)
        if dv.get(f"{{{XR}}}uid"):
            dv.set(f"{{{XR}}}uid", guid())
    for dv in new.iter(q("dataValidation")):
        if dv.get("sqref"):
            dv.set("sqref", widen(dv.get("sqref")))
        if dv.get(f"{{{XR}}}uid"):
            dv.set(f"{{{XR}}}uid", guid())
    for rule in new.iter(f"{{{X14}}}cfRule"):
        if rule.get("id"):
            rule.set("id", guid())
    return new, lay, first, last


def _cell(root, c: int, r: int):
    sd = root.find(q("sheetData"))
    for row in sd.findall(q("row")):
        if int(row.get("r")) == r:
            for cel in row.findall(q("c")):
                if split_ref(cel.get("r")) == (c, r):
                    return cel
            cel = etree.SubElement(row, q("c"))
            cel.set("r", f"{col_letter(c)}{r}")
            _sort_cells(row)
            return cel
    row = etree.SubElement(sd, q("row"))
    row.set("r", str(r))
    cel = etree.SubElement(row, q("c"))
    cel.set("r", f"{col_letter(c)}{r}")
    _sort_rows(sd)
    return cel


def _sort_cells(row):
    cells = sorted(row.findall(q("c")), key=lambda e: split_ref(e.get("r"))[0])
    for e in cells:
        row.remove(e)
        row.append(e)


def _sort_rows(sd):
    rows = sorted(sd.findall(q("row")), key=lambda e: int(e.get("r")))
    for e in rows:
        sd.remove(e)
        sd.append(e)


# ----------------------------------------------------------------------------- Test_Report
def tc_pairs(sh: Sheet) -> list[tuple[str, str, int, int]]:
    """Các cặp (Classification I, II) liền nhau trong một sheet TC, kèm dòng đầu–cuối."""
    lay = TcLayout(sh)
    seq = []
    for r in range(lay.data_start, lay.data_end + 1):
        if not sh.value(lay.cols["tvp_id"], r):
            continue
        seq.append((sh.merged_value(lay.cls[0], r) or "", sh.merged_value(lay.cls[1], r) or "", r))
    out = []
    for i_, ii, r in seq:
        if out and out[-1][0] == i_ and out[-1][1] == ii and out[-1][3] == r - 1:
            out[-1] = (i_, ii, out[-1][2], r)
        else:
            out.append((i_, ii, r, r))
    return out


def rebuild_report(rep_root, sst: SharedStrings, books: list[tuple[str, Sheet]]):
    sh = Sheet(rep_root, sst)
    hit = sh.find_text("Sheet name")
    if not hit:
        raise SystemExit("Sheet báo cáo không có ô 'Sheet name'")
    c_sheet, hdr = hit
    c_i = sh.find_text("Classification I", rows=[hdr])[0]
    c_ii = sh.find_text("Classification II", rows=[hdr])[0]
    starts = [c for c in range(1, 60) if norm(sh.value(c, hdr) or "") == "executed rate"]
    if not starts:
        raise SystemExit("Sheet báo cáo không có cột 'Executed rate'")
    rounds = [(s, s + 1, s + 2, list(range(s + 3, s + 9))) for s in starts]  # rate, executed, total, 6 trạng thái
    first = hdr + 1
    rows_old = sorted(r for r in sh.rows if r > hdr)
    block_total = next(r for r in rows_old if norm(sh.value(c_i, r) or "") == "total")
    grand = next(r for r in rows_old if norm(sh.value(c_sheet, r) or "") == "total")
    filler_r = grand + 1 if grand + 1 in sh.rows else None
    lastc = max(split_ref(c.get("r"))[0] for c in sh.rows[first].findall(q("c")))

    def row_styles(r):
        return {split_ref(c.get("r"))[0]: c.get("s") for c in sh.rows[r].findall(q("c"))}

    st_first, st_mid = row_styles(first), row_styles(first + 1)
    st_btot, st_grand = row_styles(block_total), row_styles(grand)
    st_fill = row_styles(filler_r) if filler_r else {}
    base_attrs = {k: v for k, v in sh.rows[first].attrib.items() if k not in ("r", "spans")}
    widths = col_widths(rep_root)

    sd = rep_root.find(q("sheetData"))
    new_rows: dict[int, etree._Element] = {}

    def mk_row(r, styles, attrs=None):
        e = etree.Element(q("row"))
        e.set("r", str(r))
        for k, v in (attrs or base_attrs).items():
            e.set(k, v)
        cells = {}
        for c in range(1, lastc + 1):
            cel = etree.SubElement(e, q("c"))
            cel.set("r", f"{col_letter(c)}{r}")
            if styles.get(c) is not None:
                cel.set("s", styles[c])
            cells[c] = cel
        new_rows[r] = e
        return cells

    def put_text(cel, text):
        cel.set("t", "s")
        etree.SubElement(cel, q("v")).text = str(sst.get(text))

    def put_f(cel, f):
        etree.SubElement(cel, q("f")).text = f

    L = col_letter
    r = first
    totals, merges = [], []
    for name, tsh in books:
        tl = TcLayout(tsh)
        qn = "'" + name.replace("'", "''") + "'"
        res_cols = [L(tl.cols["result1"]), L(tl.cols.get("result2", tl.cols["result1"]))]
        tvp = L(tl.cols["tvp_id"])
        pairs = tc_pairs(tsh)
        b0 = r
        for k, (i_, ii, a, b) in enumerate(pairs):
            cells = mk_row(r, st_first if k == 0 else st_mid)
            need2 = len(i_) > widths.get(c_i, 20) * 1.2 or len(ii) > widths.get(c_ii, 30) * 1.2
            if need2:
                new_rows[r].set("ht", str(round(float(base_attrs.get("ht", 15.75)) * 2, 2)))
                new_rows[r].set("customHeight", "1")
            if k == 0:
                put_text(cells[c_sheet], name)
            put_text(cells[c_i], i_)
            put_text(cells[c_ii], ii)
            for (rate, exe, tot, sts), res in zip(rounds, res_cols):
                put_f(cells[rate], f"{L(exe)}{r}/{L(tot)}{r}")
                put_f(cells[exe], f"SUM({L(sts[0])}{r}:{L(sts[4])}{r})")
                put_f(cells[tot], f"SUM({L(sts[0])}{r}:{L(sts[5])}{r})")
                for j in range(5):
                    put_f(cells[sts[j]], f"COUNTIF({qn}!${res}${a}:${res}${b},{L(sts[j])}${hdr})")
                put_f(cells[sts[5]], f"COUNTA({qn}!${tvp}${a}:${tvp}${b})-SUM({L(sts[0])}{r}:{L(sts[4])}{r})")
            r += 1
        cells = mk_row(r, st_btot)
        put_text(cells[c_i], "Total")
        for rate, exe, tot, sts in rounds:
            put_f(cells[rate], f"{L(exe)}{r}/{L(tot)}{r}")
            put_f(cells[exe], f"SUM({L(sts[0])}{r}:{L(sts[4])}{r})")
            put_f(cells[tot], f"SUM({L(sts[0])}{r}:{L(sts[5])}{r})")
            for c in sts:
                put_f(cells[c], f"SUM({L(c)}{b0}:{L(c)}{r - 1})")
        merges.append(f"{L(c_sheet)}{b0}:{L(c_sheet)}{r}")
        totals.append(r)
        r += 1
    cells = mk_row(r, st_grand)
    put_text(cells[c_sheet], "Total")
    for rate, exe, tot, sts in rounds:
        put_f(cells[rate], f"{L(exe)}{r}/{L(tot)}{r}")
        for c in [exe, tot] + sts:
            put_f(cells[c], "SUM(" + ",".join(f"{L(c)}{t}" for t in totals) + ")")
    end_new = r
    # dòng cũ còn thừa → về dạng dòng trống của mẫu
    for rr in range(end_new + 1, grand + 1):
        mk_row(rr, st_fill, {k: v for k, v in sh.rows[filler_r].attrib.items() if k not in ("r", "spans")} if filler_r else None)
    # thay dòng trong sheetData
    for row in list(sd.findall(q("row"))):
        rn = int(row.get("r"))
        if first <= rn <= max(grand, end_new):
            sd.remove(row)
    for rn in sorted(new_rows):
        sd.append(new_rows[rn])
    _sort_rows(sd)
    mc = rep_root.find(q("mergeCells"))
    for m in list(mc.findall(q("mergeCell"))):
        if Sheet._rng(m.get("ref"))[1] >= first:
            mc.remove(m)
    for ref in merges:
        etree.SubElement(mc, q("mergeCell")).set("ref", ref)
    mc.set("count", str(len(mc.findall(q("mergeCell")))))
    return end_new


# ----------------------------------------------------------------------------- Cover
def add_change(cover_root, sst: SharedStrings, values: list[str], book: Styles | None = None):
    """Thêm một dòng vào bảng Record of change. Từ dòng thứ hai trở đi, ô mới căn lề như dòng đầu của bảng."""
    sh = Sheet(cover_root, sst)
    hit = sh.find_text("Effective Date")
    if not hit:
        raise SystemExit("Sheet bìa không có bảng 'Effective Date'")
    c0, r0 = hit
    r = r0 + 1
    while sh.value(c0, r):
        r += 1
    for k, val in enumerate(values):
        cel = _cell(cover_root, c0 + k, r)
        ref = sh.cells.get((c0 + k, r0 + 1))
        if book is not None and r != r0 + 1 and ref is not None and ref.get("s") and cel.get("s"):
            cel.set("s", book.like(cel.get("s"), ref.get("s")))
        if not val:
            continue
        for ch in list(cel):
            cel.remove(ch)
        cel.set("t", "s")
        etree.SubElement(cel, q("v")).text = str(sst.get(val))
    ver = values[1].strip() if len(values) > 1 else ""
    lab = sh.find_text("Version", rows=range(1, r0))
    if ver and lab:                                   # ô Version ở khối đầu trang bìa đi theo dòng mới nhất
        cel = _cell(cover_root, lab[0] + 1, lab[1])
        for ch in list(cel):
            cel.remove(ch)
        cel.set("t", "s")
        etree.SubElement(cel, q("v")).text = str(sst.get("Version " + ver))
    return r


# ----------------------------------------------------------------------------- main
def utf8_console() -> None:
    """Windows: khi kết quả in ra bị chuyển hướng (pipe, file), Python dùng bảng mã của máy và vấp chữ có dấu."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description="Thêm sheet TC vào file mẫu, nhân bản định dạng của sheet mẫu.")
    ap.add_argument("--book", required=True, help="file .xlsx mẫu của dự án (không bị sửa)")
    ap.add_argument("--like", required=True, help="tên sheet TC dùng làm mẫu định dạng")
    ap.add_argument("--sheet", required=True, help="tên sheet mới")
    ap.add_argument("--data", required=True, help="TSV phẳng")
    ap.add_argument("--out", required=True)
    ap.add_argument("--function", default=None)
    ap.add_argument("--screen", default=None)
    ap.add_argument("--creator", default=None)
    ap.add_argument("--created", default=None)
    ap.add_argument("--source", default=None)
    ap.add_argument("--report", default=None, help="tên sheet báo cáo cần dựng lại (vd Test_Report)")
    ap.add_argument("--change", default=None, help="một dòng Record of change: ngày|version|mục|A/D/M|mô tả|tham chiếu")
    a = ap.parse_args()

    pkg = Package(Path(a.book))
    wb = pkg.xml("xl/workbook.xml")
    rels = pkg.xml("xl/_rels/workbook.xml.rels")
    ct = pkg.xml("[Content_Types].xml")
    rid_target = {r.get("Id"): r.get("Target") for r in rels}

    def path_of(sheet_el):
        t = rid_target[sheet_el.get(f"{{{RNS}}}id")]
        return t.lstrip("/") if t.startswith("/") else "xl/" + t

    sheets_el = wb.find(q("sheets"))
    by_name = {s.get("name"): s for s in sheets_el.findall(q("sheet"))}
    if a.like not in by_name:
        raise SystemExit(f"Không có sheet mẫu '{a.like}'. Các sheet: {', '.join(by_name)}")
    if a.sheet in by_name:
        raise SystemExit(f"Sheet '{a.sheet}' đã có trong file.")
    sst_name = next(("xl/" + r.get("Target").lstrip("/").replace("xl/", "", 1) for r in rels
                     if r.get("Type").endswith("/sharedStrings")), "xl/sharedStrings.xml")
    sst_root = pkg.xml(sst_name)
    sst = SharedStrings(sst_root)

    tpl_path = path_of(by_name[a.like])
    rows = read_tsv(Path(a.data))
    meta = {"function": a.function, "screen": a.screen, "creator": a.creator,
            "created": a.created, "source": a.source}
    st_name = next(("xl/" + r.get("Target").lstrip("/").replace("xl/", "", 1) for r in rels
                    if r.get("Type").endswith("/styles")), "xl/styles.xml")
    st_root = pkg.xml(st_name)
    styles = Styles(st_root)
    new_root, lay, first, last = build_sheet(pkg.xml(tpl_path), sst, rows, meta, styles)
    n_open, _ = mark_open_rows(new_root, sst, styles)

    # --- đăng ký sheet mới
    nums = [int(m.group(1)) for n in pkg.names for m in [re.match(r"xl/worksheets/sheet(\d+)\.xml$", n)] if m]
    new_path = f"xl/worksheets/sheet{max(nums) + 1}.xml"
    rid = "rId" + str(max(int(re.sub(r"\D", "", r.get("Id")) or "0") for r in rels) + 1)
    rel = etree.SubElement(rels, f"{{{PNS}}}Relationship")
    rel.set("Id", rid)
    rel.set("Type", WS_TYPE)
    rel.set("Target", new_path.replace("xl/", "", 1))
    rid_target[rid] = rel.get("Target")
    ov = etree.SubElement(ct, f"{{{CTNS}}}Override")
    ov.set("PartName", "/" + new_path)
    ov.set("ContentType", WS_CT)
    tpl_el = by_name[a.like]
    pos = list(sheets_el).index(tpl_el) + 1
    sh_el = etree.Element(q("sheet"))
    sh_el.set("name", a.sheet)
    sh_el.set("sheetId", str(max(int(s.get("sheetId")) for s in sheets_el) + 1))
    sh_el.set("state", "visible")
    sh_el.set(f"{{{RNS}}}id", rid)
    sheets_el.insert(pos, sh_el)
    dn = wb.find(q("definedNames"))
    if dn is not None:
        for d in dn.findall(q("definedName")):
            if d.get("localSheetId") and int(d.get("localSheetId")) >= pos:
                d.set("localSheetId", str(int(d.get("localSheetId")) + 1))
    bv = wb.find(q("bookViews"))
    if bv is not None:
        for v in bv.findall(q("workbookView")):
            v.set("activeTab", str(pos))
            v.set("firstSheet", "0")
    # các sheet khác bỏ trạng thái được chọn, tránh mở file ra ở chế độ nhóm sheet
    for s in sheets_el.findall(q("sheet")):
        if s is sh_el:
            continue
        p = path_of(s)
        root = pkg.xml(p)
        changed = False
        for v in root.iter(q("sheetView")):
            if v.get("tabSelected") == "1":
                v.attrib.pop("tabSelected")
                changed = True
        if changed:
            pkg.put(p, root)

    pkg.put(new_path, new_root, after=tpl_path)

    # --- báo cáo
    if a.report:
        if a.report not in by_name:
            raise SystemExit(f"Không có sheet báo cáo '{a.report}'")
        rep_path = path_of(by_name[a.report])
        rep_root = pkg.xml(rep_path)
        books = []
        for s in sheets_el.findall(q("sheet")):
            root = new_root if s is sh_el else pkg.xml(path_of(s))
            shx = Sheet(root, sst)
            if shx.find_text("No.") and s.get("name") != a.report:
                try:
                    TcLayout(shx)
                except SystemExit:
                    continue
                books.append((s.get("name"), shx))
        end = rebuild_report(rep_root, sst, books)
        pkg.put(rep_path, rep_root)
        print(f"{a.report}: dựng lại cho {', '.join(n for n, _ in books)} · dòng cuối {end}")

    if a.change:
        cover = next((s for s in sheets_el.findall(q("sheet"))
                      if Sheet(pkg.xml(path_of(s)), sst).find_text("Effective Date")), None)
        if cover is None:
            raise SystemExit("Không tìm thấy bảng Record of change")
        cp = path_of(cover)
        croot = pkg.xml(cp)
        r = add_change(croot, sst, a.change.split("|"), styles)
        pkg.put(cp, croot)
        print(f"{cover.get('name')}: thêm dòng Record of change ở hàng {r}")

    sst.finish()
    pkg.put(sst_name, sst_root)
    if styles.changed:
        pkg.put(st_name, st_root)
    pkg.put("xl/workbook.xml", wb)
    pkg.put("xl/_rels/workbook.xml.rels", rels)
    pkg.put("[Content_Types].xml", ct)
    pkg.save(Path(a.out))
    print(f"{len(rows)} TC → sheet '{a.sheet}' (dòng {first}–{last}), định dạng nhân bản từ '{a.like}' → {a.out}")
    print(f"dòng còn câu hỏi mở: {n_open}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
