# Test basis — DEMO · Quản lý người dùng v1.0

> **VÍ DỤ MINH HỌA** — ứng dụng "Demo" và mọi dữ liệu trong file này là giả, không thuộc dự án SGS. Dùng để thấy test basis trông thế nào khi đủ thông tin cho Tester.

| | |
|---|---|
| Baseline nguồn | docs/baseline/DEMO.v1.0.md |
| Ngày | 2026-09-28 |
| Trạng thái | Sẵn sàng thiết kế |
| Giả định còn hiệu lực | Không có |
| Câu hỏi còn mở (không CHẶN) | Không có |

## 0. Tóm tắt bàn giao
- Phạm vi: 1 UC trong phạm vi (UC-DEMO-001). Các UC-DEMO-002 → 006 chỉ được nhắc tới vì dùng chung đối tượng Người dùng.
- Ưu tiên test: phân quyền tạo người dùng (lộ quyền quản trị) và rule email duy nhất.
- Điểm dễ sai: email trùng khác hoa/thường; giới hạn 5 Admin tính cả người đang ở trạng thái Invited.

## 1. Dùng chung

### 1.1 Vai trò
| Vai trò | Mô tả | Cổng | Tài khoản test cần có |
|---|---|---|---|
| Admin | Quản trị tenant | Web | admin1@t1.demo.test, admin2@t1.demo.test, admin1@t2.demo.test, admin1@t3.demo.test |
| Member | Thành viên | Web | member1@t1.demo.test |

### 1.2 Ma trận phân quyền
| ID | Vai trò | Hành động | Đối tượng | Phạm vi dữ liệu | Được phép | Khi bị chặn thì thấy gì |
|---|---|---|---|---|---|---|
| PM-USER-01 | Admin | Tạo | Người dùng | Tenant của mình | Có | — |
| PM-USER-02 | Member | Tạo | Người dùng | Tenant của mình | Không | Không thấy nút "Tạo người dùng"; mở URL → trang 403 "Bạn không có quyền truy cập trang này."; gọi API → HTTP 403 |
| PM-USER-03 | Admin | Tạo | Người dùng | Tenant khác (gửi `tenantId` khác qua API) | Không | HTTP 403, không tạo ở tenant kia |

### 1.3 Mô hình trạng thái — Người dùng: Invited, Active, Deactivated, Revoked
| ID | Từ | Sự kiện | Sang | Ai được làm | Hợp lệ | UC |
|---|---|---|---|---|---|---|
| ST-USER-01 | (chưa có) | Tạo người dùng | Invited | Admin | Có | UC-DEMO-001 |
| ST-USER-02 | Invited | Chấp nhận lời mời | Active | Người được mời | Có | UC-DEMO-005 |
| ST-USER-03 | Invited | Thu hồi lời mời | Revoked | Admin | Có | UC-DEMO-006 |
| ST-USER-04 | Active | Vô hiệu hóa | Deactivated | Admin | Có | UC-DEMO-004 |
| ST-USER-05 | Deactivated | Kích hoạt lại | Active | Admin | Có | UC-DEMO-004 |
| ST-USER-06 | Revoked | Chấp nhận lời mời bằng link cũ | — | Người được mời | Không → "Lời mời không còn hiệu lực." | UC-DEMO-005 |

### 1.4 Thuật ngữ
| Thuật ngữ | Nghĩa | Không nhầm với |
|---|---|---|
| Tenant | Một tổ chức khách hàng; dữ liệu các tenant tách biệt | Nhóm, phòng ban |

### 1.5 Quy ước chung
- Hết phiên sau 30 phút không thao tác; thao tác tiếp theo chuyển tới `/login`, dữ liệu chưa lưu không được gửi.
- Nút gửi của mọi form bị tắt trong lúc đang xử lý (chặn gửi hai lần).
- Danh sách sắp xếp mới nhất trước, 20 dòng mỗi trang.
- API trả HTTP 400 kèm mã lỗi theo trường khi dữ liệu không hợp lệ.

### 1.6 Môi trường và dữ liệu test
- Tenant T1 có đúng 4 Admin; T3 có đúng 5 Admin, trong đó 1 người đang Invited; T2 có người dùng `minh@demo.test`. Dữ liệu được dựng lại trước mỗi TC để TC chạy độc lập.
- T1 có người dùng `old.user@demo.test` ở trạng thái Deactivated và `lan@demo.test` ở trạng thái Active.
- Dịch vụ email là mock, bật được chế độ lỗi; hộp thư test đọc được qua API.
- Audit log đọc được qua `GET /api/audit`.

