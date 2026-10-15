# Tự soát trước khi giao (rule 38)

Mỗi loại lỗi quét **toàn sheet** bằng script khi làm được, không đọc lướt. Rút từ các vòng soát Frameworks v1.7 → v1.10, Workspaces v1.11 và bản tổng hợp 15/10. Lỗi nào lặp qua hai vòng thì thêm vào bảng này hoặc vào script.

| # | Loại lỗi | Rule | Cách quét |
|---|---|---|---|
| 1 | Expected không có nguồn (quyết định chốt, UC, tiêu chí chấp nhận, Figma, web) mà không kèm câu hỏi hay đánh dấu đề xuất | 1, 13, 36 | Lọc Expected có chữ, Open question trống, ô UC không tô vàng; mỗi dòng ghi được nguồn |
| 2 | Câu hỏi đặt khi đã áp được rule 1 (web hợp lý, chữ báo lỗi theo mẫu) | 1, 13 | Quét cột Open question tìm câu hỏi về chữ báo lỗi, về hành vi web đã hiện |
| 3 | Open question không phải câu hỏi thật, thiếu `?`, sai nguồn, hai câu nối bằng xuống dòng, ô có câu hỏi mà không tô màu | 13, 23 | Quét toàn bộ cột Open question |
| 4 | Câu đã có trả lời chưa xoá, chưa ghi vào Expected; câu người dùng đã xoá bị thêm lại | 13 | So với `questions.md`, sheet `Cần xác nhận`, file `_Hanna-sua-*` |
| 5 | Mã Q có ở case mà không có ở `Cần xác nhận`; câu ở `Cần xác nhận` thiếu "Đề xuất mặc định" | 23 | Đối chiếu mã Q giữa sheet TC và `Cần xác nhận` |
| 6 | Ô UC tô vàng mà không có câu hỏi, hoặc Expected đề xuất mà ô UC chưa tô | 13 | Lọc ô UC màu `FFF2CC` |
| 7 | Đổi chữ người dùng đã sửa mà không hỏi | 34 | So từng ô với file `_Hanna-sua-*` mới nhất |
| 8 | Expected không quan sát được ("đúng định dạng", "hiển thị đúng") | 12 | Tìm chuỗi mơ hồ |
| 9 | Gộp nhiều loại vào một Expected ("ví dụ A, B", ba loại trong một case) | 9, 30 | Tìm "ví dụ", "hoặc" trong Expected |
| 10 | Pre, Step, Expected không khớp; dữ liệu ở Pre-condition không dựng được trên hệ thống | 31 | Đọc theo nhóm; đối chiếu số với dữ liệu demo thật |
| 11 | Dòng đăng nhập sai mẫu (`;` sau vai trò, `Đăng nhập với acc`, thiếu tên tài khoản); còn `{{…}}` | 14 | Lọc cột Pre-condition; tìm `{{` ở mọi ô |
| 12 | Step có "Kiểm tra…", "Mở màn…", bước 1 không phải URL hay menu trái, tên nút không ghi `button [Tên]` | 14 | Lọc dòng đầu mỗi Step |
| 13 | Thiếu case: trạng thái rỗng, sắp xếp, đủ vai trò (Customer Viewer, SGS, Consultant), quay lại | 4, 15, 24 | Đối chiếu pattern và cột Actor(s) của UC |
| 14 | UC Phase 1 không có case chạy được; `[Phase 2]` thiếu lý do; `[OUT]` thiếu mã UC hay lý do | 40 | `tc_check.py --uc` |
| 15 | Case mới nằm cuối sheet thay vì đúng nhóm; một nhóm Classification I ở hai nơi; Test_Report có dòng ngoài tổng | 8 | `tc_check.py` |
| 16 | Mã UC không theo baseline hiện hành; mã TC bị đánh lại | 11, 28 | Lọc cột UC; so mã TC với bản đã giao |
| 17 | Tên file, ô Version, dòng cuối Record of change khác số; Creator không phải người viết | 6, 35 | `tc_check.py --creator` |
| 18 | Định dạng (phông mức XML, căn lề, màu, dấu nháy, NFC) | 18, 19, 22, 32, 33 | `tc_fix_xlsx.py --fix` rồi `tc_check.py`, cùng 0 lỗi |
