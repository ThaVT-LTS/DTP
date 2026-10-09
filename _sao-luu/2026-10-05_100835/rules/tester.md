# Rule — Tester (thiết kế test)

Phiên bản: v0.3 · Nạp cùng `rules/common.md` và `rules/feedback.md` khi làm việc với test case. Kỹ thuật thiết kế: skill `test-design`. Tổ chức và định dạng file bàn giao: `rules/tc-authoring.md` và skill `tc-authoring`.

1. Chỉ thiết kế từ test basis đã có version. Test basis không nói thì không tự đặt kết quả mong đợi — hỏi ngược BA bằng câu hỏi `Q-T-nn`.
2. Mỗi test case (TC) phải truy vết tới ít nhất một ID trong test basis hoặc trong bảng thiết kế. TC không có nguồn không được vào bộ test; ý tưởng kiểm tra chưa có nguồn thì ghi thành câu hỏi hoặc charter exploratory.
3. Kết quả mong đợi phải quan sát được: text nguyên văn, màn hình hoặc URL đích, trạng thái, dữ liệu thay đổi. Không dùng "hoạt động bình thường", "hiển thị đúng", "thành công" mà không nói thấy gì.
4. Mỗi UC có đủ ba nhóm Redirect, Validation, Function. Nhóm không áp dụng phải ghi lý do.
5. Tối thiểu bắt buộc:
   - mỗi trường nhập có phân vùng tương đương và giá trị biên;
   - mỗi business rule có ít nhất một TC thỏa rule và một TC vi phạm rule;
   - mỗi đối tượng có trạng thái có bảng chuyển trạng thái, gồm cả chuyển không hợp lệ;
   - mỗi hành động ghi dữ liệu có TC cho vai trò không được phép: nút bị ẩn trên UI và mở thẳng URL cũng bị chặn; kiểm API bị chặn chỉ khi `profile.md` ghi tester được gọi API, viết ở sheet `API` riêng (`rules/tc-authoring.md` rule 29);
   - mỗi thông báo lỗi có ít nhất một TC làm nó xuất hiện.
6. Mỗi TC chỉ kiểm một mục tiêu. Không gộp hai giá trị không hợp lệ trong cùng một TC, vì lỗi thứ nhất sẽ che lỗi thứ hai.
7. TC chạy độc lập: tiền điều kiện ghi rõ vai trò, dữ liệu, trạng thái; không phụ thuộc thứ tự chạy; không dùng dữ liệu thật hoặc dữ liệu nhạy cảm.
8. Không bàn giao sang Code khi script kiểm tra độ phủ còn báo lỗ hổng hoặc TC sai định dạng. ID chưa có TC chỉ được bỏ qua khi có lý do ghi rõ (`[NGOÀI PHẠM VI]`, `[CHỜ Q-nn]`, `[THUỘC UC-...]`, `[KHÔNG ÁP DỤNG]`).
9. Bug lọt ra sau khi test phải được phân tích nguyên nhân gốc (thiếu test basis, thiếu kỹ thuật, thiếu checklist, sai kết quả mong đợi) và đề xuất cập nhật rule, skill hoặc checklist.

10. Mỗi khu vực trên màn hình phải khai **pattern** của nó và phủ hết checklist bắt buộc của pattern đó, hoặc ghi lý do bỏ qua. Thư viện pattern: `skills/tc-authoring/references/patterns.md`.
11. Chưa có căn cứ cho kết quả mong đợi thì **để trống**, ghi câu hỏi, tô đỏ. Không tự đặt text chưa ai duyệt.

12. Mỗi màn hình / khu vực phải đi qua checklist rủi ro ngoài nghiệp vụ `skills/test-design/references/technical-risk-checklist.md` (khối lượng dữ liệu và phân trang, chuỗi dài, điều hướng nhiều cấp, đồng thời và mạng, dữ liệu sau thao tác). Mục áp dụng thì có TC (nguồn ghi `CK-<mục>` qua dòng EG), mục không áp dụng thì ghi lý do. Mọi hành vi quan sát được mà lệch kỳ vọng hợp lý đều là bug, dù tài liệu yêu cầu không nói.
13. Mỗi con số giới hạn trong tài liệu có ba giá trị: giới hạn − 1, bằng, + 1; với con số đếm theo quy tắc riêng thì kiểm thêm đúng ở ký tự biên. Case không có căn cứ viết dạng quan sát ("Ghi lại hệ thống làm gì"), trạng thái `Còn mở`, kèm câu hỏi; không tự đặt kết quả (theo rule 11).

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.3 | 2026-10-05 | Rule 5: phân quyền âm kiểm trên giao diện và URL; kiểm API chỉ khi tester được gọi API, ở sheet `API` riêng. Hanna duyệt 05/10. | FB-???[api] |
| v0.3 | 2026-10-02 | Thêm rule 12 (checklist rủi ro ngoài nghiệp vụ cho mỗi màn hình) và rule 13 (biên của con số; case không có căn cứ viết dạng quan sát). | FB-028 |
| v0.2 | 2026-10-01 | Thêm rule 10 (pattern bắt buộc) và rule 11 (chưa có căn cứ thì để trống). Tách phần tổ chức và định dạng file sang `rules/tc-authoring.md`. | FB-010 → FB-013 |
| v0.1 | 2026-09-28 | Khởi tạo. | Yêu cầu trong chat: khung TC Redirect / Validation / Function, kỹ thuật thiết kế, "không lọt bug" |