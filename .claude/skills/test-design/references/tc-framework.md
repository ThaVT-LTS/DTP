# Khung test case — Redirect · Validation · Function

Mục lục: §0 Nguyên tắc · §1 Redirect · §2 Validation · §3 Function · §4 Phân quyền (chiều cắt ngang) · §5 Đặt tên và ưu tiên

---

## §0 Nguyên tắc

Mỗi UC có đủ ba nhóm. Nhóm không áp dụng thì ghi một dòng trong file thiết kế, vd `- UC-XXX-nnn [KHÔNG ÁP DỤNG: Validation — màn hình chỉ xem, không có trường nhập]`.

| Nhóm | Trả lời câu hỏi | Nguồn trong test basis | Kỹ thuật chính |
|---|---|---|---|
| **Redirect** | Vào được bằng những đường nào, ai bị chặn, khi đến thấy gì, rời đi về đâu? | NV, PM (quyền vào màn hình) | Ma trận điều hướng × vai trò, đoán lỗi |
| **Validation** | Mỗi trường nhận gì, từ chối gì, báo lỗi ra sao, lưu xuống có đúng không? | FD, MS | Phân vùng tương đương, giá trị biên, bảng quyết định (ràng buộc giữa các trường) |
| **Function** | Luồng, rule, trạng thái, tác động phụ có đúng không — kể cả khi đi sai hoặc có sự cố? | MF, AF, EF, BR, SE, ST, PM (quyền hành động) | Kịch bản use case, bảng quyết định, chuyển trạng thái, CRUD, pairwise, đoán lỗi |

Mỗi TC mang một **loại**:

| Loại | Nghĩa | Ví dụ |
|---|---|---|
| **Positive** (happy case) | Đi đúng đường, dữ liệu hợp lệ, có quyền | Admin tạo người dùng với dữ liệu hợp lệ → tạo thành công |
| **Negative** | Người dùng cố tình hoặc vô tình làm sai: dữ liệu không hợp lệ, vi phạm rule, không có quyền, trạng thái không cho phép | Nhập email sai định dạng; Member mở thẳng URL trang tạo người dùng |
| **Abnormal** | Sự cố ngoài ý muốn người dùng: mất mạng, timeout, dịch vụ ngoài lỗi, thao tác đồng thời, bấm hai lần, back/refresh giữa chừng, hết phiên | Dịch vụ email lỗi khi gửi lời mời |

Negative kiểm hệ thống có **chặn đúng** không; Abnormal kiểm hệ thống có **chịu được** sự cố không. Tách hai loại để không bỏ quên loại thứ hai — đây là nhóm bug hay lọt nhất vì tài liệu ít khi viết ra.

---

## §1 Redirect — đường vào, đường ra, trạng thái khi đến

**Mục tiêu:** người dùng đến được chức năng bằng mọi đường hợp lệ, bị chặn ở mọi đường không hợp lệ, thấy đúng trạng thái khi đến, và rời đi đúng nơi.

**Cách làm:** lập ma trận điều hướng trong file thiết kế: mỗi dòng NV × mỗi vai trò liên quan × trạng thái dữ liệu (nếu ảnh hưởng). Mỗi ô có kết quả khác nhau → một TC.

### R1. Đường vào hợp lệ — mỗi đường một TC
- [ ] Menu / sidebar / tab.
- [ ] Nút hoặc link từ màn hình khác (ghi rõ màn hình nguồn): nút "Tạo mới" ở danh sách, link ở màn hình chi tiết, breadcrumb.
- [ ] URL trực tiếp (deep link), kể cả URL có tham số (id, bộ lọc, trang).
- [ ] Link trong thông báo in-app hoặc email.
- [ ] Link chia sẻ ra ngoài (nếu có) — mở được không cần đăng nhập?
- [ ] Sau đăng nhập quay lại đúng trang đã yêu cầu (return URL).
- [ ] Mở trong tab mới; mở từ lịch sử trình duyệt.

