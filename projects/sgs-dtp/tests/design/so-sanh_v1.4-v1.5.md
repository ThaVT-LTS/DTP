# So sánh v1.4 → v1.5 — sheet Scopes (07/10/2026)

- Bản v1.4: file Hanna gửi ngày 07/10, lưu nguyên ở `exports/SGS-DTP_TestCase1_v1.4.xlsx`.
- Bản v1.5: `exports/SGS-DTP_TestCase1_v1.5.xlsx`; bảng phẳng: `exports/_flat/Scopes_v1.5.tsv`.
- Cách viết rút ra từ phần Hanna sửa: `phan-tich-cach-viet_v1.4.md` (cùng thư mục). Góp ý gốc: FB-042 → FB-049, FB-016 trong `feedback/log.md`.
- Mọi con số dưới đây do script đếm từ hai file.

| | v1.4 | v1.5 |
|---|---|---|
| Số dòng TC | 136 | 137 |
| Dòng có TVP_ID | 127 | 137 |
| TVP_ID trùng | 2 | 0 |
| Dòng thiếu UC | 11 | 0 |
| Ô còn `{{…}}` | 68 | 0 |
| Dòng còn câu hỏi mở | 70 | 78 |
| Dòng để trống Expected | 13 | 16 |

So với v1.4: giữ nguyên 41 dòng · sửa 86 dòng · thêm 10 dòng · bỏ 9 dòng.
Trong đó phần Hanna đã sửa (No. 1–67 của v1.4, dòng 13–69): giữ nguyên 39, sửa 18 (chỉ các chỗ ở mục 1), thêm 4.
Phần viết lại (dòng 70–148 của v1.4): giữ nguyên 2, sửa 68, thêm 6, bỏ 9.

## 1. Phần Hanna đã sửa — những chỗ AI chạm vào

Nội dung của Hanna được giữ. Chỉ sửa chỗ gõ nhầm, chỗ còn `{{…}}`, ô UC còn trống; No. và TVP_ID đánh lại cho cả sheet (mục 5).

| TC (v1.5) | Dòng v1.4 · số cũ | Cột | Trước | Sau | Vì sao |
|---|---|---|---|---|---|
| Scope_006 | dòng 18 · Scope_006 | Expected result | - Breadcrumb: Scopes<br>- Tiêu đề: Scopes<br>- Mô tả: The parts of [tenant.short] you prepare for a framework: the organisation, a product or a system.J18 | - Breadcrumb: Scopes<br>- Tiêu đề: Scopes<br>- Mô tả: The parts of [tenant.short] you prepare for a framework: the organisation, a product or a system. | bỏ chữ J18 dính ở cuối ô Expected |
| Scope_016 | dòng 28 · Scope_015 | Step | 1. Mở màn Scopes<br>2. Mở hộp thoại<br>3. Chọn Organization, nhập Name, để trống What is in scope<br>4. Bấm Create scope | 1. Mở màn Scopes<br>2. Mở hộp thoại<br>3. Chọn Organization, nhập What is in scope, để trống Name<br>4. Bấm Create scope | bước 3 đang trùng case Bỏ trống What is in scope (nhập Name, để trống What is in scope); đặt lại như bản v1.3 |
| Scope_019 | dòng 31 · Scope_016 | Test case name | Kiểm tra tạo scope khi Name chỉ có khoảng trắng | Kiểm tra tạo scope khi What is in scope chỉ có khoảng trắng | tên case đang trùng case Name chỉ có khoảng trắng |
| Scope_019 | dòng 31 · Scope_016 | Open question | Trường này bắt buộc hay không → Q-S-04 | Khoảng trắng có bị coi là rỗng → Q-S-05 | câu hỏi cũ ("Trường này bắt buộc hay không → Q-S-04") là của case System chưa chọn Belongs to organisation đã bỏ |
| Scope_026 | dòng 38 · Scope_022 | Open question | Khối Frameworks khi chưa gắn framework hiển thị gì → Q-S-13 | Danh sách scope có hiển thị What is in scope / What is out of scope không? Yêu cầu của Hanna: kiểm tra cả 4 thông tin trên Danh sách; Figma chỉ có các cột Scope, Belongs to, Frameworks, Users, Evidence coverage → Q-S-28 | câu hỏi cũ ("Khối Frameworks khi chưa gắn framework hiển thị gì → Q-S-13") là của case màn chi tiết đã bỏ; đặt câu Q-S-28 như hai case Organization, System; câu Q-S-13 chuyển xuống case trạng thái rỗng của khối Frameworks |
| Scope_027 | dòng 39 · Scope_025 | Step | 1. Mở màn Scopes<br>2. Bấm nút tạo scope để mở hộp thoại Create scope<br>3. Chọn Type: System<br>4. Nhập<br>- Name: abc<br>- What is in scope: abc<br>- What is out of scope (optional): abc<br>5. Chọn<br>- Belongs to organisation: [Organisation]<br>- Belongs to product (optional): [Production]<br>6. Bấm Create scope, tạo thành công<br>7. Kiểm tra dòng vừa tạo trong danh sách | 1. Mở màn Scopes<br>2. Bấm nút tạo scope để mở hộp thoại Create scope<br>3. Chọn Type: System<br>4. Nhập<br>- Name: abc<br>- What is in scope: abc<br>- What is out of scope (optional): abc<br>5. Chọn<br>- Belongs to organisation: [Organization]<br>- Belongs to product (optional): [Product]<br>6. Bấm Create scope, tạo thành công<br>7. Kiểm tra dòng vừa tạo trong danh sách | tên trong ngoặc vuông theo tin nhắn 07/10: [Organization], [Product] |
| Scope_027 | dòng 39 · Scope_025 | Expected result | - Hộp thoại đóng, tạo thành công<br>- Danh sách có dòng với<br>+ Name: abc<br>+ Nhãn loại: Product<br>- Cột Belongs to: [Organisation], [Production]<br>- Dòng đếm tăng 1 | - Hộp thoại đóng, tạo thành công<br>- Danh sách có dòng với<br>+ Name: abc<br>+ Nhãn loại: System<br>- Cột Belongs to: [Organization], [Product]<br>- Dòng đếm tăng 1 | case System đang ghi Nhãn loại: Product; tên trong ngoặc vuông theo tin nhắn 07/10 |
| Scope_030 | dòng 42 · Scope_033 | Step | 1. Mở màn Scopes<br>2. Nhập {{text.partial}} vào ô tìm kiếm | 1. Mở màn Scopes<br>2. Nhập [từ khóa] là một phần tên scope vào ô tìm kiếm | thay {{text.partial}} |
| Scope_030 | dòng 42 · Scope_033 | Expected result | - Bảng chỉ còn các scope có tên chứa {{text.partial}}<br>- Dòng phân trang cập nhật theo số kết quả, ví dụ 1–2 of 2 items | - Bảng chỉ còn các scope có tên chứa [từ khóa]<br>- Dòng phân trang cập nhật theo số kết quả, ví dụ 1–2 of 2 items | thay {{text.partial}} |
| Scope_031 | dòng 43 · Scope_034 | Step | 1. Mở màn Scopes<br>2. Nhập {{text.partial_upper}} vào ô tìm kiếm | 1. Mở màn Scopes<br>2. Nhập [từ khóa] viết hoa vào ô tìm kiếm | thay {{text.partial_upper}} |
| Scope_032 | dòng 44 · Scope_035 | Step | 1. Mở màn Scopes<br>2. Nhập {{text.nomatch}} vào ô tìm kiếm | 1. Mở màn Scopes<br>2. Nhập [từ khóa] không khớp tên scope nào vào ô tìm kiếm | thay {{text.nomatch}} |
| Scope_032 | dòng 44 · Scope_035 | Expected result | - Bảng và dòng phân trang ẩn<br>- Thông báo: No results for “{{text.nomatch}}”<br>- Dòng phụ: Try a different search term. | - Bảng và dòng phân trang ẩn<br>- Thông báo: No results for “[từ khóa]”<br>- Dòng phụ: Try a different search term. | thay {{text.nomatch}} |
| Scope_033 | dòng 45 · Scope_036 | Step | 1. Mở màn Scopes<br>2. Nhập {{text.sql}} vào ô tìm kiếm | 1. Mở màn Scopes<br>2. Nhập ' OR 1=1 -- vào ô tìm kiếm | thay {{text.sql}} bằng chuỗi cụ thể |
| Scope_038 | dòng 50 · Scope_041 | UC | (trống) | UC-SCP-001 | ô trống, điền theo case cùng nhóm |
| Scope_039 | dòng 51 · chưa có ID | UC | (trống) | UC-SCP-001 | ô trống, điền theo case cùng nhóm |
| Scope_040 | dòng 52 · Scope_042 | UC | (trống) | UC-SCP-001 | ô trống, điền theo case cùng nhóm |
| Scope_044 | dòng 56 · chưa có ID | UC | (trống) | UC-RDN-004 | ô trống, điền theo case cùng nhóm |
| Scope_045 | dòng 57 · chưa có ID | UC | (trống) | UC-RDN-004 | ô trống, điền theo case cùng nhóm |
| Scope_046 | dòng 58 · chưa có ID | UC | (trống) | UC-RDN-004 | ô trống, điền theo case cùng nhóm |
| Scope_047 | dòng 59 · chưa có ID | Expected result | - Hiển thị Evidence coverage = 0/101 × 100 = 0% | - Hiển thị Evidence coverage = 0/147 × 100 = 0% | 116 + 31 = 147; số 101 là của case phía trên |
| Scope_047 | dòng 59 · chưa có ID | UC | (trống) | UC-RDN-004 | ô trống, điền theo case cùng nhóm |
| Scope_048 | dòng 60 · chưa có ID | UC | (trống) | UC-RDN-004 | ô trống, điền theo case cùng nhóm |
| Scope_058 | dòng 66 · chưa có ID | UC | (trống) | UC-SCP-001 | ô trống, điền theo case cùng nhóm |

