---
name: bug-evidence
description: Xuất file báo cáo bug kèm ảnh cho một lượt chạy test có case Failed — sheet Danh sách bug và mỗi bug một sheet (Figma kết quả mong đợi, từng case Failed với Pre-condition, bước, mong đợi, thực tế, ảnh thực tế). Dùng khi được hỏi "ảnh ở đâu", "tạo file bug", "báo cáo Fail kèm ảnh".
---
# File bug kèm ảnh (v0.1 — [ĐỀ XUẤT], chờ duyệt · FB-091, FB-092, FB-090)
Tuân thủ `rules/common.md`, `rules/feedback.md`, `rules/automation.md` rule 20, 21, 24. Bug thật (Jira) chỉ tạo khi người dùng đã xác nhận Fail (`rules/automation.md` rule 8).

1. Đầu vào: kết quả từng case (`results/*.json`: tc, result, remark, shot), nội dung case (`customers-cases.json`), danh sách bug (`writeback.json` → `bugs[]`: code, title, tcs).
2. **Gộp bug theo nguyên nhân:** một mã một nguyên nhân; đánh mã `<MÀN>-BUG-nn` theo case Failed đầu tiên trong sheet. Tiêu đề nói đúng vấn đề và số liệu (vd "127 khách hàng nhưng chỉ hiện 100"). Lỗi thấy khi test tự do: thêm case mới, gắn mã.
3. Remark của mỗi case theo mẫu `rules/automation.md` rule 20 (tách dòng, tên và số thật).
4. Ảnh: ảnh chính `run/shots/<TC>.png` và ảnh phụ `<TC>-*.png` (vd sau khi Back); xem lại từng ảnh trước khi ghi Failed.
5. Mức độ và frame Figma mong đợi của từng bug: khai trong bảng `META` đầu `scripts/build-bug-report.js` (Figma không có màn → `null`, sheet ghi rõ).
6. `node scripts/build-bug-report.js <Màn>_Bug-Round<N>_kem-anh.xlsx` (`npm install` trong `scripts/`: exceljs, sharp). Chép ảnh gốc vào `evidence/<màn>-round<N>/` để đính kèm khi tạo bug.
7. Kiểm: số sheet bug = số mã bug; render một sheet ra ảnh xem bố cục; mã bug trùng với cột Bug_ID của file TC.

## Changelog
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-10-20 | Khởi tạo từ file Customers_Bug-Round1_kem-anh (19–20/10): bug gộp theo nguyên nhân, mỗi bug một sheet có Figma mong đợi và ảnh thực tế. **Chờ duyệt.** | FB-091 · FB-092 · FB-090 |
