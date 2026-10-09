# Inventory — Quan_ly_tai_lieu_mockup5.pdf · lượt 1: trích xuất nguyên văn

> Trạng thái: BẢN NHÁP — sản phẩm bước 1 của skill ba-analysis. Đi kèm: `analysis.md` · `questions.md`.

| | |
|---|---|
| Nguồn | `docs/source/Quan_ly_tai_lieu_mockup5.pdf` · 15 trang khổ ngang 987×685 pt · 680.330 byte · in từ Chromium (Skia/PDF), tạo lúc 02/10/2026 11:26 (+07) |
| Loại tài liệu | Bản thiết kế / mockup giao diện — không phải danh sách UC (a), không phải UC spec (b) |
| Cách đọc | Chép nguyên văn lớp chữ của PDF, đối chiếu với ảnh từng trang. Không tóm tắt. |
| Kiểm hai chiều | `python .claude/skills/ba-analysis/scripts/pdf_text_coverage.py` — kết quả ở `analysis.md` §1 |
| Ngày | 2026-10-02 |

**Quy ước**

- `«…»` là chuỗi chép nguyên văn từ PDF, giữ cả ký hiệu như «⇅», «⌄», «⋮», «—». Chuỗi bị xuống dòng trong PDF được ghép lại thành một chuỗi.
- Chữ ngoài `«…»` là quan sát từ ảnh trang (biểu tượng, màu, vị trí, trạng thái). Đó là mô tả của người đọc, không phải text giao diện.
- `tr.N` là trang N của PDF. Mockup tự đánh số "Màn N" trùng với số trang.
- `K1`–`K4` là khối lặp lại trên nhiều trang. Mỗi khối ghi một lần, kèm danh sách trang áp dụng; script kiểm khối đó trên từng trang trong danh sách.
- Chữ *nghiêng* ở mục C do bước phân tích thêm vào, không có trong nguồn.

---

## A. Khối dùng chung

### K1 · Khung trang — áp dụng: tr.1–15

| # | Khu vực | Phần tử | Text nguyên văn | Quan sát từ ảnh |
|---|---|---|---|---|
| 1 | Thanh biểu tượng bên trái | Logo | «F» | Ô vuông nền tối, chữ trắng, trên cùng |
| 2 | Thanh biểu tượng bên trái | Biểu tượng | — | Hình thư mục, có nền tô (đang chọn) |
| 3 | Thanh biểu tượng bên trái | Biểu tượng | — | Hình người |
| 4 | Thanh biểu tượng, dưới cùng | Biểu tượng | — | Hình chuông |
| 5 | Thanh biểu tượng, dưới cùng | Avatar | «Fe» | Hình tròn nền tối, chữ trắng |
| 6 | Menu bên | Mục menu | «Chi tiết dự án» | Biểu tượng tệp; dưới mục có một đường kẻ đứt |
| 7 | Menu bên | Mục menu | «Quản lý tài liệu» | Biểu tượng thư mục; nền tô (đang chọn) |
| 8 | Menu bên | Mục menu | «Quản lý báo giá» | Biểu tượng tệp |
| 9 | Đầu vùng nội dung | Breadcrumb | «Quản lý dự án › LTS › Quản lý tài liệu» | Hai đoạn đầu chữ xám, đoạn cuối chữ đậm hơn |
| 10 | Đầu vùng nội dung, bên phải | Nút | «Thùng rác» | Biểu tượng thùng rác, nút viền |
| 11 | Thanh công cụ | Ô nhập | «Tìm theo tên tệp…» | Placeholder chữ xám; biểu tượng kính lúp bên trái |
| 12 | Thanh công cụ | Nút | «Tìm kiếm» | Nút viền tối, chữ đậm |
| 13 | Thanh công cụ | Danh sách chọn | «Tất cả các bước» «⌄» | Không trang nào mở danh sách này |
| 14 | Thanh công cụ | Danh sách chọn | «Tài liệu dự án» «⌄» | Mở ở tr.6 |
| 15 | Thanh công cụ | Nút | «Xoá lọc» | Chữ và viền nhạt, trông như đang tắt — giống nhau ở cả 15 trang |
| 16 | Thanh công cụ, bên phải | Nút | «Tạo mới» | Nền tối, chữ trắng; dấu cộng phía trước là hình, không nằm trong lớp chữ |
| 17 | Bảng · hàng tiêu đề | Checkbox | — | Ô vuông; trạng thái theo từng trang ghi ở mục B |
| 18 | Bảng · hàng tiêu đề | Tên cột | «Thao tác» | Hàng tiêu đề nền tối, chữ trắng |
| 19 | Bảng · hàng tiêu đề | Tên cột | «Tên tệp ⇅» | «⇅» là ký hiệu sắp xếp |
| 20 | Bảng · hàng tiêu đề | Tên cột | «Định dạng ⇅» | |
| 21 | Bảng · hàng tiêu đề | Tên cột | «Dung lượng ⇅» | |
| 22 | Bảng · hàng tiêu đề | Tên cột | «Người cập nhật cuối ⇅» | |
| 23 | Bảng · hàng tiêu đề | Tên cột | «Cập nhật lần cuối ⇅» | |
| 24 | Phân trang | Danh sách chọn | «50 dòng / trang» «⌄» | |
| 25 | Phân trang | Nút | «‹ Trước» | Chữ xám |
| 26 | Phân trang | Số trang | «1» | Nền tối: trang đang xem |
| 27 | Phân trang | Nút | «Sau ›» | Chữ xám, cùng màu với nút trước |

