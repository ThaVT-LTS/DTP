# Sổ ghi nhớ góp ý

Quy tắc: `rules/feedback.md` · Quy trình: skill `feedback-loop` · Kiểm tra sổ: `python skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .`

Bản ghi `FB-001` là góp ý của người dùng. `FB-002` trở đi là **đề xuất của AI** từ lần rà file `FEEC_PM_IT_Test_Case.xlsx` (429 TC, 3 sheet) — theo `common.md` rule 8, tất cả đang **chờ duyệt**, chưa được dùng như rule.

| FB | Tiêu đề | Loại | Trạng thái | Tái phát |
|---|---|---|---|---|
| FB-001 | Mỗi nhận xét phải thành một bản ghi nhớ và cải thiện dần | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-002 | TC không ghi Pre-condition | L2-rule | Mới | 0 |
| FB-003 | TVP_ID chỉ duy nhất trong một sheet | L4-mẫu | Mới | 0 |
| FB-004 | TC không trỏ tới ID yêu cầu nào | L2-rule | Mới | 0 |
| FB-005 | Bug_ID và Remark không có định dạng | L4-mẫu | Mới | 0 |
| FB-006 | Không có tiêu chí gán Priority | L2-rule | Mới | 0 |
| FB-007 | Nhóm phân loại khai báo nhưng không có TC | L5-script | Mới | 0 |
| FB-008 | Không có quy tắc cho Pending / Blocked / NA và điều kiện kết thúc vòng | L2-rule | Mới | 0 |
| FB-009 | Câu hỏi mở nằm rời ở sheet Tổng hợp | L4-mẫu | Mới | 0 |
| FB-010 | Mỗi màn một sheet, chia khu vực, viết theo thứ tự mắt đọc | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-011 | Học cấu trúc cha–con và gộp ô của bộ TC mẫu | L4-mẫu | Đã vào rule (chờ duyệt) | 0 |
| FB-012 | Hệ thống chỉ là bản hiển thị, chưa chạy thật | L6-tri thức | Đã vào rule (chờ duyệt) | 0 |
| FB-013 | Định dạng file: Times New Roman 10, căn trái, gộp ô như mẫu | L4-mẫu | Đã vào rule (chờ duyệt) | 1 |
| FB-014 | Mỗi khi nhận tài liệu phải nêu đánh giá mục đích sản phẩm | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-015 | Đổi tên cột Chờ text cho chuyên nghiệp hơn | L4-mẫu | Đã vào rule (chờ duyệt) | 0 |
| FB-016 | Toàn bộ phải đồng nhất màu sắc, font chữ | L2-rule | Đã vào rule (chờ duyệt) | 1 |
| FB-017 | Đọc sai phạm vi UC: UC không có giờ, đang lùi Phase 2 bị coi như đã chốt | L2-rule | Đã sửa sản phẩm | 0 |
| FB-018 | Khảo sát prototype chỉ trong màn đang viết | L2-rule | Mới | 0 |
| FB-019 | File TC phải đúng form file mẫu của dự án — lệch với bảng màu của rule 22 | L4-mẫu | Đã vào rule (chờ duyệt) | 0 |
| FB-020 | Dự án Playwright thử nghiệm phải tách riêng và rút thành rule | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-021 | Bộ TC FEEC Document v3 đã lỗi thời, đi từ TC để cập nhật BA | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-022 | Dịch tạm thông báo tiếng Nhật sang tiếng Việt, không hỏi từng câu | L2-rule | Chưa rõ phạm vi | 0 |
| FB-023 | tc_check.py bỏ sót kết quả mơ hồ khi chữ ở dạng tổ hợp | L5-script | Mới | 0 |
| FB-024 | tc_build_xlsx.py đánh lại TVP_ID khi chèn hoặc xếp lại dòng | L5-script | Mới | 0 |
| FB-025 | Làm gọn: chỉ nghiệp vụ, câu hỏi, SRS / US / UC, không chạy cả bộ rule | L2-rule | Chưa rõ phạm vi | 0 |
| FB-026 | Thay TC bằng file phân tích case cha con, dễ nhìn, dễ hiểu | L4-mẫu | Đã sửa sản phẩm | 0 |
| FB-027 | Bàn giao bằng một zip giữ cấu trúc thư mục, kèm danh sách file và fb-moi.md | L4-mẫu | Đã sửa sản phẩm | 0 |
| FB-028 | Học cách kiểm của người dùng: case ngoài nghiệp vụ (trên 100 mục, tên dài, điều hướng nhiều cấp) để tránh lọt bug | L6-tri thức | Đã vào rule (chờ duyệt) | 0 |

---

## FB-001 · Mỗi nhận xét phải thành một bản ghi nhớ và cải thiện dần
- Ngày: 2026-09-29
- Nguồn: chat 29/09 · "tôi cần b xây dựng bản rule để mỗi nhận xét của tôi là 1 bản ghi nhớ và update, cải thiện hơn"
- Loại: L2-rule
- Địa chỉ: rules/feedback.md · skills/feedback-loop/ · feedback/log.md
- Tiêu chí kiểm: mọi nhận xét trong phiên đều có một bản ghi FB tương ứng, và mỗi thay đổi rule/skill đều có một dòng changelog trỏ tới FB-nnn
- Phạm vi ảnh hưởng: toàn bộ bộ quy tắc — `common.md` rule 8 trước đây chỉ nói "góp ý → cập nhật rule", không nói ghi ở đâu, ai duyệt, kiểm thế nào
- Đã sửa: thêm `rules/feedback.md` v0.1; thêm skill `feedback-loop` v0.1 (7 bước + 2 reference + script); `rules/common.md` v0.1→v0.2 rule 8 trỏ sang rule mới; tạo sổ này
- Cách kiểm: `python skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo .` → mã thoát 0
- Gate: mức 3 · fb_report.py (thiếu trường, trạng thái sai, FB không được changelog trích dẫn, tái phát chưa nâng gate)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-002 · TC không ghi Pre-condition
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L2-rule
- Địa chỉ: rules/tester.md#7 · skills/test-design/references/templates.md
- Tiêu chí kiểm: TC có bước phụ thuộc vai trò đăng nhập, dữ liệu master hoặc trạng thái đối tượng mà cột Pre-condition rỗng
- Phạm vi ảnh hưởng: 422/429 TC rỗng cột Pre-condition (PM-L0001 247/254, PM-L0002 25/25, DM-L0001 150/150)
- Trạng thái: Mới
- Tái phát: 0

