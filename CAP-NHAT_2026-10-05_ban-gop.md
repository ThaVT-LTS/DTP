# Cập nhật bộ rule qa-pipeline — bản gộp 05/10/2026

Thay cho `CAP-NHAT_tc-authoring_v0.3_chia-sheet.md` (bản đầu và bản 2). Gộp mọi thay đổi chốt trong chat ngày 05/10: bỏ khoá `{{...}}` và sheet `_Data`, `_Labels`; viết TC bằng tiếng Anh theo `profile.md`; 5 FB về cách viết; TC gọi API; chia sheet theo màn hình; bảng màu theo file TC mẫu.

Áp lên bản ngày 02/10 của thư mục `qa-pipeline`. Có 83 chỗ Tìm / Thay bằng, 1 chỗ thêm vào cuối file, 3 file mới, trên 20 file. Script `ap_dung_cap_nhat.py` đọc chính tài liệu này để áp, nên tài liệu vừa để đọc, vừa để chạy.

## Cách áp

1. Đặt `ap_dung_cap_nhat.py` và tài liệu này vào thư mục `qa-pipeline`, cùng chỗ với `CLAUDE.md`.
2. Chạy thử, chưa sửa gì: `python ap_dung_cap_nhat.py`. Mỗi chỗ sửa báo một trong ba: `OK`, `đã áp`, `cần sửa tay`.
3. Áp thật: `python ap_dung_cap_nhat.py --ap`. File cũ được sao lưu ở `_sao-luu/<ngày giờ>/` trước khi sửa.
4. Đánh số FB: script in số FB lớn nhất đang có trong `feedback/log.md`. Chạy `python ap_dung_cap_nhat.py --danh-so <số tiếp theo>` để xem trước, rồi thêm `--ap` để đổi mọi `FB-???[…]` thành số thật và gộp 11 bản ghi mới vào `feedback/log.md`.
5. Kiểm sổ: `python .claude/skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .` → 0 lỗi.

Chỗ báo `cần sửa tay` là chỗ file trên máy đã khác bản 02/10: tìm theo nhãn của chỗ sửa trong tài liệu này rồi sửa tay. Không đồng ý chỗ nào thì xoá cả chỗ đó (từ dòng **Tìm** tới hết khung **Thay bằng**) khỏi tài liệu trước khi chạy `--ap`.

## Trạng thái duyệt

| Phần | Trạng thái |
|---|---|
| Bỏ khoá `{{...}}`, `_Data`, `_Labels`; rule 14 viết bằng chữ | Hanna chốt 05/10 |
| Tiếng Anh: rule 16, rule 14 hai dạng, bảng từ tên nhóm kiểm, `tc_check.py` (mục 1–4) | Hanna duyệt 05/10 ("tốt") |
| 5 FB cách viết: rule 4, P12, rule 12 và 14, SKILL Bước 6 (mục 5–9) | Hanna duyệt 05/10 ("tốt") |
| API: rule 29, `tester.md` rule 5, P5, 14 chỗ ở `test-design`, `profile.md` (mục 10–12) | Hanna duyệt 05/10 ("duyệt") |
| Giá trị tính toán | Bị bác: không thêm rule |
| Chia sheet: rule 3, 24–28; SKILL Đầu ra, Bước 1 bước 4, Bước 4; templates §4; sheet `Phân quyền`; bố cục SGS DTP | Chờ duyệt (2 FB "Đã vào rule (chờ duyệt)") |
| Bảng màu theo file mẫu (`format.md`, `tc_check.py`, `tc_build_xlsx.py`); SKILL Bước 7 "không bỏ qua cả một loại lỗi" | Chờ duyệt (FB-016 tái phát, đề xuất của AI) |
| Căn giữa theo chiều dọc như file mẫu (rule 19, `format.md`, `tc_build_xlsx.py`) | Chờ duyệt (FB-013, đề xuất của AI) |

## Danh sách file

| # | File | Mới / Sửa | Thay đổi |
|---|---|---|---|
| 1 | `feedback/fb-moi_2026-10-05.md` | Mới | 11 bản ghi FB ngày 05/10, chưa đánh số |
| 2 | `feedback/log.md` | Sửa | Dòng Cập nhật cho FB-010, 013, 016 (tái phát), 019 |
| 3 | `rules/tc-authoring.md` | Sửa · v0.2 → v0.3 | Rule 3, 4, 7, 12, 14, 15, 16, 19, 22; mục G rule 24–29 |
| 4 | `rules/common.md` | Sửa · v0.3 → v0.4 | Rule 6: ngôn ngữ file TC |
| 5 | `rules/tester.md` | Sửa · v0.2 → v0.3 | Rule 5: phân quyền âm, API |
| 6 | `.claude/skills/tc-authoring/SKILL.md` | Sửa · v0.2 → v0.3 | Mô tả, Đầu ra, Bước 1, 4, 5, 6, 7 |
| 7 | `.claude/skills/tc-authoring/references/templates.md` | Sửa | Mẫu TSV tiếng Anh; bỏ `_Data`, `_Labels`; thêm §4 bảng UC → sheet |
| 8 | `.claude/skills/tc-authoring/references/format.md` | Sửa | Bảng màu theo file mẫu, căn giữa theo chiều dọc, bảng từ tên nhóm kiểm |
| 9 | `.claude/skills/tc-authoring/references/patterns.md` | Sửa | P5, P12, chỗ hay thiếu #3 |
| 10 | `.claude/skills/tc-authoring/scripts/tc_check.py` | Sửa | Bỏ kiểm khoá; bảng màu mới; câu mơ hồ tiếng Anh; Success/Failure; `--lang en` |
| 11 | `.claude/skills/tc-authoring/scripts/tc_build_xlsx.py` | Sửa | Bảng màu mới, căn giữa theo chiều dọc |
| 12 | `.claude/skills/test-design/SKILL.md` | Sửa · v0.1 → v0.2 | Changelog |
| 13 | `.claude/skills/test-design/references/coverage-checklist.md` | Sửa | API chỉ khi tester được gọi API (3 chỗ) |
| 14 | `.claude/skills/test-design/references/techniques.md` | Sửa | API chỉ khi tester được gọi API (6 chỗ) |
| 15 | `.claude/skills/test-design/references/tc-framework.md` | Sửa | API chỉ khi tester được gọi API (5 chỗ) |
| 16 | `projects/_template/profile.md` | Sửa | Thêm dòng ngôn ngữ viết file TC, tester được gọi API |
| 17 | `projects/sgs-dtp/profile.md` | Mới | Hồ sơ dự án SGS DTP |
| 18 | `projects/sgs-dtp/tests/design/bo-cuc-sheet_uc-v4.md` | Mới, tuỳ chọn | Bố cục sheet theo UC List v4 |
| 19 | `docs/README-ai-ecosystem-v0.3.md` | Sửa | Dòng cập nhật 05/10; mục Cấu trúc |
| 20 | `README.md` | Sửa | Một dòng ở mục Thành phần |

## 1. `feedback/fb-moi_2026-10-05.md`

**1.1 · 11 bản ghi FB ngày 05/10, chưa đánh số. Tạo file mới**

