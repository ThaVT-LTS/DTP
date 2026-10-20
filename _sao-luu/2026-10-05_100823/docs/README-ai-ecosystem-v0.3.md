# Hệ sinh thái AI kiểm thử — BA → Tester → Code

Phiên bản bộ quy tắc: v0.3 (2026-10-01). Mỗi file rule và SKILL.md có changelog riêng.

**Cập nhật 2026-10-07:** `rules/tc-authoring.md` lên v0.5 (đã ở `rules/`, chờ duyệt) theo góp ý FB-042 → FB-049 và cách viết của Hanna ở bản TC v1.4: case bấm nút gửi mà không lưu được thuộc nhóm Không thành công; kết quả kiểm ở nơi hành động trả về, mỗi loại một case; bỏ dạng `{{…}}`, dữ liệu tester nhập ghi cụ thể, dữ liệu có sẵn chưa xác định ghi `[tên]`; giá trị tính toán có nhóm TC với bộ số cụ thể; mọi ô Times New Roman 10; ô bắt đầu bằng `-` `+` `=` `@` có dấu nháy đơn; chữ lưu ở dạng NFC. Phần skill đi cùng (`tc-authoring` v0.4, `tc_check.py`, script mới `tc_fix_xlsx.py`) nằm trong `CAP-NHAT_2026-10-07_scopes-v1.5.md` ở gốc thư mục, có hiệu lực sau khi áp bằng `ap_dung_cap_nhat.py`. Việc còn mở và các câu chờ Hanna trả lời: `docs/VIEC-CON-MO.md`, mục cuối.

**Cập nhật 2026-10-05:** `rules/tc-authoring.md` và skill `tc-authoring` lên v0.3, `rules/common.md` v0.4, `rules/tester.md` v0.3, skill `test-design` v0.2. TC viết cho Tester: vai trò, dữ liệu, nhãn ghi bằng chữ ngay trong ô (`Logged in as <role>`), bỏ sheet `_Data`, `_Labels`; ngôn ngữ file TC theo `profile.md` của dự án; trạng thái rỗng đặt trước, không trỏ sang TC khác, mỗi mục một dòng; TC gọi API chỉ viết khi tester được gọi API, ở sheet `API` riêng; bảng màu theo file TC mẫu; thêm mục G Chia sheet. Phần còn chờ duyệt ghi trong changelog của từng file. Nguồn: các FB ngày 05/10.

**Mới ở v0.3:** `rules/tc-authoring.md` + skill `tc-authoring` — cách viết file test case bàn giao được: một màn một sheet, bốn cấp Classification I–IV có gộp ô, thư viện 12 pattern thao tác cơ bản, quy ước cột và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô), script dựng file và script kiểm tra. Nguồn: FB-010 → FB-013.

Mới ở v0.2: `rules/feedback.md` + skill `feedback-loop` + sổ `feedback/log.md` — mỗi nhận xét của bạn thành một bản ghi `FB-nnn` có địa chỉ sửa, cách kiểm và gate (FB-001). Bản đồ skill còn thiếu cho vai trò Tester: `docs/tester-skill-map.md`.

## Luồng làm việc

```
 Tài liệu yêu cầu (UC list, UC spec, Q&A...)
        │
        ▼
 ┌─ BA · skill ba-analysis ────────────────────────────────────────────┐
 │ 0 Kiểm kê nguồn → 1 Trích xuất (script) → 2 Đối soát hai chiều       │
 │ → 3 Read-back + câu hỏi CHẶN / QUAN TRỌNG / NHỎ                      │
 └──────────────────────────────────────────────────────────────────────┘
        │   ◆ CỔNG 1: người dùng trả lời hết câu CHẶN
        ▼
   4 Baseline v1.0 (+ changelog) → 5 Rủi ro, phạm vi → TEST BASIS v1.0
        │   ◆ CỔNG 2: checklist "Sẵn sàng bàn giao" + review phiên mới
        ▼
 ┌─ Tester · skill test-design ────────────────────────────────────────┐
 │ 0 Kiểm tra đầu vào (thiếu → Q-T gửi BA) → 1 Bản đồ kiểm thử          │
 │ → 2 Kỹ thuật: điều hướng, EP, BVA, bảng quyết định, trạng thái,      │
 │   phân quyền, CRUD, pairwise, đoán lỗi                               │
 │ → 3 TC theo khung Redirect / Validation / Function                   │
 │ → 4 rtm_check.py → 5 Review → 6 Báo cáo bàn giao (+ Excel)           │
 └──────────────────────────────────────────────────────────────────────┘
        │   ◆ CỔNG 3: rtm_check.py không còn lỗi + review độc lập
        ▼
 Code · Playwright (skill sẽ làm tiếp) — test() mang tag @UC-ID @nhóm @loại @Pn

 Thay đổi yêu cầu → BA chế độ B (báo cáo ảnh hưởng) → test basis v1.1 → Tester chế độ B
 Bug lọt → Tester "vòng học" → đề xuất sửa rule / skill / checklist → tăng version

 Nhận xét của bạn ở bất kỳ bước nào → skill feedback-loop → FB-nnn trong feedback/log.md
   → sửa sản phẩm + quét mọi chỗ cùng lỗi → sửa rule/checklist/mẫu/script (+version, +changelog)
   → gắn gate: văn xuôi → checklist → script. Tái phát = gate còn yếu, phải nâng mức.
```