### K2 · Danh sách thư mục gốc — áp dụng: tr.1–8, 14, 15

| Dòng | Checkbox | Thao tác | Tên tệp | Định dạng | Dung lượng | Người cập nhật cuối | Cập nhật lần cuối | Quan sát từ ảnh |
|---|---|---|---|---|---|---|---|---|
| 1 | có | «⋮» | «Quản lý rủi ro» | «—» | «—» | «—» | «19/08/2026 20:37» | Biểu tượng thư mục trước tên |
| 2 | có | «⋮» | «Xem xét chi phí» | «—» | «—» | «—» | «19/08/2026 20:37» | Biểu tượng thư mục trước tên |
| 3 | không có | không có nút | «Thư mục công trình cũ» · nhãn «Thư mục hệ thống» | «—» | «—» | «—» | «—» | Nhãn nền xám, chữ nhỏ, đứng cạnh tên |

### K3 · Danh sách trong thư mục "Quản lý rủi ro", dữ liệu mẫu — áp dụng: tr.10–13

| Dòng | Checkbox | Thao tác | Trước tên | Tên tệp | Định dạng | Dung lượng | Người cập nhật cuối | Cập nhật lần cuối | Quan sát từ ảnh |
|---|---|---|---|---|---|---|---|---|---|
| 1 | có | «⋮» | biểu tượng thư mục | «Tài liệu tham khảo» | «—» | «—» | «Nguyễn Văn A» | «30/09/2026 15:02» | Tên không gạch chân |
| 2 | có | «⋮» | nhãn «PDF» chữ đỏ | «Bản vẽ sơ đồ đấu nối CT-VT_rev2.pdf» | «PDF» nhãn đỏ | «2,4 MB» | «Nguyễn Văn A» | «30/09/2026 14:12» | Tên gạch chân, dạng liên kết |
| 3 | có | «⋮» | nhãn «XLSX» chữ xanh lá | «Bảng khối lượng & dự toán sơ bộ.xlsx» | «XLSX» nhãn xanh lá | «186 KB» | «Trần Thị B» | «29/09/2026 09:40» | Tên gạch chân |
| 4 | có | «⋮» | nhãn «DWG» chữ xanh dương | «Mặt bằng trạm biến áp.dwg» | «DWG» nhãn xanh dương | «5,8 MB» | «Nguyễn Văn A» | «28/09/2026 17:05» | Tên gạch chân |
| 5 | có | «⋮» | nhãn «DOCX» chữ xanh dương | «Biên bản họp rà soát yêu cầu.docx» | «DOCX» nhãn xanh dương | «74 KB» | «Lê Văn C» | «26/09/2026 11:20» | Tên gạch chân |

### K4 · Lớp xem trước tệp — áp dụng: tr.12–13

