# Checklist câu hỏi làm rõ (dùng lại cho mọi UC)

- Phân quyền
- Dữ liệu và trạng thái ban đầu
- Validation và giá trị biên
- Text thông báo chính xác — nguyên văn, cần cho Playwright `toHaveText`
- Luồng ngoại lệ: mất mạng, timeout, trùng dữ liệu, bấm back/refresh giữa chừng, hết phiên đăng nhập
- Chuyển trạng thái — cần bảng transition đầy đủ (từ trạng thái nào, sự kiện gì, sang trạng thái nào, ai thực hiện), không chỉ liệt kê enum
- Số liệu cụ thể trong rule: giới hạn, làm tròn, múi giờ
- Kết quả có quan sát được không — "hệ thống lưu dữ liệu" phải cụ thể hoá thành "hiện toast X" hoặc "bản ghi xuất hiện ở danh sách Y", vì Playwright chỉ kiểm tra được thứ hiện lên màn hình.
