# Checklist soát lỗ hổng — BA

Dùng ở bước 2. Mỗi mục trả lời được bằng "có / không / không áp dụng"; mục "không" thành phát hiện F-nn. Các mục đánh dấu **→R**, **→V**, **→F** là thứ Tester sẽ cần cho nhóm Redirect, Validation, Function — thiếu ở đây thì Tester không viết được TC.

## A. Mức tài liệu (đặc biệt với danh sách UC)
- [ ] Số lượng tóm tắt khớp số đếm thực tế ở từng sheet/mục.
- [ ] Công thức tổng bao phủ đủ các nhóm (không sót dòng section mới thêm).
- [ ] ID liên tục; ID bị thiếu có lý do; không trùng; không có khoảng trắng thừa.
- [ ] Mỗi UC có đủ tên, actor, mô tả, nguồn yêu cầu, trạng thái phạm vi.
- [ ] Tên khớp mô tả; tên không bị chép nhầm từ cột khác; dữ liệu nằm đúng cột.
- [ ] Không có hai UC cùng chức năng.
- [ ] Không còn ý kiến trái chiều chưa giải quyết về phạm vi (vd bên A đề xuất lùi, bên B muốn giữ).
- [ ] Tên vai trò thống nhất và số vai trò khớp mô hình phân quyền.
- [ ] Portal khớp actor (vai trò phía SGS không nằm ở UC chỉ có Customer Portal và ngược lại).
- [ ] Mọi mục "still to confirm", Q&A còn mở đã được liệt kê.

## B. Liên UC
- [ ] UC trong phạm vi không phụ thuộc UC ngoài phạm vi, hoặc có cách thay thế được ghi rõ.
- [ ] Mỗi đối tượng có đủ vòng đời trong phạm vi: tạo, xem, sửa, đổi trạng thái, xóa hoặc lưu trữ. Thiếu thao tác nào thì hỏi (vd tạo được nhưng không sửa được, không xóa được). **→F**
- [ ] Một khái niệm chỉ có một tên gọi; một tên gọi chỉ có một nghĩa.
- [ ] Trạng thái của cùng một đối tượng qua nhiều UC ghép lại thành một bảng chuyển trạng thái đầy đủ: ai chuyển, từ đâu sang đâu, điều kiện. **→F**
- [ ] Quy tắc giới hạn (tối đa, duy nhất, chỉ một) không mâu thuẫn với luồng khác.
- [ ] Quyền xem và sửa cùng một dữ liệu nhất quán giữa các UC (vd danh sách hiện đủ bản ghi nhưng màn hình chi tiết giới hạn theo scope). **→R →F**

## C. Mức UC (khi có UC spec)
- [ ] Đường vào: menu, URL, nút/link từ màn hình khác, link trong thông báo/email, link chia sẻ, quay lại sau đăng nhập. **→R**
- [ ] Đường ra: sau khi lưu, hủy, đóng thì về đâu; có hỏi xác nhận khi còn thay đổi chưa lưu không. **→R**
- [ ] Trạng thái khi đến: giá trị mặc định, dữ liệu được nạp, nút bật/tắt, danh sách rỗng hiển thị gì. **→R**
- [ ] Ai không được vào, và khi cố vào thì thấy gì (403, ẩn menu, chuyển trang). **→R**
- [ ] Mỗi trường có: nhãn nguyên văn, kiểu, bắt buộc, độ dài tối thiểu/tối đa, khoảng giá trị, định dạng, ký tự cho phép, mặc định, duy nhất (phân biệt hoa thường?), phụ thuộc trường khác. **→V**
- [ ] Mỗi lỗi validation có text thông báo nguyên văn và vị trí hiển thị. **→V**
- [ ] File upload: loại, dung lượng tối đa, số lượng, trùng tên. **→V**
- [ ] Luồng chính, luồng thay thế, luồng ngoại lệ đều có ID. **→F**
- [ ] Ngoại lệ đã tính: mất mạng, timeout, trùng dữ liệu, bấm hai lần, back/refresh giữa chừng, hết phiên, hai người sửa cùng lúc, dịch vụ ngoài lỗi. **→F**
- [ ] Số liệu trong rule cụ thể: giới hạn, làm tròn, múi giờ, mốc thời gian, "trước/sau" tính theo ngày nào. **→V →F**
- [ ] Hậu điều kiện quan sát được: thông báo gì, bản ghi xuất hiện ở đâu, ai nhận thông báo, audit ghi gì. **→F**

## D. Khả năng kiểm thử
- [ ] Mọi kết quả mong đợi quan sát được qua UI; nếu không thì có API hoặc DB để kiểm chứng.
- [ ] Có ma trận phân quyền làm căn cứ cho test phân quyền.
- [ ] Tích hợp ngoài có sandbox hoặc mock. Lưu ý: API gọi từ server thì Playwright không chặn được bằng `page.route`, cần mock phía backend.
- [ ] Job định kỳ có cách kích hoạt hoặc chỉnh thời gian trong môi trường test.
- [ ] Dữ liệu test cần bên ngoài cung cấp đã được xác định (ai, khi nào).
- [ ] Môi trường có đủ dữ liệu để test ranh giới (ít nhất hai tenant, hai affiliate...).

## Từ ngữ mơ hồ — gặp là đánh dấu
Tiếng Anh: such as, etc., relevant, appropriate, sensitive, supported, where permitted, where applicable, as needed, user-friendly, fast, valid, proper, permitted transitions, retention policy (khi không định nghĩa).
Tiếng Việt: v.v., phù hợp, hợp lệ, nhanh, các thông tin cần thiết, một số, khi cần, tương ứng, theo quy định (khi không dẫn quy định nào).
