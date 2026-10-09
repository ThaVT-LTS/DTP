# Rule — Viết test case (tc-authoring)

Phiên bản: v0.3 · Nạp cùng `rules/common.md`, `rules/feedback.md`, `rules/tester.md` khi viết hoặc sửa file test case. Quy trình chi tiết: skill `tc-authoring`.

Rule này nói về **file test case bàn giao được**: tổ chức, nội dung, và định dạng. Phần kỹ thuật thiết kế (phân vùng tương đương, bảng quyết định, chuyển trạng thái) vẫn ở `rules/tester.md` và skill `test-design`.

## A. Nguồn chân lý

1. Thứ tự ưu tiên khi ba nguồn mâu thuẫn: **tài liệu yêu cầu (UC/SRS) > bản thiết kế đã duyệt (Figma) > hệ thống đang chạy**. Prototype chỉ dùng để biết *màn nào tồn tại, nút nào tồn tại, nhãn đang dùng*; **không bao giờ** lấy hành vi của prototype làm kết quả mong đợi.
2. Mọi mâu thuẫn giữa ba nguồn phải được ghi thành câu hỏi `Q-<mã màn>-nn`, không tự chọn bên nào đúng.

## B. Tổ chức file

3. **Một màn hình một sheet.** Tên sheet lấy đúng tên mục menu của hệ thống, không dịch, không viết tắt.
4. Trong sheet, TC xếp theo **khu vực**; thứ tự khu vực theo mắt đọc: trên → dưới trong một cột, hết cột trái sang cột phải.
5. **Luồng nghiệp vụ xuyên màn** có sheet riêng `FLOW-nn`, không nhét vào sheet màn hình. Mỗi bước trong luồng ghi rõ màn hình thực hiện.
6. Đầu mỗi sheet có khối thông tin: tên chức năng · tên màn · người viết · ngày tạo · nguồn tham chiếu.

## C. Bốn cấp Classification

7. Bốn cột, đúng thứ tự, không đổi nghĩa giữa các sheet:

| Cấp | Nội dung | Ví dụ |
|---|---|---|
| **I** | Feature — khối chức năng người dùng gọi tên được | `Đăng nhập - Login` |
| **II** | Khu vực trên màn, hoặc nhóm kiểm | `Email` · `Bảo mật - Security` |
| **III** | Mục kiểm, hoặc nhóm kết quả | `Thành công` · `Không thành công` · `Kiểm tra dữ liệu` |
| **IV** | Case cụ thể, mỗi dòng một case | `Bỏ trống` · `Sai định dạng` |

8. **Xếp case sao cho cùng nhóm kết quả nằm liền nhau.** Thành công hết rồi mới tới Không thành công. Xen kẽ thì không gộp ô được, và người đọc mất mạch.
9. Một hành động hiện ở n nơi thì viết **n case riêng**, cùng tiền điều kiện, khác các bước. Không gộp nhiều nơi vào một ô kết quả mong đợi.

## D. Nội dung một dòng

10. Mỗi TC có đúng một `UC_ID`. Không map được thì ghi `[NGOÀI UC]` kèm lý do, không để trống.
11. `TVP_ID` duy nhất trong sheet, theo mẫu `TC_nnn`. Tham chiếu từ ngoài dùng `<tên sheet>_TC_nnn`. ID đã bỏ không dùng lại.
12. Kết quả mong đợi phải **quan sát được**: text nguyên văn, màn hình đích, trạng thái, dữ liệu thay đổi. Cấm "hoạt động bình thường", "hiển thị đúng", "thành công" mà không nói thấy gì.
13. **Chưa có căn cứ thì để trống kết quả mong đợi**, ghi câu hỏi vào cột `Open question`, tô đỏ dòng đó. Tự đặt text chưa ai duyệt sẽ tạo bug giả: tester báo lỗi, dev trả lời "đúng thiết kế", bộ test mất uy tín.
14. Dữ liệu cụ thể và nhãn giao diện viết dạng khoá `{{...}}`, khai ở sheet `_Data` và `_Labels`. Không gõ thẳng giá trị vào TC.
15. Mỗi khu vực có thao tác ghi dữ liệu phải có đủ: ít nhất một case Thành công, một case Không thành công, một case Phân quyền, một case Bảo mật.

## E. Đa ngôn ngữ

