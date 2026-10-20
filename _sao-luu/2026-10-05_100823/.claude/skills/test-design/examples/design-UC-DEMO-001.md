# Thiết kế test — UC-DEMO-001 · Tạo người dùng và gửi lời mời

> **VÍ DỤ MINH HỌA** — đi cùng `test-basis-demo.md`, `cases-demo.md`, `rtm-demo.md`.

| | |
|---|---|
| Test basis | examples/test-basis-demo.md (v1.0) |
| Ngày | 2026-09-28 |
| Trạng thái | Đã tự review |

## 1. Bản đồ kiểm thử

| ID nguồn | Nội dung tóm tắt | Nhóm | Kỹ thuật | Ưu tiên |
|---|---|---|---|---|
| NV-01 → NV-07 | Đường vào (nút, URL), chặn (chưa đăng nhập, Member), đường ra (thành công, hủy), trạng thái khi đến | Redirect | Ma trận điều hướng | P1–P3 |
| PM-USER-01, PM-USER-02 | Ai được vào màn hình, ai thấy nút | Redirect | Phân quyền | P1 |
| FD-01 Họ và tên | 2–50 sau trim, chữ có dấu, khoảng trắng, ' - | Validation | EP, BVA | P2 |
| FD-02 Email | ≤ 254, định dạng, trim, chữ thường | Validation | EP, BVA | P2 |
| FD-03 Vai trò | Admin / Member, mặc định Member | Validation | EP | P2 |
| MS-01 → MS-14 | Thông báo — mỗi cái phải được kích hoạt | Validation / Function | — | — |
| MF-01 → MF-04, AF-01, EF-01, EF-02 | Luồng chính, email của người đã vô hiệu hóa, email lỗi, mất mạng | Function | Kịch bản | P1–P2 |
| BR-01, BR-02 | Email duy nhất; tối đa 5 Admin | Function | Bảng quyết định, BVA trên con số 5 | P1 |
| ST-USER-01 | Tạo → Invited | Function | Chuyển trạng thái | P1 |
| PM-USER-02, PM-USER-03 | Member gọi API; Admin tạo sang tenant khác | Function | Phân quyền | P1 |
| SE-01 → SE-03 | Danh sách, email mời, audit | Function | CRUD, kịch bản | P2 |

## 2. Redirect — ma trận điều hướng

| NV | Admin | Member | Chưa đăng nhập |
|---|---|---|---|
| NV-01 nút "Tạo người dùng" | Mở form | Không thấy nút (PM-USER-02) | — |
| NV-02 URL /users/new | Mở form | 403 (NV-04) | → /login → quay lại (NV-03) |
| NV-05 gửi thành công | Về /users + MS-07 | — | — |
| NV-06 Hủy khi có dữ liệu | MS-12 → "Bỏ thay đổi" / "Ở lại" | — | — |
| NV-07 trạng thái khi đến | Mặc định như test basis | — | — |

## 3. Validation — phân vùng và biên theo trường

### UC-DEMO-001-FD-01 · Họ và tên
| ID | Lớp / giá trị | Hợp lệ | Giá trị test | Kết quả |
|---|---|---|---|---|
| UC-DEMO-001-EP-01 | Chữ có dấu | Có | "Nguyễn Thị Ánh" | Lưu "Nguyễn Thị Ánh" |
| UC-DEMO-001-EP-02 | Có `'` và `-` | Có | "Anne-Marie O'Neil" | Lưu nguyên văn |
| UC-DEMO-001-EP-03 | Trống | Không | "" | MS-01 |
| UC-DEMO-001-EP-04 | Chỉ khoảng trắng | Không | "   " | MS-01 |
| UC-DEMO-001-EP-05 | Có số hoặc ký tự cấm | Không | "An3" | MS-03 |
| UC-DEMO-001-EP-06 | Chuỗi script | Không | "<script>alert(1)</script>" | MS-03, không thực thi |
| UC-DEMO-001-EP-07 | Khoảng trắng đầu/cuối, phần còn lại hợp lệ | Có | "  Lan  " | Lưu "Lan" |
| UC-DEMO-001-BV-01 | 1 ký tự | Không | "A" | MS-02 |
| UC-DEMO-001-BV-02 | 2 ký tự | Có | "An" | Lưu |
| UC-DEMO-001-BV-03 | 50 ký tự | Có | "Nguyen " + 43 × "a" | Lưu đủ 50 ký tự |
| UC-DEMO-001-BV-04 | 51 ký tự | Không | "Nguyen " + 44 × "a" | MS-02 |
| UC-DEMO-001-BV-05 | 1 ký tự sau trim | Không | " A " | MS-02 (độ dài tính sau trim) |

### UC-DEMO-001-FD-02 · Email
| ID | Lớp / giá trị | Hợp lệ | Giá trị test | Kết quả |
|---|---|---|---|---|
| UC-DEMO-001-EP-08 | Định dạng chuẩn | Có | "f01@demo.test" | Lưu |
| UC-DEMO-001-EP-09 | Trống | Không | "" | MS-04 |
| UC-DEMO-001-EP-10 | Thiếu @ | Không | "lan.demo.test" | MS-05 |
| UC-DEMO-001-EP-11 | Thiếu tên miền | Không | "lan@" | MS-05 |
| UC-DEMO-001-EP-12 | Khoảng trắng ở giữa | Không | "lan nguyen@demo.test" | MS-05 |
| UC-DEMO-001-EP-13 | Khoảng trắng đầu/cuối | Có | "  v17@demo.test  " | Lưu "v17@demo.test" |
| UC-DEMO-001-EP-14 | Chữ hoa | Có | "V17@DEMO.TEST" | Lưu "v17@demo.test" |
| UC-DEMO-001-BV-06 | 254 ký tự | Có | 64 ký tự + "@" + tên miền 189 ký tự (mỗi nhãn ≤ 63) | Lưu |
| UC-DEMO-001-BV-07 | 255 ký tự | Không | 64 ký tự + "@" + tên miền 190 ký tự (mỗi nhãn ≤ 63) | MS-05 |