## FB-003 · TVP_ID chỉ duy nhất trong một sheet
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L4-mẫu
- Địa chỉ: skills/test-design/references/templates.md · skills/test-design/scripts/rtm_check.py
- Tiêu chí kiểm: hai TC khác nhau trong dự án không được mang cùng một TVP_ID
- Phạm vi ảnh hưởng: 150 ID trùng giữa các sheet (TC_001–TC_150 lặp ở PM-L0001, PM-L0002, DM-L0001). Hệ quả: Bug_ID, báo cáo và script tự động không tham chiếu được một TC bằng ID của nó. Đề xuất `PM-L0001_TC_001`
- Trạng thái: Mới
- Tái phát: 0

## FB-004 · TC không trỏ tới ID yêu cầu nào
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L2-rule
- Địa chỉ: rules/tester.md#2 · skills/test-design/references/templates.md
- Tiêu chí kiểm: mỗi TC có ít nhất một ID test basis / spec trong cột Nguồn
- Phạm vi ảnh hưởng: 429/429 TC. File không có cột nào trỏ tới spec; Classification I–IV là vùng giao diện, không phải ID yêu cầu. Hệ quả: không đo được độ phủ, không biết yêu cầu nào chưa có TC, và khi spec đổi thì không tìm được TC cần sửa
- Trạng thái: Mới
- Tái phát: 0

## FB-005 · Bug_ID và Remark không có định dạng
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L4-mẫu
- Địa chỉ: skills/test-design/references/templates.md
- Tiêu chí kiểm: Bug_ID khớp một mẫu cố định; nhiều bug trong một ô thì phân tách bằng ký tự quy ước; Remark trỏ được tới nơi lưu issue
- Phạm vi ảnh hưởng: Bug_ID lưu dạng số thực (`6.0`, `14.0`, `20.0`) và dạng danh sách trong một ô (`11, 34 `); Remark tự do (`Update - Issue 04`, `Update-Notion 4`) không cho biết issue nằm ở hệ thống nào. 24 mã bug trên 3 sheet
- Trạng thái: Mới
- Tái phát: 0

## FB-006 · Không có tiêu chí gán Priority
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L2-rule
- Địa chỉ: rules/tester.md · skills/test-design/SKILL.md#bước-3
- Tiêu chí kiểm: mỗi mức Priority có định nghĩa; tỷ lệ TC theo mức giải thích được
- Phạm vi ảnh hưởng: PM-L0001 Medium 189/254 (74%), DM-L0001 High 90/150 (60%), 1 TC không có Priority. Hai sheet cùng dự án lệch nhau nhiều như vậy cho thấy mức được gán theo cảm nhận. Hệ quả: không chọn được bộ smoke và bộ regression
- Trạng thái: Mới
- Tái phát: 0

## FB-007 · Nhóm phân loại khai báo nhưng không có TC
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L5-script
- Địa chỉ: skills/test-design/scripts/rtm_check.py · sheet Test_Report
- Tiêu chí kiểm: mỗi nhóm Classification xuất hiện trong báo cáo phải có ≥ 1 TC, hoặc có lý do loại trừ ghi rõ
- Phạm vi ảnh hưởng: `詳細検索 - Advanced Search / 検索` có 0 TC và làm sheet Test_Report hiện `#DIV/0!`. Lỗi này script bắt được, người đọc báo cáo thì dễ bỏ qua
- Trạng thái: Mới
- Tái phát: 0

## FB-008 · Không có quy tắc cho Pending / Blocked / NA và điều kiện kết thúc vòng
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L2-rule
- Địa chỉ: rules/tester.md (thêm rule về thực thi) · skill `test-execution` (chưa có)
- Tiêu chí kiểm: mỗi TC không Passed/Failed phải có lý do; vòng test chỉ được đóng khi không còn Pending
- Phạm vi ảnh hưởng: Round 1 PM-L0001 có 41 Pending + 22 NA trên 254; DM-L0001 có 73 Pending + 32 Failed trên 150. Round 2 đánh 191/254 TC là NA mà không thấy lý do trong file — không rõ là "không áp dụng nữa" hay "không chạy lại"
- Trạng thái: Mới
- Tái phát: 0

## FB-009 · Câu hỏi mở nằm rời ở sheet Tổng hợp
- Ngày: 2026-09-29
- Nguồn: AI đề xuất từ rà `FEEC_PM_IT_Test_Case.xlsx` — chờ duyệt
- Loại: L4-mẫu
- Địa chỉ: skills/test-design/references/templates.md#Q-T · sheet Tổng hợp
- Tiêu chí kiểm: mỗi câu hỏi có ID `Q-T-nn`, mức CHẶN/QUAN TRỌNG/NHỎ, người nhận, trạng thái, TC bị chặn
- Phạm vi ảnh hưởng: 9 câu hỏi (giới hạn ký tự các textbox, số dòng tối đa) chỉ có nội dung + link `prnt.sc`, không ID, không trạng thái, không nối với TC nào. Link `prnt.sc` là ảnh ngoài, sẽ mất theo thời gian
- Trạng thái: Mới
- Tái phát: 0


## FB-010 · Mỗi màn một sheet, chia khu vực, viết theo thứ tự mắt đọc
- Ngày: 2026-09-30
- Nguồn: chat 30/09 · "Khi viết thì từng màn hình trong 1 sheet riêng, nội dung của từng màn hình bên trong sẽ viết theo logic từ trên xuống dưới, từ trái qua phải" · "Chia thành các khu vực pattern"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#B · skills/tc-authoring/SKILL.md#bước-2 · references/patterns.md
- Tiêu chí kiểm: mỗi sheet là một màn; mọi TC thuộc một khu vực; thứ tự khu vực khớp thứ tự mắt đọc
- Phạm vi ảnh hưởng: toàn bộ cách tổ chức file test case
- Đã sửa: thêm `rules/tc-authoring.md` v0.1 và skill `tc-authoring` v0.1 với thư viện 12 pattern
- Cách kiểm: `python skills/tc-authoring/scripts/tc_check.py <file>.xlsx` → mã thoát 0
- Gate: mức 3 · tc_check.py
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-05 · Rule 3 nói rõ "màn hình" tính theo mục menu: danh sách, chi tiết, hộp thoại mở từ cùng một mục menu nằm chung một sheet, như sheet Scopes. Vai trò, gộp và tách sheet chuyển sang mục G. Xem FB-???[chia-sheet], FB-???[gop-tach-sheet].

