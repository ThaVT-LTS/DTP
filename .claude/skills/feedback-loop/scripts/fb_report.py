#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra sổ ghi nhớ góp ý (feedback/log.md) và sinh feedback/report.md.

Dùng:
    python fb_report.py --log feedback/log.md --repo . --out feedback/report.md

Script báo lỗi (mã thoát 1) khi:
  - bản ghi thiếu trường bắt buộc, hoặc Loại / Trạng thái / Gate không hợp lệ;
  - ID trùng, hoặc bảng tra nhanh đầu file lệch với các bản ghi;
  - FB ở trạng thái từ "Đã vào rule (chờ duyệt)" trở lên mà không changelog nào
    trong repo trỏ tới FB-nnn (tức là chưa thật sự vào rule);
  - FB loại L2-L5 đã xử lý mà thiếu "Phạm vi ảnh hưởng" (chưa quét tổng quát hoá);
  - FB có Tái phát >= 2 mà Gate chưa lên mức 3.

Cảnh báo (không làm mã thoát khác 0): FB đứng ở "Mới" quá --stale-days ngày,
FB "Đã duyệt" chưa có gate.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

LOAI = {
    "L1-sản phẩm", "L2-rule", "L3-checklist", "L4-mẫu",
    "L5-script", "L6-tri thức", "L7-trình bày",
}
LOAI_CAN_QUET = {"L2-rule", "L3-checklist", "L4-mẫu", "L5-script"}

TRANG_THAI_THU_TU = [
    "Mới",
    "Chưa rõ phạm vi",
    "Đã sửa sản phẩm",
    "Đã vào rule (chờ duyệt)",
    "Đã duyệt",
    "Đã có gate",
    "Bị bác",
]
# Từ mức này trở lên thì changelog trong repo phải trỏ tới FB-nnn.
CAN_CHANGELOG = {"Đã vào rule (chờ duyệt)", "Đã duyệt", "Đã có gate"}
DA_XU_LY = {"Đã sửa sản phẩm", "Đã vào rule (chờ duyệt)", "Đã duyệt", "Đã có gate"}
KHONG_CAN_NAP = {"Đã có gate", "Bị bác"}

BAT_BUOC = ["Ngày", "Nguồn", "Loại", "Địa chỉ", "Tiêu chí kiểm", "Trạng thái", "Tái phát"]

RE_HEADING = re.compile(r"^##\s+(FB-\d+)\s*(?:·\s*(.*))?$")
RE_FIELD = re.compile(r"^-\s*([^:]{1,30}?)\s*:\s*(.*)$")
RE_ROW = re.compile(r"^\|\s*(FB-\d+)\s*\|")
RE_GATE = re.compile(r"^(chưa có|mức\s*[123])\b")


class FB:
    def __init__(self, fid: str, title: str, line: int):
        self.id = fid
        self.title = (title or "").strip()
        self.line = line
        self.fields: dict[str, str] = {}
        self.updates: list[str] = []

    @property
    def loai(self) -> str:
        return self.fields.get("Loại", "")

    @property
    def trang_thai(self) -> str:
        return self.fields.get("Trạng thái", "")

    @property
    def gate(self) -> str:
        return self.fields.get("Gate", "chưa có").strip() or "chưa có"

    @property
    def tai_phat(self) -> int:
        raw = self.fields.get("Tái phát", "0")
        m = re.search(r"\d+", raw)
        return int(m.group()) if m else 0

    @property
    def gate_muc(self) -> int:
        m = re.search(r"mức\s*([123])", self.gate)
        return int(m.group(1)) if m else 0


