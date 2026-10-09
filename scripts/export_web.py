#!/usr/bin/env python3
"""Đóng gói bộ rule + skill + script thành qa-pipeline-web.zip để tải lên chat web.
Không gồm tài liệu khách hàng (projects/<dự-án>), bản cũ (_cu) và code automation.
Dùng (từ gốc qa-pipeline):  python scripts/export_web.py
"""
import zipfile, pathlib, datetime, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INCLUDE = ["CLAUDE.md", "README.md", "rules", ".claude/skills", ".claude/agents",
           "feedback", "docs", "evals", "projects/_template"]
SKIP_PARTS = {"__pycache__", ".git"}
NOTE = """# Đọc trước — bản dùng cho chat web

Gói này là bản sao của thư mục `qa-pipeline`, xuất ngày {date}.

Việc cần làm khi nhận gói này trong một chat:
1. Giải nén vào thư mục làm việc, giữ nguyên cấu trúc.
2. Đọc `CLAUDE.md`, rồi `rules/common.md` và `rules/feedback.md`. Rule khác đọc theo việc đang làm.
3. Đường dẫn `skills/…` trong rule và skill nghĩa là `.claude/skills/…`.
4. Tài liệu dự án không có trong gói. Người dùng sẽ đính kèm tài liệu cần làm; đặt nó vào `projects/<dự-án>/docs/source/` (sao chép từ `projects/_template`).
5. Mọi file kết quả phải gửi lại cho người dùng dưới dạng file, kèm đường dẫn nơi nó thuộc về trong `qa-pipeline`, để người dùng chép về thư mục gốc. Chat này không ghi được vào thư mục gốc.
6. Sổ `feedback/log.md` trong gói là bản sao. Bản ghi FB mới phải gửi lại cho người dùng để gộp vào sổ gốc; không coi sổ trong gói là bản mới nhất.
"""

def main():
    out = ROOT / "qa-pipeline-web.zip"
    n = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("qa-pipeline/DOC-TRUOC.md", NOTE.format(date=datetime.date.today().isoformat()))
        for item in INCLUDE:
            p = ROOT / item
            files = [p] if p.is_file() else sorted(f for f in p.rglob("*") if f.is_file())
            for f in files:
                if SKIP_PARTS & set(f.parts):
                    continue
                z.write(f, "qa-pipeline/" + f.relative_to(ROOT).as_posix()); n += 1
    print(f"{n + 1} file → {out.name} · {out.stat().st_size // 1024} KB")
    return 0

if __name__ == "__main__":
    sys.exit(main())