## FB-011 · Học cấu trúc cha–con và gộp ô của bộ TC mẫu
- Ngày: 2026-09-30
- Nguồn: chat 30/09 · "Ở file thứ 4 có sheet Test Design, theo tôi đây là cấu trúc cha - con > chúng ta cùng học các merge ô, các case thành công, thất bại vào 1 khu vực"
- Loại: L4-mẫu
- Địa chỉ: rules/tc-authoring.md#C · rules/tc-authoring.md#F · references/format.md
- Tiêu chí kiểm: bốn cấp Classification đúng nghĩa; case cùng nhóm kết quả nằm liền nhau nên gộp được
- Phạm vi ảnh hưởng: mọi sheet test case
- Đã sửa: quy ước bốn cấp + quy tắc xếp case liền nhau + script tự gộp ô
- Cách kiểm: mở file, kiểm cụm gộp không vượt ranh giới cụm cha
- Gate: mức 3 · tc_build_xlsx.py tự gộp, không gộp tay
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-012 · Hệ thống chỉ là bản hiển thị, chưa chạy thật
- Ngày: 2026-09-30
- Nguồn: chat 30/09 · "vì hệ thống chưa chắc đã hoạt động đc, nó chỉ là hiển thị thôi, còn chưa chạy đc thực tế"
- Loại: L6-tri thức
- Địa chỉ: rules/common.md#9 · rules/tc-authoring.md#A
- Tiêu chí kiểm: không có kết quả mong đợi nào lấy từ hành vi của prototype
- Phạm vi ảnh hưởng: mọi TC viết trước khi có bản chạy thật
- Đã sửa: common.md v0.2→v0.3 thêm rule 9 về thứ tự nguồn chân lý
- Cách kiểm: mỗi kết quả mong đợi phải dẫn được về tài liệu yêu cầu hoặc bản thiết kế
- Gate: mức 1
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-013 · Định dạng file test case
- Ngày: 2026-10-01
- Nguồn: chat 01/10 · "Merge các ô như hình > the font: Times New Roman, size: 10 > căn trái"
- Loại: L4-mẫu
- Địa chỉ: rules/tc-authoring.md#F · references/format.md#4 · scripts/tc_build_xlsx.py
- Tiêu chí kiểm: vùng dữ liệu dùng Times New Roman cỡ 10, căn trái; ô gộp căn giữa theo chiều dọc
- Phạm vi ảnh hưởng: mọi file test case xuất ra từ nay
- Đã sửa: ghi vào rule 18–19, và đặt cứng trong `tc_build_xlsx.py`
- Cách kiểm: mở file, kiểm phông và căn lề ở vùng dữ liệu
- Gate: mức 3 · script đặt định dạng, người viết không chỉnh tay
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 1
- Cập nhật: 2026-10-02 · Tái phát 1 — ngày 01/10 ở chat Testing người dùng nhận xét "lại sai form" trên file dựng bằng script (xem FB-019). Gate mức 3 hiện có đặt cứng một form không phải form của file mẫu, nên không chặn được lỗi này.
- Cập nhật: 2026-10-02 · Form không còn đặt cứng trong script: dự án có file mẫu thì sheet mới nhân bản form của sheet TC trong file mẫu (rule 24, `tc_add_sheet.py`), và `tc_check.py --like` so từng sheet với sheet mẫu. Cả hai thuộc skill v0.3, chờ chép vào `.claude/skills` (xem FB-019).

## FB-014 · Mỗi khi nhận tài liệu phải nêu đánh giá mục đích sản phẩm
- Ngày: 2026-09-30
- Nguồn: chat Analysis 30/09 · "hãy update vào skill, mỗi khi nhận tài liệu luôn cố gắng móc nối các dữ kiện để nói ra đánh giá mục đích của sản phẩm này là gì nha"
- Loại: L2-rule
- Địa chỉ: skills/ba-analysis/SKILL.md#bước-0
- Tiêu chí kiểm: `analysis.md` của mọi lần phân tích mở đầu bằng đoạn mục đích sản phẩm có nguồn hoặc nhãn [SUY LUẬN], kèm danh sách soát ngược
- Phạm vi ảnh hưởng: 1 sản phẩm hiện có — `projects/sgs-dtp/docs/analysis/SGS-DTP-MVP-UC-List-v2.1/analysis.md` chưa có đoạn mục đích (xếp hàng chờ bổ sung); yêu cầu này trước đó chỉ nằm trong bản skill ở chat Analysis, chưa có trong bộ v0.3
- Đã sửa: `skills/ba-analysis/SKILL.md` v0.1→v0.2, bước 0 mục 5 và 6 (ghi nhận và gộp khi dựng thư mục qa-pipeline, 2026-10-02)
- Cách kiểm: mở `analysis.md`, mục đầu tiên là "Mục đích sản phẩm" và có ít nhất một dòng soát ngược
- Gate: mức 1 · văn xuôi trong skill; nên nâng thành mục trong checklist "Sẵn sàng bàn giao"
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-015 · Đổi tên cột Chờ text cho chuyên nghiệp hơn
- Ngày: 2026-10-02
- Nguồn: chat Building 02/10 · "nên thay đổi Chờ text thành câu khác chuyên nghiệp hơn nhé"
- Loại: L4-mẫu
- Địa chỉ: rules/tc-authoring.md#13 #16 #23 · skills/tc-authoring/references/format.md#3 · scripts/tc_build_xlsx.py · scripts/tc_check.py
- Tiêu chí kiểm: không còn chuỗi "Chờ text" trong rule, skill, mẫu, script và file TC xuất ra; cột W mang tên `Open question`
- Phạm vi ảnh hưởng: 6 file trong bộ quy tắc (1 rule, SKILL.md, format.md, templates.md, 2 script) — đã đổi hết; file TC đã xuất trước ngày này vẫn mang tên cột cũ, đổi khi xuất lại
- Đã sửa: đổi tên thành `Open question` (tên do AI chọn cho cùng ngôn ngữ với các cột khác — chờ người dùng xác nhận tên); `rules/tc-authoring.md` v0.1→v0.2; skill `tc-authoring` v0.1→v0.2
- Cách kiểm: tìm chuỗi "Chờ text" trong `rules/` và `.claude/skills/` → 0 kết quả
- Gate: mức 3 · tên cột đặt cứng trong `tc_build_xlsx.py`
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-02 · File `projects/sgs-dtp/exports/SGS-DTP_TestCase.xlsx`: cột W của sheet Login và Scopes đã mang tên `Open question`.

