# Mẫu dự án Playwright

Sao chép thư mục này thành `automation/<dự-án>/` khi bắt đầu một dự án mới, rồi:
1. Đổi `name` trong `package.json`; sao `.env.example` thành `.env` và điền (`.env` không đưa lên git).
2. Sửa `tests/auth.setup.js` cho trang đăng nhập của dự án.
3. Trong thư mục dự án chạy: `npm install`, `npx playwright install chrome`, `npm test`.
4. Kết quả: `runs/latest.json` (đọc bằng máy), `npm run report` (đọc bằng mắt).

Quy ước: `rules/automation.md`. Test đặt tên `<ID TC> · <tiêu đề>`, tag trong option `tag`.