**Test basis** là tài liệu BA gửi Tester. Nó được thiết kế ngược từ khung test case: bảng đường vào/ra cho Redirect, bảng trường dữ liệu và thông báo cho Validation, bảng luồng, rule, tác động phụ, trạng thái, phân quyền cho Function. Mỗi dòng có ID nên script đo được TC đã phủ tới đâu.

## Cấu trúc

```
rules/
  common.md                      luôn nạp — nguồn, câu hỏi, ID, version, nguyên văn
  feedback.md                    luôn nạp — ghi nhận nhận xét, tổng quát hoá, gate, vòng đời FB
  ba.md                          nạp khi làm với tài liệu yêu cầu
  tester.md                      nạp khi làm với test case — kỹ thuật thiết kế
  tc-authoring.md                nạp khi viết hoặc sửa file test case — tổ chức, chia sheet, nội dung, định dạng
skills/
  ba-analysis/
    SKILL.md                     chế độ A (phân tích mới), B (thay đổi)
    references/templates.md      analysis, inventory, phát hiện, câu hỏi, read-back, ảnh hưởng, baseline
    references/gap-checklist.md  soát lỗ hổng, đánh dấu →R →V →F
    references/test-basis-template.md   mẫu bàn giao cho Tester + checklist sẵn sàng
    scripts/extract_uc_list.py   trích xuất UC list từ xlsx/csv, tự kiểm độ phủ
  test-design/
    SKILL.md                     chế độ A (thiết kế mới), B (cập nhật), vòng học từ bug lọt
    references/tc-framework.md   khung Redirect / Validation / Function, checklist từng nhóm
    references/techniques.md     11 kỹ thuật, ví dụ, tiêu chí phủ
    references/templates.md      file thiết kế, mẫu TC, Q-T, báo cáo, ánh xạ Playwright
    references/coverage-checklist.md    tiêu chí hoàn thành, 15 kiểu bug hay lọt
    scripts/rtm_check.py         đo độ phủ, bắt lỗi định dạng TC — mã thoát 1 khi còn lỗi
    scripts/tc_export_xlsx.py    xuất TC ra Excel để chạy tay
    examples/                    ví dụ đầy đủ cho một UC: test basis → thiết kế → 46 TC → RTM → Excel
  feedback-loop/
    SKILL.md                     7 bước xử lý một nhận xét, nạp bộ nhớ đầu task, xử lý tái phát
    references/classification.md xếp loại L1–L7 → sửa ở đâu → gate mức nào
    references/templates.md      mẫu bản ghi FB, dòng changelog, báo cáo cuối task
    scripts/fb_report.py         kiểm tra sổ FB, sinh feedback/report.md — mã thoát 1 khi còn lỗi
  tc-authoring/
    SKILL.md                     6 bước viết TC cho một màn, chế độ chuyển ngôn ngữ, chế độ rà bộ TC cũ
    references/patterns.md       12 pattern thao tác cơ bản rút từ bộ TC thật 150 TC
    references/format.md         cột, phông chữ, căn lề, quy tắc gộp ô, bảng màu, tên nhóm kiểm
    references/templates.md      mẫu TSV phẳng, mẫu câu hỏi, bảng UC → sheet
    scripts/tc_build_xlsx.py     dựng file xlsx từ TSV phẳng, tự gộp ô và định dạng
    scripts/tc_check.py          kiểm tra file TC — mã thoát 1 khi còn lỗi
feedback/
  log.md                         sổ ghi nhớ — mỗi nhận xét một bản ghi FB-nnn
  report.md                      sinh bằng script, không viết tay
docs/tester-skill-map.md         10 việc của tester, skill nào đã có, thiếu gì, thứ tự làm [ĐỀ XUẤT]
docs/analysis/SGS-DTP-MVP-UC-List-v2.1/  lần chạy thử BA trên file SGS (đang chờ trả lời câu CHẶN)
```