## FB-016 · Toàn bộ phải đồng nhất màu sắc, font chữ
- Ngày: 2026-10-02
- Nguồn: chat Building 02/10 · "thêm rule là toàn bộ phải đồng nhất màu sắc, font chữ ..."
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#22 · skills/tc-authoring/references/format.md#4 · scripts/tc_check.py
- Tiêu chí kiểm: mọi ô có nội dung ở mọi sheet dùng Times New Roman 10 và chỉ dùng màu trong bảng màu của format.md §4
- Phạm vi ảnh hưởng: mọi file test case; sheet phụ (Cover, Hướng dẫn, _Data, _Labels, FLOW-nn, Test_Report) trước đây không có quy ước định dạng. Chưa quét file TC nào đã xuất vì chưa có file nào trong thư mục dự án. `tc_export_xlsx.py` của skill test-design dùng định dạng riêng — xếp hàng chờ đồng bộ
- Đã sửa: rule 22; bảng màu trong format.md §4; `tc_check.py` thêm kiểm phông, cỡ chữ, màu nền, màu chữ cho mọi sheet. Phần "..." hiểu là cỡ chữ, màu nền, màu chữ, đường kẻ — chờ người dùng xác nhận phạm vi
- Cách kiểm: `python .claude/skills/tc-authoring/scripts/tc_check.py <file>.xlsx` → không có dòng "ô sai phông / cỡ chữ / màu nền / màu chữ"
- Gate: mức 3 · tc_check.py
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 1
- Cập nhật: 2026-10-02 · Tái phát 1 — người dùng nhắc lại ở chat Testing: "cả font chữ cũng đang bị khác nhau nè" (trên file `SGS-DTP_TestCase.xlsx` dựng ngày 01/10, trước bản ghi này). Bảng màu duy nhất đổi từ `17324D` sang một màu của file mẫu theo FB-019.
- Cập nhật: 2026-10-02 · Vì sao gate mức 3 không chặn được lần tái phát: `tc_check.py` v0.2 bỏ qua màu indexed và màu theme (nền xanh lá của Round 2 là màu indexed 17), và chỉ xét ô có nội dung. Bản v0.3 (chờ chép từ `_cho-duyet/tc-authoring-v0.3/`) đọc thẳng XML và xét mọi kiểu ô đang dùng: ô trống đã định dạng, kiểu mặc định của cột và dòng, chữ định dạng riêng từng đoạn, chữ nghiêng, gạch chân, màu theme và indexed. Bảng màu duy nhất giờ là `00B0F0` / `FFFFFF` / `363A45` / `FBE9E7` / `B8362B` (format.md §4, `tc_palette.py`). Đã quét `projects/sgs-dtp/exports/SGS-DTP_TestCase.xlsx`: 4 sheet, 0 lỗi định dạng.

## FB-017 · Đọc sai phạm vi UC
- Ngày: 2026-10-01
- Nguồn: chat Testing 01/10 · "đăng xuất pải có chứ > sau khi login dc thì sẽ logout dc" · "trong figma làm gì có chỗ nào quên mật khẩu, nhưng trong UC thì có à? tương tự với đổi mật khẩu cũng vậy?"
- Loại: L2-rule
- Địa chỉ: rules/ba.md#3 · skills/ba-analysis/SKILL.md · rules/tc-authoring.md#10
- Tiêu chí kiểm: trước khi gắn UC cho TC, mỗi UC có nhãn phạm vi suy từ bốn cột `ESt (Hour)`, `LTS suggestion`, `SGS Comments`, `WBS Reference` của UC List; UC không có giờ hoặc đang được đề xuất lùi không được coi là đã chốt, và UC có giờ không bị xếp "chưa có màn → chặn" chỉ vì thiết kế chưa vẽ
- Phạm vi ảnh hưởng: 2 sản phẩm của chat Testing 01/10, chưa nằm trong thư mục — sheet Login (UC-AUTH-002/003/004 bị gộp chung là "chưa có màn": AUTH-002 có 4 giờ và WBS nêu tên `CP-01 User login & logout`; AUTH-003/004 không có giờ, LTS ghi Phase 2, SGS trả lời "Ok. In case reset is needed, team can support the client") · sheet Scopes bản nháp (4 TC độ phủ gắn UC-RDN-004 như đã chốt, trong khi RDN-001/004 không có giờ, LTS ghi Phase 2, SGS chưa trả lời)
- Đã sửa: Login — đối chiếu lại bốn cột (AUTH-001 14 giờ + AUTH-002 4 giờ + AUTH-005 12 giờ); Scopes — 4 TC độ phủ chuyển sang chờ câu hỏi Q-S-11. Đề xuất nhãn `[ĐÃ CHỐT]` / `[ĐỀ XUẤT LÙI]` / `[SUY RA]` / `[NGOÀI MVP]` mới nêu trong chat, chưa ghi vào rule nào của thư mục
- Cách kiểm: tự soát — với mỗi UC được gắn cho TC, đọc được giá trị bốn cột và nhãn phạm vi của nó
- Gate: mức 1
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0
- Cập nhật: 2026-10-02 · Chuyển từ sổ tạm của chat Testing (ở đó mang số FB-014) vào sổ chính khi chat này bắt đầu dùng thư mục qa-pipeline; đổi số vì FB-014 của sổ chính là bản ghi khác.

## FB-018 · Khảo sát prototype chỉ trong màn đang viết
- Ngày: 2026-10-01
- Nguồn: chat Testing 01/10 · "bỏ qua cái demo đó nhé, tập trung Scopes"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#A
- Tiêu chí kiểm: mọi thao tác trên hệ thống đang chạy phục vụ trực tiếp màn đang viết; đổi vai trò hay mở phần demo chỉ khi người dùng yêu cầu
- Phạm vi ảnh hưởng: các lần khảo sát prototype về sau; ở lần 01/10 đã dừng thao tác đổi vai trò trên thanh Demo
- Trạng thái: Mới
- Tái phát: 0
- Cập nhật: 2026-10-02 · Chuyển từ sổ tạm của chat Testing (ở đó mang số FB-015). Việc nâng câu này thành rule chung là suy luận của AI — chờ người dùng xác nhận có muốn thành rule không.

