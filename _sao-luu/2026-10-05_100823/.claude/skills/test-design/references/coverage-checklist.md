# Checklist review bộ test — Tester

Dùng ở bước 5 (tự review) và cho phiên review độc lập. Phần A do script kiểm; phần B–D cần người hoặc AI đọc.

## A. Tiêu chí hoàn thành — script kiểm (`rtm_check.py` phải không còn lỗi)
- [ ] Mọi ID trong test basis và file thiết kế có ít nhất một TC, hoặc có dấu loại trừ kèm lý do.
- [ ] Mỗi BR có ít nhất một TC Positive và một TC Negative.
- [ ] Mỗi UC có đủ nhóm Redirect, Validation, Function (hoặc có dấu `[KHÔNG ÁP DỤNG: <nhóm>]`).
- [ ] Không có TC trỏ tới ID không tồn tại, TC thiếu trường, TC trùng ID, Nhóm lệch với chữ R/V/F trong ID.
- [ ] Không có kết quả mong đợi mơ hồ.

## B. Chất lượng từng TC
- [ ] Một TC kiểm một mục tiêu; không gộp hai giá trị không hợp lệ.
- [ ] Tiền điều kiện đủ để người khác dựng lại: vai trò, tenant, dữ liệu, trạng thái.
- [ ] Dữ liệu cụ thể (giá trị thật để nhập), không ghi "dữ liệu hợp lệ".
- [ ] Kết quả mong đợi có nguồn trong test basis; text nguyên văn khớp MS.
- [ ] Kết quả mong đợi kiểm cả điều **không được xảy ra** khi cần (không tạo bản ghi, không gửi thông báo, không lộ dữ liệu).
- [ ] TC chạy độc lập, không dựa vào TC khác chạy trước.

## C. Độ phủ theo tư duy — script không bắt được
- [ ] Mỗi dòng PM "Không" cho hành động ghi có TC kiểm **cả** UI và API.
- [ ] Có TC cho dữ liệu tenant khác, scope khác, người không được phân công (đổi id trên URL).
- [ ] Mỗi con số trong rule đã áp giá trị biên (giới hạn − 1, giới hạn, giới hạn + 1).
- [ ] Mỗi đối tượng có trạng thái có TC cho chuyển không hợp lệ quan trọng và chuyển đúng nhưng sai vai trò.
- [ ] Mỗi tác động phụ kiểm ở nơi nó hiện ra (màn hình khác, người nhận thông báo), không chỉ ở màn hình thao tác.
- [ ] Có ít nhất một TC Abnormal cho mỗi hành động ghi dữ liệu (bấm hai lần hoặc mất mạng khi gửi).

## D. Các kiểu bug hay lọt — rà lại trước khi bàn giao
| # | Kiểu bug | Kiểm bằng |
|---|---|---|
| 1 | Validation chỉ có ở UI, API nhận dữ liệu sai | TC gửi request thẳng tới API |
| 2 | Ẩn nút nhưng URL/API vẫn cho làm | TC Negative phân quyền qua URL và API |
| 3 | Lộ dữ liệu tenant khác qua id trên URL hoặc response danh sách | TC IDOR, kiểm response |
| 4 | Tạo trùng khi bấm hai lần hoặc gửi lại sau timeout | TC Abnormal double submit |
| 5 | Trim / hoa thường làm rule duy nhất sai | EP trùng sau trim, khác hoa thường |
| 6 | Sai biên ±1 (dùng < thay vì ≤) | BVA đủ hai phía |
| 7 | Múi giờ: hạn "hôm nay" lệch một ngày | Biên ngày với múi giờ người dùng khác máy chủ |
| 8 | Ký tự có dấu, CJK, emoji bị lỗi khi lưu hoặc hiển thị | EP ký tự, kiểm giá trị sau khi lưu |
| 9 | Chuỗi script bị thực thi khi hiển thị lại | EP chuỗi nguy hiểm, kiểm ở màn hình hiển thị |
| 10 | Danh sách rỗng, trang cuối, đúng một trang | F5 phân trang |
| 11 | Trạng thái cũ trong link email / thông báo sau khi đối tượng đã đổi trạng thái | R1 link thông báo + ST |
| 12 | Xóa/đổi đối tượng đang được UC khác tham chiếu | CRUD liên UC |
| 13 | Thông báo gửi nhầm người hoặc gửi thiếu | SE: kiểm người nhận và người không nhận |
| 14 | Back/refresh giữa luồng nhiều bước | R4, F6 |
| 15 | Hết phiên làm mất dữ liệu đang nhập | R5 |

| 16 | Trên 100 mục (từ 2 trang): danh sách không hiển thị, sai trang, sai tổng | `technical-risk-checklist.md` A2–A9 |
| 17 | Tên dài, chuỗi không ngắt dòng làm vỡ breadcrumb, bảng, hộp thoại | Mục B1–B2 |
| 18 | Bấm vào tên mục lúc đúng lúc lỗi, nhất là ở nhiều cấp | Mục C1–C3, lặp nhiều lần |
| 19 | Con số giới hạn chỉ thử một giá trị | Mục G: − 1, bằng, + 1, và đúng ở ký tự biên |
| 20 | Dữ liệu sau thao tác không khớp ở màn khác hoặc sau khi tải lại | Mục E |

## E. Rủi ro ngoài nghiệp vụ — rà từng màn hình
- [ ] Mỗi màn hình / khu vực đã đi qua `technical-risk-checklist.md` mục A–G; mục nào áp dụng có dòng EG, mục không áp dụng có lý do.
- [ ] Case không có căn cứ trong test basis được viết dạng quan sát ("Ghi lại hệ thống làm gì") và có câu hỏi Q-T, không tự đặt kết quả.
- [ ] Mọi con số giới hạn có ba giá trị: − 1, bằng, + 1.

Bug lọt thuộc kiểu chưa có trong bảng → thêm một dòng (theo vòng học trong SKILL.md).