def parse_log(path: Path) -> tuple[list[FB], list[str], list[str]]:
    """Trả về (danh sách FB, ID trong bảng tra nhanh, lỗi cú pháp)."""
    loi: list[str] = []
    items: list[FB] = []
    bang: list[str] = []
    cur: FB | None = None
    in_body = False

    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.rstrip()
        m = RE_HEADING.match(line)
        if m:
            cur = FB(m.group(1), m.group(2) or "", i)
            items.append(cur)
            in_body = True
            continue
        if line.startswith("## ") or line.startswith("# "):
            cur, in_body = None, False
            continue
        if not in_body:
            m = RE_ROW.match(line)
            if m:
                bang.append(m.group(1))
            continue
        if cur is None:
            continue
        m = RE_FIELD.match(line)
        if m:
            key, val = m.group(1).strip(), m.group(2).strip()
            if key == "Cập nhật":
                cur.updates.append(val)
            elif key in cur.fields:
                loi.append(f"{path.name}:{i} · {cur.id} lặp trường '{key}'")
            else:
                cur.fields[key] = val
    return items, bang, loi


def quet_changelog(repo: Path) -> set[str]:
    """Mọi FB-nnn được trích dẫn trong rule/skill (trừ chính thư mục feedback)."""
    found: set[str] = set()
    for p in repo.rglob("*.md"):
        parts = set(p.parts)
        if "feedback" in parts or ".git" in parts:
            continue
        try:
            txt = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        found.update(re.findall(r"FB-\d+", txt))
    for p in repo.rglob("*.py"):
        if "feedback" in set(p.parts):
            continue
        try:
            found.update(re.findall(r"FB-\d+", p.read_text(encoding="utf-8")))
        except (OSError, UnicodeDecodeError):
            continue
    return found


def kiem_tra(items: list[FB], bang: list[str], cited: set[str],
             stale_days: int) -> tuple[list[str], list[str]]:
    loi: list[str] = []
    canh_bao: list[str] = []
    today = dt.date.today()

    seen: set[str] = set()
    for fb in items:
        if fb.id in seen:
            loi.append(f"dòng {fb.line} · {fb.id} trùng ID")
        seen.add(fb.id)

        for k in BAT_BUOC:
            if not fb.fields.get(k):
                loi.append(f"{fb.id} · thiếu trường bắt buộc '{k}'")

        if fb.loai and fb.loai not in LOAI:
            loi.append(f"{fb.id} · Loại không hợp lệ: '{fb.loai}'")
        if fb.trang_thai and fb.trang_thai not in TRANG_THAI_THU_TU:
            loi.append(f"{fb.id} · Trạng thái không hợp lệ: '{fb.trang_thai}'")
        if "Gate" in fb.fields and not RE_GATE.match(fb.gate):
            loi.append(f"{fb.id} · Gate không hợp lệ: '{fb.gate}' "
                       f"(phải là 'chưa có' hoặc 'mức 1|2|3 · ...')")

        if fb.trang_thai in CAN_CHANGELOG and fb.id not in cited:
            loi.append(f"{fb.id} · trạng thái '{fb.trang_thai}' nhưng không "
                       f"changelog nào trong repo trỏ tới {fb.id}")

        if (fb.loai in LOAI_CAN_QUET and fb.trang_thai in DA_XU_LY
                and not fb.fields.get("Phạm vi ảnh hưởng")):
            loi.append(f"{fb.id} · {fb.loai} đã xử lý nhưng thiếu "
                       f"'Phạm vi ảnh hưởng' (chưa quét các chỗ cùng lỗi)")

        if fb.tai_phat >= 2 and fb.gate_muc < 3:
            loi.append(f"{fb.id} · tái phát {fb.tai_phat} lần mà Gate mới ở "
                       f"'{fb.gate}' — phải lên mức 3 (script)")
        elif fb.tai_phat >= 1 and fb.gate_muc < 2:
            canh_bao.append(f"{fb.id} · tái phát {fb.tai_phat} lần, Gate "
                            f"'{fb.gate}' — nên nâng một mức")

        if fb.trang_thai == "Đã duyệt" and fb.gate_muc == 0:
            canh_bao.append(f"{fb.id} · đã duyệt nhưng chưa gắn gate")

        ngay = fb.fields.get("Ngày", "")
        if fb.trang_thai in {"Mới", "Chưa rõ phạm vi"} and re.match(r"\d{4}-\d{2}-\d{2}", ngay):
            tuoi = (today - dt.date.fromisoformat(ngay[:10])).days
            if tuoi > stale_days:
                canh_bao.append(f"{fb.id} · đứng ở '{fb.trang_thai}' {tuoi} ngày")

    if bang:
        ids = [fb.id for fb in items]
        thieu = [i for i in ids if i not in bang]
        thua = [i for i in bang if i not in ids]
        if thieu:
            loi.append("bảng tra nhanh thiếu: " + ", ".join(thieu))
        if thua:
            loi.append("bảng tra nhanh có ID không tồn tại: " + ", ".join(thua))

    return loi, canh_bao