## FB-019 · File TC phải đúng form file mẫu của dự án
- Ngày: 2026-10-01
- Nguồn: chat Testing 01/10 · "lại sai form r, nó pải có mẫu như bên này chứ, b hãy cho 1 sheet ngay bên cạnh sheet login có format tương tự nhé, hãy xem thật kỹ file này"
- Loại: L4-mẫu
- Liên quan: tái phát của FB-013; lệch với cách triển khai FB-016 (rule 22)
- Địa chỉ: rules/tc-authoring.md#22 · skills/tc-authoring/references/format.md#4 · skills/tc-authoring/scripts/tc_build_xlsx.py · skills/tc-authoring/scripts/tc_check.py (PALETTE) · projects/<dự-án>/profile.md (dòng "File TC mẫu của dự án")
- Tiêu chí kiểm: sheet TC mới cùng form với sheet TC trong file mẫu của dự án — khối thông tin, khối tổng kết vòng test, hàng tiêu đề, độ rộng cột, phông, màu, viền, căn lề, dropdown Priority/Result
- Phạm vi ảnh hưởng: đo ngày 02/10 bằng `tc_check.py` của thư mục trên file theo form mẫu `SGS-DTP_TestCase.xlsx` (Cover, Test_Report, Login, Scopes; bàn giao ở chat Testing 01/10) — 12 lỗi. Riêng sheet Login, chính sheet người dùng gửi làm mẫu và được giữ nguyên, có 46 ô nền ngoài bảng màu (ví dụ `00B0F0`), 517 ô màu chữ ngoài bảng màu (ví dụ `363A45`), 2 ô phông Arial (W11, X11). Ngược lại, file dựng bằng `tc_build_xlsx.py` (tiêu đề nền `17324D`) là form người dùng đã nhận xét "sai form" ngày 01/10
- Mâu thuẫn: rule 22 đặt một bảng màu duy nhất theo format.md §4 (tiêu đề `17324D`, nhãn `EAE7E1`, dòng câu hỏi mở `FBE9E7`); file mẫu của dự án dùng bảng màu khác (tiêu đề `00B0F0`, khối Round 2 xanh lá, chữ `363A45`, viền nét rất mảnh, không tô nền dòng câu hỏi mở). Hai yêu cầu "đúng form file mẫu" (01/10) và "đồng nhất màu sắc, font chữ" (FB-016, 02/10) chỉ cùng đúng được khi bảng màu duy nhất chính là bảng màu của file mẫu
- Lựa chọn A: bảng màu duy nhất lấy theo file mẫu của dự án. Hệ quả — sửa format.md §4 và PALETTE của hai script theo màu file mẫu; trong file mẫu đưa các ô lệch về cùng kiểu (2 ô tiêu đề W11, X11; phông của Cover và Test_Report); sheet mới dựng bằng cách nhân bản sheet mẫu
- Lựa chọn B: giữ bảng màu hiện có của format.md §4. Hệ quả — file mẫu không còn là form; phải dựng lại mọi sheet, kể cả sheet Login mẫu, sang bảng màu này; rule ghi rõ form do rule quyết định, không do file mẫu
- Đã sửa: ở chat Testing 01/10, chưa nằm trong thư mục — thêm sheet Scopes vào chính file mẫu bằng cách nhân bản sheet Login; script `tc_add_sheet.py` và tuỳ chọn `tc_check.py --like`
- Cách kiểm: sau khi người dùng chọn A hoặc B — `tc_check.py` sạch trên file mẫu và trên sheet mới
- Gate: mức 1 · rule 24 dạng văn xuôi. Gate mức 3 (`tc_check.py` v0.3: `--like`, bảng màu mới) đã viết và chạy sạch, nhưng chưa có hiệu lực cho tới khi được chép từ `_cho-duyet/tc-authoring-v0.3/` vào `.claude/skills/tc-authoring/`
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-02 · Chuyển từ sổ tạm của chat Testing (ở đó mang số FB-016); đổi số vì FB-016 của sổ chính là bản ghi khác.
- Cập nhật: 2026-10-02 · Người dùng trả lời ở chat Testing: "cho 1 trong 2 màu xanh này nhé, cả font chữ cũng đang bị khác nhau nè" (kèm ảnh sheet Scopes: mũi tên chỉ khối Round 1 xanh dương và tiêu đề Round 2 xanh lá; hai ô tiêu đề cuối đang nền `17324D`, phông Arial). Hiểu là lựa chọn A, và mọi ô nền tiêu đề chỉ dùng một trong hai màu của file mẫu. [GIẢ ĐỊNH] chọn xanh dương `00B0F0` — màu file mẫu dùng nhiều nhất (nhãn, Round 1, Cover); khối Round 2 đổi sang cùng màu này.
- Cập nhật: 2026-10-02 · Đã sửa theo lựa chọn A. Sản phẩm — `projects/sgs-dtp/exports/SGS-DTP_TestCase.xlsx` (Cover, Test_Report, Login, Scopes): mọi ô có nền dùng một màu `00B0F0` (khối Round 2, hai ô tiêu đề cuối, tiêu đề và dòng tổng của Test_Report đổi theo), mọi ô Times New Roman 10, chữ `363A45`; ô `Open question` của dòng còn câu hỏi mở tô `FBE9E7` (Login 32 dòng, Scopes 68 dòng); bỏ 8 quy tắc tô màu theo Priority nằm ngoài bảng màu; nguồn phẳng của sheet Scopes ở `exports/_flat/Scopes.tsv`. Rule — `rules/tc-authoring.md` v0.3, rule 24. Skill v0.3 — `SKILL.md`, `references/format.md` §4, `references/templates.md`, `scripts/tc_palette.py` (mới), `tc_add_sheet.py` (mới), `tc_restyle.py` (mới), `tc_check.py`, `tc_build_xlsx.py`: nằm ở `_cho-duyet/tc-authoring-v0.3/` vì phiên chat trên đám mây không được ghi vào `.claude/`; chờ người dùng chép vào `.claude/skills/tc-authoring/`. Kiểm ngày 02/10 trên máy người dùng: `tc_check.py` v0.3 `--like Login` → 2 sheet · 17 UC · 0 lỗi · 0 cảnh báo; `tc_check.py` v0.2 đang cài → 8 lỗi màu, vì còn bảng màu cũ.
- Cập nhật: 2026-10-02 · [GIẢ ĐỊNH] chờ người dùng xác nhận: (1) màu nền tiêu đề là xanh dương `00B0F0`, không phải xanh lá — đổi được bằng một dòng `HEAD_FILL` trong `tc_palette.py` rồi chạy `tc_restyle.py`; (2) tiêu đề `TEST CASE` ở trang bìa về cỡ 10 theo rule 22 (file mẫu: Tahoma 20); (3) dòng tổng của Test_Report dùng chung màu nền tiêu đề (file mẫu: hai màu nhạt). Sửa tại chỗ ngoài phạm vi màu và phông (L1): khối tổng kết của sheet Login đếm từ dòng 25 trong khi dữ liệu bắt đầu ở dòng 13 — kéo 10 công thức về dòng 13; `tc_check.py` v0.3 có thêm phép kiểm này.
- Cập nhật: 2026-10-02 · File mẫu khác rule ở bốn điểm; giữ nguyên theo file mẫu (rule 24), chờ người dùng quyết: (a) ô `Bug_ID` của Round 1 (P11) và cột `Blocked` của khối tổng kết (P3:P7) căn trái, các ô tiêu đề khác căn giữa; (b) ô `Classification` chỉ gộp B11:D11, chưa phủ cột IV (format.md §2 ghi gộp bốn cột); (c) dòng `Reference` và các dòng dữ liệu của sheet Login cao cố định nên chữ nhiều dòng bị che; (d) dropdown Priority của file mẫu có thêm `Critical`, trong khi format.md §7 và `tc_check.py` chỉ nhận High / Medium / Low. Xếp hàng: `tc_export_xlsx.py` của skill test-design vẫn dùng định dạng riêng (đã nêu ở FB-016); lệnh kiểm ở `CLAUDE.md` chưa có `--like` — AI không tự sửa `CLAUDE.md`.