## 2. Từng UC

### UC-DEMO-001 · Tạo người dùng và gửi lời mời — Ưu tiên P1
Rủi ro: lộ quyền quản trị, trùng tài khoản · Actor: Admin (PM-USER-01) · Tiền điều kiện: Admin đã đăng nhập.

#### Đường vào / ra → Redirect
| ID | Từ đâu | Cách vào / ra | Vai trò | Trạng thái dữ liệu | Kết quả |
|---|---|---|---|---|---|
| UC-DEMO-001-NV-01 | Màn hình "Người dùng" (/users) | Bấm nút "Tạo người dùng" | Admin | — | Mở màn hình "Tạo người dùng", URL /users/new |
| UC-DEMO-001-NV-02 | Thanh địa chỉ | Nhập /users/new | Admin | — | Mở màn hình "Tạo người dùng" |
| UC-DEMO-001-NV-03 | Thanh địa chỉ | Nhập /users/new | Chưa đăng nhập | — | Chuyển tới /login; đăng nhập Admin xong quay lại /users/new |
| UC-DEMO-001-NV-04 | Thanh địa chỉ | Nhập /users/new | Member | — | Trang 403 "Bạn không có quyền truy cập trang này." |
| UC-DEMO-001-NV-05 | Màn hình "Tạo người dùng" | Gửi lời mời thành công | Admin | — | Về /users, hiện MS-07 |
| UC-DEMO-001-NV-06 | Màn hình "Tạo người dùng" | Bấm "Hủy" | Admin | Đã nhập dữ liệu chưa lưu | Hộp thoại MS-12; "Bỏ thay đổi" → về /users, không tạo; "Ở lại" → giữ nguyên dữ liệu |
| UC-DEMO-001-NV-07 | Mọi đường vào hợp lệ | Đến màn hình | Admin | — | Tiêu đề "Tạo người dùng"; Họ và tên, Email trống; Vai trò = "Member"; focus ở "Họ và tên"; nút "Gửi lời mời" bật |

#### Trường dữ liệu → Validation
| ID | Nhãn | Kiểu | Bắt buộc | Độ dài | Giá trị / khoảng | Định dạng, ký tự cho phép | Mặc định | Duy nhất | Phụ thuộc | Thông báo |
|---|---|---|---|---|---|---|---|---|---|---|
| UC-DEMO-001-FD-01 | Họ và tên | Text | Có | 2–50, tính sau khi trim | — | Chữ (kể cả có dấu), khoảng trắng, `'` và `-`; trim đầu/cuối | Trống | Không | — | MS-01, MS-02, MS-03, MS-14 |
| UC-DEMO-001-FD-02 | Email | Email | Có | ≤ 254 | — | Định dạng email; trim đầu/cuối; lưu chữ thường | Trống | Có — trong tenant, không phân biệt hoa thường (BR-01) | — | MS-04, MS-05, MS-06, MS-14 |
| UC-DEMO-001-FD-03 | Vai trò | Dropdown | Có | — | Admin, Member | — | Member | Không | — | MS-10, MS-13 |