```markdown
# Bản ghi FB mới — 05/10/2026

11 bản ghi từ chat ngày 05/10/2026: 2 bản về chia sheet, 9 bản về cách viết file `SGS-DTP_TestCase1` (v1.3). Chưa sửa TC nào theo các bản ghi này.

Đánh số: chạy `python ap_dung_cap_nhat.py --danh-so <số tiếp theo của feedback/log.md> --ap`. Script đổi mọi `FB-???[…]` thành số thật, theo thứ tự của bảng dưới, ở file này và ở các dòng changelog, rồi gộp bảng và bản ghi vào `feedback/log.md`. Làm tay thì thay từng `FB-???[…]` theo đúng thứ tự đó.

Số liệu ở trường "Phạm vi ảnh hưởng" được đếm bằng script trên `SGS-DTP_TestCase1_v1.3.xlsx` (Login 52, Scopes 129, Users 62, Profile 13 — tổng 256 TC), trừ chỗ ghi khác.

## Dòng cho bảng tra nhanh

| FB | Tiêu đề | Loại | Trạng thái | Tái phát |
|---|---|---|---|---|
| FB-???[chia-sheet] | Chia sheet theo màn hình, vai trò nằm trong sheet | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-???[gop-tach-sheet] | Gộp, tách sheet theo màn hình, không theo module của UC list | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-???[tieng-anh] | Viết TC bằng tiếng Anh; ít nhất tên nút giữ nguyên tiếng Anh | L2-rule | Đã duyệt | 0 |
| FB-???[rong-truoc] | Trạng thái rỗng đặt trước, theo vòng đời dữ liệu rỗng → tạo → có dữ liệu | L2-rule | Đã duyệt | 0 |
| FB-???[rong-du] | Trạng thái rỗng phải tả đủ icon, chữ, nút | L3-checklist | Đã duyệt | 0 |
| FB-???[khong-lung-lo] | Không viết lửng lơ ở Expected và Step; không biết thì đưa vào Q&A | L2-rule | Đã duyệt | 0 |
| FB-???[pre-condition] | Pre-condition đăng nhập ghi bằng vai trò: "Đăng nhập với acc Customer Admin" | L4-mẫu | Đã duyệt | 0 |
| FB-???[moi-dong] | Nhiều mục thì mỗi mục một dòng, không nối bằng " · " | L4-mẫu | Đã duyệt | 0 |
| FB-???[gia-tri-tinh] | Giá trị tính toán phải nói lấy từ đâu; TC phải dễ sửa khi Figma, UC đổi | L2-rule | Bị bác | 0 |
| FB-???[xem-truoc] | Gửi bản xem trước danh sách tính năng trước khi cập nhật file TC | L2-rule | Đã duyệt | 0 |
| FB-???[api] | TC gọi API chỉ viết khi tester được gọi API, và để ở sheet API riêng | L2-rule | Đã duyệt | 0 |

## Bản ghi

## FB-???[chia-sheet] · Chia sheet theo màn hình, vai trò nằm trong sheet
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "tài liệu UC ntn, thì gợi ý giúp tôi, nên theo bố cục các sheet ntn" · "VD: tôi đang có 2 role chính: Customer và SGS trong đó lại có Customer Admin và SGS Admin" · "Tạo Scope từ phía Customer chẳng hạn (ko pải Customer admin...) thì vẫn ở trong 1 sheet: Customer và nó có nhiều phần như Scope còn bên dưới là Certification ..." · "Hay mỗi sheet là 1 Scope  và 1 Certification  > hãy đánh giá và gợi ý cho t tham khảo" · "hãy cho tôi bản docs để t cập nhập vào Rule + Skill trên máy tính này: trên Readme"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#24 · rules/tc-authoring.md#27 · skills/tc-authoring/SKILL.md#đầu-ra · skills/tc-authoring/SKILL.md#bước-4 · skills/tc-authoring/SKILL.md#bước-5 · scripts/tc_check.py
- Tiêu chí kiểm: không sheet nào đặt theo vai trò; Pre-condition của mọi TC mở đầu bằng dòng đăng nhập theo rule 14 ("Logged in as <role>" hoặc "Not logged in" ở file tiếng Anh); khác biệt giữa các vai trò nằm ở nhóm Phân quyền; TC "làm ở vai trò A, kiểm ở vai trò B" nằm ở sheet của hành động
- Phạm vi ảnh hưởng: quét SGS-DTP_TestCase1_v1.3.xlsx bằng script ngày 05/10 — 18/256 TC có Pre-condition không ghi vai trò: Login TC_038, 039, 041, 050; Scopes TC_022, 023, 024, 026, 027, 049, 051, 052, 069, 070, 071, 090, 091, 092
- Liên quan: FB-010 (rule 3 gốc) · FB-???[pre-condition] (cách ghi vai trò bằng chữ, rule 14)
- Đã sửa: chưa sửa sản phẩm; rule 24, 27 và skill v0.3 theo tài liệu cập nhật gộp ngày 05/10
- Cách kiểm: lọc cột Pre-condition, dòng nào cũng mở đầu bằng "Logged in as" hoặc "Not logged in" (file tiếng Việt: "Đăng nhập với acc", "Chưa đăng nhập")
- Gate: mức 1 · đề xuất nâng mức 3: tc_check.py báo Pre-condition không mở đầu bằng dòng đăng nhập của rule 14
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-???[gop-tach-sheet] · Gộp, tách sheet theo màn hình, không theo module của UC list
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "vậy có nên chia đủ 21 bộ UC này thành 21 sheets ko, hay là nên làm thế nào: Giả dụ như 07 và 08 cùng là evidence nhưng chia thành Assisted mode và common > nên tách ra hay gộp lại..." · "hãy cho tôi bản docs để t cập nhập vào Rule + Skill trên máy tính này: trên Readme"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#3 · rules/tc-authoring.md#25 · rules/tc-authoring.md#26 · rules/tc-authoring.md#28 · skills/tc-authoring/SKILL.md#bước-1 · references/templates.md#4
- Tiêu chí kiểm: Cover có bảng UC → sheet; mỗi UC của baseline đúng một dòng (tên sheet · Chờ · Kiểm ở); không sheet nào được tạo chỉ vì có một module; cột UC dùng ID của baseline hiện hành
- Phạm vi ảnh hưởng: SGS DTP UC List v4 — 105 UC, 21 module → 16 sheet viết được ngay (75 UC), 26 UC chờ, 4 UC kiểm ở nơi hiện ra (đếm bằng script ngày 05/10; chi tiết ở projects/sgs-dtp/tests/design/bo-cuc-sheet_uc-v4.md). SGS-DTP_TestCase1.xlsx: 175/181 TC ghi UC theo ID nguồn v2.1 (UC-SCP-001…), 6 TC còn lại ghi [NGOÀI UC]; trong sheet Scopes có 13 TC trỏ UC mà v4 đã dời sang Workspace (UC-SCP-006 → WSP-01: 11, UC-EVD-003 → WSP-02: 1, UC-SCP-007 → WSP-04/05: 1); 6 TC trỏ UC không còn ở P1 (UC-RDN-004: 4 và UC-AUTH-003: 1 đã sang P2; UC-ACC-009: 1 không có trong v4)
- Liên quan: FB-010 (rule 3 gốc)
- Đã sửa: chưa sửa sản phẩm; rule 3, 25, 26, 28 và skill v0.3 theo tài liệu cập nhật gộp ngày 05/10
- Cách kiểm: số dòng của bảng UC → sheet ở Cover bằng số UC của baseline, không UC nào xuất hiện hai lần
- Gate: mức 1 · đề xuất nâng mức 3: tc_check.py đối chiếu bảng UC → sheet với UC list
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-???[tieng-anh] · Viết TC bằng tiếng Anh; ít nhất tên nút giữ nguyên tiếng Anh
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Chúng ta hướng đến viết TCs bằng 100% tiếng Anh, nếu không thì các btn cần viết nguyên tên tiếng Anh, vd: "Create Scope" ..."
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#16 · rules/tc-authoring.md#7 · rules/tc-authoring.md#14 · rules/common.md#6 · skills/tc-authoring/SKILL.md#bước-5 · skills/tc-authoring/SKILL.md#chế-độ-phụ--chuyển-bộ-tc-sang-ngôn-ngữ-khác · references/format.md · scripts/tc_check.py · projects/_template/profile.md · projects/sgs-dtp/profile.md
- Tiêu chí kiểm: mọi sheet, mọi cột của file TC SGS DTP viết tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt; mọi tên nút, nhãn, thông báo trùng nguyên văn Figma, kể cả chữ hoa chữ thường
- Phạm vi ảnh hưởng: 256/256 TC đang viết bằng tiếng Việt. Sheet Users, Profile còn nhiều thao tác tả bằng tiếng Việt vì chưa có Figma (vd "Mở form mời người dùng"). Lưu ý: Figma ghi "Create scope" (chữ s thường), không phải "Create Scope". Đếm thêm trên bản v1.3: Classification I ghi hai thứ tiếng (14 nhãn, vd "Đăng nhập - Login"); Classification III tiếng Việt (67 nhãn, vd "Thành công" 48 TC, "Hiển thị" 33 TC); Function Name có phần tiếng Việt (vd "AUTH-L0001_Đăng nhập"); Test_Report 116/154 ô chữ có tiếng Việt; Cover 7/53 ô
- Xung đột: `common.md` rule 6 ghi "Phần phân tích viết tiếng Việt"; `tc-authoring.md` rule 16 chỉ yêu cầu nhãn theo ngôn ngữ của hệ thống. Hai lựa chọn: (1) chuyển cả bộ sang tiếng Anh ngay ở bản tới, dùng chế độ chuyển ngôn ngữ của skill — một lần sửa lớn, sau đó thống nhất; (2) giữ tiếng Việt, chỉ bắt buộc nhãn giao diện đúng nguyên văn tiếng Anh, chuyển tiếng Anh sau — ít việc bây giờ, nhưng sẽ phải dịch lại về sau
- Đã sửa: chưa sửa sản phẩm; câu rule đã duyệt ngày 05/10, chép vào rule, skill bằng tài liệu cập nhật gộp
- Cách kiểm: lọc các ô Step, Expected có tên nút; mỗi tên nút trùng nguyên văn một nhãn trong Figma. Tìm chữ có dấu tiếng Việt ở mọi sheet, trừ cột Open question và sheet Cần xác nhận → 0 kết quả
- Gate: mức 1 · đề xuất nâng mức 3: tc_check.py cảnh báo ô có chữ tiếng Việt ngoài cột Open question và sheet Cần xác nhận; đối chiếu tên nút với danh sách nhãn Figma nếu có danh sách đó
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna chốt bằng câu hỏi chọn đáp án trong chat. Câu "Chuyển TC sang tiếng Anh khi nào?" chọn "Ngay ở bản tới". Câu "phần nào trong file TC đổi sang tiếng Anh?" chọn "Cả file, trừ câu hỏi": mọi sheet, mọi cột viết tiếng Anh, riêng cột Open question và sheet Cần xác nhận vẫn tiếng Việt; rule, FB, phân tích và chat vẫn tiếng Việt. Câu "Dòng đăng nhập ở Pre-condition ghi bằng tiếng Anh thế nào?" chọn "Logged in as <role>" (ghi ở FB-???[pre-condition]). Đây là lựa chọn (1) ở mục Xung đột. Đáp án do AI soạn, Hanna chọn. Trạng thái chuyển từ Chưa rõ phạm vi sang Mới. [Đề xuất của AI, chờ duyệt] ghi ngôn ngữ file TC ở profile.md của từng dự án thay vì ghi cứng trong rule, vì dự án Quản lý tài liệu chưa chốt ngôn ngữ giao diện (Q-02); bảng từ cố định Việt → Anh cho nhóm kiểm ở cột Classification III.
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 1–4 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-???[rong-truoc] · Trạng thái rỗng đặt trước, theo vòng đời dữ liệu rỗng → tạo → có dữ liệu
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Phần Trạng thái rỗng - Empty: vì theo logic từ chưa có gì > tạo xong thì mới hiện data và trong Figma cũng từ rỗng > có data => ưu tiên trạng thái rỗng này trước nhé > Sắp xếp lại đúng logic"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#4 · skills/tc-authoring/SKILL.md#bước-5
- Tiêu chí kiểm: ở mỗi màn danh sách, nhóm Trạng thái rỗng đứng ngay sau Điều hướng, trước nhóm tạo mới và mọi nhóm cần có dữ liệu (bảng, tìm kiếm, phân trang)
- Phạm vi ảnh hưởng: Scopes — nhóm Trạng thái rỗng (TC_052) đang đứng sau Phân trang (TC_048–051). Users chưa có TC trạng thái rỗng. Login không có danh sách
- Liên quan: rule 4 hiện chỉ nói thứ tự khu vực theo mắt đọc; góp ý này thêm thứ tự theo vòng đời dữ liệu
- Đã sửa: chưa sửa sản phẩm; câu rule đã duyệt ngày 05/10, chép vào rule, skill bằng tài liệu cập nhật gộp
- Cách kiểm: mở từng sheet có danh sách, TC trạng thái rỗng nằm trước TC tạo mới đầu tiên
- Gate: mức 1
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 5 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-???[rong-du] · Trạng thái rỗng phải tả đủ icon, chữ, nút
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Với trạng thái rỗng thì sẽ ntn, cũng nêu rõ VD: có hình icon, có text ntn cũng nêu ra nhé"
- Loại: L3-checklist
- Địa chỉ: skills/tc-authoring/references/patterns.md (pattern Bảng) · references/coverage-checklist.md
- Tiêu chí kiểm: TC trạng thái rỗng ghi đủ, mỗi phần một dòng: icon; tiêu đề nguyên văn; mô tả nguyên văn; nút và nhãn nút; các phần vẫn hiện như tiêu đề trang, ô tìm kiếm, hàng tiêu đề bảng — ghi thẳng ra, không trỏ sang TC khác
- Phạm vi ảnh hưởng: Scopes TC_052 (bản v1.3 còn ghi "giống TC_006", "giống TC_038"); Scopes TC_035 (tìm không có kết quả, chữ đang lấy từ prototype)
- Đã sửa: chưa sửa sản phẩm; câu rule đã duyệt ngày 05/10, chép vào rule, skill bằng tài liệu cập nhật gộp
- Cách kiểm: đối chiếu TC_052 với frame Scopes / Empty, đủ icon, tiêu đề "Create your first scope", mô tả, nút "Create scope"
- Gate: mức 2 · mục bắt buộc trong checklist của pattern Bảng
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 6 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-???[khong-lung-lo] · Không viết lửng lơ ở Expected và Step; không biết thì đưa vào Q&A
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Bỏ hết các thông tin lửng lơ: {{scope.new_sys}} (system)," · "cả Step cũng vậy > nếu ko bit thì QnA," · "còn nếu muốn nói Mở xem chi tiết dự án với step:1. Click vào 1 dự án , 2. Quan sát dự án"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#12 · rules/tc-authoring.md#13 · skills/tc-authoring/SKILL.md#bước-5
- Tiêu chí kiểm: Expected ghi đúng chữ, giá trị, định dạng sẽ thấy; không có chú thích trong ngoặc sau khoá, không ghi "ở cả hai màn" mà không nêu tên màn, không trỏ sang TC khác. Step là thao tác cụ thể (Click <tên phần tử>, nhập <giá trị>, quan sát <khu vực>). Chưa biết thì để trống và ghi câu hỏi
- Phạm vi ảnh hưởng: Scopes TC_027 (ví dụ Hanna chỉ ra: "Ở cả hai màn, trường Contains của khối Overview có {{scope.new_sys}} (system)"); Scopes TC_052 (trỏ TC_006, TC_038); khoảng 90 TC có Step chỉ ghi "Mở …" mà không nói bấm vào đâu (Login 6, Scopes 41, Users 38, Profile 5 — có lẫn vài bước mở URL, cần lọc tay)
- Đã sửa: chưa sửa sản phẩm; câu rule đã duyệt ngày 05/10, chép vào rule, skill bằng tài liệu cập nhật gộp
- Cách kiểm: tìm trong Expected chuỗi "}} (", "Ở cả hai", "giống TC_" → 0 kết quả; đọc lại Step của các TC trên
- Gate: mức 1 · nâng mức 3 được cho phần tìm chuỗi
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 7 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-???[pre-condition] · Pre-condition đăng nhập ghi bằng vai trò: "Đăng nhập với acc Customer Admin"
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Nếu đăng nhập thì ghi: Đăng nhập với acc Customer Admin"
- Loại: L4-mẫu
- Địa chỉ: rules/tc-authoring.md#14 · rules/tc-authoring.md#22 · rules/tc-authoring.md#24 (bản cập nhật v0.3, chờ duyệt) · skills/tc-authoring/SKILL.md (mô tả, đầu-ra, bước-5, bước-7) · references/templates.md#1 · references/format.md#4 · scripts/tc_check.py
- Tiêu chí kiểm: dòng đăng nhập trong Pre-condition ghi tên vai trò bằng chữ, theo ngôn ngữ của file TC: tiếng Anh "Logged in as <role>" (vd "Logged in as Customer Admin"), không cần đăng nhập thì "Not logged in"; tiếng Việt "Đăng nhập với acc <vai trò>", "Chưa đăng nhập"; dữ liệu ghi thẳng giá trị cụ thể, nhãn ghi nguyên văn, không ô nào ở Pre-condition, Step, Expected còn dạng {{...}}; rule và skill tc-authoring không còn khoá, sheet `_Data`, `_Labels`
- Phạm vi ảnh hưởng: 199 TC có Pre-condition dùng khoá {{user.…}} (Login 10, Scopes 115, Users 62, Profile 12); 175 TC dùng khoá dữ liệu khác như {{scope.org}}, {{email.new}}; gộp lại 248/256 TC, 422 ô ở Pre-condition, Step, Expected còn dạng {{…}} (đếm bằng script trên bản v1.3). Rule và skill: rules/tc-authoring.md rule 14, 22 và rule 24 bản v0.3; SKILL.md 4 chỗ; templates.md §1–§3; format.md §4; tc_check.py 6 chỗ
- Xung đột: rule 14 yêu cầu dữ liệu và nhãn viết dạng khoá {{...}}; rule 24 (đang chờ duyệt) ghi vai trò bằng khoá {{user.…}}. Hai lựa chọn: (1) vai trò viết bằng chữ, khoá chỉ dùng cho dữ liệu như email, tên scope — dễ đọc, lọc theo chữ "Customer Admin" vẫn ra danh sách chạy của từng vai trò; (2) bỏ hẳn khoá, ghi giá trị mẫu cụ thể — dễ đọc nhất, nhưng dữ liệu đổi thì phải sửa nhiều chỗ
- Đã sửa: chưa sửa sản phẩm; rule 14, 22, 24 và skill v0.3 theo tài liệu cập nhật gộp ngày 05/10
- Cách kiểm: tìm "{{" ở Pre-condition, Step, Expected của mọi sheet TC → 0 kết quả; tìm "{{", "_Data", "_Labels" trong rules/tc-authoring.md và skills/tc-authoring → chỉ còn ở dòng changelog v0.3; file TC tiếng Anh: Pre-condition dòng nào cũng mở đầu bằng "Logged in as" hoặc "Not logged in"
- Gate: mức 1 · đề xuất nâng mức 3 khi viết lại TC: tc_check.py báo ô TC còn "{{"
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna chọn cách của mình, nguyên văn: "Cái này có xung đột, do 1 phần tôi lấy rule từ dự án dev làm cho FEEC, đứng trên lập trường code của dev, còn hiện tại đang dùng cho Tester, đứng ở 2 góc nhìn khác nhau nên t có thể dùng cái của tôi cho hợp lý nhé". Xung đột đã có lời giải: file TC viết cho Tester, nên Pre-condition ghi vai trò bằng chữ ("Đăng nhập với acc Customer Admin"). Rule 14 (dữ liệu, nhãn viết dạng khoá {{...}}) đến từ góc nhìn của dev, không áp cho file TC của Tester: khi sửa rule thì ghi bãi bỏ trong changelog, không xoá dòng cũ; rule 24 (chờ duyệt) đổi thành ghi vai trò bằng chữ. Trạng thái chuyển từ Chưa rõ phạm vi sang Mới.
- Cập nhật: 2026-10-05 · [Cách hiểu của AI, chờ Hanna xác nhận] Dữ liệu khác (tên scope, email…) cũng bỏ khoá, viết bằng chữ dễ đọc; cần giá trị cụ thể thì ghi ví dụ.
- Cập nhật: 2026-10-05 · Hanna chốt bỏ hẳn, nguyên văn: "tôi cảm thấy toàn bộ các nội dung dưới đây đều ko phù hợp với testing > tôi thấy cần loại bỏ toàn bộ các rule dưới đây". Các nội dung được nhắc: rule 14 (dữ liệu, nhãn viết dạng khoá {{...}}, khai ở `_Data`, `_Labels`); phần khoá trong rule 24 của bản cập nhật v0.3; sheet `_Data`, `_Labels` trong skill và phần kiểm khoá của `tc_check.py`. Thay cho cách làm ở dòng cập nhật thứ nhất: rule 14 không giữ dòng cũ, không ghi bãi bỏ, mà viết lại thành cách viết của Tester (đăng nhập ghi "Đăng nhập với acc <vai trò>", dữ liệu ghi thẳng giá trị cụ thể, nhãn ghi nguyên văn ngay trong ô); rule 22, rule 24 không còn khoá; bỏ `_Data`, `_Labels` và phần kiểm khoá. Dòng cập nhật thứ hai (dữ liệu khác cũng bỏ khoá) không còn là cách hiểu chờ xác nhận, vì rule 14 bỏ hẳn, gồm cả dữ liệu và nhãn. Địa chỉ, Tiêu chí kiểm, Phạm vi ảnh hưởng, Đã sửa, Cách kiểm, Gate sửa theo; Trạng thái chuyển từ Mới sang Đã vào rule (chờ duyệt). Rule, skill sửa trong tài liệu cập nhật gộp ngày 05/10.
- Cập nhật: 2026-10-05 · File TC SGS DTP chuyển sang tiếng Anh (FB-???[tieng-anh], cùng ngày). Ở câu hỏi chọn đáp án "Dòng đăng nhập ở Pre-condition ghi bằng tiếng Anh thế nào?", Hanna chọn "Logged in as <role>"; màn không cần đăng nhập ghi "Not logged in". [Đề xuất của AI, chờ duyệt] rule 14 ghi cả hai dạng: tiếng Anh như trên, tiếng Việt "Đăng nhập với acc <vai trò>", "Chưa đăng nhập" cho dự án viết TC bằng tiếng Việt. Tiêu chí kiểm, Cách kiểm sửa theo.
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 2 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-???[moi-dong] · Nhiều mục thì mỗi mục một dòng, không nối bằng " · "
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Không viết thành 1 dòng: Bảng 3 cột: User · Role · Given mà viết theo format" · "User." · "Role." · "Given."
- Loại: L4-mẫu
- Địa chỉ: rules/tc-authoring.md#12 · skills/tc-authoring/references/format.md
- Tiêu chí kiểm: Expected có từ hai mục trở lên (cột, trường, lựa chọn, nút) thì xuống dòng, mỗi mục một dòng "- <mục>"
- Phạm vi ảnh hưởng: 16 TC ở Scopes có Expected nối nhiều mục bằng " · " (vd TC_038, TC_041, TC_102). Lưu ý: vài chỗ " · " là chữ thật trên giao diện (vd dòng phụ "Organization scope · <tên công ty>"), những chỗ đó giữ nguyên
- Đã sửa: chưa sửa sản phẩm; câu rule đã duyệt ngày 05/10, chép vào rule, skill bằng tài liệu cập nhật gộp
- Cách kiểm: tìm " · " trong Expected, chỉ còn các chỗ là chữ thật trên giao diện
- Gate: mức 3 · tc_check.py cảnh báo Expected có " · "
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 8 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-???[gia-tri-tinh] · Giá trị tính toán phải nói lấy từ đâu; TC phải dễ sửa khi Figma, UC đổi
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Cần thể hiện số lượng User ở bảng scope lấy thông tin ở đâu, tương tự Evidence coverage lấy ở đâu... Cái này cần thảo luận thêm hiển thị ntn thì hợp logic, dễ nhìn, ngoài ra cái figma hay UC này có thể chưa pải là bản cuối, nên TCs cũng cần thích nghi để sau có thể dễ dàng sửa đổi."
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#12 · skills/tc-authoring/SKILL.md#bước-4
- Tiêu chí kiểm: chưa chốt — cần thảo luận cách ghi nguồn và cách tính của giá trị hiển thị, và cách viết để dễ sửa khi Figma, UC đổi
- Phạm vi ảnh hưởng: Scopes TC_041–TC_044 (cột Frameworks, Users, Evidence coverage), TC_078 (Coverage ở khối Frameworks), TC_114 (Evidence coverage ở Summary)
- Liên quan: Q-S-11 (Evidence coverage có trong P1 không), Q-S-12 (cột Users có tính Customer Admin không)
- Đã sửa: chưa
- Cách kiểm: chưa có, chờ chốt tiêu chí
- Gate: chưa có
- Trạng thái: Bị bác
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna bỏ qua, nguyên văn: "mình bỏ qua cả phần này nhé, đã có figma và UC là nguồn tài liệu r" (trả lời câu hỏi chọn chỗ ghi cách tính và nguồn của giá trị tính toán). Không sinh rule: giá trị tính toán làm theo rule chung — Expected theo Figma và UC; Figma, UC chưa nói thì để trống và ghi câu hỏi (rule 13). Các câu hỏi về sản phẩm Q-S-11, Q-S-12 vẫn giữ trong file TC. Trạng thái chuyển từ Chưa rõ phạm vi sang Bị bác.

## FB-???[xem-truoc] · Gửi bản xem trước danh sách tính năng trước khi cập nhật file TC
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Ngoài ra chúng ta nên liệt kê các tính năng ở dạng gửi xem trước thay vì mỗi bản lại cần update file TCs nhiều lần"
- Loại: L2-rule
- Địa chỉ: skills/tc-authoring/SKILL.md (thêm bước xem trước, trước Bước 6 Dựng file) · CLAUDE.md#cổng-con-người
- Tiêu chí kiểm: trước khi ghi vào file TC, gửi bản xem trước gồm chức năng → nhóm kiểm → tên case, mỗi dòng đánh dấu Mới / Sửa / Bỏ; chỉ ghi file sau khi người dùng duyệt
- Phạm vi ảnh hưởng: ngày 05/10 file TC đã ra hai bản liền nhau (v1.2, v1.3)
- Đã sửa: chưa sửa sản phẩm; câu rule đã duyệt ngày 05/10, chép vào rule, skill bằng tài liệu cập nhật gộp
- Cách kiểm: lần cập nhật file TC kế tiếp có bản xem trước được duyệt đi trước
- Gate: mức 1
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna nói rõ thêm, nguyên văn: "cái này là tùy ko pải lúc nào cugnx làm, khi chung ta chưa thống nhất đc rule để còn viết tiếp thì tạm thời ko gửi quá nhiều lần file TCs > phân gửi TCs sau khi đã chốt hoàn chỉnh với nhau thì mới gửi sau > nếu thấy có vấn đề thì cứ gửi luôn cũng dc, tùy b". Tiêu chí kiểm mới: khi rule viết TC chưa chốt thì không gửi file TC nhiều lần; chốt xong rule mới gửi file TC; bản xem trước không bắt buộc; thấy có vấn đề cần Hanna xem ngay thì được gửi sớm. Cách kiểm mới: từ lúc ghi FB này tới khi chốt xong các FB cách viết TC, không có bản file TC nào gửi đi chỉ vì sửa từng chỗ nhỏ.
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 9 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-???[api] · TC gọi API chỉ viết khi tester được gọi API, và để ở sheet API riêng
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "t chưa hiểu cách viết có tên API có mục đích gì, hiện tại chúng ta ko có API cho tester vào check, nếu có thì cần viết ở mục riêng như kiểu test API , security ..." · câu hỏi chọn đáp án "Nhóm Bảo mật (Security) hiện nằm cuối mỗi sheet màn hình … có tách ra mục riêng giống API không?": Hanna chọn "Chỉ tách TC gọi API" (đáp án do AI soạn)
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#29 (mới) · rules/tester.md#5 · skills/tc-authoring/SKILL.md#đầu-ra · skills/tc-authoring/references/patterns.md (P5; mục "Bảy chỗ bộ TC thật hay thiếu" #3) · skills/test-design/references/coverage-checklist.md · skills/test-design/references/techniques.md · skills/test-design/references/tc-framework.md · projects/_template/profile.md · projects/sgs-dtp/profile.md · sản phẩm: SGS-DTP_TestCase1 Login!TC_051 · Scopes!TC_119, 120, 123, 126, 127 · Users!TC_054, 055, 056, 058, 059, 060
- Tiêu chí kiểm: dự án mà profile.md ghi tester không được gọi API thì sheet màn hình không có TC nào cần gọi thẳng API; khi được gọi API thì các TC đó nằm ở sheet `API` riêng; TC bảo mật làm được trên giao diện hoặc trình duyệt (chèn thẻ script, Quay lại sau khi đăng xuất, mở URL của tenant khác, xem mã trang, xem tab Network) vẫn ở cuối sheet màn hình
- Phạm vi ảnh hưởng: SGS-DTP_TestCase1_v1.3 có 12 TC cần gọi API — 9 TC chỉ gọi API (Login TC_051; Scopes TC_119, 120, 126, 127; Users TC_054, 058, 059, 060), 3 TC có cả bước giao diện và bước gọi API (Scopes TC_123; Users TC_055, 056). Rule, skill: rules/tester.md rule 5 (1 chỗ); tc-authoring patterns.md (2 chỗ: P5, mục "Bảy chỗ" #3); test-design coverage-checklist.md (3 chỗ), techniques.md (6 chỗ), tc-framework.md (5 chỗ). Không thuộc phạm vi: rules/automation.md rule 4 (code Playwright chuẩn bị dữ liệu qua API), dòng "Dịch vụ ngoài lỗi hoặc chậm (API tích hợp…)" của tc-framework.md
- Liên quan: rule 11 (TVP_ID của TC bỏ đi không dùng lại)
- Đã sửa: chưa sửa sản phẩm; câu rule đã duyệt ngày 05/10, chép vào rule, skill bằng tài liệu cập nhật gộp
- Cách kiểm: tìm "API" ở Classification, Test case name, Step, Expected của các sheet màn hình → 0 kết quả, trừ chỗ là chữ trên giao diện; profile.md của dự án có dòng "Tester được gọi API"
- Gate: mức 1
- Trạng thái: Đã duyệt
- Tái phát: 0
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 10–12 trong chat 05/10: rule 29 mới; tester.md rule 5, patterns.md P5 và 14 chỗ "UI và API" ở skill test-design; dòng "Tester được gọi API" ở profile.md, SGS DTP ghi Không), nguyên văn: "duyệt". Trạng thái chuyển từ Mới sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

```