## FB-020 · Dự án Playwright thử nghiệm phải tách riêng và rút thành rule
- Ngày: 2026-10-02
- Nguồn: chat Building 02/10 · "hãy tách biệt cho mình nhé, đây là thử nghiệm của dự án đã viết Script trc đây để b lấy đó là dự án mới > build vào rule cho tôi nhé"
- Loại: L2-rule
- Liên quan: rules/automation.md (v0.1 chưa có rule về cấu trúc, môi trường, chờ, dữ liệu)
- Địa chỉ: rules/automation.md#11-18 · automation/_template/ · automation/feec-learning/ · CLAUDE.md (mục Nhiều dự án) · README.md
- Tiêu chí kiểm: dự án mới sao từ `automation/_template/` chạy được sau khi điền `.env`; test không dùng `waitForTimeout`, `networkidle`, dữ liệu theo tên có sẵn; kết quả có ở `runs/latest.json`
- Phạm vi ảnh hưởng: 5 test fail ở lần chạy thật đầu tiên (02/10) đều do các điểm này — `#` cuối mật khẩu bị cắt trong `.env` (đăng nhập fail), `networkidle` (3 test tìm kiếm quá giờ), file mẫu `25_03_18 (11).txt` không có trên môi trường mới (1 test), menu `その他` đóng trước khi bấm (1 test)
- Đã sửa: tách dự án thử nghiệm thành `automation/feec-learning/` (đã dọn code, config theo `.env`, JSON reporter); thêm `automation/_template/`; thêm rule 11–18 vào `rules/automation.md` v0.2
- Cách kiểm: chạy lại `npm test` trong `automation/feec-learning/`, đọc `runs/latest.json`
- Gate: mức 1 · văn xuôi; mẫu dự án là mức 3 một phần (chạy được hay không)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-02 · Người dùng: "bh hãy dùng luôn folder này làm đoạn code playwright luôn nhé" — `automation/feec-learning/` là thư mục code Playwright chính thức, không còn gọi là thử nghiệm.
- Cập nhật: 2026-10-02 · Rule 11–18 là rút kinh nghiệm của AI từ lỗi thật; người dùng chỉ yêu cầu tách và đưa vào rule — nội dung từng rule chờ người dùng duyệt.

## FB-021 · Bộ TC FEEC Document v3 đã lỗi thời, đi từ TC để cập nhật BA
- Ngày: 2026-10-02
- Nguồn: chat 02/10 · "Hiện tại thông tin TCs trong đây đang bị out of date > vd: chỉ cho 10 cấp nhưng giờ là 20 cấp" · "Hãy đi từ TCs để update BA nhé > Tạo mới folder"
- Loại: L6-tri thức
- Địa chỉ: projects/quan-ly-tai-lieu/docs/analysis/Quan_ly_tai_lieu_mockup-v5/analysis.md#7 · projects/quan-ly-tai-lieu/profile.md
- Tiêu chí kiểm: mọi quy tắc lấy từ `FEEC_PM_IT_Test_Case_Document_v3.xlsx` trong analysis ghi vị trí ô (Document!Rnn · TC_nnn); chỗ TC lệch với trả lời của người dùng thì theo trả lời và ghi rõ TC đã lỗi thời
- Phạm vi ảnh hưởng: quét cả sheet Document bằng script — 17/150 TC còn giới hạn cũ 10/11 cấp: 2 TC tạo thư mục (TC_080, TC_081) và 15 TC tải thư mục/ZIP lên (TC_085, 088, 090, 093, 096, 098, 101, 107, 109, 113, 116, 118, 121, 124, 126). Lần này chỉ cập nhật phần Tạo mới folder; 15 TC tải lên xếp hàng chờ, kèm câu hỏi giới hạn 20 cấp có áp cho tải lên không (Q-12)
- Liên quan: Q-06, Q-08, Q-10, Q-12, Q-13
- Đã sửa: analysis.md v0.1→v0.2 thêm §7 (nguồn, bảng NV / FD / MS / BR / luồng / SE, rà soát 8 TC, thứ tự đề xuất) và F-35 → F-42; questions.md v0.1→v0.2 ghi trả lời một phần cho Q-06, Q-08, Q-10, Q-13; profile.md thêm 5 quyết định ngày 02/10; thêm tc-inventory-tao-thu-muc.md (lượt 1 của bộ TC, sinh bằng script)
- Cách kiểm: mở analysis.md §7, mỗi dòng NV, MS, BR, SE có cột Nguồn; giới hạn "10 cấp" chỉ còn xuất hiện khi trích TC cũ và đều ghi là lỗi thời
- Gate: mức 1
- Trạng thái: Đã sửa sản phẩm
- Cập nhật: 2026-10-02 · Đang được gọi tạm là FB-021 trong analysis.md, questions.md, profile.md.
- Cập nhật: 2026-10-02 · Phần Tạo thư mục sau đó làm lại theo cách gọn (bản ghi "Làm gọn" bên dưới). Các quyết định chốt sau khi Hanna trả lời Q1–Q12, C2, C3 nằm ở tao-thu-muc_nghiep-vu-srs-us-uc.md; analysis.md §7, questions.md v0.2 và profile.md chưa cập nhật theo các trả lời này.
- Tái phát: 0

