# Thư viện pattern — 12 loại khu vực

Rút từ một bộ TC thật đã chạy hai vòng (150 TC, module quản lý tài liệu). Mỗi pattern gồm **điểm kiểm bắt buộc** và **điểm kiểm nên có**. Khai pattern cho mỗi khu vực, rồi phủ hết phần bắt buộc, hoặc ghi lý do bỏ qua.

---

## P1 · Popup có nhập liệu

Dùng cho: tạo thư mục · đổi tên · nhập lý do từ chối · mọi hộp thoại có một ô nhập.

Bắt buộc:
1. Mở popup — tiêu đề, tên đối tượng đang thao tác, đủ các nút
2. Xoá hết nội dung ô — hiện placeholder
3. Để trống rồi bấm nút đồng ý — không gọi hành động, hiện lỗi **tại ô đó**
4. Nhập hợp lệ rồi đồng ý — đóng popup, quay về màn trước, giá trị mới hiển thị đúng
   (với popup tạo mới: thêm TC theo rule 30 — mỗi loại một TC, nhập đủ mọi trường, kiểm từng thông tin hiển thị ở danh sách và chi tiết)
5. Bấm huỷ — đóng popup, **đối tượng không đổi**

Nên có: nhập quá giới hạn ký tự · ký tự đặc biệt · trùng tên · đang gõ dở mà bấm huỷ thì có hỏi lại không · đóng bằng Esc và bằng click ra ngoài.

## P2 · Xoá có xác nhận

Bắt buộc:
1. Bấm xoá — popup hiện tiêu đề cảnh báo, **tên đối tượng bị xoá**, hai nút
2. Bấm huỷ — đóng popup, **đối tượng vẫn còn trong danh sách**
3. Bấm đồng ý — đối tượng mất khỏi danh sách, **và** hiện thông báo kết quả

Nên có: xoá đối tượng có nội dung bên trong · xoá rồi tải lại trang · xoá khi đối tượng đang được dùng ở nơi khác · khôi phục nếu hệ thống có thùng rác.

Điểm hay sai: case huỷ chỉ kiểm "popup đóng" mà quên kiểm "đối tượng vẫn còn".

## P3 · Lặp theo lối vào

Một thao tác có nhiều lối vào thì **mỗi lối vào là một bộ case riêng**, không viết gộp.

Ví dụ có bốn lối vào: menu của dòng · thanh thao tác hàng loạt · nút trên thanh công cụ · phím tắt. Mỗi lối vào chạy lại đủ chuỗi: gọi → hiện hộp thoại → huỷ → đồng ý.

## P4 · Upload

Ma trận ba trục, nhân với nhau:

| Trục | Giá trị |
|---|---|
| Lối vào | kéo thả ngoài màn hình · kéo thả trong hộp thoại · nút chọn |
| Đối tượng | tệp · thư mục · tệp nén |
| Điều kiện | định dạng không cho phép · quá dung lượng · quá số cấp · hợp lệ · dưới ngưỡng · nhiều tệp cùng lúc · rỗng · trùng tên · tên quá dài |

Đây là nhóm sinh nhiều TC nhất. Mỗi điều kiện lỗi phải có **text lỗi nguyên văn**.

Nên có: huỷ giữa chừng · mất mạng giữa chừng · thanh tiến trình · tải lên cùng lúc nhiều phiên.

## P5 · Kiểm chéo vai trò

Mẫu: *làm ở vai trò A → tải lại trang → kiểm ở vai trò B*.

Áp cho mọi thao tác ghi dữ liệu. Thiếu bước tải lại thì chỉ kiểm được giao diện, không kiểm được dữ liệu đã lưu.

Bắt buộc thêm **case phân quyền âm**: vai trò không được phép thì nút phải ẩn **và** mở thẳng URL cũng bị chặn. API phải chặn thì kiểm ở sheet `API`, chỉ khi `profile.md` ghi tester được gọi API (`rules/tc-authoring.md` rule 29).

## P6 · Trùng tên theo mọi đường vào

Đặt cạnh nhau bốn case: tạo trùng tên · đổi tên thành tên đã có · upload trùng tên · di chuyển vào nơi đã có tên đó.

Pattern này tự bắt lỗi thiết kế: nếu bốn đường cho ra bốn hành vi khác nhau thì thiết kế đang không nhất quán.

## P7 · Thông tin bản ghi sau khi tạo

Sau khi tạo thành công, kiểm từng trường hiển thị: tên · người tạo · thời gian tạo đúng định dạng · các trường hệ thống tự điền.

