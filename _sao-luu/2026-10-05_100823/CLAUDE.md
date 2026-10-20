# QA Pipeline

Thư mục này là nguồn sự thật duy nhất cho pipeline **BA → Check Design → Thiết kế test → Viết TC → Chạy manual → Automation**.
Nền là bộ quy tắc **Hệ sinh thái AI kiểm thử v0.3** (xem `docs/README-ai-ecosystem-v0.3.md`). Mọi bước đọc file của bước trước và ghi kết quả ra file.

## Rule
Luôn nạp:
@rules/common.md
@rules/feedback.md

Nạp theo việc đang làm (đọc file trước khi bắt đầu):
- Tài liệu yêu cầu, design → `rules/ba.md`
- Thiết kế test, test case → `rules/tester.md`, `rules/tc-authoring.md`
- Chạy manual, viết Playwright → `rules/automation.md` (đề xuất, chờ duyệt)

## Nhiều dự án
Mỗi dự án một thư mục `projects/<dự-án>/`. Đường dẫn `docs/…` và `tests/…` trong rule và skill hiểu là nằm trong thư mục dự án đó:
`docs/source` (tài liệu gốc, chỉ đọc) · `docs/analysis` · `docs/baseline` · `docs/test-basis` · `docs/change` · `docs/design-review` · `tests/design` · `tests/cases` · `tests/questions.md` · `tests/rtm.md` · `runs/` (log chạy) · `exports/` (file Excel bàn giao) · `profile.md`.
Code Playwright: mỗi dự án một thư mục `automation/<dự-án>/` (sao từ `automation/_template/`); `automation/feec-learning/` là code Playwright chính thức hiện tại (hệ thống FEEC, môi trường dev); test cũ mang ID tạm `LEARN-*` cho tới khi có TC chính thức. Sổ góp ý dùng chung ở `feedback/log.md`.

## Quy trình
| Bước | Skill | Cổng |
|---|---|---|
| 1 Phân tích | `ba-analysis` (A: mới, B: thay đổi) | Cổng 1: người dùng trả lời hết câu CHẶN |
| 2 Check design | `design-check` | Điểm lệch thành câu hỏi |
| 3 Baseline + test basis | `ba-analysis` bước 4–5 | Cổng 2: checklist "Sẵn sàng bàn giao" + review phiên mới |
| 4 Thiết kế test | `test-design` | Cổng 3: `rtm_check.py` sạch + agent `coverage-reviewer` |
| 5 File TC Excel | `tc-authoring` | `tc_fix_xlsx.py` và `tc_check.py` cùng 0 lỗi |
| 5b Rà soát TC | `tc-review` (lượt 1 báo cáo, lượt 2 áp khi người dùng nói "update") | Người dùng duyệt báo cáo rà soát trước khi sửa file TC |
| 6 Chạy manual | `manual-run` (kết quả vào `runs/` và cột Round N) | Con người xác nhận mọi kết quả Fail |
| 6b File bug kèm ảnh | `bug-evidence` | Con người xác nhận Fail trước khi tạo bug thật |
| 6c Luồng E2E | `e2e-flow` (ảnh Figma thao tác / mong đợi / thực tế, kết quả theo Plan) | Con người xác nhận Fail; UC chưa Done ghi Pending |
| 7 Automation | `write-e2e-spec` | Con người quyết khi màn hình trái với test basis |
| Mọi nhận xét | `feedback-loop` | Chỉ người dùng chuyển FB sang `Đã duyệt` |

## Cổng con người
AI không tự duyệt. Phải dừng lại hỏi ở: câu CHẶN; baseline và test basis; TC do agent soát đề xuất thêm; kết quả mong đợi chưa có căn cứ (để trống, ghi câu hỏi, không tự đặt); kết quả Fail trước khi ghi bug; màn hình trái với yêu cầu; mọi việc ra ngoài (gửi khách, tạo bug, xoá dữ liệu).

## Script (chạy từ gốc thư mục này)
    python .claude/skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .        # đầu mỗi task
    python .claude/skills/ba-analysis/scripts/extract_uc_list.py <file.xlsx> <out.md> --summary summary.json
    python .claude/skills/test-design/scripts/rtm_check.py --basis projects/<p>/docs/test-basis/<tên>.md projects/<p>/tests/design/*.md --cases projects/<p>/tests/cases/*.md --out projects/<p>/tests/rtm.md
    python .claude/skills/tc-authoring/scripts/tc_fix_xlsx.py projects/<p>/exports/<file>.xlsx --fix --creator <người viết>   # chờ file script
    python .claude/skills/tc-authoring/scripts/tc_check.py projects/<p>/exports/<file>.xlsx --creator <người viết> [--uc <file UC>]
    node .claude/skills/tc-review/scripts/build-report.js <báo-cáo.xlsx>              # tc-review lượt 1 (cần <WORK>/in, <WORK>/out)
    node .claude/skills/tc-review/scripts/make-plan.js; powershell -File .claude/skills/tc-review/scripts/apply-tc.ps1 -Src <vX.xlsx> -Dst <vY.xlsx> -PlanPath apply-plan.json
    node .claude/skills/manual-run/scripts/make-writeback.js; powershell -File .claude/skills/manual-run/scripts/apply-writeback.ps1 <file.xlsx> writeback.json
    node .claude/skills/e2e-flow/scripts/build-e2e-v3.js <out.xlsx> E2E1_001 …       # sau khi chạy run2-<ID>.js
    node .claude/skills/bug-evidence/scripts/build-bug-report.js <Màn>_Bug-Round<N>_kem-anh.xlsx
Script Node của 4 skill trên: chạy `npm install` một lần trong từng thư mục `scripts/` (exceljs, sharp, playwright, pg). Script `.ps1` cần Excel trên máy (COM). Một số script viết cho SGS DTP (cột, tên sheet): đọc đầu file trước khi dùng cho dự án khác.
Trong rule và skill, đường dẫn `skills/…` nghĩa là `.claude/skills/…`.

## Khi sửa hoặc thêm rule, skill (ở bất kỳ chat nào)
Thư mục này (repo `ThaVT-LTS/DTP` trên GitHub) là **một bộ rule duy nhất**: rule, skill, script chỉ sửa ở đây rồi đẩy lên GitHub; phiên chat và Claude Code đều đọc từ GitHub, không giữ bản rule riêng ở từng nơi. Thay đổi chỉ có hiệu lực khi đã ghi vào đây.
1. Ghi bản ghi `FB-nnn` trong `feedback/log.md` (nguyên văn yêu cầu của người dùng).
2. Sửa file rule/skill trong thư mục này, tăng version, thêm dòng changelog trỏ `FB-nnn`.
3. Nếu thay đổi làm thêm, bỏ hoặc đổi tên một skill, một bước, một cổng hay một lệnh script: cập nhật bảng "Quy trình" và mục "Script" ở file này, và bảng câu lệnh mẫu trong `README.md`.
4. Chạy `python .claude/skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .` cho tới khi sạch.
5. Chạy `python scripts/export_web.py` để làm mới `scripts/qa-pipeline-web.zip`.
6. Báo người dùng: file nào đã đổi, version mới, FB nào đang chờ duyệt.

## Khi đổi model hoặc sửa rule/skill
Chạy lại bộ bài kiểm trong `evals/` và so điểm (xem `evals/README.md`).