Trùng email (duy nhất) xử lý ở bảng quyết định §4.2 vì phụ thuộc trạng thái người dùng trùng.

### UC-DEMO-001-FD-03 · Vai trò
| ID | Lớp / giá trị | Hợp lệ | Giá trị test | Kết quả |
|---|---|---|---|---|
| UC-DEMO-001-EP-15 | Admin | Có | Admin | Tạo Admin (khi chưa đủ 5) |
| UC-DEMO-001-EP-16 | Member (mặc định) | Có | Member | Tạo Member |
| UC-DEMO-001-EP-17 | Ngoài danh sách, gửi qua API | Không | "Owner" | MS-13 |

## 4. Function

### 4.1 Kịch bản
- MF-01 → MF-04: tạo Member mới — Positive, P1, `@smoke`.
- AF-01: email của người dùng đang Deactivated — trùng với DT-01-R5.
- EF-01: dịch vụ email lỗi — Abnormal.
- EF-02: mất kết nối khi gửi — Abnormal.

### 4.2 Bảng quyết định UC-DEMO-001-DT-01 · tạo người dùng (BR-01, BR-02)

| | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| C1 Email đã tồn tại trong tenant | N | N | N | Y | Y |
| C2 Người dùng trùng email đang Deactivated | – | – | – | N | Y |
| C3 Vai trò chọn là Admin | N | Y | Y | – | – |
| C4 Tenant đã có 5 Admin | – | N | Y | – | – |
| Tạo người dùng Invited, hiện MS-07 | X | X | | | |
| Từ chối, hiện MS-10 | | | X | | |
| Từ chối, hiện MS-06 | | | | X | |
| Không tạo, hiện MS-08 | | | | | X |

- UC-DEMO-001-DT-01-R1 — dữ liệu: email mới; thêm một TC với "minh@demo.test" chỉ tồn tại ở T2 (BR-01 Positive).
- UC-DEMO-001-DT-01-R2 — T1 đang có 4 Admin (biên 4 → 5).
- UC-DEMO-001-DT-01-R3 — T3 đang có 5 Admin, trong đó 1 người Invited (biên 5 → 6, và kiểm luôn "tính cả Invited").
- UC-DEMO-001-DT-01-R4 — email trùng khác hoa thường: nhập "LAN@DEMO.TEST" khi T1 có "lan@demo.test".
- UC-DEMO-001-DT-01-R5 — nhập "old.user@demo.test" (Deactivated).

Kiểm tra đủ: C1 = N phủ bởi R1–R3 (C3 × C4, trong đó C3 = N thì C4 không ảnh hưởng); C1 = Y phủ bởi R4–R5 (C2). Không cột nào trùng điều kiện.

### 4.3 Chuyển trạng thái
- ST-USER-01 — tạo → Invited: kiểm ở TC luồng chính (cột Trạng thái "Đã mời").

### 4.4 Phân quyền (thêm chiều ranh giới dữ liệu)
| PM | Kiểm ở UI | Kiểm ở API |
|---|---|---|
| PM-USER-01 Admin tạo trong tenant mình | Luồng chính | — |
| PM-USER-02 Member tạo | Không thấy nút; URL → 403 | POST /api/users → 403 |
| PM-USER-03 Admin tạo sang tenant khác | — (UI không cho chọn tenant) | POST /api/users với `tenantId` = T2 → 403 |

### 4.5 Tác động phụ
SE-01 danh sách (trong TC luồng chính), SE-02 hộp thư test, SE-03 `GET /api/audit` — mỗi cái một TC riêng để lỗi ở email hoặc audit không làm fail TC luồng chính.

### 4.6 Đoán lỗi
| ID | Tình huống | Kết quả mong đợi | Nguồn của kết quả |
|---|---|---|---|
| UC-DEMO-001-EG-01 | Bấm "Gửi lời mời" hai lần liên tiếp | Chỉ một người dùng được tạo | Test basis §1.5 (nút bị tắt khi xử lý) |
| UC-DEMO-001-EG-02 | Tạo thành công rồi bấm Back của trình duyệt | Không tạo thêm người dùng | Test basis §1.5 + BR-01 |
| UC-DEMO-001-EG-03 | Hai Admin cùng tenant gửi cùng một email gần như đồng thời | Một người thành công, người kia nhận MS-06 | BR-01 |
| UC-DEMO-001-EG-04 | Hết phiên khi đang nhập, rồi bấm "Gửi lời mời" | Chuyển tới /login, không tạo người dùng | Test basis §1.5 |

## 5. Loại trừ và câu hỏi
- ST-USER-02 [THUỘC UC-DEMO-005]
- ST-USER-03 [THUỘC UC-DEMO-006]
- ST-USER-04 [THUỘC UC-DEMO-004]
- ST-USER-05 [THUỘC UC-DEMO-004]
- ST-USER-06 [THUỘC UC-DEMO-005]

Không có câu hỏi Q-T cho UC này.
