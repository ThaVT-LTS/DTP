# Rule — BA (phân tích yêu cầu)

Phiên bản: v0.1 · Nạp cùng `rules/common.md` khi làm việc với tài liệu yêu cầu (`docs/`). Quy trình chi tiết: skill `ba-analysis`.

1. Đọc tài liệu theo hai lượt có sản phẩm: lượt 1 trích xuất nguyên văn (không tóm tắt), lượt 2 đối soát hai chiều. Không báo "đã đọc kỹ" khi chưa có hai sản phẩm này.
2. Đề xuất của AI không được đi vào baseline hay test basis khi chưa được duyệt; đề xuất làm thay đổi yêu cầu phải quay lại thành câu hỏi.
3. Mỗi UC phải được xếp vào một trong ba nhóm: trong phạm vi test, ngoài phạm vi, chưa đủ thông tin — kèm lý do và nguồn.
4. Chỉ xuất test basis khi không còn câu CHẶN và mọi UC trong phạm vi có đủ các phần bắt buộc của template (đường vào/ra, trường dữ liệu, thông báo, luồng, business rule, tác động phụ, phân quyền, trạng thái), hoặc ghi rõ `[KHÔNG ÁP DỤNG]` / `[CHỜ Q-nn]` cho phần thiếu.
5. Nhãn trường, tên nút, text thông báo phải được chép nguyên văn vào test basis. Tester dùng chúng làm kết quả mong đợi, bước Code dùng làm locator và assertion.
6. Có thông tin mới sau baseline thì phân tích ảnh hưởng trước, không sửa baseline trực tiếp. Mọi thay đổi phải truy vết được tới ID bị ảnh hưởng để Tester tìm đúng test case cần sửa.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-09-28 | Khởi tạo. Rule nhãn nguồn, câu hỏi, ID, version chuyển sang `common.md`. Thêm rule 3–5 về phân loại phạm vi và điều kiện xuất test basis. | Thiết kế trong chat lượt 1 và yêu cầu "BA xuất tài liệu gửi Tester" — rule 4, 5 chờ duyệt |
