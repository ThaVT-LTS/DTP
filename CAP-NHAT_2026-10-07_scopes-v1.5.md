# Tài liệu cập nhật 07/10/2026 — tc-authoring v0.4 (sau bản Scopes v1.5)

Nguồn: góp ý của Hanna ngày 06/10 và 07/10 — FB-042 → FB-049 và FB-016 trong `feedback/log.md`.

Phần rule (`rules/tc-authoring.md` v0.5) đã được ghi thẳng vào thư mục. Tài liệu này chứa phần AI không ghi được từ xa (thư mục `.claude`), cùng hai file phải đổi cùng lúc với script mới (`CLAUDE.md`, `README.md`). Mọi thay đổi đều **chờ Hanna duyệt**.

## Cách áp

Mở cửa sổ lệnh ở thư mục `Documents\qa-pipeline`, chạy lần lượt:

    python ap_dung_cap_nhat.py --doc CAP-NHAT_2026-10-07_scopes-v1.5.md
    python ap_dung_cap_nhat.py --doc CAP-NHAT_2026-10-07_scopes-v1.5.md --ap
    python .claude/skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .
    python scripts/export_web.py

- Lệnh đầu chỉ chạy thử: phải ra 26 chỗ `[OK]` và 1 chỗ `[tạo mới]`, không có `[cần sửa tay]`.
- Lệnh thứ hai áp thật; file cũ được sao vào `_sao-luu/<ngày giờ>/`.
- Sau khi áp, bỏ qua dòng "Bước tiếp: đánh số FB": tài liệu này dùng số FB thật, không cần đánh số.
- Chưa áp thì rule mới ở `rules/` vẫn có hiệu lực; SKILL.md, references và `tc_check.py` còn là bản 05/10, và chưa có lệnh `tc_fix_xlsx.py`.

## Nội dung

| # | File | Đổi gì |
|---|---|---|
| 1 | `tc_check.py` | Thêm kiểm: ô TC còn `{{…}}`; dòng có nội dung mà thiếu TVP_ID; cột No. không liền mạch; ô bắt đầu bằng `-` `+` `=` `@` thiếu dấu nháy đơn; ô có chữ dạng tổ hợp; ô trống đã định dạng mà sai phông. So tên nhóm sau khi chuẩn hoá NFC. Cảnh báo khu vực còn nhóm Kiểm tra dữ liệu |
| 2 | `tc_fix_xlsx.py` (mới) | Đưa file TC có sẵn về Times New Roman 10 cho mọi ô, gắn dấu nháy đơn đầu ô, chuẩn hoá dạng chữ; `--check` để chỉ kiểm |
| 3 | `SKILL.md` v0.3 → v0.4 | Bước 4, 5, 6, 7 theo rule mới |
| 4 | `references/format.md` | §4: phông cho mọi ô, dấu nháy đơn, dạng chữ, kiểu Normal; §7: nhóm Kiểm tra dữ liệu |
| 5 | `references/patterns.md` | P1, P7: nơi kiểm sau khi tạo; P12: cột giá trị tính toán |
| 6 | `CLAUDE.md` | Cổng bước 5 và mục Script thêm `tc_fix_xlsx.py --check` |
| 7 | `README.md` | Ghi bản cập nhật 07/10; thư viện `lxml` |

Kết quả chạy thử hai script trên các bản file TC (AI chạy ngày 07/10):

| File | `tc_check.py` bản 05/10 | `tc_check.py` bản này | `tc_fix_xlsx.py --check` |
|---|---|---|---|
| `SGS-DTP_TestCase1_v1.3.xlsx` | chưa chạy lại | 12 lỗi | còn chỗ phải sửa: 15 kiểu ô sai phông, 203 ô thiếu dấu nháy đơn |
| `SGS-DTP_TestCase1_v1.4.xlsx` | 8 lỗi, trong đó 1 lỗi giả ("thiếu Không thành công") | 26 lỗi | còn chỗ phải sửa: 16 kiểu ô sai phông, 45 chuỗi dạng tổ hợp, 182 ô thiếu dấu nháy đơn |
| `SGS-DTP_TestCase1_v1.5.xlsx` | 0 lỗi | 3 lỗi: Login 50 TC, Users 62 TC, Profile 13 TC còn `{{…}}` (ba sheet này chưa viết lại) | sạch |
| `SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx` (Hanna sửa bản v1.5 bằng ONLYOFFICE, gửi 13:28 ngày 07/10) | 2 lỗi: 17 ô sai phông, Scope_104 thiếu UC | 6 lỗi: 3 lỗi `{{…}}` như trên, 18 ô sai phông, 7 ô có chữ dạng tổ hợp, Scope_104 thiếu UC | còn chỗ phải sửa: 5 kiểu ô sai phông (18 ô), 7 chuỗi dạng tổ hợp |

## 1. `.claude/skills/tc-authoring/scripts/tc_check.py`

