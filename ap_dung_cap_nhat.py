#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Áp tài liệu cập nhật (Tìm / Thay bằng) vào thư mục qa-pipeline.

Đặt file này và tài liệu cập nhật vào thư mục qa-pipeline (cùng chỗ với CLAUDE.md), rồi:

    python ap_dung_cap_nhat.py                  # chạy thử: chỉ báo, không sửa gì
    python ap_dung_cap_nhat.py --ap             # áp thật; file cũ sao lưu ở _sao-luu/<ngày giờ>/
    python ap_dung_cap_nhat.py --danh-so 21     # xem trước việc đánh số FB-???[…] từ FB-021
    python ap_dung_cap_nhat.py --danh-so 21 --ap

Tuỳ chọn: --doc <tài liệu> (mặc định: CAP-NHAT_2026-10-05_ban-gop.md cạnh script)
          --repo <thư mục qa-pipeline> (mặc định: thư mục đang đứng)

Mỗi chỗ sửa chỉ được áp khi đoạn Tìm xuất hiện đúng một lần. Chỗ đã áp từ trước thì bỏ qua,
nên chạy lại nhiều lần không sao. Chỗ không khớp thì báo "cần sửa tay", không đụng vào file đó.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
import unicodedata
from pathlib import Path

DOC_DEFAULT = "CAP-NHAT_2026-10-05_ban-gop.md"
FB_NEW = "feedback/fb-moi_2026-10-05.md"
PH = re.compile(r"FB-\?\?\?\[([a-z0-9-]+)\]")
SKIP_DIRS = {"_sao-luu", ".git", "__pycache__", "node_modules"}

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


# ------------------------------------------------------------------ đọc tài liệu
def parse_doc(text: str):
    """Trả về danh sách thao tác: (đường dẫn, nhãn, loại, tìm, thay). Loại: R, A, N."""
    lines = text.split("\n")
    ops, cur, i, pending = [], None, 0, None

    def block(j):
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        m = re.match(r"^(`{3,})(\S*)\s*$", lines[j]) if j < len(lines) else None
        if not m:
            raise SystemExit(f"Tài liệu lỗi: thiếu khung code sau dòng {j}")
        fence, k, buf = m.group(1), j + 1, []
        while k < len(lines) and lines[k] != fence:
            buf.append(lines[k])
            k += 1
        if k >= len(lines):
            raise SystemExit(f"Tài liệu lỗi: khung code mở ở dòng {j + 1} không đóng")
        return "\n".join(buf), k + 1

    while i < len(lines):
        line = lines[i]
        if re.match(r"^`{3,}", line):                      # khung code không gắn nhãn: bỏ qua
            _, i = block(i)
            continue
        h = re.match(r"^## \d+\. `([^`]+)`", line)
        if h:
            cur, i = h.group(1), i + 1
            continue
        if cur and re.match(r"^\*\*(.*) Tìm\*\*$", line):
            label = re.match(r"^\*\*(.*) Tìm\*\*$", line).group(1).rstrip(". ")
            find, i = block(i + 1)
            pending = (label, find)
            continue
        if cur and line.strip() == "**Thay bằng**":
            if pending is None:
                raise SystemExit(f"Tài liệu lỗi: dòng {i + 1} có **Thay bằng** mà không có **Tìm** đi trước")
            rep, i = block(i + 1)
            ops.append((cur, pending[0], "R", pending[1], rep))
            pending = None
            continue
        m = re.match(r"^\*\*(.*) (Thêm vào cuối file|Tạo file mới)\*\*", line) if cur else None
        if m:
            content, i = block(i + 1)
            ops.append((cur, m.group(1).rstrip(". "), "A" if m.group(2).startswith("Thêm") else "N", None, content))
            continue
        i += 1
    if pending:
        raise SystemExit("Tài liệu lỗi: có **Tìm** mà thiếu **Thay bằng**")
    return ops