Chưa sửa, để Hanna xem (không phải lỗi gõ rõ ràng):

- Scope_003 (dòng 15 của v1.4): ô IV ghi "Bấm tên scope" nhưng Step chỉ có "1. Vào màn hình Scopes", chưa có bước bấm tên scope.
- Scope_025, Scope_026, Scope_027 (3 case Thành công của Tạo scope) đều tạo `Name: abc`; theo Scope_020 (Trùng tên) thì lần tạo thứ hai sẽ bị chặn với "A scope with this name already exists." Cần tên khác nhau cho ba case, hoặc ghi rõ dữ liệu được dọn giữa các case.
- Scope_025 và Scope_026 cùng tên case "Kiểm tra thông tin vừa tạo"; Scope_027 tên "Kiểm tra scope System vừa tạo hiện ở danh sách".
- Scope_035 (Tiêu đề cột) còn ghi 5 cột trên một dòng nối bằng " · "; phần viết lại bên dưới ghi mỗi mục một dòng (rule 12).
- 6 case Evidence coverage của Hanna (Scope_044 → Scope_049) có tên tiếng Anh; các case khác tên tiếng Việt.
- 5 case Evidence coverage Hanna thêm (Scope_044 → Scope_048) chưa có câu hỏi ở cột Open question; công thức lấy theo prototype, câu Q-S-11 chưa có trả lời (xem FB-048).

## 2. Case thêm — đề xuất của AI, chờ Hanna duyệt

| TC (v1.5) | Khu vực ▸ nhóm ▸ case | Tên case | Expected | Vì sao thêm |
|---|---|---|---|---|
| Scope_050 | Bảng danh sách - Table ▸ Hiển thị ▸ Cột Evidence coverage | Kiểm tra Evidence coverage khi scope chưa gắn framework nào | để trống, có câu hỏi | case biên: không có framework nào để tính |
| Scope_051 | Bảng danh sách - Table ▸ Hiển thị ▸ Cột Evidence coverage | Kiểm tra Evidence coverage khi phần thập phân đúng bằng .5 | để trống, có câu hỏi | case biên: hai case làm tròn phía trên (35.56 → 36, 53.47 → 53) chưa cho biết .5 làm tròn về đâu |
| Scope_052 | Bảng danh sách - Table ▸ Hiển thị ▸ Cột Evidence coverage | Kiểm tra Evidence coverage khi kết quả trên 0% và dưới 0.5% | để trống, có câu hỏi | case biên: 0% trong khi đã có evidence |
| Scope_053 | Bảng danh sách - Table ▸ Hiển thị ▸ Cột Evidence coverage | Kiểm tra Evidence coverage khi kết quả từ 99.5% đến dưới 100% | để trống, có câu hỏi | case biên: 100% trong khi chưa đủ |
| Scope_084 | Khối Frameworks - Frameworks ▸ Trạng thái rỗng ▸ Chưa gắn framework | Kiểm tra khối Frameworks khi scope chưa gắn framework | để trống, có câu hỏi | câu Q-S-13 trước nằm nhờ ở case tạo scope (dòng 38 của v1.4); đưa về đúng khối |
| Scope_088 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Tier | Kiểm tra cột Tier của framework không phân tier | - Hiển thị: No tiers | tách từ case Cột Tier của v1.4 (dòng 96): mỗi loại framework một case |
| Scope_090 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Coverage | Kiểm tra cột Coverage khi kết quả phải làm tròn xuống | - Hiển thị Coverage = 6/31 × 100 = 19.35% → 19% | thêm theo góp ý 07/10: giá trị tính toán cần nhiều case |
| Scope_091 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Coverage | Kiểm tra cột Coverage khi chưa requirement nào đủ evidence | - Hiển thị Coverage = 0/78 × 100 = 0% | thêm theo góp ý 07/10: giá trị tính toán cần nhiều case |
| Scope_092 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Coverage | Kiểm tra cột Coverage khi mọi requirement đều đủ evidence | - Hiển thị Coverage = 61/61 × 100 = 100% | thêm theo góp ý 07/10: giá trị tính toán cần nhiều case |
| Scope_106 | Gắn framework - Link framework ▸ Thành công ▸ Framework không phân tier | Kiểm tra gắn framework không phân tier | - Hộp thoại đóng<br>- Bảng Frameworks có thêm dòng [Framework] · &lt;phiên bản&gt;<br>- Cột Tier của dòng đó: No tiers | thêm: mỗi loại framework một case Thành công, như 3 case theo Type ở Tạo scope |