## 2. `feedback/log.md`

**2.1 · Cuối bản ghi FB-010, thêm dòng Cập nhật. Tìm**

```text
- Gate: mức 3 · tc_check.py
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-011 ·
```

**Thay bằng**

```text
- Gate: mức 3 · tc_check.py
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-05 · Rule 3 nói rõ "màn hình" tính theo mục menu: danh sách, chi tiết, hộp thoại mở từ cùng một mục menu nằm chung một sheet, như sheet Scopes. Vai trò, gộp và tách sheet chuyển sang mục G. Xem FB-???[chia-sheet], FB-???[gop-tach-sheet].

## FB-011 ·
```

**2.2 · Cuối bản ghi FB-013, thêm dòng Cập nhật (đề xuất căn lề, chờ duyệt). Tìm**

```text
- Tái phát: 0

## FB-014 ·
```

**Thay bằng**

```text
- Tái phát: 0
- Cập nhật: 2026-10-05 · [Đề xuất của AI, chờ duyệt] Rà theo file mẫu khi xử lý FB-016 tái phát: ô dữ liệu ở cả file mẫu SGS và FEEC căn giữa theo chiều dọc, còn rule 19 và format.md §4 ghi căn trên; câu gốc của FB này chỉ nói "căn trái". Đề xuất sửa rule 19, format.md §4 và tc_build_xlsx.py thành căn giữa theo chiều dọc, như file mẫu (tài liệu cập nhật gộp ngày 05/10).

## FB-014 ·
```

**2.3 · Cuối bản ghi FB-016: Tái phát 0 → 1, thêm dòng Cập nhật. Tìm**

```text
- Tái phát: 0

## FB-017 ·
```

**Thay bằng**