# ------------------------------------------------------------------ đọc, ghi file giữ nguyên kiểu xuống dòng
class TextFile:
    def __init__(self, path: Path):
        self.path = path
        raw = path.read_bytes()
        self.bom = raw.startswith(b"\xef\xbb\xbf")
        self.crlf = b"\r\n" in raw
        text = raw.decode("utf-8-sig").replace("\r\n", "\n")
        nfc = unicodedata.normalize("NFC", text)
        self.nfc_changed = nfc != text
        self.text = nfc

    def save(self):
        out = self.text.replace("\n", "\r\n") if self.crlf else self.text
        data = out.encode("utf-8")
        self.path.write_bytes((b"\xef\xbb\xbf" if self.bom else b"") + data)


def tolerant(s: str) -> re.Pattern:
    """Biểu thức tìm s, coi FB-???[…] và FB-nnn là như nhau (để nhận ra chỗ đã áp sau khi đánh số)."""
    parts, pos = [], 0
    for m in PH.finditer(s):
        parts.append(re.escape(s[pos:m.start()]))
        parts.append(r"FB-(?:\?\?\?\[" + re.escape(m.group(1)) + r"\]|\d{3})")
        pos = m.end()
    parts.append(re.escape(s[pos:]))
    return re.compile("".join(parts))


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


# ------------------------------------------------------------------ áp tài liệu
def apply_doc(repo: Path, doc: Path, write: bool) -> int:
    ops = parse_doc(doc.read_text(encoding="utf-8"))
    print(f"Tài liệu: {doc.name} · {len(ops)} chỗ sửa · thư mục: {repo}")
    print("Chế độ:", "ÁP THẬT" if write else "CHẠY THỬ (không sửa gì; thêm --ap để áp)")
    files: dict[str, TextFile] = {}
    changed, created, manual = set(), {}, []
    counts = {"OK": 0, "đã áp": 0, "cần sửa tay": 0, "tạo mới": 0}
    log_text = None
    if (repo / "feedback/log.md").exists():
        log_text = TextFile(repo / "feedback/log.md").text

    last_path = None
    for path, label, kind, find, rep in ops:
        if path != last_path:
            print(f"\n{path}")
            last_path = path
        target = repo / path
        rep = nfc(rep)
        if kind == "N":
            if target.exists():
                cur = TextFile(target).text
                if tolerant(rep.rstrip("\n")).fullmatch(cur.rstrip("\n")):
                    status = "đã áp"
                else:
                    status = "cần sửa tay"
                    manual.append((path, label, "file đã có trên máy, không ghi đè; so với nội dung trong tài liệu rồi thêm tay"))
            elif path == FB_NEW and log_text and merged_already(rep, log_text):
                status = "đã áp"
            else:
                status = "tạo mới"
                created[path] = rep.rstrip("\n") + "\n"
            counts[status] += 1
            print(f"  [{status}] {label}")
            continue
        if not target.exists():
            counts["cần sửa tay"] += 1
            manual.append((path, label, "không có file này trên máy"))
            print(f"  [cần sửa tay] {label} — không có file")
            continue
        tf = files.setdefault(path, TextFile(target))
        if kind == "A":
            if tolerant(rep).search(tf.text):
                status = "đã áp"
            else:
                tf.text = tf.text.rstrip("\n") + "\n\n" + rep + "\n"
                changed.add(path)
                status = "OK"
            counts[status] += 1
            print(f"  [{status}] {label}")
            continue
        find = nfc(find)
        n = tf.text.count(find)
        rep_here = bool(tolerant(rep).search(tf.text))
        if find in rep:                               # thay bằng = đoạn tìm + phần thêm
            if rep_here:
                status = "đã áp"
            elif n == 1:
                status = "OK"
            else:
                status = "cần sửa tay"
        else:
            if n == 1:
                status = "OK"
            elif n == 0 and rep_here:
                status = "đã áp"
            else:
                status = "cần sửa tay"
        if status == "OK":
            tf.text = tf.text.replace(find, rep, 1)
            changed.add(path)
        elif status == "cần sửa tay":
            why = "không thấy đoạn Tìm" if n == 0 else f"đoạn Tìm xuất hiện {n} lần"
            manual.append((path, label, why))
        counts[status] += 1
        extra = "" if status != "cần sửa tay" else f" — {manual[-1][2]}"
        print(f"  [{status}] {label}{extra}")

    print("\nTổng:", " · ".join(f"{k} {v}" for k, v in counts.items()))
    nfc_files = [p for p in changed if files[p].nfc_changed]
    if nfc_files:
        print("Lưu ý: các file sau có chữ ở dạng tổ hợp, sẽ được lưu ở dạng dựng sẵn (NFC):", ", ".join(nfc_files))
    if manual:
        print("\nCần sửa tay (tìm theo nhãn trong tài liệu):")
        for path, label, why in manual:
            print(f"  - {path} · {label} · {why}")
    if write and (changed or created):
        backup = backup_dir(repo)
        for path in sorted(changed):
            dst = backup / path
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(repo / path, dst)
            files[path].save()
        for path, content in created.items():
            target = repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        print(f"\nĐã sửa {len(changed)} file, tạo {len(created)} file. Bản cũ ở {backup.relative_to(repo)}")
        print("Bước tiếp: đánh số FB — python ap_dung_cap_nhat.py --danh-so <số tiếp theo>")
    elif not write and (changed or created):
        print("\nChưa sửa gì. Chạy lại với --ap để áp.")
    return 1 if manual else 0