## 3. Case bỏ

| Dòng v1.4 · số cũ | Khu vực ▸ nhóm ▸ case | Tên case | Vì sao bỏ |
|---|---|---|---|
| dòng 89 · Scope_071 | Sửa scope - Edit scope ▸ Thành công ▸ Đổi Name — Overview của scope con | Kiểm tra tên mới ở Overview của scope con | Hệ quả suy ra (tên mới ở Overview của scope con), không có căn cứ trực tiếp ở UC hay Figma; nơi hiển thị này đã có khu vực Tổng quan ▸ Scope System (FB-042, FB-044) |
| dòng 90 · Scope_072 | Sửa scope - Edit scope ▸ Thành công ▸ Đổi Name — cột Belongs to | Kiểm tra tên mới ở cột Belongs to của danh sách | Hệ quả suy ra (tên mới ở cột Belongs to của danh sách); nơi hiển thị này đã có khu vực Bảng danh sách ▸ Cột Belongs to (FB-042, FB-044) |
| dòng 109 · Scope_091 | Gắn framework - Link framework ▸ Thành công ▸ Hiện ở danh sách Scopes | Kiểm tra framework vừa gắn hiện ở cột Frameworks của danh sách | Nơi hiển thị đã có case riêng: Bảng danh sách ▸ Cột Frameworks — đã gắn (FB-044) |
| dòng 111 · Scope_093 | Gắn framework - Link framework ▸ Thành công ▸ Hiện ở khối Summary | Kiểm tra framework vừa gắn hiện ở khối Summary | Nơi hiển thị đã có case riêng: Tổng hợp ▸ Evidence coverage; case này để trống Expected (FB-044) |
| dòng 127 · Scope_109 | Gán người dùng - Assign users ▸ Thành công ▸ Tick thêm — cột Users ở danh sách | Kiểm tra cột Users ở danh sách sau khi gán | Nơi hiển thị đã có case riêng: Bảng danh sách ▸ Cột Users, so số ở cột với số dòng ở khối Users (FB-044) |
| dòng 138 · Scope_120 | Customer User ▸ API ▸ Tạo scope | Kiểm tra Customer User gọi API tạo scope | Case gọi API: profile.md ghi Tester không được gọi API, không viết ở sheet màn hình (FB-039, rule 29) |
| dòng 139 · Scope_121 | Customer User ▸ API ▸ Sửa, gắn framework, gán người dùng | Kiểm tra Customer User gọi API sửa scope, gắn framework, gán người dùng | Case gọi API (FB-039, rule 29) |
| dòng 145 · Scope_127 | Cách ly tenant - Tenant isolation ▸ API ▸ Chi tiết scope tenant khác | Kiểm tra gọi API chi tiết scope của tenant khác | Case gọi API (FB-039, rule 29) |
| dòng 146 · Scope_128 | Cách ly tenant - Tenant isolation ▸ API ▸ Gán người của tenant khác | Kiểm tra gán người dùng của tenant khác vào scope | Case gọi API; trên giao diện không có thao tác gán người của tenant khác (FB-039, rule 29) |

Muốn giữ case nào thì báo, AI thêm lại ở đúng khu vực hiển thị của nó.

## 4. Phần viết lại (từ Chi tiết scope trở xuống) — từng TC

Cột đổi: III = nhóm kết quả · IV = case · Name · Pre = Pre-condition · Step · Exp = Expected result · OQ = Open question.

