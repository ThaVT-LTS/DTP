#!/usr/bin/env python3
"""Cổng máy cho bộ test case. Chỉ dùng thư viện chuẩn.
Dùng:  python scripts/check_tc.py projects/<dự-án> [--automation automation/tests]
Thoát 1 nếu có lỗi."""
import re, sys, pathlib

ENUM = {
    "Type": {"Positive", "Negative", "Abnormal"},
    "Priority": {"High", "Medium", "Low"},
    "Automation": {"Auto-UI", "Auto-API", "Manual"},
    "Status": {"draft", "reviewed", "approved", "blocked"},
}
REQUIRED = ["UC", "BR", "Flow", "Type", "Technique", "Priority", "Automation", "Status", "Pre-condition"]
BR_RE = re.compile(r"\bBR-[A-Za-z0-9-]+")


def parse_tcs(path):
    tcs, cur, section = [], None, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip(), "file": path.name,
                   "fields": {}, "Steps": [], "Expected": []}
            tcs.append(cur); section = None; continue
        if cur is None:
            continue
        if line.startswith("### "):
            section = line[4:].strip(); continue
        if section in ("Steps", "Expected"):
            if line.strip():
                cur[section].append(line.strip())
            continue
        m = re.match(r"^-\s+([A-Za-z-]+):\s*(.*)$", line)
        if m:
            cur["fields"][m.group(1)] = m.group(2).strip()
    return tcs


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); return 2
    proj = pathlib.Path(args[0])
    auto = pathlib.Path(args[args.index("--automation") + 1]) if "--automation" in args else None
    errs, warns, seen, br_covered, all_tcs = [], [], {}, set(), []

    ba = {}
    for f in sorted((proj / "docs" / "ba").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        st = re.search(r"^status:\s*(\w+)", text, re.M)
        ba[f.stem] = {"brs": set(BR_RE.findall(text)), "status": st.group(1) if st else "?"}

    for f in sorted((proj / "testcases").glob("*.md")):
        for tc in parse_tcs(f):
            all_tcs.append(tc)
            i, fl = tc["id"], tc["fields"]
            where = f"{f.name} {i}"
            if i in seen:
                errs.append(f"{where}: trùng mã TC với {seen[i]}")
            seen[i] = f.name
            for k in REQUIRED:
                if not fl.get(k):
                    errs.append(f"{where}: thiếu trường {k}")
            for k, allowed in ENUM.items():
                if fl.get(k) and fl[k] not in allowed:
                    errs.append(f"{where}: {k}='{fl[k]}' không hợp lệ ({', '.join(sorted(allowed))})")
            uc = fl.get("UC", "")
            if uc and uc not in ba:
                errs.append(f"{where}: UC '{uc}' không có file trong docs/ba")
            elif uc and ba[uc]["status"] != "approved":
                warns.append(f"{where}: UC {uc} chưa approved (đang {ba[uc]['status']})")
            brs = BR_RE.findall(fl.get("BR", ""))
            for b in brs:
                br_covered.add(b)
                if uc in ba and b not in ba[uc]["brs"]:
                    errs.append(f"{where}: {b} không có trong docs/ba/{uc}.md")
            blocked = fl.get("Status") == "blocked"
            if blocked and not re.search(r"Q-\w+", fl.get("Blocked-by", "")):
                errs.append(f"{where}: Status blocked nhưng thiếu Blocked-by: Q-…")
            if not tc["Steps"]:
                errs.append(f"{where}: thiếu Steps")
            if not tc["Expected"] and not blocked:
                errs.append(f"{where}: Expected trống mà không blocked")
            if re.search(r"\bTC[-_ ]?\d+", fl.get("Pre-condition", "")):
                warns.append(f"{where}: Pre-condition có vẻ phụ thuộc TC khác")
            if len(tc["Expected"]) > 6:
                warns.append(f"{where}: {len(tc['Expected'])} Expected — xem có nhiều mục tiêu không")

    for uc, info in ba.items():
        if uc.upper().startswith("UC-EXAMPLE"):
            continue
        if not any(t["fields"].get("UC") == uc for t in all_tcs):
            errs.append(f"{uc}: chưa có TC nào")
        for b in sorted(info["brs"] - br_covered):
            errs.append(f"{uc}: {b} chưa có TC nào phủ")

    if auto is not None:
        code = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in auto.rglob("*.spec.ts"))
        for tc in all_tcs:
            fl = tc["fields"]
            if fl.get("Automation", "").startswith("Auto") and fl.get("Status") == "approved" and tc["id"] not in code:
                warns.append(f"{tc['file']} {tc['id']}: approved + {fl['Automation']} nhưng chưa có spec")

    n = len(all_tcs)
    by = lambda k: ", ".join(f"{v}={sum(1 for t in all_tcs if t['fields'].get(k)==v)}" for v in sorted(ENUM[k]))
    print(f"UC: {len(ba)} | TC: {n} | Status: {by('Status')} | Automation: {by('Automation')}")
    for w in warns: print("CẢNH BÁO:", w)
    for e in errs: print("LỖI:", e)
    print(f"=> {len(errs)} lỗi, {len(warns)} cảnh báo")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