### R2. Trạng thái khi đến
- [ ] Tiêu đề trang, breadcrumb, menu đang chọn.
- [ ] Giá trị mặc định của từng trường; focus đầu tiên.
- [ ] Dữ liệu được nạp đúng đối tượng theo id trên URL.
- [ ] Nút bật/tắt đúng (vd "Lưu" bị tắt khi chưa nhập gì).
- [ ] Danh sách rỗng hiển thị empty state; danh sách có dữ liệu hiển thị đúng phân trang và sắp xếp mặc định.

### R3. Chặn truy cập — Negative
- [ ] Chưa đăng nhập → chuyển tới đăng nhập.
- [ ] Vai trò không có quyền → trang 403 / thông báo / không thấy menu (theo PM).
- [ ] Đổi id trên URL sang dữ liệu của tenant khác (IDOR) → bị chặn, không lộ dữ liệu.
- [ ] Dữ liệu ngoài scope / affiliate / phân công của người dùng → bị chặn.
- [ ] Đối tượng không tồn tại hoặc đã xóa → 404 hoặc thông báo.
- [ ] Đối tượng ở trạng thái không cho phép (vd mở trang sửa của bản ghi đã đóng) → chặn hoặc chỉ xem.
- [ ] Menu/nút bị ẩn với vai trò không có quyền **và** URL tương ứng cũng bị chặn — kiểm cả hai, vì ẩn nút không phải là phân quyền.

### R4. Đường ra
- [ ] Lưu thành công → về đâu, thông báo gì (text nguyên văn).
- [ ] Hủy / đóng → về đâu; còn thay đổi chưa lưu thì có hộp thoại xác nhận không.
- [ ] Nút Back của trình duyệt sau khi submit → không gửi lại dữ liệu, không lỗi trang.
- [ ] Refresh (F5) → dữ liệu đã nhập còn hay mất, có cảnh báo không.

### R5. Phiên và ngữ cảnh — Abnormal
- [ ] Hết phiên khi đang ở trang → hành động tiếp theo chuyển tới đăng nhập, không mất dữ liệu âm thầm.
- [ ] Đăng xuất ở tab khác.
- [ ] Người dùng có nhiều tenant/vai trò: đổi ngữ cảnh thì trang hiện tại xử lý ra sao.

---

## §2 Validation — dữ liệu nhập

**Mục tiêu:** mọi trường nhận đúng giá trị hợp lệ, từ chối giá trị không hợp lệ với đúng thông báo, và dữ liệu lưu xuống đúng như đã nhập.

**Cách làm:** với mỗi FD, lập bảng phân vùng tương đương (EP) và giá trị biên (BV) theo `techniques.md` §1–2, rồi áp checklist dưới đây để không sót lớp. Mỗi lớp không hợp lệ một TC riêng. Nhiều lớp hợp lệ có thể gộp vào một TC Positive.

### V1. Checklist chung cho mọi trường
- [ ] **Bắt buộc:** để trống; chỉ nhập khoảng trắng. Trường không bắt buộc: để trống vẫn lưu được.
- [ ] **Độ dài:** min−1, min, max, max+1 (thêm min+1, max−1 khi rule nhạy cảm). Dán (paste) chuỗi dài hơn max: bị cắt hay báo lỗi?
- [ ] **Khoảng trắng:** đầu/cuối được trim không; độ dài tính trước hay sau trim; nhiều khoảng trắng giữa.
- [ ] **Ký tự:** chữ có dấu tiếng Việt; ký tự CJK (Trung, Nhật, Hàn); emoji; ký tự đặc biệt; xuống dòng trong trường một dòng.
- [ ] **Chuỗi nguy hiểm:** `<script>alert(1)</script>` → lưu và hiển thị dạng text, không thực thi; `' OR 1=1 --` → không lỗi hệ thống.
- [ ] **Duy nhất:** giá trị đã tồn tại; khác hoa/thường; trùng sau khi trim; trùng với bản ghi đã xóa hoặc vô hiệu hóa; trùng ở tenant khác (được hay không).
- [ ] **Thời điểm báo lỗi:** khi rời trường, khi gõ, hay khi bấm lưu; lỗi biến mất khi sửa đúng; nhiều lỗi cùng lúc hiển thị đủ.
- [ ] **Thông báo:** text nguyên văn, vị trí, ngôn ngữ.
- [ ] **Giá trị lưu xuống:** lưu xong mở lại thấy đúng giá trị (không bị cắt, không đổi dấu, không đổi múi giờ).
- [ ] **Phía server** (khi tester được gọi API, viết ở sheet `API`): gửi request thẳng tới API bỏ qua kiểm tra trên UI → server vẫn từ chối. Validation chỉ có ở UI là bug bảo mật.