| TC (v1.5) | Số cũ (v1.4) | Khu vực ▸ nhóm ▸ case | Loại | Cột đổi | Ghi chú |
|---|---|---|---|---|---|
| Scope_062 | Scope_054 | Phần đầu - Header ▸ Hiển thị ▸ Các thành phần | sửa | Step |  |
| Scope_063 | chưa có ID | Phần đầu - Header ▸ Hiển thị ▸ Dòng phụ theo loại | sửa | UC |  |
| Scope_064 | chưa có ID | Phần đầu - Header ▸ Hiển thị ▸ Dòng phụ theo loại | sửa | UC |  |
| Scope_065 | Scope_055 | Phần đầu - Header ▸ Hiển thị ▸ Dòng phụ theo loại | giữ | — |  |
| Scope_066 | Scope_056 | Phần đầu - Header ▸ Nút quay lại ▸ Bấm ← | sửa | Step |  |
| Scope_067 | Scope_057 | Phần đầu - Header ▸ Menu ⋮ ▸ Các mục | sửa | Step |  |
| Scope_068 | Scope_058 | Phần đầu - Header ▸ Menu ⋮ ▸ Bấm Edit scope | sửa | Step, Exp | Expected bỏ câu trỏ sang chỗ khác ("giống khi bấm nút Edit ở khối Overview") |
| Scope_069 | Scope_059 | Điều hướng trong màn - Section nav ▸ Hiển thị ▸ Ba mục | sửa | Step, Exp |  |
| Scope_070 | Scope_060 | Điều hướng trong màn - Section nav ▸ Bấm mục ▸ Frameworks, Users | sửa | Step, Exp | Expected đang ghi Bước 1, Bước 2 trong khi thao tác ở bước 2, bước 3 |
| Scope_071 | Scope_061 | Tổng quan - Overview ▸ Hiển thị ▸ Scope Organization | sửa | Pre, Step, Exp | ô tô vàng ở v1.4; thông tin của scope ghi từng dòng, dữ liệu trong ngoặc vuông |
| Scope_072 | Scope_062 | Tổng quan - Overview ▸ Hiển thị ▸ Scope Product | sửa | Pre, Exp | ô tô vàng ở v1.4 |
| Scope_073 | Scope_063 | Tổng quan - Overview ▸ Hiển thị ▸ Scope System | sửa | Pre, Exp |  |
| Scope_074 | Scope_064 | Tổng quan - Overview ▸ Hiển thị ▸ Trường không có dữ liệu | sửa | Pre, Step |  |
| Scope_075 | Scope_065 | Sửa scope - Edit scope ▸ Mở hộp thoại ▸ Bấm Edit | sửa | Step, Exp |  |
| Scope_076 | Scope_066 | Sửa scope - Edit scope ▸ Không thành công ▸ Xoá trống Name | sửa | III, Step | từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công |
| Scope_077 | Scope_067 | Sửa scope - Edit scope ▸ Không thành công ▸ Xoá trống What is in scope | sửa | III, Step | từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công |
| Scope_078 | Scope_068 | Sửa scope - Edit scope ▸ Không thành công ▸ Trùng tên scope khác | sửa | III, Step | từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công; ô Step tô vàng ở v1.4 |
| Scope_079 | Scope_074 | Sửa scope - Edit scope ▸ Không thành công ▸ Bấm Cancel | sửa | Step |  |
| Scope_080 | Scope_075 | Sửa scope - Edit scope ▸ Không thành công ▸ Scope đang có audit | sửa | Pre, Step, Exp |  |
| Scope_081 | Scope_069 | Sửa scope - Edit scope ▸ Thành công ▸ Đổi Name — tiêu đề chi tiết | sửa | Step, Exp | ô Step tô vàng ở v1.4 |
| Scope_082 | Scope_070 | Sửa scope - Edit scope ▸ Thành công ▸ Đổi Name — danh sách | sửa | Pre, Step, Exp | ô Step tô vàng ở v1.4; thao tác đổi tên đưa từ Pre-condition vào Step để case tự chạy được |
| Scope_083 | Scope_073 | Sửa scope - Edit scope ▸ Thành công ▸ Sửa In scope, Out of scope | sửa | Step, Exp |  |
| Scope_084 | — | Khối Frameworks - Frameworks ▸ Trạng thái rỗng ▸ Chưa gắn framework | thêm | — | xem mục 2 |
| Scope_085 | Scope_076 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Tiêu đề khối và cột | sửa | Step, Exp |  |
| Scope_086 | Scope_077 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Framework · version | sửa | Step |  |
| Scope_087 | Scope_078 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Tier | sửa | Name, Step, Exp | tách từ case Cột Tier của v1.4: mỗi loại framework một case |
| Scope_088 | — | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Tier | thêm | — | xem mục 2 |
| Scope_089 | Scope_079 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Coverage | sửa | Name, Step, Exp, OQ | thay case Cột Coverage để trống Expected của v1.4 bằng các case có số cụ thể |
| Scope_090 | — | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Coverage | thêm | — | xem mục 2 |
| Scope_091 | — | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Coverage | thêm | — | xem mục 2 |
| Scope_092 | — | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Coverage | thêm | — | xem mục 2 |
| Scope_093 | Scope_080 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Cột Status | sửa | Step |  |
| Scope_094 | Scope_081 | Khối Frameworks - Frameworks ▸ Hiển thị ▸ Nút Change tier | sửa | Step |  |
| Scope_095 | Scope_082 | Khối Frameworks - Frameworks ▸ Liên kết ▸ Bấm tên framework | sửa | Step |  |
| Scope_096 | Scope_083 | Gắn framework - Link framework ▸ Mở hộp thoại ▸ Bấm nút gắn framework | sửa | Step, Exp |  |
| Scope_097 | Scope_084 | Gắn framework - Link framework ▸ Danh sách framework ▸ Các lựa chọn | sửa | Step |  |
| Scope_098 | Scope_085 | Gắn framework - Link framework ▸ Danh sách framework ▸ Framework đã gắn | sửa | Step |  |
| Scope_099 | Scope_086 | Gắn framework - Link framework ▸ Chọn framework ▸ Framework có tier | sửa | Step |  |
| Scope_100 | Scope_087 | Gắn framework - Link framework ▸ Chọn framework ▸ Framework không tier | sửa | Step |  |
| Scope_101 | Scope_088 | Gắn framework - Link framework ▸ Không thành công ▸ Chưa chọn framework | sửa | III, Step | từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công |
| Scope_102 | Scope_089 | Gắn framework - Link framework ▸ Không thành công ▸ Chưa chọn tier | sửa | III, Step | từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công |
| Scope_103 | Scope_094 | Gắn framework - Link framework ▸ Không thành công ▸ Bấm Cancel | sửa | Step |  |
| Scope_104 | Scope_095 | Gắn framework - Link framework ▸ Không thành công ▸ Scope đang có audit | sửa | Pre, Step | ô Step tô vàng ở v1.4 |
| Scope_105 | Scope_090 | Gắn framework - Link framework ▸ Thành công ▸ Framework có tier | sửa | IV, Name, Step, Exp | tên case cũ: Hiện ở khối Frameworks; nhóm Thành công đặt theo loại framework |
| Scope_106 | — | Gắn framework - Link framework ▸ Thành công ▸ Framework không phân tier | thêm | — | xem mục 2 |
| Scope_107 | Scope_092 | Gắn framework - Link framework ▸ Thành công ▸ Hiện ở màn Workspaces | sửa | Pre, Step, Exp | hệ quả ở màn khác, giữ ở sheet của hành động theo rule 27 |
| Scope_108 | Scope_096 | Gỡ framework - Unlink framework ▸ Lối vào ▸ Tìm chức năng gỡ | sửa | Step |  |
| Scope_109 | Scope_097 | Đổi tier - Change tier ▸ Mở hộp thoại ▸ Không có audit | sửa | Step, Exp | ô Step tô vàng ở v1.4 |
| Scope_110 | Scope_098 | Đổi tier - Change tier ▸ Mở hộp thoại ▸ Đang có audit | sửa | Pre, Step, Exp | ô Step tô vàng ở v1.4 |
| Scope_111 | Scope_101 | Đổi tier - Change tier ▸ Không thành công ▸ Bấm Cancel | sửa | Step | ô Step tô vàng ở v1.4 |
| Scope_112 | Scope_102 | Đổi tier - Change tier ▸ Không thành công ▸ Đóng hộp thoại khoá | sửa | Pre, Step | ô Step tô vàng ở v1.4 |
| Scope_113 | Scope_099 | Đổi tier - Change tier ▸ Thành công ▸ Nâng tier | sửa | Step, Exp | ô Step tô vàng ở v1.4; Expected đang ghi Sau bước 2, Sau bước 4 trong khi thao tác ở bước 3, bước 5 |
| Scope_114 | Scope_100 | Đổi tier - Change tier ▸ Thành công ▸ Hạ tier | sửa | Step | ô Step tô vàng ở v1.4 |
| Scope_115 | Scope_103 | Khối Users - Users ▸ Hiển thị ▸ Tiêu đề khối và cột | sửa | Step, Exp | dòng cuối của Expected đang là "- F106" (hỏng từ bản v1.3); đặt lại 3 cột User, Role, Given |
| Scope_116 | Scope_104 | Khối Users - Users ▸ Hiển thị ▸ Dòng Customer Admin | sửa | Step |  |
| Scope_117 | Scope_105 | Khối Users - Users ▸ Hiển thị ▸ Dòng người được gán | sửa | Step |  |
| Scope_118 | Scope_106 | Gán người dùng - Assign users ▸ Mở hộp thoại ▸ Bấm Assign users | sửa | Step, Exp |  |
| Scope_119 | Scope_107 | Gán người dùng - Assign users ▸ Mở hộp thoại ▸ Vai trò trong danh sách | sửa | Step |  |
| Scope_120 | Scope_114 | Gán người dùng - Assign users ▸ Không thành công ▸ Bấm Cancel | sửa | Step |  |
| Scope_121 | Scope_108 | Gán người dùng - Assign users ▸ Thành công ▸ Tick thêm — khối Users | sửa | Step, Exp | ô tô vàng ở v1.4 |
| Scope_122 | Scope_110 | Gán người dùng - Assign users ▸ Thành công ▸ Tick thêm — người được gán thấy scope | sửa | Pre, Step, Exp | ô tô vàng ở v1.4; Expected đang cụt ("- Danh sách có") |
| Scope_123 | Scope_111 | Gán người dùng - Assign users ▸ Thành công ▸ Tick thêm — chi tiết người dùng | sửa | Pre, Step, Exp | ô tô vàng ở v1.4; Expected đang cụt; hệ quả ở màn khác, giữ ở sheet của hành động theo rule 27 |
| Scope_124 | Scope_112 | Gán người dùng - Assign users ▸ Thành công ▸ Bỏ tick — khối Users | sửa | Step, Exp | ô Step tô vàng ở v1.4 |
| Scope_125 | Scope_113 | Gán người dùng - Assign users ▸ Thành công ▸ Bỏ tick — người bị bỏ gán | sửa | Pre, Step, Exp | ô tô vàng ở v1.4; Expected đang cụt |
| Scope_126 | Scope_115 | Tổng hợp - Summary ▸ Hiển thị ▸ Evidence coverage | sửa | Step |  |
| Scope_127 | Scope_116 | Customer User ▸ Danh sách ▸ Chỉ scope được gán | sửa | Pre, Exp | ô Pre-condition tô vàng ở v1.4 |
| Scope_128 | Scope_117 | Customer User ▸ Danh sách ▸ Mô tả trang | sửa | Pre, Exp | ô Pre-condition tô vàng ở v1.4 |
| Scope_129 | Scope_118 | Customer User ▸ Chi tiết ▸ Không có thao tác ghi | sửa | Pre, Step, Exp | ô tô vàng ở v1.4 |
| Scope_130 | Scope_119 | Customer User ▸ Chi tiết ▸ Scope không được gán, mở bằng URL | sửa | Pre, Step, Exp | ô tô vàng ở v1.4; Expected đang cụt |
| Scope_131 | Scope_122 | Customer Viewer ▸ Danh sách và chi tiết ▸ Quyền xem | sửa | Pre | ô Pre-condition tô vàng ở v1.4 |
| Scope_132 | Scope_123 | Vai trò SGS - SGS roles ▸ Được phân công ▸ Chỉ đọc | sửa | Pre, Step, Exp | ô Pre-condition tô vàng ở v1.4 |
| Scope_133 | Scope_124 | Vai trò SGS - SGS roles ▸ Không được phân công ▸ Không thấy scope | sửa | Name, Pre, Step, Exp | ô Pre-condition tô vàng ở v1.4; bỏ bước gọi API (Tester không được gọi API) |
| Scope_134 | Scope_125 | Cách ly tenant - Tenant isolation ▸ Danh sách ▸ Scope của tenant khác | sửa | Pre, Exp | ô Pre-condition tô vàng ở v1.4 |
| Scope_135 | Scope_126 | Cách ly tenant - Tenant isolation ▸ URL ▸ Chi tiết scope tenant khác | sửa | Pre, Step | ô tô vàng ở v1.4 |
| Scope_136 | Scope_129 | Dữ liệu nhập - Input ▸ Mã độc ▸ Name chứa thẻ script | sửa | Step, Exp |  |
| Scope_137 | Scope_130 | Ghi vết - Audit log ▸ Thao tác ghi ▸ Tạo, sửa, gắn, gán | giữ | — |  |

