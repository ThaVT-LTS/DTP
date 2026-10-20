---
name: write-e2e-spec
description: Viết spec Playwright từ bộ test case đã qua cổng 3. Dùng khi được yêu cầu tự động hoá một UC hoặc một nhóm TC, hoặc sửa spec sau khi test basis đổi.
---
# Viết spec Playwright (v0.1 — [ĐỀ XUẤT], chờ duyệt)
Tuân thủ `rules/common.md`, `rules/feedback.md`, `rules/automation.md`. Ánh xạ TC → code: `skills/test-design/references/templates.md` §6. Ứng với việc số 10 `automation-handoff` trong `docs/tester-skill-map.md`.

1. Điều kiện: `automation/` đã cài Playwright; URL và tài khoản test có trong `.env`; `tests/design-report.md` đã có.
2. Lấy các TC `Tự động hóa: Có` của UC trong `tests/cases/`. Đọc lại các ID trong `Nguồn` ở test basis.
3. Page Object trước (`automation/pages/`): mở màn hình thật, lấy locator theo nhãn nguyên văn. Phần tử không có tên ổn định → liệt kê để nhờ dev thêm test-id.
4. Dữ liệu: fixture đăng nhập theo vai trò và dữ liệu tạo qua API trong `automation/fixtures/`.
5. Viết spec theo `rules/automation.md`: title là ID TC, tag đủ, mỗi ý `Mong đợi` một `expect` có comment ID nguồn.
6. Chạy thật, tự sửa locator và thời gian chờ. Giá trị mong đợi lệch → dừng, báo người dùng.
7. Kết thúc: `npx tsc --noEmit`; báo TC đã phủ, TC bỏ qua (`[CHỜ Q-nn]`, không tự động hoá được), phần tử cần dev bổ sung.
8. Khi test basis lên version mới: làm sau `test-design` chế độ B; tìm spec theo tag ID đổi, sửa assertion theo TC mới **trước** khi chạy lại.
