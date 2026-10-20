# Checklist rủi ro ngoài nghiệp vụ (hạ tầng · giao diện · dữ liệu)

Phiên bản v0.1 · FB-028. Rút từ hướng dẫn của người dùng ngày 02/10/2026 khi làm phần "Tạo thư mục" của `quan-ly-tai-lieu`.

## Vì sao có checklist này
Rất nhiều bug **không do nghiệp vụ** mà chưa ai nghĩ ra case: có trên 100 mục thì lỗi, tên thư mục quá dài làm vỡ đường dẫn, bấm vào tên thư mục thì lúc đúng lúc lỗi. Test basis không nói gì về các chỗ này, nên viết TC chỉ từ nghiệp vụ sẽ để lọt. **Mọi hành vi quan sát được mà lệch kỳ vọng hợp lý đều được coi là bug** (treo, trắng trang, mất dữ liệu, vỡ giao diện, thông báo sai, dữ liệu sai sau khi tải lại), dù không có dòng nào trong tài liệu yêu cầu.

## Cách dùng
1. Với **mỗi màn hình / khu vực**, đi qua từng mục A–G. Mục nào áp dụng thì ghi một dòng EG trong `tests/design/<UC-ID>.md` (`<UC>-EG-nn`, cột "Nguồn" ghi `CK-<mục>`), rồi viết TC.
2. Mục không áp dụng: ghi `[KHÔNG ÁP DỤNG: lý do]`. Không bỏ trống.
3. **Kết quả mong đợi:** hầu hết mục này không có căn cứ trong test basis. Không tự đặt kết quả. Viết case ở dạng *quan sát*: cột kết quả ghi **"Ghi lại hệ thống làm gì"** kèm các dấu hiệu coi là lỗi (treo, trắng trang, sai số, vỡ bố cục, lỗi console, mất dữ liệu); trạng thái = `Còn mở`; đưa thành câu hỏi `Q-T-nn` cho BA. Được người dùng trả lời thì đổi thành `Đã chốt`.
4. Phần lớn lỗi ở đây chỉ xuất hiện **khi vượt một ngưỡng** (số mục, độ dài, độ sâu). Luôn thử ngay dưới, đúng bằng và ngay trên ngưỡng, rồi một giá trị lớn hẳn.

## A. Khối lượng dữ liệu và phân trang (CK-A)
| # | Kiểm | Ghi chú |
|---|---|---|
| A1 | Số mục 0, 1, đúng một trang, một trang + 1 | Ví dụ cỡ trang 50: 50 / 51 |
| A2 | **Trên 100 mục (từ 2 trang trở lên)**, mỗi trang đầy | Có bug chỉ xảy ra khi tổng vượt 100: "không hiển thị trang nào" |
| A3 | Rất nhiều mục (vài trăm, vài nghìn) | Thời gian tải, treo, timeout, cắt bớt im lặng |
| A4 | Chuyển qua lại các trang, trang đầu / giữa / cuối, bấm số trang | Tổng số và số thứ tự khớp |
| A5 | Tìm / lọc / sắp xếp khi có nhiều trang | Về trang 1 hay giữ trang; kết quả của mọi trang |
| A6 | Tạo, xoá, đổi tên xong khi danh sách nhiều trang | Mục mới nằm ở trang nào; xoá hết dòng của trang cuối thì lùi trang |
| A7 | Đổi cỡ trang khi đang ở trang cuối | |
| A8 | Chọn tất cả: "tất cả trang này" hay "toàn bộ"; thao tác hàng loạt qua nhiều trang | |
| A9 | Tải trang 2 lỗi nhưng trang 1 bình thường (mạng, 5xx) | Hiển thị lỗi cục bộ, không trắng cả danh sách |

## B. Chuỗi dài và hiển thị (CK-B)
| # | Kiểm | Ghi chú |
|---|---|---|
| B1 | Tên dài tối đa, và chuỗi **không có khoảng trắng** để ngắt dòng (`2222…`, `3333…`) | Kiểm mọi nơi tên xuất hiện: bảng, breadcrumb, tiêu đề, hộp thoại, thông báo, tooltip |
| B2 | Breadcrumb / đường dẫn dài và nhiều cấp | Rút gọn bằng "…" đúng không; bấm được từng mục; không đẩy vỡ bố cục |
| B3 | Zoom 125 / 150 / 200%, cửa sổ hẹp, màn hình nhỏ | Nút bị che, cuộn ngang ngoài ý muốn |
| B4 | Ký tự Full-width, chữ có dấu tổ hợp (NFC / NFD), emoji, CJK, ký tự điều khiển | Lưu rồi hiển thị lại có giữ nguyên; độ dài đếm khớp |
| B5 | Chuỗi chứa `< > & " '`, `%`, `#`, `?`, `/` | Không bị thực thi như HTML; không làm hỏng URL |
| B6 | Nội dung trống, chỉ khoảng trắng | Dòng xẹp mất, nút bấm không thấy |