## 5. Bảng đối chiếu số TC (toàn sheet)

Bản v1.4: cột No. là số dòng Excel (13, 14, …), có ô trống; 9 dòng chưa có TVP_ID; `Scope_016` và `Scope_052` mỗi số dùng hai lần. Bản v1.5 đánh lại liền mạch theo thứ tự trên sheet. Chưa có kết quả chạy ở cột Result nên việc đánh lại không làm mất kết quả nào.

| Dòng v1.4 | No. cũ | TVP_ID cũ | → | No. mới | TVP_ID mới | Tên case |
|---|---|---|---|---|---|---|
| 13 | 13 | Scope_001 | → | 1 | Scope_001 | Kiểm tra vào màn Scopes từ menu trái |
| 14 | 14 | Scope_002 | → | 2 | Scope_002 | Kiểm tra mở màn Scopes bằng URL |
| 15 | 15 | Scope_003 | → | 3 | Scope_003 | Kiểm tra mở chi tiết scope từ danh sách |
| 16 | 16 | Scope_004 | → | 4 | Scope_004 | Kiểm tra mở chi tiết scope bằng URL |
| 17 | 17 | Scope_005 | → | 5 | Scope_005 | Kiểm tra mở chi tiết bằng mã scope không tồn tại |
| 18 | 18 | Scope_006 | → | 6 | Scope_006 | Kiểm tra phần đầu màn Scopes |
| 19 | (trống) | Scope_052 | → | 7 | Scope_007 | Kiểm tra màn Scopes khi tenant chưa có scope nào |
| 20 | 20 | Scope_007 | → | 8 | Scope_008 | Kiểm tra hiển thị nút tạo scope |
| 21 | 21 | Scope_008 | → | 9 | Scope_009 | Kiểm tra mở hộp thoại Create scope |
| 22 | 22 | Scope_009 | → | 10 | Scope_010 | Kiểm tra các trường mặc định của hộp thoại Create scope |
| 23 | 23 | Scope_010 | → | 11 | Scope_011 | Kiểm tra các trường hiện thêm khi chọn System |
| 24 | 24 | Scope_011 | → | 12 | Scope_012 | Kiểm tra đổi loại sau khi đã chọn System |
| 25 | 25 | Scope_012 | → | 13 | Scope_013 | Kiểm tra danh sách chọn của Belongs to organisation |
| 26 | 26 | Scope_013 | → | 14 | Scope_014 | Kiểm tra danh sách chọn của Belongs to product (optional) |
| 27 | 27 | Scope_014 | → | 15 | Scope_015 | Kiểm tra tạo scope khi chưa chọn Type |
| 28 | 28 | Scope_015 | → | 16 | Scope_016 | Kiểm tra tạo scope khi bỏ trống Name |
| 29 | 29 | Scope_016 | → | 17 | Scope_017 | Kiểm tra tạo scope khi Name chỉ có khoảng trắng |
| 30 | 30 | Scope_017 | → | 18 | Scope_018 | Kiểm tra tạo scope khi bỏ trống What is in scope |
| 31 | 31 | Scope_016 | → | 19 | Scope_019 | Kiểm tra tạo scope khi Name chỉ có khoảng trắng |
| 32 | 32 | Scope_019 | → | 20 | Scope_020 | Kiểm tra tạo scope trùng tên scope đang có |
| 33 | (trống) | Scope_020 | → | 21 | Scope_021 | Kiểm tra nhập quá giới hạn ký tự |
| 34 | (trống) | Scope_028 | → | 22 | Scope_022 | Kiểm tra huỷ tạo scope bằng Cancel |
| 35 | (trống) | Scope_029 | → | 23 | Scope_023 | Kiểm tra đóng hộp thoại tạo scope bằng nút × |
| 36 | 33 | Scope_030 | → | 24 | Scope_024 | Kiểm tra nhấn Esc khi đang mở hộp thoại tạo scope |
| 37 | 34 | Scope_021 | → | 25 | Scope_025 | Kiểm tra thông tin vừa tạo |
| 38 | 35 | Scope_022 | → | 26 | Scope_026 | Kiểm tra thông tin vừa tạo |
| 39 | 38 | Scope_025 | → | 27 | Scope_027 | Kiểm tra scope System vừa tạo hiện ở danh sách |
| 40 | 47 | Scope_031 | → | 28 | Scope_028 | Kiểm tra dòng đếm số scope |
| 41 | 48 | Scope_032 | → | 29 | Scope_029 | Kiểm tra ô tìm kiếm |
| 42 | 49 | Scope_033 | → | 30 | Scope_030 | Kiểm tra tìm theo một phần tên scope |
| 43 | 50 | Scope_034 | → | 31 | Scope_031 | Kiểm tra tìm kiếm khi nhập chữ hoa |
| 44 | 51 | Scope_035 | → | 32 | Scope_032 | Kiểm tra tìm kiếm không ra kết quả |
| 45 | 52 | Scope_036 | → | 33 | Scope_033 | Kiểm tra nhập ký tự đặc biệt vào ô tìm kiếm |
| 46 | 53 | Scope_037 | → | 34 | Scope_034 | Kiểm tra xoá từ khoá tìm kiếm |
| 47 | 54 | Scope_038 | → | 35 | Scope_035 | Kiểm tra tiêu đề các cột |
| 48 | 55 | Scope_039 | → | 36 | Scope_036 | Kiểm tra cột Scope |
| 49 | 56 | Scope_040 | → | 37 | Scope_037 | Kiểm tra cột Belongs to với scope Organization |
| 50 | (trống) | Scope_041 | → | 38 | Scope_038 | Kiểm tra cột Belongs to với scope Product |
| 51 | (trống) | (trống) | → | 39 | Scope_039 | Kiểm tra cột Belongs to với scope System |
| 52 | (trống) | Scope_042 | → | 40 | Scope_040 | Kiểm tra cột Belongs to với scope System và bỏ trống lựa chọn Belongs to organisation và Belongs to product (optional) |
| 53 | 57 | Scope_043 | → | 41 | Scope_041 | Kiểm tra cột Frameworks của scope đã gắn framework |
| 54 | 58 | Scope_044 | → | 42 | Scope_042 | Kiểm tra cột Frameworks của scope chưa gắn framework |
| 55 | 59 | Scope_045 | → | 43 | Scope_043 | Kiểm tra cột Users khớp với màn chi tiết |
| 56 | (trống) | (trống) | → | 44 | Scope_044 | Calculate Evidence coverage with multiple frameworks |
| 57 | (trống) | (trống) | → | 45 | Scope_045 | Calculate Evidence coverage with 2 frameworks |
| 58 | (trống) | (trống) | → | 46 | Scope_046 | All requirements have mandatory evidence |
| 59 | (trống) | (trống) | → | 47 | Scope_047 | No requirements have mandatory evidence |
| 60 | (trống) | (trống) | → | 48 | Scope_048 | Only one framework is linked |
| 61 | 60 | Scope_046 | → | 49 | Scope_049 | One framework has 100% and another has 0% |
| 62 | 61 | Scope_047 | → | 54 | Scope_054 | Kiểm tra thứ tự mặc định của danh sách |
| 63 | 62 | Scope_048 | → | 55 | Scope_055 | Kiểm tra sắp xếp tăng dần theo tên |
| 64 | 63 | Scope_049 | → | 56 | Scope_056 | Kiểm tra sắp xếp giảm dần theo tên |
| 65 | 64 | Scope_050 | → | 57 | Scope_057 | Kiểm tra dòng phân trang mặc định |
| 66 | (trống) | (trống) | → | 58 | Scope_058 | Kiểm tra các giá trị trong Items per page |
| 67 | 65 | Scope_051 | → | 59 | Scope_059 | Kiểm tra đổi số dòng mỗi trang |
| 68 | 66 | Scope_052 | → | 60 | Scope_060 | Kiểm tra nút chuyển trang khi chỉ có một trang |
| 69 | 67 | Scope_053 | → | 61 | Scope_061 | Kiểm tra chuyển sang trang 2 |
| 70 | 68 | Scope_054 | → | 62 | Scope_062 | Kiểm tra phần đầu màn chi tiết |
| 71 | (trống) | (trống) | → | 63 | Scope_063 | Kiểm tra dòng phụ theo loại scope Organization |
| 72 | (trống) | (trống) | → | 64 | Scope_064 | Kiểm tra dòng phụ theo loại scope Product |
| 73 | 69 | Scope_055 | → | 65 | Scope_065 | Kiểm tra dòng phụ theo loại scope System |
| 74 | 70 | Scope_056 | → | 66 | Scope_066 | Kiểm tra nút quay lại |
| 75 | 71 | Scope_057 | → | 67 | Scope_067 | Kiểm tra menu ⋮ của scope |
| 76 | 72 | Scope_058 | → | 68 | Scope_068 | Kiểm tra mục Edit scope trong menu ⋮ |
| 77 | 73 | Scope_059 | → | 69 | Scope_069 | Kiểm tra cột điều hướng bên trái |
| 78 | 74 | Scope_060 | → | 70 | Scope_070 | Kiểm tra bấm mục trong cột điều hướng |
| 79 | 75 | Scope_061 | → | 71 | Scope_071 | Kiểm tra khối Overview của scope Organization |
| 80 | 76 | Scope_062 | → | 72 | Scope_072 | Kiểm tra khối Overview của scope Product |
| 81 | 77 | Scope_063 | → | 73 | Scope_073 | Kiểm tra khối Overview của scope System |
| 82 | 78 | Scope_064 | → | 74 | Scope_074 | Kiểm tra trường không có dữ liệu |
| 83 | 79 | Scope_065 | → | 75 | Scope_075 | Kiểm tra mở hộp thoại Edit scope |
| 84 | 80 | Scope_066 | → | 76 | Scope_076 | Kiểm tra lưu khi xoá trống Name |
| 85 | 81 | Scope_067 | → | 77 | Scope_077 | Kiểm tra lưu khi xoá trống What is in scope |
| 86 | 82 | Scope_068 | → | 78 | Scope_078 | Kiểm tra đổi Name trùng tên scope khác |
| 87 | 83 | Scope_069 | → | 81 | Scope_081 | Kiểm tra tên mới ở màn chi tiết sau khi sửa |
| 88 | 84 | Scope_070 | → | 82 | Scope_082 | Kiểm tra tên mới ở màn danh sách |
| 89 | 85 | Scope_071 | → | — | bỏ | Kiểm tra tên mới ở Overview của scope con |
| 90 | 86 | Scope_072 | → | — | bỏ | Kiểm tra tên mới ở cột Belongs to của danh sách |
| 91 | 87 | Scope_073 | → | 83 | Scope_083 | Kiểm tra sửa In scope và Out of scope |
| 92 | 88 | Scope_074 | → | 79 | Scope_079 | Kiểm tra huỷ sửa scope |
| 93 | 89 | Scope_075 | → | 80 | Scope_080 | Kiểm tra sửa scope khi đang có audit |
| 94 | 90 | Scope_076 | → | 85 | Scope_085 | Kiểm tra khối Frameworks |
| 95 | 91 | Scope_077 | → | 86 | Scope_086 | Kiểm tra cột Framework · version |
| 96 | 92 | Scope_078 | → | 87 | Scope_087 | Kiểm tra cột Tier |
| 97 | 93 | Scope_079 | → | 89 | Scope_089 | Kiểm tra cột Coverage |
| 98 | 94 | Scope_080 | → | 93 | Scope_093 | Kiểm tra cột Status |
| 99 | 95 | Scope_081 | → | 94 | Scope_094 | Kiểm tra nút Change tier trên từng dòng |
| 100 | 96 | Scope_082 | → | 95 | Scope_095 | Kiểm tra mở workspace từ tên framework |
| 101 | 97 | Scope_083 | → | 96 | Scope_096 | Kiểm tra mở hộp thoại gắn framework |
| 102 | 98 | Scope_084 | → | 97 | Scope_097 | Kiểm tra danh sách framework |
| 103 | 99 | Scope_085 | → | 98 | Scope_098 | Kiểm tra framework đã gắn vào scope có trong danh sách không |
| 104 | 100 | Scope_086 | → | 99 | Scope_099 | Kiểm tra chọn framework có phân tier |
| 105 | 101 | Scope_087 | → | 100 | Scope_100 | Kiểm tra chọn framework không phân tier |
| 106 | 102 | Scope_088 | → | 101 | Scope_101 | Kiểm tra bấm gắn khi chưa chọn framework |
| 107 | 103 | Scope_089 | → | 102 | Scope_102 | Kiểm tra bấm gắn khi chưa chọn tier |
| 108 | 104 | Scope_090 | → | 105 | Scope_105 | Kiểm tra framework vừa gắn hiện ở khối Frameworks |
| 109 | 105 | Scope_091 | → | — | bỏ | Kiểm tra framework vừa gắn hiện ở cột Frameworks của danh sách |
| 110 | 106 | Scope_092 | → | 107 | Scope_107 | Kiểm tra workspace mới hiện ở màn Workspaces |
| 111 | 107 | Scope_093 | → | — | bỏ | Kiểm tra framework vừa gắn hiện ở khối Summary |
| 112 | 108 | Scope_094 | → | 103 | Scope_103 | Kiểm tra huỷ gắn framework |
| 113 | 109 | Scope_095 | → | 104 | Scope_104 | Kiểm tra gắn thêm framework khi scope đang có audit |
| 114 | 110 | Scope_096 | → | 108 | Scope_108 | Kiểm tra lối vào gỡ framework khỏi scope |
| 115 | 111 | Scope_097 | → | 109 | Scope_109 | Kiểm tra hộp thoại đổi tier |
| 116 | 112 | Scope_098 | → | 110 | Scope_110 | Kiểm tra hộp thoại đổi tier khi đang có audit |
| 117 | 113 | Scope_099 | → | 113 | Scope_113 | Kiểm tra nâng tier |
| 118 | 114 | Scope_100 | → | 114 | Scope_114 | Kiểm tra hạ tier |
| 119 | 115 | Scope_101 | → | 111 | Scope_111 | Kiểm tra huỷ đổi tier |
| 120 | 116 | Scope_102 | → | 112 | Scope_112 | Kiểm tra đóng hộp thoại khoá bằng Close |
| 121 | 117 | Scope_103 | → | 115 | Scope_115 | Kiểm tra khối Users |
| 122 | 118 | Scope_104 | → | 116 | Scope_116 | Kiểm tra dòng của Customer Admin |
| 123 | 119 | Scope_105 | → | 117 | Scope_117 | Kiểm tra dòng của người được gán |
| 124 | 120 | Scope_106 | → | 118 | Scope_118 | Kiểm tra mở hộp thoại Assign users |
| 125 | 121 | Scope_107 | → | 119 | Scope_119 | Kiểm tra những vai trò có trong danh sách gán |
| 126 | 122 | Scope_108 | → | 121 | Scope_121 | Kiểm tra người vừa gán hiện ở khối Users |
| 127 | 123 | Scope_109 | → | — | bỏ | Kiểm tra cột Users ở danh sách sau khi gán |
| 128 | 124 | Scope_110 | → | 122 | Scope_122 | Kiểm tra người vừa được gán thấy scope |
| 129 | 125 | Scope_111 | → | 123 | Scope_123 | Kiểm tra scope hiện ở chi tiết người dùng |
| 130 | 126 | Scope_112 | → | 124 | Scope_124 | Kiểm tra bỏ gán người dùng |
| 131 | 127 | Scope_113 | → | 125 | Scope_125 | Kiểm tra người bị bỏ gán không còn thấy scope |
| 132 | 128 | Scope_114 | → | 120 | Scope_120 | Kiểm tra huỷ gán người dùng |
| 133 | 129 | Scope_115 | → | 126 | Scope_126 | Kiểm tra khối Summary |
| 134 | 130 | Scope_116 | → | 127 | Scope_127 | Kiểm tra màn Scopes với Customer User |
| 135 | 131 | Scope_117 | → | 128 | Scope_128 | Kiểm tra mô tả trang với Customer User |
| 136 | 132 | Scope_118 | → | 129 | Scope_129 | Kiểm tra màn chi tiết với Customer User |
| 137 | 133 | Scope_119 | → | 130 | Scope_130 | Kiểm tra Customer User mở scope không được gán bằng URL |
| 138 | 134 | Scope_120 | → | — | bỏ | Kiểm tra Customer User gọi API tạo scope |
| 139 | 135 | Scope_121 | → | — | bỏ | Kiểm tra Customer User gọi API sửa scope, gắn framework, gán người dùng |
| 140 | 136 | Scope_122 | → | 131 | Scope_131 | Kiểm tra màn Scopes với Customer Viewer |
| 141 | 137 | Scope_123 | → | 132 | Scope_132 | Kiểm tra SGS Consultant xem scope của khách được phân công |
| 142 | 138 | Scope_124 | → | 133 | Scope_133 | Kiểm tra người dùng SGS không được phân công tenant A |
| 143 | 139 | Scope_125 | → | 134 | Scope_134 | Kiểm tra cách ly danh sách scope giữa hai tenant |
| 144 | 140 | Scope_126 | → | 135 | Scope_135 | Kiểm tra mở chi tiết scope của tenant khác bằng URL |
| 145 | 141 | Scope_127 | → | — | bỏ | Kiểm tra gọi API chi tiết scope của tenant khác |
| 146 | 142 | Scope_128 | → | — | bỏ | Kiểm tra gán người dùng của tenant khác vào scope |
| 147 | 143 | Scope_129 | → | 136 | Scope_136 | Kiểm tra tạo scope có Name chứa mã độc |
| 148 | 144 | Scope_130 | → | 137 | Scope_137 | Kiểm tra ghi audit cho các thao tác trên scope |
| — | — | — | → | 50 | Scope_050 | Kiểm tra Evidence coverage khi scope chưa gắn framework nào (thêm) |
| — | — | — | → | 51 | Scope_051 | Kiểm tra Evidence coverage khi phần thập phân đúng bằng .5 (thêm) |
| — | — | — | → | 52 | Scope_052 | Kiểm tra Evidence coverage khi kết quả trên 0% và dưới 0.5% (thêm) |
| — | — | — | → | 53 | Scope_053 | Kiểm tra Evidence coverage khi kết quả từ 99.5% đến dưới 100% (thêm) |
| — | — | — | → | 84 | Scope_084 | Kiểm tra khối Frameworks khi scope chưa gắn framework (thêm) |
| — | — | — | → | 88 | Scope_088 | Kiểm tra cột Tier của framework không phân tier (thêm) |
| — | — | — | → | 90 | Scope_090 | Kiểm tra cột Coverage khi kết quả phải làm tròn xuống (thêm) |
| — | — | — | → | 91 | Scope_091 | Kiểm tra cột Coverage khi chưa requirement nào đủ evidence (thêm) |
| — | — | — | → | 92 | Scope_092 | Kiểm tra cột Coverage khi mọi requirement đều đủ evidence (thêm) |
| — | — | — | → | 106 | Scope_106 | Kiểm tra gắn framework không phân tier (thêm) |

