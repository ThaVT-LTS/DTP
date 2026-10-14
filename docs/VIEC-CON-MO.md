# Việc còn mở của bộ qa-pipeline

Cập nhật gần nhất: 2026-10-07 (mục cuối file). Bản đầu: 2026-10-02, từ chat Building. File này để mọi chat đều biết việc gì còn dang dở, không phụ thuộc lịch sử chat nào.

## Chờ người dùng duyệt
- 16 bản ghi trong `feedback/log.md` đang ở trạng thái "Mới" hoặc "Đã vào rule (chờ duyệt)", gồm FB-014 (mục đích sản phẩm), FB-015 (tên cột `Open question`), FB-016 (đồng nhất phông và màu).
- Phần do AI đề xuất: `CLAUDE.md`, `rules/automation.md`, skill `design-check`, `manual-run`, `write-e2e-spec`, agent `coverage-reviewer`.
- Tên cột `Open question`: người dùng chưa xác nhận tên; phạm vi của "..." trong FB-016 (độ rộng cột, chiều cao dòng) chưa xác nhận.

## Việc kỹ thuật chưa làm
- `git init` cho thư mục và nơi sao lưu.
- Cài Playwright trong `automation/`; gắn Playwright MCP cho Claude Code.
- Dựng bộ bài kiểm trong `evals/` (chưa có bài nào).
- Đồng bộ định dạng của `skills/test-design/scripts/tc_export_xlsx.py` theo bảng màu ở `skills/tc-authoring/references/format.md` §4 (FB-016).
- Chưa chạy thử trọn một vòng pipeline trên một UC thật.

## Dự án SGS-DTP (người dùng bảo để sau)
- Phân tích ngày 28/09 dựa trên UC List v2.1, đã cũ. Bản mới nhất trong `docs/source` là v2.2 (Phase 1: 98 UC, Phase 2: 61 UC). Cần chạy lại `ba-analysis` trên v2.2 và đối chiếu 63 câu Q&A (file 24/09: mọi câu đều ghi "Close" kể cả câu chưa có trả lời thật).
- 6 câu CHẶN Q-01 → Q-06 chưa trả lời. Q-01 có thể trả lời bằng v2.2 nếu người dùng xác nhận đó là phạm vi đã chốt với SGS. Q-02 mâu thuẫn với Q&A #58.
- Nguồn tài liệu: SharePoint LTS "SGS-Trust Digital Platform / 01 Documents". Chỉ vào lại khi người dùng báo; không đặt kiểm tra hằng ngày.
- Bản dịch: `exports/SGS_DTP_MVP_Use Case_List_v2.2_VI.xlsx` (thêm cột Description tiếng Việt). Lỗi có sẵn trong file gốc: UC-USR-009 trống mô tả; UC-RGF-001 lệch cột; ô tổng giờ dòng 2 báo #REF!; UC-MKT-005 tên UC trùng nội dung cột Actor.

## Chưa đọc được
- Phần AI của "bên khác" (hai link artifact và một link chat): tài khoản này không có quyền mở.
- `TC_RULES.md` và skill `lqa-testcase-writer` không có trong chat Analysis hay Testing. Người dùng đã quyết: dùng `tc-authoring` v0.3 (cột UC và cột `Open question` bắt buộc).

## Automation (02/10/2026)
- Đã chuyển playwright-learning vào `automation/feec-learning/` (thư mục code Playwright chính thức) và dọn code; rule 11–18 ở `rules/automation.md` v0.2 (FB-020). Cần chạy `npm install` + `npm test` trong VS Code để xác nhận.
- Q-AUTO-01: hành vi đúng của màn Projects khi tìm không có kết quả (xem `automation/README.md`).
- `Desktop\playwright-base` trống, có thể xoá; `Desktop\playwright-learning` giữ làm bản gốc đến khi chạy ổn.