| # | Khu vực | Phần tử | Text nguyên văn | Quan sát từ ảnh |
|---|---|---|---|---|
| 1 | Thanh trên, bên trái | Tên tệp đang xem | «Bản vẽ sơ đồ đấu nối CT-VT_rev2.pdf» | Chữ trắng, đậm, trên nền tối |
| 2 | Thanh trên, bên phải | Nút | «Sao chép liên kết» | Biểu tượng mắt xích, nút viền |
| 3 | Thanh trên, bên phải | Nút | «Quản lý phiên bản» | Biểu tượng đồng hồ có mũi tên vòng |
| 4 | Thanh trên, bên phải | Nút | «Tải xuống» | Biểu tượng tải xuống |
| 5 | Thanh trên, góc phải | Nút đóng | «×» | |
| 6 | Bên trái khung xem | Nút tròn | «‹» | |
| 7 | Bên phải khung xem | Nút tròn | «›» | |
| 8 | Đáy màn | Thanh công cụ 6 nút | «−» · «+» · «⇔» · «⇕» · «↺» · «↻» | Chỉ có ký hiệu, không có nhãn hay tooltip |
| 9 | Góc dưới bên trái | Gợi ý phím | «Dùng phím mũi tên trái/phải để chuyển tệp · Esc để đóng» | Chữ xám nhạt |
| 10 | Khung xem nền trắng | Nội dung tệp minh hoạ, không phải text giao diện | «SƠ ĐỒ ĐẤU NỐI CT – VT» · «Rev.2 · Tờ 1/3» · «MBA T1» · «CT» · «MBA T2» · «TỦ ĐO VT» · «Dự án K2400425-002 · Bản vẽ minh hoạ» | Sơ đồ khối có đường nối; hai thanh xám giả lập dòng chữ |
| 11 | Phía sau lớp phủ | Trang danh sách | — | Bị phủ tối: K1, K3 và tiêu đề «Quản lý tài liệu › Quản lý rủi ro» vẫn nằm trong lớp chữ |

---

## B. Từng màn

### Màn 1 · tr.1 · Danh sách thư mục gốc

- Chú thích của mockup, không phải giao diện: «Màn 1 — Danh sách thư mục gốc» (ô viền tròn, góc dưới bên phải).
- Nền: K1 + K2. Tiêu đề trang (chữ lớn): «Quản lý tài liệu».
- Trạng thái: chưa chọn dòng nào; checkbox tiêu đề rỗng; «Xoá lọc» nhạt; trang «1».

### Màn 2 · tr.2 · Bấm "Tạo mới"

- Chú thích: «Màn 2 — Bấm “Tạo mới”: 3 lựa chọn»
- Nền: K1 + K2. Tiêu đề: «Quản lý tài liệu».
- Menu thả xuống ngay dưới nút «Tạo mới», căn mép phải:

| # | Mục | Biểu tượng | Quan sát từ ảnh |
|---|---|---|---|
| 1 | «Tạo thư mục mới» | thư mục | Chữ đậm, nền tô: mục đang được trỏ |
| 2 | «Tải tệp lên» | mũi tên tải lên | |
| 3 | «Tải thư mục lên» | mũi tên tải lên | |

### Màn 3 · tr.3 · Menu "⋮" của thư mục

- Chú thích: «Màn 3 — Menu thao tác “⋮” trên từng dòng»
- Nền: K1 + K2. Tiêu đề: «Quản lý tài liệu».
- Dòng 1 («Quản lý rủi ro») có nền tô; nút «⋮» của dòng này có viền tím (đang mở menu).
- Menu mở ngay dưới nút:

| # | Mục | Biểu tượng | Quan sát từ ảnh |
|---|---|---|---|
| 1 | «Đổi tên» | bút | |
| 2 | «Di chuyển» | thư mục | |
| — | — | — | đường kẻ ngang ngăn cách |
| 3 | «Xoá» | thùng rác | Chữ và biểu tượng màu đỏ |

### Màn 4 · tr.4 · Chọn một dòng

- Chú thích: «Màn 4 — Chọn từng dòng bằng checkbox: hiện thanh thao tác hàng loạt (đã chọn 1)»
- Nền: K1 + K2. Tiêu đề: «Quản lý tài liệu».
- Checkbox tiêu đề hiện «–» trên nền tím (chọn một phần).
- Dòng 1: checkbox «✓» nền tím, dòng có nền tô. Dòng 2: checkbox rỗng. Dòng 3: không có checkbox.
- Thanh thao tác hàng loạt nổi ở giữa đáy màn, nền tối:

