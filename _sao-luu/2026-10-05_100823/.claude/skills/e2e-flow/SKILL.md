---
name: e2e-flow
description: Viết, chạy luồng E2E nhiều màn, nhiều vai trò trên môi trường local bằng Playwright và xuất workbook E2E (mỗi bước: ảnh Figma màn thao tác, ảnh Figma kết quả mong đợi, ảnh thực tế, bảng mong đợi ↔ thực tế; kết quả tính theo Plan). Dùng khi được yêu cầu "chạy E2E wave N", "viết luồng E2E", "xuất file E2E".
---
# Luồng E2E có ảnh Figma và ảnh thực tế (v0.1 — [ĐỀ XUẤT], chờ duyệt · FB-093, FB-094, FB-089)
Tuân thủ `rules/common.md`, `rules/feedback.md`, `rules/automation.md` (rule 19–26), `rules/tc-authoring.md` rule 14.

## Chuẩn bị
1. Môi trường: chỉ localhost (dự án SGS DTP). `git fetch`, báo nhánh, commit, ngày, chậm bao nhiêu commit (`rules/automation.md` rule 22). Kiểm web, backend, worker, Mailpit chạy; đăng nhập thử từng vai trò.
2. `npm install` trong `scripts/` (playwright, pg, exceljs, sharp). `scripts/lib.js` đọc `BASE_URL`, `MAILPIT_URL`, `DB_URL` từ biến môi trường (mặc định localhost của SGS DTP) và đường dẫn Chromium của Playwright.
3. Plan của dự án (UC → wave, trạng thái) dùng để tính Pending / Blocked.

## Viết luồng — `flows2/<ID>.json` (mẫu: `references/example-flow-E2E1_001.json`)
4. Mỗi bước: `act` (ảnh Figma màn thao tác, khung đỏ `①②`), `expImg` (ảnh Figma **kết quả** sau thao tác, khung xanh `A B`, hoặc `null` + `expNote` "Figma chưa có màn …"), `do`, `input`, `exp[]` = `{t, uc}` mỗi ý một UC. Vị trí khung lấy theo pixel ảnh gốc; xem lại bằng `node scripts/preview2.js flows2/<ID>.json` cho tới khi khung nằm đúng chỗ.
5. Tài khoản: `references/example-accounts.json` (vai trò, nhân vật, cổng, email có `{run}`, nguồn: seed / tạo trong luồng / tạo qua DB). Builder sinh bảng Tài khoản test và Pre-condition đánh số (`rules/tc-authoring.md` rule 14).

## Chạy — `run2-<ID>.js` (mẫu: `scripts/example-run2-E2E1_001.js`)
6. Dùng `lib.js` (signInAs, onboardCustomer, waitMail, db…) và `rec2.js`: mỗi bước `R.step(n, page, fn)`, mỗi ý `R.exp(r, i, ok, actual)` với `ok` = `true` / `false` (có nhưng sai, kể cả sai bố cục so với Figma) / `'absent'` (chưa build, không kiểm được). Không tự quyết Passed/Failed: builder quyết từ `ok` + trạng thái Plan của UC.
7. Mỗi lượt tạo dữ liệu có hậu tố riêng; dữ liệu tiền đề màn chưa có thì tạo qua DB và `R.note`. Ảnh email: chụp `MAILPIT/view/<id>.html` khổ 900×620.
8. Nhiều luồng chạy song song bằng agent con theo `references/agent-spec.md`; nhắc agent: lỗi môi trường không ghi Failed, không làm hỏng tài khoản seed.

## Xuất workbook
9. `node scripts/build-e2e-v3.js <out.xlsx> E2E1_001 … E2E1_0nn` → sheet Hướng dẫn, Danh sách E2E (UC Pending theo Plan, độ phủ UC của wave), mỗi luồng một sheet. Công thức kết quả viết bằng so sánh trực tiếp (không COUNTIF). Kết quả: Failed > Blocked > Pending > Passed.
10. Kiểm bằng Excel: mở bản sao, `CalculateFull`, đọc lại ô kết quả; render PDF → PNG xem bố cục (Windows: `Windows.Data.Pdf`). Ký hiệu ⒶⒷ không hiện với Arial — dùng (A)(B).
11. File đang mở trong ONLYOFFICE thì build ra bản tạm, nhờ người dùng đóng rồi mới chép đè.

## Changelog
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-10-20 | Khởi tạo từ lượt chạy 15 luồng E2E Wave 1 SGS DTP (19–20/10): ảnh Figma thao tác / mong đợi / thực tế, bảng mong đợi ↔ thực tế, kết quả theo Plan, bảng tài khoản và Pre-condition đánh số. **Chờ duyệt.** | FB-094 · FB-093 · FB-089 · FB-096 |
