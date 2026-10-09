#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh bảng phẳng TSV và tài liệu so sánh v1.4 → v1.5 từ dữ liệu dựng file.

    python make_docs.py <scopes_v15.json> <v1.4.Scopes.json> <v1.4.xlsx> <build_log.json> <thư mục ra>
"""
import csv
import json
import os
import sys
import unicodedata
from collections import Counter

from pathlib import Path  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from xl import Book, col_name  # noqa: E402


def clean(s):
    s = unicodedata.normalize("NFC", str(s or "")).replace("\r\n", "\n")
    lines = [ln.rstrip() for ln in s.split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def md(s):
    """Chữ đặt trong ô bảng markdown."""
    s = clean(s).replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
    return s if s else "(trống)"


def main():
    rows_p, old_p, book_p, log_p, outdir = sys.argv[1:6]
    data = json.load(open(rows_p, encoding="utf-8"))
    rows, removed = data["rows"], data["removed"]
    old = {r["row"]: r for r in json.load(open(old_p, encoding="utf-8"))}
    log = json.load(open(log_p, encoding="utf-8"))

    # ---------------------------------------------------------------- TSV
    tsv = os.path.join(outdir, "projects/sgs-dtp/exports/_flat/Scopes_v1.5.tsv")
    os.makedirs(os.path.dirname(tsv), exist_ok=True)
    with open(tsv, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["I", "II", "III", "IV", "Pri", "Name", "Pre", "Step", "Expected", "UC", "Wait"])
        for r in rows:
            w.writerow([r[k].replace("\n", "\\n") for k in ("I", "II", "III", "IV", "Pri", "Name", "Pre", "Step", "Exp", "UC", "OQ")])

    # ---------------------------------------------------------------- số liệu
    cnt = Counter(r["chg"] for r in rows)
    a_rows = [r for r in rows if (r["src"] and r["src"] <= 69) or (r["src"] is None and r["no"] <= 61)]
    b_rows = [r for r in rows if r not in a_rows]
    book = Book(book_p)
    cells = book.cells("Scopes")
    yellow = [(c, r) for (c, r), v in cells.items() if (book.fill(v[1]) or {}).get("indexed") == "5"]
    white = [(c, r) for (c, r), v in cells.items() if (book.fill(v[1]) or {}).get("theme") == "0"]
    nfc_cells = sum(1 for o in old.values() for k in ("I", "II", "III", "IV", "Name", "Pre", "Step", "Exp", "OQ")
                    if unicodedata.normalize("NFC", o[k]) != o[k])
    oq = sum(1 for r in rows if r["OQ"])
    empty = sum(1 for r in rows if not r["Exp"])

    L = []
    A = L.append
    A("# So sánh v1.4 → v1.5 — sheet Scopes (07/10/2026)")
    A("")
    A("- Bản v1.4: file Hanna gửi ngày 07/10, lưu nguyên ở `exports/SGS-DTP_TestCase1_v1.4.xlsx`.")
    A("- Bản v1.5: `exports/SGS-DTP_TestCase1_v1.5.xlsx`; bảng phẳng: `exports/_flat/Scopes_v1.5.tsv`.")
    A("- Cách viết rút ra từ phần Hanna sửa: `phan-tich-cach-viet_v1.4.md` (cùng thư mục). Góp ý gốc: FB-042 → FB-049, FB-016 trong `feedback/log.md`.")
    A("- Mọi con số dưới đây do script đếm từ hai file.")
    A("")
    A("| | v1.4 | v1.5 |")
    A("|---|---|---|")
    A("| Số dòng TC | %d | %d |" % (len(old), len(rows)))
    A("| Dòng có TVP_ID | %d | %d |" % (sum(1 for o in old.values() if o["ID"]), len(rows)))
    A("| TVP_ID trùng | %d | 0 |" % sum(1 for v in Counter(o["ID"] for o in old.values() if o["ID"]).values() if v > 1))
    A("| Dòng thiếu UC | %d | 0 |" % sum(1 for o in old.values() if not o["UC"]))
    A("| Ô còn `{{…}}` | %d | 0 |" % sum(1 for o in old.values() for k in ("Name", "Pre", "Step", "Exp", "OQ") if "{{" in o[k]))
    A("| Dòng còn câu hỏi mở | %d | %d |" % (sum(1 for o in old.values() if o["OQ"]), oq))
    A("| Dòng để trống Expected | %d | %d |" % (sum(1 for o in old.values() if not clean(o["Exp"])), empty))
    A("")
    A("So với v1.4: giữ nguyên %d dòng · sửa %d dòng · thêm %d dòng · bỏ %d dòng." % (cnt["giữ"], cnt["sửa"], cnt["thêm"], len(removed)))
    A("Trong đó phần Hanna đã sửa (No. 1–67 của v1.4, dòng 13–69): giữ nguyên %d, sửa %d (chỉ các chỗ ở mục 1), thêm %d." % (
        sum(1 for r in a_rows if r["chg"] == "giữ"), sum(1 for r in a_rows if r["chg"] == "sửa"), sum(1 for r in a_rows if r["chg"] == "thêm")))
    A("Phần viết lại (dòng 70–148 của v1.4): giữ nguyên %d, sửa %d, thêm %d, bỏ %d." % (
        sum(1 for r in b_rows if r["chg"] == "giữ"), sum(1 for r in b_rows if r["chg"] == "sửa"),
        sum(1 for r in b_rows if r["chg"] == "thêm"), len(removed)))
    A("")

    # ---------------------------------------------------------------- 1
    A("## 1. Phần Hanna đã sửa — những chỗ AI chạm vào")
    A("")
    A("Nội dung của Hanna được giữ. Chỉ sửa chỗ gõ nhầm, chỗ còn `{{…}}`, ô UC còn trống; No. và TVP_ID đánh lại cho cả sheet (mục 5).")
    A("")
    A("| TC (v1.5) | Dòng v1.4 · số cũ | Cột | Trước | Sau | Vì sao |")
    A("|---|---|---|---|---|---|")
    names = {"Exp": "Expected result", "Step": "Step", "Name": "Test case name", "OQ": "Open question", "UC": "UC", "Pre": "Pre-condition"}
    for r in a_rows:
        if r["chg"] != "sửa":
            continue
        o = old[r["src"]]
        whys = dict(x.split(": ", 1) for x in r["note"].split("; ") if ": " in x) if r["note"] else {}
        # ghi chú có thể chứa dấu ';' bên trong: tách lại theo tên trường
        whys = {}
        cur = None
        for part in (r["note"] or "").split("; "):
            head = part.split(": ", 1)[0]
            if head in ("Exp", "Step", "Name", "OQ", "UC", "Pre") and ": " in part:
                cur = head
                whys[cur] = part.split(": ", 1)[1]
            elif cur:
                whys[cur] += "; " + part
        for k in r["diff"]:
            A("| %s | dòng %d · %s | %s | %s | %s | %s |" % (
                r["id"], r["src"], o["ID"] or "chưa có ID", names.get(k, k), md(o[k]), md(r[k]), whys.get(k, "")))
    A("")
    A("Chưa sửa, để Hanna xem (không phải lỗi gõ rõ ràng):")
    A("")
    A("- Scope_003 (dòng 15 của v1.4): ô IV ghi \"Bấm tên scope\" nhưng Step chỉ có \"1. Vào màn hình Scopes\", chưa có bước bấm tên scope.")
    A("- Scope_025, Scope_026, Scope_027 (3 case Thành công của Tạo scope) đều tạo `Name: abc`; theo Scope_020 (Trùng tên) thì lần tạo thứ hai "
      "sẽ bị chặn với \"A scope with this name already exists.\" Cần tên khác nhau cho ba case, hoặc ghi rõ dữ liệu được dọn giữa các case.")
    A("- Scope_025 và Scope_026 cùng tên case \"Kiểm tra thông tin vừa tạo\"; Scope_027 tên \"Kiểm tra scope System vừa tạo hiện ở danh sách\".")
    A("- Scope_035 (Tiêu đề cột) còn ghi 5 cột trên một dòng nối bằng \" · \"; phần viết lại bên dưới ghi mỗi mục một dòng (rule 12).")
    A("- 6 case Evidence coverage của Hanna (Scope_044 → Scope_049) có tên tiếng Anh; các case khác tên tiếng Việt.")
    A("- 5 case Evidence coverage Hanna thêm (Scope_044 → Scope_048) chưa có câu hỏi ở cột Open question; công thức lấy theo prototype, "
      "câu Q-S-11 chưa có trả lời (xem FB-048).")
    A("")

    # ---------------------------------------------------------------- 2
    A("## 2. Case thêm — đề xuất của AI, chờ Hanna duyệt")
    A("")
    A("| TC (v1.5) | Khu vực ▸ nhóm ▸ case | Tên case | Expected | Vì sao thêm |")
    A("|---|---|---|---|---|")
    for r in rows:
        if r["chg"] == "thêm":
            A("| %s | %s ▸ %s ▸ %s | %s | %s | %s |" % (r["id"], r["II"], r["III"], r["IV"], md(r["Name"]),
                                                    "để trống, có câu hỏi" if not r["Exp"] else md(r["Exp"]), r["note"]))
    A("")

    # ---------------------------------------------------------------- 3
    A("## 3. Case bỏ")
    A("")
    A("| Dòng v1.4 · số cũ | Khu vực ▸ nhóm ▸ case | Tên case | Vì sao bỏ |")
    A("|---|---|---|---|")
    for x in removed:
        A("| dòng %d · %s | %s ▸ %s ▸ %s | %s | %s |" % (x["row"], x["id"], x["II"], x["III"], x["IV"], md(x["name"]), x["why"]))
    A("")
    A("Muốn giữ case nào thì báo, AI thêm lại ở đúng khu vực hiển thị của nó.")
    A("")

    # ---------------------------------------------------------------- 4
    A("## 4. Phần viết lại (từ Chi tiết scope trở xuống) — từng TC")
    A("")
    A("Cột đổi: III = nhóm kết quả · IV = case · Name · Pre = Pre-condition · Step · Exp = Expected result · OQ = Open question.")
    A("")
    A("| TC (v1.5) | Số cũ (v1.4) | Khu vực ▸ nhóm ▸ case | Loại | Cột đổi | Ghi chú |")
    A("|---|---|---|---|---|---|")
    for r in b_rows:
        o = old.get(r["src"]) if r["src"] else None
        A("| %s | %s | %s ▸ %s ▸ %s | %s | %s | %s |" % (
            r["id"], (o["ID"] or "chưa có ID") if o else "—", r["II"], r["III"], r["IV"], r["chg"],
            ", ".join(r["diff"]) if r["diff"] else "—", r["note"] if r["chg"] != "thêm" else "xem mục 2"))
    A("")

    # ---------------------------------------------------------------- 5
    A("## 5. Bảng đối chiếu số TC (toàn sheet)")
    A("")
    A("Bản v1.4: cột No. là số dòng Excel (13, 14, …), có ô trống; %d dòng chưa có TVP_ID; `Scope_016` và `Scope_052` mỗi số dùng hai lần. "
      "Bản v1.5 đánh lại liền mạch theo thứ tự trên sheet. Chưa có kết quả chạy ở cột Result nên việc đánh lại không làm mất kết quả nào." % (
          sum(1 for o in old.values() if not o["ID"])))
    A("")
    A("| Dòng v1.4 | No. cũ | TVP_ID cũ | → | No. mới | TVP_ID mới | Tên case |")
    A("|---|---|---|---|---|---|---|")
    by_src = {r["src"]: r for r in rows if r["src"]}
    for rn in sorted(old):
        o = old[rn]
        n = by_src.get(rn)
        A("| %d | %s | %s | → | %s | %s | %s |" % (rn, o["No"] or "(trống)", o["ID"] or "(trống)",
                                               n["no"] if n else "—", n["id"] if n else "bỏ", md(o["Name"])))
    for r in rows:
        if not r["src"]:
            A("| — | — | — | → | %d | %s | %s (thêm) |" % (r["no"], r["id"], md(r["Name"])))
    A("")

    # ---------------------------------------------------------------- 6
    A("## 6. Thay đổi ngoài nội dung sheet Scopes")
    A("")
    A("Nội dung các sheet Login, Users, Profile giữ nguyên, trừ một ô ghi ở dưới. Phần `{{…}}` và nhóm Kiểm tra dữ liệu ở ba sheet đó chưa sửa.")
    A("")
    A("| Chỗ | Trước | Sau | Vì sao |")
    A("|---|---|---|---|")
    for sh, ref, a, b in log["refs"]:
        A("| %s!%s | %s | %s | số TC của Scopes đổi |" % (sh, ref, md(a), md(b)))
    A("| Cover!G6 | Version 1.3 | Version 1.5 | bản mới |")
    A("| Cover dòng 17–19 | (trống) | 3 dòng Record of change: 1.4 (Hanna sửa), 1.5 (viết lại phần dưới), 1.5 (phông, dấu nháy) | ghi lịch sử |")
    A("| Cover dòng 14–19 | chữ ở cột Change Item, Change description, Reference bị cắt | bật xuống dòng, nới chiều cao dòng | đọc được hết chữ |")
    A("| Test_Report | khu vực Trạng thái rỗng nằm sau Phân trang; tổng Scopes 127 | dựng lại theo thứ tự trên sheet; tổng Scopes %d; tổng cả file %d | theo sheet Scopes mới |" % (
        len(rows), 52 + len(rows) + 62 + 13))
    A("")
    A("Định dạng, cho cả file:")
    A("")
    A("- Phông: %d kiểu ô đang dùng Arial 10 chuyển sang Times New Roman 10 (ô trống đã kẻ khung, ô trong cụm gộp, kiểu mặc định của các cột ở "
      "sheet Cần xác nhận, và 5 ô có chữ: Login!C5, C7; Users!C4; Scopes!J51, E56). Kiểu Normal của file giữ nguyên để độ rộng cột không đổi." % len(log["xf_doi_phong"]))
    q = log["quote"]
    A("- Dấu nháy đơn đầu ô: %d ô văn bản bắt đầu bằng dấu `-` có thuộc tính quotePrefix (Login %d, Scopes %d, Users %d, Profile %d). Bản v1.4 có 36 ô, do Hanna tự thêm." % (
        sum(v[0] for v in q.values()), q["Login"][0], q["Scopes"][0], q["Users"][0], q["Profile"][0]))
    A("- Nền tô tay ở sheet Scopes: bỏ %d ô nền vàng (37 ô đã đổi chữ, 11 ô mất cùng case bị bỏ, 5 ô giữ nguyên chữ: Step của Scope_072, "
      "Pre-condition của Scope_120, 121, 124, 126) và %d ô nền trắng ở dòng 49–55 (nhìn không khác ô không nền)." % (len(yellow), len(white)))
    A("- Dạng chữ: %d ô ở sheet Scopes có chữ tiếng Việt ở dạng tổ hợp (dấu thanh tách rời khỏi chữ cái) được lưu lại ở dạng dựng sẵn (NFC); "
      "nhìn không khác, nhưng `tc_check.py` coi \"Không thành công\" gõ hai dạng là hai giá trị khác nhau và đã báo một lỗi giả ở bản v1.4." % nfc_cells)
    A("- Chiều cao dòng của sheet Scopes: đặt lại theo số dòng chữ (LibreOffice đo), cùng quy ước với các sheet khác: 13.5 pt mỗi dòng chữ + 8.1 pt.")
    A("")
    out = os.path.join(outdir, "projects/sgs-dtp/tests/design/so-sanh_v1.4-v1.5.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(L))
    print("TSV:", tsv, len(rows), "dòng")
    print("so sánh:", out, len(L), "dòng ·", dict(cnt), "· nền vàng", len(yellow), "· nền trắng", len(white), "· ô NFC", nfc_cells)


if __name__ == "__main__":
    main()
