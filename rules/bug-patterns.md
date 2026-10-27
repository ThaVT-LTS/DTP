# Mẫu lỗi do người dùng phát hiện khi test tay — dùng khi thiết kế TC và khi chạy

> Nguồn: rule 29 của `automation.md`. Mỗi lần người dùng báo một bug bằng tay, thêm một dòng ở đây (mẫu tổng quát + cách kiểm + mã ví dụ), rồi thêm case vào file TC.
> Skill `test-design`, `tc-authoring`, `design-check` đọc file này: mỗi màn hình mới phải có case cho các mẫu áp dụng được.

| # | Mẫu lỗi (tổng quát) | Cách kiểm trên mọi màn | Ví dụ (mã bug, ngày) |
|---|---|---|---|
| 1 | Danh sách thả xuống / ô chọn nhiều không cuộn được khi nhiều mục | Tạo ≥ 15 mục, mở dropdown, cuộn tới mục cuối và chọn được | SC-BUG-04 (22/10) |
| 2 | Đường kẻ, khung trang trí trông như một ô nhập trống | Mọi đường kẻ / divider phải tách khối rõ ràng (khoảng trắng, màu nhạt đúng token), không nằm sát dưới dòng gợi ý | SC-BUG-05 (23/10) |
| 3 | Thẻ lựa chọn: dòng chính (đậm) không phải thứ người dùng vừa tìm / nhận ra | Dòng đậm = tên đối tượng người dùng tìm (vd tên framework); thông tin phụ (phiên bản, edition) ở dòng nhỏ | WS-BUG-04 (23/10) |
| 4 | Menu ⋮ của dòng không theo trạng thái, hoặc có mục thừa | Menu chỉ có thao tác hợp lệ với trạng thái của dòng (vd Active trống: Archive · Delete; Active đã dùng: Archive; Archived: không có ⋮); không lặp "Open" khi bấm dòng đã mở | WS-BUG-05 (23/10) |
| 5 | Nhãn bộ lọc hứa nhiều hơn những gì danh sách hiện | Nhãn lựa chọn khớp đúng dữ liệu hiện ra (vd không ghi "and deleted" khi mục đã xoá không bao giờ hiện) | WS-BUG-06 (23/10) |
| 6 | Hai cách thêm cùng loại dữ liệu không đồng nhất (một cái chọn nhiều, một cái chọn một) | So sánh Upload / Link / Import cùng đối tượng: nếu một cách cho nhiều mục thì cách kia cũng cho chọn nhiều (checkbox) | WD-BUG-19 (23/10) |
| 7 | Danh sách chọn trộn mục chọn được với mục bị khoá | Mục có nút chọn bật được lên trên, mục bị khoá (đã link, không đủ điều kiện) xuống dưới; dựa theo đúng điều kiện bật/tắt nút | WD-BUG-20 (23/10) |
| 8 | Giờ hiển thị sai múi giờ / không thống nhất giữa các màn | Thao tác lúc giờ biết trước, so mọi nhãn thời gian (Last updated, Last sync, cycle, activity) với giờ Đài Loan (UTC+8) | FW-BUG-17 (23/10) |
| 9 | Wizard nhiều bước: Back làm mất dữ liệu đã nhập / file đã tải | Ở mỗi bước bấm Back rồi Next: dữ liệu, file vẫn còn; bấm nhanh hai lần không nhảy quá bước | FW-BUG-16 (22/10) |
| 10 | Ảnh trong email (logo) không hiện | Trước khi log: bấm "Show blocked content" của Outlook; chỉ là bug nếu vẫn không hiện (link ảnh ngoài bị client chặn) | (không log, 22/10) |
| 11 | Dialog/drawer dài phải cuộn vì trường chọn ít lựa chọn (radio) xếp dọc | Mở mọi form tạo/sửa ở 1920×1080: radio ≤ 4 lựa chọn ngắn nên xếp 1 hàng ngang; form không phải cuộn mới thấy nút | SC-BUG-08 (26/10) |
| 12 | Ô chọn (dropdown) danh sách dài không cho gõ để tìm, hoặc chỉ tải 100 mục đầu | Mọi dropdown chọn scope/workspace/user/khách hàng: gõ một phần tên phải lọc được; tạo > 100 mục và chọn được mục cuối | BU-BUG-20 (26/10), DC_041, Scope_125 |
| 13 | Giá trị gán cứng trong code lệch UC hoặc cắt dữ liệu (limit 100 không tìm kiếm / phân trang, số ngày · MB · số file viết thẳng, tên tổ chức / ID cố định, text không qua i18n, bộ lọc mặc định làm ẩn dữ liệu) | Trước mỗi lượt chạy hoặc khi có build mới: quét code theo skill `hardcode-check` (`git show` trên commit đang deploy, không mặc định `origin/main`), lập bảng chỗ → màn → giá trị, so với bảng giá trị của UC; chỗ lệch hoặc cắt dữ liệu thì thêm case vào TC và kiểm trên web | BU-BUG-20 (26/10), quét code 26/10 |
| 13 | Email song ngữ: phần tiếng Trung còn chữ tiếng Anh (vai trò, nút), chân trang viết cứng tên affiliate | Mở mail thật (mời, thông báo) với mỗi vai trò: kiểm từng câu, nút, footer ở cả EN và zh-TW; tên affiliate lấy từ dữ liệu | NO-BUG-03 (26/10) |
| 14 | Mục đã archive / chỉ đọc vẫn mời làm thao tác ghi (nút, link hoặc câu hướng dẫn trong thông báo như "… with Send additional documents") | Sau khi archive / khoá: đọc hết nút, menu **và chữ trong mọi khung thông báo** của màn; không còn thao tác ghi nào được hiện hay được nhắc tới | BU-BUG-22 (27/10) |
