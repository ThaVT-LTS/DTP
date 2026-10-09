# Rule — Chạy manual và Automation (Playwright)

Phiên bản: v0.2 · **[ĐỀ XUẤT] — chờ duyệt.** Nạp cùng `rules/common.md`, `rules/feedback.md`, `rules/tester.md` khi chạy test hoặc viết spec. Skill: `manual-run`, `write-e2e-spec`. Ánh xạ TC → Playwright: `skills/test-design/references/templates.md` §6.

1. Chỉ chạy và chỉ tự động hoá TC thuộc bộ test đã qua cổng 3 (`rtm_check.py` sạch, đã review).
2. Title của `test()` là `<ID TC> · <tiêu đề>`; ID không đổi khi sửa nội dung. Tag đặt trong option `tag`, không nhét vào title: `@<UC-ID>`, `@<nhóm>`, `@<loại>`, `@P<n>`, và các ID trong trường `Nguồn` của TC.
3. Locator lấy từ nhãn nguyên văn trong test basis (FD, MS, NV); ưu tiên role, label, test-id. Phần tử không có tên ổn định thì liệt kê để nhờ dev bổ sung, không dùng selector theo vị trí.
4. Mỗi test tự chuẩn bị dữ liệu qua API hoặc fixture, không phụ thuộc test khác; tài khoản và URL lấy từ biến môi trường, không ghi trong code.
5. Mỗi ý trong `Mong đợi` của TC ứng với ít nhất một `expect`, comment ghi ID nguồn.
6. TC có nguồn đang `[CHỜ Q-nn]` thì `test.fixme('<Q-nn> chờ trả lời')`; không viết assertion đoán.
7. **Không sửa kết quả mong đợi cho test pass.** Khi chạy lệch: được sửa locator, thời gian chờ, bước thao tác. Giá trị mong đợi lệch thì dừng và báo người dùng quyết: bug, TC sai, hay yêu cầu đã đổi.
8. Kết quả chạy ghi vào `runs/`, không ghi vào file TC. Kết quả Fail phải được người dùng xác nhận trước khi thành bug.
9. Spec kiểm chứng một lần (cho một bug, một bản demo) để ở `automation/tests/verification/`; xong thì nâng thành spec hồi quy hoặc xoá. Bộ hồi quy không chứa spec loại này.
10. Phiên bản Playwright, Node và cấu hình chạy do `package.json` và `playwright.config.ts` quyết định; rule không ghi số phiên bản.

11. Mỗi dự án một thư mục tự đóng gói `automation/<dự-án>/` (có `package.json`, `playwright.config.js`, `.env`). Dự án mới sao từ `automation/_template/`. Test viết trước khi có TC chính thức mang ID tạm `LEARN-*` và tag `@legacy`; khi có TC chính thức thì đổi sang ID TC thật, test nào chưa đổi thì chưa tính vào bộ hồi quy.
12. Đăng nhập một lần: project `setup` lưu `storageState`, các project test dùng lại; test đăng nhập chạy ở project riêng không có `storageState`. Tất cả project dùng cùng một trình duyệt (`channel: 'chrome'`).
13. Cấu hình môi trường (`BASE_URL`, tài khoản) ở `.env`, không đưa lên git; có `.env.example` để người khác điền. Giá trị chứa `#` hoặc khoảng trắng phải đặt trong dấu nháy kép, nếu không bị cắt cụt (lỗi đã gặp: mật khẩu mất ký tự `#` cuối).
14. Mỗi màn hình một Page Object; chức năng dùng chung nhiều màn (tìm kiếm, bảng) tách thành class cha để kế thừa. Locator khai báo ở constructor, thao tác là phương thức.
15. Không dùng `waitForTimeout` và không chờ `networkidle` (ứng dụng có request nền thì không bao giờ idle). Chờ bằng web-first assertion. Bước dễ rớt (mở menu, dialog) bọc trong `expect(...).toPass()`.
16. Dữ liệu tạo trong test dùng tên duy nhất mỗi lần chạy (`uniqueName`). Không dựa vào tên dữ liệu có sẵn trên môi trường (lỗi đã gặp: file mẫu biến mất khi đổi môi trường): chọn theo vị trí hoặc tự tạo. Bắt buộc dùng dữ liệu có sẵn thì khai báo ở `fixtures/testdata.js` kèm chú thích. Test tạo dữ liệu mà chưa có bước dọn thì ghi rõ ở đầu spec.
17. Mỗi dự án ghi kết quả máy đọc được vào `automation/<dự-án>/runs/latest.json` (reporter `json`) và báo cáo HTML; AI đọc file này để biết test nào fail, người dùng không phải chụp màn hình. Kết quả tổng hợp theo TC vẫn ghi ở `projects/<dự-án>/runs/` (rule 8).
18. Test chưa có cơ sở để khẳng định (kết quả mong đợi chưa rõ, dữ liệu chưa tự tạo được) viết thành `test.fixme('<mã câu hỏi> …')` kèm lý do, không để comment hay đoán assertion cho pass.


## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-10-02 | Khởi tạo. Rule 2, 5, 6, 7, 9 lấy theo cách làm của đề xuất FEEC Local E2E (v13, 30/09/2026); rule 8 theo yêu cầu "một số yêu cầu cần confirm vẫn cần con người vào". Đề xuất của AI — **chờ duyệt** | Thiết kế trong chat Building 02/10 |
| v0.2 | 2026-10-02 | Thêm rule 11–18 rút từ dự án thử nghiệm `automation/feec-learning` (chạy thật lần đầu: lỗi `#` trong `.env`, `networkidle`, dữ liệu phụ thuộc môi trường, menu rớt). Đề xuất của AI — **chờ duyệt** | FB-020 |