**check-1 docstring Tìm**

````
  - Ô có nội dung sai phông / cỡ chữ, hoặc dùng màu nền / màu chữ ngoài bảng màu (mọi sheet)
Cảnh báo:
````

**Thay bằng**

````
  - Ô sai phông / cỡ chữ (kể cả ô trống đã định dạng), hoặc dùng màu nền / màu chữ ngoài bảng màu (mọi sheet).
    Ô nằm trong cụm gộp và kiểu mặc định của cột thì openpyxl không đọc được: kiểm bằng tc_fix_xlsx.py --check
  - Ô văn bản bắt đầu bằng - + = @ mà không có dấu nháy đơn ở đầu (quotePrefix); ô có chữ ở dạng tổ hợp, chưa phải NFC (mọi sheet)
  - Ô của TC còn dạng {{…}}; dòng có nội dung mà thiếu TVP_ID; cột No. không liền mạch từ 1
Cảnh báo: khu vực còn nhóm Kiểm tra dữ liệu / Validation (case bấm nút gửi mà không lưu được thuộc nhóm Không thành công, rule 8);
````

**check-1b import Tìm**

````
import openpyxl
````

**Thay bằng**

````
import openpyxl
from openpyxl.cell.cell import MergedCell
````

**check-2 hằng số Tìm**

````
FONT, SIZE = "Times New Roman", 10
````

**Thay bằng**

````
FONT, SIZE = "Times New Roman", 10
FORMULA_START = ("-", "+", "=", "@")                   # rules/tc-authoring.md rule 32


def nfc(v):
    """Chuỗi ở dạng dựng sẵn; chữ gõ dạng tổ hợp nhìn giống hệt nhưng so sánh thì khác (rule 33)."""
    return unicodedata.normalize("NFC", v) if isinstance(v, str) else v
````

**check-3 check_format Tìm**

````
def check_format(ws, errors):
    """Mọi ô có nội dung: đúng phông, đúng cỡ, màu thuộc bảng màu. Gộp lỗi theo sheet."""
    bad = {"phông": [], "cỡ chữ": [], "màu nền": [], "màu chữ": []}
    for row in ws.iter_rows():
        for c in row:
            if c.value is None or str(c.value).strip() == "":
                continue
            f = c.font
````

**Thay bằng**

````
def check_format(ws, errors):
    """Mọi ô đã định dạng, kể cả ô trống: đúng phông, đúng cỡ, màu thuộc bảng màu.
    Ô văn bản: có dấu nháy đơn khi bắt đầu bằng - + = @, và chữ ở dạng NFC. Gộp lỗi theo sheet.
    Ô nằm trong cụm gộp (không phải ô neo) bị bỏ qua: openpyxl không giữ kiểu thật của các ô đó."""
    bad = {"phông": [], "cỡ chữ": [], "màu nền": [], "màu chữ": [], "thiếu dấu nháy đơn đầu ô": [], "có chữ dạng tổ hợp (chưa NFC)": []}
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c, MergedCell):
                continue
            empty = c.value is None or str(c.value).strip() == ""
            if empty and not c.has_style:
                continue
            if isinstance(c.value, str):
                if c.value.lstrip()[:1] in FORMULA_START and not c.quotePrefix:
                    bad["thiếu dấu nháy đơn đầu ô"].append(c.coordinate)
                if nfc(c.value) != c.value:
                    bad["có chữ dạng tổ hợp (chưa NFC)"].append(c.coordinate)
            f = c.font
````

**check-4 thông báo lỗi định dạng Tìm**

````
            errors.append(f"{ws.title} · {len(cells)} ô sai {kind}: {', '.join(cells[:5])}{more}")
````

**Thay bằng**

````
            label = kind if kind.startswith(("thiếu", "có")) else "sai " + kind
            errors.append(f"{ws.title} · {len(cells)} ô {label}: {', '.join(cells[:5])}{more}")
````

**check-5 dòng thiếu TVP_ID Tìm**

````
    for r in range(DATA_ROW, ws.max_row + 1):
        tvp = ws.cell(r, C_TVP).value
        if not tvp:
            continue
        where = f"{ws.title}!{r}"
````

**Thay bằng**

````
    numbers, braces = [], []
    for r in range(DATA_ROW, ws.max_row + 1):
        tvp = ws.cell(r, C_TVP).value
        where = f"{ws.title}!{r}"
        if not tvp:
            if any(str(ws.cell(r, c).value or "").strip() for c in (C_NAME, C_STEP, C_EXP)):
                errors.append(f"{where} · dòng có nội dung mà thiếu TVP_ID")
            continue
        numbers.append(ws.cell(r, C_NO).value)
````

**check-6 nhóm theo khu vực Tìm**

````
        if ws.cell(r, C_II).value:
            cur_ii = ws.cell(r, C_II).value
        areas.setdefault(cur_ii, set()).add(str(ws.cell(r, C_III).value or ""))
