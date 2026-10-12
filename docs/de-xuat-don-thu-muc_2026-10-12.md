# Đề xuất dọn thư mục qa-pipeline — 12/10/2026 [CHỜ DUYỆT]

Theo `docs/BAN-GIAO_2026-10-12.md` Việc 1. Đã chụp trạng thái: commit `1a523ef` "Trước khi dọn thư mục 12/10". Chưa dời, chưa xoá file nào.
Nơi lưu trữ đề xuất: `Documents\qa-pipeline-luu-tru\2026-10-12\` (ngoài repo).

| # | Mục | Thực tế trên máy | Đề xuất |
|---|---|---|---|
| 1 | `_cho-duyet/tc-authoring-v0.3/skill/scripts/` | `tc_add_sheet.py`, `tc_palette.py`, `tc_restyle.py` chỉ có ở đây; SKILL.md Bước 6 và `exports/_build/v1.5/build_v15.py` (dòng 34) đang dùng. `tc_check.py`, `tc_build_xlsx.py` có ở hai nơi nhưng **là hai nhánh khác nhau, không phải cũ/mới**: bản `_cho-duyet` (02/10, 504 dòng) có `--like`, kiểm kiểu ô, kiểm Test_Report; bản `.claude` (08/10, 248 dòng) có kiểm căn lề, Open question, `--lang en`, cảnh báo Pre-condition mở màn | Chép 3 file chỉ có ở đây vào `.claude/skills/tc-authoring/scripts/`. Giữ `tc_check.py`, `tc_build_xlsx.py` bản `.claude` làm bản chính; phần `--like`, kiểm kiểu ô, kiểm Test_Report ghi FB để ghép sau. Sửa đường dẫn ở SKILL.md Bước 6 và `build_v15.py`, chạy thử, rồi đưa `_cho-duyet/` vào lưu trữ |
| 2 | `_cu/` (112 KB) | Rule, skill, mẫu cũ ngày 02/10 | Lưu trữ |
| 3 | `_sao-luu/` (356 KB) | 2 bản sao lưu 05/10, đã nằm trong repo | Lưu trữ; `.gitignore` (đã thêm); `git rm -r --cached _sao-luu` |
| 4 | `_to_delete/` | Chỉ có `.wtest` rỗng (do lần thử quyền xoá trước đây) | Hanna xoá cả thư mục |
| 5 | `CAP-NHAT_2026-10-05_ban-gop.md` | Đã áp ngày 05/10 | Lưu trữ |
| 6 | `CAP-NHAT_2026-10-07_scopes-v1.5.md`, `ap_dung_cap_nhat.py` | Phần `.claude` của bản 07/10 chưa áp | Giữ tới khi Việc 2 xong |
| 7 | `ea_flat.tsv` (gốc thư mục) | 129 dòng = bảng phẳng sheet Assisted workspace v1.15 | Dời thành `projects/sgs-dtp/exports/_flat/Assisted-workspace_v1.15.tsv` |
| 8 | `qa-pipeline-web.zip` | Do `export_web.py` tạo, đang nằm trong repo | Giữ trên máy; `.gitignore` (đã thêm); `git rm --cached qa-pipeline-web.zip` |
| 9 | `projects/sgs-dtp/exports/` | 15 file TC v1.3 → v1.15. Mỗi bản sau chứa đủ sheet của bản trước; v1.15 có đủ 7 sheet (Login 52, Scopes 136, Frameworks 166, Workspaces 45, Assisted workspace 129, Users 62, Profile 13) | **Giữ:** v1.15; v1.12 (còn phải soát lại theo `tu-soat.md`); 3 bản `_Hanna-sua-*` (rule 34); `SGS-DTP_TestCase.xlsx` (form mẫu). **Lưu trữ:** v1.3, v1.4, v1.5, v1.6–v1.11, v1.13, v1.14 (12 file). `SGS_DTP_MVP_Use Case_List_v2.2_VI.xlsx` là tài liệu, dời sang `docs/analysis/` |

## Phát hiện thêm
- Form mẫu từ 05/10 (`SGS-DTP_TestCase1.xlsx`, theo `profile.md`) chỉ có ở `Downloads\SGS`, chưa có trong `exports/`.
- UC List v5.3 (baseline theo Phụ lục bàn giao) chưa có trên máy. Bản mới nhất trên máy là v4 ở `Downloads\SGS`.
- `git commit` trên máy để lại file khoá trong `.git` vì quyền xoá đang tắt; đã đổi tên thành `.git/stale-*-lock-20261012`. Những lần commit sau cũng sẽ vậy cho tới khi Hanna cho phép xoá trong thư mục này.
- Repo đang Public: `docs/BAN-GIAO_2026-10-12.md` (đã commit) có mật khẩu chung của hệ thống demo và mã Figma.