| # | Phần tử | Text nguyên văn | Quan sát từ ảnh |
|---|---|---|---|
| 1 | Số đếm | «1» | Huy hiệu tím |
| 2 | Nhãn | «mục đã chọn» | Chữ trắng, đậm |
| 3 | Nút | «Tải xuống» | Biểu tượng tải xuống, nút viền |
| 4 | Nút | «Di chuyển» | Biểu tượng thư mục, nút viền |
| 5 | Nút | «Xoá» | Nền đỏ, biểu tượng thùng rác |
| 6 | Nút | «×» | Đứng sau một vạch ngăn |

### Màn 5 · tr.5 · Chọn tất cả

- Chú thích: «Màn 5 — Checkbox ở tiêu đề: chọn tất cả 2 mục — thư mục hệ thống không được chọn»
- Nền: K1 + K2. Tiêu đề: «Quản lý tài liệu».
- Checkbox tiêu đề «✓»; dòng 1 và dòng 2 «✓», cả hai dòng có nền tô; dòng 3 không có checkbox.
- Ô chú giải nền tối, chữ trắng nhỏ, ngay dưới dòng 3: «Thư mục đặc biệt: không thể xoá, đổi tên hay di chuyển — nên không có checkbox và nút ⋮»
- Thanh thao tác hàng loạt bố cục như Màn 4: «2» · «mục đã chọn» · «Tải xuống» · «Di chuyển» · «Xoá» · «×»

### Màn 6 · tr.6 · Bộ lọc phạm vi tài liệu

- Chú thích: «Màn 6 — Bộ lọc phạm vi tài liệu»
- Nền: K1 + K2. Tiêu đề: «Quản lý tài liệu».
- Danh sách chọn «Tài liệu dự án» đang mở:

| # | Lựa chọn | Biểu tượng | Quan sát từ ảnh |
|---|---|---|---|
| 1 | «Tài liệu dự án ✓» | thư mục | Chữ đậm, nền tô: đang chọn |
| 2 | «Thư mục công trình cũ» | thư mục | |

- Danh sách bên dưới vẫn hiện đủ 3 dòng của K2, kể cả dòng «Thư mục công trình cũ».

### Màn 7 · tr.7 · Tạo thư mục mới

- Chú thích: «Màn 7 — Tạo thư mục mới»
- Nền: K1 + K2 bị phủ lớp mờ. Tiêu đề: «Quản lý tài liệu».
- Hộp thoại ở giữa màn:

| # | Phần tử | Text nguyên văn | Quan sát từ ảnh |
|---|---|---|---|
| 1 | Tiêu đề | «Tạo thư mục» | Biểu tượng thư mục bên trái, chữ lớn |
| 2 | Nút đóng | «×» | Góc trên bên phải |
| 3 | Dòng mô tả | «Thư mục mới sẽ được tạo tại: Quản lý tài liệu» | Đoạn «Quản lý tài liệu» chữ đậm hơn phần trước |
| 4 | Nhãn trường | «Tên thư mục *» | Dấu «*» màu đỏ |
| 5 | Ô nhập | «Nhập tên thư mục» | Placeholder; viền tím (đang focus); ô rỗng |
| 6 | Bộ đếm | «Còn 255 ký tự (tối đa 255)» | Dưới ô, căn phải, chữ xám nhỏ |
| 7 | Nút | «Huỷ» | Nút viền |
| 8 | Nút | «Lưu» | Nền tối, trông như đang bật dù ô còn rỗng |

### Màn 8 · tr.8 · Tải thư mục lên

- Chú thích: «Màn 8 — Tải thư mục lên»
- Nền: K1 + K2 bị phủ lớp mờ. Tiêu đề: «Quản lý tài liệu».
- Hộp thoại:

| # | Phần tử | Text nguyên văn | Quan sát từ ảnh |
|---|---|---|---|
| 1 | Tiêu đề | «Tải thư mục lên» | Biểu tượng tải lên bên trái |
| 2 | Nút đóng | «×» | Góc trên bên phải |
| 3 | Vùng kéo thả | — | Viền đứt; biểu tượng tải lên trong ô tím nhạt ở giữa |
| 4 | Hướng dẫn | «Kéo & thả thư mục hoặc tệp ZIP vào đây, hoặc chọn bằng các nút bên dưới.» | Hai dòng, căn giữa |
| 5 | Giới hạn | «Dung lượng tối đa 5 GB» | Chữ xám nhỏ |
| 6 | Nút | «Chọn thư mục» | Nền tối |
| 7 | Nút | «Chọn tệp ZIP» | Nút viền |
| 8 | Nút | «Đóng» | Góc dưới bên phải hộp thoại |