````

**Thay bằng**

````
        if ws.cell(r, C_II).value:
            cur_ii = nfc(ws.cell(r, C_II).value)
        areas.setdefault(cur_ii, set()).add(nfc(str(ws.cell(r, C_III).value or "")))
````

**check-7 ô còn {{…}} Tìm**

````
        pre = str(ws.cell(r, C_PRE).value or "")
        if OPEN_SCREEN.search(pre):
````

**Thay bằng**

````
        cells_tc = [str(ws.cell(r, c).value or "") for c in (C_I, C_II, C_III, C_IV, C_NAME, C_PRE, C_STEP, C_EXP)]
        if any("{{" in v for v in cells_tc):
            braces.append(str(tvp))
        pre = str(ws.cell(r, C_PRE).value or "")
        if OPEN_SCREEN.search(pre):
````

**check-8 No. liền mạch, nhóm Kiểm tra dữ liệu Tìm**

````
    for area, lv3 in areas.items():
        if not area:
            continue
        joined = " ".join(lv3).lower()
````

**Thay bằng**

````
    if braces:
        more = f" … (+{len(braces) - 5})" if len(braces) > 5 else ""
        errors.append(f"{ws.title} · {len(braces)} TC còn dạng {{{{…}}}}, phải ghi giá trị cụ thể hoặc [tên] (rule 14): {', '.join(braces[:5])}{more}")
    if numbers and [str(n).strip() for n in numbers] != [str(i) for i in range(1, len(numbers) + 1)]:
        first_bad = next((i for i, n in enumerate(numbers, 1) if str(n).strip() != str(i)), None)
        errors.append(f"{ws.title} · cột No. không liền mạch từ 1 (TC thứ {first_bad} đang ghi {numbers[first_bad - 1]!r})")

    for area, lv3 in areas.items():
        if not area:
            continue
        joined = " ".join(lv3).lower()
        if "kiểm tra dữ liệu" in joined or re.search(r"\bvalidation\b", joined):
            warns.append(f"{ws.title} · khu vực '{area}' còn nhóm Kiểm tra dữ liệu: case bấm nút gửi mà không lưu được thì đưa vào Không thành công (rule 8)")
````

## 2. `.claude/skills/tc-authoring/scripts/tc_fix_xlsx.py`

**fix-1 script mới Tạo file mới**

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đưa một file test case có sẵn về đúng định dạng, làm thẳng trên XML nên logo, dropdown, công thức giữ nguyên.

    python tc_fix_xlsx.py TestCase.xlsx --out TestCase_fixed.xlsx     # sửa, ghi ra file mới
    python tc_fix_xlsx.py TestCase.xlsx --check                       # chỉ kiểm: mã thoát 1 nếu còn chỗ phải sửa

Ba việc (rules/tc-authoring.md rule 18, 32, 33):
  1. Phông: mọi kiểu ô, mọi đoạn chữ định dạng riêng dùng phông khác Times New Roman 10 → Times New Roman 10.
     Gồm cả ô trống đã kẻ khung, ô trong cụm gộp và kiểu mặc định của cột. Kiểu Normal của file giữ nguyên,
     vì Excel tính độ rộng cột theo phông của kiểu Normal.
  2. Dấu nháy đơn: ô văn bản bắt đầu bằng - + = @ được gắn thuộc tính quotePrefix, để sửa ô trong Excel
     không bị hiểu là công thức. Không thêm ký tự ' vào nội dung.
  3. Dạng chữ: mọi chuỗi về dạng dựng sẵn (NFC).

