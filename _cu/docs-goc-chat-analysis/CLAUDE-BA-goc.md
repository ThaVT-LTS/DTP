# Rule — BA (luôn nạp)

- Mọi thông tin phải gắn nhãn `[UC: vị trí]`, `[GIẢ ĐỊNH]` hoặc `[ĐỀ XUẤT]`; không có nguồn thì không viết như sự thật.
- Không tự trả lời câu hỏi làm rõ. Câu mức **CHẶN** chưa trả lời → dừng, không bàn giao sang Code/Test. Câu mức thấp hơn → làm tiếp, gắn `[GIẢ ĐỊNH]`.
- Mọi phần tử phân tích phải có ID theo quy ước chung (`UC03-MF-04`, `AF-4a`, `EF-01`, `BR-12`). Đánh số bước cách quãng (10, 20, 30…) để chèn bước mới về sau mà không vỡ ID/tag.
- Text hiển thị / thông báo lỗi phải trích **nguyên văn** từ tài liệu gốc, không diễn giải. Không có text chính xác trong nguồn → đưa thành câu hỏi CHẶN, không tự bịa.
- Đề xuất (suggestion) không được đưa vào baseline hay test khi chưa được người dùng duyệt.
- Baseline chỉ thay đổi khi người dùng duyệt; mỗi lần đổi phải tăng version và ghi changelog.
- Hình, sơ đồ, bảng nào không đọc được phải liệt kê ra — không im lặng bỏ qua.
- Ghi kết quả ra file ngay khi xong mỗi UC/luồng — không để trôi trong lịch sử chat.

Quy trình chi tiết nằm ở skill `ba-analysis` (UC mới) và `ba-change-handling` (khi có thông tin mới) — rule này chỉ là ràng buộc luôn đúng, không lặp lại quy trình ở đây.
