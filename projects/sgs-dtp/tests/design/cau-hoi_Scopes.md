# Câu hỏi mở của sheet Scopes

- Sinh bằng `exports/_build/v1.5/make_questions.py` từ `exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx` (bản Hanna sửa, gửi lúc 13:28 ngày 07/10). Số TC và số đếm do script đọc từ file.
- Sheet Scopes: 136 TC, trong đó **76 TC còn câu hỏi mở**, dùng **27 mã** `Q-S`; **4 TC để trống Expected**, số còn lại đã ghi Expected kèm câu hỏi.
- Danh sách có 28 câu. Sheet `Cần xác nhận` của file TC mới có **4 câu** (Q-S-23, Q-S-24, Q-S-26, Q-S-28); 24 câu còn lại chỉ được nhắc ở cột Open question của từng TC, chưa có chỗ nào trong thư mục ghi câu hỏi đầy đủ — file này bù chỗ đó.
- Cột "Câu hỏi" và "Căn cứ" ở mục 2 là bản AI viết ngày 01/10 (Q-S-28: ngày 06/10), dựa trên UC List v2.1, Figma và prototype; mã UC trong đó là mã của v2.1 (vd `SCP-001`). **Chưa soát lại theo UC List v4.** Cột "Ghi nhận" là điều thấy trong các bản file TC ngày 07/10 và trong `tests/design/bo-cuc-sheet_uc-v4.md`.
- Mức do AI xếp, chờ Hanna duyệt: CHẶN là chưa trả lời thì không viết được Expected cho cả một nhóm TC.
- Câu không còn TC nào chờ: Q-S-21.

## 1. Tổng hợp

| Mức | Số câu | Mã | Số TC đang chờ |
|---|---|---|---|
| CHẶN | 6 | 05, 10, 11, 17, 21, 24 | 30 |
| QUAN TRỌNG | 13 | 04, 07, 09, 14, 15, 16, 18, 19, 20, 22, 23, 25, 28 | 30 |
| NHỎ | 9 | 01, 02, 03, 06, 08, 12, 13, 26, 27 | 17 |

TC chờ hai mã cùng lúc: Scope_106; vì vậy tổng cột cuối lớn hơn 76.

## 2. Từng câu hỏi