```text
- Tái phát: 1
- Cập nhật: 2026-10-05 · Tái phát. Hanna chỉ ra, nguyên văn: "Create: Hanna > cùng 1 font chữ nhé" (ảnh ô Scopes!C5). Ô Scopes!C5 (Creator = Hanna) dùng Arial 10, mọi ô khác Times New Roman 10; quét cả 7 sheet của SGS-DTP_TestCase1_v1.3 thì chỉ có ô này. tc_check.py có báo "Scopes · 1 ô sai phông: C5=Arial" nhưng lẫn trong 14 lỗi màu giả: bảng màu ở format.md §4 và trong hai script (17324D, EAE7E1, FFFFFF, C9C5BE) không khớp file TC mẫu (00B0F0, 363A45, FBE9E7, B8362B; file mẫu SGS và FEEC giống nhau). AI bỏ qua cả loại lỗi màu nên sót lỗi phông. Cảnh báo ký tự ngoài bảng chữ Latin cũng báo giả 17/27 dòng vì dấu · — ←. Sửa gate (chờ duyệt, ở tài liệu cập nhật gộp ngày 05/10): bảng màu theo file mẫu ở format.md §4, tc_check.py, tc_build_xlsx.py; cảnh báo ký tự bỏ qua dấu câu; SKILL Bước 7 thêm "không bỏ qua cả một loại lỗi; lỗi giả thì sửa bảng màu hoặc script trước". Kiểm: với bảng màu mới, tc_check.py trên v1.3 chỉ còn 1 lỗi (C5); sửa C5 xong còn 0 lỗi; cảnh báo ký tự còn 10 dòng, đều là nhãn giao diện 繁體中文 ở Profile. Đã sửa C5 ở bản làm việc, vào file TC bản tới.

## FB-017 ·
```

**2.4 · Cuối bản ghi FB-019, thêm dòng Cập nhật. Tìm**

```text
- Tái phát: 0

## FB-020 ·
```

**Thay bằng**

```text
- Tái phát: 0
- Cập nhật: 2026-10-05 · tc_check.py bỏ phần kiểm khoá {{…}} theo FB-???[pre-condition], nên phần "khoá {{…}}" trong Tiêu chí kiểm không còn áp dụng; chuẩn hoá NFC vẫn cần cho phần so từ mơ hồ. Cảnh báo chữ tiếng Việt mới (`--lang en`) đã chuẩn hoá NFC trước khi so.

## FB-020 ·
```

## 3. `rules/tc-authoring.md`

**3.1 · Dòng Phiên bản (đầu file). Tìm**

```text
Phiên bản: v0.2 ·
```

**Thay bằng**

```text
Phiên bản: v0.3 ·
```

**3.2 · Rule 3, mục B · chia sheet (chờ duyệt). Tìm**

```text
3. **Một màn hình một sheet.** Tên sheet lấy đúng tên mục menu của hệ thống, không dịch, không viết tắt.
```

**Thay bằng**

```text
3. **Một màn hình một sheet.** Màn hình tính theo mục menu: danh sách, chi tiết, hộp thoại, panel mở từ cùng một mục menu mặc định nằm chung một sheet, như sheet `Scopes` gồm cả Danh sách và Chi tiết; phần nào đủ lớn thì tách (rule 25). Tên sheet lấy đúng tên mục menu của hệ thống, không dịch, không viết tắt; sheet tách ra thì lấy tên màn như trên giao diện. Vai trò, gộp và tách: mục G.
```

**3.3 · Rule 4 · trạng thái rỗng đặt trước. Tìm**

```text
4. Trong sheet, TC xếp theo **khu vực**; thứ tự khu vực theo mắt đọc: trên → dưới trong một cột, hết cột trái sang cột phải.
```

**Thay bằng**

```text
4. Trong sheet, TC xếp theo **khu vực**; thứ tự khu vực theo mắt đọc: trên → dưới trong một cột, hết cột trái sang cột phải. Màn có danh sách thì xếp theo vòng đời dữ liệu trước: mở màn → trạng thái rỗng (Empty state) → tạo mới → các khu vực cần có dữ liệu (bảng, tìm kiếm, lọc, phân trang); trong từng chặng vẫn theo mắt đọc.
```

**3.4 · Rule 7 · ví dụ tiếng Anh, mỗi ô một thứ tiếng. Tìm**

```text
| **I** | Feature — khối chức năng người dùng gọi tên được | `Đăng nhập - Login` |
| **II** | Khu vực trên màn, hoặc nhóm kiểm | `Email` · `Bảo mật - Security` |
| **III** | Mục kiểm, hoặc nhóm kết quả | `Thành công` · `Không thành công` · `Kiểm tra dữ liệu` |
| **IV** | Case cụ thể, mỗi dòng một case | `Bỏ trống` · `Sai định dạng` |
```

**Thay bằng**

```text
| **I** | Feature — khối chức năng người dùng gọi tên được | `Login` |
| **II** | Khu vực trên màn, hoặc nhóm kiểm | `Email` · `Security` |
| **III** | Mục kiểm, hoặc nhóm kết quả | `Success` · `Failure` · `Validation` |
| **IV** | Case cụ thể, mỗi dòng một case | `Empty` · `Invalid format` |

Ví dụ trên là file TC tiếng Anh. Mỗi ô ghi một thứ tiếng theo ngôn ngữ của file (rule 16), vd `Login`, không ghi `Đăng nhập - Login`. Tên nhóm kiểm dùng bảng từ cố định ở `references/format.md` §7.
```

**3.5 · Rule 12 · không trỏ sang TC khác, mỗi mục một dòng. Tìm**

```text
12. Kết quả mong đợi phải **quan sát được**: text nguyên văn, màn hình đích, trạng thái, dữ liệu thay đổi. Cấm "hoạt động bình thường", "hiển thị đúng", "thành công" mà không nói thấy gì.
```

**Thay bằng**

```text
12. Kết quả mong đợi phải **quan sát được**: text nguyên văn, màn hình đích, trạng thái, dữ liệu thay đổi. Cấm "hoạt động bình thường", "hiển thị đúng", "thành công" mà không nói thấy gì; tiếng Anh cũng vậy, vd "works normally", "displays correctly", "as expected".
    - Ghi thẳng trong ô: không trỏ sang TC khác ("giống TC_006"), không ghi "ở cả hai màn" mà không nêu tên từng màn.
    - Từ hai mục trở lên (cột, trường, lựa chọn, nút) thì mỗi mục một dòng `- <mục>`, không nối bằng " · "; chỉ giữ " · " khi đó là chữ thật trên giao diện.
```

**3.6 · Rule 14 · viết lại cả dòng, không giữ dòng cũ. Tìm**

```text
14. Dữ liệu cụ thể và nhãn giao diện viết dạng khoá `{{...}}`, khai ở sheet `_Data` và `_Labels`. Không gõ thẳng giá trị vào TC.
```

**Thay bằng**

```text
14. **Viết bằng chữ, cho Tester đọc là chạy được.**
    - Dòng đăng nhập ở Pre-condition: file TC tiếng Anh ghi `Logged in as <role>`, vd `Logged in as Customer Admin`; màn không cần đăng nhập ghi `Not logged in`. File TC tiếng Việt ghi `Đăng nhập với acc <vai trò>` và `Chưa đăng nhập`.
    - Dữ liệu ghi thẳng giá trị cụ thể, nhãn giao diện ghi đúng nguyên văn, ngay trong ô của TC.
    - Step là thao tác cụ thể, vd `1. Click a scope in the list`, `2. Observe the scope detail`; không ghi chung chung kiểu "Mở …". Chưa biết thao tác hay kết quả thì để trống và ghi câu hỏi (rule 13).
```

**3.7 · Rule 15 · tên nhóm tiếng Anh, case Bảo mật làm được trên giao diện. Tìm**

```text
15. Mỗi khu vực có thao tác ghi dữ liệu phải có đủ: ít nhất một case Thành công, một case Không thành công, một case Phân quyền, một case Bảo mật.
```

**Thay bằng**

```text
15. Mỗi khu vực có thao tác ghi dữ liệu phải có đủ: ít nhất một case Thành công, một case Không thành công, một case Phân quyền, một case Bảo mật (file tiếng Anh: Success, Failure, Permission, Security). Case Bảo mật là case tester làm được trên giao diện hoặc trình duyệt; case cần gọi thẳng API theo rule 29.
```

**3.8 · Rule 16 · ngôn ngữ file TC theo profile.md. Tìm**

```text
16. Hệ thống chạy ngôn ngữ nào thì TC viết theo nhãn ngôn ngữ đó. Khi chuyển ngôn ngữ cho bộ TC có sẵn:
```

**Thay bằng**

```text
16. **Ngôn ngữ của file TC theo dòng "Ngôn ngữ viết file TC" trong `profile.md` của dự án**, áp cho mọi sheet, mọi cột; phần ngoại lệ (vd cột `Open question` và sheet `Cần xác nhận` viết tiếng Việt) cũng ghi ở dòng đó. Nhãn giao diện luôn ghi đúng nguyên văn theo ngôn ngữ hệ thống đang chạy, kể cả chữ hoa chữ thường, vd `Create scope`. Khi chuyển ngôn ngữ cho bộ TC có sẵn:
```

**3.9 · Rule 19 · căn giữa theo chiều dọc như file mẫu (đề xuất, chờ duyệt). Tìm**

```text
19. **Căn lề trái** cho mọi ô. Ô đã gộp căn giữa theo chiều dọc; ô dữ liệu căn trên theo chiều dọc.
```

**Thay bằng**

```text
19. **Căn lề trái** cho mọi ô. Ô đã gộp và ô dữ liệu căn giữa theo chiều dọc, như file TC mẫu.
```

**3.10 · Rule 22, mục F, câu cuối · bỏ `_Data`, `_Labels`. Tìm**

```text
Sheet phụ (`Cover`, `Hướng dẫn`, `_Data`, `_Labels`, `FLOW-nn`, `Test_Report`) theo cùng quy ước với sheet màn hình.
```

**Thay bằng**

```text
Sheet phụ (`Cover`, `Hướng dẫn`, `FLOW-nn`, `Test_Report`) theo cùng quy ước với sheet màn hình.
```

**3.11 · Thêm mục G (rule 24–28 chia sheet, chờ duyệt; rule 29 API) ngay trước Changelog. Tìm**

```text
## Changelog
```

**Thay bằng**

```text
## G. Chia sheet

24. **Không chia sheet theo vai trò.** Màn nhiều vai trò dùng, hoặc có ở nhiều portal, vẫn là một sheet. Vai trò nằm trong sheet:
    - Pre-condition của mọi TC mở đầu bằng dòng đăng nhập theo rule 14 (`Logged in as <role>` hoặc `Not logged in`; file tiếng Việt: `Đăng nhập với acc <vai trò>`, `Chưa đăng nhập`), kể cả khi đã có điều kiện dữ liệu. Lọc cột Pre-condition theo tên vai trò là ra danh sách chạy của vai trò đó, nên tên vai trò ghi đúng như tài liệu yêu cầu.
    - Khác biệt giữa các vai trò viết ở nhóm Phân quyền cuối sheet (rule 15).
    - Chức năng có màn ở nhiều portal thì thêm tên portal vào đầu Classification I, vd `[SGS] Certification list`.
    - Ngoại lệ: màn mà mỗi vai trò thấy một nội dung khác hẳn, vd dashboard theo vai trò, thì Classification I là vai trò.
25. **Gộp, tách theo màn hình, không theo module của UC list.** Module chỉ để tham khảo; việc nối TC về UC do cột UC của từng dòng đảm nhận.
    - Hai module nằm trên cùng một màn thì gộp một sheet. Một module trải qua nhiều màn lớn thì tách theo màn.
    - UC do System thực hiện mà không có màn riêng thì không có sheet riêng; kiểm ở nơi kết quả hiện ra, vd ghi vết kiểm ở nhóm Ghi vết của sheet có hành động.
    - Màn chưa có thiết kế thì chưa tạo sheet. UC chưa chốt có làm hay không thì chưa viết TC. UC đã chốt nhưng còn câu hỏi chi tiết thì vẫn viết, phần còn mở ghi `Open question` (rule 13).
    - Sheet nhỏ không sao; sheet trộn nhiều màn không liên quan thì tách.
26. **Một form chỉ test đầy đủ ở một sheet**, là sheet của màn chủ của form. Đường vào form từ màn khác chỉ kiểm mở đúng form và giá trị điền sẵn.
27. **TC điểm hiển thị đặt ở sheet của hành động** (rule 9), kể cả khi điểm đó ở màn khác hay vai trò khác: làm bằng vai trò A, tải lại trang, kiểm bằng vai trò B (pattern P5). Chuỗi nhiều hành động qua nhiều chức năng, dữ liệu tạo ngay trong luồng, thì đưa vào `FLOW-nn` (rule 5).
28. **Cover có bảng UC → sheet.** Mỗi UC của baseline đúng một dòng; cột Sheet ghi một trong ba: tên sheet · `Chờ: <lý do>` · `Kiểm ở: <sheet>`. Cột UC của TC dùng ID của baseline hiện hành, không dùng ID của nguồn cũ; baseline đổi ID thì đổi theo trước khi chia lại sheet.
29. **TC chỉ viết những gì tester làm được bằng công cụ đang có.** TC gọi thẳng API chỉ viết khi `profile.md` của dự án ghi tester được gọi API, và đặt ở sheet `API` riêng, không trộn vào sheet màn hình. Mở trang bằng URL, xem mã trang hay xem tab Network trên trình duyệt vẫn tính là thao tác giao diện. TC bảo mật làm được trên giao diện giữ ở cuối sheet màn hình.

## Changelog
```

