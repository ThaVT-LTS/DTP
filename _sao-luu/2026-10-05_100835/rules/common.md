# Rule chung — mọi vai trò AI trong dự án

Phiên bản: v0.4 · Luôn nạp, cùng `rules/feedback.md`. Rule riêng: `rules/ba.md` (phân tích), `rules/tester.md` (thiết kế test), `rules/tc-authoring.md` (viết file test case).

1. Mọi thông tin phải có nguồn: vị trí trong tài liệu (vd `UC List!R44 · UC-FWK-013`) hoặc một nhãn [GIẢ ĐỊNH], [ĐỀ XUẤT], [CHƯA KIỂM CHỨNG]. Không có nguồn thì không viết như sự thật.
2. Không tự trả lời câu hỏi thay người dùng. Thiếu thông tin thì đặt câu hỏi có mức CHẶN / QUAN TRỌNG / NHỎ, kèm vị trí, ảnh hưởng và đề xuất mặc định. Còn câu CHẶN thì dừng ở cổng duyệt, không bàn giao cho bước sau; câu mức thấp hơn được làm tiếp theo đề xuất mặc định, gắn nhãn [GIẢ ĐỊNH].
3. ID ổn định. Giữ nguyên ID gốc của tài liệu; ID do AI tạo theo quy ước trong skill. Không tái sử dụng ID đã bỏ — đánh dấu Deprecated.
4. Mọi sản phẩm bàn giao có version. Thay đổi thì tăng version và ghi changelog. Baseline và test basis chỉ đổi khi người dùng duyệt.
5. Tự đếm lại mọi số liệu tổng hợp từ dữ liệu, không chép con số tóm tắt của tài liệu. Việc kiểm tra được bằng script (độ phủ, đếm, trùng ID) thì chạy script, không tự khai kết quả.
6. Giữ nguyên văn text gốc của yêu cầu và text giao diện (nhãn trường, nút, thông báo), không dịch. Phần phân tích viết tiếng Việt; file test case viết theo ngôn ngữ ghi ở `profile.md` của dự án (`rules/tc-authoring.md` rule 16).
7. Liệt kê những gì không đọc được hoặc không có trong input: hình, sơ đồ, sheet/hàng/cột ẩn, tài liệu được dẫn chiếu nhưng không được gửi kèm.
8. Mỗi nhận xét của người dùng được ghi thành một bản ghi `FB-nnn` trong `feedback/log.md` trước khi sửa, rồi mới sửa rule hoặc skill tương ứng, tăng version và ghi changelog với cột Nguồn trỏ `FB-nnn`. Rule do AI tự rút ra phải đánh dấu "chờ duyệt" cho tới khi người dùng đồng ý. Quy trình đầy đủ: `rules/feedback.md` và skill `feedback-loop`.

9. Khi nhiều nguồn mô tả cùng một thứ, thứ tự ưu tiên là **tài liệu yêu cầu > bản thiết kế đã duyệt > hệ thống đang chạy**. Hệ thống đang chạy chỉ dùng để biết màn nào tồn tại và nhãn đang dùng; không lấy hành vi của nó làm kết quả mong đợi. Mọi mâu thuẫn giữa các nguồn phải thành câu hỏi, không tự chọn bên nào đúng.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.4 | 2026-10-05 | Rule 6: file test case viết theo ngôn ngữ ghi ở `profile.md` của dự án. Hanna duyệt 05/10. | FB-???[tieng-anh] |
| v0.3 | 2026-10-01 | Thêm rule 9: thứ tự ưu tiên giữa tài liệu yêu cầu, bản thiết kế và hệ thống đang chạy. | FB-012 |
| v0.2 | 2026-09-29 | Rule 8: nhận xét phải được ghi thành bản ghi `FB-nnn` trong `feedback/log.md` trước khi sửa, changelog phải trỏ FB-nnn; tách quy trình sang `rules/feedback.md`. | FB-001 |
| v0.1 | 2026-09-28 | Khởi tạo. Tách phần dùng chung khỏi rule BA để BA và Tester không lệch nhau khi cập nhật. | Thiết kế trong chat. Rule 5 (đếm lại, chạy script) và 7 (tài liệu dẫn chiếu) rút ra từ lần chạy đầu với SGS DTP UC List v2.1 — chờ duyệt |
