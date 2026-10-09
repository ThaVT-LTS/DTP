---
name: test-design
description: Viết test case manual và auto từ UC/BR đã duyệt, kèm ma trận độ phủ. Dùng khi được yêu cầu viết TC cho một UC hoặc một dự án.
---
# Thiết kế test case
1. Đọc `profile.md`, `docs/ba/<UC-ID>.md` (phải `approved`), `docs/design-review/<UC-ID>.md`, `docs/questions.md`.
2. Lập khung độ phủ trước khi viết TC: đi đủ 9 mục trong `.claude/rules/testcase.md`, ghi vào `coverage/matrix.md` (dòng = luồng/BR/trường/vai trò, cột = mã TC dự kiến).
3. Viết TC vào `testcases/<UC-ID>.md` đúng định dạng của rule. Expected lấy từ BR/design; không có nguồn → `Status: blocked` + `Blocked-by: Q-…`.
4. Phân loại `Automation`: Auto-UI, Auto-API, hoặc Manual (chỉ kiểm được bằng mắt, cần thiết bị/thao tác ngoài trình duyệt).
5. Chạy `python scripts/check_tc.py projects/<dự-án>`; sửa hết lỗi.
6. **Dừng lại.** Báo: số TC theo Type và Automation, số TC blocked, mục N/A trong matrix. Chờ duyệt.
7. Xuất Excel theo template của dự án chỉ khi được yêu cầu, ghi vào `exports/`; file `.md` vẫn là bản gốc.