## Dự án quan-ly-tai-lieu (nhận từ tài khoản web, 02/10/2026)
- Đã chép vào `projects/quan-ly-tai-lieu/` (16 file, đủ theo danh sách) và `ba-analysis/scripts/pdf_text_coverage.py` (script đề xuất, chờ duyệt; chưa ghi vào CLAUDE.md).
- 7 bản ghi FB mới đánh số FB-021 → FB-027 (bản web gọi tạm FB-017 → FB-020; đã sửa theo ở `profile.md`, `analysis.md`, `questions.md`).
- Tên thư mục `quan-ly-tai-lieu` là tên tạm, chờ Q-02. Cổng 1 chờ Q-01 → Q-04. Khi lệch, theo `tao-thu-muc_nghiep-vu-srs-us-uc.md` và file phân tích case cha con (mới hơn analysis/questions v0.2).
- FB-022 và FB-021 (cách làm gọn) đang "chưa rõ phạm vi": cần Hanna cho biết có áp cho phần khác không.

## Case ngoài nghiệp vụ (FB-028)
- Chờ duyệt: `technical-risk-checklist.md`, rule Tester 12–13, mẫu case cha con (templates §7).
- Hanna duyệt `projects/quan-ly-tai-lieu/tests/design/bo-sung-case-ngoai-nghiep-vu_tao-thu-muc.md` (21 case, 4 câu hỏi) rồi mới đưa vào file Excel.
- Chưa có script kiểm mục `CK-` (nhóm EG); cân nhắc thêm vào `rtm_check.py` sau.

## File TC SGS-DTP v1.3 (06/10/2026, FB-040, FB-041)
- 07/10/2026: bản v1.3 đã được thay bằng v1.4 (Hanna sửa) và v1.5; dòng nào ở mục này còn hiệu lực thì đã ghi lại ở mục dưới. Phông Arial ở cột TVP_ID/Pre-condition đã sửa ở v1.5.
- `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.3.xlsx` (bản so sánh: `tests/design/so-sanh_v1.2-v1.3.md`). Hanna kiểm lại Pre-condition/Step ở Scopes, Login, Users và 3 case mới Scope_130–132.
- Q-S-28 (danh sách Scopes có hiển thị In scope / Out of scope không) chờ Hanna; Expected của danh sách đang chỉ ghi Type và Name.
- Name tạo mới đổi sang giá trị cụ thể: abc, sys-abc, prod-abc (thay `{{scope.new_*}}`); bản tiếng Anh sẽ viết lại khi tài khoản kia làm lại cả file.
- Đã sửa sẵn trong file: ô K13 (Scope_001) bị đọc thành công thức; dòng Test_Report "Trạng thái rỗng" bị #REF!.
- `tc_check.py` vẫn báo phông Arial ở cột TVP_ID/Pre-condition (có từ v1.2, chưa quyết bỏ hay giữ).

## File TC SGS-DTP v1.5 và bản Hanna sửa (07/10/2026, FB-042 → FB-051)

**Trạng thái file**
- `exports/SGS-DTP_TestCase1_v1.4.xlsx`: bản Hanna gửi sáng 07/10, lưu nguyên.
- `exports/SGS-DTP_TestCase1_v1.5.xlsx`: bản AI dựng sáng 07/10 (Scopes 137 TC). Dựng lại được bằng `exports/_build/v1.5/` (xem README ở đó).
- `exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx`: **bản mới nhất về nội dung** — Hanna sửa bản v1.5 bằng ONLYOFFICE và gửi lúc 13:28 ngày 07/10 (Scopes 136 TC), lưu nguyên. Hanna giữ tên file v1.5; trong thư mục đổi tên để không đè bản AI dựng.
- AI chưa dựng bản kế tiếp (v1.6). Chờ Hanna trả lời các câu dưới đây rồi dựng **từ file Hanna gửi**, không dựng lại từ v1.4.

**Tài liệu đi kèm** (đều ở `projects/sgs-dtp/tests/design/`)
- `phan-tich-cach-viet_v1.4.md`: 8 điểm trong cách viết của Hanna, 7 chỗ khác rule đang có.
- `so-sanh_v1.4-v1.5.md`: từng TC giữ, sửa, thêm, bỏ; bảng số cũ → số mới.
- `so-sanh_v1.5-ban-Hanna-sua-0710.md`: Hanna đổi gì ở bản v1.5, chỗ cần Hanna xem lại, lỗi định dạng sau khi lưu bằng ONLYOFFICE, giải thích 3 case Hanna chưa hiểu.
- `cau-hoi_Scopes.md`: 28 câu hỏi Q-S, TC nào đang chờ câu nào (sinh bằng script từ file Hanna gửi).

