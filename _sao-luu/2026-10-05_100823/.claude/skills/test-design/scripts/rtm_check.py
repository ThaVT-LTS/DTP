#!/usr/bin/env python3
"""
Kiểm tra độ phủ (RTM) — test basis + file thiết kế ↔ test case.

Dùng:
  python rtm_check.py --basis docs/test-basis/x.md tests/design/*.md --cases tests/cases/*.md [--out tests/rtm.md]

Báo lỗi (mã thoát 1) khi:
  - ID trong test basis / thiết kế chưa có TC và không có dấu loại trừ
  - business rule (BR) thiếu TC Positive hoặc TC Negative
  - UC thiếu nhóm Redirect / Validation / Function mà không có [KHÔNG ÁP DỤNG: <nhóm>]
  - TC thiếu trường bắt buộc, sai giá trị, trùng ID, trỏ tới ID không tồn tại, tag thiếu, kết quả mơ hồ

Quy ước ID và mẫu TC: xem references/templates.md và SKILL.md của ba-analysis.
"""
import argparse, collections, datetime, re, sys

UC = r"UC-[A-Z]+-\d{3}"
TYPES = "NV|FD|MS|MF|AF|EF|BR|SE|EP|BV|EG|PW"
REQUIRED = ["Nhóm", "Loại", "Ưu tiên", "Kỹ thuật", "Nguồn", "Tiền điều kiện", "Bước", "Mong đợi", "Tag", "Tự động hóa"]
GROUPS = {"Redirect": "R", "Validation": "V", "Function": "F"}
KINDS = {"Positive", "Negative", "Abnormal"}
EXCL = re.compile(r"\[(NGOÀI PHẠM VI|CHỜ Q[^\]]*|THUỘC [^\]]*|KHÔNG ÁP DỤNG[^\]]*)\]")
VAGUE = re.compile(r"hoạt động bình thường|hiển thị đúng|như mong đợi|đúng yêu cầu|đúng như thiết kế|"
                   r"^\s*thành công\.?\s*$|^\s*không (có )?lỗi\.?\s*$|^\s*ok\.?\s*$", re.I)


def build_patterns(uc):
    elem = re.compile(rf"\b(?:{uc}-(?:{TYPES})-\d+|{uc}-DT-\d+-R\d+|ST-[A-Z]+-\d+|PM-[A-Z]+-\d+)\b")
    uc_alone = re.compile(rf"\b({uc})\b(?!-[A-Z])")
    tc_head = re.compile(rf"^#{{3,4}}\s+({uc}-TC-([RVF])\d+)\s*[·:\-–]\s*(.+?)\s*$")
    return elem, uc_alone, tc_head


def kind_of(i):
    m = re.search(rf"-(?:({TYPES})-\d+|DT-\d+-R\d+)$", i)
    if m:
        return m.group(1) or "DT"
    return i.split("-")[0]  # ST / PM


def uc_of(i, uc_re):
    m = re.match(rf"({uc_re})", i)
    return m.group(1) if m else "(dùng chung)"


def parse_basis(files, elem, uc_alone):
    defined, excluded, na_groups, where = {}, {}, collections.defaultdict(set), {}
    for f in files:
        for n, line in enumerate(open(f, encoding="utf-8"), 1):
            ids = elem.findall(line)
            mark = EXCL.search(line)
            for k, i in enumerate(ids):
                where.setdefault(i, f"{f}:{n}")
                defined[i] = True
                if k == 0 and mark:
                    excluded[i] = mark.group(0)
            if mark and "KHÔNG ÁP DỤNG" in mark.group(0):
                for g in GROUPS:
                    if g.lower() in mark.group(0).lower():
                        for u in uc_alone.findall(line):
                            na_groups[u].add(g)
    return set(defined), excluded, na_groups, where