## 6. Thay đổi ngoài nội dung sheet Scopes

Nội dung các sheet Login, Users, Profile giữ nguyên, trừ một ô ghi ở dưới. Phần `{{…}}` và nhóm Kiểm tra dữ liệu ở ba sheet đó chưa sửa.

| Chỗ | Trước | Sau | Vì sao |
|---|---|---|---|
| Cần xác nhận!D2 | Chưa có Figma trang 02. Customer Portal tạm theo prototype của Scopes (Scopes TC_110: Users ở mục Administration). | Chưa có Figma trang 02. Customer Portal tạm theo prototype của Scopes (Scopes Scope_123: Users ở mục Administration). | số TC của Scopes đổi |
| Cần xác nhận!E20 | Scopes Scope_021, Scope_025, Scope_131 | Scopes Scope_025, Scope_026, Scope_027 | số TC của Scopes đổi |
| Users!W13 | Tên mục menu lấy theo prototype của Scopes (Scopes TC_110), chờ Figma trang 02 → Q-U-01 | Tên mục menu lấy theo prototype của Scopes (Scopes Scope_123), chờ Figma trang 02 → Q-U-01 | số TC của Scopes đổi |
| Cover!G6 | Version 1.3 | Version 1.5 | bản mới |
| Cover dòng 17–19 | (trống) | 3 dòng Record of change: 1.4 (Hanna sửa), 1.5 (viết lại phần dưới), 1.5 (phông, dấu nháy) | ghi lịch sử |
| Cover dòng 14–19 | chữ ở cột Change Item, Change description, Reference bị cắt | bật xuống dòng, nới chiều cao dòng | đọc được hết chữ |
| Test_Report | khu vực Trạng thái rỗng nằm sau Phân trang; tổng Scopes 127 | dựng lại theo thứ tự trên sheet; tổng Scopes 137; tổng cả file 264 | theo sheet Scopes mới |