### Màn 9 · tr.9 · Bên trong thư mục, trống

- Chú thích: «Màn 9 — Bên trong thư mục (trống)»
- Nền: K1, không có dòng dữ liệu.
- Tiêu đề trang: «Quản lý tài liệu › Quản lý rủi ro». Dấu «›» màu xám. Breadcrumb trên cùng vẫn là «Quản lý dự án › LTS › Quản lý tài liệu».
- Hàng tiêu đề bảng vẫn có checkbox rỗng dù danh sách rỗng.
- Trạng thái rỗng trong khung bảng: biểu tượng tải lên trong ô tím nhạt; «Chưa có tệp nào» (chữ đậm); «Thư mục này chưa có tệp được tải lên. Bấm + Tạo mới để tải tệp hoặc tạo thư mục con.» — cụm «+ Tạo mới» chữ đậm.
- Phân trang vẫn hiện trang «1».

### Màn 10 · tr.10 · Bên trong thư mục, có tệp

- Chú thích: «Màn 10 — Bên trong thư mục (có tệp) — bấm tên tệp để xem trước, bấm tên thư mục để mở — dữ liệu minh hoạ»
- Huy hiệu «Dữ liệu mẫu»: nền vàng, góc trên bên phải, phía trên nút «Thùng rác».
- Nền: K1 + K3. Tiêu đề: «Quản lý tài liệu › Quản lý rủi ro».

### Màn 11 · tr.11 · Menu "⋮" của tệp

- Chú thích: «Màn 11 — Menu “⋮” của TỆP: nhiều lựa chọn hơn thư mục (Xem trước, Tải xuống, Sao chép)»
- Huy hiệu «Dữ liệu mẫu». Nền: K1 + K3. Tiêu đề: «Quản lý tài liệu › Quản lý rủi ro».
- Dòng 2 («Bản vẽ sơ đồ đấu nối CT-VT_rev2.pdf») có nền tô; nút «⋮» của dòng có viền tím. Menu:

| # | Mục | Biểu tượng | Quan sát từ ảnh |
|---|---|---|---|
| 1 | «Xem trước» | con mắt | |
| 2 | «Tải xuống» | tải xuống | |
| 3 | «Đổi tên» | bút | |
| 4 | «Di chuyển» | thư mục | |
| 5 | «Sao chép» | hai trang chồng nhau | |
| — | — | — | đường kẻ ngang ngăn cách |
| 6 | «Xoá» | thùng rác | Chữ và biểu tượng màu đỏ |

### Màn 12 · tr.12 · Xem trước tệp

- Chú thích: «Màn 12 — Xem trước tệp (bấm tên tệp hoặc “Xem trước”)»
- Nền: K4 phủ toàn màn; phía sau là K1 + K3 và tiêu đề «Quản lý tài liệu › Quản lý rủi ro».
- Khung xem ở giữa màn.

### Màn 13 · tr.13 · Xem trước kèm bảng Quản lý phiên bản

- Chú thích: «Màn 13 — Xem trước — mở bảng Quản lý phiên bản»
- Nền: K4; khung xem dịch sang trái. Phía sau là K1 + K3 và tiêu đề «Quản lý tài liệu › Quản lý rủi ro».
- Bảng bên phải, nền trắng, cao hết màn, che phần phải của danh sách và thanh công cụ:

| # | Phần tử | Text nguyên văn | Quan sát từ ảnh |
|---|---|---|---|
| 1 | Tiêu đề bảng | «Quản lý phiên bản» | Biểu tượng đồng hồ lịch sử, chữ đậm |
| 2 | Nút | «Tải lên phiên bản mới» | Biểu tượng tải lên, nút viền rộng hết bảng |
| 3 | Ghi chú | «Tên tệp sẽ không thay đổi. Vui lòng chọn tệp cùng định dạng.» | Chữ xám nhỏ, hai dòng |
| 4 | Phiên bản | «Phiên bản 2» · huy hiệu «Hiện tại» | Huy hiệu nền xanh lá, chữ trắng |
| 5 | Dung lượng | «2,4 MB» | Căn phải |
| 6 | Thời điểm · người | «30/09/2026 14:12 · Nguyễn Văn A» | Chữ xám |
| 7 | Nút | «Tải xuống» | Nút viền nhỏ |
| 8 | Phiên bản | «Phiên bản 1» | Không có huy hiệu |
| 9 | Dung lượng | «2,1 MB» | Căn phải |
| 10 | Thời điểm · người | «25/09/2026 09:03 · Trần Thị B» | Chữ xám |
| 11 | Nút | «Tải xuống» | Nút viền nhỏ |