### V2. Theo kiểu dữ liệu
| Kiểu | Cần thử thêm |
|---|---|
| Số | âm, 0, thập phân, dấu phân cách hàng nghìn, số rất lớn, chữ, min−1 / min / max / max+1, số 0 ở đầu |
| Ngày, giờ | sai định dạng, ngày không tồn tại (31/02), năm nhuận, quá khứ/tương lai theo rule, từ ngày > đến ngày, biên hôm qua / hôm nay / ngày mai, múi giờ người dùng khác múi giờ máy chủ |
| Email | thiếu @, thiếu tên miền, có khoảng trắng, hai dấu chấm liền, độ dài tối đa (254), hoa/thường |
| Mật khẩu | từng điều kiện của chính sách, đúng min/max, ẩn/hiện, dán vào |
| Dropdown, radio, checkbox | giá trị mặc định; danh sách đúng nguồn; giá trị đã vô hiệu hóa không xuất hiện; bắt buộc chọn; gửi giá trị ngoài danh sách qua API (sheet `API`, khi tester được gọi API) |
| File upload | loại cho phép theo đuôi **và** theo nội dung thật (đổi đuôi .exe → .pdf); dung lượng max−1 / max / max+1 byte, file 0 byte; số lượng file tối đa; tên file dài, có dấu, ký tự đặc biệt; trùng tên; file hỏng; ngắt mạng giữa chừng |
| Trường phụ thuộc | bật/tắt theo trường khác; bắt buộc có điều kiện (dùng bảng quyết định); danh sách con lọc theo trường cha; đổi trường cha thì trường con reset không |

### V3. Ràng buộc giữa nhiều trường
Khi rule nói "nếu A thì B bắt buộc" hoặc "A phải nhỏ hơn B" → lập bảng quyết định (`techniques.md` §3), mỗi rule một TC.

---

## §3 Function — luồng nghiệp vụ

**Mục tiêu:** mọi luồng, rule, chuyển trạng thái và tác động phụ cho kết quả đúng, kể cả khi đi sai hoặc có sự cố.

### F1. Luồng — kịch bản use case
- [ ] **Positive:** luồng chính end-to-end với dữ liệu hợp lệ điển hình. Mỗi vai trò được phép có hành vi khác nhau → một TC riêng.
- [ ] **Positive:** mỗi luồng thay thế (AF) một TC.
- [ ] **Abnormal:** mỗi luồng ngoại lệ (EF) một TC.

### F2. Business rule — bảng quyết định
- [ ] Mỗi rule (cột) của bảng quyết định một TC.
- [ ] Mỗi BR có ít nhất một TC thỏa rule (Positive) và một TC vi phạm rule (Negative).
- [ ] Rule có con số (tối đa 5, trong 30 ngày, tối đa 1 active) → áp giá trị biên cho con số đó: 4 / 5 / 6, ngày 29 / 30 / 31, 0 / 1 / 2.

