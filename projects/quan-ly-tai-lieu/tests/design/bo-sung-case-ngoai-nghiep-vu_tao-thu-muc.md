# Bổ sung case ngoài nghiệp vụ — Tạo thư mục (UC-DOC-007)

Áp `skills/test-design/references/technical-risk-checklist.md` (FB-028) lên file `Tao_thu_muc_phan_tich_case_cha_con.xlsx` (11 case cha, 74 case con). File đó đã phủ tốt phần nghiệp vụ và biên ký tự; phần dưới là **chỗ còn thiếu**, viết theo mẫu case cha con (templates §7). Mọi case ở đây chưa có căn cứ nên **kết quả mong đợi = "Ghi lại hệ thống làm gì"** và trạng thái `Còn mở`; câu hỏi gửi Hanna ở cuối. Chờ Hanna duyệt rồi mới đưa vào file Excel.

## 12. Danh sách nhiều mục sau khi tạo (CK-A)
| ID | Case con | Điều kiện / Dữ liệu | Thao tác | Kết quả mong đợi | Nguồn | Trạng thái |
|---|---|---|---|---|---|---|
| 12.1 | Tạo khi danh sách đúng một trang đầy | Thư mục đang đứng có 50 mục, cỡ trang 50 | Tạo thư mục thứ 51 | Ghi lại hệ thống làm gì: mục mới nằm trang nào, có trang 2 không, tổng số | CK-A1, A6 | Còn mở |
| 12.2 | Tạo khi danh sách trên 100 mục | Có 101 mục (3 trang) | Tạo thư mục mới | Ghi lại: danh sách có hiển thị không, trang nào, có lỗi / trắng trang không | CK-A2 | Còn mở |
| 12.3 | Tạo ở trang không phải trang đầu | Đang ở trang 2 | Tạo thư mục | Ghi lại: về trang 1 hay giữ trang 2; thư mục mới có thấy không | CK-A6 | Còn mở |
| 12.4 | Tạo rồi tìm thư mục mới khi nhiều trang | Như 12.2 | Tạo "Báo cáo", tìm "Báo cáo" | Ghi lại: tìm ra không, ở trang nào | CK-A5 | Còn mở |
| 12.5 | Tải trang 2 lỗi, trang 1 bình thường | Giả lập lỗi mạng khi chuyển trang | Chuyển sang trang 2 | Ghi lại: lỗi cục bộ hay trắng cả danh sách | CK-A9 | Còn mở |

## 13. Tên dài trên giao diện (CK-B)
| ID | Case con | Điều kiện / Dữ liệu | Thao tác | Kết quả mong đợi | Nguồn | Trạng thái |
|---|---|---|---|---|---|---|
| 13.1 | Tên 255 ký tự không có khoảng trắng | Tạo "2222…2" (255 số 2) | Xem danh sách, breadcrumb, thông báo thành công, hộp thoại tạo con | Ghi lại: chỗ nào vỡ bố cục, cắt, tràn, che nút | CK-B1 | Còn mở |
| 13.2 | Hai thư mục dài lồng nhau | "2222…" › "3333…" như ảnh 2 | Mở thư mục con, mở hộp thoại tạo mới | Rút gọn bằng "…" (đã chốt Q10); ghi lại thêm: có che nút, cuộn ngang không | CK-B2, Q10 | Còn mở |
| 13.3 | Zoom 150% và cửa sổ hẹp với tên dài | Như 13.1 | Phóng to 150%, thu hẹp cửa sổ | Ghi lại: nút «Lưu», «Huỷ» còn thấy và bấm được không | CK-B3 | Còn mở |
| 13.4 | Tên có ký tự đặc biệt trong URL | Tạo "A#B&C%D" rồi mở thư mục | Mở thư mục, F5 | Ghi lại: URL có hỏng, vào đúng thư mục không | CK-B5, C4 | Còn mở |

