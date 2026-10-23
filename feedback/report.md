# Báo cáo sổ góp ý

Sinh tự động bởi `fb_report.py` — không sửa tay. Nguồn: `feedback\log.md`. Ngày: 2026-10-21.

Tổng: **102** bản ghi · lỗi: **0** · cảnh báo: **19**

## Cần nạp khi bắt đầu task

| FB | Tiêu đề | Loại | Trạng thái | Gate |
|---|---|---|---|---|
| FB-001 | Mỗi nhận xét phải thành một bản ghi nhớ và cải thiện dần | L2-rule | Đã vào rule (chờ duyệt) | mức 3 · fb_report.py (thiếu trường, trạng thái sai, FB không được changelog trích dẫn, tái phát chưa nâng gate) |
| FB-002 | TC không ghi Pre-condition | L2-rule | Mới | chưa có |
| FB-003 | TVP_ID chỉ duy nhất trong một sheet | L4-mẫu | Mới | chưa có |
| FB-004 | TC không trỏ tới ID yêu cầu nào | L2-rule | Mới | chưa có |
| FB-005 | Bug_ID và Remark không có định dạng | L4-mẫu | Mới | chưa có |
| FB-006 | Không có tiêu chí gán Priority | L2-rule | Mới | chưa có |
| FB-007 | Nhóm phân loại khai báo nhưng không có TC | L5-script | Mới | chưa có |
| FB-008 | Không có quy tắc cho Pending / Blocked / NA và điều kiện kết thúc vòng | L2-rule | Mới | chưa có |
| FB-009 | Câu hỏi mở nằm rời ở sheet Tổng hợp | L4-mẫu | Mới | chưa có |
| FB-010 | Mỗi màn một sheet, chia khu vực, viết theo thứ tự mắt đọc | L2-rule | Đã vào rule (chờ duyệt) | mức 3 · tc_check.py |
| FB-011 | Học cấu trúc cha–con và gộp ô của bộ TC mẫu | L4-mẫu | Đã vào rule (chờ duyệt) | mức 3 · tc_build_xlsx.py tự gộp, không gộp tay |
| FB-012 | Hệ thống chỉ là bản hiển thị, chưa chạy thật | L6-tri thức | Đã vào rule (chờ duyệt) | mức 1 |
| FB-013 | Định dạng file test case | L4-mẫu | Đã vào rule (chờ duyệt) | mức 3 · script đặt định dạng, người viết không chỉnh tay |
| FB-014 | Mỗi khi nhận tài liệu phải nêu đánh giá mục đích sản phẩm | L2-rule | Đã vào rule (chờ duyệt) | mức 1 · văn xuôi trong skill; nên nâng thành mục trong checklist "Sẵn sàng bàn giao" |
| FB-015 | Đổi tên cột Chờ text cho chuyên nghiệp hơn | L4-mẫu | Đã vào rule (chờ duyệt) | mức 3 · tên cột đặt cứng trong `tc_build_xlsx.py` |
| FB-016 | Toàn bộ phải đồng nhất màu sắc, font chữ | L2-rule | Đã vào rule (chờ duyệt) | mức 3 · tc_check.py; từ 07/10 thêm tc_fix_xlsx.py --check đọc thẳng XML (trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) |
| FB-017 | Đọc sai phạm vi UC | L2-rule | Đã sửa sản phẩm | mức 1 |
| FB-018 | Khảo sát prototype chỉ trong màn đang viết | L2-rule | Mới | chưa có |
| FB-019 | File TC phải đúng form file mẫu của dự án | L4-mẫu | Đã vào rule (chờ duyệt) | mức 1 · rule 24 dạng văn xuôi. Gate mức 3 (`tc_check.py` v0.3: `--like`, bảng màu mới) đã viết và chạy sạch, nhưng chưa có hiệu lực cho tới khi được chép từ `_cho-duyet/tc-authoring-v0.3/` vào `.claude/skills/tc-authoring/` |
| FB-020 | Dự án Playwright thử nghiệm phải tách riêng và rút thành rule | L2-rule | Đã vào rule (chờ duyệt) | mức 1 · văn xuôi; mẫu dự án là mức 3 một phần (chạy được hay không) |
| FB-021 | Bộ TC FEEC Document v3 đã lỗi thời, đi từ TC để cập nhật BA | L6-tri thức | Đã sửa sản phẩm | mức 1 |
| FB-022 | Dịch tạm thông báo tiếng Nhật sang tiếng Việt, không hỏi từng câu | L2-rule | Chưa rõ phạm vi | mức 1 |
| FB-023 | tc_check.py bỏ sót kết quả mơ hồ khi chữ ở dạng tổ hợp | L5-script | Mới | chưa có |
| FB-024 | tc_build_xlsx.py đánh lại TVP_ID khi chèn hoặc xếp lại dòng | L5-script | Mới | chưa có |
| FB-025 | Làm gọn: chỉ nghiệp vụ, câu hỏi, SRS / US / UC, không chạy cả bộ rule | L2-rule | Chưa rõ phạm vi | chưa có |
| FB-026 | Thay TC bằng file phân tích case cha con, dễ nhìn, dễ hiểu | L4-mẫu | Đã sửa sản phẩm | chưa có |
| FB-027 | Bàn giao bằng một zip giữ cấu trúc thư mục, kèm danh sách file và fb-moi.md | L4-mẫu | Đã sửa sản phẩm | chưa có |
| FB-028 | Học cách kiểm của người dùng: case ngoài nghiệp vụ để tránh lọt bug | L6-tri thức | Đã vào rule (chờ duyệt) | mức 1 · văn xuôi (chưa có script kiểm mục `CK-`). `rtm_check.py` không cần sửa: nguồn là dòng EG có sẵn |
| FB-029 | Chia sheet theo màn hình, vai trò nằm trong sheet | L2-rule | Đã vào rule (chờ duyệt) | mức 1 · đề xuất nâng mức 3: tc_check.py báo Pre-condition không mở đầu bằng dòng đăng nhập của rule 14 |
| FB-030 | Gộp, tách sheet theo màn hình, không theo module của UC list | L2-rule | Đã vào rule (chờ duyệt) | mức 1 · đề xuất nâng mức 3: tc_check.py đối chiếu bảng UC → sheet với UC list |
| FB-031 | Viết TC bằng tiếng Anh; ít nhất tên nút giữ nguyên tiếng Anh | L2-rule | Đã duyệt | mức 1 · đề xuất nâng mức 3: tc_check.py cảnh báo ô có chữ tiếng Việt ngoài cột Open question và sheet Cần xác nhận; đối chiếu tên nút với danh sách nhãn Figma nếu có danh sách đó |
| FB-032 | Trạng thái rỗng đặt trước, theo vòng đời dữ liệu rỗng → tạo → có dữ liệu | L2-rule | Đã duyệt | mức 1 |
| FB-033 | Trạng thái rỗng phải tả đủ icon, chữ, nút | L3-checklist | Đã duyệt | mức 2 · mục bắt buộc trong checklist của pattern Bảng |
| FB-034 | Không viết lửng lơ ở Expected và Step; không biết thì đưa vào Q&A | L2-rule | Đã duyệt | mức 1 · nâng mức 3 được cho phần tìm chuỗi |
| FB-035 | Pre-condition đăng nhập ghi bằng vai trò: "Đăng nhập với acc Customer Admin" | L4-mẫu | Đã duyệt | mức 3 · tc_check.py báo lỗi TC còn dạng {{…}} (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) |
| FB-036 | Nhiều mục thì mỗi mục một dòng, không nối bằng " · " | L4-mẫu | Đã duyệt | mức 3 · tc_check.py cảnh báo Expected có " · " |
| FB-038 | Gửi bản xem trước danh sách tính năng trước khi cập nhật file TC | L2-rule | Đã duyệt | mức 1 |
| FB-039 | TC gọi API chỉ viết khi tester được gọi API, và để ở sheet API riêng | L2-rule | Đã duyệt | mức 1 |
| FB-040 | Pre-condition không ghi mở màn hình đang test; liệt kê thao tác khi phải qua màn khác | L2-rule | Đã vào rule (chờ duyệt) | mức 2 · cảnh báo bằng script (chưa chặn) |
| FB-041 | Thiếu case kiểm hiển thị từng thông tin sau khi tạo | L3-checklist | Đã vào rule (chờ duyệt) | mức 1 · văn xuôi (chưa có script kiểm) |
| FB-042 | Thông tin chưa kiểm chứng không được viết vào TC dạng khẳng định | L2-rule | Đã vào rule (chờ duyệt) | mức 1 · rule 13 và SKILL Bước 4 (văn xuôi). Đề xuất mức 3: thêm cột Căn cứ vào bảng phẳng (UC / Figma / hệ thống đang chạy), script báo dòng có Expected mà không có căn cứ — chờ Hanna quyết |
| FB-043 | Nhóm Thành công của chức năng tạo: mỗi loại một case, bỏ case không cần thiết | L3-checklist | Đã vào rule (chờ duyệt) | mức 2 · references/patterns.md P1, P7 (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) và rule 30 |
| FB-044 | Hiển thị ở màn chi tiết kiểm ở khu vực Chi tiết, không lặp ở khu vực Tạo mới | L2-rule | Đã vào rule (chờ duyệt) | mức 1 · rule 9 và SKILL Bước 4 (văn xuôi) |
| FB-045 | Case kiểm tra dữ liệu có bước bấm nút gửi mà không lưu thì gộp vào nhóm Không thành công | L2-rule | Đã vào rule (chờ duyệt) | mức 3 · tc_check.py cảnh báo khu vực còn nhóm Kiểm tra dữ liệu (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) |
| FB-046 | Bỏ {{…}}; dữ liệu chưa xác định viết chung chung trong ngoặc vuông [tên] | L4-mẫu | Đã vào rule (chờ duyệt) | mức 3 · tc_check.py báo lỗi TC còn dạng {{…}} (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) |
| FB-047 | Học cách viết của Hanna ở TC 1–67 sheet Scopes (v1.4) để viết phần còn lại | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-048 | Cột Evidence coverage cần nhiều TC hơn để xác định hiển thị thế nào là đúng | L3-checklist | Chưa rõ phạm vi | mức 2 · references/patterns.md P12, mục cột giá trị tính toán (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) |
| FB-049 | Ô bắt đầu bằng dấu gạch phải có dấu nháy đơn để không thành công thức | L5-script | Đã vào rule (chờ duyệt) | mức 3 · tc_fix_xlsx.py --check và tc_check.py báo ô thiếu dấu nháy đơn (bản 07/10 trong `CAP-NHAT_2026-10-07_scopes-v1.5.md`, chờ áp) |
| FB-050 | Hanna sửa trực tiếp bản v1.5: điền Expected, bỏ và sắp xếp lại case | L6-tri thức | Mới | chưa có |
| FB-051 | Ba case đọc không hiểu ý: Vai trò trong danh sách, Customer Viewer, Ghi vết - Audit log | L2-rule | Chưa rõ phạm vi | chưa có |
| FB-052 | Chuyển sang module 04 Framework Content Management: kiểm Figma và hệ thống thực tế, đề xuất các case cha theo cách học từ Scopes | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-053 | Soát lại và sửa các TC của sheet Frameworks do model trước viết (bản v1.6) | L1-sản phẩm | Đã sửa sản phẩm | chưa có |
| FB-054 | Sheet Frameworks bản 1.7: câu hỏi thừa, định dạng ô Classification, chữ Hanna sửa bị đổi | L1-sản phẩm | Đã vào rule (chờ duyệt) | chưa có |
| FB-055 | Sheet Frameworks bản 1.8: ghi chú chưa thành câu hỏi, 2 case mất câu hỏi, Total to meet lệch, Cover dẫn nhầm FB | L1-sản phẩm | Đã vào rule (chờ duyệt) | chưa có |
| FB-056 | Sheet Frameworks bản 1.9: đổi chữ Hanna, ô Open question còn khẳng định, hồ sơ sai số | L1-sản phẩm | Đã vào rule (chờ duyệt) | chưa có |
| FB-057 | Giá trị tính toán (Total to meet): phải hiểu logic trước khi viết, không viết bừa | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-058 | Comment của Hanna chờ lệnh: chỉ làm lại khi Hanna bảo | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-059 | Soát chéo hai model và đưa mọi góp ý vào rule, skill | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-060 | Chuyển sang module 06 Workspace Management: kiểm Figma và hệ thống, đề xuất case cha, rút kinh nghiệm từ comment của Opus | L6-tri thức | Mới | chưa có |
| FB-061 | Luồng tạo workspace đổi sang Scope › Link framework; UC v5.3, đọc trực tiếp bản mới nhất | L6-tri thức | Mới | chưa có |
| FB-062 | Chốt phạm vi sheet Workspaces: Gắn framework ở Scopes; viết TC như bình thường, câu hỏi vào Open question | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-063 | Làm lại sheet Workspaces theo review của Opus | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-064 | Vì sao vẫn bị comment nhiều: không cập nhật logic màn cũ, không tự soát trước khi giao | L6-tri thức | Đã vào rule (chờ duyệt) | chưa có |
| FB-065 | Viết TC cho "07. Evidence – Assisted mode": sheet Assisted workspace | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-066 | Làm lại sheet Assisted workspace theo review của Opus (36 lỗi) | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-067 | Opus soát một lần cho đủ lỗi, không tìm lắt nhắt qua nhiều vòng | L6-tri thức | Đã vào rule (chờ duyệt) | chưa có |
| FB-068 | Vì sao sửa review v1.13 mà vẫn còn lỗi (26/36) | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-069 | Làm lại sheet Assisted workspace theo review v1.14 (18 mục), quét cùng kiểu lỗi trên cả sheet | L6-tri thức | Đã sửa sản phẩm | chưa có |
| FB-070 | Bảy quy tắc viết TC SGS DTP Phase 1 (từ bộ nhớ tài khoản web) | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-071 | Đánh dấu Phase 2 ở cột Remark (V), không ở tên case | L4-mẫu | Đã sửa sản phẩm | chưa có |
| FB-072 | Gom thư mục, file thừa của qa-pipeline vào một chỗ | L5-script | Đã sửa sản phẩm | chưa có |
| FB-073 | Soát toàn bộ file TC v0.1 Phase 1 theo 3 wave, trả bản có nhận xét (không sửa) | L1-sản phẩm | Mới | chưa có |
| FB-074 | Creator ghi Claude thay vì Hanna | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-075 | File giao còn `{{…}}` | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-076 | Ô trống, ô gộp hiện Arial; phông phải đúng ở mức XML | L5-script | Đã vào rule (chờ duyệt) | chưa có |
| FB-077 | Dòng đăng nhập `Login acc <vai trò> <điều kiện>`, không `;` | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-078 | Quá nhiều câu hỏi; câu đã xoá bị tô lại; thứ tự 5 nguồn; Expected đề xuất tô vàng; Đề xuất mặc định | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-079 | Chữ báo lỗi chưa thấy trên web ghi theo mẫu của app | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-080 | Step chưa rõ bấm vào đâu | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-081 | UC có mà web chưa có: `[Phase 2]`, `[Ngoài Phase 1]`; độ phủ UC theo wave; `[OUT]`; mã TC không đánh lại | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-082 | So sánh v0.22 và v0.2_Phase1: chèn đúng nhóm, Test_Report theo nhóm, một số phiên bản, Priority Critical, một bộ rule duy nhất | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-083 | Case `[OUT]` phải xoá khỏi file TC, không giữ lại | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-084 | Câu hỏi Cần xác nhận đã đóng thì xoá khỏi sheet; câu trả lời đưa vào Expected | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-085 | Không thêm sheet mới vào file TC; báo cáo, rà soát, bug để ở file riêng | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-086 | Mã TC đồng nhất với cột No. | L2-rule | Chưa rõ phạm vi | chưa có |
| FB-087 | Bộ case abnormal cho ô nhập: biên độ dài, vượt 1 ký tự, sai định dạng nhiều dạng, dữ liệu đặc biệt — viết rõ cách tạo chuỗi | L3-checklist | Đã vào rule (chờ duyệt) | chưa có |
| FB-088 | Hộp thoại nhiều bước: nhóm case theo từng bước (tab) | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-089 | Pre-condition ngắn gọn, đánh số: môi trường → tài khoản → điều kiện dữ liệu | L4-mẫu | Đã vào rule (chờ duyệt) | chưa có |
| FB-090 | Remark "Thực tế" tách dòng, có tên và số liệu thật; nêu đúng vấn đề | L4-mẫu | Đã vào rule (chờ duyệt) | chưa có |
| FB-091 | Kết quả Fail phải có file bằng chứng kèm ảnh, dạng như E2E | L4-mẫu | Đã vào rule (chờ duyệt) | chưa có |
| FB-092 | Bug gộp theo nguyên nhân; bug phát hiện khi test tự do thì thêm cả case | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-093 | Kết quả: Failed khi lệch cả thiết kế; Pending cho UC chưa Done theo Plan, giữ case không bỏ | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-094 | Sheet E2E: mỗi bước có ảnh Figma màn thao tác, ảnh Figma kết quả mong đợi và ảnh thực tế | L4-mẫu | Đã vào rule (chờ duyệt) | chưa có |
| FB-095 | Quyết định của dev / dự án đè Figma thì TC theo quyết định đó | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-096 | Chỉ chạy test trên localhost; luôn nêu rõ môi trường, nhánh, commit, ngày | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-097 | Rà soát TC theo Figma, UC và web: từng case Xoá / Sửa / Lệch web / Wave sau / OK, chỉ wave đang làm, chưa sửa khi chưa có lệnh | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-098 | Lệch giữa quy ước dự án và web hiện tại cần người dùng chốt (404 scope; Documents / Evidence Library) | L6-tri thức | Chưa rõ phạm vi | chưa có |
| FB-099 | Nghiệp vụ cấm thao tác và web ẩn nút → đúng, không phải bug (xoá workspace có evidence / request) | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-100 | Case cần email thật: gửi mời, lấy link từ người dùng trước rồi mới chạy; hỏi lại thay vì chạy hàng loạt | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-101 | Đối chiếu US / decision log / contract mới nhất trước khi ghi bug; bug sai thì Rút, không xoá mã | L2-rule | Đã vào rule (chờ duyệt) | chưa có |
| FB-102 | Mã TC có tiền tố theo màn (vd Documents DC_001), duy nhất trong file | L2-rule | Đã vào rule (chờ duyệt) | chưa có |