16. Hệ thống chạy ngôn ngữ nào thì TC viết theo nhãn ngôn ngữ đó. Khi chuyển ngôn ngữ cho bộ TC có sẵn:
    - chỉ dịch chuỗi **có căn cứ** — bảng đối chiếu thật, hoặc danh sách phần tử đã duyệt;
    - chuỗi chưa có bản dịch chính thức thì **giữ nguyên gốc**, tô đỏ, ghi vào cột `Open question`;
    - dịch theo thứ tự **chuỗi dài trước, chuỗi ngắn sau**, nếu không chuỗi ngắn sẽ cắt nát chuỗi dài.
17. Dịch chỉ đổi **ngôn ngữ**, không đổi **hành vi**. TC nào sai hành vi so với thiết kế mới thì dịch xong vẫn sai — phải liệt kê riêng.

## F. Định dạng file

18. **Phông chữ: Times New Roman, cỡ 10** cho toàn bộ vùng dữ liệu.
19. **Căn lề trái** cho mọi ô. Ô đã gộp căn giữa theo chiều dọc; ô dữ liệu căn trên theo chiều dọc.
20. **Quy tắc gộp ô** cho bốn cột Classification:
    - gộp các dòng **liền nhau có cùng giá trị**; ô trống nghĩa là "giống dòng trên";
    - cụm con **không được vượt ranh giới cụm cha** — cột III đổi cụm thì cột IV phải cắt theo;
    - cụm chỉ một dòng thì không gộp;
    - chỉ ô neo giữ giá trị, các ô còn lại để trống.
21. Người viết làm việc trên **bảng phẳng** (giá trị lặp lại ở mọi dòng); việc gộp ô do script làm lúc xuất file. Không sửa tay trên file đã gộp — ô gộp không lọc được, không sort được, copy xuống là vỡ.

22. **Định dạng đồng nhất toàn bộ.** Mọi sheet trong một file và mọi file test case của dự án dùng **một** phông (Times New Roman 10) và **một** bảng màu khai ở `references/format.md` §4: màu hàng tiêu đề, màu nhãn, màu dòng còn câu hỏi mở, màu đường kẻ. Không dùng màu hay phông ngoài bảng đó; cần thêm thì sửa bảng màu và script trước. Sheet phụ (`Cover`, `Hướng dẫn`, `_Data`, `_Labels`, `FLOW-nn`, `Test_Report`) theo cùng quy ước với sheet màn hình.
23. Cột ghi chuỗi hoặc câu hỏi còn thiếu của một dòng tên là **`Open question`** (trước đây: `Chờ text`). Nội dung ghi mã câu hỏi `Q-<mã màn>-nn` kèm tóm tắt điều cần xác nhận.
24. **Form theo file mẫu của dự án.** Dự án có file TC mẫu (ghi ở `profile.md`, dòng "File TC mẫu của dự án") thì file bàn giao là chính file đó: sheet mới được **thêm vào file mẫu, ngay cạnh một sheet TC đã duyệt, bằng cách nhân bản form của sheet ấy** — khối thông tin, khối tổng kết, hàng tiêu đề, độ rộng cột, căn lề, đường kẻ, dropdown, trang in. Không dựng lại form bằng script tự vẽ.
    - Bố cục của file mẫu khác rule 18–19 hoặc `references/format.md` §1–§3 ở đâu thì **theo file mẫu**, và ghi điểm khác thành câu hỏi cho người dùng.
    - Phông và màu vẫn theo rule 22. Bảng màu lấy **một** màu nền tiêu đề của file mẫu; file mẫu có ô lệch (màu khác, phông khác) thì đưa cả file mẫu về chuẩn trước khi dùng làm mẫu.
    - Dự án chưa có file mẫu thì hỏi người dùng trước khi bàn giao; file dựng bằng form mặc định chỉ là bản tạm.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.3 | 2026-10-02 | Thêm rule 24: form theo file mẫu của dự án — sheet mới thêm vào file mẫu bằng cách nhân bản một sheet TC đã duyệt; bố cục theo file mẫu, phông và màu theo rule 22 với bảng màu lấy một màu nền tiêu đề của file mẫu; chưa có file mẫu thì hỏi. **Chờ duyệt.** | FB-019 · FB-016 |
| v0.2 | 2026-10-02 | Đổi tên cột `Chờ text` → `Open question` (rule 13, 16, 23). Thêm rule 22: định dạng đồng nhất toàn bộ — một phông, một bảng màu cho mọi sheet và mọi file. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: thứ tự nguồn chân lý, một màn một sheet, bốn cấp Classification, quy tắc chưa có căn cứ thì để trống, quy tắc chuyển ngôn ngữ, và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô). | FB-010 · FB-011 · FB-012 · FB-013 |
