#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đối soát hai chiều giữa lớp chữ của một PDF (mockup, đặc tả in từ web) và inventory Markdown.

    python pdf_text_coverage.py <file.pdf> <uc-inventory.md> [--also analysis.md questions.md]
                                [--count "✓" --count "–"] [--out coverage.md]

[ĐỀ XUẤT — chờ duyệt] Script do AI viết khi chạy ba-analysis trên mockup PDF, vì extract_uc_list.py
chỉ đọc bảng xlsx. Theo rules/common.md rule 5: việc kiểm được bằng script thì chạy script.

Quy ước trong inventory:
  - Chuỗi nguyên văn đặt trong «…».
  - Mục cho một trang: tiêu đề `### Màn <N>` (N = số trang PDF).
  - Khối dùng chung: tiêu đề `### K<n> · <tên> — áp dụng: tr.1–8, 14, 15`.
  - Chuỗi «…» ở mục khác (danh sách chức năng, ma trận…) và trong file --also chỉ được kiểm chiều xuôi trên toàn PDF.

Kiểm:
  - Chiều ngược (độ phủ): mọi cụm chữ trên trang N nằm trong một chuỗi «…» của mục áp dụng cho trang N.
    Cụm dài ≤ 2 ký tự phải khớp nguyên một từ, không chỉ là chuỗi con.
  - Chiều xuôi: mọi từ của mỗi chuỗi «…» có trên mọi trang mà mục đó áp dụng
    (bắt chép sai dấu, chép thừa, khai sai trang áp dụng). Từ bị xuống dòng trong PDF được ghép lại từ hai từ liền.
  - --count: đếm số cụm chữ đúng bằng chuỗi cho trước trên từng trang — dùng để đếm lại số liệu.
Mã thoát 1 khi còn lỗi.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import pdfplumber