**3.12 · Dòng changelog. Tìm**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
```

**Thay bằng**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.3 | 2026-10-05 | Rule 3: "màn hình" tính theo mục menu. Rule 4: màn có danh sách xếp theo vòng đời dữ liệu, trạng thái rỗng trước. Rule 7: ví dụ tiếng Anh, mỗi ô một thứ tiếng, tên nhóm kiểm theo bảng từ. Rule 12: không trỏ sang TC khác, mỗi mục một dòng. Rule 14 viết lại theo góc nhìn Tester: dòng đăng nhập `Logged in as <role>`, dữ liệu và nhãn ghi thẳng trong ô, Step là thao tác cụ thể. Rule 15: tên nhóm tiếng Anh, case Bảo mật làm được trên giao diện. Rule 16: ngôn ngữ file TC theo `profile.md`. Rule 22 bỏ sheet `_Data`, `_Labels`. Thêm mục G: chia sheet (rule 24–28) và rule 29 — TC gọi API chỉ khi tester được gọi API, ở sheet `API` riêng. Hanna duyệt 05/10, trừ phần **chờ duyệt**: rule 3 và 24–28 (chia sheet), rule 19 (căn giữa theo chiều dọc như file mẫu, đề xuất của AI). | FB-???[chia-sheet] · FB-???[gop-tach-sheet] · FB-???[pre-condition] · FB-???[tieng-anh] · FB-???[rong-truoc] · FB-???[khong-lung-lo] · FB-???[moi-dong] · FB-???[api] · FB-013 |
```

## 4. `rules/common.md`

**4.1 · Dòng Phiên bản (đầu file). Tìm**

```text
Phiên bản: v0.3 · Luôn nạp
```

**Thay bằng**

```text
Phiên bản: v0.4 · Luôn nạp
```

**4.2 · Rule 6 · ngôn ngữ file test case. Tìm**

```text
6. Giữ nguyên văn text gốc của yêu cầu và text giao diện (nhãn trường, nút, thông báo), không dịch. Phần phân tích viết tiếng Việt.
```

**Thay bằng**

```text
6. Giữ nguyên văn text gốc của yêu cầu và text giao diện (nhãn trường, nút, thông báo), không dịch. Phần phân tích viết tiếng Việt; file test case viết theo ngôn ngữ ghi ở `profile.md` của dự án (`rules/tc-authoring.md` rule 16).
```

**4.3 · Dòng changelog. Tìm**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
```

**Thay bằng**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.4 | 2026-10-05 | Rule 6: file test case viết theo ngôn ngữ ghi ở `profile.md` của dự án. Hanna duyệt 05/10. | FB-???[tieng-anh] |
```

## 5. `rules/tester.md`

**5.1 · Dòng Phiên bản (đầu file). Tìm**

```text
Phiên bản: v0.2 · Nạp cùng
```

**Thay bằng**

```text
Phiên bản: v0.3 · Nạp cùng
```

**5.2 · Rule 5, dòng thứ tư · phân quyền âm và API. Tìm**

```text
   - mỗi hành động ghi dữ liệu có TC cho vai trò không được phép: bị ẩn trên UI và bị chặn ở API;
```

**Thay bằng**

```text
   - mỗi hành động ghi dữ liệu có TC cho vai trò không được phép: nút bị ẩn trên UI và mở thẳng URL cũng bị chặn; kiểm API bị chặn chỉ khi `profile.md` ghi tester được gọi API, viết ở sheet `API` riêng (`rules/tc-authoring.md` rule 29);
```

**5.3 · Dòng changelog. Tìm**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
```

**Thay bằng**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.3 | 2026-10-05 | Rule 5: phân quyền âm kiểm trên giao diện và URL; kiểm API chỉ khi tester được gọi API, ở sheet `API` riêng. Hanna duyệt 05/10. | FB-???[api] |
```

## 6. `.claude/skills/tc-authoring/SKILL.md`

**6.1 · Dòng `description:`, chỗ thứ nhất · chia sheet (chờ duyệt). Tìm**

```text
một màn hình một sheet, bốn cấp
```

**Thay bằng**

```text
một màn hình (tính theo mục menu) một sheet, vai trò nằm trong sheet, bốn cấp
```

**6.2 · Dòng `description:`, chỗ thứ hai · bỏ khoá. Tìm**

```text
dữ liệu và nhãn giao diện tách ra khoá {{...}},
```

**Thay bằng**

```text
vai trò, dữ liệu và nhãn ghi bằng chữ ngay trong ô,
```

**6.3 · Tiêu đề. Tìm**

```text
# Viết test case (v0.2)
```

**Thay bằng**

```text
# Viết test case (v0.3)
```

**6.4 · Mục Đầu ra · bỏ `_Data`, `_Labels`; thêm `Phân quyền` (chờ duyệt), `API`. Tìm**

```text
  Cover            thông tin bộ test, lịch sử thay đổi
  Hướng dẫn        quy ước, giải nghĩa bốn cấp, giá trị hợp lệ
  _Data            dữ liệu test dùng chung, gọi bằng {{...}}
  _Labels          nhãn giao diện nguyên văn, gọi bằng {{...}}
  _Patterns        checklist của từng loại khu vực
  <Màn hình>       mỗi màn một sheet
```

**Thay bằng**

```text
  Cover            thông tin bộ test, lịch sử thay đổi, bảng UC → sheet
  Hướng dẫn        quy ước, giải nghĩa bốn cấp, giá trị hợp lệ
  _Patterns        checklist của từng loại khu vực
  Phân quyền       tuỳ chọn: ma trận vai trò × UC, mỗi ô ghi TC ID đã phủ, không chứa TC
  <Màn hình>       mỗi màn một sheet, màn tính theo mục menu (rules/tc-authoring.md rule 3, mục G)
  API              tuỳ chọn: TC gọi thẳng API, chỉ khi profile.md ghi tester được gọi API (rule 29)
```

**6.5 · Bước 1 · thêm bước 4–6. Tìm**

```text
3. Chốt tên sheet theo tên mục menu của hệ thống.
```

**Thay bằng**

```text
3. Chốt tên sheet theo tên mục menu của hệ thống.
4. Lập bảng UC → sheet theo `rules/tc-authoring.md` mục G: mỗi UC của baseline đúng một chỗ — tên sheet, `Chờ: <lý do>` hoặc `Kiểm ở: <sheet>`. Ghi vào Cover. Mẫu: `references/templates.md` §4.
5. Liệt kê vai trò và phạm vi dữ liệu của từng vai trò (thấy dữ liệu nào, làm được gì). Tên vai trò lấy đúng như tài liệu yêu cầu, vì Pre-condition ghi vai trò bằng tên này (`rules/tc-authoring.md` rule 14).
6. Đọc `profile.md` của dự án: ngôn ngữ viết file TC (rule 16), tester có được gọi API không (rule 29), file TC mẫu.
```

**6.6 · Bước 4 · TC điểm hiển thị ở sheet của hành động (chờ duyệt). Tìm**

```text
Mỗi điểm hiển thị là một TC riêng. Điểm nào chỉ xuất hiện sau một hành động khác thì ghi rõ — đây là chỗ sai nhiều nhất.
```

**Thay bằng**

```text
Mỗi điểm hiển thị là một TC riêng. Điểm nào chỉ xuất hiện sau một hành động khác thì ghi rõ — đây là chỗ sai nhiều nhất.

TC điểm hiển thị viết ở sheet của hành động, kể cả khi điểm đó nằm ở màn khác hay vai trò khác (rule 27). Chỉ chuỗi nhiều hành động qua nhiều chức năng mới tách ra `FLOW-nn`.
```

**6.7 · Bước 5 · thứ tự nhóm, tên tiếng Anh, trạng thái rỗng trước. Tìm**

```text
Theo pattern của từng khu vực, theo thứ tự: hiển thị → nhập liệu → kiểm tra dữ liệu → thành công → không thành công → phân quyền → bảo mật.
```

**Thay bằng**

```text
Theo pattern của từng khu vực, theo thứ tự: hiển thị → nhập liệu → kiểm tra dữ liệu → thành công → không thành công → phân quyền → bảo mật (file tiếng Anh: Display → Input → Validation → Success → Failure → Permission → Security; bảng từ ở `references/format.md` §7). Màn có danh sách thì trạng thái rỗng đứng trước tạo mới và các khu vực cần dữ liệu (`rules/tc-authoring.md` rule 4).
```

**6.8 · Bước 5 · dòng cuối của "Quy tắc không được phá". Tìm**

```text
- giá trị và nhãn dùng khoá `{{...}}`.
```

**Thay bằng**

```text
- Pre-condition mở đầu bằng dòng đăng nhập theo `rules/tc-authoring.md` rule 14 (`Logged in as <role>` / `Not logged in`); dữ liệu và nhãn ghi thẳng trong ô;
- Step là thao tác cụ thể; Expected mỗi mục một dòng, không trỏ sang TC khác (rule 12, 14);
- không viết TC gọi thẳng API khi `profile.md` ghi tester không được gọi API (rule 29).
```

**6.9 · Bước 6 · chưa gửi file TC khi rule còn đang bàn. Tìm**

```text
Script tự: gộp ô bốn cột Classification theo quy tắc, đặt phông Times New Roman 10, căn trái, tô đỏ dòng còn câu hỏi mở, dựng khối thông tin đầu sheet và hàng tiêu đề hai tầng.
```

**Thay bằng**

```text
Script tự: gộp ô bốn cột Classification theo quy tắc, đặt phông Times New Roman 10, căn trái, tô đỏ dòng còn câu hỏi mở, dựng khối thông tin đầu sheet và hàng tiêu đề hai tầng.

Rule viết TC còn đang bàn với người dùng thì chưa gửi file TC; chốt xong mới gửi một lần. Bản xem trước (chức năng → nhóm kiểm → tên case, đánh dấu Mới / Sửa / Bỏ) là tuỳ chọn. Thấy vấn đề cần người dùng xem ngay thì gửi sớm.
```

**6.10 · Bước 7, câu "Script báo" · bỏ phần kiểm khoá. Tìm**

```text
dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khoá `{{...}}` chưa có trong `_Data`/`_Labels` · khu vực thiếu nhóm bắt buộc
```

**Thay bằng**

```text
dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khu vực thiếu nhóm bắt buộc
```

**6.11 · Bước 7 · `--lang en`; không bỏ qua cả một loại lỗi (câu sau, chờ duyệt). Tìm**

```text
Sửa đến khi script sạch, hoặc ghi lý do loại trừ.
```

**Thay bằng**

```text
Chạy thêm `--lang en` khi `profile.md` ghi file TC viết tiếng Anh: script cảnh báo ô còn chữ tiếng Việt, trừ cột `Open question` và sheet `Cần xác nhận`.

Sửa đến khi script sạch, hoặc ghi lý do loại trừ từng dòng. Không bỏ qua cả một loại lỗi: lỗi giả thì sửa bảng màu hoặc script trước, vì lỗi thật có thể nằm lẫn trong đó.
```

**6.12 · Dòng changelog. Tìm**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
```

**Thay bằng**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.3 | 2026-10-05 | Vai trò, dữ liệu, nhãn ghi bằng chữ ngay trong ô (`rules/tc-authoring.md` rule 14); bỏ sheet `_Data`, `_Labels` khỏi Đầu ra, Bước 7, `tc_check.py`, `references/templates.md`, `references/format.md`. Đầu ra: Cover thêm bảng UC → sheet; thêm sheet `Phân quyền` và `API` tuỳ chọn. Bước 1 thêm bước 4–6: bảng UC → sheet, vai trò, đọc `profile.md`. Bước 4: TC điểm hiển thị ở sheet của hành động. Bước 5: thứ tự nhóm bằng tiếng Anh, trạng thái rỗng trước, quy tắc Pre-condition, Step, Expected, API. Bước 6: chưa gửi file TC khi rule còn đang bàn. Bước 7: `--lang en`, không bỏ qua cả một loại lỗi. `references/format.md`: bảng màu theo file TC mẫu, bảng từ tên nhóm kiểm (§7). `references/patterns.md`: P5, P12, mục hay thiếu #3. `tc_check.py`: bảng màu mới, câu mơ hồ tiếng Anh, nhóm Success/Failure, `--lang en`, cảnh báo ký tự bỏ qua dấu câu, bỏ qua sheet `Phân quyền`. `tc_build_xlsx.py`: bảng màu mới. Hanna duyệt 05/10, trừ phần **chờ duyệt**: chia sheet (Đầu ra, Bước 1 bước 4, Bước 4, sheet `Phân quyền`), câu "không bỏ qua cả một loại lỗi" ở Bước 7, bảng màu và căn giữa theo chiều dọc (đề xuất của AI theo file mẫu). | FB-???[chia-sheet] · FB-???[gop-tach-sheet] · FB-???[pre-condition] · FB-???[tieng-anh] · FB-???[rong-truoc] · FB-???[rong-du] · FB-???[khong-lung-lo] · FB-???[moi-dong] · FB-???[xem-truoc] · FB-???[api] · FB-016 · FB-013 |
```

## 7. `.claude/skills/tc-authoring/references/templates.md`

