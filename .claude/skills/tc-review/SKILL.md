---
name: tc-review
description: Rà soát file test case Excel theo UC, US, decision log, Figma và hệ thống đang chạy; kết luận từng case Xoá / Sửa / Lệch web / Wave sau / OK, xử lý sheet Cần xác nhận, rồi khi người dùng bảo "update" thì áp vào file TC bằng Excel. Dùng khi được yêu cầu "rà soát", "kiểm tra lại TC", "TC lệch Figma/UC/web", "xoá case [OUT]".
---
# Rà soát test case (v0.1 — [ĐỀ XUẤT], chờ duyệt · FB-097, FB-083, FB-084)
Tuân thủ `rules/common.md`, `rules/feedback.md`, `rules/tc-authoring.md`. **Hai lượt, có cổng người dùng ở giữa:** lượt 1 chỉ rà và báo cáo, **không sửa file TC** (`rules/feedback.md` rule 15); lượt 2 chỉ chạy khi người dùng nói "update".

## Lượt 1 — rà và báo cáo
1. Xác định phạm vi: file TC, sheet, wave (theo Plan của dự án, vd `SGS_DTP_Detailed_Plan_v3.0.xlsx` sheet "Plan by UC"), commit của hệ thống dùng để so (`rules/automation.md` rule 22).
2. Xuất mọi case của từng sheet ra JSON (`{row, tc, c1..c4, priority, name, pre, steps, expected, openQuestion, uc}`) và sheet Cần xác nhận (`{row, id, sheet, question, …}`) vào thư mục làm việc `<WORK>/in/`.
3. Chia sheet cho agent con (mỗi agent 1–3 sheet, tối đa ~200 case). Mỗi agent làm theo `references/review-spec.md`, ghi `<WORK>/out/<Sheet>.json`.
4. Kết luận của mỗi case:
   | Kết luận | Nghĩa |
   |---|---|
   | Xoá | `[OUT]`, tính năng không có trong UC / Figma hiện hành, Phase 2, trùng case khác |
   | Sửa | đúng phạm vi nhưng sai nhãn, nút, chữ thông báo, bước, vai trò, Expected, mã UC; chữ tự đặt không có nguồn |
   | Lệch web | case đúng theo nguồn, web làm khác hoặc chưa build → báo dev, không sửa case |
   | Wave sau | UC thuộc wave sau theo Plan → giữ, không rà sâu |
   | OK | đúng và khớp web |
   Câu Cần xác nhận: `Đóng` (đã có câu trả lời, ghi câu trả lời + nguồn) · `Giữ` (vẫn cần BA/khách) · `Bỏ` (chỉ liên quan case bị xoá hoặc ngoài wave).
5. Kiểm đủ: mỗi sheet đủ case, không case `[OUT]` nào khác "Xoá" (script, `rules/common.md` rule 5).
6. Xuất báo cáo file riêng (`rules/tc-authoring.md` rule 3): `node scripts/build-report.js <out.xlsx>` → tab Tổng quan + mỗi sheet một tab + tab Cần xác nhận. Báo người dùng số theo từng kết luận và các lỗi lặp lại nhiều nhất. **Dừng, chờ lệnh.**

## Lượt 2 — áp vào file TC (khi người dùng bảo "update")
7. Agent con viết nội dung ô mới cho mọi case "Sửa" theo `references/edit-spec.md` → `<WORK>/edits/<Sheet>.json` (chỉ các trường đổi, giữ đúng văn phong file). Quyết định mới của người dùng (vd dev bỏ một dòng chữ) đưa vào edit-spec trước khi chạy.
8. `node scripts/make-plan.js` → `apply-plan.json` (dòng xoá, ô sửa, câu hỏi Đóng cần xoá; cảnh báo nếu edit không khớp dòng).
9. Lưu ra **version mới** (không ghi đè bản cũ): `powershell -File scripts/apply-tc.ps1 -Src <vX.xlsx> -Dst <vY.xlsx> -PlanPath apply-plan.json`. Excel tự chỉnh Test_Report và ô gộp; script giữ nhãn Classification khi xoá dòng đầu cụm gộp, bỏ qua ô Classification đang gộp (báo lại để người dùng quyết), đánh lại cột No., xoá dòng Test_Report thành `#REF!`.
10. Kiểm sau khi ghi (script): không mất case ngoài danh sách Xoá, không còn `[OUT]`, không ô Classification trống, câu Đóng đã xoá, Test_Report không có ô lỗi. Báo người dùng các điểm phải tự quyết.

## Gom lại một khối case (vd hộp thoại nhiều bước, `rules/tc-authoring.md` rule 7)
- Soạn khối mới trong JSON (`c2` = tên bước, `@open` = các bước mở hộp thoại, `@keep` = giữ nội dung cũ), rồi `scripts/apply-cc.ps1` (xoá dòng cũ, chèn khối, gộp ô), `scripts/tr-only.ps1` (dựng lại phần Test_Report của sheet), `scripts/fix-cc.ps1` (ghi nhãn vào ô gộp, đặt chiều cao dòng). Luôn chạy thử trên bản sao trước.

## Script
- Node (`npm install` trong `scripts/`): `build-report.js`, `make-plan.js`. PowerShell + Excel: `apply-tc.ps1`, `apply-cc.ps1`, `tr-only.ps1`, `fix-cc.ps1`.
- Tên sheet tiếng Việt (vd `Cần xác nhận`) truyền qua file JSON đọc UTF-8, không viết thẳng trong `.ps1` (PowerShell 5.1 đọc file script theo ANSI).
- Một số script viết cho sheet Customers / SGS DTP (cột G = mã TC, M–Q = Round 1): đọc đầu file trước khi dùng cho dự án khác.

## Changelog
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-10-20 | Khởi tạo từ lượt rà soát 1.089 case Wave 1 SGS DTP (19/10): hai lượt có cổng "update", kết luận Xoá / Sửa / Lệch web / Wave sau / OK, xử lý Cần xác nhận, áp bằng Excel COM, gom khối hộp thoại nhiều bước. **Chờ duyệt.** | FB-097 · FB-083 · FB-084 · FB-088 |