def parse_cases(files, tc_head):
    tcs, issues = [], []
    for f in files:
        cur = None
        for n, line in enumerate(open(f, encoding="utf-8"), 1):
            m = tc_head.match(line.rstrip("\n"))
            if m:
                cur = dict(id=m.group(1), letter=m.group(2), title=m.group(3), file=f, line=n, fields={})
                tcs.append(cur)
                continue
            if re.match(r"^#{1,6}\s", line):
                cur = None
                continue
            if cur is not None:
                fm = re.match(r"^- ([^:]+?):\s*(.*)$", line.rstrip("\n"))
                if fm:
                    cur["fields"][fm.group(1).strip()] = fm.group(2).strip()
    return tcs, issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--basis", nargs="+", required=True, help="test basis + file thiết kế")
    ap.add_argument("--cases", nargs="+", required=True, help="file test case")
    ap.add_argument("--out", help="ghi RTM ra file markdown")
    ap.add_argument("--uc-pattern", default=UC, help=f"regex ID UC (mặc định {UC})")
    a = ap.parse_args()

    elem, uc_alone, tc_head = build_patterns(a.uc_pattern)
    defined, excluded, na_groups, where = parse_basis(a.basis, elem, uc_alone)
    tcs, _ = parse_cases(a.cases, tc_head)

    errors, warnings = [], []
    seen = collections.Counter(t["id"] for t in tcs)
    for i, c in seen.items():
        if c > 1:
            errors.append(f"TC trùng ID: {i} ({c} lần)")

    active = []
    for t in tcs:
        f, tid = t["fields"], t["id"]
        if "deprecated" in f.get("Trạng thái", "").lower():
            continue
        active.append(t)
        for k in REQUIRED:
            if not f.get(k):
                errors.append(f"{tid}: thiếu trường '{k}'")
        g = f.get("Nhóm", "")
        if g and GROUPS.get(g) != t["letter"]:
            errors.append(f"{tid}: Nhóm '{g}' không khớp chữ '{t['letter']}' trong ID")
        if f.get("Loại") and f["Loại"] not in KINDS:
            errors.append(f"{tid}: Loại '{f['Loại']}' phải là Positive / Negative / Abnormal")
        if f.get("Ưu tiên") and f["Ưu tiên"] not in ("P1", "P2", "P3"):
            errors.append(f"{tid}: Ưu tiên '{f['Ưu tiên']}' phải là P1 / P2 / P3")
        src = elem.findall(f.get("Nguồn", ""))
        t["src"] = src
        if f.get("Nguồn") and not src:
            errors.append(f"{tid}: Nguồn không chứa ID hợp lệ")
        for i in src:
            if i not in defined:
                errors.append(f"{tid}: Nguồn trỏ tới {i} — không có trong test basis / thiết kế")
        tag = f.get("Tag", "")
        uc_id = tid.split("-TC-")[0]
        for need in [f"@{uc_id}", f"@{g.lower()}" if g else None,
                     f"@{f.get('Loại', '').lower()}" if f.get("Loại") else None,
                     f"@{f.get('Ưu tiên')}" if f.get("Ưu tiên") else None]:
            if need and not re.search(rf"(?<!\S){re.escape(need)}(?!\S)", tag):
                errors.append(f"{tid}: Tag thiếu {need}")
        for part in re.split(r";", f.get("Mong đợi", "")):
            if part.strip() and VAGUE.search(part.strip()):
                errors.append(f"{tid}: kết quả mong đợi mơ hồ — \"{part.strip()}\"")
                break
        if uc_id not in {uc_of(i, a.uc_pattern) for i in defined}:
            warnings.append(f"{tid}: UC {uc_id} không có ID nào trong test basis / thiết kế")

    cover = collections.defaultdict(list)
    for t in active:
        for i in set(t.get("src", [])):
            cover[i].append(t)
    gaps = sorted(i for i in defined if i not in excluded and not cover.get(i))
    for i in gaps:
        errors.append(f"Lỗ hổng: {i} chưa có TC ({where[i]})")

    br_issue = []
    for i in sorted(defined):
        if kind_of(i) == "BR" and i not in excluded:
            kinds = {t["fields"].get("Loại") for t in cover.get(i, [])}
            miss = [k for k in ("Positive", "Negative") if k not in kinds]
            if miss:
                br_issue.append((i, miss))
                errors.append(f"{i}: thiếu TC {' và '.join(miss)}")

    ucs = sorted({uc_of(i, a.uc_pattern) for i in defined} - {"(dùng chung)"})
    by_uc = collections.defaultdict(collections.Counter)
    for t in active:
        by_uc[t["id"].split("-TC-")[0]][t["letter"]] += 1
    for u in ucs:
        for g, l in GROUPS.items():
            if by_uc[u][l] == 0 and g not in na_groups.get(u, set()):
                errors.append(f"{u}: chưa có TC nhóm {g} (hoặc ghi [KHÔNG ÁP DỤNG: {g} — lý do])")

    # ---------- RTM ----------
    kinds_count = collections.Counter(t["fields"].get("Loại") for t in active)
    grp_count = collections.Counter(t["letter"] for t in active)
    out = [f"# RTM — ma trận truy vết", "",
           f"Sinh bởi `rtm_check.py` lúc {datetime.datetime.now():%Y-%m-%d %H:%M}. Không sửa tay.", "",
           f"Nguồn: {', '.join(a.basis)} · Test case: {', '.join(a.cases)}", "",
           "## Tóm tắt", "", "| Chỉ số | Giá trị |", "|---|---|",
           f"| ID trong test basis + thiết kế | {len(defined)} |",
           f"| Đã có TC | {sum(1 for i in defined if cover.get(i))} |",
           f"| Loại trừ có lý do | {len(excluded)} |",
           f"| Lỗ hổng (chưa có TC) | {len(gaps)} |",
           f"| TC đang dùng | {len(active)} (Redirect {grp_count['R']} · Validation {grp_count['V']} · Function {grp_count['F']}) |",
           f"| Theo loại | Positive {kinds_count['Positive']} · Negative {kinds_count['Negative']} · Abnormal {kinds_count['Abnormal']} |",
           f"| TC deprecated | {len(tcs) - len(active)} |",
           f"| Lỗi | {len(errors)} |",
           f"| Cảnh báo | {len(warnings)} |", ""]
    out += ["## Lỗi", ""] + ([f"- {e}" for e in errors] or ["Không có."]) + [""]
    if warnings:
        out += ["## Cảnh báo", ""] + [f"- {w}" for w in warnings] + [""]
    out += ["## Số TC theo UC", "", "| UC | Redirect | Validation | Function | Tổng |", "|---|---|---|---|---|"]
    for u in ucs:
        c = by_uc[u]
        out.append(f"| {u} | {c['R']} | {c['V']} | {c['F']} | {sum(c.values())} |")
    out += ["", "## Truy vết ID → TC", ""]
    groups = collections.defaultdict(list)
    for i in defined:
        groups[uc_of(i, a.uc_pattern)].append(i)
    order = {k: n for n, k in enumerate(["NV", "FD", "MS", "MF", "AF", "EF", "BR", "SE", "PM", "ST", "EP", "BV", "DT", "PW", "EG"])}
    for u in sorted(groups):
        out += [f"### {u}", "", "| ID | Loại | TC |", "|---|---|---|"]
        for i in sorted(groups[u], key=lambda x: (order.get(kind_of(x), 99), x)):
            if i in excluded:
                cell = f"— {excluded[i]}"
            elif cover.get(i):
                cell = ", ".join(sorted(t["id"].split("-TC-")[1] if t["id"].startswith(u) else t["id"] for t in cover[i]))
            else:
                cell = "**CHƯA CÓ TC**"
            out.append(f"| {i} | {kind_of(i)} | {cell} |")
        out.append("")
    text = "\n".join(out)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text)
    print(f"ID: {len(defined)} · có TC: {sum(1 for i in defined if cover.get(i))} · loại trừ: {len(excluded)} · "
          f"lỗ hổng: {len(gaps)} · TC: {len(active)} · lỗi: {len(errors)} · cảnh báo: {len(warnings)}")
    for e in errors[:50]:
        print("  LỖI", e)
    for w in warnings[:20]:
        print("  CẢNH BÁO", w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