Không dùng openpyxl để lưu: openpyxl làm rơi ảnh và dropdown dạng x14. Cần thư viện lxml.
"""
from __future__ import annotations

import argparse
import copy
import re
import sys
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path

from lxml import etree

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
RNS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
FONT, SIZE = "Times New Roman", 10.0
START = ("-", "+", "=", "@")


def q(tag: str) -> str:
    return f"{{{NS}}}{tag}"


def to_bytes(root) -> bytes:
    return b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' + etree.tostring(root, encoding="UTF-8")


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def sig(el):
    return (etree.QName(el).localname, tuple(sorted(el.attrib.items())), tuple(sig(c) for c in el))


def font_ok(font) -> bool:
    name, sz = font.find(q("name")), font.find(q("sz"))
    return name is not None and name.get("val") == FONT and sz is not None and float(sz.get("val")) == SIZE


def fixed_font(font):
    """Bản sao của `font` với tên và cỡ chuẩn; giữ đậm, màu."""
    f = copy.deepcopy(font)
    for tag in ("name", "sz", "scheme", "family", "charset"):
        for e in f.findall(q(tag)):
            f.remove(e)
    sz = etree.Element(q("sz"))
    sz.set("val", "10")
    name = etree.Element(q("name"))
    name.set("val", FONT)
    color = f.find(q("color"))
    if color is not None:
        color.addprevious(sz)
        color.addnext(name)
    else:
        f.append(sz)
        f.append(name)
    return f


def col_letters(ref: str) -> str:
    return re.match(r"[A-Z]+", ref).group(0)


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Đưa file test case về Times New Roman 10, thêm dấu nháy đơn đầu ô, chuẩn hoá dạng chữ.")
    ap.add_argument("xlsx")
    ap.add_argument("--out", help="file ghi ra (không ghi đè file gốc)")
    ap.add_argument("--check", action="store_true", help="chỉ kiểm, không ghi")
    a = ap.parse_args()
    if not a.check and not a.out:
        ap.error("cần --out <file ra> hoặc --check")
    if a.out and Path(a.out).resolve() == Path(a.xlsx).resolve():
        ap.error("--out phải khác file gốc")

    with zipfile.ZipFile(a.xlsx) as z:
        names = z.namelist()
        data = {n: z.read(n) for n in names}
    wb = etree.fromstring(data["xl/workbook.xml"])
    rels = {r.get("Id"): r.get("Target") for r in etree.fromstring(data["xl/_rels/workbook.xml.rels"])}
    sheets = []
    for s in wb.find(q("sheets")):
        t = rels[s.get(f"{{{RNS}}}id")]
        sheets.append((s.get("name"), t.lstrip("/") if t.startswith("/") else "xl/" + t))
    st = etree.fromstring(data["xl/styles.xml"])
    fonts, xfs = st.find(q("fonts")), st.find(q("cellXfs"))
    has_sst = "xl/sharedStrings.xml" in data
    sst = etree.fromstring(data["xl/sharedStrings.xml"]) if has_sst else None
    sis = sst.findall(q("si")) if sst is not None else []
    roots = {p: etree.fromstring(data[p]) for _, p in sheets}
    dirty = set()                                   # sheet nào có ô đổi thì mới ghi lại
    report = []

    # ---------------------------------------------------------------- 1. phông của kiểu ô
    used = Counter()
    for name, p in sheets:
        root = roots[p]
        for c in root.iter(q("c")):
            used[int(c.get("s", "0"))] += 1
        for col in root.iter(q("col")):
            used[int(col.get("style", "0"))] += 1
        for row in root.iter(q("row")):
            if row.get("s"):
                used[int(row.get("s"))] += 1

    def add(parent, el) -> int:
        s = sig(el)
        for i, e in enumerate(parent):
            if sig(e) == s:
                return i
        parent.append(el)
        parent.set("count", str(len(parent)))
        return len(parent) - 1

    # phông chữ thường của file: phông chuẩn, không đậm, được nhiều ô dùng nhất
    weight = Counter()
    for i, xf in enumerate(xfs):
        f = fonts[int(xf.get("fontId", "0"))]
        if font_ok(f) and f.find(q("b")) is None:
            weight[int(xf.get("fontId", "0"))] += used.get(i, 0)
    plain = weight.most_common(1)[0][0] if weight else None

    bad_xf = []
    for i, xf in enumerate(xfs):
        f = fonts[int(xf.get("fontId", "0"))]
        if font_ok(f):
            continue
        bad_xf.append(i)
        only_name_size = f.find(q("b")) is None and f.find(q("i")) is None and f.find(q("color")) is None
        new_id = plain if (only_name_size and plain is not None) else add(fonts, fixed_font(f))
        xf.set("fontId", str(new_id))
        xf.set("applyFont", "1")
    n_cells = sum(used.get(i, 0) for i in bad_xf)
    if bad_xf:
        where = Counter()
        for name, p in sheets:
            for c in roots[p].iter(q("c")):
                if int(c.get("s", "0")) in bad_xf:
                    where[name] += 1
        report.append("phông: %d kiểu ô khác %s %g, dùng ở %d ô và kiểu mặc định của cột (%s)" % (
            len(bad_xf), FONT, SIZE, n_cells, ", ".join("%s %d" % kv for kv in where.items())))

    # đoạn chữ định dạng riêng trong ô
    n_runs = 0
    for si in sis:
        for rpr in si.iter(q("rPr")):
            rf, sz = rpr.find(q("rFont")), rpr.find(q("sz"))
            if (rf is not None and rf.get("val") != FONT) or (sz is not None and float(sz.get("val")) != SIZE):
                n_runs += 1
                if rf is not None:
                    rf.set("val", FONT)
                if sz is not None:
                    sz.set("val", "10")
                for e in rpr.findall(q("scheme")):
                    rpr.remove(e)
    if n_runs:
        report.append("phông: %d đoạn chữ định dạng riêng khác %s %g" % (n_runs, FONT, SIZE))

    # ---------------------------------------------------------------- 3. dạng chữ (làm trước để mục 2 đọc chuỗi đã chuẩn)
    n_nfc = 0
    for si in sis:
        for t in si.iter(q("t")):
            if t.text and nfc(t.text) != t.text:
                t.text = nfc(t.text)
                n_nfc += 1
    for p, root in roots.items():
        for t in root.iter(q("t")):
            if t.text and nfc(t.text) != t.text:
                t.text = nfc(t.text)
                n_nfc += 1
                dirty.add(p)
    if n_nfc:
        report.append("dạng chữ: %d chuỗi ở dạng tổ hợp, chưa phải dạng dựng sẵn (NFC)" % n_nfc)

    # ---------------------------------------------------------------- 2. dấu nháy đơn
    texts = ["".join(t.text or "" for t in si.iter(q("t")) if t.getparent().tag != q("rPh")) for si in sis]
    cache: dict[str, str] = {}

    def quoted(s: str) -> str:
        if s not in cache:
            xf = xfs[int(s)]
            if xf.get("quotePrefix") == "1":
                cache[s] = s
            else:
                new = copy.deepcopy(xf)
                new.set("quotePrefix", "1")
                cache[s] = str(add(xfs, new))
        return cache[s]

    missing = Counter()
    sample = []
    for name, p in sheets:
        for c in roots[p].iter(q("c")):
            if c.find(q("f")) is not None:
                continue
            t = c.get("t")
            if t == "s" and c.find(q("v")) is not None:
                txt = texts[int(c.find(q("v")).text)]
            elif t == "inlineStr":
                txt = "".join(x.text or "" for x in c.iter(q("t")))
            elif t == "str" and c.find(q("v")) is not None:
                txt = c.find(q("v")).text or ""
            else:
                continue
            if txt.lstrip()[:1] in START:
                s = c.get("s", "0")
                new = quoted(s)
                if new != s:
                    c.set("s", new)
                    dirty.add(p)
                    missing[name] += 1
                    if len(sample) < 5:
                        sample.append("%s!%s" % (name, c.get("r")))
    if missing:
        report.append("dấu nháy đơn: %d ô bắt đầu bằng - + = @ chưa có quotePrefix (%s), vd %s" % (
            sum(missing.values()), ", ".join("%s %d" % kv for kv in missing.items()), ", ".join(sample)))

    if not report:
        print("Sạch: mọi ô %s %g, ô bắt đầu bằng - + = @ đều có dấu nháy đơn, mọi chuỗi ở dạng NFC." % (FONT, SIZE))
        return 0
    for line in report:
        print(("CẦN SỬA · " if a.check else "ĐÃ SỬA · ") + line)
    if a.check:
        return 1

    data["xl/styles.xml"] = to_bytes(st)
    if has_sst:
        data["xl/sharedStrings.xml"] = to_bytes(sst)
    for p in dirty:
        data[p] = to_bytes(roots[p])
    with zipfile.ZipFile(a.out, "w", zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.writestr(n, data[n])
    print("→ " + a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
````

## 3. `.claude/skills/tc-authoring/SKILL.md`

**skill-1 phiên bản Tìm**

````
# Viết test case (v0.3)
````

**Thay bằng**

````
# Viết test case (v0.4)
````

**skill-2 Bước 4, nơi kiểm kết quả Tìm**

````
Mỗi điểm hiển thị là một TC riêng. Điểm nào chỉ xuất hiện sau một hành động khác thì ghi rõ — đây là chỗ sai nhiều nhất.

TC điểm hiển thị viết ở sheet của hành động, kể cả khi điểm đó nằm ở màn khác hay vai trò khác (rule 27). Chỉ chuỗi nhiều hành động qua nhiều chức năng mới tách ra `FLOW-nn`.
````

**Thay bằng**

````
Bảng này để biết dữ liệu đi tới đâu, không phải để nhân case. Cách đặt TC (`rules/tc-authoring.md` rule 9, 13, 30):

- Nhóm Thành công của hành động kiểm ở **nơi hành động trả về** (vd tạo scope xong thì kiểm dòng vừa tạo ở danh sách); chỗ hiển thị khác nhau theo loại thì mỗi loại một case.
- Điểm hiển thị khác **trong cùng sheet** đã có khu vực riêng (vd màn chi tiết) thì kiểm ở khu vực đó, không lặp ở khu vực của hành động.
- Điểm hiển thị ở **màn khác, sheet khác** hoặc vai trò khác: viết ở sheet của hành động (rule 27). Chỉ chuỗi nhiều hành động qua nhiều chức năng mới tách ra `FLOW-nn`.
- Điểm hiển thị do suy ra mà UC, Figma không nêu thì không viết thành câu khẳng định: để trống Expected và hỏi, hoặc không viết case.
- Điểm nào chỉ xuất hiện sau một hành động khác thì ghi rõ — đây là chỗ sai nhiều nhất.
````

**skill-3 Bước 5, thứ tự nhóm Tìm**

````
Theo pattern của từng khu vực, theo thứ tự: hiển thị → nhập liệu → kiểm tra dữ liệu → thành công → không thành công → phân quyền → bảo mật (file tiếng Anh: Display → Input → Validation → Success → Failure → Permission → Security; bảng từ ở `references/format.md` §7).
````

**Thay bằng**

````
Theo pattern của từng khu vực, theo thứ tự: hiển thị → nhập liệu → không thành công → thành công → phân quyền → bảo mật (file tiếng Anh: Display → Input → Failure → Success → Permission → Security; bảng từ ở `references/format.md` §7). Case bấm nút gửi mà không lưu được (bỏ trống trường bắt buộc, chỉ có khoảng trắng, trùng tên, quá giới hạn) thuộc nhóm Không thành công, cùng Cancel, ×, Esc; không lập nhóm Kiểm tra dữ liệu cho các case đó (rule 8). Thứ tự Không thành công trước Thành công lấy theo bản v1.4 của Hanna, **chờ Hanna chọn**.
````

**skill-4 Bước 5, quy tắc viết Tìm**

````
- Pre-condition mở đầu bằng dòng đăng nhập theo `rules/tc-authoring.md` rule 14 (`Logged in as <role>` / `Not logged in`); dữ liệu và nhãn ghi thẳng trong ô;
````

**Thay bằng**

````
- Pre-condition mở đầu bằng dòng đăng nhập theo `rules/tc-authoring.md` rule 14 (`Logged in as <role>` / `Not logged in`); dữ liệu và nhãn ghi thẳng trong ô;
- không dùng dạng `{{…}}`: dữ liệu tester tự nhập ghi giá trị cụ thể (`Name: abc`), dữ liệu phải có sẵn mà chưa xác định ghi `[tên]` (`Belongs to organisation: [Organization]`); nhập nhiều trường thì mỗi trường một dòng; text nguyên văn đặt riêng một dòng trong ngoặc kép (rule 14);
- giá trị tính toán hiển thị trên màn (tỉ lệ, tổng, số đếm) có một nhóm TC với bộ số cụ thể, kể cả các biên chưa có căn cứ (rule 31);
````

**skill-5 Bước 6, sửa file có sẵn Tìm**

````
Script tự: gộp ô bốn cột Classification theo quy tắc, đặt phông Times New Roman 10, căn trái, tô đỏ dòng còn câu hỏi mở, dựng khối thông tin đầu sheet và hàng tiêu đề hai tầng.
````

**Thay bằng**

````
Script tự: gộp ô bốn cột Classification theo quy tắc, đặt phông Times New Roman 10, căn trái, tô đỏ dòng còn câu hỏi mở, dựng khối thông tin đầu sheet và hàng tiêu đề hai tầng.

File TC đã có sẵn (vd file người dùng vừa sửa tay rồi gửi lại) thì đưa về đúng định dạng bằng:

```
python scripts/tc_fix_xlsx.py TestCase.xlsx --out TestCase_fixed.xlsx
```

Script làm thẳng trên XML nên logo, dropdown, công thức giữ nguyên: mọi kiểu ô về Times New Roman 10 (kể cả ô trống, ô trong cụm gộp, kiểu mặc định của cột), ô văn bản bắt đầu bằng `-` `+` `=` `@` được gắn dấu nháy đơn (quotePrefix), mọi chuỗi về dạng dựng sẵn (NFC). Cần thư viện `lxml`.
````

**skill-6 Bước 7, lệnh kiểm Tìm**

````
```
python scripts/tc_check.py TestCase.xlsx
```

Script báo: TC thiếu `UC_ID` · `TVP_ID` trùng · kết quả mong đợi mơ hồ · dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khu vực thiếu nhóm bắt buộc · UC chưa có TC nào · ô sai phông, sai cỡ chữ hoặc dùng màu ngoài bảng màu (mọi sheet).
````

**Thay bằng**

````
```
python scripts/tc_check.py TestCase.xlsx
python scripts/tc_fix_xlsx.py TestCase.xlsx --check
```

`tc_check.py` báo: TC thiếu `UC_ID` · `TVP_ID` trùng · dòng có nội dung mà thiếu `TVP_ID` · cột `No.` không liền mạch từ 1 · ô của TC còn dạng `{{…}}` · kết quả mong đợi mơ hồ · dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khu vực thiếu nhóm bắt buộc · khu vực còn nhóm Kiểm tra dữ liệu (cảnh báo) · UC chưa có TC nào · ô sai phông, sai cỡ chữ hoặc dùng màu ngoài bảng màu · ô bắt đầu bằng `-` `+` `=` `@` mà thiếu dấu nháy đơn · ô có chữ dạng tổ hợp (mọi sheet).

`tc_fix_xlsx.py --check` đọc thẳng XML nên thấy cả những ô openpyxl không đọc được kiểu: ô nằm trong cụm gộp và kiểu mặc định của cột. Hai lệnh cùng sạch mới coi là qua.
````

**skill-7 changelog Tìm**

````
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.3 | 2026-10-05 |
````

**Thay bằng**

````
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.4 | 2026-10-07 | Bước 4: kết quả kiểm ở nơi hành động trả về; nơi khác trong cùng sheet kiểm ở khu vực của nó; điểm hiển thị suy ra thì không khẳng định. Bước 5: case bấm nút gửi mà không lưu được vào nhóm Không thành công, nhóm này đứng trước Thành công; bỏ `{{…}}`, dùng giá trị cụ thể hoặc `[tên]`; giá trị tính toán có nhóm TC riêng. Bước 6: thêm `tc_fix_xlsx.py` để đưa file có sẵn về một phông, thêm dấu nháy đơn đầu ô, chuẩn hoá dạng chữ. Bước 7: kiểm bằng cả `tc_check.py` và `tc_fix_xlsx.py --check`. `tc_check.py`: thêm kiểm `{{…}}`, dòng thiếu `TVP_ID`, cột `No.`, dấu nháy đơn, chữ dạng tổ hợp, ô trống đã định dạng; so tên nhóm sau khi chuẩn hoá NFC. `references/format.md` §4, §7 và `references/patterns.md` P1, P7, P12 sửa theo. Theo góp ý của Hanna ngày 06/10, 07/10 — **chờ duyệt**. | FB-042 · FB-043 · FB-044 · FB-045 · FB-046 · FB-048 · FB-049 · FB-016 |
| v0.3 | 2026-10-05 |
````

## 4. `.claude/skills/tc-authoring/references/format.md`

**format-1 phông cho mọi ô Tìm**

````
- **Times New Roman, cỡ 10** cho toàn bộ vùng dữ liệu.
- **Căn lề trái** cho mọi ô.
````

**Thay bằng**

````
- **Times New Roman, cỡ 10** cho mọi ô của mọi sheet: ô có chữ, ô trống đã kẻ khung, ô nằm trong cụm gộp, và kiểu mặc định của cột.
- **Căn lề trái** cho mọi ô.
````

**format-2 dấu nháy đơn, dạng chữ, kiểu Normal Tìm**

````
- `tc_check.py` kiểm phông, cỡ chữ, màu nền, màu chữ của mọi ô có nội dung và báo lỗi theo từng sheet.
````

**Thay bằng**

````
- `tc_check.py` kiểm phông, cỡ chữ, màu nền, màu chữ của mọi ô đã định dạng và báo lỗi theo từng sheet; ô nằm trong cụm gộp và kiểu mặc định của cột do `tc_fix_xlsx.py --check` kiểm (đọc thẳng XML).
- **Dấu nháy đơn đầu ô.** Ô văn bản bắt đầu bằng `-`, `+`, `=` hoặc `@` phải có thuộc tính quotePrefix của kiểu ô (trong Excel thấy dấu `'` ở đầu ô trên thanh công thức). Thiếu thì khi sửa ô, Excel hiểu nội dung là công thức. Script đặt thuộc tính này; không gõ ký tự `'` vào nội dung (`rules/tc-authoring.md` rule 32).
- **Dạng chữ.** Mọi chuỗi lưu ở dạng dựng sẵn (NFC). Chữ gõ ở dạng tổ hợp nhìn giống hệt nhưng script coi là chuỗi khác (rule 33).
- **Kiểu Normal của file giữ nguyên** như file TC mẫu (Arial 10): Excel tính độ rộng cột theo phông của kiểu Normal, đổi là lệch độ rộng mọi cột. Vì vậy không dùng "Clear Formats" trên file TC — ô sẽ về kiểu Normal; cần xoá định dạng thì chạy lại `tc_fix_xlsx.py`.
````

**format-3 nhóm Kiểm tra dữ liệu Tìm**

````
| Kiểm tra dữ liệu | Validation |
````

**Thay bằng**

````
| Kiểm tra dữ liệu | Validation — chỉ cho kiểm tra hiện ra ngay khi nhập, chưa bấm nút gửi; case bấm nút gửi mà không lưu được thuộc nhóm Không thành công (`rules/tc-authoring.md` rule 8) |
````

## 5. `.claude/skills/tc-authoring/references/patterns.md`

**patterns-1 P1 Tìm**

````
3. Để trống rồi bấm nút đồng ý — không gọi hành động, hiện lỗi **tại ô đó**
4. Nhập hợp lệ rồi đồng ý — đóng popup, quay về màn trước, giá trị mới hiển thị đúng
   (với popup tạo mới: thêm TC theo rule 30 — mỗi loại một TC, nhập đủ mọi trường, kiểm từng thông tin hiển thị ở danh sách và chi tiết)
````

**Thay bằng**

````
3. Để trống rồi bấm nút đồng ý — không gọi hành động, hiện lỗi **tại ô đó** (nhóm Không thành công, cùng case huỷ: `rules/tc-authoring.md` rule 8)
4. Nhập hợp lệ rồi đồng ý — đóng popup, quay về màn trước, giá trị mới hiển thị đúng
   (với popup tạo mới: thêm TC theo rule 30 — mỗi loại đúng một TC, nhập đủ mọi trường, kiểm từng thông tin ở nơi hành động trả về; màn chi tiết kiểm ở khu vực của màn chi tiết, rule 9)
````

**patterns-2 P7 Tìm**

````
Bắt buộc (rule 30): **mỗi loại tạo một TC**, nhập đủ mọi trường của form (kể cả trường optional), tạo xong mở nơi hiển thị rồi kiểm từng thông tin đúng giá trị đã nhập; danh sách và màn chi tiết là hai TC riêng.
````

**Thay bằng**

````
Bắt buộc (rule 30): **mỗi loại tạo đúng một TC**, nhập đủ mọi trường của form (kể cả trường optional), tạo xong kiểm từng thông tin đúng giá trị đã nhập ở nơi hành động trả về (vd danh sách). Màn chi tiết kiểm ở khu vực của màn chi tiết, mỗi loại một TC, không lặp ở khu vực tạo (rule 9).
````

**patterns-3 P12, giá trị tính toán Tìm**

````
Bắt buộc thêm: tên dài tối đa và chuỗi không có khoảng trắng (breadcrumb, ô bảng, tiêu đề, thông báo), bấm vào từng tên ở mọi độ sâu. Chi tiết: `technical-risk-checklist.md` mục B, C.
````

**Thay bằng**

````
Bắt buộc thêm: tên dài tối đa và chuỗi không có khoảng trắng (breadcrumb, ô bảng, tiêu đề, thông báo), bấm vào từng tên ở mọi độ sâu. Chi tiết: `technical-risk-checklist.md` mục B, C.

Bắt buộc thêm, khi bảng có **cột giá trị tính toán** (tỉ lệ, tổng, số đếm; `rules/tc-authoring.md` rule 31): một nhóm TC với bộ số cụ thể — nhiều thành phần · một thành phần · 0% · 100% · kết quả phải làm tròn lên · kết quả phải làm tròn xuống; và các biên chưa có căn cứ, để trống Expected kèm câu hỏi — phần thập phân đúng bằng .5 · trên 0% mà dưới 1% · trên 99% mà chưa đủ · chưa có thành phần nào.
````

## 6. `CLAUDE.md`

**claude-1 cổng bước 5 Tìm**

````
| 5 File TC Excel | `tc-authoring` | `tc_check.py` sạch |
````

**Thay bằng**

````
| 5 File TC Excel | `tc-authoring` | `tc_check.py` và `tc_fix_xlsx.py --check` sạch |
````

**claude-2 lệnh script Tìm**

````
    python .claude/skills/tc-authoring/scripts/tc_check.py projects/<p>/exports/<file>.xlsx
````

**Thay bằng**

````
    python .claude/skills/tc-authoring/scripts/tc_check.py projects/<p>/exports/<file>.xlsx
    python .claude/skills/tc-authoring/scripts/tc_fix_xlsx.py projects/<p>/exports/<file>.xlsx --check        # phông, dấu nháy đơn đầu ô, dạng chữ; bỏ --check, thêm --out <file mới> để sửa
````

## 7. `README.md`

**readme-1 thành phần Tìm**

````
- `_cu/`: các file bản dựng đầu (02/10 sáng) đã bị thay thế và bản skill BA lấy từ chat Analysis. Xoá được khi không cần đối chiếu nữa.
````

**Thay bằng**

````
- Cập nhật 07/10/2026: `rules/tc-authoring.md` v0.5 và `tc-authoring` v0.4 (chờ duyệt) theo góp ý FB-042 → FB-049 — case không lưu được vào nhóm Không thành công, kết quả kiểm ở nơi hành động trả về, bỏ `{{…}}` dùng `[tên]`, giá trị tính toán có nhóm TC riêng, mọi ô Times New Roman 10, dấu nháy đơn đầu ô. Script mới `tc_fix_xlsx.py` đưa một file TC có sẵn về đúng định dạng.
- `_cu/`: các file bản dựng đầu (02/10 sáng) đã bị thay thế và bản skill BA lấy từ chat Analysis. Xoá được khi không cần đối chiếu nữa.
````

**readme-2 thư viện Tìm**

````
- Máy cần Python có `openpyxl` và `lxml` cho các script Excel (`lxml` dùng cho `tc_add_sheet.py`, `tc_restyle.py`).
````

**Thay bằng**

````
- Máy cần Python có `openpyxl` và `lxml` cho các script Excel (`lxml` dùng cho `tc_fix_xlsx.py`, `tc_add_sheet.py`, `tc_restyle.py`).
````