## Chờ người dùng duyệt

- FB-001 · Mỗi nhận xét phải thành một bản ghi nhớ và cải thiện dần (rules/feedback.md · skills/feedback-loop/ · feedback/log.md)
- FB-010 · Mỗi màn một sheet, chia khu vực, viết theo thứ tự mắt đọc (rules/tc-authoring.md#B · skills/tc-authoring/SKILL.md#bước-2 · references/patterns.md)
- FB-011 · Học cấu trúc cha–con và gộp ô của bộ TC mẫu (rules/tc-authoring.md#C · rules/tc-authoring.md#F · references/format.md)
- FB-012 · Hệ thống chỉ là bản hiển thị, chưa chạy thật (rules/common.md#9 · rules/tc-authoring.md#A)
- FB-013 · Định dạng file test case (rules/tc-authoring.md#F · references/format.md#4 · scripts/tc_build_xlsx.py)
- FB-014 · Mỗi khi nhận tài liệu phải nêu đánh giá mục đích sản phẩm (skills/ba-analysis/SKILL.md#bước-0)
- FB-015 · Đổi tên cột Chờ text cho chuyên nghiệp hơn (rules/tc-authoring.md#13 #16 #23 · skills/tc-authoring/references/format.md#3 · scripts/tc_build_xlsx.py · scripts/tc_check.py)
- FB-016 · Toàn bộ phải đồng nhất màu sắc, font chữ (rules/tc-authoring.md#22 · skills/tc-authoring/references/format.md#4 · scripts/tc_check.py)
- FB-019 · File TC phải đúng form file mẫu của dự án (rules/tc-authoring.md#22 · skills/tc-authoring/references/format.md#4 · skills/tc-authoring/scripts/tc_build_xlsx.py · skills/tc-authoring/scripts/tc_check.py (PALETTE) · projects/<dự-án>/profile.md (dòng "File TC mẫu của dự án"))
- FB-020 · Dự án Playwright thử nghiệm phải tách riêng và rút thành rule (rules/automation.md#11-18 · automation/_template/ · automation/feec-learning/ · CLAUDE.md (mục Nhiều dự án) · README.md)
- FB-028 · Học cách kiểm của người dùng: case ngoài nghiệp vụ để tránh lọt bug (skills/test-design/references/technical-risk-checklist.md · skills/test-design/references/coverage-checklist.md#D,E · skills/test-design/references/templates.md#7 · skills/test-design/SKILL.md · skills/tc-authoring/references/patterns.md#P9,P12 · rules/tester.md#12,13)
- FB-029 · Chia sheet theo màn hình, vai trò nằm trong sheet (rules/tc-authoring.md#24 · rules/tc-authoring.md#27 · skills/tc-authoring/SKILL.md#đầu-ra · skills/tc-authoring/SKILL.md#bước-4 · skills/tc-authoring/SKILL.md#bước-5 · scripts/tc_check.py)
- FB-030 · Gộp, tách sheet theo màn hình, không theo module của UC list (rules/tc-authoring.md#3 · rules/tc-authoring.md#25 · rules/tc-authoring.md#26 · rules/tc-authoring.md#28 · skills/tc-authoring/SKILL.md#bước-1 · references/templates.md#4)
- FB-040 · Pre-condition không ghi mở màn hình đang test; liệt kê thao tác khi phải qua màn khác (rules/tc-authoring.md#14 · skills/tc-authoring/scripts/tc_check.py (OPEN_SCREEN) · skills/test-design/references/coverage-checklist.md#E)
- FB-041 · Thiếu case kiểm hiển thị từng thông tin sau khi tạo (rules/tc-authoring.md#30 · skills/tc-authoring/references/patterns.md#P1,P7 · skills/test-design/references/coverage-checklist.md#E)
- FB-042 · Thông tin chưa kiểm chứng không được viết vào TC dạng khẳng định (rules/tc-authoring.md#13 · rules/tc-authoring.md#9 · skills/tc-authoring/SKILL.md#bước-4 · sản phẩm: Scopes!Scope_023, Scope_024 (v1.3))
- FB-043 · Nhóm Thành công của chức năng tạo: mỗi loại một case, bỏ case không cần thiết (rules/tc-authoring.md#30 · skills/tc-authoring/references/patterns.md#P1,P7 · skills/test-design/references/coverage-checklist.md#E · sản phẩm: Scopes, Tạo scope ▸ Thành công)
- FB-044 · Hiển thị ở màn chi tiết kiểm ở khu vực Chi tiết, không lặp ở khu vực Tạo mới (rules/tc-authoring.md#9 · rules/tc-authoring.md#30 · skills/tc-authoring/SKILL.md#bước-4 · sản phẩm: Scopes (Tạo scope, Sửa scope, Gắn framework, Gán người dùng))
- FB-045 · Case kiểm tra dữ liệu có bước bấm nút gửi mà không lưu thì gộp vào nhóm Không thành công (rules/tc-authoring.md#8 · skills/tc-authoring/SKILL.md#bước-5 · skills/tc-authoring/references/format.md#7 · sản phẩm: Scopes (Sửa scope, Gắn framework), Login (Email, Mật khẩu))
- FB-046 · Bỏ {{…}}; dữ liệu chưa xác định viết chung chung trong ngoặc vuông [tên] (rules/tc-authoring.md#14 · skills/tc-authoring/scripts/tc_check.py · sản phẩm: mọi sheet TC)
- FB-049 · Ô bắt đầu bằng dấu gạch phải có dấu nháy đơn để không thành công thức (skills/tc-authoring/scripts/tc_build_xlsx.py · skills/tc-authoring/scripts/tc_check.py · skills/tc-authoring/references/format.md#4 · rules/tc-authoring.md#F)
- FB-054 · Sheet Frameworks bản 1.7: câu hỏi thừa, định dạng ô Classification, chữ Hanna sửa bị đổi (sản phẩm: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.8_Frameworks.xlsx`, sheet Frameworks · danh sách lỗi: `projects/sgs-dtp/tests/design/review_Frameworks_v1.7.md`)
- FB-055 · Sheet Frameworks bản 1.8: ghi chú chưa thành câu hỏi, 2 case mất câu hỏi, Total to meet lệch, Cover dẫn nhầm FB (sản phẩm: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.9_Frameworks.xlsx`, sheet Frameworks và sheet Cover · danh sách lỗi: `projects/sgs-dtp/tests/design/review_Frameworks_v1.8.md`)
- FB-056 · Sheet Frameworks bản 1.9: đổi chữ Hanna, ô Open question còn khẳng định, hồ sơ sai số (sản phẩm: `projects/sgs-dtp/exports/SGS-DTP_TestCase1_v1.10_Frameworks.xlsx`, sheet Frameworks · danh sách lỗi: `projects/sgs-dtp/tests/design/review_Frameworks_v1.9.md` · hồ sơ: `tests/design/khung-case-cha_Frameworks.md` mục 9)
- FB-057 · Giá trị tính toán (Total to meet): phải hiểu logic trước khi viết, không viết bừa (rules/tc-authoring.md#31 · sản phẩm: Frameworks, nhóm Total to meet (Framework_128 → 133) · `projects/sgs-dtp/tests/design/khung-case-cha_Frameworks.md`)
- FB-058 · Comment của Hanna chờ lệnh: chỉ làm lại khi Hanna bảo (rules/feedback.md#15)
- FB-059 · Soát chéo hai model và đưa mọi góp ý vào rule, skill (skills/tc-authoring/SKILL.md#chế-độ-phụ--soát-chéo-giữa-hai-model · skills/tc-authoring/scripts/tc_check.py · rules/tc-authoring.md v0.6 · rules/feedback.md v0.2)
- FB-064 · Vì sao vẫn bị comment nhiều: không cập nhật logic màn cũ, không tự soát trước khi giao (chưa sửa rule, skill; đề xuất ở câu trả lời của chat (chờ Hanna chọn))
- FB-067 · Opus soát một lần cho đủ lỗi, không tìm lắt nhắt qua nhiều vòng (`rules/tc-authoring.md` rule 39 · `.claude/skills/tc-authoring/SKILL.md` chế độ soát chéo bước 2b)
- FB-070 · Bảy quy tắc viết TC SGS DTP Phase 1 (từ bộ nhớ tài khoản web) (`projects/sgs-dtp/profile.md` mục "Quy tắc viết TC của dự án" · `rules/tc-authoring.md` v0.9 rule 1, 2, 13, 38, 40)
- FB-074 · Creator ghi Claude thay vì Hanna (rules/tc-authoring.md rule 6 · tc_add_sheet.py `--creator` bắt buộc)
- FB-075 · File giao còn `{{…}}` (rules/tc-authoring.md rule 14)
- FB-076 · Ô trống, ô gộp hiện Arial; phông phải đúng ở mức XML (rules/tc-authoring.md rule 18, 38 · tc_fix_xlsx.py (chờ file))
- FB-077 · Dòng đăng nhập `Login acc <vai trò> <điều kiện>`, không `;` (rules/tc-authoring.md rule 14, 24)
- FB-078 · Quá nhiều câu hỏi; câu đã xoá bị tô lại; thứ tự 5 nguồn; Expected đề xuất tô vàng; Đề xuất mặc định (rules/tc-authoring.md rule 1, 2, 13, 23, 36)
- FB-079 · Chữ báo lỗi chưa thấy trên web ghi theo mẫu của app (rules/tc-authoring.md rule 13)
- FB-080 · Step chưa rõ bấm vào đâu (rules/tc-authoring.md rule 14)
- FB-081 · UC có mà web chưa có: `[Phase 2]`, `[Ngoài Phase 1]`; độ phủ UC theo wave; `[OUT]`; mã TC không đánh lại (rules/tc-authoring.md rule 10, 11, 40 · SKILL.md Bước 0 · profile.md wave)
- FB-082 · So sánh v0.22 và v0.2_Phase1: chèn đúng nhóm, Test_Report theo nhóm, một số phiên bản, Priority Critical, một bộ rule duy nhất (rules/tc-authoring.md rule 8, 15, 24, 35 · CLAUDE.md · tc_rows.py (chờ file))
- FB-083 · Case `[OUT]` phải xoá khỏi file TC, không giữ lại (rules/tc-authoring.md rule 10, 40)
- FB-084 · Câu hỏi Cần xác nhận đã đóng thì xoá khỏi sheet; câu trả lời đưa vào Expected (rules/tc-authoring.md rule 13)
- FB-085 · Không thêm sheet mới vào file TC; báo cáo, rà soát, bug để ở file riêng (rules/tc-authoring.md rule 3)
- FB-087 · Bộ case abnormal cho ô nhập: biên độ dài, vượt 1 ký tự, sai định dạng nhiều dạng, dữ liệu đặc biệt — viết rõ cách tạo chuỗi (rules/tc-authoring.md rule 15)
- FB-088 · Hộp thoại nhiều bước: nhóm case theo từng bước (tab) (rules/tc-authoring.md rule 7)
- FB-089 · Pre-condition ngắn gọn, đánh số: môi trường → tài khoản → điều kiện dữ liệu (rules/tc-authoring.md rule 14 · skills/e2e-flow/SKILL.md)
- FB-090 · Remark "Thực tế" tách dòng, có tên và số liệu thật; nêu đúng vấn đề (rules/automation.md rule 20 · skills/manual-run/SKILL.md bước 4)
- FB-091 · Kết quả Fail phải có file bằng chứng kèm ảnh, dạng như E2E (skills/bug-evidence/SKILL.md · rules/automation.md rule 21)
- FB-092 · Bug gộp theo nguyên nhân; bug phát hiện khi test tự do thì thêm cả case (rules/automation.md rule 21)
- FB-093 · Kết quả: Failed khi lệch cả thiết kế; Pending cho UC chưa Done theo Plan, giữ case không bỏ (rules/automation.md rule 19)
- FB-094 · Sheet E2E: mỗi bước có ảnh Figma màn thao tác, ảnh Figma kết quả mong đợi và ảnh thực tế (skills/e2e-flow/SKILL.md)
- FB-095 · Quyết định của dev / dự án đè Figma thì TC theo quyết định đó (rules/tc-authoring.md rule 1)
- FB-096 · Chỉ chạy test trên localhost; luôn nêu rõ môi trường, nhánh, commit, ngày (rules/automation.md rule 22 · projects/sgs-dtp/profile.md)
- FB-097 · Rà soát TC theo Figma, UC và web: từng case Xoá / Sửa / Lệch web / Wave sau / OK, chỉ wave đang làm, chưa sửa khi chưa có lệnh (skills/tc-review/SKILL.md (mới) · rules/feedback.md rule 15)
- FB-099 · Nghiệp vụ cấm thao tác và web ẩn nút → đúng, không phải bug (xoá workspace có evidence / request) (rules/tc-authoring.md rule 1)
- FB-100 · Case cần email thật: gửi mời, lấy link từ người dùng trước rồi mới chạy; hỏi lại thay vì chạy hàng loạt (rules/automation.md rule 27)
- FB-101 · Đối chiếu US / decision log / contract mới nhất trước khi ghi bug; bug sai thì Rút, không xoá mã (rules/automation.md rule 28)
- FB-102 · Mã TC có tiền tố theo màn (vd Documents DC_001), duy nhất trong file (rules/tc-authoring.md rule 11)

## Thống kê

| Trạng thái | Số lượng |
|---|---|
| Bị bác | 1 |
| Chưa rõ phạm vi | 6 |
| Mới | 15 |
| Đã duyệt | 8 |
| Đã sửa sản phẩm | 15 |
| Đã vào rule (chờ duyệt) | 57 |

| Loại | Số lượng |
|---|---|
| L1-sản phẩm | 5 |
| L2-rule | 52 |
| L3-checklist | 5 |
| L4-mẫu | 17 |
| L5-script | 6 |
| L6-tri thức | 17 |

## Lỗi

Không có.

## Cảnh báo

- FB-002 · đứng ở 'Mới' 22 ngày
- FB-003 · đứng ở 'Mới' 22 ngày
- FB-004 · đứng ở 'Mới' 22 ngày
- FB-005 · đứng ở 'Mới' 22 ngày
- FB-006 · đứng ở 'Mới' 22 ngày
- FB-007 · đứng ở 'Mới' 22 ngày
- FB-008 · đứng ở 'Mới' 22 ngày
- FB-009 · đứng ở 'Mới' 22 ngày
- FB-018 · đứng ở 'Mới' 20 ngày
- FB-022 · đứng ở 'Chưa rõ phạm vi' 19 ngày
- FB-023 · đứng ở 'Mới' 19 ngày
- FB-024 · đứng ở 'Mới' 19 ngày
- FB-025 · đứng ở 'Chưa rõ phạm vi' 19 ngày
- FB-034 · tái phát 1 lần, Gate 'mức 1 · nâng mức 3 được cho phần tìm chuỗi' — nên nâng một mức
- FB-048 · đứng ở 'Chưa rõ phạm vi' 14 ngày
- FB-050 · đứng ở 'Mới' 14 ngày
- FB-051 · đứng ở 'Chưa rõ phạm vi' 14 ngày
- FB-060 · đứng ở 'Mới' 12 ngày
- FB-061 · đứng ở 'Mới' 12 ngày