**7.1 · Mục 1, hai dòng mẫu của TSV · viết tiếng Anh. Tìm**

```text
Đăng nhập - Login	Email	Hiển thị	Mặc định	High	Kiểm tra hiển thị mặc định của trường Email	Chưa đăng nhập, mở {{url.customer}}	1. Kiểm tra trường Email	- Nhãn: Email kèm dấu * đỏ\n- Placeholder: name@company.com	AUTH-001	
Đăng nhập - Login	Email	Kiểm tra dữ liệu	Bỏ trống	High	Kiểm tra bỏ trống Email rồi đăng nhập	Chưa đăng nhập	1. Để trống Email\n2. Bấm Sign in	- Không gọi đăng nhập\n- Hiện lỗi dưới trường Email	AUTH-001	Text lỗi nguyên văn → Q-L-01
```

**Thay bằng**

```text
Login	Email	Display	Default	High	Verify the default display of the Email field	Not logged in, open the Customer Portal sign-in page	1. Observe the Email field	- Label: Email with a red *\n- Placeholder: name@company.com	AUTH-001	
Login	Email	Validation	Empty	High	Verify signing in with an empty Email	Not logged in, open the Customer Portal sign-in page	1. Leave Email empty\n2. Click Sign in	- The sign-in request is not sent\n- An error message shows under the Email field	AUTH-001	Text lỗi nguyên văn → Q-L-01
```

**7.2 · Mục 1, lệnh dựng file · tên chức năng tiếng Anh. Tìm**

```text
--function "AUTH-L0001_Đăng nhập"
```

**Thay bằng**

```text
--function "AUTH-L0001_Login"
```

**7.3 · Bỏ mục 2 (`_Data`) và mục 3 (`_Labels`), mục 4 đổi số thành 2. Tìm**

```text
## 2. Sheet `_Data`

| Khoá | Giá trị | Mô tả | Ghi chú |
|---|---|---|---|
| `{{user.cust_admin}}` | | Customer Admin của tenant A | Tạo được dữ liệu |
| `{{user.cust_viewer}}` | | Vai trò chỉ đọc | Dùng cho case phân quyền |
| `{{user.tenantB_admin}}` | | Admin của tenant B | Dùng cho case cách ly dữ liệu |
| `{{url.customer}}` | | Địa chỉ cổng khách hàng | |

## 3. Sheet `_Labels`

| Khoá | Nhãn nguyên văn | Màn hình | Nguồn |
|---|---|---|---|
| `{{btn.sign_in}}` | Sign in | Login | Thiết kế, trang 1 |
| `{{msg.required_email}}` | — chưa có — | Login | Chờ Q-L-01 |

Nhãn chưa có thì để `— chưa có —`, không tự đặt.

## 4. Mẫu câu hỏi
```

**Thay bằng**

```text
## 2. Mẫu câu hỏi
```

**7.4 · Mục 5 đổi số thành 3. Tìm**

```text
## 5. Mẫu báo cáo cuối việc
```

**Thay bằng**

```text
## 3. Mẫu báo cáo cuối việc
```

**7.5 · Mục 4 Bảng UC → sheet (chờ duyệt). Thêm vào cuối file**

```markdown
## 4. Bảng UC → sheet (ở Cover)

Mỗi UC của baseline đúng một dòng. Cột `Sheet` ghi một trong ba: tên sheet · `Chờ: <lý do>` · `Kiểm ở: <sheet>` (UC không có sheet riêng). Xem `rules/tc-authoring.md` mục G.

| UC | Tên UC | Sheet | Ghi chú |
|---|---|---|---|
| SCP-03 | Create scope | Scopes | |
| WSP-01 | Create workspace | Workspaces | Mở từ Scopes ("Link framework") chỉ kiểm mở đúng form, scope điền sẵn (rule 26) |
| AUD-01 | Record audit events | Kiểm ở: mọi sheet có hành động ghi vết | Nhóm Ghi vết |
| BLK-01 | Upload documents in bulk | Chờ: chưa có thiết kế Bulk | |
```

## 8. `.claude/skills/tc-authoring/references/format.md`

**8.1 · Mục 4, dòng căn lề ô dữ liệu (đề xuất, chờ duyệt). Tìm**

```text
- Ô dữ liệu: **căn trên theo chiều dọc**, bật xuống dòng tự động.
```

**Thay bằng**

```text
- Ô dữ liệu: **căn giữa theo chiều dọc** như file TC mẫu, bật xuống dòng tự động.
```

**8.2 · Mục 4, bảng màu · theo file TC mẫu (chờ duyệt). Tìm**

```text
| Hàng tiêu đề (nhóm cột và tên cột) | `17324D` | `FFFFFF`, đậm |
| Nhãn khối thông tin, tiêu đề bảng tổng kết | `EAE7E1` hoặc không nền | mặc định, đậm |
| Vùng dữ liệu | không nền | mặc định |
| Dòng còn câu hỏi mở (cột `Expected result` và `Open question`) | `FBE9E7` | `B8362B` |
| Đường kẻ ô | — | `C9C5BE`, nét mảnh |
```

**Thay bằng**

```text
| Hàng tiêu đề (nhóm cột và tên cột) | `00B0F0` | màu mặc định, đậm |
| Nhãn khối thông tin, tiêu đề bảng tổng kết | `00B0F0` | màu mặc định, đậm |
| Vùng dữ liệu, giá trị của khối thông tin | không nền | `363A45` |
| Dòng còn câu hỏi mở | `FBE9E7` ở cột `Expected result` và `Open question` | `363A45` ở `Expected result`, `B8362B` ở `Open question` |
| Đường kẻ ô | — | màu mặc định, nét mảnh |

Bảng màu lấy theo file TC mẫu (`profile.md`, dòng "File TC mẫu của dự án"); file mẫu SGS DTP và FEEC dùng cùng bảng này. File mẫu đổi màu thì sửa bảng này và `PALETTE` của hai script trước.
```

**8.3 · Mục 4, dòng phông chữ · bỏ `_Data`, `_Labels`. Tìm**

```text
kể cả `Cover`, `Hướng dẫn`, `_Data`, `_Labels`, `_Patterns`, `FLOW-nn`, `Test_Report`.
```

**Thay bằng**

```text
kể cả `Cover`, `Hướng dẫn`, `_Patterns`, `FLOW-nn`, `Test_Report`.
```

**8.4 · Mục 7 · thêm bảng từ tên nhóm kiểm. Tìm**

```text
Mọi giá trị không thuộc danh sách trên đều bị `tc_check.py` báo lỗi.
```

**Thay bằng**

```text
Mọi giá trị không thuộc danh sách trên đều bị `tc_check.py` báo lỗi.

**Tên nhóm kiểm** — bảng từ cố định, ghi theo ngôn ngữ của file TC (`rules/tc-authoring.md` rule 16). Mỗi ô một thứ tiếng: file tiếng Anh ghi `Login`, không ghi `Đăng nhập - Login`.

| Tiếng Việt | English |
|---|---|
| Hiển thị | Display |
| Nhập liệu | Input |
| Kiểm tra dữ liệu | Validation |
| Thành công | Success |
| Không thành công | Failure |
| Phân quyền | Permission |
| Bảo mật | Security |
| Điều hướng | Navigation |
| Trạng thái rỗng | Empty state |
| Ghi vết | Audit log |
| Tìm kiếm | Search |
| Lọc | Filter |
| Sắp xếp | Sort |
| Phân trang | Pagination |
```

## 9. `.claude/skills/tc-authoring/references/patterns.md`

**9.1 · P5 · phân quyền âm: giao diện và URL; API theo rule 29. Tìm**

```text
Bắt buộc thêm **case phân quyền âm**: vai trò không được phép thì nút phải ẩn **và** API phải chặn. Kiểm giao diện thôi là chưa đủ.
```

**Thay bằng**

```text
Bắt buộc thêm **case phân quyền âm**: vai trò không được phép thì nút phải ẩn **và** mở thẳng URL cũng bị chặn. API phải chặn thì kiểm ở sheet `API`, chỉ khi `profile.md` ghi tester được gọi API (`rules/tc-authoring.md` rule 29).
```

**9.2 · P12 · trạng thái rỗng tả đủ. Tìm**

```text
Bắt buộc: tiêu đề cột · checkbox ba trạng thái (rỗng, chọn một phần, chọn hết) · sắp xếp tăng và giảm · menu của dòng khác nhau theo loại dòng · bấm vào dòng · trạng thái rỗng.
```

**Thay bằng**

```text
Bắt buộc: tiêu đề cột · checkbox ba trạng thái (rỗng, chọn một phần, chọn hết) · sắp xếp tăng và giảm · menu của dòng khác nhau theo loại dòng · bấm vào dòng · trạng thái rỗng.

Trạng thái rỗng ghi đủ, mỗi phần một dòng: icon; tiêu đề nguyên văn; mô tả nguyên văn; nút kèm nhãn nút; các phần vẫn hiện trên màn như tiêu đề trang, ô tìm kiếm, hàng tiêu đề bảng. Ghi thẳng ra, không trỏ sang TC khác. TC trạng thái rỗng đứng trước TC tạo mới (`rules/tc-authoring.md` rule 4).
```

**9.3 · Mục "Bảy chỗ bộ TC thật hay thiếu", chỗ 3. Tìm**

```text
3. **Gọi thẳng API** — mọi case đều qua giao diện.
```

**Thay bằng**

```text
3. **Gọi thẳng API** — tester được gọi API (ghi ở `profile.md`) mà bộ TC chưa có sheet `API`.
```

## 10. `.claude/skills/tc-authoring/scripts/tc_check.py`

**10.1 · Docstring, dòng cách dùng. Tìm**

```text
    python tc_check.py TestCase.xlsx [--uc uc_list.txt] [--sheets Login,Scopes]
```

**Thay bằng**

```text
    python tc_check.py TestCase.xlsx [--uc uc_list.txt] [--sheets Login,Scopes] [--lang en]
```

**10.2 · Docstring · bỏ dòng kiểm khoá, thêm câu mơ hồ tiếng Anh, nhóm Success/Failure. Tìm**

```text
  - Kết quả mong đợi mơ hồ ("hoạt động bình thường", "hiển thị đúng", "thành công"…)
  - Khoá {{...}} không có trong sheet _Data hoặc _Labels
  - Khu vực (Classification II) có thao tác ghi dữ liệu mà thiếu nhóm Không thành công
```

**Thay bằng**

```text
  - Kết quả mong đợi mơ hồ ("hoạt động bình thường", "hiển thị đúng", "thành công", "works normally", "as expected"…)
  - Khu vực (Classification II) có nhóm Thành công / Success mà thiếu nhóm Không thành công / Failure
```

**10.3 · Docstring, dòng cảnh báo. Tìm**

```text
Cảnh báo: dòng còn ký tự ngoài bảng chữ Latin mà không khai ở cột Open question.
```

**Thay bằng**

```text
Cảnh báo: dòng còn ký tự ngoài bảng chữ Latin (không tính dấu câu như · — ←) mà không khai ở cột Open question;
  với --lang en: ô còn chữ tiếng Việt, trừ cột Open question và sheet Cần xác nhận.
```

**10.4 · Dòng import. Tìm**

```text
import argparse, re, sys

```

**Thay bằng**

```text
import argparse, re, sys, unicodedata

```

**10.5 · Danh sách từ mơ hồ, biểu thức ký tự, `SYS_SHEETS` · bỏ `KEY`, `_Data`, `_Labels`; thêm `Phân quyền`. Tìm**

```text
VAGUE = ["hoạt động bình thường", "hiển thị đúng", "thành công", "bình thường",
         "đúng như mong đợi", "ok", "chính xác"]
NON_LATIN = re.compile(r"[^\x00-\x7FÀ-ỹ\s]")
KEY = re.compile(r"\{\{[^}]+\}\}")
SYS_SHEETS = {"Cover", "Hướng dẫn", "_Data", "_Labels", "_Patterns", "_Nav",
              "_Effects", "Test_Report", "Đối chiếu nhãn", "Cần xác nhận"}
```

**Thay bằng**

```text
VAGUE = ["hoạt động bình thường", "hiển thị đúng", "thành công", "bình thường",
         "đúng như mong đợi", "ok", "chính xác",
         "works normally", "works correctly", "work correctly", "works as expected", "as expected",
         "displays correctly", "displayed correctly", "display correctly",
         "successfully", "success", "correctly", "properly", "normally"]
NON_LATIN = re.compile(r"[^\x00-\x7FÀ-ỹ\s·—–…‹›←→↑↓“”‘’•×]")   # dấu câu thường gặp không tính
VI_CHARS = re.compile(r"[ăâđêôơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]", re.I)
SYS_SHEETS = {"Cover", "Hướng dẫn", "_Patterns", "_Nav",
              "_Effects", "Test_Report", "Đối chiếu nhãn", "Cần xác nhận", "Phân quyền"}
Q_SHEET = "Cần xác nhận"   # sheet câu hỏi: viết theo ngôn ngữ câu hỏi, --lang en không kiểm
```

**10.6 · Bảng màu · theo file TC mẫu (chờ duyệt). Tìm**

```text
PALETTE_FILL = {"17324D", "EAE7E1", "FBE9E7"}          # references/format.md §4
PALETTE_FONT = {"FFFFFF", "B8362B", "000000"}
```

**Thay bằng**