def viet_bao_cao(items: list[FB], loi: list[str], canh_bao: list[str],
                 log_path: Path) -> str:
    can_nap = [fb for fb in items if fb.trang_thai not in KHONG_CAN_NAP]
    cho_duyet = [fb for fb in items if fb.trang_thai == "Đã vào rule (chờ duyệt)"]
    theo_tt: dict[str, int] = {}
    theo_loai: dict[str, int] = {}
    for fb in items:
        theo_tt[fb.trang_thai] = theo_tt.get(fb.trang_thai, 0) + 1
        theo_loai[fb.loai] = theo_loai.get(fb.loai, 0) + 1

    out = [
        "# Báo cáo sổ góp ý",
        "",
        f"Sinh tự động bởi `fb_report.py` — không sửa tay. Nguồn: `{log_path}`. "
        f"Ngày: {dt.date.today().isoformat()}.",
        "",
        f"Tổng: **{len(items)}** bản ghi · lỗi: **{len(loi)}** · cảnh báo: **{len(canh_bao)}**",
        "",
        "## Cần nạp khi bắt đầu task",
        "",
    ]
    if can_nap:
        out += ["| FB | Tiêu đề | Loại | Trạng thái | Gate |", "|---|---|---|---|---|"]
        out += [f"| {fb.id} | {fb.title} | {fb.loai} | {fb.trang_thai} | {fb.gate} |"
                for fb in can_nap]
    else:
        out.append("Không còn FB nào cần nạp — tất cả đã có gate hoặc bị bác.")
    out.append("")

    if cho_duyet:
        out += ["## Chờ người dùng duyệt", ""]
        out += [f"- {fb.id} · {fb.title} ({fb.fields.get('Địa chỉ', '')})" for fb in cho_duyet]
        out.append("")

    out += ["## Thống kê", "", "| Trạng thái | Số lượng |", "|---|---|"]
    out += [f"| {k or '(trống)'} | {v} |" for k, v in sorted(theo_tt.items())]
    out += ["", "| Loại | Số lượng |", "|---|---|"]
    out += [f"| {k or '(trống)'} | {v} |" for k, v in sorted(theo_loai.items())]
    out.append("")

    out += ["## Lỗi", ""]
    out += [f"- {x}" for x in loi] if loi else ["Không có."]
    out += ["", "## Cảnh báo", ""]
    out += [f"- {x}" for x in canh_bao] if canh_bao else ["Không có."]
    out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Kiểm tra sổ góp ý và sinh báo cáo.")
    ap.add_argument("--log", default="feedback/log.md")
    ap.add_argument("--repo", default=".", help="gốc repo để quét changelog trỏ FB-nnn")
    ap.add_argument("--out", default="feedback/report.md")
    ap.add_argument("--stale-days", type=int, default=7)
    args = ap.parse_args()

    log_path = Path(args.log)
    if not log_path.is_file():
        print(f"LỖI: không thấy sổ {log_path}", file=sys.stderr)
        return 2

    items, bang, loi_cu_phap = parse_log(log_path)
    cited = quet_changelog(Path(args.repo))
    loi, canh_bao = kiem_tra(items, bang, cited, args.stale_days)
    loi = loi_cu_phap + loi

    bao_cao = viet_bao_cao(items, loi, canh_bao, log_path)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(bao_cao, encoding="utf-8")

    print(f"{len(items)} bản ghi · {len(loi)} lỗi · {len(canh_bao)} cảnh báo → {out_path}")
    for x in loi:
        print("LỖI: " + x)
    for x in canh_bao:
        print("Cảnh báo: " + x)
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