## FB-022 · Dịch tạm thông báo tiếng Nhật sang tiếng Việt, không hỏi từng câu
- Ngày: 2026-10-02
- Nguồn: chat 02/10 · "Ngoài ra tôi muốn chuyển thông báo từ tiếng Nhật sang tiếng Việt (ko cần hỏi lại câu cụ thể, đại khái là được)"
- Loại: L2-rule
- Địa chỉ: rules/common.md#6 · rules/tc-authoring.md#16 · projects/quan-ly-tai-lieu/docs/analysis/Quan_ly_tai_lieu_mockup-v5/analysis.md#7
- Tiêu chí kiểm: mỗi thông báo tiếng Nhật thuộc phạm vi đang làm có một bản tiếng Việt gắn nhãn [DỊCH TẠM], và text gốc tiếng Nhật vẫn giữ nguyên văn ở cột bên cạnh
- Phạm vi ảnh hưởng: phần Tạo mới folder có 2 thông báo tiếng Nhật (TC_081, TC_082, ô K93/W93, K94/W94) và 2 chuỗi tham chiếu ở Đổi tên (TC_054, TC_055). Cả sheet Document có 129 ô tiếng Nhật trên 48 TC — chưa dịch vì ngoài phạm vi. Xung đột với rule đang có: common.md rule 6 ("Giữ nguyên văn text gốc … không dịch") và tc-authoring.md rule 16 (chuỗi chưa có bản dịch chính thức thì giữ gốc, tô đỏ, ghi Open question). Cách làm lần này không bỏ rule: giữ nguyên văn tiếng Nhật, thêm bản dịch tạm bên cạnh. Chưa rõ: chỉ áp cho lần này, hay thành ngoại lệ chung của hai rule trên
- Liên quan: Q-10
- Đã sửa: analysis.md §7.5 có cột "Tiếng Việt [DỊCH TẠM]" cho MS-01, MS-02 và chuỗi tham chiếu MS-03; text tiếng Nhật giữ nguyên văn ở cột bên cạnh
- Cách kiểm: ở analysis.md §7.5, mỗi dòng MS-01, MS-02, MS-03 vừa có 「…」 tiếng Nhật vừa có bản tiếng Việt cùng dòng
- Gate: mức 1
- Trạng thái: Chưa rõ phạm vi
- Cập nhật: 2026-10-02 · Đang được gọi tạm là FB-022 trong analysis.md, questions.md, profile.md.
- Cập nhật: 2026-10-02 · Trong tài liệu gọn tao-thu-muc_nghiep-vu-srs-us-uc.md, các câu thông báo Hanna đưa thẳng bằng tiếng Việt (vd "Vui lòng nhập tên tệp.") được dùng nguyên văn; câu tiếng Nhật chỉ còn giữ để đối chiếu ở MSG-01.
- Tái phát: 0

## FB-023 · tc_check.py bỏ sót kết quả mơ hồ khi chữ ở dạng tổ hợp
- Ngày: 2026-10-02
- Nguồn: AI đề xuất khi rà `FEEC_PM_IT_Test_Case_Document_v3.xlsx` cho phần Tạo mới folder — chờ duyệt
- Loại: L5-script
- Địa chỉ: skills/tc-authoring/scripts/tc_check.py
- Tiêu chí kiểm: tc_check.py chuẩn hoá Unicode về NFC trước khi so từ mơ hồ, khoá {{…}} và nhãn; ô K95 「- Cho phép tạo bình thường」 phải bị báo là mơ hồ
- Phạm vi ảnh hưởng: sheet Document có 378 / 1.737 ô chữ ở dạng tổ hợp; 16 TC có kết quả mơ hồ đang bị bỏ sót (TC_083, TC_106 → TC_110, TC_115 → TC_119, TC_123 → TC_127)
- Trạng thái: Mới
- Cập nhật: 2026-10-02 · Đang được gọi tạm là FB-023 trong analysis.md.
- Tái phát: 0

## FB-024 · tc_build_xlsx.py đánh lại TVP_ID khi chèn hoặc xếp lại dòng
- Ngày: 2026-10-02
- Nguồn: AI đề xuất khi lập thứ tự mới cho khu vực Tạo thư mục (analysis.md §7.9) — chờ duyệt
- Loại: L5-script
- Địa chỉ: skills/tc-authoring/scripts/tc_build_xlsx.py · rules/tc-authoring.md#11 · rules/common.md#3
- Tiêu chí kiểm: chèn một dòng vào giữa rồi dựng lại file, các TC cũ giữ nguyên TVP_ID và TC mới lấy số tiếp theo
- Phạm vi ảnh hưởng: mọi file dựng bằng tc_build_xlsx.py — script sinh "TC_%03d" theo thứ tự dòng, TSV không có cột TVP_ID. Với khu vực Tạo thư mục, xếp lại theo §7.9 sẽ đổi ID của TC_079 → TC_083 và làm Bug_ID cũ mất liên kết (TC_081 đang gắn bug 1)
- Trạng thái: Mới
- Cập nhật: 2026-10-02 · Đang được gọi tạm là FB-024 trong analysis.md.
- Tái phát: 0

## FB-025 · Làm gọn: chỉ nghiệp vụ, câu hỏi, SRS / US / UC, không chạy cả bộ rule
- Ngày: 2026-10-02
- Nguồn: chat 02/10 · "chết thật, t dã xây dựng quá nhiều rule trong khi t chỉ cần break out 1 số điểm thôi > tập trung tìm hiểu mỗi phần tạo mới thư mục cần hiểu những nghiệp vụ nào, cần hỏi lại những gì, sau đó đưa ra SRS/US/UC phù hợp thôi á > tiếp sau mới đi đến viết TCs chỉ riêng phần tạo thư mục chứ ko pải quá nhiều rule như trên"
- Loại: L2-rule
- Địa chỉ: CLAUDE.md#quy-trình · CLAUDE.md#cổng-con-người · rules/common.md#2 · rules/common.md#8 · rules/feedback.md#1
- Tiêu chí kiểm: khi người dùng yêu cầu làm gọn một phần, sản phẩm chỉ gồm nghiệp vụ cần hiểu, câu hỏi kèm đề xuất mặc định, SRS / US / UC; không ghi FB, không chạy script, không dừng ở cổng, trừ khi người dùng yêu cầu
- Phạm vi ảnh hưởng: xung đột với quy trình đang có — CLAUDE.md (bước 1 → 5 có cổng và script), common.md rule 2 (câu hỏi xếp mức CHẶN / QUAN TRỌNG / NHỎ, dừng ở cổng), common.md rule 8 và feedback.md rule 1 (mọi nhận xét thành FB trước khi sửa). Hai lựa chọn: (1) cách làm gọn chỉ dùng khi người dùng nói rõ, bộ rule đầy đủ vẫn là mặc định — giữ được kiểm soát, nhưng mỗi lần muốn gọn phải nhắc; (2) cách làm gọn là mặc định, bộ rule đầy đủ chỉ chạy khi được yêu cầu — nhanh hơn, nhưng script và checklist không tự chạy nữa. Chưa rõ chọn cách nào, và có áp cho phần khác hay dự án khác không
- Đã sửa: phần Tạo thư mục làm theo cách gọn — tao-thu-muc_nghiep-vu-srs-us-uc.md (16 điểm nghiệp vụ, 12 câu hỏi kèm mặc định, 9 FR, 10 BR, 8 thông báo, 23 AC, UC-DOC-007 kèm sơ đồ luồng); trong lúc làm không ghi FB, không chạy script
- Trạng thái: Chưa rõ phạm vi
- Tái phát: 0