## 14. Bấm vào tên thư mục ở nhiều cấp (CK-C)
| ID | Case con | Điều kiện / Dữ liệu | Thao tác | Kết quả mong đợi | Nguồn | Trạng thái |
|---|---|---|---|---|---|---|
| 14.1 | Vào từng thư mục vừa tạo, mỗi cấp | Chuỗi 20 cấp từ 6.1 | Bấm tên từng thư mục để vào, lùi lên từng cấp | Ghi lại: mỗi lần có đúng nội dung bên trong không; có lần nào lỗi, trống, sai thư mục | CK-C1, C2 | Còn mở |
| 14.2 | Vào ra lặp lại nhiều lần | Một thư mục có nhiều mục | Vào ra 20 lần liên tiếp, có lần bấm nhanh | Ghi lại: đúng nội dung mọi lần, hay đôi lúc lỗi | CK-C1 | Còn mở |
| 14.3 | F5, Back, dán URL, tab mới ở cấp sâu | Đang ở cấp 10 | F5; Back / Forward; mở URL ở tab mới | Ghi lại: đứng đúng thư mục, breadcrumb đúng | CK-C3 | Còn mở |
| 14.4 | Tạo thư mục xong rồi vào ngay | Vừa tạo ở 4.1 | Bấm tên thư mục vừa tạo | Thấy «Bấm + Tạo mới để tải tệp hoặc tạo thư mục con.» (đã chốt 9.5); ghi lại thêm: có lần nào lỗi | CK-C1, E4 | Còn mở |
| 14.5 | Đổi tên thư mục cha khi đang đứng trong con | Hai tab: tab 1 ở trong "B", tab 2 đổi tên cha "A" | Tạo thư mục ở tab 1 | Ghi lại: breadcrumb, thông báo, tạo được không | CK-C6, D3 | Còn mở |

## 15. Dữ liệu sau khi tạo (CK-E)
| ID | Case con | Điều kiện / Dữ liệu | Thao tác | Kết quả mong đợi | Nguồn | Trạng thái |
|---|---|---|---|---|---|---|
| 15.1 | Sau khi tạo, tải lại trang | Vừa tạo "Hồ sơ" | F5; đăng xuất đăng nhập lại | Ghi lại: thư mục còn đó, đúng tên, đúng ngày giờ | CK-E1 | Còn mở |
| 15.2 | Người dùng khác xem | Tài khoản khác cùng dự án | Mở cùng thư mục cha | Ghi lại: thấy thư mục mới chưa, có cần tải lại | CK-E1 | Còn mở |
| 15.3 | Thư mục mới xuất hiện ở các nơi khác | Vừa tạo | Tìm kiếm; xem breadcrumb; hộp thoại di chuyển | Ghi lại: có hiện ở mọi nơi | CK-E2 | Còn mở |
| 15.4 | Hai người cùng tạo tên giống nhau | Hai tài khoản, cùng thư mục, cùng tên "Báo cáo", bấm Lưu gần như cùng lúc | Cả hai bấm «Lưu» | Ghi lại: tên có tự thêm (1) cho một bên, hay tạo trùng | CK-D3 | Còn mở |
| 15.5 | Tạo khi mạng chậm | Giả lập mạng chậm | Bấm «Lưu» | Ghi lại: có trạng thái đang xử lý, nút có khoá, có tạo trùng khi bấm lại | CK-D2, 10.2 | Còn mở |

## 16. Bộ gõ (CK-F)
| ID | Case con | Điều kiện / Dữ liệu | Thao tác | Kết quả mong đợi | Nguồn | Trạng thái |
|---|---|---|---|---|---|---|
| 16.1 | Bộ đếm khi đang gõ bằng bộ gõ tiếng Việt / Nhật | Bộ gõ Telex hoặc IME tiếng Nhật, đang ở chữ chưa xác nhận | Gõ "Tại sảo" kiểu Telex, hoặc gõ tiếng Nhật chưa bấm Enter | Ghi lại: bộ đếm đúng khi đang gõ dở và sau khi xác nhận (đã chốt "Tại sảo" = 9) | CK-F2, Q8 | Còn mở |
| 16.2 | Bấm Enter khi đang gõ dở bằng IME | Như 16.1 | Bấm Enter để xác nhận chữ | Ghi lại: Enter xác nhận chữ hay bấm «Lưu» luôn | CK-F2 | Còn mở |

## Câu hỏi gửi Hanna (đề xuất)
1. Cỡ trang mặc định là bao nhiêu và có đổi được không? Có giới hạn tổng số mục trong một thư mục không?
2. Tên thư mục 255 ký tự không có khoảng trắng phải hiển thị thế nào ở bảng, breadcrumb, thông báo (cắt "…" hay xuống dòng)?
3. Hai người cùng tạo tên giống nhau cùng lúc: kết quả mong đợi?
4. Có cần cập nhật tức thì cho người dùng khác, hay chỉ khi tải lại?
