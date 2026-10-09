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

## Thành phần
- `rules/`, `.claude/skills/{ba-analysis,test-design,tc-authoring,feedback-loop}`, `feedback/`: nguyên bộ **ai-ecosystem v0.3** (01/10/2026). Mô tả đầy đủ: `docs/README-ai-ecosystem-v0.3.md`.
- Phần thêm ở bản này, đều là đề xuất chờ duyệt: `CLAUDE.md`, `rules/automation.md`, skill `design-check`, `manual-run`, `write-e2e-spec`, agent `coverage-reviewer`, `evals/`.
- Skill `tc-authoring` v0.3 và `rules/tc-authoring.md` v0.3 (02/10/2026, FB-019 · FB-016), chờ duyệt: file TC theo form file mẫu của dự án (`tc_add_sheet.py`), cả file một phông một bảng màu (`tc_restyle.py`, `tc_palette.py`), `tc_check.py --like <sheet mẫu>`. Rule đã nằm ở `rules/`; phần skill nằm ở `_cho-duyet/tc-authoring-v0.3/` cho tới khi được chép vào `.claude/skills/tc-authoring/` (xem `DOC-TRUOC.md` trong thư mục đó).
- `_cu/`: các file bản dựng đầu (02/10 sáng) đã bị thay thế và bản skill BA lấy từ chat Analysis. Xoá được khi không cần đối chiếu nữa.

## Việc cần làm một lần (chưa làm)
- `git init` trong thư mục này để theo dõi thay đổi.
- Chạy Playwright: trong `automation/<dự-án>/` chạy `npm install`, `npx playwright install chrome`, `npm test` (dự án mới: sao `automation/_template/`; kết quả ở `runs/latest.json`).
- Cho Claude Code điều khiển trình duyệt: `claude mcp add playwright npx @playwright/mcp@latest`.
- Máy cần Python có `openpyxl` và `lxml` cho các script Excel (`lxml` dùng cho `tc_add_sheet.py`, `tc_restyle.py`).
- Dựng bộ bài kiểm theo `evals/README.md`.