| Mã · mức | Câu hỏi | Căn cứ ghi ngày 01/10 | TC đang chờ | Ghi nhận |
|---|---|---|---|---|
| **Q-S-01**<br>NHỎ<br>chưa có trong sheet | **Mô tả trang của Customer User.** Customer User thấy mô tả "Scopes assigned to you. Only scopes assigned to you are listed." — đây có phải text chính thức? | Figma Scopes / List chỉ có bản Customer Admin. Prototype đổi mô tả theo vai trò. | Scope_128 | — |
| **Q-S-02**<br>NHỎ<br>chưa có trong sheet | **Tên khách hàng ngắn hay đầy đủ.** Mô tả trang danh sách dùng tên ngắn, dòng phụ màn chi tiết dùng tên pháp lý. Lấy từ hai trường khác nhau có đúng chủ ý? | Danh sách: "The parts of ABC Trading you prepare…". Chi tiết: "Organization scope · ABC Trading Co., Ltd." | Scope_006 | — |
| **Q-S-03**<br>NHỎ<br>chưa có trong sheet | **Nhãn nút có dấu +.** Nhãn chính thức là "Create scope" / "Link framework" hay "+ Create scope" / "+ Link framework"? | Figma không có dấu +. Prototype có dấu +. | Scope_008, Scope_085 | — |
| **Q-S-04**<br>QUAN TRỌNG<br>chưa có trong sheet | **Trường Belongs to khi tạo scope System.** 1) Belongs to organisation bắt buộc hay không? 2) Mỗi trường chọn được một hay nhiều scope? 3) Đổi từ System sang loại khác thì giá trị đã chọn bị bỏ? 4) Figma frame Create scope có hai trường này không? | Prototype: chọn System hiện "Belongs to organisation" (không * , không "(optional)") và "Belongs to product (optional)" mặc định None. UC-SCP-003: "a system may belong to both an organization and a product". | Scope_011, Scope_012 | Bản v1.4: Hanna thêm case tạo scope System bỏ trống cả hai trường Belongs to, cột Belongs to hiện "—" (Scope_040). Phần 1 có câu trả lời theo hệ thống đang chạy (không bắt buộc), chờ SGS xác nhận. Case "System chưa chọn Belongs to organisation" của v1.3 đã được Hanna thay bằng case khác (Scope_019). |
| **Q-S-05**<br>CHẶN<br>chưa có trong sheet | **Kiểm tra dữ liệu khi tạo, sửa, gắn.** Cần text lỗi nguyên văn cho: không chọn Type; bỏ trống Name; bỏ trống What is in scope; chưa chọn Framework; chưa chọn tier. Giới hạn ký tự của Name, What is in scope, What is out of scope. Trùng tên trong tenant: chặn hay cho phép, có phân biệt hoa thường? Name chỉ có khoảng trắng coi là rỗng? Nút gắn bị khoá khi chưa chọn hay bấm được rồi báo lỗi? | UC, Figma và prototype đều không có text lỗi hay giới hạn. | Scope_015 → 021, Scope_076 → 078, Scope_101, Scope_102<br>Expected trống: Scope_021 | Bản v1.4: Hanna điền text lỗi theo hệ thống đang chạy và vẫn giữ câu hỏi: "Choose the type of scope." (Scope_015) · "Enter a name." (Scope_016, 017, 076) · "Describe what is in scope." (Scope_018, 019, 077) · "A scope with this name already exists." (Scope_020, 078). Chưa có: giới hạn ký tự (Scope_021), chưa chọn framework, chưa chọn tier (Scope_101, 102). Câu "UC, Figma và prototype đều không có text lỗi" ở cột căn cứ vì vậy không còn đúng với hệ thống đang chạy. |
| **Q-S-06**<br>NHỎ<br>chưa có trong sheet | **Huỷ khi đang nhập dở.** Đang nhập dở mà bấm Cancel, × hoặc nhấn Esc: đóng ngay hay hỏi xác nhận? | Prototype đóng ngay, kể cả khi nhấn Esc. Thiết kế không ghi. | Scope_022, Scope_024 | Bản v1.4: Hanna điền Expected cho case nhấn Esc (hộp thoại đóng, không tạo scope — Scope_024), vẫn giữ câu hỏi. |
| **Q-S-07**<br>QUAN TRỌNG<br>chưa có trong sheet | **Tìm kiếm.** 1) Tìm theo trường nào (tên, mô tả)? 2) Có phân biệt hoa thường, có dấu? 3) Dòng đếm "&lt;n&gt; scopes" giữ tổng hay đổi theo kết quả? 4) Text khi không có kết quả? | Prototype: không phân biệt hoa thường, tìm chuỗi con trong tên; dòng đếm giữ "4 scopes" trong khi phân trang đổi thành "1–2 of 2 items"; không có kết quả thì hiện "No results for “zzqq”" và "Try a different search term." Figma chưa có trạng thái này. | Scope_030 → 032 | Chiều 07/10: Hanna điền Expected cho case nhập chữ hoa — không phân biệt chữ hoa, chữ thường (Scope_031), vẫn giữ câu hỏi. |
| **Q-S-08**<br>NHỎ<br>chưa có trong sheet | **Sắp xếp.** Thứ tự mặc định khi mở màn là gì? Cột nào sắp xếp được? | Figma không có icon sắp xếp. Prototype chỉ cột Scope sắp được (A→Z, Z→A); mặc định không theo tên. | Scope_054 → 056 | Bản v1.4: Hanna điền thứ tự mặc định là thời gian cũ nhất xuống mới nhất (Scope_054), vẫn giữ câu hỏi. |
| **Q-S-09**<br>QUAN TRỌNG<br>chưa có trong sheet | **Phân trang.** Dùng bản Figma hay bản prototype? Số dòng mỗi trang mặc định là bao nhiêu? | Figma: "1–4 of 4 items · Page 1 of 1", không chọn số dòng. Prototype: "Items per page 10" (10/25/50/100) · "1–4 of 4 items" · "[1] of 1 page" · nút ‹ ›. | Scope_057, Scope_059, Scope_061 | Bản v1.4: Hanna điền theo hệ thống đang chạy và vẫn giữ câu hỏi: mặc định 10 items (Scope_057), chọn giá trị khác thì bảng hiển thị đủ số dòng (Scope_059); thêm case các giá trị 10, 25, 50, 100 items (Scope_058, không kèm câu hỏi). |
| **Q-S-10**<br>CHẶN<br>chưa có trong sheet | **Trạng thái rỗng.** Text tiêu đề, mô tả và nút (nếu có) của màn Scopes khi tenant chưa có scope nào. | Figma có frame Scopes / Empty, AI chưa đối chiếu được text. | Scope_007 | Bản v1.4: Hanna điền text theo hệ thống đang chạy ("Create your first scope" và đoạn mô tả — Scope_007), vẫn giữ câu hỏi. |
| **Q-S-11**<br>CHẶN<br>chưa có trong sheet | **Evidence coverage trong MVP.** 1) MVP có hiển thị độ phủ bằng chứng trên màn Scopes không? 2) Nếu có thì thuộc UC nào, bao nhiêu giờ? 3) Công thức: tổng requirement đã có bằng chứng / tổng requirement của mọi framework, như prototype? Làm tròn thế nào? | Hiện ở 3 chỗ: cột Evidence coverage (danh sách), cột Coverage (khối Frameworks), khối Summary. UC tính và xem chỉ số là RDN-001, RDN-004: 0 giờ, LTS đề xuất Phase 2, SGS chưa ý kiến → [ĐỀ XUẤT LÙI]. SCP-001/002 không nhắc độ phủ. Prototype: Head office 54% = (74+6)/(116+31), không phải trung bình 41,5%. | Scope_035, Scope_049, Scope_051 → 053, Scope_089 → 092, Scope_126 | Bản v1.4: Hanna thêm 6 case có bộ số cụ thể và phép tính cho cột Evidence coverage (Scope_044 → 049); 5 case đầu không kèm câu hỏi. Bản v1.5: AI thêm 3 case biên về làm tròn (Scope_051 → 053) và viết 4 case cột Coverage cùng kiểu (Scope_089 → 092). Chiều 07/10: Hanna điền kết quả cho 3 case biên (12.5% → 13%, 0.4% → 0%, 99.6% → 100%) và cho khối Summary ("Hiển thị thông tin giống khung Frameworks" — Scope_126), vẫn giữ câu hỏi. Cách ghi Expected cho giá trị tính toán chờ Hanna xác nhận (FB-048). `tests/design/bo-cuc-sheet_uc-v4.md` (05/10) ghi UC-RDN-004 đã sang P2 ở UC List v4; sheet Scopes đang có 15 TC trỏ UC-RDN-004. |
| **Q-S-12**<br>NHỎ<br>chưa có trong sheet | **Cột Users đếm những ai.** Số ở cột Users có tính Customer Admin không? Tenant có 3 admin thì scope mới tạo hiện 3? | Prototype: cột Users bằng số dòng ở khối Users, gồm cả dòng "Customer Admin · sees every scope" (Retail loyalty app = 1, chỉ có admin). | Scope_043 | — |
| **Q-S-13**<br>NHỎ<br>chưa có trong sheet | **Scope chưa gắn framework.** Xác nhận text "None linked yet" ở cột Frameworks; cột Evidence coverage hiện "—"; khối Frameworks ở màn chi tiết khi chưa có framework hiển thị gì? | Figma có "None linked yet" cho AI platform. Prototype không có scope nào chưa gắn framework. | Scope_042, Scope_050, Scope_084 | Bản v1.5: AI thêm 2 case — cột Evidence coverage khi scope chưa gắn framework (Scope_050), khối Frameworks khi chưa gắn framework (Scope_084). Chiều 07/10: Hanna điền theo hệ thống đang chạy và vẫn giữ câu hỏi: cột Evidence coverage hiện "—" (Scope_050); khối Frameworks hiện "No framework linked yet. Link one to create a workspace and start collecting evidence." (Scope_084). |
| **Q-S-14**<br>QUAN TRỌNG<br>chưa có trong sheet | **Xoá và lưu trữ scope.** MVP có xoá scope không? Ngoài "Active" scope còn trạng thái nào? | Menu ⋮ chỉ có "Edit scope". SCP-005 Archive: 0 giờ, LTS đề xuất Phase 2. Nhưng WBS ghi "CP-06 CRUD (P1) implies hard delete only" — WBS có tính xoá, không có UC xoá, không có nút xoá. | Scope_062, Scope_067 | — |
| **Q-S-15**<br>QUAN TRỌNG<br>chưa có trong sheet | **Hộp thoại sửa scope.** Hộp thoại Edit scope của prototype có phải thiết kế chính thức? Không cho đổi Type và Belongs to — đúng chủ ý? | SCP-004 có 5 giờ, Figma không có frame sửa. Prototype: Name *, What is in scope *, What is out of scope (optional), Cancel / Save. | Scope_068, Scope_075 | — |
| **Q-S-16**<br>QUAN TRỌNG<br>chưa có trong sheet | **Khoá khi đang có audit.** 1) Quy tắc khoá có đúng không? 2) Một framework đang audit thì sửa scope bị khoá toàn bộ? 3) Gắn thêm framework, gán người dùng có bị khoá? 4) Text chính thức? | Prototype, scope Customer data platform: bấm Edit → "The scope can't be edited while an audit is running."; Change tier → "Tier can't be changed during an audit … Unlinking the framework and editing the scope are blocked for the same reason." Không UC nào ghi quy tắc này. Figma có frame Change tier locked, AI chưa đối chiếu text. | Scope_080, Scope_110 | Chiều 07/10: Hanna chuyển case gắn thêm framework khi scope đang có audit sang nhóm Thành công và bỏ câu hỏi ở TC đó (Scope_104). Phần 3 có câu trả lời theo hệ thống đang chạy (vẫn gắn được), chờ SGS xác nhận. |
| **Q-S-17**<br>CHẶN<br>chưa có trong sheet | **Tier thuộc UC nào.** 1) "obligation level" trong SCP-002 có phải là tier? 2) Đổi tier sau khi gắn thuộc UC nào (SCP-004, SCP-006 hay chưa có)? 3) Framework không phân tier: hộp thoại gắn ẩn phần tier? 4) Hiển thị tier thống nhất thế nào? | Tier có ở cột Tier, hộp thoại Link, hộp thoại Change tier, cột Frameworks của danh sách. Không UC nào nhắc tier. Prototype ghi "Medium · 中" ở bảng Frameworks nhưng "Medium" ở danh sách và Summary. | Scope_087, Scope_100, Scope_106, Scope_109, Scope_111, Scope_112 | `tests/design/bo-cuc-sheet_uc-v4.md` (05/10) ghi: UC List v4 không có UC đổi tier, tier chỉ chọn lúc tạo workspace; 6 TC Đổi tier (Scope_109 → 114) đang ghi [NGOÀI UC]. Chiều 07/10: Hanna điền Expected cho case chọn framework không phân tier — 'Không hiển thị button "Change tier"' (Scope_100), vẫn giữ câu hỏi. |
| **Q-S-18**<br>QUAN TRỌNG<br>chưa có trong sheet | **Số requirement của tier High.** Tier High của Appendix 10 có 79 hay 76 requirement? | Figma (Link framework): Basic 44 · Medium 61 · High 79. Prototype: 44 · 61 · 76, mô tả "Medium + 15 more controls" (61 + 15 = 76). | Scope_099 | — |
| **Q-S-19**<br>QUAN TRỌNG<br>chưa có trong sheet | **Framework đã gắn trong danh sách chọn.** Framework đã gắn vào scope phải ẩn, hiện nhưng khoá, hay cho gắn lần hai (ví dụ khác phiên bản)? | Prototype: Head office đã có ISO/IEC 27001 và ISO 22301, danh sách vẫn liệt kê và chọn được cả hai. | Scope_098 | Chiều 07/10: Hanna điền theo hệ thống đang chạy và vẫn giữ câu hỏi: framework đã gắn vẫn hiện trong danh sách chọn, có thông báo đỏ "… is already linked to this scope." (Scope_098). |
| **Q-S-20**<br>QUAN TRỌNG<br>chưa có trong sheet | **Workspace sau khi gắn framework.** Workspace được tạo ngay hay sau một khoảng? Trạng thái ban đầu là gì? Danh sách đầy đủ các trạng thái? | SCP-006: "triggering workspace creation". Prototype có "Preparing" và "Audit in progress". | Scope_093, Scope_105 → 107 | `tests/design/bo-cuc-sheet_uc-v4.md` (05/10) đề xuất chuyển các TC Gắn framework, Gỡ framework sang sheet Workspaces (nay là Scope_096 → 107); file TC vẫn để ở sheet Scopes. |
| **Q-S-21**<br>CHẶN<br>chưa có trong sheet | **Gỡ framework (SCP-007).** MVP có gỡ framework không? Lối vào ở đâu? Bằng chứng và lịch sử review giữ lại hiển thị ở đâu? | SCP-007 có 8 giờ, WBS: "PRESALE WBS GAP — Unlinking a framework from a scope is not priced". Figma và prototype không có lối vào. Nhưng text khoá audit có nhắc "Unlinking the framework … blocked". | không còn TC nào | Chiều 07/10: Hanna bỏ TC duy nhất của câu này (Scope_108 ở bản v1.5). Câu hỏi vẫn mở. |
| **Q-S-22**<br>QUAN TRỌNG<br>chưa có trong sheet | **Đổi tier và bằng chứng.** Nâng tier: bằng chứng đã tải giữ nguyên? Hạ tier: bằng chứng của requirement bị bỏ ra sao, có cảnh báo? | Figma Change tier: cảnh báo độ phủ giảm khi nâng tier. Hộp thoại Link ghi "You can change the tier later; uploaded evidence stays." Prototype không có dữ liệu để mở hộp thoại đổi tier không khoá. | Scope_113, Scope_114 | Chiều 07/10: Hanna điền Expected cho case hạ tier (Scope_114); nội dung đang giống case nâng tier, cần Hanna xem lại (`so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 3). |
| **Q-S-23**<br>QUAN TRỌNG | **Ai được gán vào scope, thu hồi.** Customer Viewer có được gán? Người đang chờ kích hoạt có được gán? Bỏ tick (thu hồi) có thuộc USR-006, có cần xác nhận? | USR-006: "Grant a Customer User access…". Prototype: danh sách có cả Customer Viewer (Iris Huang) và người "invitation pending"; bỏ tick là thu hồi. | Scope_119, Scope_124, Scope_125<br>Expected trống: Scope_119 | Sheet Cần xác nhận (viết 05/10) ghi: phần "thu hồi có thuộc USR-006 không" đã được UC List v4 trả lời — USR-05 có "Grant or remove". Ô Open question của Scope_124, Scope_125 vẫn còn hỏi phần này. |
| **Q-S-24**<br>CHẶN | **Customer Viewer có vào màn Scopes.** Customer Viewer có vào được màn Scopes không? Thấy những gì? | Actor của SCP-001/002 không có Customer Viewer. RDN-004 có Customer Viewer. Prototype gán được Viewer vào scope. | Scope_131<br>Expected trống: Scope_131 | `tests/design/bo-cuc-sheet_uc-v4.md` (05/10) có cùng câu hỏi theo UC List v4, mặc định ghi ở đó: theo cột Actor(s), Customer Viewer không mở được. |
| **Q-S-25**<br>QUAN TRỌNG<br>chưa có trong sheet | **SGS xem scope của khách.** Lối vào danh sách và chi tiết scope của khách từ SGS Portal nằm ở đâu? | SCP-001/002: SGS roles được phân công xem chỉ đọc, portal "Customer Portal & SGS Portal". Chưa thấy màn tương ứng. | Scope_132, Scope_133 | — |
| **Q-S-26**<br>NHỎ | **Mở scope không tồn tại hoặc không có quyền.** Mở URL chi tiết scope không tồn tại, không được gán, hoặc của tenant khác thì hiển thị gì? | Thiết kế không có màn lỗi cho trường hợp này. | Scope_005, Scope_130, Scope_135 | Bản v1.4: Hanna điền text theo hệ thống đang chạy cho mã scope không tồn tại ("This scope doesn’t exist" và dòng mô tả — Scope_005), vẫn giữ câu hỏi. |
| **Q-S-27**<br>NHỎ<br>chưa có trong sheet | **Ghi audit cho thao tác trên scope.** Tạo, sửa scope, gắn framework, đổi tier, gán người dùng có thuộc diện phải ghi audit? | AUD-001: "sensitive platform, review and service-request actions" — không liệt kê thao tác cụ thể. | Scope_137<br>Expected trống: Scope_137 | — |
| **Q-S-28**<br>QUAN TRỌNG | **In scope / Out of scope ở danh sách.** Danh sách scope có hiển thị What is in scope và What is out of scope của từng scope không? | Hanna yêu cầu kiểm tra cả 4 thông tin (Type, Name, In scope, Out of scope) trên Danh sách sau khi tạo; Figma Screens 05 chỉ có cột Scope (kèm nhãn loại), Belongs to, Frameworks, Users, Evidence coverage. | Scope_025 → 027 | — |

## 3. Nguyên văn ô Open question của từng TC

| Mã | TC | Expected | Ô Open question |
|---|---|---|---|
| Q-S-01 | Scope_128 | đã ghi | Text lấy từ prototype, Figma chỉ có bản Customer Admin → Q-S-01 |
| Q-S-02 | Scope_006 | đã ghi | Mô tả dùng tên ngắn (ABC Trading), màn chi tiết dùng tên đầy đủ (ABC Trading Co., Ltd.) → Q-S-02 |
| Q-S-03 | Scope_008 | đã ghi | Nhãn: Figma 'Create scope', prototype '+ Create scope' → Q-S-03 |
| Q-S-03 | Scope_085 | đã ghi | Nhãn nút: Figma 'Link framework', prototype '+ Link framework' → Q-S-03 |
| Q-S-04 | Scope_011 | đã ghi | Belongs to organisation không có * cũng không ghi (optional) → Q-S-04 |
| Q-S-04 | Scope_012 | đã ghi | Giá trị Belongs to đã chọn có bị bỏ khi đổi loại → Q-S-04 |
| Q-S-05 | Scope_015, Scope_016, Scope_018, Scope_076, Scope_077 | đã ghi | Text lỗi nguyên văn → Q-S-05 |
| Q-S-05 | Scope_017, Scope_019 | đã ghi | Khoảng trắng có bị coi là rỗng → Q-S-05 |
| Q-S-05 | Scope_020 | đã ghi | Chặn hay cho phép trùng tên; có phân biệt hoa thường → Q-S-05 |
| Q-S-05 | Scope_021 | trống | Giới hạn ký tự từng trường → Q-S-05 |
| Q-S-05 | Scope_078 | đã ghi | Chặn hay cho phép trùng tên → Q-S-05 |
| Q-S-05 | Scope_101 | đã ghi | Hiện lỗi hay khoá nút khi chưa chọn; text lỗi → Q-S-05 |
| Q-S-05 | Scope_102 | đã ghi | Hiện lỗi hay khoá nút; text lỗi → Q-S-05 |
| Q-S-06 | Scope_022 | đã ghi | Đang nhập dở có hỏi xác nhận không → Q-S-06 |
| Q-S-06 | Scope_024 | đã ghi | Thiết kế không ghi; prototype đóng hộp thoại ngay → Q-S-06 |
| Q-S-07 | Scope_030 | đã ghi | Dòng đếm có đổi theo kết quả không (prototype giữ nguyên tổng) → Q-S-07 |
| Q-S-07 | Scope_031 | đã ghi | Có phân biệt hoa thường không (prototype không phân biệt) → Q-S-07 |
| Q-S-07 | Scope_032 | đã ghi | Text lấy từ prototype, Figma chưa có trạng thái này → Q-S-07 |
| Q-S-08 | Scope_054 | đã ghi | Mặc định sắp theo gì (prototype không theo tên) → Q-S-08 |
| Q-S-08 | Scope_055, Scope_056 | đã ghi | Figma không có icon sắp xếp → Q-S-08 |
| Q-S-09 | Scope_057 | đã ghi | Figma: 1–4 of 4 items · Page 1 of 1. Prototype: Items per page 10 · 1–4 of 4 items · [1] of 1 page · ‹ › → Q-S-09 |
| Q-S-09 | Scope_059 | đã ghi | Có chọn số dòng không; giá trị 10/25/50/100 theo prototype → Q-S-09 |
| Q-S-09 | Scope_061 | đã ghi | Số dòng mỗi trang mặc định → Q-S-09 |
| Q-S-10 | Scope_007 | đã ghi | Figma có frame Scopes / Empty, chưa đối chiếu được text → Q-S-10 |
| Q-S-11 | Scope_035 | đã ghi | Cột Evidence coverage có trong MVP không → Q-S-11 |
| Q-S-11 | Scope_049 | đã ghi | [ĐỀ XUẤT LÙI] RDN-004 0 giờ, LTS đề xuất Phase 2. Prototype: 54% = (74+6)/(116+31) → Q-S-11 |
| Q-S-11 | Scope_051 | đã ghi | 1/8 × 100 = 12.5%: hiển thị 12% hay 13% (cách làm tròn khi phần thập phân đúng bằng .5) → Q-S-11 |
| Q-S-11 | Scope_052 | đã ghi | 1/250 × 100 = 0.4%: làm tròn như các case trên thì ra 0% dù đã có 1 requirement đủ evidence; hiển thị 0%, 1% hay &lt;1% → Q-S-11 |
| Q-S-11 | Scope_053 | đã ghi | 249/250 × 100 = 99.6%: làm tròn như các case trên thì ra 100% dù còn 1 requirement chưa đủ evidence; hiển thị 100% hay 99% → Q-S-11 |
| Q-S-11 | Scope_089 → 092 | đã ghi | [ĐỀ XUẤT LÙI] RDN-004. Cách tính và làm tròn lấy theo cột Evidence coverage ở danh sách; prototype hiện &lt;%&gt; + thanh tiến trình + &lt;đã có&gt;/&lt;tổng&gt; → Q-S-11 |
| Q-S-11 | Scope_126 | đã ghi | [ĐỀ XUẤT LÙI] RDN-004. Prototype: mỗi framework một dòng %, thanh tiến trình, '&lt;n&gt; of &lt;m&gt; requirements have their mandatory evidence'; ghi chú 'Preparation progress only — not a compliance decision.' → Q-S-11 |
| Q-S-12 | Scope_043 | đã ghi | Có tính Customer Admin không → Q-S-12 |
| Q-S-13 | Scope_042 | đã ghi | Text theo Figma, prototype chưa có dữ liệu để đối chiếu → Q-S-13 |
| Q-S-13 | Scope_050 | đã ghi | Scope chưa gắn framework: cột Evidence coverage hiện —, 0% hay để trống → Q-S-13 |
| Q-S-13 | Scope_084 | đã ghi | Khối Frameworks khi chưa gắn framework hiển thị gì → Q-S-13 |
| Q-S-14 | Scope_062 | đã ghi | Ngoài Active còn trạng thái nào → Q-S-14 |
| Q-S-14 | Scope_067 | đã ghi | Không có Archive, Delete: SCP-005 lùi Phase 2, nhưng WBS CP-06 ghi CRUD → Q-S-14 |
| Q-S-15 | Scope_068 | đã ghi | Figma không có frame sửa scope → Q-S-15 |
| Q-S-15 | Scope_075 | đã ghi | Figma không có frame sửa scope; không cho đổi Type, Belongs to có đúng chủ ý → Q-S-15 |
| Q-S-16 | Scope_080 | đã ghi | Quy tắc và text lấy từ prototype, UC không ghi → Q-S-16 |
| Q-S-16 | Scope_110 | đã ghi | Text lấy từ prototype, chưa đối chiếu frame Change tier locked → Q-S-16 |
| Q-S-17 | Scope_087 | đã ghi | Prototype ghi 'Medium · 中' ở đây nhưng 'Medium' ở danh sách và Summary; tier có phải 'obligation level' của SCP-002 → Q-S-17 |
| Q-S-17 | Scope_100 | đã ghi | Phần chọn tier ẩn đi hay hiện No tiers → Q-S-17 |
| Q-S-17 | Scope_106 | đã ghi | Phần chọn tier ẩn đi hay hiện No tiers → Q-S-17; trạng thái ban đầu của workspace → Q-S-20 |
| Q-S-17 | Scope_109 | đã ghi | Theo Figma, prototype chưa có dữ liệu để mở; đổi tier thuộc UC nào → Q-S-17 |
| Q-S-17 | Scope_111, Scope_112 | đã ghi | Đổi tier thuộc UC nào → Q-S-17 |
| Q-S-18 | Scope_099 | đã ghi | Số requirement tier High: Figma 79, prototype 76 → Q-S-18 |
| Q-S-19 | Scope_098 | đã ghi | Prototype vẫn liệt kê và cho chọn → ẩn, khoá hay cho gắn lần hai → Q-S-19 |
| Q-S-20 | Scope_093 | đã ghi | Danh sách trạng thái đầy đủ → Q-S-20 |
| Q-S-20 | Scope_105 | đã ghi | Trạng thái ban đầu của workspace → Q-S-20 |
| Q-S-20 | Scope_106 | đã ghi | Phần chọn tier ẩn đi hay hiện No tiers → Q-S-17; trạng thái ban đầu của workspace → Q-S-20 |
| Q-S-20 | Scope_107 | đã ghi | Workspace tạo ngay hay sau một khoảng → Q-S-20 |
| Q-S-22 | Scope_113 | đã ghi | Bằng chứng đã tải có giữ nguyên → Q-S-22 |
| Q-S-22 | Scope_114 | đã ghi | Hạ tier có cảnh báo gì; bằng chứng của requirement bị bỏ ra sao → Q-S-22 |
| Q-S-23 | Scope_119 | trống | USR-006 chỉ nói Customer User; prototype có cả Customer Viewer và người chưa kích hoạt → Q-S-23 |
| Q-S-23 | Scope_124 | đã ghi | Thu hồi có thuộc USR-006, có hỏi xác nhận → Q-S-23 |
| Q-S-23 | Scope_125 | đã ghi | Thu hồi có thuộc USR-006 → Q-S-23 |
| Q-S-24 | Scope_131 | trống | SCP-001/002 không có Customer Viewer trong actor, nhưng prototype gán được Viewer vào scope → Q-S-24 |
| Q-S-25 | Scope_132, Scope_133 | đã ghi | Lối vào từ SGS Portal ở đâu → Q-S-25 |
| Q-S-26 | Scope_005 | đã ghi | Hiện trang lỗi, thông báo, hay quay về danh sách → Q-S-26 |
| Q-S-26 | Scope_130, Scope_135 | đã ghi | Hiện trang gì → Q-S-26 |
| Q-S-27 | Scope_137 | trống | Thao tác trên scope có thuộc diện phải ghi audit → Q-S-27 |
| Q-S-28 | Scope_025 → 027 | đã ghi | Danh sách scope có hiển thị What is in scope / What is out of scope không? Yêu cầu của Hanna: kiểm tra cả 4 thông tin trên Danh sách; Figma chỉ có các cột Scope, Belongs to, Frameworks, Users, Evidence coverage → Q-S-28 |

## 4. Cần Hanna chọn

1. Có đưa 24 câu còn thiếu vào sheet `Cần xác nhận` của file TC không? AI chưa đưa, vì căn cứ đang viết theo UC List v2.1 và prototype; nên soát theo UC List v4 trước (file UC List v4 chưa có trong `docs/source`).
2. Các TC Hanna đã điền Expected theo hệ thống đang chạy mà vẫn giữ câu hỏi (xem cột "Ghi nhận"): coi là Expected tạm chờ SGS xác nhận, hay coi là đã có căn cứ và đóng câu hỏi? Liên quan dòng 1 ở `so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 2.
3. Q-S-23: phần "thu hồi có thuộc USR-006 không" được sheet `Cần xác nhận` ghi là đã có trả lời ở UC List v4. Nếu đúng thì sửa ô Open question của Scope_124, Scope_125 (Scope_125 chỉ còn hỏi phần này).
4. Q-S-11: Evidence coverage có kiểm ở giai đoạn này không, khi `bo-cuc-sheet_uc-v4.md` ghi UC-RDN-004 đã sang P2? Góp ý ngày 07/10 yêu cầu thêm TC cho cột này nên file TC đã thêm; cần Hanna xác nhận để biết các TC đó chạy ở giai đoạn nào.