**Chờ Hanna áp** (AI không ghi được vào `.claude` từ xa)
- `CAP-NHAT_2026-10-07_scopes-v1.5.md`: skill `tc-authoring` v0.4, `tc_check.py`, script mới `tc_fix_xlsx.py`, `CLAUDE.md`, `README.md`. Lệnh áp ghi ở đầu tài liệu đó. Chưa áp thì SKILL.md, references và `tc_check.py` còn là bản 05/10; `rules/tc-authoring.md` v0.5 đã nằm ở `rules/` (chờ duyệt).

**Chờ Hanna trả lời** (xếp theo mức ảnh hưởng tới bản kế tiếp)
1. FB-051 — case chưa có Expected mà tester không tự xác định được trên hệ thống (Scope_119, 131, 137, 021): giữ và viết lại cho rõ, hay bỏ khỏi file TC và chỉ giữ ở danh sách câu hỏi? Đề xuất cho từng case ở `so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 5.
2. Expected điền theo hệ thống đang chạy, giữ câu hỏi: Hanna đã làm ở 18 TC qua hai bản. Trái rule 1 và rule 13. Hanna xác nhận thì AI sửa hai rule đó và điền tiếp các TC còn trống.
3. FB-048 — giá trị tính toán: bản Hanna sửa ghi phép tính và kết quả cho cả case biên (cách A); quyết định 05/10 trong `profile.md` ghi ngược lại. Cần Hanna xác nhận bỏ quyết định 05/10.
4. Ngôn ngữ file TC: `profile.md` ghi tiếng Anh; sheet Scopes viết tiếng Việt, Hanna vừa đổi nốt 6 tên case tiếng Anh sang tiếng Việt.
5. Thứ tự nhóm: Không thành công trước Thành công (theo bản v1.4), ngược câu cũ của rule 8.
6. Case hệ quả ở màn khác (Scope_107 ở Workspaces, Scope_123 ở chi tiết người dùng): để ở sheet Scopes hay chuyển sang sheet của màn đó.
7. Đánh lại TVP_ID khi chưa có kết quả chạy (rule 11); câu mẫu dòng đăng nhập ("Đăng nhập account …" trong file, "Đăng nhập với acc …" trong rule 14).
8. Các chỗ nội dung cần Hanna xem lại trong bản Hanna sửa: Scope_114, Scope_100, Scope_104, Scope_098, Scope_126, Scope_031 (`so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 3). Trong phần Hanna viết ở v1.4: Scope_003 thiếu bước bấm tên scope; Scope_025, 026, 027 cùng tạo `Name: abc` trong khi Scope_020 ghi trùng tên bị chặn (`so-sanh_v1.4-v1.5.md` mục 1).
9. Hanna sửa 18 ô ở sheet Scopes bằng cách nào (gõ thẳng hay dán từ chỗ khác) — để tìm nguyên nhân ô quay về Arial (FB-016).

**Đã biết, chưa làm**
- Login, Users, Profile chưa viết lại theo cách mới: còn dạng `{{…}}` (Login 60 ô ở 50 TC, Users 144 ô ở 62 TC, Profile 21 ô ở 13 TC); Login còn 4 TC ở nhóm Kiểm tra dữ liệu; TC để trống Expected: Login 18, Users 12, Profile 2; TC còn nhắc API: Users 6, Login 1. Chờ Hanna bảo có viết lại không.
- Tên màn nhật ký ghi ba kiểu, chưa kiểu nào còn căn cứ: "Audit Logs" (Scopes), "Audit Trail" (Login), "nhật ký hoạt động của tổ chức" (Users).
- Sheet `Cần xác nhận` thiếu 24 trong 28 câu Q-S và cả 13 câu Q-L của Login; 4 ô Open question của Login không có mã (TC_006, 007, 043, 052).
- Việc của `tests/design/bo-cuc-sheet_uc-v4.md` (05/10) chưa làm: cột UC của Scopes còn mã theo UC List v2.1 (vd `UC-SCP-001`); các TC Gắn framework (Scope_096 → 107) chưa chuyển sang sheet Workspaces; 15 TC trỏ UC-RDN-004, mà tài liệu đó ghi RDN-004 đã sang P2 ở UC List v4 — trong khi góp ý 07/10 yêu cầu thêm TC cho cột Evidence coverage (Q-S-11). File UC List v4 chưa có trong `docs/source`.
- 4 TC gọi API ở Scopes đã bỏ ở v1.5 theo quyết định 05/10 (FB-039).