Bắt buộc (rule 30): **mỗi loại tạo một TC**, nhập đủ mọi trường của form (kể cả trường optional), tạo xong mở nơi hiển thị rồi kiểm từng thông tin đúng giá trị đã nhập; danh sách và màn chi tiết là hai TC riêng.

Định dạng ngày giờ phải ghi rõ trong kết quả mong đợi.

## P8 · Xem trước

Bắt buộc:
1. Mở bằng từng lối vào (menu, bấm thẳng vào tên)
2. Loại nội dung xem được — hiện đúng nội dung và đủ các nút điều khiển
3. Loại nội dung **không** xem được — hiện thông báo thay thế
4. Từng nút điều khiển: phóng to, thu nhỏ, giới hạn trên và dưới của mức phóng, đặt lại, tải xuống, đóng
5. Đóng bằng nút và bằng phím Esc

Nên có: chuyển qua lại giữa các mục · có quay vòng ở đầu và cuối danh sách không · tệp hỏng · tệp rất lớn.

## P9 · Phân trang

Mỗi cỡ trang × (ít hơn cỡ trang · nhiều hơn) × (trang đầu · trang giữa · trang cuối), cộng nút trước, nút sau, bấm số trang.

Nên có: đổi cỡ trang khi đang ở trang cuối · phân trang kết hợp bộ lọc · phân trang kết hợp chọn hàng loạt.

Bắt buộc thêm: **tổng số mục vượt 100 (từ 2 trang, mỗi trang đầy)** và tải một trang lỗi trong khi trang khác bình thường. Chi tiết: `skills/test-design/references/technical-risk-checklist.md` mục A.

## P10 · Tìm kiếm

Bắt buộc: hiển thị mặc định · khi đặt con trỏ · tìm ra kết quả · tìm không ra kết quả · ký tự đặc biệt và câu lệnh SQL · nhập quá giới hạn.

Nên có: phân biệt hoa thường · phân biệt dấu · khoảng trắng đầu cuối · tìm bằng phím Enter · xoá nội dung tìm.

## P11 · Bộ lọc dạng danh sách chọn

Bắt buộc: giá trị mặc định · mở danh sách · chọn giá trị khác · xoá lọc.

Nên có: lọc nhiều điều kiện cùng lúc · lọc ra rỗng · giữ hay bỏ lọc khi đổi trang hoặc chuyển màn.

## P12 · Bảng dữ liệu

Bắt buộc: tiêu đề cột · checkbox ba trạng thái (rỗng, chọn một phần, chọn hết) · sắp xếp tăng và giảm · menu của dòng khác nhau theo loại dòng · bấm vào dòng · trạng thái rỗng.

Trạng thái rỗng ghi đủ, mỗi phần một dòng: icon; tiêu đề nguyên văn; mô tả nguyên văn; nút kèm nhãn nút; các phần vẫn hiện trên màn như tiêu đề trang, ô tìm kiếm, hàng tiêu đề bảng. Ghi thẳng ra, không trỏ sang TC khác. TC trạng thái rỗng đứng trước TC tạo mới (`rules/tc-authoring.md` rule 4).

Nên có: dòng không được chọn (nếu có loại dòng đặc biệt) · nội dung quá dài · cột ẩn hiện · giữ hay bỏ lựa chọn khi đổi trang.

Bắt buộc thêm: tên dài tối đa và chuỗi không có khoảng trắng (breadcrumb, ô bảng, tiêu đề, thông báo), bấm vào từng tên ở mọi độ sâu. Chi tiết: `technical-risk-checklist.md` mục B, C.

---

## Bảy chỗ bộ TC thật hay thiếu

Kiểm lại bộ test của mình theo danh sách này:

1. **Di chuyển** thường chỉ có một hai case trong khi đổi tên có năm sáu — thiếu hộp thoại chọn đích, di chuyển vào chính nó, vào thư mục con của nó, huỷ giữa chừng, trùng tên ở đích.
2. **Phân quyền âm** — chỉ kiểm "làm được", không kiểm "không được phép thì bị chặn".
3. **Gọi thẳng API** — tester được gọi API (ghi ở `profile.md`) mà bộ TC chưa có sheet `API`.
4. **Cách ly dữ liệu giữa các khách hàng** — gần như không bao giờ có.
5. **Trạng thái rỗng, đang tải, lỗi mạng.**
6. **Huỷ giữa chừng khi đang nhập dở.**
7. **Kiểm lại sau khi tải lại trang** — không có bước này thì không biết dữ liệu đã lưu thật chưa.
