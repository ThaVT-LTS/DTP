# Mẫu test basis — tài liệu BA bàn giao cho Tester

File: `docs/test-basis/<tên>.v<x.y>.md`. Sinh ở bước 5 từ baseline đã duyệt. Tester chỉ thiết kế test từ file này.

Mỗi bảng tương ứng một nhóm test case của Tester: **Đường vào/ra → Redirect**, **Trường dữ liệu + Thông báo → Validation**, **Luồng + Rule + Tác động phụ + Trạng thái + Phân quyền → Function**. Mọi dòng có ID (quy ước ID trong SKILL.md) vì script kiểm tra độ phủ của Tester đọc các ID này. Phần chưa có thông tin ghi `[CHỜ Q-nn]`; phần không liên quan ghi `[KHÔNG ÁP DỤNG]` kèm lý do; phần thuộc UC khác ghi `[THUỘC UC-...]`.

---

```markdown
# Test basis — <dự án / module> v<x.y>

| | |
|---|---|
| Baseline nguồn | docs/baseline/<tên>.v<x.y>.md |
| Ngày | YYYY-MM-DD |
| Trạng thái | Sẵn sàng thiết kế / Sẵn sàng một phần (liệt kê UC chưa đủ) |
| Giả định còn hiệu lực | Q-07, Q-11 (đề xuất mặc định) ... |
| Câu hỏi còn mở (không CHẶN) | Q-16, Q-18 ... |

## 0. Tóm tắt bàn giao
- Phạm vi: <n> UC trong phạm vi · <n> ngoài · <n> chưa đủ thông tin (danh sách ở §3)
- Ưu tiên test (theo rủi ro): <UC, lý do>
- Điểm dễ sai: <ID, lý do>

## 1. Dùng chung

### 1.1 Vai trò
| Vai trò | Mô tả | Cổng | Tài khoản test cần có |
|---|---|---|---|

### 1.2 Ma trận phân quyền
| ID | Vai trò | Hành động | Đối tượng | Phạm vi dữ liệu | Được phép | Khi bị chặn thì thấy gì |
|---|---|---|---|---|---|---|
| PM-SRQ-01 | Customer User | Hủy | Service Request | của tổ chức mình | Có | — |
| PM-SRQ-02 | Customer User | Hủy | Service Request | của tổ chức khác | Không | 404 "<text>" |

Ghi cả dòng "Không" — đó là nguồn của test phân quyền negative.

### 1.3 Mô hình trạng thái
#### <Đối tượng>: <danh sách trạng thái>
| ID | Từ | Sự kiện / hành động | Sang | Ai được làm | Điều kiện | Hợp lệ |
|---|---|---|---|---|---|---|
| ST-SRQ-01 | Submitted | Accept | Accepted | SGS User | — | Có |
| ST-SRQ-09 | Closed | Cancel | — | Customer Admin | — | Không → "<text>" |

Liệt kê cả chuyển không hợp lệ quan trọng và hệ thống phản ứng thế nào.

### 1.4 Thuật ngữ
| Thuật ngữ | Nghĩa | Không nhầm với |
|---|---|---|

### 1.5 Quy ước chung
Định dạng ngày giờ và múi giờ; phân trang (số dòng mặc định); sắp xếp mặc định; thời gian hết phiên; thông báo lỗi chung (mất mạng, lỗi máy chủ, 403, 404) — nguyên văn.

### 1.6 Môi trường và dữ liệu test
Tenant, affiliate, tài khoản theo vai trò; tích hợp ngoài và cách mock; cách kích hoạt job định kỳ; dữ liệu do bên ngoài cung cấp.

## 2. Từng UC

### UC-XXX-nnn · <tên nguyên văn> — Ưu tiên P1/P2/P3
Rủi ro: <vì sao dễ sai> · Actor: <vai trò> (PM-...) · Tiền điều kiện: ...

#### Đường vào / ra → Redirect
| ID | Từ đâu | Cách vào / ra | Vai trò | Trạng thái dữ liệu | Kết quả (đích, text, trạng thái khi đến) |
|---|---|---|---|---|---|
| UC-XXX-nnn-NV-01 | Menu "<nhãn>" | Bấm menu | Admin | — | Mở "<tiêu đề màn hình>", URL /... |
| UC-XXX-nnn-NV-02 | URL trực tiếp | Nhập /... | Chưa đăng nhập | — | Chuyển tới đăng nhập, sau đó quay lại /... |

Trạng thái khi đến: tiêu đề, giá trị mặc định, nút bật/tắt, danh sách rỗng hiển thị gì.

#### Trường dữ liệu → Validation
| ID | Nhãn (nguyên văn) | Kiểu | Bắt buộc | Độ dài min–max | Giá trị / khoảng | Định dạng, ký tự cho phép | Mặc định | Duy nhất | Phụ thuộc | Thông báo (ID) |
|---|---|---|---|---|---|---|---|---|---|---|
| UC-XXX-nnn-FD-01 | Họ và tên | Text | Có | 2–50 (sau trim) | — | Chữ có dấu, khoảng trắng, ' - | Trống | Không | — | MS-01, MS-02, MS-03 |

#### Thông báo và text giao diện
| ID | Khi nào | Text nguyên văn | Vị trí |
|---|---|---|---|
| UC-XXX-nnn-MS-01 | Để trống Họ và tên | Vui lòng nhập họ và tên. | Dưới trường |

#### Luồng → Function
- UC-XXX-nnn-MF-01: ...
- UC-XXX-nnn-AF-01 (rẽ từ MF-03): ...
- UC-XXX-nnn-EF-01 (tại MF-04): ...

#### Business rule
| ID | Rule (nguyên văn) | Điều kiện | Kết quả khi thỏa | Kết quả khi vi phạm (MS) |
|---|---|---|---|---|

#### Tác động phụ và hậu điều kiện
| ID | Sau hành động | Thấy ở đâu / ai nhận | Nội dung |
|---|---|---|---|
| UC-XXX-nnn-SE-01 | Tạo thành công | Danh sách "<tên>" | Bản ghi mới ở đầu, trạng thái "<text>" |

#### Ghi chú cho Tester
Giả định đang áp dụng, điểm dễ sai, phần `[CHỜ Q-nn]`.

## 3. Ngoài phạm vi và chưa đủ thông tin
| UC | Nhóm | Lý do / câu hỏi |
|---|---|---|
```

