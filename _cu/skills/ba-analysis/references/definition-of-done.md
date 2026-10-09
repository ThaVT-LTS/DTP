# Definition of Done — bàn giao BA → Code/Test

- Có đoạn đánh giá mục đích sản phẩm (bước 0).
- Mọi bước UC có ID.
- Không còn câu hỏi mức CHẶN đang mở.
- Mọi kết quả mong đợi đều quan sát được trên UI — không có "hệ thống xử lý ngầm" mà không có dấu hiệu quan sát được.
- Mỗi UC có đủ ba bảng đầu vào cho thiết kế test, hoặc ghi "N/A — lý do": (1) trường dữ liệu: bắt buộc, định dạng, độ dài và giá trị biên; (2) chuyển trạng thái: từ trạng thái nào, sự kiện gì, sang trạng thái nào, ai thực hiện; (3) vai trò × hành động: ai được làm, ai bị chặn.
- Baseline đã có version, lưu trong repo cạnh code test.

Không có tiêu chí này thì bước review không có thước đo để so. Nếu BA trích đúng nhãn trường, tên nút và text thông báo, bước Code dùng thẳng làm locator/assertion (`getByLabel`, `getByRole`, `toHaveText`) mà không phải đoán.