### F3. Trạng thái — chuyển trạng thái
- [ ] Mỗi chuyển hợp lệ một TC: đúng người làm, trạng thái sau đúng, tác động phụ đúng.
- [ ] Chuyển không hợp lệ quan trọng: nút không hiện; gọi API thẳng bị từ chối thì kiểm ở sheet `API` khi tester được gọi API.
- [ ] Đúng chuyển nhưng sai người (vai trò không được phép) → bị chặn.
- [ ] Chuỗi chuyển quan trọng (vd gửi → trả về → gửi lại → duyệt) một TC.

### F4. Tác động phụ và dữ liệu liên UC — ma trận CRUD
- [ ] Sau hành động, dữ liệu cập nhật đúng ở màn hình khác: danh sách, chi tiết, dashboard, bộ đếm.
- [ ] Thông báo gửi đúng người nhận, đúng nội dung; người không liên quan không nhận.
- [ ] Audit ghi đúng người, hành động, thời điểm, đối tượng.
- [ ] Xóa hoặc đổi trạng thái đối tượng đang được UC khác tham chiếu → UC kia hiển thị gì.

### F5. Danh sách, tìm kiếm, lọc, sắp xếp, phân trang
- [ ] 0 bản ghi, 1 bản ghi, đúng một trang, một trang + 1, trang cuối.
- [ ] Tìm kiếm: khớp đúng, khớp một phần, có dấu/không dấu, hoa/thường, ký tự đặc biệt, không có kết quả.
- [ ] Nhiều bộ lọc kết hợp → pairwise (`techniques.md` §8).
- [ ] Danh sách chỉ hiện dữ liệu người dùng được quyền thấy (tenant, scope, phân công).

### F6. Abnormal — sự cố
- [ ] Bấm nút gửi hai lần liên tiếp → chỉ tạo một bản ghi.
- [ ] Mất mạng hoặc timeout khi gửi → thông báo, không tạo nửa chừng; gửi lại không tạo trùng.
- [ ] Hai người sửa cùng bản ghi → cơ chế xử lý xung đột theo test basis (khóa, cảnh báo, ghi đè).
- [ ] Bản ghi bị người khác xóa hoặc đổi trạng thái trong lúc mình đang thao tác.
- [ ] Dịch vụ ngoài lỗi hoặc chậm (API tích hợp, email, lưu trữ file).
- [ ] Back / refresh giữa luồng nhiều bước.
- [ ] Hết phiên giữa luồng.

---

## §4 Phân quyền — chiều cắt ngang

Phân quyền không phải nhóm riêng mà là một chiều áp lên cả Redirect và Function:
- **Redirect:** ai vào được màn hình (R3).
- **Function:** ai làm được hành động, trên dữ liệu nào (PM).

Mỗi dòng PM "Được phép = Có" cần ít nhất một TC Positive; mỗi dòng "Không" cho hành động ghi dữ liệu cần một TC Negative kiểm giao diện (nút ẩn hoặc tắt, mở thẳng URL bị chặn); khi tester được gọi API thì thêm TC gọi thẳng API bị từ chối, ở sheet `API`. Với hệ thống nhiều tenant, luôn có TC cho dữ liệu của tenant khác, scope khác và người không được phân công.

---

## §5 Đặt tên và ưu tiên

- ID: `<UC-ID>-TC-<R|V|F><nn>` — vd `UC-EVD-008-TC-V07`. Số thứ tự không tái sử dụng.
- Tiêu đề: `<đối tượng> <điều kiện> <kết quả>` — vd "Họ và tên 51 ký tự bị từ chối", "Member mở URL tạo người dùng bị chặn".
- Ưu tiên:
  - **P1** — luồng chính, phân quyền, dữ liệu và bảo mật; lỗi ở đây chặn nghiệp vụ hoặc lộ dữ liệu.
  - **P2** — luồng thay thế, business rule, validation của trường chính.
  - **P3** — hiển thị, trường hợp hiếm, trường phụ.
- Tag: `@<UC-ID> @<redirect|validation|function> @<positive|negative|abnormal> @P<n>`, thêm `@smoke` cho P1 Positive của luồng chính.