QUOTE = re.compile(r"«([^«»]+)»")
SEC_PAGE = re.compile(r"^###\s+Màn\s+(\d+)\b")
SEC_SHARED = re.compile(r"^###\s+(K\d+)\b.*?áp dụng:\s*tr\.\s*([0-9,\s–\-]+)")
HEADING = re.compile(r"^#{1,6}\s")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def parse_pages(spec: str) -> set[int]:
    pages: set[int] = set()
    for part in re.split(r"[,\s]+", spec.strip()):
        if not part:
            continue
        m = re.match(r"^(\d+)[–\-](\d+)$", part)
        if m:
            pages.update(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.isdigit():
            pages.add(int(part))
    return pages


def pdf_phrases(path: Path) -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            # tách theo cỡ chữ: chữ của menu, bảng nổi không trộn với chữ của danh sách nằm phía sau
            words = page.extract_words(keep_blank_chars=True, x_tolerance=1.5, y_tolerance=2,
                                       extra_attrs=["size"])
            out[i] = [t for t in (norm(w["text"]) for w in words) if t]
    return out


def parse_inventory(path: Path):
    """Trả về: [(tên mục, tập trang | None, [chuỗi])]."""
    sections, cur_name, cur_pages, cur = [], "(đầu file)", None, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if HEADING.match(line):
            sections.append((cur_name, cur_pages, cur))
            cur_name, cur_pages, cur = line.lstrip("#").strip(), None, []
            m = SEC_PAGE.match(line)
            if m:
                cur_pages = {int(m.group(1))}
            m = SEC_SHARED.match(line)
            if m:
                cur_pages = parse_pages(m.group(2))
        cur += [norm(q) for q in QUOTE.findall(line)]
    sections.append((cur_name, cur_pages, cur))
    return [s for s in sections if s[2]]


PUNCT = ".,:;!?()“”\"'"


def bare(t: str) -> str:
    return t.strip(PUNCT)


def token_ok(tok: str, toks: set[str]) -> bool:
    """Từ có trên trang (bỏ dấu câu hai đầu), hoặc ghép được từ hai từ liền (chữ bị xuống dòng)."""
    b = bare(tok)
    if not b or b in toks:
        return True
    return any(b[:i] in toks and b[i:] in toks for i in range(1, len(b)))


def quote_ok(q: str, text: str, toks: set[str]) -> list[str]:
    """Trả về các từ không khớp; rỗng nghĩa là chuỗi «…» có trên trang."""
    if q in text:
        return []
    return [t for t in q.split() if not token_ok(t, toks)]


def main() -> int:
    ap = argparse.ArgumentParser(description="Đối soát hai chiều PDF ↔ inventory.")
    ap.add_argument("pdf")
    ap.add_argument("inventory")
    ap.add_argument("--also", nargs="*", default=[], help="file Markdown khác có trích «…» cần kiểm chiều xuôi")
    ap.add_argument("--count", action="append", default=[], help="chuỗi cần đếm trên từng trang")
    ap.add_argument("--out", help="ghi báo cáo Markdown")
    a = ap.parse_args()

    phrases = pdf_phrases(Path(a.pdf))
    page_toks = {p: {bare(t) for ph in ps for t in ph.split()} for p, ps in phrases.items()}
    page_text = {p: " ".join(ps) for p, ps in phrases.items()}
    all_toks = set().union(*page_toks.values())
    all_text = "\n".join(page_text.values())
    sections = parse_inventory(Path(a.inventory))

    by_page: dict[int, list[str]] = defaultdict(list)
    for _, pages, quotes in sections:
        for p in pages or ():
            by_page[p] += quotes

    errors, report = [], []
    total = covered = 0
    report += ["## Chiều ngược — cụm chữ trong PDF có trong inventory", "",
               "| Trang | Cụm chữ | Có trong inventory | Thiếu |", "|---|---|---|---|"]
    for p in sorted(phrases):
        cands = by_page.get(p, [])
        miss = []
        for ph in phrases[p]:
            if len(ph) <= 2:
                ok = any(ph in c.split() for c in cands)
            else:
                ok = any(ph in c for c in cands)
            total += 1
            covered += ok
            if not ok:
                miss.append(ph)
        for m in miss:
            errors.append(f"tr.{p} · cụm chữ chưa có trong inventory: «{m}»")
        report.append(f"| {p} | {len(phrases[p])} | {len(phrases[p]) - len(miss)} | "
                      f"{', '.join('«' + m + '»' for m in miss) or '—'} |")

    report += ["", "## Chiều xuôi — chuỗi «…» có thật trong PDF", ""]
    n_quotes = 0
    for name, pages, quotes in sections:
        for q in quotes:
            n_quotes += 1
            if pages:
                for p in sorted(pages):
                    bad = quote_ok(q, page_text.get(p, ""), page_toks.get(p, set()))
                    if bad:
                        errors.append(f"{name} · «{q}» · không thấy {bad} ở tr.{p}")
            else:
                bad = quote_ok(q, all_text, all_toks)
                if bad:
                    errors.append(f"{name} · «{q}» · không thấy {bad} trong PDF")
    for extra in a.also:
        for n, line in enumerate(Path(extra).read_text(encoding="utf-8").splitlines(), 1):
            for q in QUOTE.findall(line):
                n_quotes += 1
                bad = quote_ok(norm(q), all_text, all_toks)
                if bad:
                    errors.append(f"{Path(extra).name}:{n} · «{norm(q)}» · không thấy {bad} trong PDF")
    report.append(f"{n_quotes} chuỗi «…» đã kiểm.")

    if a.count:
        report += ["", "## Đếm", "", "| Chuỗi | " + " | ".join(f"tr.{p}" for p in sorted(phrases)) + " |",
                   "|---|" + "---|" * len(phrases)]
        for s in a.count:
            s = norm(s)
            report.append(f"| «{s}» | " + " | ".join(str(phrases[p].count(s)) for p in sorted(phrases)) + " |")

    head = [f"# Đối soát PDF ↔ inventory", "",
            f"Nguồn: `{a.pdf}` ({len(phrases)} trang) · Inventory: `{a.inventory}`", "",
            f"Cụm chữ trong PDF: **{total}** · có trong inventory: **{covered}** · lỗi: **{len(errors)}**", ""]
    text = "\n".join(head + report + ["", "## Lỗi", ""] + ([f"- {e}" for e in errors] or ["Không có."]))
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf-8")
    print(f"{len(phrases)} trang · {total} cụm chữ · phủ {covered}/{total} · {n_quotes} chuỗi «…» · lỗi {len(errors)}")
    for e in errors[:60]:
        print("  LỖI", e)
    if a.count:
        print("\n".join(l for l in report if l.startswith("| «")))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