**Kỹ thuật**
- Máy Hanna mở file TC bằng ONLYOFFICE (thấy trên ảnh chụp 07/10). Câu "tôi đã có excel r ạ" lúc 09:02 AI chưa hiểu chắc là máy đã có Excel hay ý khác.
- Kiểu Normal của file là Arial 10, giữ như file mẫu. Ô nào mất định dạng phông thì về Arial: đã xảy ra với 18 ô ở bản Hanna sửa. Hai cách, chờ Hanna chọn (FB-016): chạy `tc_fix_xlsx.py` mỗi lần nhận file về (đang làm), hoặc đổi kiểu Normal sang Times New Roman 10 — Excel và ONLYOFFICE tính độ rộng cột theo phông của kiểu Normal, nên phải mở thử trên cả hai, AI chưa thử được.
- Xoá dòng TC cuối cùng của một khu vực làm Test_Report ra `#REF!` (bản Hanna sửa: 54 ô). Mỗi lần nhận file về phải dựng lại Test_Report.
- Bản v1.5 AI mới kiểm bằng LibreOffice và ở mức XML, chưa mở bằng Excel thật.
- `tc_check.py` bản 05/10: v1.5 ra 0 lỗi, 10 cảnh báo; bản Hanna sửa ra 2 lỗi (17 ô sai phông, Scope_104 thiếu UC). Bản trong tài liệu cập nhật 07/10 báo thêm 3 lỗi `{{…}}` ở Login, Users, Profile và ô có chữ dạng tổ hợp.
- `_cho-duyet/tc-authoring-v0.3/` đã vào `_luu-tru/` (14/10); 3 script còn dùng đã chép vào skill. Còn lại: ghép `--like`, kiểm kiểu ô, kiểm Test_Report của `tc_check.py` bản cũ vào bản của skill (FB-072).

**Đề xuất của AI, chưa làm, chờ Hanna quyết**
- Đưa hai script ở `exports/_build/v1.5/` thành script chung của skill `tc-authoring`: `compare_edit.py` (so file Hanna sửa với bản gốc) và phần dựng lại sheet từ bảng phẳng ở mức XML trong `build_v15.py`.
- Thêm cột "Căn cứ" cho mỗi TC (UC, Figma, hệ thống đang chạy) để phân biệt Expected đã có căn cứ với Expected tạm; khi đó script báo được dòng có Expected mà không có căn cứ (FB-042).

## 2026-10-08 · Sheet Frameworks (module 04)
- Khung case cha v0.1 chờ Hanna duyệt: `projects/sgs-dtp/tests/design/khung-case-cha_Frameworks.md` (FB-052). 17 câu hỏi Q-F-01…17; cần trả lời trước nhất: Q-F-04 (import là cập nhật hay thêm bản riêng), Q-F-07 (ai chọn tier), Q-F-08 (có cho bấm nút xác nhận trên prototype không), Q-F-15 (FWK-04/05/07 chưa có màn).
- Chưa lưu: bản so sánh `SGS-DTP_TestCase1_v1.5` Hanna sửa 07/10 19:54 (đã ghi trong FB-050); file xlsx mới chưa copy vào `exports/`.
- 2026-10-08 09:15: đã viết sheet Frameworks vào `exports/SGS-DTP_TestCase1_v1.6_Frameworks.xlsx` (118 case). Việc còn lại: Hanna soát; trả lời Q-F; viết thêm 13 case nhóm C khi có thiết kế; so sánh bản v1.5 Hanna sửa lúc 19:54; Test_Report đã được dựng lại (bản gốc có ô #REF! ở dòng 29).