```text
PALETTE_FILL = {"00B0F0", "FBE9E7"}                    # references/format.md §4, theo file TC mẫu
PALETTE_FONT = {"363A45", "B8362B", "000000"}
```

**10.7 · Bỏ cả hàm `collect_keys` và tham số `keys` của `check_sheet`. Tìm**

```text
def collect_keys(wb) -> set[str]:
    keys = set()
    for name in ("_Data", "_Labels"):
        if name in wb.sheetnames:
            for row in wb[name].iter_rows(values_only=True):
                for v in row:
                    if isinstance(v, str):
                        keys.update(KEY.findall(v))
    return keys


def check_sheet(ws, keys, errors, warns):
```

**Thay bằng**

```text
def check_sheet(ws, errors, warns):
```

**10.8 · Trong `check_sheet`, bỏ vòng kiểm khoá. Tìm**

```text
                    break
        for cell in (C_PRE, C_STEP, C_EXP):
            txt = ws.cell(r, cell).value
            if isinstance(txt, str):
                for k in KEY.findall(txt):
                    if keys and k not in keys:
                        errors.append(f"{where} · khoá {k} chưa khai trong _Data/_Labels")
        if not wait:
```

**Thay bằng**

```text
                    break
        if not wait:
```

**10.9 · Trong `check_sheet`, kiểm thêm nhóm Success / Failure. Tìm**

```text
        if "thành công" in joined and "không thành công" not in joined:
            errors.append(f"{ws.title} · khu vực '{area}' có nhóm Thành công nhưng thiếu Không thành công")
```

**Thay bằng**

```text
        if "thành công" in joined and "không thành công" not in joined:
            errors.append(f"{ws.title} · khu vực '{area}' có nhóm Thành công nhưng thiếu Không thành công")
        if re.search(r"\bsuccess", joined) and not re.search(r"\bfailure", joined):
            errors.append(f"{ws.title} · khu vực '{area}' có nhóm Success nhưng thiếu Failure")
```

**10.10 · Thêm hàm `check_lang_en` ngay trước `main`. Tìm**

```text
def main() -> int:
```

**Thay bằng**

```text
def check_lang_en(ws, warns):
    """--lang en: ô còn chữ tiếng Việt, trừ cột Open question của sheet TC và sheet câu hỏi."""
    if ws.title == Q_SHEET:
        return
    tc_sheet = ws.title not in SYS_SHEETS
    cells = []
    for row in ws.iter_rows():
        for c in row:
            if not isinstance(c.value, str) or (tc_sheet and c.column == C_WAIT):
                continue
            if VI_CHARS.search(unicodedata.normalize("NFC", c.value)):
                cells.append(c.coordinate)
    if cells:
        more = f" … (+{len(cells) - 5})" if len(cells) > 5 else ""
        warns.append(f"{ws.title} · {len(cells)} ô còn chữ tiếng Việt: {', '.join(cells[:5])}{more}")


def main() -> int:
```

**10.11 · Trong `main`, thêm tuỳ chọn `--lang`. Tìm**

```text
    ap.add_argument("--sheets", help="chỉ kiểm các sheet này, phân tách bằng dấu phẩy")
```

**Thay bằng**

```text
    ap.add_argument("--sheets", help="chỉ kiểm các sheet này, phân tách bằng dấu phẩy")
    ap.add_argument("--lang", choices=["en"], help="en: file TC viết tiếng Anh, cảnh báo ô còn chữ tiếng Việt")
```

**10.12 · Trong `main`, bỏ dòng gọi `collect_keys`. Tìm**

```text
    wb = openpyxl.load_workbook(Path(a.xlsx), data_only=True)
    keys = collect_keys(wb)
```

**Thay bằng**

```text
    wb = openpyxl.load_workbook(Path(a.xlsx), data_only=True)
```

**10.13 · Trong `main`, gọi `check_lang_en`. Tìm**

```text
        if not only or ws.title in only:
            check_format(ws, errors)
```

**Thay bằng**

```text
        if not only or ws.title in only:
            check_format(ws, errors)
            if a.lang == "en":
                check_lang_en(ws, warns)
```

**10.14 · Trong `main`, bỏ đối số `keys` khi gọi `check_sheet`. Tìm**

```text
        ucs |= check_sheet(ws, keys, errors, warns)
```

**Thay bằng**

```text
        ucs |= check_sheet(ws, errors, warns)
```

## 11. `.claude/skills/tc-authoring/scripts/tc_build_xlsx.py`

**11.1 · Bảng màu · theo file TC mẫu (chờ duyệt). Tìm**

```text
# Bảng màu duy nhất — khớp references/format.md §4 và PALETTE trong tc_check.py
ink   = Font(name=FONT, size=SIZE)
bold  = Font(name=FONT, size=SIZE, bold=True)
white = Font(name=FONT, size=SIZE, bold=True, color="FFFFFF")
red   = Font(name=FONT, size=SIZE, color="B8362B")
head  = PatternFill("solid", fgColor="17324D")
subtle= PatternFill("solid", fgColor="EAE7E1")
pink  = PatternFill("solid", fgColor="FBE9E7")
thin  = Side(style="thin", color="C9C5BE")
```

**Thay bằng**

```text
# Bảng màu duy nhất — theo file TC mẫu, khớp references/format.md §4 và PALETTE trong tc_check.py
ink   = Font(name=FONT, size=SIZE, color="363A45")
bold  = Font(name=FONT, size=SIZE, bold=True)
white = Font(name=FONT, size=SIZE, bold=True)    # chữ hàng tiêu đề: đậm, màu mặc định như file mẫu
red   = Font(name=FONT, size=SIZE, color="B8362B")
head  = PatternFill("solid", fgColor="00B0F0")
subtle= PatternFill("solid", fgColor="00B0F0")
pink  = PatternFill("solid", fgColor="FBE9E7")
thin  = Side(style="thin")                       # màu mặc định như file mẫu
```

**11.2 · Căn lề ô dữ liệu · căn giữa theo chiều dọc như file mẫu (đề xuất, chờ duyệt). Tìm**

```text
TOP   = Alignment(horizontal="left", vertical="top", wrap_text=True)
```

**Thay bằng**

```text
TOP   = Alignment(horizontal="left", vertical="center", wrap_text=True)   # căn giữa theo chiều dọc như file mẫu
```

## 12. `.claude/skills/test-design/SKILL.md`

**12.1 · Tiêu đề. Tìm**

```text
# Tester — Thiết kế test (v0.1)
```

**Thay bằng**

```text
# Tester — Thiết kế test (v0.2)
```

**12.2 · Dòng changelog. Tìm**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
```

**Thay bằng**

```text
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.2 | 2026-10-05 | `references/coverage-checklist.md`, `techniques.md`, `tc-framework.md`: phân quyền âm kiểm trên giao diện và URL; kiểm API chỉ khi `profile.md` ghi tester được gọi API, viết ở sheet `API` riêng (14 chỗ). Hanna duyệt 05/10. | FB-???[api] |
```

## 13. `.claude/skills/test-design/references/coverage-checklist.md`

**13.1 · Dòng PM "Không" · UI và URL; API khi được gọi. Tìm**

```text
- [ ] Mỗi dòng PM "Không" cho hành động ghi có TC kiểm **cả** UI và API.
```

**Thay bằng**

```text
- [ ] Mỗi dòng PM "Không" cho hành động ghi có TC kiểm giao diện: nút ẩn hoặc tắt, mở thẳng URL bị chặn. Kiểm API khi `profile.md` ghi tester được gọi API, viết ở sheet `API` riêng.
```

**13.2 · Bảng lỗi hay lọt, dòng 1. Tìm**

```text
| 1 | Validation chỉ có ở UI, API nhận dữ liệu sai | TC gửi request thẳng tới API |
```

**Thay bằng**

```text
| 1 | Validation chỉ có ở UI, API nhận dữ liệu sai | TC gửi request thẳng tới API, ở sheet `API`, khi tester được gọi API |
```

**13.3 · Bảng lỗi hay lọt, dòng 2. Tìm**

```text
| 2 | Ẩn nút nhưng URL/API vẫn cho làm | TC Negative phân quyền qua URL và API |
```

**Thay bằng**

```text
| 2 | Ẩn nút nhưng URL/API vẫn cho làm | TC Negative phân quyền qua URL; qua API khi tester được gọi API (sheet `API`) |
```

## 14. `.claude/skills/test-design/references/techniques.md`

**14.1 · Giá trị biên, "Lỗi hay gặp". Tìm**

```text
thử biên trên UI nhưng quên API;
```

**Thay bằng**

```text
thử biên trên UI nhưng quên API (khi tester được gọi API);
```

**14.2 · Chuyển trạng thái, ô không hợp lệ. Tìm**

```text
   - mỗi ô không hợp lệ có rủi ro (hủy khi đã đóng, duyệt khi chưa gửi) một TC — kiểm cả nút không hiện và API bị từ chối;
```

**Thay bằng**

```text
   - mỗi ô không hợp lệ có rủi ro (hủy khi đã đóng, duyệt khi chưa gửi) một TC — kiểm nút không hiện; API bị từ chối thì kiểm ở sheet `API` khi tester được gọi API;
```

**14.3 · Ma trận phân quyền, bước 3. Tìm**

```text
3. TC cho mỗi ô: "Có" → làm được; "Không" → UI ẩn hoặc tắt **và** API từ chối, không lộ dữ liệu trong response.
```

**Thay bằng**

```text
3. TC cho mỗi ô: "Có" → làm được; "Không" → UI ẩn hoặc tắt, mở thẳng URL bị chặn; khi tester được gọi API thì thêm TC API từ chối, không lộ dữ liệu trong response (sheet `API`).
```

**14.4 · Ma trận phân quyền, "Tiêu chí phủ". Tìm**

```text
**Tiêu chí phủ:** mọi dòng PM; dòng "Không" của hành động ghi dữ liệu kiểm cả UI và API.
```

**Thay bằng**

```text
**Tiêu chí phủ:** mọi dòng PM; dòng "Không" của hành động ghi dữ liệu kiểm giao diện và URL; kiểm API khi tester được gọi API.
```

**14.5 · Ma trận phân quyền, "Lỗi hay gặp". Tìm**

```text
quên response của API danh sách có lộ bản ghi ngoài quyền không.
```

**Thay bằng**

```text
khi tester được gọi API, quên response của API danh sách có lộ bản ghi ngoài quyền không.
```

**14.6 · Bảng tiêu chí phủ, dòng Phân quyền PM. Tìm**

```text
| Phân quyền PM | mỗi dòng ≥ 1 TC; dòng "Không" của hành động ghi: UI + API |
```

**Thay bằng**

```text
| Phân quyền PM | mỗi dòng ≥ 1 TC; dòng "Không" của hành động ghi: UI + URL, thêm API khi tester được gọi API |
```

## 15. `.claude/skills/test-design/references/tc-framework.md`

**15.1 · Bảng loại TC, ví dụ Negative. Tìm**

```text
Nhập email sai định dạng; Member gọi API tạo người dùng |
```

**Thay bằng**

```text
Nhập email sai định dạng; Member mở thẳng URL trang tạo người dùng |
```

**15.2 · Checklist "Phía server". Tìm**

```text
- [ ] **Phía server:** gửi request thẳng tới API bỏ qua kiểm tra trên UI → server vẫn từ chối. Validation chỉ có ở UI là bug bảo mật.
```

**Thay bằng**

```text
- [ ] **Phía server** (khi tester được gọi API, viết ở sheet `API`): gửi request thẳng tới API bỏ qua kiểm tra trên UI → server vẫn từ chối. Validation chỉ có ở UI là bug bảo mật.
```

**15.3 · Bảng theo loại trường, dòng Dropdown. Tìm**

```text
gửi giá trị ngoài danh sách qua API |
```

**Thay bằng**

```text
gửi giá trị ngoài danh sách qua API (sheet `API`, khi tester được gọi API) |
```

**15.4 · Checklist chuyển trạng thái. Tìm**

```text
- [ ] Chuyển không hợp lệ quan trọng: nút không hiện, và gọi API thẳng bị từ chối.
```

**Thay bằng**

```text
- [ ] Chuyển không hợp lệ quan trọng: nút không hiện; gọi API thẳng bị từ chối thì kiểm ở sheet `API` khi tester được gọi API.
```

**15.5 · Đoạn ma trận phân quyền. Tìm**

```text
cần một TC Negative kiểm **cả UI** (nút ẩn hoặc tắt) **và API** (gọi thẳng bị từ chối).
```

**Thay bằng**

```text
cần một TC Negative kiểm giao diện (nút ẩn hoặc tắt, mở thẳng URL bị chặn); khi tester được gọi API thì thêm TC gọi thẳng API bị từ chối, ở sheet `API`.
```

## 16. `projects/_template/profile.md`

**16.1 · Thêm hai dòng: ngôn ngữ viết file TC, tester được gọi API. Tìm**

```text
- Ngôn ngữ giao diện của hệ thống (TC viết theo nhãn ngôn ngữ này):
```

**Thay bằng**

```text
- Ngôn ngữ giao diện của hệ thống (TC viết theo nhãn ngôn ngữ này):
- Ngôn ngữ viết file TC:              (vd: tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt · rules/tc-authoring.md rule 16)
- Tester được gọi API:                (Có / Không; có thì ghi công cụ, vd Swagger, Postman · rules/tc-authoring.md rule 29)
```

## 17. `projects/sgs-dtp/profile.md`

**17.1 · Hồ sơ dự án SGS DTP; máy đã có file này thì thêm tay các dòng còn thiếu. Tạo file mới**

```markdown
# Hồ sơ dự án: sgs-dtp
- Khách hàng / sản phẩm: SGS DTP
- Ngôn ngữ giao diện của hệ thống (TC viết theo nhãn ngôn ngữ này): tiếng Anh (Figma "SGS DTP DS")
- Ngôn ngữ viết file TC: tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt
- Tester được gọi API: Không
- Dạng ID UC của tài liệu gốc: `<MODULE>-nn`, vd `SCP-01` (UC List v4); khác `UC-<MODULE>-<số>` nên phải sửa `ID_RE` trong extract_uc_list.py nếu chạy script đó
- File TC mẫu của dự án: `SGS-DTP_TestCase1.xlsx` (đường dẫn trên máy: Hanna điền)
- Môi trường test / URL: chưa có
- Nguồn thiết kế: Figma "SGS DTP DS" (figma.com/design/KM5Oc1DaB78FXOMimDyB0U/SGS-DTP-DS); tài liệu yêu cầu: SGS DTP Use Case List v4 (02/10/2026)
## Quyết định đã chốt của dự án
- 2026-10-05 · Hanna · File TC viết tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt; dòng đăng nhập ở Pre-condition ghi `Logged in as <role>`, màn không cần đăng nhập ghi `Not logged in` (FB-???[tieng-anh], FB-???[pre-condition])
- 2026-10-05 · Hanna · Tester không được gọi API: không viết TC gọi API ở sheet màn hình; khi được gọi API thì viết ở sheet `API` riêng (FB-???[api])
- 2026-10-05 · Hanna · Giá trị tính toán (vd cột Users, Evidence coverage) không ghi cách tính trong TC; Expected theo Figma và UC, chưa có thì để trống và ghi câu hỏi (FB-???[gia-tri-tinh], Bị bác)
```

## 18. `projects/sgs-dtp/tests/design/bo-cuc-sheet_uc-v4.md`

**18.1 · Bố cục sheet theo UC List v4, tuỳ chọn (chờ duyệt). Tạo file mới**

```markdown
# Bố cục sheet — SGS DTP · UC List v4