---

## Checklist "Sẵn sàng bàn giao" (BA tự chạy trước khi giao)

- [ ] Không còn câu CHẶN mở; giả định còn hiệu lực được liệt kê ở đầu file.
- [ ] Mỗi UC trong phạm vi có ít nhất một dòng NV, và có dòng cho vai trò không được vào.
- [ ] Mỗi UC có nhập liệu có bảng FD đủ cột; mỗi quy tắc validation trỏ tới một MS có text nguyên văn.
- [ ] Mỗi UC có MF; AF và EF có ID (hoặc ghi "không có").
- [ ] Mỗi BR ghi rõ kết quả khi thỏa và khi vi phạm.
- [ ] Mỗi đối tượng có trạng thái có bảng ST, gồm cả chuyển không hợp lệ quan trọng.
- [ ] Ma trận PM có cả dòng "Không" cho các hành động ghi dữ liệu và cho dữ liệu ngoài phạm vi (tenant, scope, phân công).
- [ ] Mỗi SE nói rõ thấy ở đâu (màn hình, người nhận) — quan sát được.
- [ ] Mọi text UI chép nguyên văn; không có từ mơ hồ trong danh sách của gap-checklist.
- [ ] Phần thiếu ghi `[CHỜ Q-nn]` / `[KHÔNG ÁP DỤNG]` / `[THUỘC UC-...]`, không để trống.