## Thư mục đầu ra trong repo dự án

```
docs/analysis/<tài liệu>/        uc-inventory.md · analysis.md · questions.md
docs/baseline/                   <tên>.v1.0.md · changelog.md
docs/test-basis/                 <tên>.v1.0.md
docs/change/                     báo cáo ảnh hưởng khi yêu cầu đổi
tests/design/<UC-ID>.md          bảng kỹ thuật
tests/cases/<module>.md          test case
tests/questions.md               câu hỏi Tester gửi BA
tests/rtm.md                     sinh bằng script
tests/design-report.md           bàn giao cho Code
```

## Cách gọi (ví dụ câu lệnh cho AI)

1. "Phân tích file `docs/source/UC_v2.1.xlsx`" → AI chạy ba-analysis đến bước 3 rồi dừng, trả về câu hỏi.
2. Trả lời câu hỏi (ghi vào `questions.md` hoặc chat "Q-01: đồng ý đề xuất") → "Chốt baseline và xuất test basis".
3. "Thiết kế test cho UC-EVD-008 từ test basis v1.0" → AI chạy test-design, tự chạy `rtm_check.py`, sửa đến khi sạch.
4. Review bộ TC trong một phiên mới: đưa test basis + file thiết kế + TC + `coverage-checklist.md`, yêu cầu duy nhất là tìm case thiếu.
5. "Xuất Excel" khi cần chạy tay.

## Cài vào công cụ

Rule và skill viết ở dạng Markdown trung lập. Với **Claude Code**:
- Chép `skills/ba-analysis`, `skills/test-design` và `skills/feedback-loop` vào `.claude/skills/` của repo.
- Trong `CLAUDE.md` ở gốc repo, import rule: `@rules/common.md`, `@rules/feedback.md`, `@rules/ba.md`, `@rules/tester.md` (hoặc chép nội dung vào).
- Chép cả `feedback/log.md` vào repo và commit nó — đây là bộ nhớ dùng chung giữa các phiên và giữa các công cụ.
- Script chạy từ gốc repo: `python .claude/skills/test-design/scripts/rtm_check.py ...`.

Với công cụ khác (GitHub Copilot, Cursor...), vị trí và định dạng file rule khác nhau — cho mình biết bạn dùng công cụ nào để chuyển đúng định dạng.

## Cập nhật theo góp ý

Quy tắc đầy đủ: `rules/feedback.md`. Tóm lại: mỗi nhận xét của bạn → một bản ghi `FB-nnn` trong `feedback/log.md` (nguyên văn câu bạn nói) → sửa chỗ bạn chỉ ra → **quét tìm mọi chỗ khác cùng lỗi** → sửa rule/checklist/mẫu/script tương ứng, tăng version, changelog trỏ `FB-nnn` → gắn gate. Rule do AI tự rút ra được đánh dấu "chờ duyệt" cho tới khi bạn đồng ý; chỉ bạn chuyển FB sang trạng thái `Đã duyệt`.

Đầu mỗi task, AI chạy:

```
python skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .
```

và nạp mọi FB chưa có gate. Script cũng bắt trường hợp AI nói "đã vào rule" mà không changelog nào trỏ tới FB đó.

## Giới hạn cần biết

Không bộ test nào bảo đảm không lọt bug. Bộ quy tắc này giảm rủi ro bằng: tiêu chí phủ tối thiểu cho từng loại phần tử, script đo độ phủ thay vì AI tự khai, review ở phiên độc lập, charter exploratory cho vùng tài liệu mỏng, và vòng học — mỗi bug lọt được truy nguyên nhân rồi thành một mục mới trong checklist. Chất lượng bộ test không vượt quá chất lượng test basis: yêu cầu thiếu thì TC cũng thiếu, nên cổng 1 và cổng 2 quan trọng ngang cổng 3.