#### Thông báo và text giao diện
| ID | Khi nào | Text nguyên văn | Vị trí |
|---|---|---|---|
| UC-DEMO-001-MS-01 | Họ và tên trống hoặc chỉ khoảng trắng | Vui lòng nhập họ và tên. | Dưới trường |
| UC-DEMO-001-MS-02 | Họ và tên dưới 2 hoặc trên 50 ký tự | Họ và tên từ 2 đến 50 ký tự. | Dưới trường |
| UC-DEMO-001-MS-03 | Họ và tên có ký tự không cho phép | Họ và tên chỉ gồm chữ, khoảng trắng, dấu ' và -. | Dưới trường |
| UC-DEMO-001-MS-04 | Email trống | Vui lòng nhập email. | Dưới trường |
| UC-DEMO-001-MS-05 | Email sai định dạng hoặc quá 254 ký tự | Email không đúng định dạng. | Dưới trường |
| UC-DEMO-001-MS-06 | Email đã tồn tại trong tenant | Email đã tồn tại trong tổ chức. | Dưới trường, sau khi bấm gửi |
| UC-DEMO-001-MS-07 | Tạo thành công | Đã gửi lời mời đến {email}. | Toast trên màn hình "Người dùng" |
| UC-DEMO-001-MS-08 | Email thuộc người dùng đã vô hiệu hóa | Người dùng này đã bị vô hiệu hóa. Hãy kích hoạt lại thay vì tạo mới. | Hộp thông báo |
| UC-DEMO-001-MS-09 | Dịch vụ email lỗi | Đã tạo người dùng nhưng chưa gửi được email. Bạn có thể gửi lại lời mời sau. | Toast cảnh báo |
| UC-DEMO-001-MS-10 | Tenant đã có 5 Admin | Tổ chức đã có tối đa 5 Admin. | Dưới trường Vai trò |
| UC-DEMO-001-MS-11 | Mất kết nối khi gửi | Không kết nối được máy chủ. Vui lòng thử lại. | Toast lỗi |
| UC-DEMO-001-MS-12 | Hủy khi có thay đổi chưa lưu | Bỏ các thay đổi chưa lưu? — nút "Bỏ thay đổi", "Ở lại" | Hộp thoại |
| UC-DEMO-001-MS-13 | API nhận vai trò ngoài danh sách | HTTP 400, `{"error": "INVALID_ROLE"}` | Response API |
| UC-DEMO-001-MS-14 | API nhận Họ và tên hoặc Email không hợp lệ | HTTP 400, `{"error": "VALIDATION", "fields": [...]}` | Response API |

#### Luồng → Function
- UC-DEMO-001-MF-01: Admin mở màn hình "Tạo người dùng".
- UC-DEMO-001-MF-02: Admin nhập Họ và tên, Email, chọn Vai trò.
- UC-DEMO-001-MF-03: Admin bấm "Gửi lời mời".
- UC-DEMO-001-MF-04: Hệ thống kiểm tra BR-01, BR-02; tạo người dùng trạng thái Invited (ST-USER-01); gửi email mời; về /users và hiện MS-07.
- UC-DEMO-001-AF-01 (rẽ từ MF-04): email trùng người dùng đang Deactivated → không tạo, hiện MS-08.
- UC-DEMO-001-EF-01 (tại MF-04): dịch vụ email lỗi → vẫn tạo người dùng Invited, hiện MS-09.
- UC-DEMO-001-EF-02 (tại MF-03): mất kết nối khi gửi → hiện MS-11, dữ liệu trên form giữ nguyên, không tạo người dùng.

#### Business rule
| ID | Rule | Điều kiện | Kết quả khi thỏa | Kết quả khi vi phạm |
|---|---|---|---|---|
| UC-DEMO-001-BR-01 | Email là duy nhất trong tenant, không phân biệt hoa thường. Email trùng ở tenant khác vẫn hợp lệ. | Email đã tồn tại trong tenant? | Tạo người dùng | MS-06; nếu người dùng trùng đang Deactivated thì MS-08 |
| UC-DEMO-001-BR-02 | Mỗi tenant có tối đa 5 người dùng vai trò Admin, tính cả người đang Invited. | Vai trò = Admin và tenant đã có 5 Admin | Tạo người dùng | MS-10 |

#### Tác động phụ và hậu điều kiện
| ID | Sau hành động | Thấy ở đâu / ai nhận | Nội dung |
|---|---|---|---|
| UC-DEMO-001-SE-01 | Tạo thành công | Màn hình "Người dùng" | Dòng mới ở đầu danh sách, cột Trạng thái "Đã mời" |
| UC-DEMO-001-SE-02 | Tạo thành công | Hộp thư của email đã nhập | Email tiêu đề "Lời mời tham gia Demo", có link kích hoạt |
| UC-DEMO-001-SE-03 | Tạo thành công | `GET /api/audit` | Bản ghi action = "user.invited", actor = Admin đang đăng nhập, target = email mới |

#### Ghi chú cho Tester
Email lưu chữ thường sau trim — kiểm giá trị sau khi lưu, không chỉ thông báo.

## 3. Ngoài phạm vi và chưa đủ thông tin
| UC | Nhóm | Lý do |
|---|---|---|
| UC-DEMO-002 → 006 | Ngoài đợt này | Chỉ dùng chung đối tượng Người dùng |