- Không thấy nút đóng riêng của bảng; nút «×» trên thanh trên vẫn còn.

### Màn 14 · tr.14 · Thùng rác, trống

- Chú thích: «Màn 14 — Thùng rác (trống)»
- Nền: K1 + K2 bị phủ lớp mờ. Tiêu đề: «Quản lý tài liệu».
- Hộp thoại:

| # | Phần tử | Text nguyên văn | Quan sát từ ảnh |
|---|---|---|---|
| 1 | Tiêu đề | «Thùng rác» | Biểu tượng thùng rác bên trái |
| 2 | Nút đóng | «×» | Góc trên bên phải |
| 3 | Mô tả | «Có thể khôi phục hoặc xoá vĩnh viễn tệp/thư mục đã xoá. Xoá vĩnh viễn không thể hoàn tác.» | Câu thứ hai chữ đỏ, đậm |
| 4 | Trạng thái rỗng | «Thùng rác trống» | Biểu tượng thùng rác trong ô tím nhạt; chữ đậm |
| 5 | Trạng thái rỗng | «Chưa có tệp hay thư mục nào bị xoá.» | Chữ xám |
| 6 | Chân · số lượng | «0 mục» | |
| 7 | Nút | «Khôi phục» | Chữ và viền nhạt, trông như đang tắt |
| 8 | Nút | «Xoá vĩnh viễn» | Nền đỏ nhạt, trông như đang tắt |

### Màn 15 · tr.15 · Thùng rác, có mục

- Chú thích: «Màn 15 — Thùng rác (có mục, đã chọn 2) — dữ liệu minh hoạ»
- Huy hiệu «Dữ liệu mẫu». Nền: K1 + K2 bị phủ lớp mờ. Tiêu đề: «Quản lý tài liệu».
- Hộp thoại: tiêu đề «Thùng rác», nút «×», mô tả «Có thể khôi phục hoặc xoá vĩnh viễn tệp/thư mục đã xoá. Xoá vĩnh viễn không thể hoàn tác.» (câu thứ hai chữ đỏ, đậm).
- Bảng trong hộp thoại, hàng tiêu đề nền xám nhạt:

| Dòng | Checkbox | Tên | Vị trí ban đầu | Người xoá | Thời gian xoá | Quan sát từ ảnh |
|---|---|---|---|---|---|---|
| tiêu đề | «–» nền tím | «Tên» | «Vị trí ban đầu» | «Người xoá» | «Thời gian xoá» | |
| 1 | «✓» nền tím | «Biên bản họp cũ.docx» | «Quản lý rủi ro» | «Nguyễn Văn A» | «30/09/2026 16:40» | Dòng có nền tô |
| 2 | «✓» nền tím | «Bản vẽ sơ đồ đấu nối CT-VT_rev1.pdf» | «Quản lý rủi ro» | «Nguyễn Văn A» | «30/09/2026 14:10» | Tên xuống hai dòng; dòng có nền tô |
| 3 | rỗng | «Ảnh khảo sát hiện trường» | «Xem xét chi phí» | «Trần Thị B» | «27/09/2026 10:05» | Không có phần mở rộng, không có biểu tượng loại |

- Chân hộp thoại: «Đã chọn 2 / 3 mục» — dòng chữ bị mép dưới hộp thoại cắt mất một phần; nút «Khôi phục» (viền, đang bật) và «Xoá vĩnh viễn» (nền đỏ, đang bật).
- Hộp thoại không có ô tìm kiếm, nút sắp xếp hay phân trang.

---

## C. Chức năng suy ra từ mockup — ID do AI đặt

Mockup không có ID UC. Theo quy ước ID của skill ba-analysis, AI đặt ID dạng `UC-DOC-nnn` (khớp mẫu `UC-[A-Z]+-\d{3}` mà script của Tester đọc) [ĐỀ XUẤT]. Tên chức năng do AI đặt, không phải text của nguồn. Cột "Nguồn" là các trang mà chức năng xuất hiện.

