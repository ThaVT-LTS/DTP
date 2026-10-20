# qa-pipeline — hướng dẫn dùng

Một thư mục dùng chung cho cả pipeline BA → Check Design → Test case → Chạy manual → Automation.
Claude đọc `CLAUDE.md` (quy tắc), `.claude/rules/` (rule theo thư mục), `.claude/skills/` (skill từng bước).

## Mở thư mục này ở đâu
- **App Claude Desktop:** menu "+" cạnh ô chat → "Add folder" → chọn `Documents\qa-pipeline`. Mọi chat mở thư mục này đều thấy cùng dữ liệu.
- **VS Code + Claude Code:** File → Open Folder → `qa-pipeline`, rồi mở Claude Code. Rule và skill tự được nạp.
- Hai tài khoản khác nhau mở cùng thư mục vẫn dùng chung được, vì dữ liệu nằm trong file.

## Bắt đầu một dự án
1. Sao chép `projects/_template` thành `projects/<tên-dự-án>` (đã có sẵn `projects/sgs-dtp`, kèm lần chạy thử BA trên UC List v2.1).
2. Điền `profile.md`. Bỏ tài liệu khách gửi vào `docs/source/`.
3. Gõ lần lượt, mỗi bước chờ duyệt xong mới sang bước sau:

| Bước | Câu lệnh mẫu | Bạn làm gì sau đó |
|---|---|---|
| 1 | "Phân tích file projects/sgs-dtp/docs/source/UC_v2.1.xlsx" | Trả lời câu hỏi trong questions.md |
| 2 | "Check design cho màn Login theo file Figma này" | Trả lời điểm lệch |
| 3 | "Chốt baseline và xuất test basis" | Review test basis |
| 4 | "Thiết kế test cho UC-AUTH-001 từ test basis v1.0" | Duyệt kết quả review độc lập |
| 5 | "Viết file TC Excel cho màn Login" | Kiểm file, trả lời ô còn đỏ |
| 6 | "Chạy manual bộ smoke, Round 1" | Xác nhận các kết quả Fail |
| 7 | "Viết spec Playwright cho UC-AUTH-001" | Quyết chỗ màn hình trái yêu cầu |
| Khi yêu cầu đổi | "Có bản UC mới, phân tích thay đổi" | Duyệt báo cáo ảnh hưởng |
| Khi bạn nhận xét | nói thẳng nhận xét | Duyệt FB trong feedback/log.md |
| Rà soát TC | "Rà soát file TC v0.2 theo Figma, UC, web, chỉ Wave 1" → sau đó "update" | Duyệt báo cáo rà soát, rồi bảo update |
| Chạy một sheet | "Chạy test case sheet Customers trên localhost, ghi Round 1" | Xác nhận Fail, xem file bug kèm ảnh |
| Luồng E2E | "Chạy E2E Wave 1 trên local" | Xác nhận Fail; kiểm Pending theo Plan |