def merged_already(fb_file_text: str, log_text: str) -> bool:
    m = re.search(r"^## FB-\?\?\?\[[a-z0-9-]+\] · (.+)$", fb_file_text, re.M)
    return bool(m) and re.search(r"^## FB-\d+ · " + re.escape(m.group(1)) + r"$", log_text, re.M) is not None


def backup_dir(repo: Path) -> Path:
    d = repo / "_sao-luu" / dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    d.mkdir(parents=True, exist_ok=True)
    return d


# ------------------------------------------------------------------ đánh số FB và gộp vào log.md
def number_fb(repo: Path, doc: Path, start: int, write: bool) -> int:
    log_path = repo / "feedback/log.md"
    log = TextFile(log_path)
    used = [int(x) for x in re.findall(r"^(?:## |\| )FB-(\d+)\b", log.text, re.M)]
    top = max(used) if used else 0
    print(f"feedback/log.md: số FB lớn nhất hiện có là FB-{top:03d}.")
    if start <= top:
        print(f"Không đánh số: FB-{start:03d} đã dùng hoặc nhỏ hơn số đang có. Chọn từ {top + 1} trở lên.")
        return 1
    new_file = repo / FB_NEW
    if not new_file.exists():
        print(f"Không thấy {FB_NEW}. Chạy --ap trước, hoặc FB đã được gộp rồi.")
        return 1
    fb = TextFile(new_file)
    order = []
    for m in PH.finditer(fb.text):
        if m.group(1) not in order:
            order.append(m.group(1))
    mapping = {slug: f"FB-{start + i:03d}" for i, slug in enumerate(order)}
    print("Đánh số:")
    for slug, num in mapping.items():
        title = re.search(r"^## FB-\?\?\?\[" + re.escape(slug) + r"\] · (.+)$", fb.text, re.M)
        print(f"  {num}  {title.group(1) if title else slug}")

    skip = {doc.resolve(), Path(__file__).resolve()}
    touched: dict[Path, TextFile] = {}
    for p in repo.rglob("*"):
        if not p.is_file() or p.suffix not in (".md", ".py") or p.resolve() in skip:
            continue
        if SKIP_DIRS & set(p.relative_to(repo).parts):
            continue
        try:
            tf = TextFile(p)
        except UnicodeDecodeError:
            continue
        new = PH.sub(lambda m: mapping.get(m.group(1), m.group(0)), tf.text)
        if new != tf.text:
            tf.text = new
            touched[p] = tf
    left = sorted({m.group(0) for tf in touched.values() for m in PH.finditer(tf.text)})
    print(f"Sẽ đổi số trong {len(touched)} file:", ", ".join(str(p.relative_to(repo)) for p in touched))
    if left:
        print("Còn chỗ chưa có trong bảng FB mới:", ", ".join(left))

    fbt = touched[new_file].text if new_file in touched else fb.text
    rows = re.findall(r"^\| FB-\d{3} \|.*$", fbt, re.M)
    recs = fbt[fbt.index("## Bản ghi") + len("## Bản ghi"):].strip("\n") if "## Bản ghi" in fbt else ""
    ids = re.findall(r"^## (FB-\d{3}) ·", recs, re.M)
    logt = touched[log_path].text if log_path in touched else log.text
    dup = [i for i in ids if re.search(r"^## " + i + r" ·", logt, re.M)]
    if dup:
        print("Không gộp: log.md đã có", ", ".join(dup))
        return 1
    table_rows = list(re.finditer(r"^\| FB-\d+ \|.*$", logt, re.M))
    first_rec = re.search(r"^## FB-\d+ ·", logt, re.M)
    table_rows = [m for m in table_rows if not first_rec or m.start() < first_rec.start()]
    if not table_rows:
        print("Không thấy bảng tra nhanh trong log.md; gộp tay.")
        return 1
    cut = table_rows[-1].end()
    logt = logt[:cut] + "\n" + "\n".join(rows) + logt[cut:]
    logt = logt.rstrip("\n") + "\n\n" + recs + "\n"
    print(f"Gộp vào feedback/log.md: {len(rows)} dòng bảng, {len(ids)} bản ghi ({ids[0]} → {ids[-1]}).")
    if not write:
        print("\nChưa sửa gì. Thêm --ap để đánh số và gộp.")
        return 0
    backup = backup_dir(repo)
    for p, tf in touched.items():
        dst = backup / p.relative_to(repo)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)
        if p != log_path:
            tf.save()
    if log_path not in touched:
        dst = backup / "feedback/log.md"
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(log_path, dst)
        touched[log_path] = log
    touched[log_path].text = logt
    touched[log_path].save()
    moved = backup / (FB_NEW + ".da-gop")
    moved.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(new_file), str(moved))
    print(f"Đã đánh số và gộp. {FB_NEW} đã chuyển vào {moved.relative_to(repo)}. Bản cũ ở {backup.relative_to(repo)}")
    print("Bước tiếp: python .claude/skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Áp tài liệu cập nhật vào thư mục qa-pipeline.")
    ap.add_argument("--doc", help="tài liệu cập nhật (mặc định: " + DOC_DEFAULT + " cạnh script)")
    ap.add_argument("--repo", default=".", help="thư mục qa-pipeline (mặc định: thư mục đang đứng)")
    ap.add_argument("--ap", action="store_true", help="áp thật (mặc định chỉ chạy thử)")
    ap.add_argument("--danh-so", type=int, metavar="N", help="đánh số FB-???[…] từ FB-N và gộp vào feedback/log.md")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    doc = Path(a.doc).resolve() if a.doc else Path(__file__).resolve().parent / DOC_DEFAULT
    if not (repo / "CLAUDE.md").exists() or not (repo / "rules").is_dir():
        print(f"{repo} không giống thư mục qa-pipeline (thiếu CLAUDE.md hoặc rules/). Dùng --repo để chỉ đúng thư mục.")
        return 2
    if not doc.exists():
        print(f"Không thấy tài liệu {doc}. Dùng --doc để chỉ đúng file.")
        return 2
    if a.danh_so is not None:
        return number_fb(repo, doc, a.danh_so, a.ap)
    return apply_doc(repo, doc, a.ap)


if __name__ == "__main__":
    sys.exit(main())