| ID | Chức năng | Nguồn | *Xử lý test* | *Phát hiện* | *Câu hỏi* |
|---|---|---|---|---|---|
| UC-DOC-001 | Xem danh sách thư mục và tệp | tr.1, 9, 10 · K1, K2, K3 | *Trong phạm vi* | *F-13, F-14, F-15, F-16, F-32* | *Q-09, Q-20* |
| UC-DOC-002 | Mở thư mục, quay lại cấp trên | tr.9, 10 · chú thích tr.10 | *Trong phạm vi* | *F-12* | *Q-08* |
| UC-DOC-003 | Tìm kiếm theo tên | K1 #11–12 | *Chưa đủ thông tin* | *F-10* | *Q-07* |
| UC-DOC-004 | Lọc theo bước | K1 #13 | *Chưa đủ thông tin* | *F-06, F-07* | *Q-05* |
| UC-DOC-005 | Lọc phạm vi tài liệu, xoá lọc | tr.6 · K1 #14–15 | *Chưa đủ thông tin* | *F-08, F-11* | *Q-06, Q-07* |
| UC-DOC-006 | Sắp xếp và phân trang | K1 #19–27 | *Trong phạm vi* | *F-13, F-14* | *Q-09* |
| UC-DOC-007 | Tạo thư mục | tr.2, 7 | *Trong phạm vi* | *F-17, F-31* | *Q-10, Q-20* |
| UC-DOC-008 | Tải tệp lên | tr.2 (chỉ có mục menu) | *Chưa đủ thông tin* | *F-18* | *Q-11* |
| UC-DOC-009 | Tải thư mục lên | tr.2, 8 | *Trong phạm vi* | *F-19* | *Q-12* |
| UC-DOC-010 | Đổi tên | tr.3, 11 (chỉ có mục menu) | *Chưa đủ thông tin* | *F-20* | *Q-13* |
| UC-DOC-011 | Di chuyển | tr.3, 4, 5, 11 (chỉ có mục menu, nút) | *Chưa đủ thông tin* | *F-20* | *Q-13* |
| UC-DOC-012 | Sao chép tệp | tr.11 (chỉ có mục menu) | *Chưa đủ thông tin* | *F-20, F-21* | *Q-13, Q-14* |
| UC-DOC-013 | Xoá vào thùng rác | tr.3, 4, 5, 11 (chỉ có mục menu, nút) | *Chưa đủ thông tin* | *F-20* | *Q-13* |
| UC-DOC-014 | Tải xuống | tr.4, 5, 11, 12, 13 | *Chưa đủ thông tin* | *F-21* | *Q-14* |
| UC-DOC-015 | Chọn hàng loạt | tr.4, 5 | *Trong phạm vi* | *F-22* | *Q-14* |
| UC-DOC-016 | Xem trước tệp | tr.10, 11, 12 · K4 | *Trong phạm vi* | *F-23, F-24* | *Q-15* |
| UC-DOC-017 | Sao chép liên kết | K4 #2 | *Chưa đủ thông tin* | *F-25* | *Q-16* |
| UC-DOC-018 | Xem lịch sử phiên bản, tải một phiên bản | tr.13 | *Trong phạm vi* | *F-26, F-27* | *Q-17* |
| UC-DOC-019 | Tải lên phiên bản mới | tr.13 (chỉ có nút và ghi chú) | *Chưa đủ thông tin* | *F-26* | *Q-17* |
| UC-DOC-020 | Xem và chọn mục trong thùng rác | tr.14, 15 | *Trong phạm vi* | *F-28, F-29* | *Q-18* |
| UC-DOC-021 | Khôi phục | tr.15 (chỉ có nút) | *Chưa đủ thông tin* | *F-28* | *Q-18* |
| UC-DOC-022 | Xoá vĩnh viễn | tr.15 (chỉ có nút) | *Chưa đủ thông tin* | *F-28* | *Q-18* |

*Toàn bộ cột "Xử lý test" là [GIẢ ĐỊNH – chờ Q-04]. Quy tắc phân nhóm ở `analysis.md` §3.*

---

## D. Ma trận thao tác × lối vào

Theo bước 0 mục 6 của skill ba-analysis. `có (tr.N)` = có trên mockup ở trang N · `—` = không có ở lối vào này · `?` = có lối vào nhưng không có màn kết quả.

