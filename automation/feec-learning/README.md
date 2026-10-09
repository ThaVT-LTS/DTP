# automation — Playwright

Nguồn gốc: chuyển từ `Desktop\playwright-learning` (02/10/2026), đã dọn theo `rules/automation.md`. Từ 02/10/2026 đây là thư mục code Playwright chính thức cho hệ thống FEEC (môi trường dev). Test cũ mang ID tạm `LEARN-*`, tag `@legacy`.

## Chạy lần đầu (trong VS Code, mở thư mục `automation\feec-learning`)
```
npm install
npx playwright install chrome
npm test
npm run report
```
Cấu hình môi trường: `.env` (đã nằm trong `.gitignore`, không đưa lên git). Mẫu: `.env.example`.

## Cấu trúc
- `pages/` Page Object · `fixtures/testdata.js` dữ liệu dùng chung · `tests/` spec · `tests/verification/` spec kiểm chứng một lần.
- Test cũ mang ID tạm `LEARN-*` và tag `@legacy`; khi có test case chính thức thì đổi sang ID TC thật.

## Còn mở
- Q-AUTO-01: màn Projects hiển thị gì khi tìm không có kết quả → `LEARN-PRJ-SEARCH-002` đang `test.fixme`.
- Dữ liệu có sẵn trên môi trường dev (`25_03_18 (n).txt`) → test tải xuống phụ thuộc dữ liệu này; move/xoá đang `fixme`.
- Chưa có bước dọn folder sau khi tạo.
- Nếu từng đưa mật khẩu admin vào git/chat thì nên đổi.
