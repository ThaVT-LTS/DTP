# Câu hỏi mở của sheet Assisted workspace

- Sinh bằng script từ `cases_ea.py` của bản dựng v1.15 (file `exports/SGS-DTP_TestCase1_v1.15_Assisted-workspace.xlsx`). Số đếm do script tính: **129 TC**, **35 TC để trống Expected** (đều có câu hỏi), **77 TC có Open question**, **57 mã** `Q-EA`.
- Mỗi mã là một câu hỏi, gắn ở các TC mà câu trả lời làm đổi Expected của TC đó.
- Chưa đưa vào sheet `Cần xác nhận`: chờ Hanna chọn câu nào lên sheet đó (như ở Scopes). Mức CHẶN, QUAN TRỌNG, NHỎ chưa xếp: chờ Hanna.

## 1. Danh sách

| Mã | Câu hỏi và căn cứ | TC đang chờ |
|---|---|---|
| Q-EA-01 | Để có workspace 38 trên 61 requirement đủ evidence thì phải tạo 38 requirement có evidence: có dữ liệu dựng sẵn hoặc cách dựng nhanh không? (Figma Workspace / Requirement ghi 38 of 61 · 62%; hệ thống mới chỉ có 0 of 61 và 6 of 31) | Assisted workspace_005 |
| Q-EA-02 | Nhãn vàng “No design yet” cạnh ô Owner là gì và khi nào hiện? (chỉ có ở hệ thống, requirement nào cũng có; UC và Figma không nêu) | Assisted workspace_038 |
| Q-EA-03 | Requirement ở trạng thái Partial khi nào? (UC EVA-07 chỉ ghi Provided, Missing, Out of scope; Figma có chip Partial ở nhóm Access Control 58%) | Assisted workspace_016, Assisted workspace_030 |
| Q-EA-04 | Requirement ngoài tier hoặc đã retired có hiện trong cây với trạng thái Out of scope không, hay bị ẩn? (UC WSP-06 ghi “not counted”, UC EVA-07 có trạng thái Out of scope; hệ thống ở workspace Medium chỉ hiện 61 requirement, không có chip Out of scope) | Assisted workspace_017 |
| Q-EA-05 | “Clarification requested” hiện ở đâu (chip trạng thái, bộ lọc) và khi nào xuất hiện? (UC EVA-01, EVA-02 và D41: làm rõ qua Gap Analysis; Figma không có; bộ lọc hệ thống chỉ có All, Missing, Partial, Provided) | Assisted workspace_018, Assisted workspace_027 |
| Q-EA-06 | Khi có cả bộ lọc trạng thái và từ khoá tìm kiếm thì hai điều kiện áp cùng lúc đúng không? (UC EVA-01 chỉ ghi “search and filter”) | Assisted workspace_031 |
| Q-EA-07 | Khi bộ lọc trạng thái không có requirement nào khớp thì hiện thông báo gì? (hệ thống chỉ có thông báo cho trường hợp tìm kiếm: “No matching requirements” / “Try another search or filter”; Figma không có trạng thái này) | Assisted workspace_032 |
| Q-EA-08 | Nhãn “from <tier>” hiện thế nào với requirement thêm ở Medium hoặc High? (Figma, hệ thống chỉ có “from Basic”) | Assisted workspace_035 |
| Q-EA-09 | Requirement có nhiều expected evidence thì thẻ nào nhận file khi bấm Upload evidence hoặc Link existing evidence, dòng đếm ghi thế nào, và có expected evidence không bắt buộc (Optional) không? (Figma, hệ thống chỉ có requirement một expected evidence “Mandatory”; hộp thoại Upload ghi “For <requirement> · <EE>”) | Assisted workspace_045 |
| Q-EA-10 | Câu “No evidence yet. Upload a file or link one that is already in this workspace.” có đúng văn bản chính thức không? (chỉ lấy từ hệ thống; Figma chưa có thẻ expected evidence trống) | Assisted workspace_044 |
| Q-EA-11 | Dòng evidence ở màn requirement có hiện nhãn version (v1, v2, v3) như D21 không? (UC D21: “requirements show only the current version of each document with a version label”; Figma chỉ có tên file access-control-policy-v3.pdf, không có nhãn) | Assisted workspace_050 |
| Q-EA-12 | Định dạng ngày ở dòng evidence là “Uploaded Sep 12, 2026” hay “12 Sep 2026”? (Figma dòng evidence ghi “Sep 12, 2026”, Figma chi tiết evidence và hộp thoại Upload ghi “12 Sep 2026”) | Assisted workspace_046 |
| Q-EA-13 | Evidence không có ngày hết hạn thì dòng evidence hiện thế nào (bỏ “valid until” hay ghi “no expiry”)? (Figma chỉ có evidence có “valid until Sep 2027”; hộp thoại Upload ghi “Leave empty if it doesn't expire.”) | Assisted workspace_049 |
| Q-EA-14 | Evidence quá ngày Valid until thì requirement còn Provided không, và dòng evidence có chip Expired không? (UC D7: hết hạn chỉ hiện dạng ngày, không phải trạng thái; Figma Documents lại có chip Expired và Expires soon) | Assisted workspace_051 |
| Q-EA-15 | Requirement có yêu cầu làm rõ đang mở (Gap Analysis) thì hiện ở khu vực nào của chi tiết requirement? (UC EVA-02: “open clarifications (GAP-03)”; Figma, hệ thống không có) | Assisted workspace_039 |
| Q-EA-16 | Valid from có điền sẵn ngày hôm nay không? (Figma hộp thoại Upload điền sẵn Valid from “20 Sep 2026”, hệ thống để trống; UC không nêu) | Assisted workspace_054 |
| Q-EA-17 | Ô Name điền sẵn từ tên file thế nào (bỏ đuôi file, thay dấu gạch bằng khoảng trắng hay giữ nguyên)? (UC EVA-03: “titles from file names”; Figma ô Name ghi “AD inactive account policy – screenshot” cho file ad-inactive-accounts.png) | Assisted workspace_055 |
| Q-EA-18 | Hộp thoại Upload chọn nhiều file thì hiện thế nào (mỗi file một dòng với ô Name riêng hay chung)? (UC EVA-03 và D21: nhiều file một lần, title từ tên file, metadata dùng chung; Figma chỉ có một dòng file và một ô Name) | Assisted workspace_056 |
| Q-EA-19 | Câu báo lỗi khi bỏ trống File và Name có đúng văn bản chính thức không? (hệ thống: “Choose a file.” và “Enter a name.”; UC D8 chỉ ghi không lưu được khi thiếu; Figma không có trạng thái lỗi) | Assisted workspace_057 |
| Q-EA-20 | Name có giới hạn độ dài không? (UC D8 chỉ ghi Name bắt buộc) | Assisted workspace_061 |
| Q-EA-21 | File đúng 20 MB có được nhận không (1 MB là 1.048.576 hay 1.000.000 byte)? (Figma ghi “Any file type · up to 20 MB”; UC, hệ thống không nêu) | Assisted workspace_063 |
| Q-EA-22 | File 0 KB và file thực thi (.exe) có được tải lên không? (Figma ghi “Any file type”; UC EVC-07: quét mã độc trước khi dùng) | Assisted workspace_065 |
| Q-EA-23 | Valid until trước Valid from thì có báo lỗi không? (UC, Figma, hệ thống chưa nêu) | Assisted workspace_067 |
| Q-EA-24 | Ô “Also use for” chọn được nhiều requirement không, và có liệt kê requirement ngoài tier không? (Figma ghi “Other requirements in this workspace”, một giá trị; UC không nêu) | Assisted workspace_068 |
| Q-EA-25 | Trạng thái Scanning, Blocked, Scan failed hiện ở đâu trên dòng evidence? (UC EVA-07 và EVC-07: quét trước khi dùng; Figma chỉ có “Scanning for viruses…” trong hộp thoại và “scanned, clean” ở chi tiết) | Assisted workspace_076, Assisted workspace_077, Assisted workspace_078 |
| Q-EA-26 | Upload lại đúng file đã có (cùng nội dung) cho requirement khác thì hệ thống xử lý thế nào? (UC EVC-04: file giống hệt bị từ chối khi thêm version; EVA-03 chưa nêu) | Assisted workspace_080 |
| Q-EA-27 | Danh sách Link existing evidence chỉ gồm evidence của workspace này, hay của cả scope (gồm evidence Not mapped upload từ Evidence Library)? (Figma ghi “Evidence already in this workspace” và Documents ghi “Each file belongs to one workspace”; UC EVC-09 gắn evidence với scope, EVA-04 ghi “Library doc”) | Assisted workspace_089 |
| Q-EA-28 | Ô “Search evidence” tìm theo tên evidence hay cả tên file? (Figma, hệ thống chỉ có ô tìm kiếm) | Assisted workspace_085 |
| Q-EA-29 | Nút xác nhận hiện thế nào khi chọn nhiều evidence (“Link 2 items”?), và requirement một expected evidence có hai file thì dòng đếm “1 mandatory item · 1 provided” có đổi không? (Figma, hệ thống chỉ có “Link 1 item”) | Assisted workspace_084 |
| Q-EA-30 | Khi không còn evidence nào để chọn thì hiện câu gì? (hệ thống hiện “Every file of this workspace is already linked here.” cả khi workspace chưa có evidence nào; Figma chưa có trạng thái này) | Assisted workspace_090 |
| Q-EA-31 | Có hộp thoại xác nhận trước khi gỡ liên kết không? (hệ thống gỡ ngay; UC EVA-05 chỉ ghi “The document stays in the library”; Figma chưa có) | Assisted workspace_095, Assisted workspace_096, Assisted workspace_097, Assisted workspace_098, Assisted workspace_100 |
| Q-EA-32 | Evidence không còn gắn requirement nào được gọi là “Not mapped” hay “Not linked”, ở Evidence Library (chip, tab) và ở dòng phụ trong danh sách Link? (UC EVA-07 và EVC-09: Not mapped; Figma Documents: chip và tab “Not linked”; hệ thống: “Not linked to any requirement” ở Library, “not linked yet” ở danh sách Link) | Assisted workspace_087, Assisted workspace_098 |
| Q-EA-33 | Chi tiết requirement có ô Owner không và chưa gán thì hiện gì? (UC EVA-06 có gán owner, hệ thống có ô Owner ghi “Nobody yet”; Figma Workspace / Requirement không có ô Owner) | Assisted workspace_038, Assisted workspace_101, Assisted workspace_102, Assisted workspace_103, Assisted workspace_104, Assisted workspace_105, Assisted workspace_106, Assisted workspace_107, Assisted workspace_115, Assisted workspace_121, Assisted workspace_126 |
| Q-EA-34 | Danh sách Owner có người Customer Viewer không? (UC EVA-06 ghi “The owner must have access to the scope”; hệ thống chỉ liệt kê người có quyền vào scope) | Assisted workspace_103 |
| Q-EA-35 | Dữ liệu requirement retired tạo ở đâu và hiện thế nào trong workspace đã có từ trước? (UC WSP-06; Figma, hệ thống chưa có framework có requirement retired) | Assisted workspace_111 |
| Q-EA-36 | Workspace đã Archive hiện thế nào khi mở: nút Upload, Link, Gỡ, ô Owner bị ẩn hay vô hiệu, có dòng thông báo chỉ đọc không? (UC WSP-04 “Make the workspace read-only”; Figma, hệ thống chưa có workspace Archived) | Assisted workspace_112, Assisted workspace_113, Assisted workspace_114, Assisted workspace_115 |
| Q-EA-37 | Mở workspace của scope mà người dùng không được gán thì hiện trang gì? (hệ thống hiện “This workspace doesn't exist” / “It may have been removed, or it belongs to an organisation you can't see.” cho Customer User; Figma chưa có) | Assisted workspace_127 |
| Q-EA-38 | Ô tìm kiếm của cây requirement có phân biệt chữ hoa, chữ thường không? (hệ thống không phân biệt; UC, Figma không nêu) | Assisted workspace_023 |
| Q-EA-39 | Câu “No matching requirements” / “Try another search or filter.” có đúng văn bản chính thức không? (chỉ lấy từ hệ thống; Figma chưa có trạng thái không có kết quả) | Assisted workspace_024 |
| Q-EA-40 | Evidence gắn từ ô “Also use for” vào expected evidence nào của requirement kia, khi requirement đó có nhiều expected evidence? (Figma ghi “Other requirements in this workspace”; UC không nêu) | Assisted workspace_075 |
| Q-EA-41 | Kiểm tra Blocked và Scan failed bằng scanner thật hay bằng file mẫu nào (vd file thử EICAR)? (UC EVC-07: scanner adapter còn chờ CrowdStrike; hệ thống chưa có cách tạo file bị chặn) | Assisted workspace_077, Assisted workspace_078, Assisted workspace_079, Assisted workspace_088 |
| Q-EA-42 | Bỏ chọn owner (về lại “Nobody yet”) được không? (UC EVA-06 chỉ ghi gán owner; Figma, hệ thống chưa nêu) | Assisted workspace_106 |
| Q-EA-43 | Nút Link khi chưa chọn evidence nào là nút xám không bấm được hay bị ẩn? (hệ thống: xám; Figma chỉ có trạng thái “Link 1 item”) | Assisted workspace_082 |
| Q-EA-44 | Dung lượng file ở dòng file hiển thị thế nào với file cỡ MB (19,99 MB, 19.99 MB hay 20.0 MB)? (Figma chỉ có “402 KB”) | Assisted workspace_062 |
| Q-EA-45 | Nhóm 1 Access Control của Appendix 10 · 2022 · Medium có bao nhiêu requirement: 11 như hệ thống hay 6 dòng với 58% như Figma frame Workspace / Requirement? (hai nguồn lệch nhau) | Assisted workspace_011, Assisted workspace_012, Assisted workspace_013, Assisted workspace_013, Assisted workspace_072, Assisted workspace_093 |
| Q-EA-46 | Workspace tier High của Appendix 10 · 2022 có 76 requirement không? (76 lấy từ sheet Frameworks; hệ thống chưa có workspace High, Figma không có) | Assisted workspace_110 |
| Q-EA-47 | Requirement có tính Provided khi evidence còn Scanning, Blocked hoặc Scan failed không? (UC EVA-07, EVC-07: quét trước khi dùng; UC không nói rõ chip của requirement) | Assisted workspace_079 |
| Q-EA-48 | Trường “source” trong UC EVA-02 (“Text, tier, source, owner, expected evidence and linked documents”) là trường nào và hiện ở đâu? (nhãn “from Basic” là tier; Figma, hệ thống không có trường khác) | Assisted workspace_040 |
| Q-EA-49 | Name chỉ có khoảng trắng có bị coi là trống không? (UC D8 chỉ ghi Name bắt buộc) | Assisted workspace_060 |
| Q-EA-50 | File lớn hơn 20 MB bị chặn lúc chọn file hay lúc bấm Upload, và báo lỗi gì? (Figma ghi “up to 20 MB”; UC, hệ thống không nêu thông báo) | Assisted workspace_064 |
| Q-EA-51 | Thông báo sau khi gỡ liên kết ghi gì? (hệ thống báo “Mapping removed from 4.1. The file stays in your library.”; UC, Figma không nêu) | Assisted workspace_099 |
| Q-EA-52 | Partial có được tính vào phần trăm của nhóm không, và tính bao nhiêu? (Figma: nhóm Access Control 58% khớp công thức Provided tính 1, Partial tính 0,5 chia 6 requirement của frame, số requirement này lệch hệ thống: xem Q-EA-45; phần trăm workspace 38/61 = 62% chỉ đếm Provided) | Assisted workspace_013 |
| Q-EA-53 | Nhãn “from <tier>” hiện thế nào với requirement của framework không có tier (vd ISO/IEC 27001)? (Figma, hệ thống chỉ có “from Basic”) | Assisted workspace_036 |
| Q-EA-54 | Tìm evidence trong hộp thoại Link mà không có kết quả thì hiện gì? (Figma, hệ thống chưa nêu) | Assisted workspace_086 |
| Q-EA-55 | Ô tìm kiếm của cây requirement tìm theo những trường nào ngoài mã và tên requirement (mô tả, tên nhóm)? (UC EVA-01 chỉ ghi “search and filter”; hệ thống tìm được theo mã và tên) | Assisted workspace_022 |
| Q-EA-56 | Customer User và Customer Viewer thấy ô Owner ở trạng thái nào (xám, ẩn, chỉ chữ)? (UC EVA-06 chỉ Customer Admin gán owner; hệ thống: ô xám, không mở được danh sách; Figma không có ô Owner) | Assisted workspace_120, Assisted workspace_125 |
| Q-EA-57 | Người đang là owner của requirement bị gỡ quyền vào scope thì ô Owner hiện gì (giao lại cho ai hay bỏ trống)? (UC D43: giao lại hoặc bỏ trống, chưa nói giao cho ai; thao tác gỡ quyền thuộc sheet Users, Scopes) | Assisted workspace_107 |

## 2. Bảng đổi mã (đọc trước khi trả lời theo mã của bản cũ)

| Mã | Bản 1.13 | Bản 1.14 | Bản 1.15 (hiện hành) |
|---|---|---|---|
| Q-EA-03 | Partial khi nào, và có tính vào % nhóm không | như 1.13 | chỉ còn “Partial khi nào”; vế % nhóm thành Q-EA-52 |
| Q-EA-06 | Trường tìm kiếm, bộ lọc kết hợp từ khoá, chữ hoa | bỏ vế chữ hoa | chỉ còn “lọc và từ khoá áp cùng lúc”; vế trường tìm kiếm thành Q-EA-55 |
| Q-EA-08 | Nhãn from <tier> với Medium/High và với framework không tier | như 1.13 | chỉ còn Medium/High; framework không tier thành Q-EA-53 |
| Q-EA-16 | Valid from điền sẵn; Valid until trước Valid from | chỉ còn Valid from điền sẵn | như 1.14 |
| Q-EA-20 | Độ dài Name; Name chỉ khoảng trắng | như 1.13 | chỉ còn độ dài Name; vế khoảng trắng thành Q-EA-49 |
| Q-EA-21 | File đúng 20 MB; thông báo khi lớn hơn 20 MB | như 1.13 | chỉ còn file đúng 20 MB; vế lớn hơn 20 MB thành Q-EA-50 |
| Q-EA-24 | Nhiều requirement; ngoài tier; gắn vào expected evidence nào | bỏ vế “expected evidence nào” (thành Q-EA-40) | như 1.14 |
| Q-EA-25 | Hiện ở đâu; Provided khi chưa quét; test bằng scanner nào | chỉ còn “hiện ở đâu” (hai vế kia thành Q-EA-47, 41) | như 1.14 |
| Q-EA-27 | 4 câu về danh sách Link (Not mapped, đã gắn, Blocked/Scanning, workspace hay scope) | chỉ còn “workspace hay scope” | như 1.14 |
| Q-EA-28 | Tìm theo tên hay tên file; không có kết quả | như 1.13 | chỉ còn “tên hay tên file”; vế không có kết quả thành Q-EA-54 |
| Q-EA-31 | Hộp thoại xác nhận khi gỡ; thông báo sau khi gỡ | như 1.13 | chỉ còn hộp thoại xác nhận; vế thông báo thành Q-EA-51 |
| Q-EA-32 | Not mapped hay Not linked ở Library | gộp thêm vế dòng phụ trong danh sách Link (Q-EA-38 cũ) | như 1.14 |
| Q-EA-34 | Viewer trong danh sách Owner; bỏ owner; thông báo | chỉ còn “Viewer trong danh sách” | như 1.14 (bỏ owner là Q-EA-42) |
| Q-EA-38 | Dòng phụ Not mapped/Not linked trong danh sách Link | chữ hoa ở ô tìm kiếm (mã dùng lại) | như 1.14 |

Mã mới ở bản 1.15: Q-EA-49 → 57. Mã mới ở bản 1.14: Q-EA-40 → 48.

## 3. Ý chưa thành câu hỏi

- Thông báo gửi cho người được gán owner: UC EVA-06 không nói, chưa có căn cứ để đặt câu hỏi hay case; ghi ở khung case cha mục 4.