## FB-026 · Thay TC bằng file phân tích case cha con, dễ nhìn, dễ hiểu
- Ngày: 2026-10-02
- Nguồn: chat 02/10, trả lời câu hỏi "Viết TC phần tạo thư mục ra đâu?" · "không cần viết TCs mà cho tôi file phân tích chi tiết theo kiểu case cha con, dễ nhìn, dễ hiểu"
- Loại: L4-mẫu
- Địa chỉ: skills/test-design/references/templates.md · projects/quan-ly-tai-lieu/tests/design/Tao_thu_muc_phan_tich_case_cha_con.xlsx
- Tiêu chí kiểm: file phân tích có cột Case cha (gộp ô theo nhóm) và Case con; mỗi case con có điều kiện / dữ liệu, thao tác, kết quả mong đợi, căn cứ và trạng thái (Đã chốt / Theo mặc định / Suy ra / Còn mở)
- Phạm vi ảnh hưởng: phần Tạo thư mục — 11 case cha, 74 case con. Chưa rõ: chỉ dùng cho phần này, hay thành mẫu chung thay cho bước viết TC
- Đã sửa: tạo Tao_thu_muc_phan_tich_case_cha_con.xlsx gồm 4 sheet: Case cha con, Thông báo, Quy tắc, Còn mở; chưa thêm mẫu vào templates.md
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-027 · Bàn giao bằng một zip giữ cấu trúc thư mục, kèm danh sách file và fb-moi.md
- Ngày: 2026-10-02
- Nguồn: chat 02/10 · "Hãy xuất toàn bộ file bạn đã tạo hoặc sửa trong project này thành một file zip, giữ nguyên cấu trúc thư mục như trong `Documents\qa-pipeline` (ví dụ `projects/quan-ly-tai-lieu/docs/analysis/...`, `.claude/skills/...`). Kèm một danh sách ghi: file nào, thư mục đích nào, mới hay sửa file cũ. Bản ghi FB mới gom thành một file `fb-moi.md`, ghi rõ nguyên văn yêu cầu của tôi, chưa cần đánh số."
- Loại: L4-mẫu
- Địa chỉ: DOC-TRUOC.md#5 · DOC-TRUOC.md#6
- Tiêu chí kiểm: gói bàn giao là một file zip; đường dẫn trong zip trùng đường dẫn trong qa-pipeline; có danh sách ghi file, thư mục đích, mới hay sửa; FB mới nằm trong feedback/fb-moi.md, chưa đánh số, trường Nguồn trích nguyên văn
- Phạm vi ảnh hưởng: mọi lần bàn giao từ chat web. Gói xuất ngày 02/10 gồm trọn nội dung hai gói đã gửi trước đó trong cùng chat (v0.1, v0.2), trừ FB-017-020_gop-vao-so-goc.md vì đã thay bằng file này
- Đã sửa: gói qa-pipeline_xuat_2026-10-02.zip kèm _DANH-SACH-FILE.md và feedback/fb-moi.md; chưa sửa DOC-TRUOC.md
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-028 · Học cách kiểm của người dùng: case ngoài nghiệp vụ để tránh lọt bug
- Ngày: 2026-10-02
- Nguồn: chat Building 02/10 · "hãy học cách viết TCs mà tôi đã hướng dẫn cho acc kia, ko cần chạy playwright nữa, nhưng cần update các cách test tránh lọt bug". Hướng dẫn gốc (ảnh chụp chat với tài khoản kia): "giả sử c đang có 2 page, mỗi page có hiện 50 items, tức là có từ 51 > 100 items. lỗi xảy ra ko hiển thị page nào vì c có trên 100 items > hóa ra là lỗi liên quan đến infrastructure / FE gì đó" · "có rất nhiều case c bắt lỗi ko phải do nghiệp vụ mà chưa ai nghĩ ra dc case nhé" · (ảnh breadcrumb tên dài `2222…` › `3333…`) · "ngoài ra có những case click vào các tên folder thì nó hiện ra đúng nội dung bên trong, nhưng thực tế nhiều khi nó bị lỗi" · "có ti tỉ thứ sẽ dc coi là bug"
- Loại: L6-tri thức
- Liên quan: FB-026 (file phân tích case cha con) · tái phát của nhóm "bug lọt do chỉ viết TC từ nghiệp vụ"
- Địa chỉ: skills/test-design/references/technical-risk-checklist.md · skills/test-design/references/coverage-checklist.md#D,E · skills/test-design/references/templates.md#7 · skills/test-design/SKILL.md · skills/tc-authoring/references/patterns.md#P9,P12 · rules/tester.md#12,13
- Tiêu chí kiểm: mỗi màn hình có dòng EG (nguồn `CK-…`) cho từng mục A–G hoặc lý do không áp dụng; có case tổng số mục trên 100, tên dài không khoảng trắng, bấm vào tên ở nhiều cấp, giới hạn − 1 / bằng / + 1; case không có căn cứ ghi "Ghi lại hệ thống làm gì" và có câu hỏi
- Phạm vi ảnh hưởng: mọi bộ test; áp thử cho Tạo thư mục — file case cha con có 74 case con nhưng không có nhóm nào về khối lượng dữ liệu, tên dài trên giao diện, điều hướng nhiều cấp, dữ liệu sau thao tác, bộ gõ; bổ sung 5 nhóm (12–16, 21 case) ở `projects/quan-ly-tai-lieu/tests/design/bo-sung-case-ngoai-nghiep-vu_tao-thu-muc.md`
- Đã sửa: thêm `technical-risk-checklist.md` (A–G, 36 mục); coverage-checklist thêm kiểu bug 16–20 và mục E; patterns P9, P12; templates §7 (mẫu case cha con); test-design SKILL v0.2; rules/tester.md v0.3 rule 12, 13
- Cách kiểm: sau khi người dùng duyệt, chạy lại thiết kế cho một UC khác và đếm dòng EG theo `CK-`; so với số bug lọt ở vòng test sau
- Gate: mức 1 · văn xuôi (chưa có script kiểm mục `CK-`). `rtm_check.py` không cần sửa: nguồn là dòng EG có sẵn
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-02 · Người dùng không còn cần chạy Playwright cho lần này (bỏ qua việc chạy lại `npm test`). Các mục A–G là tổng quát hoá của AI từ ví dụ người dùng nêu — chờ người dùng bổ sung mục còn thiếu.