v0.1 · 2026-10-05 · Áp `rules/tc-authoring.md` mục G (chờ duyệt) cho `SGS DTP Use Case List v4.xlsx` (bản 02/10/2026), sheet P1 Use Cases; số R là số hàng trong sheet đó. Đếm bằng script: 105 UC → 16 sheet viết được ngay (75 UC), 26 UC chờ, 4 UC kiểm ở nơi hiện ra; mỗi UC nằm đúng một chỗ.

## Bảng UC → sheet

| Sheet | UC | Ghi chú |
|---|---|---|
| Login | AUTH-01, AUTH-03 | Đã có; bổ sung màn kích hoạt tài khoản |
| Top bar | AUTH-02, NTF-02, PRF-01 | Chuông thông báo ở top bar (R114). Đăng xuất, đổi ngôn ngữ ở đây là [GIẢ ĐỊNH], xem lại Figma |
| Home | CKP-01..04 | Classification I là vai trò: mỗi vai trò một dashboard |
| Customer Accounts | ACC-01..06 | Phía SGS |
| Users | USR-01..05, ROL-02 | Cả hai portal |
| Frameworks | FWK-01..07 | |
| Scopes | SCP-01..04 | Đã có |
| Workspaces | WSP-01..05 | Form tạo workspace test đầy đủ ở đây; mở từ Scopes ("Link framework") chỉ kiểm mở form, scope điền sẵn (R35) |
| Assisted workspace | EVA-01..07, WSP-06 | Bên trong một Assisted workspace (R37, R42–R48); WSP-06 hiện ở cây requirement (R40, R43) |
| Evidence Library | EVC-01..08 | Thư viện across workspaces (R50); EVC-08 consultant chỉ xem, ở nhóm Phân quyền |
| Service Requests | SRQ-01..03, SRQ-06, SRQ-07 | Đổi consultant khi đang xử lý: chờ Q12 |
| Certifications | CRT-01..03 | Màn SGS và màn Customer chung một sheet |
| Marketplace | MKT-01..06 | |
| Training | TRN-01..03 | TRN-03 có cho gửi yêu cầu đào tạo không: chờ Q10 |
| Audit Log | AUD-02, AUD-03 | Màn SGS và màn Customer chung một sheet |
| Retention | RET-01..03 | Phải lùi ngày, chạy job; ngày xoá hiện ở hộp Archive thì test ở Workspaces (R38) |
| Chờ: chưa có thiết kế Bulk, NirmatAI | BLK-01..10, CFG-01..05, INT-01..06 | Changes vs Source: D4, D9. CFG-01..03 là tab Bulk settings của chi tiết framework (R23); có thiết kế thì vào sheet Frameworks |
| Chờ: chưa chốt có làm | SOA-01..02, RET-04..05, CKP-05 | Q5, Q6, Q9 |
| Kiểm ở: nơi hiện ra | NTF-01, NTF-03, AUD-01, ROL-01 | NTF-01 ở Service Requests và FLOW-03; NTF-03 ở Users, Customer Accounts, Login; AUD-01 ở nhóm Ghi vết mọi sheet; ROL-01 ở nhóm Phân quyền, Bảo mật mọi sheet |

Sheet thêm: `Phân quyền` (ma trận vai trò × UC, tuỳ chọn) và 4 sheet luồng:

- FLOW-01 Onboarding: ACC-03 → ACC-05 → AUTH-03 → SCP-03 → USR-03/05 → AUTH-03 → SCP-01
- FLOW-02 Certification: SCP-03 → CRT-01 → CRT-02, SCP-02
- FLOW-03 Service request: SRQ-01 → SRQ-06 → SRQ-07, kèm NTF-02
- FLOW-04 Consultant: ACC-06 → EVC-08 → AUD-03

## Vì sao tách 07 (Evidence – Assisted mode) và 08 (Evidence – Common)

- EVA diễn ra bên trong một Assisted workspace: cây requirement, chi tiết requirement, upload, map, gỡ evidence, gán owner (R42–R48); phần thân overview của Assisted workspace chính là cây requirement (R37).
- EVC là thư viện evidence "across workspaces, with filters by workspace, standard and scope" (R50) cùng các thao tác trên một evidence (R51–R55); Bulk cũng dùng evidence (BLK-08 · R69).
- Hai màn khác nhau nên tách. Chỗ nối đặt ở sheet của hành động (rule 27): upload ở requirement rồi kiểm trong thư viện → sheet Assisted workspace; xoá evidence trong thư viện rồi kiểm requirement đang map nó → sheet Evidence Library.

## Việc cần làm trên SGS-DTP_TestCase1.xlsx

- Đổi cột UC sang ID v4 qua cột Source ref: 175/181 TC đang ghi ID nguồn v2.1; một số số đã khác, vd UC-USR-006 → USR-05, UC-AUTH-005 → AUTH-03.
- Chuyển 13 TC trong Scopes sang sheet Workspaces: UC-SCP-006 → WSP-01 (11 TC "Gắn framework"), UC-EVD-003 → WSP-02 (1), UC-SCP-007 → WSP-04/05 (1 TC "Gỡ framework"). Scopes chỉ giữ TC bấm "Link framework" mở panel Create workspace với scope điền sẵn.
- 6 TC trỏ UC không còn ở P1: UC-RDN-004 (4, Scopes) và UC-AUTH-003 (1, Login) đã sang P2 (P2 Deferred!H40, H3); UC-ACC-009 (1, Login) không có trong v4.
- Viết lại cả file bằng tiếng Anh (rule 16, `profile.md`), trừ cột Open question và sheet Cần xác nhận; bỏ dạng `{{…}}`, dòng đăng nhập ghi `Logged in as <role>`, dữ liệu ghi giá trị cụ thể (rule 14; số lượng ở FB-???[pre-condition]).
- 18 TC chưa ghi vai trò ở Pre-condition (rule 24): Login TC_038, 039, 041, 050; Scopes TC_022, 023, 024, 026, 027, 049, 051, 052, 069, 070, 071, 090, 091, 092.
- Bỏ TC gọi API khỏi sheet màn hình (rule 29): 9 TC chỉ gọi API (Login TC_051; Scopes TC_119, 120, 126, 127; Users TC_054, 058, 059, 060), TVP_ID không dùng lại (rule 11); 3 TC bỏ bước gọi API, giữ phần giao diện (Scopes TC_123; Users TC_055, 056).
- Ô Scopes!C5 (Creator) đổi sang Times New Roman 10 (FB-016).

## Câu hỏi còn mở

- QUAN TRỌNG · SGS Admin có mở được chi tiết scope (SCP-02) không? ACC-02 (R8) cho SGS xem danh sách scope trong chi tiết khách hàng, còn SCP-01/02 chỉ ghi "assigned SGS users (read-only)" (R30–R31). Mặc định: theo cột Actor(s), SGS Admin không mở được.
- QUAN TRỌNG · Customer Viewer có mở được Scopes, Workspaces không? Viewer chỉ có ở CRT-02, AUD-03, CKP-05. Mặc định: theo cột Actor(s), không mở được.
- NHỎ · 6 TC "Đổi tier" đang ghi [NGOÀI UC]: v4 không có UC đổi tier, tier chỉ chọn lúc tạo workspace (R35). Nếu Figma vẫn có nút đổi tier thì đây là chỗ Figma lệch với UC.
```

## 19. `docs/README-ai-ecosystem-v0.3.md`

**19.1 · Dòng cập nhật, đặt trên dòng "Mới ở v0.3". Tìm**

```text
**Mới ở v0.3:**
```

**Thay bằng**

```text
**Cập nhật 2026-10-05:** `rules/tc-authoring.md` và skill `tc-authoring` lên v0.3, `rules/common.md` v0.4, `rules/tester.md` v0.3, skill `test-design` v0.2. TC viết cho Tester: vai trò, dữ liệu, nhãn ghi bằng chữ ngay trong ô (`Logged in as <role>`), bỏ sheet `_Data`, `_Labels`; ngôn ngữ file TC theo `profile.md` của dự án; trạng thái rỗng đặt trước, không trỏ sang TC khác, mỗi mục một dòng; TC gọi API chỉ viết khi tester được gọi API, ở sheet `API` riêng; bảng màu theo file TC mẫu; thêm mục G Chia sheet. Phần còn chờ duyệt ghi trong changelog của từng file. Nguồn: các FB ngày 05/10.

**Mới ở v0.3:**
```

**19.2 · Mục Cấu trúc, dòng `tc-authoring.md`. Tìm**

```text
tc-authoring.md                nạp khi viết hoặc sửa file test case — tổ chức, nội dung, định dạng
```

**Thay bằng**

```text
tc-authoring.md                nạp khi viết hoặc sửa file test case — tổ chức, chia sheet, nội dung, định dạng
```

**19.3 · Mục Cấu trúc, dòng `references/format.md` của `tc-authoring/`. Tìm**

```text
references/format.md         cột, phông chữ, căn lề, quy tắc gộp ô
```

**Thay bằng**

```text
references/format.md         cột, phông chữ, căn lề, quy tắc gộp ô, bảng màu, tên nhóm kiểm
```

**19.4 · Mục Cấu trúc, dòng `references/templates.md` của `tc-authoring/`. Tìm**

```text
references/templates.md      mẫu TSV phẳng, mẫu câu hỏi
```

**Thay bằng**

```text
references/templates.md      mẫu TSV phẳng, mẫu câu hỏi, bảng UC → sheet
```

## 20. `README.md`

**20.1 · Mục Thành phần, sau dòng đầu tiên. Tìm**

```text
Mô tả đầy đủ: `docs/README-ai-ecosystem-v0.3.md`.
```

**Thay bằng**

```text
Mô tả đầy đủ: `docs/README-ai-ecosystem-v0.3.md`.
- Cập nhật 05/10/2026: `tc-authoring` v0.3, `common.md` v0.4, `tester.md` v0.3, `test-design` v0.2 — viết TC bằng chữ cho Tester, ngôn ngữ file TC theo `profile.md`, TC gọi API ở sheet riêng, chia sheet theo màn hình, bảng màu theo file mẫu. Tóm tắt ở dòng "Cập nhật 2026-10-05" đầu `docs/README-ai-ecosystem-v0.3.md`.
```

## Kiểm sau khi áp

- Chạy lại `python ap_dung_cap_nhat.py`: mọi chỗ báo `đã áp`.
- `rules/tc-authoring.md`: rule đánh số liền 1 → 29; dòng Phiên bản và dòng changelog đầu bảng cùng ghi v0.3. `rules/common.md` v0.4, `rules/tester.md` v0.3, skill `tc-authoring` v0.3, skill `test-design` v0.2.
- Tìm `{{` trong `rules/tc-authoring.md` và thư mục `.claude/skills/tc-authoring/`: không còn kết quả nào. Tìm `_Data`, `_Labels`: chỉ còn ở dòng changelog v0.3.
- `python .claude/skills/tc-authoring/scripts/tc_check.py <file TC>.xlsx --lang en` chạy được; lỗi màu giả không còn.
- Sau khi đánh số: `fb_report.py` báo 0 lỗi; không còn chuỗi `FB-???[` trong thư mục.
