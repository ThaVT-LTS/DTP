---
name: manual-run
description: Chạy test case trên trình duyệt thật (tay hoặc Playwright hỗ trợ) và ghi kết quả vòng chạy — vào log `runs/` và, khi người dùng yêu cầu, vào cột Round N của file TC. Dùng khi được yêu cầu chạy TC cho một sheet, một UC, một tag hoặc một vòng test (Round N).
---
# Chạy test case (v0.2 — [ĐỀ XUẤT], chờ duyệt)
Tuân thủ `rules/common.md`, `rules/feedback.md`, `rules/automation.md` (rule 8, 19–26). Ứng với việc số 5 `test-execution` trong `docs/tester-skill-map.md`. Định nghĩa Pending / Blocked / NA: `rules/automation.md` rule 19 (chờ duyệt, thay phần "còn chờ chốt" của FB-008).

1. Xác nhận với người dùng: môi trường, URL, tài khoản theo vai trò, vòng chạy, phạm vi (sheet, tag hoặc danh sách TC). Báo nhánh, commit, ngày của bản đang chạy và chậm bao nhiêu commit so với `origin/main` (`rules/automation.md` rule 22).
2. Chỉ chạy TC đã qua cổng rà soát. Đọc TC từ file TC (xuất ra JSON) hoặc `tests/cases/*.md`.
3. Với mỗi TC: chuẩn bị theo Pre-condition (dữ liệu có hậu tố riêng; tài khoản seed không được để hỏng — rule 23), thao tác từng bước, chụp ảnh ở mỗi ý của Expected (`run/shots/<TC>.png`, ảnh phụ `<TC>-<bước>.png`).
4. Kết quả theo bảng `rules/automation.md` rule 19; Remark case Failed theo mẫu rule 20; xem ảnh trước khi ghi Failed (rule 24). Lỗi môi trường thì dựng lại và chạy lại, không ghi Failed.
5. Nhiều case: chia nhóm cho agent con theo `references/run-spec.md`, mỗi agent ghi `results/<nhóm>.json` (`tc, result, remark, bug, shot`).
6. Ghi log `runs/<ngày>-round<N>.md`. Khi người dùng yêu cầu ghi vào file TC: `node scripts/make-writeback.js` (gộp kết quả, gộp bug theo tiêu đề) rồi `powershell -File scripts/apply-writeback.ps1 <file.xlsx> writeback.json` (Result, Test person, Test date, Bug_ID, Remark; đổi mã TC và tham chiếu Cần xác nhận nếu có). Sửa lẻ sau đó: `scripts/apply-batch.ps1`; phần Test_Report của sheet: `scripts/tr-only.ps1`. Sao lưu trước, thử trên bản sao trước (rule 25).
7. Fail → **không tự tạo bug thật.** Trình người dùng: bước, mong đợi, thực tế, ảnh — bằng file bug kèm ảnh (skill `bug-evidence`). Người dùng quyết: bug, TC sai, hay yêu cầu đổi.
8. TC `Tự động hóa: Không` vì chỉ kiểm được bằng mắt → chụp ảnh, để người dùng kết luận.
9. TC sai phát hiện trong lúc chạy (vd thiếu bước) thì ghi ở Remark và báo; chỉ sửa TC khi người dùng đồng ý; vấn đề cách làm thành FB.
10. Kiểm thử ngoài case (tự do) dùng script khám phá (mẫu `scripts/example-explore-dialog.js`); lỗi tìm được thì đề xuất case mới (rule 21).

## Changelog
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.2 | 2026-10-20 | Chạy theo sheet TC, ghi kết quả vào cột Round N bằng script; agent con theo run-spec; kết quả và Remark theo `rules/automation.md` rule 19–20; Fail kèm file bug có ảnh; kiểm thử tự do. **Chờ duyệt.** | FB-090 · FB-091 · FB-093 · FB-096 · chạy Customers Round 1 (19–20/10) |
| v0.1 | 2026-10-02 | Khởi tạo. | Thiết kế trong chat Building 02/10 |
