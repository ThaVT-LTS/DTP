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
| FB-016 | Toàn bộ phải đồng nhất màu sắc, font chữ | L2-rule | Đã vào rule (chờ duyệt) | 3 |
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
| FB-029 | Chia sheet theo màn hình, vai trò nằm trong sheet | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-030 | Gộp, tách sheet theo màn hình, không theo module của UC list | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-031 | Viết TC bằng tiếng Anh; ít nhất tên nút giữ nguyên tiếng Anh | L2-rule | Đã duyệt | 0 |
| FB-032 | Trạng thái rỗng đặt trước, theo vòng đời dữ liệu rỗng → tạo → có dữ liệu | L2-rule | Đã duyệt | 0 |
| FB-033 | Trạng thái rỗng phải tả đủ icon, chữ, nút | L3-checklist | Đã duyệt | 0 |
| FB-034 | Không viết lửng lơ ở Expected và Step; không biết thì đưa vào Q&A | L2-rule | Đã duyệt | 1 |
| FB-035 | Pre-condition đăng nhập ghi bằng vai trò: "Đăng nhập với acc Customer Admin" | L4-mẫu | Đã duyệt | 1 |
| FB-036 | Nhiều mục thì mỗi mục một dòng, không nối bằng " · " | L4-mẫu | Đã duyệt | 0 |
| FB-037 | Giá trị tính toán phải nói lấy từ đâu; TC phải dễ sửa khi Figma, UC đổi | L2-rule | Bị bác | 0 |
| FB-038 | Gửi bản xem trước danh sách tính năng trước khi cập nhật file TC | L2-rule | Đã duyệt | 0 |
| FB-039 | TC gọi API chỉ viết khi tester được gọi API, và để ở sheet API riêng | L2-rule | Đã duyệt | 0 |
| FB-040 | Pre-condition không ghi mở màn hình đang test; liệt kê thao tác khi phải qua màn khác | L2-rule | Đã vào rule (chờ duyệt) | 1 |
| FB-041 | Thiếu case kiểm hiển thị từng thông tin sau khi tạo | L3-checklist | Đã vào rule (chờ duyệt) | 0 |
| FB-042 | Thông tin chưa kiểm chứng không được viết vào TC dạng khẳng định | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-043 | Nhóm Thành công của chức năng tạo: mỗi loại một case, bỏ case không cần thiết | L3-checklist | Đã vào rule (chờ duyệt) | 0 |
| FB-044 | Hiển thị ở màn chi tiết kiểm ở khu vực Chi tiết, không lặp ở khu vực Tạo mới | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-045 | Case kiểm tra dữ liệu có bước bấm nút gửi mà không lưu thì gộp vào nhóm Không thành công | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-046 | Bỏ {{…}}; dữ liệu chưa xác định viết chung chung trong ngoặc vuông [tên] | L4-mẫu | Đã vào rule (chờ duyệt) | 0 |
| FB-047 | Học cách viết của Hanna ở TC 1–67 sheet Scopes (v1.4) để viết phần còn lại | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-048 | Cột Evidence coverage cần nhiều TC hơn để xác định hiển thị thế nào là đúng | L3-checklist | Chưa rõ phạm vi | 0 |
| FB-049 | Ô bắt đầu bằng dấu gạch phải có dấu nháy đơn để không thành công thức | L5-script | Đã vào rule (chờ duyệt) | 0 |
| FB-050 | Hanna sửa trực tiếp bản v1.5: điền Expected, bỏ và sắp xếp lại case | L6-tri thức | Mới | 0 |
| FB-051 | Ba case đọc không hiểu ý: Vai trò trong danh sách, Customer Viewer, Ghi vết - Audit log | L2-rule | Chưa rõ phạm vi | 0 |
| FB-052 | Chuyển sang module 04 Framework Content Management: kiểm Figma và hệ thống, đề xuất case cha theo cách học từ Scopes | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-053 | Soát lại và sửa các TC của sheet Frameworks do model trước viết (bản v1.6) | L1-sản phẩm | Đã sửa sản phẩm | 0 |
| FB-054 | Sheet Frameworks: xoá câu hỏi đã có trả lời; ô Classification phải xuống dòng, căn giữa dọc, căn trái; giữ nguyên chữ Hanna sửa | L1-sản phẩm | Đã vào rule (chờ duyệt) | 0 |
| FB-055 | Sheet Frameworks bản 1.8: ghi chú ở Open question chưa thành câu hỏi, 2 case tìm theo Requirements/Updated mất câu hỏi, case Total to meet bước/Expected lệch nhau, dòng 1.7 ở Cover dẫn nhầm FB-054 | L1-sản phẩm | Đã vào rule (chờ duyệt) | 0 |
| FB-056 | Sheet Frameworks bản 1.9: đổi chữ Hanna ở case tìm theo Requirements/Updated, ô Open question còn dạng khẳng định, hồ sơ khung case cha sai số | L1-sản phẩm | Đã vào rule (chờ duyệt) | 0 |
| FB-057 | Giá trị tính toán (Total to meet): phải hiểu logic của nó trước khi viết, không viết bừa | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-058 | Comment của Hanna chờ lệnh: chỉ làm lại khi Hanna bảo | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-059 | Soát chéo hai model: Opus chỉ liệt kê lỗi, Sonnet sửa, lặp tới khi hết comment; đưa mọi góp ý vào rule, skill | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-060 | Chuyển sang module 06 Workspace Management (Figma Screens 05 Workspace & Evidence): kiểm Figma và hệ thống, đề xuất case cha, rút kinh nghiệm từ comment của Opus | L6-tri thức | Mới | 0 |
| FB-061 | Luồng tạo workspace đổi: không tạo từ màn Workspaces (Customer Admin) nữa mà tạo từ Scope › Link framework › Link and create workspace; UC lên v5.3, đọc trực tiếp bản mới nhất | L6-tri thức | Mới | 0 |
| FB-062 | Hanna chốt: viết TC như bình thường, câu hỏi chưa rõ ghi Open question; 11 case Gắn framework vẫn ở sheet Scopes; Q-W-03 (mode, tên, chu kỳ) Hanna chưa biết | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-063 | Hanna: Sonnet đọc review Opus (review_Workspaces_v1.11.md) là làm lại sheet Workspaces | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-064 | Hanna hỏi vì sao Sonnet vẫn bị comment nhiều: không cập nhật logic của màn đã làm khi luồng hoặc nguồn đổi, không tự soát trước khi giao | L6-tri thức | Đã vào rule (chờ duyệt) | 0 |
| FB-065 | Hanna yêu cầu viết TC cho 07. Evidence – Assisted mode: sheet Assisted workspace (v1.13) | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-066 | Hanna bảo đọc lại review Opus và update sheet Assisted workspace: sửa 36 lỗi, ra v1.14 | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-067 | Hanna: Opus soát một lần cho đủ lỗi, không tìm lắt nhắt; lỗi mới do Sonnet sửa thì được | L6-tri thức | Đã vào rule (chờ duyệt) | 0 |
| FB-068 | Hanna hỏi vì sao Sonnet sửa review v1.13 mà vẫn còn lỗi, chỉ đạt 26/36: sửa đúng chỗ review chỉ, không quét cùng kiểu lỗi, không chạy soát nội dung rule 38 | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-069 | Hanna bảo làm lại sheet Assisted workspace theo review v1.14 (18 mục): ra v1.15, mỗi kiểu lỗi quét cả sheet | L6-tri thức | Đã sửa sản phẩm | 0 |
| FB-070 | Bảy quy tắc viết TC SGS DTP Phase 1 từ bộ nhớ tài khoản web: theo web khi hợp lý, thông báo lỗi theo mẫu app, câu hỏi đã xoá là xong, UC chưa có trên web đánh dấu Phase 2, dòng đăng nhập "Login acc <role> (<tên>)" | L2-rule | Đã vào rule (chờ duyệt) | 0 |
| FB-071 | Đánh dấu Phase 2 bằng chữ Phase 2 ở cột Remark (V) Round 2, bỏ tiền tố [Phase 2] ở tên case: v0.2, 58 case | L4-mẫu | Đã sửa sản phẩm | 0 |
| FB-072 | Gom _cu, _sao-luu, _cho-duyet, _to_delete, tài liệu cập nhật, file TC cũ vào _luu-tru; 3 script vào skill; zip vào scripts/ | L5-script | Đã sửa sản phẩm | 0 |

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
- Cập nhật: 2026-10-05 · Rule 3 nói rõ "màn hình" tính theo mục menu: danh sách, chi tiết, hộp thoại mở từ cùng một mục menu nằm chung một sheet, như sheet Scopes. Vai trò, gộp và tách sheet chuyển sang mục G. Xem FB-029, FB-030.

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
- Cập nhật: 2026-10-05 · [Đề xuất của AI, chờ duyệt] Rà theo file mẫu khi xử lý FB-016 tái phát: ô dữ liệu ở cả file mẫu SGS và FEEC căn giữa theo chiều dọc, còn rule 19 và format.md §4 ghi căn trên; câu gốc của FB này chỉ nói "căn trái". Đề xuất sửa rule 19, format.md §4 và tc_build_xlsx.py thành căn giữa theo chiều dọc, như file mẫu (tài liệu cập nhật gộp ngày 05/10).

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
- Gate: mức 3 · tc_check.py; từ 07/10 thêm tc_fix_xlsx.py --check đọc thẳng XML (trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 3
- Cập nhật: 2026-10-02 · Tái phát 1 — người dùng nhắc lại ở chat Testing: "cả font chữ cũng đang bị khác nhau nè" (trên file `SGS-DTP_TestCase.xlsx` dựng ngày 01/10, trước bản ghi này). Bảng màu duy nhất đổi từ `17324D` sang một màu của file mẫu theo FB-019.
- Cập nhật: 2026-10-02 · Vì sao gate mức 3 không chặn được lần tái phát: `tc_check.py` v0.2 bỏ qua màu indexed và màu theme (nền xanh lá của Round 2 là màu indexed 17), và chỉ xét ô có nội dung. Bản v0.3 (chờ chép từ `_cho-duyet/tc-authoring-v0.3/`) đọc thẳng XML và xét mọi kiểu ô đang dùng: ô trống đã định dạng, kiểu mặc định của cột và dòng, chữ định dạng riêng từng đoạn, chữ nghiêng, gạch chân, màu theme và indexed. Bảng màu duy nhất giờ là `00B0F0` / `FFFFFF` / `363A45` / `FBE9E7` / `B8362B` (format.md §4, `tc_palette.py`). Đã quét `projects/sgs-dtp/exports/SGS-DTP_TestCase.xlsx`: 4 sheet, 0 lỗi định dạng.
- Cập nhật: 2026-10-05 · Tái phát. Hanna chỉ ra, nguyên văn: "Create: Hanna > cùng 1 font chữ nhé" (ảnh ô Scopes!C5). Ô Scopes!C5 (Creator = Hanna) dùng Arial 10, mọi ô khác Times New Roman 10; quét cả 7 sheet của SGS-DTP_TestCase1_v1.3 thì chỉ có ô này. tc_check.py có báo "Scopes · 1 ô sai phông: C5=Arial" nhưng lẫn trong 14 lỗi màu giả: bảng màu ở format.md §4 và trong hai script (17324D, EAE7E1, FFFFFF, C9C5BE) không khớp file TC mẫu (00B0F0, 363A45, FBE9E7, B8362B; file mẫu SGS và FEEC giống nhau). AI bỏ qua cả loại lỗi màu nên sót lỗi phông. Cảnh báo ký tự ngoài bảng chữ Latin cũng báo giả 17/27 dòng vì dấu · — ←. Sửa gate (chờ duyệt, ở tài liệu cập nhật gộp ngày 05/10): bảng màu theo file mẫu ở format.md §4, tc_check.py, tc_build_xlsx.py; cảnh báo ký tự bỏ qua dấu câu; SKILL Bước 7 thêm "không bỏ qua cả một loại lỗi; lỗi giả thì sửa bảng màu hoặc script trước". Kiểm: với bảng màu mới, tc_check.py trên v1.3 chỉ còn 1 lỗi (C5); sửa C5 xong còn 0 lỗi; cảnh báo ký tự còn 10 dòng, đều là nhãn giao diện 繁體中文 ở Profile. Đã sửa C5 ở bản làm việc, vào file TC bản tới.
- Cập nhật: 2026-10-07 · Tái phát 3 (lần ngày 05/10 đã có dòng Cập nhật ở trên nhưng số đếm chưa được tăng, nay cộng cả) — Hanna nhắc ở chat Testing 07/10, trên `SGS-DTP_TestCase1_v1.4.xlsx`: "Cần thống nhất tất cả các ô đều cùng font chữ Times New Roman và size 10." Quét v1.4 bằng script: 5 ô có nội dung đang là Arial 10 (Login!C5, C7; Users!C4; Scopes!J51, E56 — hai ô ở Scopes do Hanna vừa nhập); 817 ô dùng kiểu ô có phông Arial, phần lớn là ô bị gộp không hiển thị; 7 cột của sheet Cần xác nhận có kiểu mặc định Arial, nên gõ vào dòng mới của sheet đó sẽ ra Arial. Nguyên nhân: (1) `tc_check.py` đã báo phông Arial từ v1.2 nhưng file vẫn được gửi đi (`docs/VIEC-CON-MO.md` ghi "chưa quyết bỏ hay giữ"); (2) script chỉ xét ô có nội dung, không xét ô trống và kiểu mặc định của cột; (3) chưa có script đưa file có sẵn về một phông, nên mỗi lần phải sửa tay.
- Cập nhật: 2026-10-07 · Đã sửa ở bản v1.5: 16 kiểu ô Arial chuyển sang Times New Roman 10 (817 ô và kiểu mặc định của các cột ở sheet Cần xác nhận); `tc_fix_xlsx.py --check` trên bản v1.5: sạch. Xử lý ba nguyên nhân của lần tái phát 3: (1) SKILL Bước 7 ghi hai lệnh kiểm cùng sạch mới coi là qua; (2) `tc_fix_xlsx.py --check` xét mọi kiểu ô đang dùng, gồm ô trống, ô trong cụm gộp, kiểu mặc định của cột — `tc_check.py` dùng openpyxl nên không đọc được kiểu của ô trong cụm gộp; (3) `tc_fix_xlsx.py` đưa file có sẵn về một phông. `rules/tc-authoring.md` v0.5 rule 18 ghi rõ "mọi ô của mọi sheet". Kiểu Normal của file vẫn là Arial 10 như file mẫu, giữ để độ rộng cột không đổi: dùng Clear Formats thì ô về Arial — ghi ở format.md §4, chờ Hanna cho ý kiến có đổi kiểu Normal không.
- Cập nhật: 2026-10-07 · Không tăng Tái phát: lần này không phải Hanna nhắc và không phải file AI giao bị sai. Kiểm file Hanna sửa và gửi lúc 13:28 (lưu bằng ONLYOFFICE, `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx`) bằng `tc_fix_xlsx.py --check`: 18 ô ở sheet Scopes về phông Arial 10 — K39, H56 → H61, K62 → K65, K96, K117, K125, E130, K130, C142, C148; đều là ô Hanna vừa sửa hoặc vừa tô màu, các sheet khác không có. Nhìn trong file: kiểu ô của 18 ô này không còn khai phông riêng nên ô lấy phông của kiểu Normal, mà kiểu Normal của file là Arial 10. Bốn ô Hanna cũng sửa nội dung thì vẫn giữ Times New Roman (K43, K110, K112, K137), nên việc sửa chữ tự nó không làm mất phông; AI chưa xác định được thao tác nào làm mất (ngờ là dán cả ô từ chỗ khác vào) — cần hỏi Hanna. Đây là nguyên nhân gốc còn lại của FB này: chừng nào kiểu Normal còn là Arial thì ô mất định dạng sẽ ra Arial. Hai cách xử lý, chờ Hanna chọn: (A) giữ kiểu Normal, mỗi lần nhận file về chạy `tc_fix_xlsx.py` trước khi làm tiếp (đang làm); (B) đổi kiểu Normal sang Times New Roman 10 — Excel và ONLYOFFICE tính độ rộng cột theo phông của kiểu Normal, nên phải mở thử trên cả hai để chắc cột không đổi, AI chưa thử được.

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
- Cập nhật: 2026-10-05 · tc_check.py bỏ phần kiểm khoá {{…}} theo FB-035, nên phần "khoá {{…}}" trong Tiêu chí kiểm không còn áp dụng; chuẩn hoá NFC vẫn cần cho phần so từ mơ hồ. Cảnh báo chữ tiếng Việt mới (`--lang en`) đã chuẩn hoá NFC trước khi so.

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

## FB-029 · Chia sheet theo màn hình, vai trò nằm trong sheet
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "tài liệu UC ntn, thì gợi ý giúp tôi, nên theo bố cục các sheet ntn" · "VD: tôi đang có 2 role chính: Customer và SGS trong đó lại có Customer Admin và SGS Admin" · "Tạo Scope từ phía Customer chẳng hạn (ko pải Customer admin...) thì vẫn ở trong 1 sheet: Customer và nó có nhiều phần như Scope còn bên dưới là Certification ..." · "Hay mỗi sheet là 1 Scope  và 1 Certification  > hãy đánh giá và gợi ý cho t tham khảo" · "hãy cho tôi bản docs để t cập nhập vào Rule + Skill trên máy tính này: trên Readme"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#24 · rules/tc-authoring.md#27 · skills/tc-authoring/SKILL.md#đầu-ra · skills/tc-authoring/SKILL.md#bước-4 · skills/tc-authoring/SKILL.md#bước-5 · scripts/tc_check.py
- Tiêu chí kiểm: không sheet nào đặt theo vai trò; Pre-condition của mọi TC mở đầu bằng dòng đăng nhập theo rule 14 ("Logged in as <role>" hoặc "Not logged in" ở file tiếng Anh); khác biệt giữa các vai trò nằm ở nhóm Phân quyền; TC "làm ở vai trò A, kiểm ở vai trò B" nằm ở sheet của hành động
- Phạm vi ảnh hưởng: quét SGS-DTP_TestCase1_v1.3.xlsx bằng script ngày 05/10 — 18/256 TC có Pre-condition không ghi vai trò: Login TC_038, 039, 041, 050; Scopes TC_022, 023, 024, 026, 027, 049, 051, 052, 069, 070, 071, 090, 091, 092
- Liên quan: FB-010 (rule 3 gốc) · FB-035 (cách ghi vai trò bằng chữ, rule 14)
- Đã sửa: chưa sửa sản phẩm; rule 24, 27 và skill v0.3 theo tài liệu cập nhật gộp ngày 05/10
- Cách kiểm: lọc cột Pre-condition, dòng nào cũng mở đầu bằng "Logged in as" hoặc "Not logged in" (file tiếng Việt: "Đăng nhập với acc", "Chưa đăng nhập")
- Gate: mức 1 · đề xuất nâng mức 3: tc_check.py báo Pre-condition không mở đầu bằng dòng đăng nhập của rule 14
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-030 · Gộp, tách sheet theo màn hình, không theo module của UC list
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

## FB-031 · Viết TC bằng tiếng Anh; ít nhất tên nút giữ nguyên tiếng Anh
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
- Cập nhật: 2026-10-05 · Hanna chốt bằng câu hỏi chọn đáp án trong chat. Câu "Chuyển TC sang tiếng Anh khi nào?" chọn "Ngay ở bản tới". Câu "phần nào trong file TC đổi sang tiếng Anh?" chọn "Cả file, trừ câu hỏi": mọi sheet, mọi cột viết tiếng Anh, riêng cột Open question và sheet Cần xác nhận vẫn tiếng Việt; rule, FB, phân tích và chat vẫn tiếng Việt. Câu "Dòng đăng nhập ở Pre-condition ghi bằng tiếng Anh thế nào?" chọn "Logged in as <role>" (ghi ở FB-035). Đây là lựa chọn (1) ở mục Xung đột. Đáp án do AI soạn, Hanna chọn. Trạng thái chuyển từ Chưa rõ phạm vi sang Mới. [Đề xuất của AI, chờ duyệt] ghi ngôn ngữ file TC ở profile.md của từng dự án thay vì ghi cứng trong rule, vì dự án Quản lý tài liệu chưa chốt ngôn ngữ giao diện (Q-02); bảng từ cố định Việt → Anh cho nhóm kiểm ở cột Classification III.
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 1–4 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.

## FB-032 · Trạng thái rỗng đặt trước, theo vòng đời dữ liệu rỗng → tạo → có dữ liệu
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

## FB-033 · Trạng thái rỗng phải tả đủ icon, chữ, nút
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

## FB-034 · Không viết lửng lơ ở Expected và Step; không biết thì đưa vào Q&A
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
- Tái phát: 1
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 7 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.
- Cập nhật: 2026-10-07 · Tái phát 1 tại Scopes!Scope_023, Scope_024 của bản v1.3 (dựng ngày 06/10, sau khi FB này được duyệt ngày 05/10): Expected khẳng định điều chưa có căn cứ ("- Danh sách có abc"), không có câu hỏi. Hanna chỉ ra ở chat Testing 06/10, ghi thành FB-042. Nguyên nhân: rule đúng nhưng gate mới ở mức 1.
- Cập nhật: 2026-10-07 · Sau lần tái phát 1: phần "khẳng định điều chưa có căn cứ" theo dõi ở FB-042. Gate vẫn mức 1 vì chưa có cách kiểm bằng máy; đề xuất ở FB-042 (thêm cột Căn cứ vào bảng phẳng để script đếm được), chờ Hanna quyết.

## FB-035 · Pre-condition đăng nhập ghi bằng vai trò: "Đăng nhập với acc Customer Admin"
- Ngày: 2026-10-05
- Nguồn: chat 05/10 · "Nếu đăng nhập thì ghi: Đăng nhập với acc Customer Admin"
- Loại: L4-mẫu
- Địa chỉ: rules/tc-authoring.md#14 · rules/tc-authoring.md#22 · rules/tc-authoring.md#24 (bản cập nhật v0.3, chờ duyệt) · skills/tc-authoring/SKILL.md (mô tả, đầu-ra, bước-5, bước-7) · references/templates.md#1 · references/format.md#4 · scripts/tc_check.py
- Tiêu chí kiểm: dòng đăng nhập trong Pre-condition ghi tên vai trò bằng chữ, theo ngôn ngữ của file TC: tiếng Anh "Logged in as <role>" (vd "Logged in as Customer Admin"), không cần đăng nhập thì "Not logged in"; tiếng Việt "Đăng nhập với acc <vai trò>", "Chưa đăng nhập"; dữ liệu ghi thẳng giá trị cụ thể, nhãn ghi nguyên văn, không ô nào ở Pre-condition, Step, Expected còn dạng {{...}}; rule và skill tc-authoring không còn khoá, sheet `_Data`, `_Labels`
- Phạm vi ảnh hưởng: 199 TC có Pre-condition dùng khoá {{user.…}} (Login 10, Scopes 115, Users 62, Profile 12); 175 TC dùng khoá dữ liệu khác như {{scope.org}}, {{email.new}}; gộp lại 248/256 TC, 422 ô ở Pre-condition, Step, Expected còn dạng {{…}} (đếm bằng script trên bản v1.3). Rule và skill: rules/tc-authoring.md rule 14, 22 và rule 24 bản v0.3; SKILL.md 4 chỗ; templates.md §1–§3; format.md §4; tc_check.py 6 chỗ
- Xung đột: rule 14 yêu cầu dữ liệu và nhãn viết dạng khoá {{...}}; rule 24 (đang chờ duyệt) ghi vai trò bằng khoá {{user.…}}. Hai lựa chọn: (1) vai trò viết bằng chữ, khoá chỉ dùng cho dữ liệu như email, tên scope — dễ đọc, lọc theo chữ "Customer Admin" vẫn ra danh sách chạy của từng vai trò; (2) bỏ hẳn khoá, ghi giá trị mẫu cụ thể — dễ đọc nhất, nhưng dữ liệu đổi thì phải sửa nhiều chỗ
- Đã sửa: chưa sửa sản phẩm; rule 14, 22, 24 và skill v0.3 theo tài liệu cập nhật gộp ngày 05/10
- Cách kiểm: tìm "{{" ở Pre-condition, Step, Expected của mọi sheet TC → 0 kết quả; tìm "{{", "_Data", "_Labels" trong rules/tc-authoring.md và skills/tc-authoring → chỉ còn ở dòng changelog v0.3; file TC tiếng Anh: Pre-condition dòng nào cũng mở đầu bằng "Logged in as" hoặc "Not logged in"
- Gate: mức 3 · tc_check.py báo lỗi TC còn dạng {{…}} (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp)
- Trạng thái: Đã duyệt
- Tái phát: 1
- Cập nhật: 2026-10-05 · Hanna chọn cách của mình, nguyên văn: "Cái này có xung đột, do 1 phần tôi lấy rule từ dự án dev làm cho FEEC, đứng trên lập trường code của dev, còn hiện tại đang dùng cho Tester, đứng ở 2 góc nhìn khác nhau nên t có thể dùng cái của tôi cho hợp lý nhé". Xung đột đã có lời giải: file TC viết cho Tester, nên Pre-condition ghi vai trò bằng chữ ("Đăng nhập với acc Customer Admin"). Rule 14 (dữ liệu, nhãn viết dạng khoá {{...}}) đến từ góc nhìn của dev, không áp cho file TC của Tester: khi sửa rule thì ghi bãi bỏ trong changelog, không xoá dòng cũ; rule 24 (chờ duyệt) đổi thành ghi vai trò bằng chữ. Trạng thái chuyển từ Chưa rõ phạm vi sang Mới.
- Cập nhật: 2026-10-05 · [Cách hiểu của AI, chờ Hanna xác nhận] Dữ liệu khác (tên scope, email…) cũng bỏ khoá, viết bằng chữ dễ đọc; cần giá trị cụ thể thì ghi ví dụ.
- Cập nhật: 2026-10-05 · Hanna chốt bỏ hẳn, nguyên văn: "tôi cảm thấy toàn bộ các nội dung dưới đây đều ko phù hợp với testing > tôi thấy cần loại bỏ toàn bộ các rule dưới đây". Các nội dung được nhắc: rule 14 (dữ liệu, nhãn viết dạng khoá {{...}}, khai ở `_Data`, `_Labels`); phần khoá trong rule 24 của bản cập nhật v0.3; sheet `_Data`, `_Labels` trong skill và phần kiểm khoá của `tc_check.py`. Thay cho cách làm ở dòng cập nhật thứ nhất: rule 14 không giữ dòng cũ, không ghi bãi bỏ, mà viết lại thành cách viết của Tester (đăng nhập ghi "Đăng nhập với acc <vai trò>", dữ liệu ghi thẳng giá trị cụ thể, nhãn ghi nguyên văn ngay trong ô); rule 22, rule 24 không còn khoá; bỏ `_Data`, `_Labels` và phần kiểm khoá. Dòng cập nhật thứ hai (dữ liệu khác cũng bỏ khoá) không còn là cách hiểu chờ xác nhận, vì rule 14 bỏ hẳn, gồm cả dữ liệu và nhãn. Địa chỉ, Tiêu chí kiểm, Phạm vi ảnh hưởng, Đã sửa, Cách kiểm, Gate sửa theo; Trạng thái chuyển từ Mới sang Đã vào rule (chờ duyệt). Rule, skill sửa trong tài liệu cập nhật gộp ngày 05/10.
- Cập nhật: 2026-10-05 · File TC SGS DTP chuyển sang tiếng Anh (FB-031, cùng ngày). Ở câu hỏi chọn đáp án "Dòng đăng nhập ở Pre-condition ghi bằng tiếng Anh thế nào?", Hanna chọn "Logged in as <role>"; màn không cần đăng nhập ghi "Not logged in". [Đề xuất của AI, chờ duyệt] rule 14 ghi cả hai dạng: tiếng Anh như trên, tiếng Việt "Đăng nhập với acc <vai trò>", "Chưa đăng nhập" cho dự án viết TC bằng tiếng Việt. Tiêu chí kiểm, Cách kiểm sửa theo.
- Cập nhật: 2026-10-05 · Hanna duyệt câu rule đề xuất (mục 2 trong chat 05/10), nguyên văn: "tốt". Trạng thái chuyển sang Đã duyệt. Câu rule chép vào rule, skill bằng tài liệu cập nhật gộp; chưa sửa sản phẩm.
- Cập nhật: 2026-10-07 · Tái phát 1 — bản v1.3 (06/10) còn 422 ô dạng `{{…}}`; Hanna nhắc ở chat Testing 06/10: "thay {{ }} = tên []", và nói rõ thêm ngày 07/10 (ghi ở FB-046). Đếm lại trên v1.4: 293 ô ở 174 TC (Scopes 68 / 49, Login 60 / 50, Users 144 / 62, Profile 21 / 13). Nguyên nhân: sản phẩm chưa được sửa sau khi rule được duyệt, và `tc_check.py` chưa báo ô còn `{{`.
- Cập nhật: 2026-10-07 · Nâng gate từ mức 1 lên mức 3 sau lần tái phát 1: `tc_check.py` bản 07/10 báo lỗi khi ô của TC còn `{{…}}`. Sheet Scopes bản v1.5 đã về 0 ô; Login, Users, Profile còn 225 ô ở 125 TC (xem FB-046).

## FB-036 · Nhiều mục thì mỗi mục một dòng, không nối bằng " · "
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

## FB-037 · Giá trị tính toán phải nói lấy từ đâu; TC phải dễ sửa khi Figma, UC đổi
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

## FB-038 · Gửi bản xem trước danh sách tính năng trước khi cập nhật file TC
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

## FB-039 · TC gọi API chỉ viết khi tester được gọi API, và để ở sheet API riêng
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

## FB-040 · Pre-condition không ghi mở màn hình đang test; liệt kê thao tác khi phải qua màn khác
- Ngày: 2026-10-06
- Nguồn: chat Building 06/10, góp ý của Hanna trên `SGS-DTP_TestCase1_v1.2.xlsx` · "Vấn đề 1: Viết Pre-condition. Trên task test cho màn hình Scopes > thì test chỉ tập trung test trên màn hình đó. VD: Pre condition là Đăng nhập account. Steps: Mở màn hình Scopes. Nếu từ màn hình A pải làm nhiều thao tác data thì mới ra màn hình B thì Pre condition mới là A: làm thao tác ... (liệt kê ra) còn Step vẫn là mở màn hình B xong làm thao tác gì tiếp theo"
- Loại: L2-rule
- Liên quan: tái phát một phần của FB-035 (cách ghi dòng đăng nhập ở Pre-condition) và FB-036 (mỗi mục một dòng)
- Địa chỉ: rules/tc-authoring.md#14 · skills/tc-authoring/scripts/tc_check.py (OPEN_SCREEN) · skills/test-design/references/coverage-checklist.md#E
- Tiêu chí kiểm: không còn Pre-condition ghi "mở màn …" / "open … screen"; mọi TC có Step 1 là mở màn đang test (hoặc thao tác đầu trên màn đó); Pre-condition qua màn khác thì liệt kê từng thao tác kèm giá trị cụ thể
- Phạm vi ảnh hưởng: file v1.2 — Pre-condition ghi "Đăng nhập account , mở màn Scopes" ở 95 TC của sheet Scopes (gồm cả dạng "mở chi tiết {{…}}"), 35 TC của Login và 17 TC của Users; Profile không bị
- Đã sửa: rule 14 (hai gạch đầu dòng mới) và `tc_check.py` cảnh báo khi Pre-condition ghi mở màn hình; file TC đã sửa theo: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.3.xlsx` (180 dòng đổi Pre-condition/Step, bảng so sánh ở `tests/design/so-sanh_v1.2-v1.3.md`)
- Cách kiểm: `tc_check.py` không còn cảnh báo "Pre-condition ghi mở màn hình"
- Gate: mức 2 · cảnh báo bằng script (chưa chặn)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 1
- Cập nhật: 2026-10-06 · Hanna chỉ ra ngày 06/10; câu gốc của FB-035 chỉ nói dòng đăng nhập, chưa nói về dòng mở màn hình.

## FB-041 · Thiếu case kiểm hiển thị từng thông tin sau khi tạo
- Ngày: 2026-10-06
- Nguồn: chat Building 06/10, góp ý của Hanna trên `SGS-DTP_TestCase1_v1.2.xlsx` · "Vấn đề 2: Thiếu các case kiểm tra hiển thị. Trên Tạo Scopes > sau khi tạo thành công thì từng thông tin hiển thị đúng ntn cho 1 TCs, mô tả cho cả 4 thông tin dưới đây. VD: Step: khi chọn Type là: Organization, Name: abc, What is in scope: abc, What is out of scope (optional): abc. Click button: Create scope > tạo thành công > Kiểm tra thông tin hiển thị trên Danh sách. Expect: Hiển thị các thông tin tương ứng: Type là: Organization, Name: abc, What is in scope: abc, What is out of scope (optional): abc"
- Loại: L3-checklist
- Liên quan: pattern P7 (thông tin bản ghi sau khi tạo) chỉ nêu chung; FB-037
- Địa chỉ: rules/tc-authoring.md#30 · skills/tc-authoring/references/patterns.md#P1,P7 · skills/test-design/references/coverage-checklist.md#E
- Tiêu chí kiểm: mỗi Type (Organization, Product, System) có TC nhập đủ 4 thông tin (kèm Belongs to với System), tạo xong kiểm từng thông tin ở danh sách và ở màn chi tiết; Expected liệt kê từng giá trị
- Phạm vi ảnh hưởng: sheet Scopes v1.2 có Scope_021, Scope_025 (scope mới hiện ở danh sách), Scope_022, Scope_026 (chi tiết) nhưng chỉ kiểm tên/có hiện, nhập thiếu trường (Out of scope để trống), không có TC cho loại Product; các màn có thao tác tạo khác (Users, Framework gắn…) cần rà
- Đã sửa: rule 30; pattern P1, P7; coverage-checklist; file v1.3: viết lại Scope_021, 022, 025, 026 kiểm đủ Type, Name, In scope, Out of scope; thêm Scope_130–132 (Organization để trống Out of scope, Product ở danh sách, Product ở chi tiết); câu hỏi mới Q-S-28 (danh sách có hiển thị In/Out of scope không)
- Cách kiểm: mỗi loại Type có TC hiển thị ở danh sách và chi tiết
- Gate: mức 1 · văn xuôi (chưa có script kiểm)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-06 · Việc nhập "đủ 4 thông tin trong một TC" trái với rule 6 của Tester (một TC một mục tiêu) nhưng Hanna nói rõ muốn vậy cho case hiển thị; mục tiêu của TC là "thông tin hiển thị đúng sau khi tạo", nên vẫn là một mục tiêu.

## FB-042 · Thông tin chưa kiểm chứng không được viết vào TC dạng khẳng định
- Ngày: 2026-10-06
- Nguồn: chat Testing 06/10, góp ý của Hanna trên `SGS-DTP_TestCase1_v1.3.xlsx`, sheet Scopes, kèm ảnh khoanh đỏ Scope_023 "Organization — hiện ở Belongs to organisation" (Expected: "- Danh sách có abc") · "thông tin này chưa đc kiểm chứng > ko dc cho vào TCs dạng khẳng định ntn"
- Loại: L2-rule
- Liên quan: FB-034 (tái phát, xem dòng Cập nhật 07/10 ở đó) · rule 13 · `common.md` rule 1
- Địa chỉ: rules/tc-authoring.md#13 · rules/tc-authoring.md#9 · skills/tc-authoring/SKILL.md#bước-4 · sản phẩm: Scopes!Scope_023, Scope_024 (v1.3)
- Tiêu chí kiểm: mọi Expected có nội dung đều chỉ ra được căn cứ ở UC hoặc Figma; kết quả do AI suy ra (vd dữ liệu vừa tạo sẽ hiện ở một danh sách chọn, ở một màn khác) thì để trống Expected và ghi câu hỏi ở cột Open question, hoặc bỏ TC nếu không cần
- Phạm vi ảnh hưởng: quét `SGS-DTP_TestCase1_v1.4.xlsx` bằng script ngày 07/10, tiêu chí "nhóm Thành công, ô IV nêu nơi hiển thị, Expected có nội dung, Open question trống" — Scopes 9 TC (Scope_069, 070, 071, 072, 091, 108, 109, 110, 111 theo số của v1.4); Users 6 TC; Login 0; Profile 0. Ở v1.4 Hanna đã tự bỏ Scope_023, 024, 026, 027 của v1.3. Script chỉ lọc theo tên case; căn cứ của từng TC phải rà tay
- Đã sửa: sản phẩm: sheet Scopes bản v1.5 (`projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.5.xlsx`) — bỏ 5 case hệ quả suy ra hoặc lặp nơi hiển thị (so-sanh mục 3); trong 9 TC đã quét, 4 TC bị bỏ (Scope_071, 072, 091, 109 theo số v1.4), 5 TC còn lại là kết quả ở nơi hành động trả về hoặc hệ quả theo UC (Scope_081, 082, 121, 122, 123 theo số v1.5). Rule: `rules/tc-authoring.md` v0.5 rule 13 thêm ý "kết quả suy ra cũng là chưa có căn cứ"; SKILL Bước 4 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md` (chờ áp). Users: 6 TC chưa rà
- Cách kiểm: đọc lại từng TC nhóm Thành công có ô IV nêu nơi hiển thị: Expected phải chỉ ra được căn cứ ở UC hoặc Figma, hoặc có câu hỏi ở cột Open question; `projects/sgs-dtp/tests/design/so-sanh_v1.4-v1.5.md` mục 3 liệt kê case đã bỏ
- Gate: mức 1 · rule 13 và SKILL Bước 4 (văn xuôi). Đề xuất mức 3: thêm cột Căn cứ vào bảng phẳng (UC / Figma / hệ thống đang chạy), script báo dòng có Expected mà không có căn cứ — chờ Hanna quyết
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-07 · Nhận xét ngày 06/10 không được ghi ngay: phiên chat Testing bị ngắt trước khi ghi sổ. Ghi lại ngày 07/10, trước khi sửa file.
- Cập nhật: 2026-10-07 · Đã sửa sheet Scopes ở bản v1.5 và đưa vào rule 13 (v0.5, chờ duyệt). Chưa có cách kiểm bằng máy: script chỉ lọc được theo tên case. Câu hỏi còn mở với Hanna: ở bản v1.4, 8 case được điền Expected theo hệ thống đang chạy và vẫn giữ câu hỏi (Scope_005, 007, 017, 020, 024, 054, 057, 059 theo số v1.5), trong khi rule 1 và rule 13 ghi không lấy hành vi của hệ thống đang chạy làm Expected — AI giữ nguyên các ô đó và chưa điền thêm kiểu này ở phần dưới.

## FB-043 · Nhóm Thành công của chức năng tạo: mỗi loại một case, bỏ case không cần thiết
- Ngày: 2026-10-06
- Nguồn: chat Testing 06/10, góp ý của Hanna trên `SGS-DTP_TestCase1_v1.3.xlsx`, sheet Scopes, khu vực Tạo scope · "nên bỏ bớt case ko cần thiết > Nên cho 3 case Type theo 3 loại: Organization/Product/System"
- Loại: L3-checklist
- Liên quan: sửa lại FB-041 (rule 30, chờ duyệt) · rule 9 · pattern P1, P7
- Địa chỉ: rules/tc-authoring.md#30 · skills/tc-authoring/references/patterns.md#P1,P7 · skills/test-design/references/coverage-checklist.md#E · sản phẩm: Scopes, Tạo scope ▸ Thành công
- Tiêu chí kiểm: nhóm Thành công của một chức năng tạo có đúng một TC cho mỗi loại (Scopes: Organization, Product, System); TC nhập đủ mọi trường và kiểm thông tin ở nơi hành động trả về (danh sách); không có TC lặp lại cùng một loại chỉ để kiểm ở nơi hiển thị khác
- Phạm vi ảnh hưởng: v1.3 — Tạo scope ▸ Thành công có 10 TC cho 3 loại (Scope_021 → 027, 130 → 132); ở v1.4 Hanna đã tự sửa còn 3 TC. Quét v1.4 bằng script, nhóm Thành công có ô IV nêu nơi hiển thị: Scopes 17 / 20 TC (Tạo scope 3, Sửa scope 4, Gắn framework 4, Gán người dùng 6); Users 9 / 20 TC; Login 0 / 4; Profile không có nhóm Thành công
- Xung đột: rule 30 (FB-041, chờ duyệt) ghi "mỗi loại một TC, mỗi nơi hiển thị một TC"; rule 9 ghi "một hành động hiện ở n nơi thì viết n case riêng"; pattern P7 ghi "danh sách và màn chi tiết là hai TC riêng". Góp ý này giữ phần "mỗi loại một TC" và bỏ phần nhân theo nơi hiển thị
- Đã sửa: sản phẩm: sheet Scopes bản v1.5 — nhóm Thành công đặt theo loại ở Gắn framework (Scope_105 có tier, Scope_106 không phân tier); khối Overview, cột Tier mỗi loại một case; không còn case lặp cùng một loại cho nơi hiển thị khác trong sheet. Rule: `rules/tc-authoring.md` v0.5 rule 9 và rule 30 ("mỗi loại đúng một TC", bỏ "mỗi nơi hiển thị một TC"); patterns P1, P7 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md` (chờ áp). Users: 9 TC chưa rà
- Cách kiểm: đếm ở bảng phẳng `projects/sgs-dtp/exports/_flat/Scopes_v1.5.tsv`: mỗi khu vực có hành động tạo, nhóm Thành công có đúng một TC cho mỗi loại; `projects/sgs-dtp/tests/design/so-sanh_v1.4-v1.5.md` mục 4
- Gate: mức 2 · references/patterns.md P1, P7 (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) và rule 30
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-07 · Ghi lại ngày 07/10 (phiên 06/10 bị ngắt trước khi ghi sổ).
- Cập nhật: 2026-10-07 · Đã sửa sheet Scopes và rule 9, 30 (v0.5, chờ duyệt). Phần xung đột với rule 27: case hệ quả ở màn khác (Workspaces: Scope_107; chi tiết người dùng: Scope_123) AI giữ ở sheet Scopes theo rule 27, chờ Hanna cho biết có chuyển sang sheet của màn đó không.

## FB-044 · Hiển thị ở màn chi tiết kiểm ở khu vực Chi tiết, không lặp ở khu vực Tạo mới
- Ngày: 2026-10-06
- Nguồn: chat Testing 06/10, góp ý của Hanna trên `SGS-DTP_TestCase1_v1.3.xlsx`, sheet Scopes, case "Organization — hiện ở màn chi tiết" · "hiện ở màn chi tiết > phần này để ở màn hình Chi tiết scope rồi > bỏ ở chỗ Tạo mới scope nhé"
- Loại: L2-rule
- Liên quan: FB-043 · FB-041 · rule 27 (chờ duyệt)
- Địa chỉ: rules/tc-authoring.md#9 · rules/tc-authoring.md#30 · skills/tc-authoring/SKILL.md#bước-4 · sản phẩm: Scopes (Tạo scope, Sửa scope, Gắn framework, Gán người dùng)
- Tiêu chí kiểm: thông tin hiển thị ở một màn hay một khu vực được kiểm ở khu vực của chính nơi đó; nhóm Thành công của hành động chỉ kiểm nơi hành động trả về; không TC nào ở khu vực của hành động lặp lại điều đã có TC ở khu vực hiển thị
- Phạm vi ảnh hưởng: v1.3 — Scope_022, 026, 130, 132 kiểm màn chi tiết ngay trong khu vực Tạo scope (Hanna đã bỏ ở v1.4). v1.4 còn 4 TC cùng kiểu, số theo v1.4: Scope_091 (Gắn framework ▸ Hiện ở danh sách Scopes, trùng Scope_043 "Cột Frameworks — đã gắn"); Scope_093 (Hiện ở khối Summary, trùng Scope_115); Scope_109 (Tick thêm — cột Users ở danh sách, trùng Scope_045); Scope_111 (Tick thêm — chi tiết người dùng, trùng Users!TC_007 và TC_038). Users: 9 TC nhóm Thành công nêu nơi hiển thị, chưa rà
- Xung đột: rule 27 (chờ duyệt) đặt TC điểm hiển thị ở sheet của hành động; góp ý này nói về khu vực trong cùng một sheet: nơi hiển thị nào đã có khu vực riêng thì kiểm ở khu vực đó
- Đã sửa: sản phẩm: sheet Scopes bản v1.5 — bỏ 3 trong 4 TC đã quét (Scope_091, 093, 109 theo số v1.4: framework vừa gắn ở danh sách Scopes, ở Summary; cột Users sau khi gán) và 2 TC tên mới ở Overview của scope con, ở cột Belongs to; TC thứ tư (Scope_111 của v1.4, chi tiết người dùng) là màn khác nên giữ, nay là Scope_123. Rule: `rules/tc-authoring.md` v0.5 rule 9 viết lại; SKILL Bước 4 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md` (chờ áp)
- Cách kiểm: `projects/sgs-dtp/tests/design/so-sanh_v1.4-v1.5.md` mục 3 (case bỏ) và mục 4; đọc nhóm Thành công của Sửa scope, Gắn framework, Gán người dùng: chỉ còn kết quả ở nơi hành động trả về và hệ quả ở màn khác
- Gate: mức 1 · rule 9 và SKILL Bước 4 (văn xuôi)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-07 · Ghi lại ngày 07/10 (phiên 06/10 bị ngắt trước khi ghi sổ).
- Cập nhật: 2026-10-07 · Đã sửa sheet Scopes và rule 9 (v0.5, chờ duyệt).

## FB-045 · Case kiểm tra dữ liệu có bước bấm nút gửi mà không lưu thì gộp vào nhóm Không thành công
- Ngày: 2026-10-06
- Nguồn: chat Testing 06/10, trên `SGS-DTP_TestCase1_v1.3.xlsx` · "Vì các step của Kiểm tra dữ liệu đều phải click vào button Create scope => Nên gộp cùng các case ko thành công" · chat Testing 07/10, trên `SGS-DTP_TestCase1_v1.4.xlsx` · "Kiểm tra với trường hợp bỏ trống trường bắt buộc thì ko cho phép lưu. Về bản chất cùng step click vào Create scope/ Save và không lưu thành công thì cho hết vào cùng case Không thành công: ID 21 > 33"
- Loại: L2-rule
- Địa chỉ: rules/tc-authoring.md#8 · skills/tc-authoring/SKILL.md#bước-5 · skills/tc-authoring/references/format.md#7 · sản phẩm: Scopes (Sửa scope, Gắn framework), Login (Email, Mật khẩu)
- Tiêu chí kiểm: case có bước cuối là bấm nút gửi (Create scope, Save, Link and create workspace, Sign in…) mà kết quả là không lưu thì nằm trong nhóm Không thành công của khu vực, cùng các case Cancel, ×, Esc; không còn nhóm Kiểm tra dữ liệu riêng cho các case đó
- Phạm vi ảnh hưởng: quét v1.4 theo ô III = "Kiểm tra dữ liệu" — Scopes 5 TC (Sửa scope 3, Gắn framework 2); Login 4 TC (Email 2, Mật khẩu 2); Users 0; Profile 0. Khu vực Tạo scope: Hanna đã tự gộp ở v1.4 (10 TC Không thành công, No 27 → 33)
- Xung đột: SKILL Bước 5 xếp "kiểm tra dữ liệu → thành công → không thành công" thành ba nhóm; `references/format.md` §7 có tên nhóm "Kiểm tra dữ liệu / Validation"; rule 8 ghi "Thành công hết rồi mới tới Không thành công", còn ở v1.4 Hanna xếp Không thành công trước Thành công
- Đã sửa: sản phẩm: sheet Scopes bản v1.5 — 5 TC Kiểm tra dữ liệu chuyển vào Không thành công (Sửa scope: Scope_076 → 078; Gắn framework: Scope_101, 102); cả sheet không còn nhóm Kiểm tra dữ liệu; nhóm Không thành công đứng trước Thành công ở Sửa scope, Gắn framework, Đổi tier, Gán người dùng như Hanna làm ở Tạo scope. Login: 4 TC chưa sửa. Rule: `rules/tc-authoring.md` v0.5 rule 8; SKILL Bước 5 và format.md §7 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md` (chờ áp)
- Cách kiểm: `python .claude/skills/tc-authoring/scripts/tc_check.py <file>.xlsx` (bản 07/10) → không có cảnh báo "còn nhóm Kiểm tra dữ liệu"; trên bản v1.5 còn 2 cảnh báo, đều ở sheet Login (Email, Mật khẩu)
- Gate: mức 3 · tc_check.py cảnh báo khu vực còn nhóm Kiểm tra dữ liệu (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-07 · Hanna nhắc lại ngày 07/10 vì nhận xét ngày 06/10 chưa được xử lý (phiên bị ngắt), nên không tính là tái phát.
- Cập nhật: 2026-10-07 · Đã sửa sheet Scopes và rule 8 (v0.5, chờ duyệt). Còn chờ Hanna chọn thứ tự hai nhóm: câu cũ của rule 8 ghi Thành công trước, bản v1.4 xếp Không thành công trước; bản v1.5 và rule v0.5 đang theo bản v1.4.

## FB-046 · Bỏ {{…}}; dữ liệu chưa xác định viết chung chung trong ngoặc vuông [tên]
- Ngày: 2026-10-06
- Nguồn: chat Testing 06/10, kèm ảnh ô Expected của Scope_006 có `{{tenant.short}}` · "thay {{ }} = tên []" · chat Testing 07/10 · "Với dự án hoặc hệ thống chưa xác định rõ ràng hiển thị ntn về đầu vào dữ liệu, nên chỉ cần viết chung chung trong step và expect là hiển thị kiểu trong ngoặc vuông [data]" · "- Belongs to organisation: [Organization]" · "- Belongs to product (optional): [Product]"
- Loại: L4-mẫu
- Liên quan: FB-035 (tái phát, xem dòng Cập nhật 07/10 ở đó) · rule 14
- Địa chỉ: rules/tc-authoring.md#14 · skills/tc-authoring/scripts/tc_check.py · sản phẩm: mọi sheet TC
- Tiêu chí kiểm: không ô nào của sheet TC còn `{{`; dữ liệu đã xác định ghi giá trị cụ thể (vd Name: abc); dữ liệu mà dự án, hệ thống chưa xác định thì viết chung chung, tên đặt trong ngoặc vuông, vd `[Organization]`, `[Product]`
- Phạm vi ảnh hưởng: đếm bằng script trên v1.4 — Scopes 68 ô / 49 TC; Login 60 ô / 50 TC; Users 144 ô / 62 TC; Profile 21 ô / 13 TC
- Xung đột: rule 14 (FB-035, Đã duyệt) ghi "Dữ liệu ghi thẳng giá trị cụ thể"; góp ý này thêm trường hợp dữ liệu chưa xác định thì viết `[tên]`
- Đã sửa: sản phẩm: sheet Scopes bản v1.5 — 68 ô còn `{{…}}` về 0; dữ liệu tester nhập ghi giá trị cụ thể (abc, abc1), dữ liệu có sẵn chưa xác định ghi `[tên]`; bảng tên ngoặc vuông ở `projects/sgs-dtp/tests/design/phan-tich-cach-viet_v1.4.md` mục 4. Login 60 ô, Users 144 ô, Profile 21 ô chưa sửa. Rule: `rules/tc-authoring.md` v0.5 rule 14
- Cách kiểm: `python .claude/skills/tc-authoring/scripts/tc_check.py <file>.xlsx` (bản 07/10) → không có lỗi "còn dạng {{…}}"; trên bản v1.5 còn 3 lỗi: Login 50 TC, Users 62 TC, Profile 13 TC
- Gate: mức 3 · tc_check.py báo lỗi TC còn dạng {{…}} (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-07 · Đã sửa sheet Scopes và rule 14 (v0.5, chờ duyệt). AI hiểu ranh giới như sau, chờ Hanna xác nhận: dữ liệu tester tự gõ thì ghi giá trị cụ thể; dữ liệu phải có sẵn trên hệ thống mà chưa xác định thì ghi `[tên]`. Chờ Hanna cho biết có viết lại Login, Users, Profile theo cách này không.

## FB-047 · Học cách viết của Hanna ở TC 1–67 sheet Scopes (v1.4) để viết phần còn lại
- Ngày: 2026-10-07
- Nguồn: chat Testing 07/10, kèm file `SGS-DTP_TestCase1_v1.4.xlsx` · "Test case từ 1 đến 67 trong phần Danh sách scope tôi đã chỉnh sửa lại > b hãy xem và phân tích cách làm nhé, bên dưới thì b tự sửa"
- Loại: L6-tri thức
- Liên quan: FB-042 → FB-046 · FB-048 · FB-049
- Địa chỉ: projects/sgs-dtp/tests/design/phan-tich-cach-viet_v1.4.md · projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.5.xlsx (Scopes, từ Chi tiết scope trở xuống)
- Tiêu chí kiểm: có file phân tích nêu từng điểm trong cách viết của Hanna kèm ô dẫn chứng; phần Chi tiết scope, Phân quyền, Bảo mật của sheet Scopes viết theo các điểm đó; bảng so sánh v1.4 → v1.5 ghi từng TC là giữ, sửa, bỏ hay thêm
- Đã sửa: `projects/sgs-dtp/tests/design/phan-tich-cach-viet_v1.4.md` (8 điểm trong cách viết, dẫn chứng trước → sau, 7 chỗ khác rule đang có); `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.5.xlsx` — phần Hanna sửa (dòng 13–69 của v1.4) giữ nguyên trừ 14 ô gõ nhầm hoặc còn `{{…}}` ở 10 TC và 9 ô UC trống, phần dưới viết lại: giữ 2, sửa 68, thêm 6, bỏ 9 TC; `projects/sgs-dtp/tests/design/so-sanh_v1.4-v1.5.md`
- Cách kiểm: mở `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.5.xlsx` đối chiếu với `phan-tich-cach-viet_v1.4.md` mục 1; `tc_check.py` (bản 05/10) trên bản v1.5: 0 lỗi
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0
- Cập nhật: 2026-10-07 · Đã giao bản v1.5 và hai tài liệu. Phần cách viết thành rule nằm ở FB-042 → FB-046, FB-048, FB-049.

## FB-048 · Cột Evidence coverage cần nhiều TC hơn để xác định hiển thị thế nào là đúng
- Ngày: 2026-10-07
- Nguồn: chat Testing 07/10, trên `SGS-DTP_TestCase1_v1.4.xlsx` · "Cột Evidence coverage: cần có nhiều TCs hơn để phân tích hiển thị ntn là đúng"
- Loại: L3-checklist
- Liên quan: FB-037 (Bị bác 05/10) · Q-S-11 · quyết định ngày 05/10 trong `projects/sgs-dtp/profile.md`
- Địa chỉ: skills/test-design/references/coverage-checklist.md · rules/tc-authoring.md (rule mới về giá trị tính toán) · sản phẩm: Scopes ▸ Bảng danh sách ▸ Cột Evidence coverage; Khối Frameworks ▸ Cột Coverage
- Tiêu chí kiểm: mỗi giá trị tính toán hiển thị trên màn (tỉ lệ, tổng, số đếm) có các TC với bộ số cụ thể: nhiều thành phần, một thành phần, 0%, 100%, kết quả phải làm tròn lên, kết quả phải làm tròn xuống; biên chưa có căn cứ (đúng .5, dưới 1%, trên 99%, chưa có thành phần nào) có TC để trống Expected kèm câu hỏi
- Phạm vi ảnh hưởng: v1.3 có 1 TC cho cột Evidence coverage (Scope_044, Expected trống); ở v1.4 Hanna viết 6 TC. Giá trị tính toán khác ở sheet Scopes, số theo v1.4: cột Users (Scope_045), cột Coverage ở khối Frameworks (Scope_079, Expected trống), khối Summary (Scope_115, Expected trống), dòng đếm "<n> scopes" (Scope_031). Login, Users, Profile: chưa rà
- Xung đột: ngày 05/10 Hanna bác FB-037 và `profile.md` ghi "Giá trị tính toán (vd cột Users, Evidence coverage) không ghi cách tính trong TC; Expected theo Figma và UC, chưa có thì để trống và ghi câu hỏi". Ở v1.4, Expected của 6 TC do Hanna viết ghi cả phép tính, vd "(74+6+0)/(116+31+78) × 100 = 35.56% → 36%"; công thức lấy theo prototype, Q-S-11 chưa có trả lời. Lựa chọn A: theo v1.4, ghi phép tính và kết quả, mỗi TC kèm câu hỏi Q-S-11 cho tới khi công thức được xác nhận. Lựa chọn B: giữ quyết định 05/10, Expected để trống cho tới khi Figma hoặc UC nêu công thức
- Đã sửa: sản phẩm (tạm theo lựa chọn A): sheet Scopes bản v1.5 — giữ 6 TC Evidence coverage của Hanna (sửa một chỗ cộng nhầm ở Scope_047: 0/101 thành 0/147); thêm 4 TC biên để trống Expected kèm câu hỏi (Scope_050 → 053: chưa gắn framework, phần thập phân đúng bằng .5, trên 0% dưới 0.5%, từ 99.5% đến dưới 100%); cột Coverage ở khối Frameworks từ 1 TC để trống thành 4 TC có số cụ thể (Scope_089 → 092), kèm câu hỏi Q-S-11. Khối Summary giữ 1 TC để trống. Rule: `rules/tc-authoring.md` v0.5 rule 31 (ghi rõ chờ Hanna chọn)
- Cách kiểm: đếm ở `projects/sgs-dtp/exports/_flat/Scopes_v1.5.tsv`: cột Evidence coverage 10 TC, cột Coverage 4 TC; TC nào dùng công thức chưa được SGS xác nhận thì có câu hỏi Q-S-11 ở cột Open question — hiện 5 TC của Hanna (Scope_044 → 048) chưa có
- Gate: mức 2 · references/patterns.md P12, mục cột giá trị tính toán (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp)
- Trạng thái: Chưa rõ phạm vi
- Tái phát: 0
- Cập nhật: 2026-10-07 · Chuyển sang Chưa rõ phạm vi vì còn xung đột chờ Hanna chọn A hoặc B (xem trường Xung đột). Trong lúc chờ, bản v1.5 theo cách của bản v1.4.

## FB-049 · Ô bắt đầu bằng dấu gạch phải có dấu nháy đơn để không thành công thức
- Ngày: 2026-10-07
- Nguồn: chat Testing 07/10, trên `SGS-DTP_TestCase1_v1.4.xlsx` · "Nếu bắt đầu trong ô là: - Hai số bằng nhau > thì cần thêm dấu: '- Hai số bằng nhau => để không bị thành câu lệnh trong excel"
- Loại: L5-script
- Địa chỉ: skills/tc-authoring/scripts/tc_build_xlsx.py · skills/tc-authoring/scripts/tc_check.py · skills/tc-authoring/references/format.md#4 · rules/tc-authoring.md#F
- Tiêu chí kiểm: mọi ô văn bản bắt đầu bằng `-`, `+`, `=` hoặc `@`, ở mọi sheet, đều có dấu nháy đơn ở đầu (thuộc tính quotePrefix của kiểu ô), để khi sửa ô trong Excel hay ONLYOFFICE nội dung không bị hiểu là công thức
- Phạm vi ảnh hưởng: đếm bằng script trên v1.4 — 218 ô, đều ở cột Expected result: Scopes 123, Users 50, Login 34, Profile 11; mới có 36 ô có dấu nháy, là 36 ô Hanna tự thêm khi sửa ở sheet Scopes. Ô Scopes!K13 đã từng bị đọc thành công thức (`docs/VIEC-CON-MO.md`, bản v1.3), khi đó chỉ sửa một ô
- Đã sửa: sản phẩm: bản v1.5 — 216 ô có quotePrefix (Login 34, Scopes 121, Users 50, Profile 11). Script mới `tc_fix_xlsx.py` (trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) gắn dấu nháy cho file có sẵn; `rules/tc-authoring.md` v0.5 rule 32; format.md §4
- Cách kiểm: `python .claude/skills/tc-authoring/scripts/tc_fix_xlsx.py <file>.xlsx --check` → "Sạch"; AI đã chạy trên bản v1.5: sạch; trên bản v1.4: 182 ô thiếu
- Gate: mức 3 · tc_fix_xlsx.py --check và tc_check.py báo ô thiếu dấu nháy đơn (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp)
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-07 · Đã sửa cả 4 sheet TC ở bản v1.5 và đưa vào rule 32 (v0.5, chờ duyệt). Ô Expected của case khối Users từng hỏng thành "- F106" từ bản v1.3 (nay là Scope_115) đã đặt lại 3 cột User, Role, Given. AI chỉ kiểm được bằng LibreOffice; chưa mở thử trên Excel thật.

## FB-050 · Hanna sửa trực tiếp bản v1.5: điền Expected, bỏ và sắp xếp lại case
- Ngày: 2026-10-07
- Nguồn: chat Testing 07/10 lúc 13:28, kèm file `SGS-DTP_TestCase1_v1.5.xlsx` Hanna đã sửa (lưu bằng ONLYOFFICE) · "đã sửa lại 1 số case, bỏ và sắp xếp lại case"
- Loại: L6-tri thức
- Liên quan: FB-047 (cách viết ở bản v1.4) · FB-048 · FB-042 · FB-051 · Q-S-07, Q-S-11, Q-S-13, Q-S-16, Q-S-17, Q-S-19, Q-S-21, Q-S-22
- Địa chỉ: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx` (file Hanna gửi, lưu nguyên) · `projects/sgs-dtp/tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md` · bản file TC kế tiếp
- Tiêu chí kiểm: bản file TC kế tiếp giữ mọi chỗ Hanna sửa ở file gửi lúc 13:28 (17 TC đổi chữ, 1 TC bỏ, 1 TC chuyển nhóm); có bảng so sánh nêu từng ô trước → sau; chỗ AI thấy cần Hanna xem lại được nêu riêng, AI không tự sửa nội dung
- Phạm vi ảnh hưởng: so từng ô bằng script với bản v1.5 AI giao. Sheet Scopes còn 136 TC (v1.5: 137). Đổi chữ ở 17 TC: điền Expected cho 11 TC đang để trống (Scope_031, 050, 051, 052, 053, 084, 098, 100, 104, 114, 126), 10 TC trong đó vẫn giữ câu hỏi ở cột Open question; đổi 6 tên case từ tiếng Anh sang tiếng Việt (Scope_044 → 049). Bỏ 1 TC: Scope_108 (Gỡ framework — Expected trống, không có lối vào trên Figma lẫn prototype). Chuyển Scope_104 (gắn thêm framework khi scope đang có audit) từ nhóm Không thành công sang Thành công, bỏ câu hỏi Q-S-16 của TC đó. TVP_ID giữ nguyên, cột No. đánh lại 1 → 136. Sau khi sửa, sheet Scopes còn 4 TC để trống Expected: Scope_021, 119, 131, 137. Login, Users, Profile, Cover, Cần xác nhận: không đổi nội dung
- Đã sửa: chưa dựng bản mới. Đã lưu nguyên file Hanna gửi vào `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx` và viết `projects/sgs-dtp/tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md`
- Cách kiểm: `python projects/sgs-dtp/exports/_build/v1.5/compare_edit.py <file Hanna gửi> <bản kế tiếp> Scopes` — nội dung Hanna sửa không đổi, trừ các ô được liệt kê là AI chạm vào ở bảng so sánh của bản đó
- Trạng thái: Mới
- Tái phát: 0
- Cập nhật: 2026-10-07 · Điều AI hiểu từ các chỗ sửa, chờ Hanna xác nhận, chưa đưa vào rule: (1) chỗ chưa có căn cứ ở UC, Figma thì Hanna điền Expected theo hệ thống đang chạy và giữ câu hỏi — đây là lần thứ hai (bản v1.4: 8 TC; bản này: 10 TC), trái `rules/tc-authoring.md` rule 1 và rule 13; (2) giá trị tính toán: Hanna ghi phép tính và kết quả cho cả case biên (12.5% → 13%, 0.4% → 0%, 99.6% → 100%), tức lựa chọn A của FB-048; (3) tên case viết tiếng Việt, trong khi `projects/sgs-dtp/profile.md` ghi file TC viết tiếng Anh; (4) case không chạy được và không có Expected (Scope_108) thì bỏ khỏi file TC.
- Cập nhật: 2026-10-07 · Lỗi phát sinh trong file sau khi sửa (do AI kiểm ra, không phải góp ý): sheet Test_Report có 54 ô #REF! ở ba dòng — dòng Gỡ framework, dòng Total của Scopes và dòng Total cuối — vì dòng duy nhất của khu vực Gỡ framework bị xoá; 18 ô ở sheet Scopes về phông Arial (ghi ở FB-016); 7 ô có chữ dạng tổ hợp; Scope_104 trống ô UC, ô Open question của TC này đã hết câu hỏi mà còn nền hồng; 33 ô nền trắng và 24 ô nền vàng (3 dòng Hanna đánh dấu) nằm ngoài bảng màu của file. Chỗ nội dung cần Hanna xem lại ghi ở `projects/sgs-dtp/tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 3: Expected của Scope_114 (Hạ tier) giống hệt Scope_113 (Nâng tier) và nhắc "bước 5" trong khi case có 4 bước; Expected của Scope_100 nói về nút Change tier trong khi Step dừng ở hộp thoại Link a framework.
- Cập nhật: 2026-10-07 19:55 · Hanna gửi thêm một file `SGS-DTP_TestCase1_v1.5.xlsx` (lưu 14:54, md5 9462dcc1…), kèm lời "thôi bỏ qua, chúng ta chuyển qua UC…" — AI hiểu là hoãn các câu hỏi đang chờ (FB-048, FB-050, FB-051), không trả lời. So với bản 13:28 theo tên case (ID đã đánh lại 001 → 140 vì khoảng trống Scope_108 được lấp): 4 dòng mới trống tên, trống Step, nằm ở nhóm Gán người dùng ▸ Mở hộp thoại (Scope_118 → 121); Scope_122 (cũ Scope_119, "Kiểm tra những vai trò có trong danh sách gán") được điền Expected "Customer Admin được mặc định Assign trong Scope"; Scope_134 (cũ Scope_131, Customer Viewer) viết lại Step thành 3 bước (gán 1 scope cho Customer Viewer → đăng nhập Customer Viewer đó → mở chi tiết một scope) và điền Expected "Customer Viewer có thể nhìn thấy Scope trong danh sách Scopes." 29 case còn lại chỉ đổi số TVP_ID. Chưa dựng bản mới, chưa đưa vào rule. Bảng so sánh: `projects/sgs-dtp/tests/design/so-sanh_v1.5-ban-Hanna-sua-0710-1954.md`.

## FB-051 · Ba case đọc không hiểu ý: Vai trò trong danh sách, Customer Viewer, Ghi vết - Audit log
- Ngày: 2026-10-07
- Nguồn: chat Testing 07/10 lúc 13:28, kèm 3 ảnh chụp sheet Scopes (dòng Scope_119, Scope_131, Scope_137 tô vàng) · "1. chưa hiểu ý câu này: Vai trò trong danh sách" · "2. chưa hiểu ý câu này: Customer Viewer" · "3. chưa hiểu ý câu này: Ghi vết - Audit log"
- Loại: L2-rule
- Liên quan: FB-034 (không viết lửng lơ ở Expected và Step) · FB-042 · FB-050 · rule 13, rule 14 · Q-S-23, Q-S-24, Q-S-27
- Địa chỉ: sản phẩm: Scopes!Scope_119, Scope_131, Scope_137 (và Scope_021 cùng kiểu) · rules/tc-authoring.md#13 (case để trống Expected) — sửa rule sau khi Hanna trả lời câu hỏi ở trường Câu hỏi cho Hanna
- Tiêu chí kiểm: đọc ba ô Classification, tên case và Step của một TC là hiểu case kiểm điều gì, nhìn vào đâu, so với cái gì, không phải hỏi lại người viết; Step không ghi thao tác mà màn hình không cho làm (vd "đối chiếu vai trò" khi hộp thoại không hiện vai trò); tên màn hình ghi trong Step là tên đã thấy trên Figma hoặc trên hệ thống
- Phạm vi ảnh hưởng: cả 3 TC là case để trống Expected vì chưa có căn cứ, viết ra để giữ chỗ cho một câu hỏi. Quét file Hanna gửi lúc 13:28 bằng script, TC để trống Expected: Scopes 4 (3 TC này và Scope_021 — Step ghi "dài hơn giới hạn" khi chưa biết giới hạn), Login 18, Users 12, Profile 2; ba sheet sau chưa rà cách viết. Tên màn nhật ký ghi ba kiểu ở ba sheet, chưa kiểu nào còn căn cứ để chỉ ra: "Audit Logs" (Scopes!Scope_137), "Audit Trail" (Login!TC_052), "nhật ký hoạt động của tổ chức" (Users!TC_062)
- Câu hỏi cho Hanna: case chưa có Expected mà tester không tự xác định được kết quả trên hệ thống thì (A) giữ trong file TC và viết lại cho rõ nhìn gì, so với gì; hay (B) bỏ khỏi file TC, chỉ giữ ở danh sách câu hỏi, như Hanna đã bỏ Scope_108?
- Đã sửa: chưa sửa sản phẩm. Đã giải thích ý của 3 case và đề xuất cách viết lại trong chat 07/10 và ở `projects/sgs-dtp/tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 5
- Trạng thái: Chưa rõ phạm vi
- Tái phát: 0
- Cập nhật: 2026-10-07 · Nguyên nhân phía AI: (1) Scope_119 — Step "Đối chiếu vai trò của từng người trong danh sách" không làm được vì hộp thoại Assign users chỉ hiện tên và email (theo Expected của Scope_118); hai ý "không có Customer Admin" và "người chưa kích hoạt" đã nằm ở Scope_118, case này chỉ còn một ý là Customer Viewer có trong danh sách không. (2) Scope_131 — ô cấp IV ghi "Quyền xem", Step không nói xem cái gì. (3) Scope_137 — Step ghi "Mở Audit Logs" là tên màn AI viết từ ngày 01/10, nay không tìm lại được căn cứ; đây là thông tin chưa kiểm chứng (cùng loại lỗi với FB-042).
- Cập nhật: 2026-10-07 19:55 · Hanna: "thôi bỏ qua" — câu hỏi A/B chưa được trả lời, giữ trạng thái Chưa rõ phạm vi. Trong file gửi lúc 19:55 Hanna đã tự viết lại 2 trong 3 case: Scope_134 (Customer Viewer: có Step và Expected) và Scope_122 (vai trò trong danh sách gán: có Expected); case ghi vết (Scope_140, cũ Scope_137) vẫn để trống Expected.

## FB-052 · Chuyển sang module 04 Framework Content Management: kiểm Figma và hệ thống thực tế, đề xuất các case cha theo cách học từ Scopes
- Ngày: 2026-10-07
- Nguồn: chat Testing 07/10 lúc 19:55, kèm file `SGS-DTP_TestCase1_v1.5.xlsx` và 7 dòng UC FWK-01 → FWK-07 · "thôi bỏ qua, chúng ta chuyển qua UC, hãy vào hệ thống thực tế và figma để kiểm tra > chúng ta sẽ có những case cha ntn, sau khi học từ Scopes"
- Loại: L6-tri thức
- Liên quan: FB-050, FB-051 (hoãn) · FB-042 · FB-043 → FB-047 · rules/tc-authoring.md v0.5 rule 8, 9, 27, 30
- Địa chỉ: `projects/sgs-dtp/tests/design/khung-case-cha_Frameworks.md` · `projects/sgs-dtp/docs/analysis/uc-fwk_v4-dong-dan.md` (7 dòng UC Hanna dán, lưu nguyên) · `projects/sgs-dtp/tests/design/bo-cuc-sheet_uc-v4.md` (dòng sheet Frameworks)
- Tiêu chí kiểm: mỗi nhánh Classification I → III của sheet Frameworks nêu nguồn (dòng UC, frame Figma, màn hình trên hệ thống); điều Figma, UC, hệ thống nói khác nhau thành câu hỏi Q-F-nn, không tự chọn; không viết khẳng định chưa kiểm chứng; nhóm Không thành công đặt trước Thành công, một case cho mỗi loại/trạng thái, kết quả kiểm ở nơi thao tác trả về
- Phạm vi ảnh hưởng: sheet Frameworks chưa có TC nào; 7 UC (FWK-01 → 07) và 7 frame Figma của trang 04 Frameworks
- Đã sửa: đã viết `khung-case-cha_Frameworks.md` v0.1 (57 nhóm III, 11 khối I, 131 case IV dự kiến, 17 câu hỏi Q-F-01…17, 4 câu CHẶN/quan trọng nhất ở mục 6). Chưa có TC nào được viết.
- Cách kiểm: đối chiếu từng nhánh của khung với dòng UC và frame Figma ghi ở cột Nguồn
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0
- Cập nhật: 2026-10-08 · Bắt đầu làm sau khi Hanna mở máy; việc đọc Figma và hệ thống thực hiện ngày 08/10.
- Cập nhật: 2026-10-08 · Đã ghi tài liệu khung vào thư mục; chờ Hanna duyệt khung và trả lời Q-F-04, Q-F-07, Q-F-08, Q-F-15.
- Cập nhật: 2026-10-08 09:15 · Hanna yêu cầu viết luôn TC vào file v1.5 mới. Đã thêm sheet `Frameworks` (118 case: 41 V + 77 VQ, bỏ 13 case C; 74 dòng còn Open question, 55 dòng Expected trống) vào bản sao `exports/SGS-DTP_TestCase1_v1.6_Frameworks.xlsx`, dựng từ `exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710-1954.xlsx` (file Hanna gửi, giữ nguyên). Nguồn dựng: `exports/_build/frameworks/`. Khung case cha chưa được Hanna duyệt riêng; Q-F-04, Q-F-07, Q-F-08, Q-F-15 còn mở.

## FB-053 · Soát lại và sửa các TC của sheet Frameworks do model trước viết (bản v1.6)
- Ngày: 2026-10-08
- Nguồn: chat Testing 08/10 lúc 09:20, sau khi đổi model sang Opus 5.5 · "hãy review, update lại của model Sonnet 5 vừa tạo ra TCs của Frameworks"
- Loại: L1-sản phẩm
- Liên quan: FB-052 (khung case cha, bản v1.6) · FB-042 (không khẳng định điều chưa kiểm chứng) · FB-047, FB-050 (cách viết của Hanna ở sheet Scopes) · FB-043 → FB-046 · FB-051
- Địa chỉ: sản phẩm: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.6_Frameworks.xlsx`, sheet Frameworks (Framework_001 → Framework_118) · `projects/sgs-dtp/tests/design/khung-case-cha_Frameworks.md` · nguồn dựng `projects/sgs-dtp/exports/_build/frameworks/`
- Tiêu chí kiểm: từng TC của sheet Frameworks được đối chiếu lại với UC v4 (FWK-01 → 07), Figma, hệ thống thực tế và file mẫu import; Expected có nội dung thì chỉ ra được căn cứ, căn cứ chỉ là hệ thống đang chạy thì kèm câu hỏi; Step chạy được trên màn đang có; cấu trúc, tên nhóm, Pre-condition, mã UC theo cách của sheet Scopes bản Hanna sửa; nhóm bắt buộc của từng pattern có case hoặc có lý do bỏ; có bảng ghi từng TC là giữ, sửa, bỏ hay thêm
- Phạm vi ảnh hưởng: 118 TC của sheet Frameworks ở bản v1.6
- Đã sửa: chưa
- Cách kiểm: bảng so sánh bản v1.6 với bản đã soát ở `projects/sgs-dtp/tests/design/`; script kiểm cột Căn cứ của bảng phẳng; `tc_check.py`
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0
- Cập nhật: 2026-10-08 · Đã soát và sửa qua các bản 1.7 → 1.10 (vòng soát chéo Opus/Sonnet, FB-054 → FB-056). Bản mới nhất: `exports/SGS-DTP_TestCase1_v1.10_Frameworks.xlsx`; danh sách lỗi còn lại: `tests/design/review_Frameworks_v1.10.md`.

## FB-054 · Sheet Frameworks bản 1.7: câu hỏi thừa, định dạng ô Classification, chữ Hanna sửa bị đổi
- Ngày: 2026-10-08
- Nguồn: chat Testing 08/10 15:29 (ảnh Hanna chú thích trên bản 1.7: "nếu đã có câu trả lời thì nên xóa câu hỏi"; "với những text bị che chữ thì cần cho xuống dòng, luôn cần chữ vào giữa ô, căn trái") và 15:38 "hãy sửa lại lần nữa theo comment mới nhất của Opus"
- Loại: L1-sản phẩm
- Liên quan: FB-053 · FB-042 (khẳng định chưa kiểm chứng) · FB-036
- Địa chỉ: sản phẩm: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.8_Frameworks.xlsx`, sheet Frameworks · danh sách lỗi: `projects/sgs-dtp/tests/design/review_Frameworks_v1.7.md`
- Tiêu chí kiểm: (1) cột Open question chỉ còn câu hỏi chưa có trả lời, không còn ghi chú nguồn hay kết quả đã thấy; (2) mọi ô Classification (cột B, C, D) có xuống dòng, căn giữa dọc, căn trái; (3) chữ ở các case Hanna đã sửa 08/10 15:16 không bị đổi nếu Hanna chưa bảo; (4) Expected không khẳng định điều chưa kiểm chứng; (5) không có hai case trùng tên
- Phạm vi ảnh hưởng: sheet Frameworks (166 case); script dựng sheet `tc_add_sheet.py` không đặt căn lề cho ô Classification của sheet mới (lỗi ở bản 1.6 → 1.7)
- Đã sửa: bản 1.8, kiểm bằng script: 498 ô Classification đã căn đúng; tên case trùng đã đổi; 93 case còn câu hỏi. Chưa sửa script `tc_add_sheet.py`, chưa sửa `khung-case-cha_Frameworks.md`
- Cách kiểm: mở bản 1.8, xem cột B, C, D, cột Open question; chạy `tc_check.py`
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-08 · Theo yêu cầu 16:15 "tất cả các góp ý của t cho vào rule, skill nhé": tiêu chí (1) → `rules/tc-authoring.md` v0.6 rule 13; (2) → rule 19 và `tc_check.py` (kiểm căn lề); (3) → rule 34. Skill `tc-authoring` v0.4.

## FB-055 · Sheet Frameworks bản 1.8: ghi chú chưa thành câu hỏi, 2 case mất câu hỏi, Total to meet lệch, Cover dẫn nhầm FB
- Ngày: 2026-10-08
- Nguồn: chat Testing 08/10 15:41 "tiếp tục kiểm tra lại Sonnet nhé" (Opus soát bản 1.8) và 15:48 "tiếp tục update đến khi nào hết comment của Opus"
- Loại: L1-sản phẩm
- Liên quan: FB-053, FB-054
- Địa chỉ: sản phẩm: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.9_Frameworks.xlsx`, sheet Frameworks và sheet Cover · danh sách lỗi: `projects/sgs-dtp/tests/design/review_Frameworks_v1.8.md`
- Tiêu chí kiểm: cột Open question chỉ chứa câu hỏi (không phải ghi chú/khẳng định); case nào có Expected dựa trên điều chưa kiểm chứng thì phải có câu hỏi tương ứng; Step và Expected của một case không mâu thuẫn nhau; Cover: mỗi dòng Record of change dẫn đúng FB của chính phiên bản đó
- Phạm vi ảnh hưởng: khoảng 30 case ở cột Open question, 2 case tìm kiếm (Requirements, Updated), 3 case Total to meet, dòng 1.7 ở Cover
- Đã sửa: bản 1.9. Đổi các ghi chú thành câu hỏi thật ở 24 case (cụm Q-F-14, Q-F-19, Q-F-13, Q-F-11, Q-F-20, Q-F-09, Q-F-21, Q-F-08); khôi phục câu hỏi cho case tìm theo Requirements và Updated (patch trước đó lỡ xoá, chưa kiểm được trên hệ thống nên Expected cũng để trống lại); xoá câu hỏi ở case tìm theo mã (đã được case "không có kết quả" trả lời); case Total to meet tier giữa: Expected đổi theo Rank cho khớp Pre/Step; case tier cao nhất: bỏ bước so với khối Content (không còn Expected tương ứng); Pre-condition viết rõ hơn; dòng 1.7 ở Cover trỏ lại đúng một shared string mới, chỉ còn "FB-053" (trước trỏ chung ô với dòng 1.8 nên cả hai cùng hiện "FB-053, FB-054")
- Cách kiểm: so Open question của bản 1.8 và 1.9 theo từng case; mở Cover xem cột G dòng 21, 22; `tc_check.py`
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-08 · Theo yêu cầu 16:15: Open question là câu hỏi thật → `rules/tc-authoring.md` v0.6 rule 23 và cảnh báo của `tc_check.py`; Expected chưa kiểm chứng phải kèm câu hỏi → rule 13; Step/Expected khớp → rule 31; Cover dẫn đúng FB → rule 35.

## FB-056 · Sheet Frameworks bản 1.9: đổi chữ Hanna, ô Open question còn khẳng định, hồ sơ sai số
- Ngày: 2026-10-08
- Nguồn: chat Testing 08/10 15:56 (Opus soát bản 1.9) và 15:59 "vẫn còn comment kìa"
- Loại: L1-sản phẩm
- Liên quan: FB-054, FB-055
- Địa chỉ: sản phẩm: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.10_Frameworks.xlsx`, sheet Frameworks · danh sách lỗi: `projects/sgs-dtp/tests/design/review_Frameworks_v1.9.md` · hồ sơ: `tests/design/khung-case-cha_Frameworks.md` mục 9
- Tiêu chí kiểm: (1) case Hanna đã viết Expected (bản 15:16) thì giữ nguyên chữ, không xoá, không báo sai trong chat; (2) mọi ô Open question là câu hỏi thật (có dấu hỏi, nói rõ hỏi ai điều gì), không phải cụm từ hay khẳng định; (3) hồ sơ ghi đúng số case của từng bản
- Phạm vi ảnh hưởng: 2 case tìm kiếm (Requirements, Updated), 26 ô Open question, mục 9 của khung case cha, `questions.md`
- Đã sửa: bản 1.10. Khôi phục Expected của Hanna ở 2 case (bỏ câu hỏi thừa, hỏi lại Hanna trong chat đã kiểm chưa); viết lại 26 ô Open question thành câu hỏi; sửa mục 9; thêm dòng Q-F vào `questions.md`; Cover thêm dòng 1.9 và 1.10. Chưa sửa script `tc_add_sheet.py` ở thư mục dự án (căn lề ô Classification làm tay ở bước hậu xử lý)
- Cách kiểm: so Expected hai case với file Hanna 15:16; đọc cột Open question; `tc_check.py`; `fb_report.py`
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
- Cập nhật: 2026-10-08 · Theo yêu cầu 16:15: giữ chữ người dùng → `rules/tc-authoring.md` v0.6 rule 34; ghi đúng nguồn trong câu hỏi → rule 23; hồ sơ đúng số → rule 35; báo đúng trong chat → `rules/feedback.md` v0.2 rule 16.

## FB-057 · Giá trị tính toán (Total to meet): phải hiểu logic trước khi viết, không viết bừa
- Ngày: 2026-10-08
- Nguồn: chat Testing 08/10 15:16, kèm file `SGS-DTP_TestCase1_v1.6_Frameworks.xlsx` Hanna sửa · "Giá trị tính toán: Total to meet => cần check lại case này: cần hiểu logic của nó, chứ ko viết bừa"
- Loại: L2-rule
- Liên quan: FB-048 (giá trị tính toán, còn chờ chọn A/B) · FB-055 (case Total to meet bước/Expected lệch) · Q-F-10
- Địa chỉ: rules/tc-authoring.md#31 · sản phẩm: Frameworks, nhóm Total to meet (Framework_128 → 133) · `projects/sgs-dtp/tests/design/khung-case-cha_Frameworks.md`
- Tiêu chí kiểm: mỗi giá trị tính toán có ghi ở file thiết kế: nghĩa của từng số, cách tính, căn cứ từng phần, và đã thử lại trên số thật của Figma/hệ thống; nguồn cho số khác nhau thì có câu hỏi; Pre, Step, Expected của case khớp nhau
- Phạm vi ảnh hưởng: sheet Frameworks 6 case Total to meet (bản 1.10); sheet Scopes các giá trị tính toán ở FB-048 (Evidence coverage, Coverage, Summary, dòng đếm)
- Đã sửa: sản phẩm bản 1.7 → 1.10 (logic Total to meet ghi theo công thức, Figma lệch thành Q-F-10); rule: `rules/tc-authoring.md` v0.6 rule 31
- Cách kiểm: tự soát — với mỗi case giá trị tính toán, chỉ ra được dòng giải thích cách tính ở file thiết kế và câu hỏi khi nguồn lệch
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-058 · Comment của Hanna chờ lệnh: chỉ làm lại khi Hanna bảo
- Ngày: 2026-10-08
- Nguồn: chat Testing 08/10 15:30 · "lưu ý, t viết comment nhưng khi nào t bảo làm lại hãy làm, hãy đợi lệnh của tôi"
- Loại: L2-rule
- Liên quan: FB-054 · FB-059
- Địa chỉ: rules/feedback.md#15
- Tiêu chí kiểm: sau một comment của Hanna, AI chỉ ghi FB và nói lại điều đã hiểu; không có lần dựng file nào trước khi Hanna bảo làm; yêu cầu "kiểm tra" chỉ sinh file review, không sinh file sản phẩm mới
- Phạm vi ảnh hưởng: mọi vòng sửa theo comment; phiên 08/10: lần 15:29 → 15:38 đã đợi lệnh đúng
- Đã sửa: `rules/feedback.md` v0.2 rule 15
- Cách kiểm: tự soát — mỗi bản sản phẩm mới có một câu lệnh làm lại của Hanna đứng trước nó trong chat
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-059 · Soát chéo hai model và đưa mọi góp ý vào rule, skill
- Ngày: 2026-10-08
- Nguồn: chat Testing 08/10 · 10:04 "chỉ yêu cầu Opus liệt kê lỗi/thiếu sót (không sửa file)" · 15:48 "tiếp tục update đến khi nào hết comment của Opus" · 15:59 "vẫn còn comment kìa" · 16:15 "tất cả các góp ý của t cho vào rule, skill nhé"
- Loại: L2-rule
- Liên quan: FB-053 → FB-058
- Địa chỉ: skills/tc-authoring/SKILL.md#chế-độ-phụ--soát-chéo-giữa-hai-model · skills/tc-authoring/scripts/tc_check.py · rules/tc-authoring.md v0.6 · rules/feedback.md v0.2
- Tiêu chí kiểm: mỗi vòng soát có file `tests/design/review_<sheet>_v<bản>.md`; bên soát không sửa file; mỗi loại lỗi được quét toàn sheet bằng script; bên sửa sửa hết mục của file review và báo số liệu bằng script; các góp ý của Hanna ngày 08/10 (FB-054 → FB-058) đều có chỗ trong rule hoặc skill
- Phạm vi ảnh hưởng: 4 vòng soát ngày 08/10 (review v1.7, v1.8, v1.9, v1.10). Vòng 1.8 bỏ sót vì chỉ liệt kê ID đã thấy, không quét hết sheet. Quét bằng `tc_check.py` mới trên bản 1.10: 0 lỗi căn lề ở Frameworks, 0 lỗi tô màu Open question ở Frameworks, nhiều cảnh báo "không phải câu hỏi" (đã liệt kê ở review v1.10); sheet Scopes 1 lỗi tô màu (Scope_105); file Hanna 15:16 có 70 ô sai căn lề ở Frameworks
- Đã sửa: skill `tc-authoring` v0.4 (chế độ phụ soát chéo, Bước 6, Bước 7, `references/format.md`), `tc_check.py` thêm kiểm căn lề, kiểm tô màu Open question, cảnh báo câu hỏi thiếu dấu ?; `rules/tc-authoring.md` v0.6; `rules/feedback.md` v0.2
- Cách kiểm: `python .claude/skills/tc-authoring/scripts/tc_check.py projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.10_Frameworks.xlsx --sheets Frameworks` → không còn lỗi căn lề, tô màu; số cảnh báo "không phải câu hỏi" giảm về 0 sau vòng sửa kế tiếp
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-060 · Chuyển sang module 06 Workspace Management: kiểm Figma và hệ thống, đề xuất case cha, rút kinh nghiệm từ comment của Opus
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 08:41 · "Sonnet hãy rút kinh nghiệm từ comment của Opus và tiếp tục làm UC:  06. Workspace Management, trong figma là Screens: 05 Workspace & Evidence"
- Loại: L6-tri thức
- Liên quan: FB-052 (cách làm module Frameworks) · FB-053 → FB-059 · rules/tc-authoring.md v0.6 · UC v4 WSP-01 → WSP-06
- Địa chỉ: `projects/sgs-dtp/tests/design/khung-case-cha_Workspaces.md` (chưa tạo) · `projects/sgs-dtp/tests/design/bo-cuc-sheet_uc-v4.md` (dòng sheet Workspaces, Assisted workspace)
- Tiêu chí kiểm: mỗi nhánh Classification I → III của sheet nêu nguồn (dòng UC, frame Figma, màn trên hệ thống); điều ba nguồn nói khác nhau thành câu hỏi Q-W-nn (là câu hỏi thật, có dấu ?); không viết khẳng định chưa kiểm chứng; áp rule 13, 19, 23, 31, 34 của v0.6; chưa viết file TC trước khi Hanna duyệt khung
- Phạm vi ảnh hưởng: sheet Workspaces (WSP-01 → 05), có thể thêm sheet Assisted workspace (WSP-06 + EVA); 13 TC trong sheet Scopes trỏ UC đã dời sang WSP
- Đã sửa: khung `khung-case-cha_Workspaces.md` v0.1 (09/10); sheet Workspaces v1.11 (FB-062) · cập nhật: UC lên v5.3, luồng tạo đổi (FB-061); chưa đọc Figma trang 05 Workspaces
- Cách kiểm: đối chiếu từng nhánh của khung với dòng UC và frame Figma ở cột Nguồn
- Trạng thái: Mới
- Tái phát: 0

## FB-061 · Luồng tạo workspace đổi sang Scope › Link framework; UC v5.3, đọc trực tiếp bản mới nhất
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 09:15 và 09:20 · "thay vì tạo mới từ màn hình workspace role customer admin thì nay tạo từ luồng tạo scope > tạo framwork thì có btn create workspace ở đây" · "sao ko xem trực tiếp, vì có thể có nhiều bản UC khác nhau theo update mới nhất của khách hàng"
- Loại: L6-tri thức
- Liên quan: FB-060 · UC v5.3 (SharePoint) · prototype `sgs-dtp-ds-demo-prototype.vercel.app` (vai trò Customer Admin)
- Địa chỉ: `projects/sgs-dtp/tests/design/khung-case-cha_Workspaces.md` · `projects/sgs-dtp/tests/design/bo-cuc-sheet_uc-v4.md` (dòng sheet Workspaces / Scopes sẽ lệch)
- Tiêu chí kiểm: khung Workspaces ghi form tạo workspace là hộp thoại "Link a framework" mở từ Scope; không viết case Tạo từ màn danh sách Workspaces; UC đọc trực tiếp từ SharePoint bản mới nhất, không hỏi tải file; ghi rõ phiên bản UC đã đọc ở đầu khung
- Phạm vi ảnh hưởng: sheet Scopes (11 case Gắn framework, 6 case Đổi tier) và sheet Workspaces; bố cục v4 phải cập nhật (rule 26: một chức năng một sheet)
- Đã sửa: khung `khung-case-cha_Workspaces.md` v0.1 theo luồng mới; chưa sửa bố cục v4 và sheet Scopes (chờ Hanna trả lời Q-W-01)
- Cách kiểm: mở khung, đối chiếu mục 3 với hộp thoại Link a framework trên hệ thống
- Trạng thái: Mới
- Tái phát: 0

## FB-062 · Chốt phạm vi sheet Workspaces: Gắn framework ở Scopes; viết TC như bình thường, câu hỏi vào Open question
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 09:54 · "thống nhất Sonnet tạo TCs như bt, có câu hỏi nào thì viết Open Question như mọi khi" · "Q-W-01 … => vẫn ở màn hình Scopes, khi nào sang màn hình Workspace thì sẽ hiển thị tương ứng" · "Q-W-03 … tôi cũng chưa biết nó nằm ở đâu > hãy viết TCs như tôi nói"
- Loại: L6-tri thức
- Liên quan: FB-060 · FB-061 · `khung-case-cha_Workspaces.md` · SGS-DTP_TestCase1_v1.11_Workspaces.xlsx
- Địa chỉ: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.11_Workspaces.xlsx` (sheet Workspaces) · `projects/sgs-dtp/tests/design/khung-case-cha_Workspaces.md` (mục 6, Q-W-01 đã trả lời)
- Tiêu chí kiểm: sheet Workspaces chỉ có màn danh sách và điều hướng, phân quyền, bảo mật; không có case tạo workspace, Change tier; mỗi câu hỏi còn mở nằm ở ô Open question của đúng case, dạng câu hỏi có dấu ?; Q-W-01 không còn trong ô nào
- Phạm vi ảnh hưởng: sheet Workspaces (35 TC), Cover dòng 1.11; sheet Scopes không đổi
- Đã sửa: dựng sheet Workspaces v1.11 (35 case, 5 case Expected để trống, 15 case có Open question); Q-W-12 → Q-W-15 (hộp thoại Link a framework) chưa gắn vào ô nào vì thuộc case của sheet Scopes, đã báo Hanna
- Cách kiểm: `python .claude/skills/tc-authoring/scripts/tc_check.py projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.11_Workspaces.xlsx --sheets Workspaces` → 0 lỗi (đã chạy ở bản dựng)
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-063 · Làm lại sheet Workspaces theo review của Opus
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 11:08 · "Sonnet đọc là làm lại nhé" (sau `review_Workspaces_v1.11.md`)
- Loại: L6-tri thức
- Liên quan: FB-060 · FB-061 · FB-062 · rules/tc-authoring.md rule 1, 9, 12, 13, 23, 31, 35
- Địa chỉ: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.12_Workspaces.xlsx` · `projects/sgs-dtp/tests/design/review_Workspaces_v1.11.md` · `projects/sgs-dtp/tests/design/khung-case-cha_Workspaces.md` (mục 7)
- Tiêu chí kiểm: Expected ghi nguồn Figma đã đọc (trang 05 Workspaces & Evidence, 05 Workspaces (Customer Admin)); con số coverage kiểm lại trên số Figma; mỗi câu hỏi nằm ở case mà câu trả lời làm đổi Expected; không còn Expected lặp "đúng định dạng"; Cover 1.11 và 1.12 dẫn đúng FB
- Phạm vi ảnh hưởng: sheet Workspaces (45 TC); sheet khác không đổi chữ nào (so từng ô với v1.10)
- Đã sửa: đọc Figma; sửa 7 nhóm lỗi của review; thêm Q-W-16 → Q-W-20; Q-W-05, Q-W-12 → 15 thuộc case Gắn framework ở sheet Scopes, vẫn chờ Hanna quyết nơi ghi
- Cách kiểm: `python .claude/skills/tc-authoring/scripts/tc_check.py projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.12_Workspaces.xlsx --sheets Workspaces` → 0 lỗi, 0 cảnh báo
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-064 · Vì sao vẫn bị comment nhiều: không cập nhật logic màn cũ, không tự soát trước khi giao
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 13:30 · "Tại sao Sonnet vẫn bị nhiều comment lại, Sonnet không update logic khi làm màn hình cũ à"
- Loại: L6-tri thức
- Liên quan: FB-060 → FB-063 · FB-053 → FB-059 · sheet Scopes (11 case Gắn framework, Scope_107, Q-S-20) · sheet Frameworks
- Địa chỉ: chưa sửa rule, skill; đề xuất ở câu trả lời của chat (chờ Hanna chọn)
- Tiêu chí kiểm: khi luồng, UC hoặc Figma đổi, có bảng "màn đã làm bị ảnh hưởng" và case cũ được cập nhật hoặc nêu câu hỏi trước khi giao; trước khi giao có bước tự soát theo rule 1, 9, 12, 13, 23, 31 và đọc đủ nguồn (UC, Figma, hệ thống)
- Phạm vi ảnh hưởng: skill `tc-authoring` (thêm bước), `rules/tc-authoring.md`
- Đã sửa: `rules/tc-authoring.md` v0.7 (rule 36, 37, 38); skill `tc-authoring` v0.5 (Bước 1b, Bước 6b); README. Nguồn lệnh: Hanna 09/10 16:35 "hãy làm các bước như b trình bày nhé"
- Cách kiểm: lần giao kế tiếp, review của Opus không còn lỗi thuộc nhóm "chưa đọc đủ nguồn" và "không khớp với sheet cũ"
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-065 · Viết TC cho "07. Evidence – Assisted mode": sheet Assisted workspace
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 16:35 · "tiếp theo hãy viết tc cho phần mới: 07. Evidence – Assisted mode"
- Loại: L6-tri thức
- Liên quan: FB-060 → FB-064 · rules/tc-authoring.md rule 35, 36, 37, 38 · `khung-case-cha_Workspaces.md`
- Địa chỉ: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.13_Assisted-workspace.xlsx` (sheet Assisted workspace, 114 TC; sheet Workspaces đổi 2 ô K55, W55)
- Tiêu chí kiểm: đọc đủ UC v5.3, Figma, hệ thống; mọi TC để trống Expected có câu hỏi; mỗi câu hỏi ở đúng TC; có bảng ba nguồn và bảng màn đã làm bị ảnh hưởng trước khi giao
- Phạm vi ảnh hưởng: sheet Assisted workspace (mới), sheet Workspaces (1 case Customer Viewer), Cover dòng 1.13
- Đã sửa: dựng sheet v1.13; Opus review ra 36 lỗi (`review_Assisted-workspace_v1.13.md`), trong đó bản v1.13 giao khi chưa có bản ghi FB này và chưa có hai bảng của rule 36, 37
- Cách kiểm: `tc_check.py` trên v1.13 → 0 lỗi, 0 cảnh báo; review của Opus
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-066 · Làm lại sheet Assisted workspace theo review của Opus (36 lỗi)
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 17:06 · "đọc lại và update nhé" (sau `review_Assisted-workspace_v1.13.md`)
- Loại: L6-tri thức
- Liên quan: FB-063 · FB-064 · FB-065 · rules/tc-authoring.md rule 1, 9, 12, 13, 23, 31, 34, 35, 36, 37, 38
- Địa chỉ: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.14_Assisted-workspace.xlsx` · `projects/sgs-dtp/tests/design/khung-case-cha_Evidence-Assisted.md` · `projects/sgs-dtp/tests/design/cau-hoi_Assisted-workspace.md`
- Tiêu chí kiểm: không còn Expected không có nguồn hoặc mâu thuẫn với câu hỏi đang mở; mỗi mã Q-EA là một câu hỏi; số liệu nhóm dùng số có thật; sheet nằm sau Workspaces; cột UC theo thao tác; có bảng ba nguồn và bảng màn đã làm bị ảnh hưởng
- Phạm vi ảnh hưởng: sheet Assisted workspace (122 TC); sheet Workspaces và các sheet khác không đổi so với v1.13; Cover dòng 1.14
- Đã sửa: bỏ Expected thiếu nguồn (from Medium, requirement Partial, file lớn hơn 20 MB, evidence của workspace khác); thêm Expected có căn cứ UC cho danh sách Link không có evidence chưa sạch; nhóm 1 Access Control 11 requirement thay nhóm 4 requirement; tách Q-EA-25, 27, 34; gộp Q-EA-16 vào Q-EA-23, Q-EA-38 vào Q-EA-32; thay Q-S-07 mượn bằng Q-EA-38; thêm Q-EA-40 → 48; tách case Archived thành 4 case; thêm case source, bỏ owner, chip khi Blocked, Customer User và Customer Viewer thấy owner; cột UC theo thao tác; sheet đặt sau Workspaces; viết khung case cha và file câu hỏi. Chưa làm: đọc sheet Changes vs Source của UC, case D43, Request certification (ghi ở `docs/VIEC-CON-MO.md`)
- Cách kiểm: `tc_check.py` trên v1.14 → 0 lỗi, 0 cảnh báo (2 sheet); script đếm lại 122 TC, 31 TC để trống Expected (đều có câu hỏi), 62 TC có Open question, 48 mã Q-EA
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-067 · Opus soát một lần cho đủ lỗi, không tìm lắt nhắt qua nhiều vòng
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 17:28 · "Lần sau Opus cố gắng gửi luôn 1 lần thay vì tìm lắt nhắt, còn nếu bắt buộc vì Sonnet update nên mới phát sinh lỗi mới thì ko sao"
- Loại: L6-tri thức
- Liên quan: FB-065 · FB-066 · `review_Assisted-workspace_v1.13.md` · `review_Assisted-workspace_v1.14.md` · skill `tc-authoring` chế độ soát chéo
- Địa chỉ: `rules/tc-authoring.md` rule 39 · `.claude/skills/tc-authoring/SKILL.md` chế độ soát chéo bước 2b
- Tiêu chí kiểm: ở vòng soát lại, mục "sót từ vòng trước" bằng 0; mọi mục khác là "chưa sửa hết" hoặc "phát sinh do bản sửa"
- Phạm vi ảnh hưởng: mọi lượt soát chéo TC (Opus soát, Sonnet sửa) ở mọi sheet
- Đã sửa: `rules/tc-authoring.md` v0.8 (rule 39); skill `tc-authoring` v0.6 (bước 2b); README; `review_Assisted-workspace_v1.14.md` thêm dòng phân loại: 8 trên 18 mục là sót từ vòng v1.13
- Cách kiểm: đếm mục "sót từ vòng trước" ở đầu file review của vòng soát lại kế tiếp
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-068 · Vì sao sửa review v1.13 mà vẫn còn lỗi (26/36)
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 17:30 · "Sonnet check lại lần nữa xem tại sao vẫn bị lỗi, chỉ đạt 26/36 chứ ko pải toàn bộ"
- Loại: L6-tri thức
- Liên quan: FB-064 · FB-066 · FB-067 · `review_Assisted-workspace_v1.14.md` · rules/tc-authoring.md rule 38, 39
- Địa chỉ: chưa sửa rule, skill; nguyên nhân và đề xuất ở câu trả lời của chat (chờ Hanna chọn)
- Tiêu chí kiểm: sau mỗi lượt sửa theo review, FB ghi bảng "mục review → kiểu lỗi → số case đã quét bằng script → số case còn dính"; lượt soát kế tiếp không có mục "chưa sửa hết"
- Phạm vi ảnh hưởng: bên sửa (Sonnet) ở mọi lượt sửa theo review; skill `tc-authoring` chế độ soát chéo bước 3
- Đã sửa: áp dụng ở lượt làm lại v1.15 (FB-069): mỗi kiểu lỗi quét toàn sheet bằng `quet-noi-dung_Assisted-workspace.py`, 0 phát hiện trên 129 case; chưa đưa vào rule, skill. Số thật trong file review: 27 mục đạt, 9 mục chưa đạt (3, 4, 7, 15, 22, 23, 28, 34, 35); con số 26 báo trong chat lượt trước không lấy từ script (`rules/feedback.md` rule 16)
- Cách kiểm: script quét 20 dòng trên `ea_flat.tsv` tìm lại 5 nhóm lỗi "chưa sửa hết" (104, 115, 011-013, 072, câu hỏi nhiều vế) ra đủ
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-069 · Làm lại sheet Assisted workspace theo review v1.14 (18 mục), quét cùng kiểu lỗi trên cả sheet
- Ngày: 2026-10-09
- Nguồn: chat Testing 09/10 18:22 · "Làm lại" (sau `review_Assisted-workspace_v1.14.md` và FB-068)
- Loại: L6-tri thức
- Liên quan: FB-066 · FB-067 · FB-068 · rules/tc-authoring.md rule 34, 35, 36, 37, 38, 39
- Địa chỉ: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.15_Assisted-workspace.xlsx` · `projects/sgs-dtp/tests/design/khung-case-cha_Evidence-Assisted.md` · `projects/sgs-dtp/tests/design/cau-hoi_Assisted-workspace.md` · `projects/sgs-dtp/exports/_build/v1.15/`
- Tiêu chí kiểm: script quét nội dung 0 phát hiện; sheet Workspaces và các sheet khác không đổi ô nào so với v1.14; lượt soát kế tiếp không có mục "chưa sửa hết"
- Phạm vi ảnh hưởng: sheet Assisted workspace (129 TC); Cover dòng 1.15; hồ sơ đi kèm
- Đã sửa: mục 1 → 4 (bỏ “from Medium” ở case Medium; Expected Customer Viewer liệt kê điều thấy được; UC case Workspaces sau upload là EVA-03; Q-EA-45 gắn case nhóm 11 requirement); mục 5 (tách Q-EA-3, 6, 8, 20, 21, 28, 31 thành mã riêng, thêm Q-EA-49 → 55); mục 6 (Q-EA-3 bỏ số 6 requirement, Q-EA-52 nêu rõ lệch Q-EA-45); mục 7, 8 (Pre-condition ghi tên Wei Chen, Iris Huang, Linh Tran, Mei Lin; tách case Customer Viewer trong danh sách Owner); mục 9 (Q-EA-31 gắn mọi case gỡ); mục 10 (tách case Customer User có quyền thành 3 case); mục 11, 12 (Q-EA-56 cho ô Owner xám, Q-EA-33 gắn mọi case Owner, Expected “Nobody yet”); mục 13 (Pre-condition, Step case Archived có dữ liệu cụ thể); mục 14 (case evidence chưa gắn có Expected danh sách có dòng evidence, kèm Q-EA-32); mục 15 (bảng đổi mã trong file câu hỏi); mục 16, 18 (khung case cha sửa Q-W-11, hệ thống có workspace nào); mục 17 (mục 6 khung: tự soát bằng script). Thêm theo quét: case tìm theo nhóm, tìm evidence không kết quả, thông báo sau khi gỡ, owner bị gỡ quyền vào scope (D43, Q-EA-57)
- Cách kiểm: `tc_check.py` trên v1.15 → 0 lỗi, 0 cảnh báo; `quet-noi-dung_Assisted-workspace.py` → 0 phát hiện trên 129 case; 129 TC, 35 TC để trống Expected (đều có câu hỏi), 77 TC có Open question, 57 mã Q-EA (script đếm)
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0


## FB-070 · Bảy quy tắc viết TC SGS DTP Phase 1 (từ bộ nhớ tài khoản web)
- Ngày: 2026-10-14
- Nguồn: chat Desktop 14/10 10:09, Hanna dán từ bộ nhớ tài khoản web (project "Hanna Test"). Nguyên văn:
  - When writing test cases: Steps must state exactly what to click or enter to reach the result being checked in Expected.
  - When writing test cases: keep Open questions only for conflicts between sources or things that genuinely must be checked; remove questions once answered.
  - When writing test cases: if the web/prototype already shows a behaviour and it is logical, follow the web without an Open question; if the web has more features than the UC list, follow the web (UC is updated later).
  - When reviewing test cases: a question the user has deleted means it is resolved — do not re-add it or colour the row red again.
  - When writing test cases: if the UC has something the web does not have yet, still write the case and mark it Phase 2.
  - When writing test cases: error messages not yet seen on the web are written following the app's existing message pattern (or behaviour only if it can't be guessed), and updated later if the web differs — no Open question for them.
  - When writing test cases: Pre-condition login line is written "Login acc <role> <condition>", e.g. "Login acc Customer Admin (Linh Tran) chưa có sự kiện nào" (not "Đăng nhập với acc …;").
- Loại: L2-rule
- Liên quan: FB-050 (Expected theo hệ thống) · FB-031, FB-035 (dòng đăng nhập) · rules/tc-authoring.md rule 1, 2, 13, 14, 38
- Địa chỉ: `projects/sgs-dtp/profile.md` mục "Quy tắc viết TC của dự án" · `rules/tc-authoring.md` v0.9 rule 1, 2, 13, 38, 40
- Tiêu chí kiểm: TC SGS DTP không còn Open question cho hành vi web đã thể hiện hợp lý hoặc cho text thông báo lỗi; dòng đăng nhập Pre-condition dạng "Login acc <role> (<tên>) …"; soát chéo không thêm lại câu hỏi người dùng đã xoá
- Phạm vi ảnh hưởng: mọi sheet của file TC SGS DTP (dòng đăng nhập: Scopes, Frameworks, Workspaces, Assisted workspace, Users, Profile, Login); Open question của mọi sheet cần rà theo web
- Đã sửa: rule chung giữ thứ tự nguồn UC > Figma > hệ thống, thêm ngoại lệ "profile dự án ghi khác"; quy tắc dự án ghi ở profile.md; thêm rule 40 (câu hỏi người dùng đã xoá là đã giải quyết)
- Ghi chú: quy tắc do Hanna đặt; chỗ đánh dấu Phase 2 (tiền tố "[Phase 2]" ở tên case) là đề xuất của AI, chờ Hanna chọn
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0

## FB-071 · Đánh dấu Phase 2 ở cột Remark (V), không ở tên case
- Ngày: 2026-10-14
- Nguồn: chat Desktop 14/10 10:19 · "Điền ở Remark cột V" (ảnh chụp file SGS-DTP_TestCase_v0.1_Phase1.xlsx, khoanh cột V Remark của Round 2), trả lời câu hỏi đánh dấu Phase 2 ở đâu (FB-070 quy tắc 5)
- Loại: L4-mẫu
- Liên quan: FB-070
- Địa chỉ: `projects/sgs-dtp/profile.md` mục Quy tắc viết TC, quy tắc 5 · `projects/sgs-dtp/exports/SGS-DTP_TestCase_v0.2_Phase1.xlsx` · `projects/sgs-dtp/exports/_build/v0.2/phase2_to_remark.py`
- Tiêu chí kiểm: không còn tên case bắt đầu bằng `[Phase 2]`; mọi case đó có `Phase 2` ở cột V; các ô khác không đổi so với v0.1
- Phạm vi ảnh hưởng: 58 case trên 11 sheet (Scopes 15, Workspace detail 10, Workspaces 9, Settings 6, Customers 5, Gap Analysis 4, Frameworks 2, Marketplace 2, Training Courses 2, Home 2, Certifications 1); Cover dòng 0.2
- Đã sửa: v0.2 dựng bằng sửa thẳng XML (giữ logo, dropdown, công thức); so từng ô với v0.1: chỉ đổi 58 ô tên, 58 ô V và Cover; LibreOffice tính lại 0 lỗi
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0

## FB-072 · Gom thư mục, file thừa của qa-pipeline vào một chỗ
- Ngày: 2026-10-14
- Nguồn: chat Desktop 14/10 10:19 · "ktra những folder hay thông tin file nào thừa thì merge để chung 1 chỗ nhé" (ảnh khoanh `_cho-duyet`, `_cu`, `_sao-luu`, `_to_delete` và các file ở gốc)
- Loại: L5-script
- Liên quan: docs/BAN-GIAO_2026-10-12.md Việc 1 · docs/de-xuat-don-thu-muc_2026-10-12.md
- Địa chỉ: `_luu-tru/` · `.claude/skills/tc-authoring/SKILL.md` v0.7 Bước 6 · `scripts/export_web.py` · `.gitignore` · `README.md` · `CLAUDE.md`
- Tiêu chí kiểm: gốc thư mục chỉ còn `CLAUDE.md`, `README.md`, `.gitignore` và các thư mục làm việc; không script nào trỏ tới `_cho-duyet`; `export_web.py` chạy được
- Phạm vi ảnh hưởng: `_cu`, `_sao-luu`, `_cho-duyet`, `_to_delete`, `CAP-NHAT_*`, `ap_dung_cap_nhat.py` → `_luu-tru/`; file TC v1.3–v1.15 và v0.21 → `_luu-tru/sgs-dtp-exports-cu/`; `ea_flat.tsv` → `projects/sgs-dtp/exports/_build/v1.15/`; `qa-pipeline-web.zip` → `scripts/`; UC v2.2_VI → `docs/analysis/`. Không xoá file nào
- Đã sửa: 3 script `tc_add_sheet.py`, `tc_palette.py`, `tc_restyle.py` chép vào skill; SKILL.md, `build_v15.py`, README, CLAUDE.md, VIEC-CON-MO trỏ chỗ mới; `_luu-tru/` không đưa lên git
- Ghi chú: `CLAUDE.md`, `README.md`, `.gitignore` phải ở gốc (Claude đọc `CLAUDE.md` ở gốc; git đọc `.gitignore` ở gốc). Còn lại: ghép `--like` và kiểm kiểu ô của `tc_check.py` bản cũ
- Trạng thái: Đã sửa sản phẩm
- Tái phát: 0