## C. Cấu trúc lồng sâu và điều hướng (CK-C)
| # | Kiểm | Ghi chú |
|---|---|---|
| C1 | **Bấm vào tên từng thư mục / mục ở mọi độ sâu → đúng nội dung bên trong** | Thực tế đôi khi lỗi dù lần đầu đúng: lặp 10–20 lần, vào ra liên tục |
| C2 | Vào từng cấp tới giới hạn, rồi lùi lên từng cấp | Breadcrumb, danh sách, tiêu đề đều khớp |
| C3 | Refresh (F5), nút Back / Forward, dán URL trực tiếp, mở tab mới ở **mỗi** cấp | |
| C4 | Tên chứa ký tự đặc biệt khi nằm trong URL | `%`, `#`, `&`, `?`, `/`, dấu cách, tên rất dài làm URL vượt giới hạn |
| C5 | Cùng tên ở các nhánh khác nhau | Vào nhầm nhánh |
| C6 | Đổi tên / xoá / di chuyển thư mục cha khi đang đứng trong thư mục con | |
| C7 | Giới hạn cấp và giới hạn độ dài đường dẫn | Đúng giới hạn − 1, = giới hạn, + 1 |

## D. Trạng thái, đồng thời, mạng (CK-D)
| # | Kiểm |
|---|---|
| D1 | Bấm hai lần nhanh vào nút ghi dữ liệu; gửi lại sau timeout |
| D2 | Mất mạng, chậm mạng, lỗi 5xx giữa thao tác: có trạng thái đang tải, nút có khoá, báo lỗi, không tạo dở dang |
| D3 | Hai người cùng thao tác trên cùng dữ liệu; người kia xoá hoặc đổi mục đang mở |
| D4 | Hết phiên khi đang nhập dở |
| D5 | Giữ tab mở lâu rồi thao tác (dữ liệu cũ) |
| D6 | Huỷ giữa chừng (Huỷ, ×, Esc, bấm ra ngoài) rồi mở lại: ô còn dữ liệu cũ không |

## E. Dữ liệu sau thao tác (CK-E)
| # | Kiểm |
|---|---|
| E1 | Sau tạo / sửa / xoá: F5, sang màn khác, đăng xuất đăng nhập lại, người dùng khác xem |
| E2 | Mọi nơi có tham chiếu cập nhật: tìm kiếm, breadcrumb, yêu thích, thùng rác, thông báo |
| E3 | Thứ tự sắp xếp, định dạng ngày giờ, múi giờ |
| E4 | Mục vừa tạo / vừa xoá có xuất hiện ngay hay phải tải lại |

## F. Cách nhập và môi trường (CK-F)
| # | Kiểm |
|---|---|
| F1 | Dán chuỗi quá dài; kéo thả; bàn phím Tab / Enter / Esc |
| F2 | Bộ gõ (IME): gõ tiếng Nhật / Việt khi đang gõ dở; bộ đếm ký tự trong lúc gõ |
| F3 | Trình duyệt khác, hệ điều hành khác, độ phân giải khác |
| F4 | Bấm ở nơi dễ nhầm: ngoài hộp thoại, đúng mép, double-click |

## G. Giới hạn đã nêu trong tài liệu (CK-G)
Mỗi **con số** trong tài liệu (255 ký tự, 20 cấp, 50 mục/trang, dung lượng tệp…) phải có ba case: giới hạn − 1, giới hạn, giới hạn + 1. Với con số đếm theo quy tắc riêng (Full-width tính 1, chữ có dấu tính 2…), kiểm thêm **đúng ở ký tự biên** (ví dụ ô có 254 chữ, gõ thêm một chữ có dấu tính 2) và hành vi khi dán quá giới hạn.

## Khi bug lọt thuộc kiểu chưa có ở đây
Thêm một dòng vào mục phù hợp, ghi FB, tăng version (theo `CLAUDE.md`).