Định dạng, cho cả file:

- Phông: 16 kiểu ô đang dùng Arial 10 chuyển sang Times New Roman 10 (ô trống đã kẻ khung, ô trong cụm gộp, kiểu mặc định của các cột ở sheet Cần xác nhận, và 5 ô có chữ: Login!C5, C7; Users!C4; Scopes!J51, E56). Kiểu Normal của file giữ nguyên để độ rộng cột không đổi.
- Dấu nháy đơn đầu ô: 216 ô văn bản bắt đầu bằng dấu `-` có thuộc tính quotePrefix (Login 34, Scopes 121, Users 50, Profile 11). Bản v1.4 có 36 ô, do Hanna tự thêm.
- Nền tô tay ở sheet Scopes: bỏ 53 ô nền vàng (37 ô đã đổi chữ, 11 ô mất cùng case bị bỏ, 5 ô giữ nguyên chữ: Step của Scope_072, Pre-condition của Scope_120, 121, 124, 126) và 12 ô nền trắng ở dòng 49–55 (nhìn không khác ô không nền).
- Dạng chữ: 57 ô ở sheet Scopes có chữ tiếng Việt ở dạng tổ hợp (dấu thanh tách rời khỏi chữ cái) được lưu lại ở dạng dựng sẵn (NFC); nhìn không khác, nhưng `tc_check.py` coi "Không thành công" gõ hai dạng là hai giá trị khác nhau và đã báo một lỗi giả ở bản v1.4.
- Chiều cao dòng của sheet Scopes: đặt lại theo số dòng chữ (LibreOffice đo), cùng quy ước với các sheet khác: 13.5 pt mỗi dòng chữ + 8.1 pt.