| Thao tác | Menu «Tạo mới» (tr.2) | «⋮» của thư mục (tr.3) | «⋮» của tệp (tr.11) | Thanh hàng loạt (tr.4–5) | Bấm vào tên (tr.10) | Thanh trên khi xem trước (tr.12) | Bảng phiên bản (tr.13) | Hộp thoại Thùng rác (tr.15) | Màn đích |
|---|---|---|---|---|---|---|---|---|---|
| Tạo thư mục | có (tr.2) | — | — | — | — | — | — | — | tr.7 |
| Tải tệp lên | có (tr.2) | — | — | — | — | — | — | — | ? |
| Tải thư mục lên | có (tr.2) | — | — | — | — | — | — | — | tr.8 |
| Mở thư mục | — | — | — | — | có (chú thích tr.10) | — | — | — | tr.9, tr.10 |
| Xem trước | — | — | có (tr.11) | — | có (chú thích tr.10, tr.12) | — | — | — | tr.12 |
| Tải xuống | — | **—** | có (tr.11) | có (tr.4–5) | — | có (tr.12) | có, từng phiên bản (tr.13) | — | ? |
| Đổi tên | — | có (tr.3) | có (tr.11) | — | — | — | — | — | ? |
| Di chuyển | — | có (tr.3) | có (tr.11) | có (tr.4–5) | — | — | — | — | ? |
| Sao chép | — | **—** | có (tr.11) | **—** | — | — | — | — | ? |
| Xoá | — | có (tr.3) | có (tr.11) | có (tr.4–5) | — | — | — | — | ? (không có hộp thoại xác nhận) |
| Sao chép liên kết | — | — | — | — | — | có (tr.12) | — | — | ? |
| Quản lý phiên bản | — | — | — | — | — | có (tr.12) | — | — | tr.13 |
| Tải lên phiên bản mới | — | — | — | — | — | — | có (tr.13) | — | ? |
| Khôi phục | — | — | — | — | — | — | — | có (tr.15) | ? |
| Xoá vĩnh viễn | — | — | — | — | — | — | — | có (tr.15) | ? |

Lối vào khác:

- «Thùng rác»: nút ở đầu vùng nội dung (K1 #10), có trên cả 15 trang, mở hộp thoại tr.14 / tr.15.
- Chuyển tệp khi xem trước: nút «‹» «›» và phím mũi tên trái/phải (K4 #6, #7, #9).
- Đóng xem trước: nút «×» và phím Esc (K4 #5, #9).
- Ô chữ in đậm ở **—** là chỗ lệch giữa các lối vào: thư mục không có «Tải xuống» và «Sao chép» ở menu «⋮», nhưng thanh hàng loạt có «Tải xuống» khi chỉ chọn thư mục (F-21).

---

## E. Phần không đọc được hoặc không có trong nguồn

1. Biểu tượng không kèm chữ ở thanh bên trái (K1 #2–#4: thư mục, người, chuông): không xác định được đích.
2. Sáu nút ký hiệu trên thanh công cụ xem trước «−» «+» «⇔» «⇕» «↺» «↻»: mockup không có nhãn hay tooltip. Nghĩa "thu nhỏ, phóng to, vừa chiều ngang, vừa chiều dọc, xoay trái, xoay phải" chỉ là [SUY LUẬN] từ hình ký hiệu.
3. tr.15: dòng «Đã chọn 2 / 3 mục» bị mép dưới hộp thoại cắt một phần.
4. Trạng thái tương tác mà PDF tĩnh không giữ được: hover, tooltip (trừ ô chú giải ở tr.5), hiệu ứng chuyển, thời gian chờ, thông báo tạm thời. PDF được in từ trình duyệt Chromium nên có thể còn một bản HTML có tương tác [CHƯA KIỂM CHỨNG].
5. Nội dung tệp trong khung xem trước (K4 #10) là bản vẽ minh hoạ, không phải text giao diện.
6. 10 ảnh nhúng (tr.2–8, 11, 14, 15) là mặt nạ bóng đổ của menu, thanh thao tác và hộp thoại, không chứa nội dung. Đã kiểm bằng `pdfimages` và xem ảnh. PDF không có lớp ghi chú, form hay JavaScript (`pdfinfo`).
7. Tài liệu được dẫn chiếu nhưng không có trong input [CHƯA KIỂM CHỨNG]: các bản mockup trước bản 5 (tên tệp có số 5); tài liệu yêu cầu của module; các màn «Chi tiết dự án» và «Quản lý báo giá»; hồ sơ dự án «LTS» và «Dự án K2400425-002» (chỉ xuất hiện trong breadcrumb và dữ liệu minh hoạ).
