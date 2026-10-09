# Hồ sơ dự án: sgs-dtp
- Khách hàng / sản phẩm: SGS DTP
- Ngôn ngữ giao diện của hệ thống (TC viết theo nhãn ngôn ngữ này): tiếng Anh (Figma "SGS DTP DS")
- Ngôn ngữ viết file TC: tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt
- Tester được gọi API: Không
- Dạng ID UC của tài liệu gốc: `<MODULE>-nn`, vd `SCP-01` (UC List v4); khác `UC-<MODULE>-<số>` nên phải sửa `ID_RE` trong extract_uc_list.py nếu chạy script đó
- File TC mẫu của dự án:              `exports/SGS-DTP_TestCase.xlsx`, sheet TC mẫu `Login` (file bàn giao phải đúng form mẫu). Form do người dùng gửi 01/10/2026; ngày 02/10/2026 đưa về một màu, một phông theo FB-019 — chờ người dùng xem lại. Nội dung hai sheet Login, Scopes là bản nháp viết trước khi có baseline và test basis.; từ 05/10/2026 form mẫu là `SGS-DTP_TestCase1.xlsx` (Hanna điền đường dẫn)
- File TC hiện tại (07/10/2026): bản mới nhất về nội dung là `exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx` — Hanna sửa bản v1.5 và gửi lúc 13:28, lưu nguyên; bản AI dựng gần nhất là `exports/SGS-DTP_TestCase1_v1.5.xlsx`. Bản kế tiếp dựng từ file Hanna gửi. Cách viết của sheet Scopes: `tests/design/phan-tich-cach-viet_v1.4.md`; Hanna đổi gì ở bản v1.5: `tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md`. Sheet Login, Users, Profile chưa viết lại theo cách đó
- Hanna mở và sửa file TC bằng ONLYOFFICE (thấy trên ảnh chụp ngày 07/10)
- Môi trường test / URL: chưa có
- Nguồn thiết kế: Figma "SGS DTP DS" (figma.com/design/KM5Oc1DaB78FXOMimDyB0U/SGS-DTP-DS); tài liệu yêu cầu: SGS DTP Use Case List v4 (02/10/2026)
## Quyết định đã chốt của dự án
- 2026-10-05 · Hanna · File TC viết tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt; dòng đăng nhập ở Pre-condition ghi `Logged in as <role>`, màn không cần đăng nhập ghi `Not logged in` (FB-031, FB-035)
- 2026-10-05 · Hanna · Tester không được gọi API: không viết TC gọi API ở sheet màn hình; khi được gọi API thì viết ở sheet `API` riêng (FB-039)
- 2026-10-05 · Hanna · Giá trị tính toán (vd cột Users, Evidence coverage) không ghi cách tính trong TC; Expected theo Figma và UC, chưa có thì để trống và ghi câu hỏi (FB-037, Bị bác)

## Đang chờ Hanna xác nhận (07/10/2026)
Hai bản Hanna sửa ngày 07/10 (v1.4 và bản sửa trên v1.5) làm khác ba quyết định ở trên. AI chưa sửa mục "Quyết định đã chốt"; chi tiết ở `tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 2 và `tests/design/phan-tich-cach-viet_v1.4.md` mục 3.
- Ngôn ngữ file TC: quyết định 05/10 ghi tiếng Anh; sheet Scopes viết tiếng Việt, Hanna đã đổi nốt 6 tên case tiếng Anh sang tiếng Việt.
- Dòng đăng nhập ở Pre-condition: quyết định 05/10 ghi `Logged in as <role>`; file ghi "Đăng nhập account Customer Admin".
- Giá trị tính toán: quyết định 05/10 ghi không ghi cách tính trong TC; Hanna ghi phép tính và kết quả ở các case Evidence coverage, kể cả case biên (FB-048).
- Expected theo hệ thống đang chạy kèm câu hỏi: Hanna làm ở 18 TC; `rules/tc-authoring.md` rule 1 và rule 13 đang ghi ngược lại (FB-050).