## Thành phần
- Cập nhật 20/10/2026 (FB-083 → FB-098, chờ duyệt): `rules/tc-authoring.md` v0.11 (xoá case `[OUT]`, câu Đóng xoá khỏi Cần xác nhận, không thêm sheet, mã TC = No. — chờ chốt cách thêm case, hộp thoại nhiều bước nhóm theo bước, Pre-condition đánh số, bộ case abnormal, quyết định của dev đè Figma); `rules/automation.md` v0.3 (rule 19–26: bảng kết quả theo Plan, mẫu Remark, bug một nguyên nhân một mã, môi trường và commit, tài khoản seed, ghi Excel bằng COM, điều đã gặp ở local); skill mới `tc-review`, `e2e-flow`, `bug-evidence`; `manual-run` v0.2. Rút từ lượt rà soát 1.089 case Wave 1, chạy sheet Customers và 15 luồng E2E SGS DTP ngày 19–20/10. Môi trường local và tài khoản: `projects/sgs-dtp/profile.md`.
- `rules/`, `.claude/skills/{ba-analysis,test-design,tc-authoring,feedback-loop}`, `feedback/`: nguyên bộ **ai-ecosystem v0.3** (01/10/2026). Mô tả đầy đủ: `docs/README-ai-ecosystem-v0.3.md`.
- Cập nhật 15/10/2026 (FB-074 → FB-082, chờ duyệt): `rules/tc-authoring.md` v0.10 và `tc-authoring` v0.8 — gộp bản tổng hợp 15/10 của phiên chat vào rule có sẵn (tổng vẫn 40 rule): thứ tự 5 nguồn, Open question tinh gọn, dòng `Login acc`, Step `button [Tên]`, Priority Critical, `[Phase 2]`/`[OUT]`, độ phủ UC theo wave, cổng `tc_fix_xlsx.py` + `tc_check.py --creator`. Script `tc_fix_xlsx.py`, `tc_rows.py` chờ file kèm theo.
- Cập nhật 09/10/2026 (FB-067, chờ duyệt): `tc-authoring` v0.6 và `rules/tc-authoring.md` v0.8 — chế độ soát chéo thêm bước 2b: bên soát gửi đủ lỗi trong một lần; lỗi sót từ vòng trước đánh dấu và đếm riêng (rule 39).
- Cập nhật 09/10/2026 (FB-064, chờ duyệt): `tc-authoring` v0.5 và `rules/tc-authoring.md` v0.7 — thêm Bước 1b (đọc đủ UC, Figma, hệ thống; rà màn đã làm khi luồng đổi) và Bước 6b (tự soát nội dung trước khi giao); rule 36–38.
- Cập nhật 05/10/2026: `tc-authoring` v0.3, `common.md` v0.4, `tester.md` v0.3, `test-design` v0.2 — viết TC bằng chữ cho Tester, ngôn ngữ file TC theo `profile.md`, TC gọi API ở sheet riêng, chia sheet theo màn hình, bảng màu theo file mẫu. Tóm tắt ở dòng "Cập nhật 2026-10-05" đầu `docs/README-ai-ecosystem-v0.3.md`.
- Phần thêm ở bản này, đều là đề xuất chờ duyệt: `CLAUDE.md`, `rules/automation.md`, skill `design-check`, `manual-run`, `write-e2e-spec`, agent `coverage-reviewer`, `evals/`.
- Skill `tc-authoring` v0.3 và `rules/tc-authoring.md` v0.3 (02/10/2026, FB-019 · FB-016), chờ duyệt: file TC theo form file mẫu của dự án (`tc_add_sheet.py`), cả file một phông một bảng màu (`tc_restyle.py`, `tc_palette.py`), `tc_check.py --like <sheet mẫu>`. Rule đã nằm ở `rules/`; `tc_add_sheet.py`, `tc_palette.py`, `tc_restyle.py` đã chép vào `.claude/skills/tc-authoring/scripts/` (14/10, FB-072).
- `_luu-tru/` (14/10, FB-072, không đưa lên git): mọi thứ không còn dùng gom về một chỗ — `_cu/` (bản dựng đầu 02/10), `_sao-luu/` (sao lưu 05/10), `_cho-duyet/` (skill tc-authoring v0.3 cũ), `_to_delete/`, `cap-nhat/` (tài liệu cập nhật 05/10, 07/10 và `ap_dung_cap_nhat.py`), `sgs-dtp-exports-cu/` (file TC nhánh v1.x và v0.21). Xoá được khi không cần đối chiếu.
- Gói cho chat web: `scripts/qa-pipeline-web.zip` (do `scripts/export_web.py` tạo).

## Việc cần làm một lần (chưa làm)
- `git init` trong thư mục này để theo dõi thay đổi.
- Chạy Playwright: trong `automation/<dự-án>/` chạy `npm install`, `npx playwright install chrome`, `npm test` (dự án mới: sao `automation/_template/`; kết quả ở `runs/latest.json`).
- Cho Claude Code điều khiển trình duyệt: `claude mcp add playwright npx @playwright/mcp@latest`.
- Máy cần Python có `openpyxl` và `lxml` cho các script Excel (`lxml` dùng cho `tc_add_sheet.py`, `tc_restyle.py`).
- Dựng bộ bài kiểm theo `evals/README.md`.
