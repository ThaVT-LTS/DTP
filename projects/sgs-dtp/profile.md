# Hồ sơ dự án: sgs-dtp
- Khách hàng / sản phẩm: SGS DTP
- Ngôn ngữ giao diện của hệ thống (TC viết theo nhãn ngôn ngữ này): tiếng Anh (Figma "SGS DTP DS")
- Ngôn ngữ viết file TC: tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt
- Tester được gọi API: Không
- Dạng ID UC của tài liệu gốc: `<MODULE>-nn`, vd `SCP-01` (UC List v4); khác `UC-<MODULE>-<số>` nên phải sửa `ID_RE` trong extract_uc_list.py nếu chạy script đó
- File TC mẫu của dự án:              `exports/SGS-DTP_TestCase.xlsx`, sheet TC mẫu `Login` (file bàn giao phải đúng form mẫu). Form do người dùng gửi 01/10/2026; ngày 02/10/2026 đưa về một màu, một phông theo FB-019 — chờ người dùng xem lại. Nội dung hai sheet Login, Scopes là bản nháp viết trước khi có baseline và test basis.; từ 05/10/2026 form mẫu là `SGS-DTP_TestCase1.xlsx` (Hanna điền đường dẫn)
- File TC hiện tại (14/10/2026): `exports/SGS-DTP_TestCase_v0.2_Phase1.xlsx` (dấu Phase 2 ở cột V, FB-071), dựng từ `exports/SGS-DTP_TestCase_v0.1_Phase1.xlsx` — bản tài khoản web dựng (23 sheet, theo UC v5.3), chép từ Downloads\SGS ngày 14/10; bản trước của nhánh đó và nhánh `SGS-DTP_TestCase1_v1.x` (tới v1.15) đã vào `_luu-tru/sgs-dtp-exports-cu/`, không dựng tiếp. Kế hoạch test và báo cáo phần thiếu TC: `tests/plan/`. UC baseline: `docs/source/00 Use case list/SGS DTP Use Case List v5.3.xlsx`
- Hanna mở và sửa file TC bằng ONLYOFFICE (thấy trên ảnh chụp ngày 07/10)
- Môi trường test / URL: chưa có
- Nguồn thiết kế: Figma "SGS DTP DS" (figma.com/design/KM5Oc1DaB78FXOMimDyB0U/SGS-DTP-DS); tài liệu yêu cầu: SGS DTP Use Case List v4 (02/10/2026)
## Quy tắc viết TC của dự án (ghi đè rule chung, FB-070, 14/10/2026)
Hanna đặt cho SGS DTP Phase 1. Chỗ trái với `rules/tc-authoring.md` thì theo mục này.
1. Step ghi rõ bấm gì, nhập gì để đi tới kết quả được kiểm ở Expected.
2. Open question chỉ giữ khi các nguồn mâu thuẫn nhau hoặc thật sự cần kiểm tra; có trả lời thì xoá.
3. Web/prototype đã thể hiện hành vi và hợp lý thì theo web, không đặt Open question. Web có nhiều tính năng hơn danh sách UC thì theo web (UC cập nhật sau). (Ghi đè rule 1, 2, 13 của rule chung.)
4. Khi soát: câu hỏi người dùng đã xoá là đã giải quyết, không thêm lại, không tô đỏ lại dòng.
5. UC có mà web chưa có: vẫn viết case, đánh dấu Phase 2 bằng chữ `Phase 2` ở cột **V (Remark của Round 2)**; tên case không mang tiền tố `[Phase 2]` (Hanna 14/10, FB-071).
6. Thông báo lỗi chưa thấy trên web: viết theo mẫu thông báo sẵn có của app (không đoán được thì chỉ mô tả hành vi), cập nhật sau nếu web khác; không đặt Open question cho phần này.
7. Dòng đăng nhập ở Pre-condition: `Login acc <role> (<tên tài khoản demo>) <điều kiện>`, vd `Login acc Customer Admin (Linh Tran) chưa có sự kiện nào`; không viết "Đăng nhập với acc …;". Thay quyết định `Logged in as <role>` ngày 05/10.
   Tài khoản demo đang dùng: Customer Admin = Linh Tran (ABC Trading); Customer User = Wei Chen; Customer Viewer = Iris Huang; SGS Admin = Minh Nguyen (SGS Taiwan); Customer Admin tổ chức khác = Chen Wei-Ting (Formosa Chips) hoặc Quang Le (Saigon Foods).

## Quyết định đã chốt của dự án
- 2026-10-05 · Hanna · File TC viết tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt; dòng đăng nhập ở Pre-condition ghi `Logged in as <role>` (thay bằng mục Quy tắc 7 ngày 14/10, FB-070), màn không cần đăng nhập ghi `Not logged in` (FB-031, FB-035)
- 2026-10-05 · Hanna · Tester không được gọi API: không viết TC gọi API ở sheet màn hình; khi được gọi API thì viết ở sheet `API` riêng (FB-039)
- 2026-10-05 · Hanna · Giá trị tính toán (vd cột Users, Evidence coverage) không ghi cách tính trong TC; Expected theo Figma và UC, chưa có thì để trống và ghi câu hỏi (FB-037, Bị bác)

## Đang chờ Hanna xác nhận (07/10/2026)
Hai bản Hanna sửa ngày 07/10 (v1.4 và bản sửa trên v1.5) làm khác ba quyết định ở trên. AI chưa sửa mục "Quyết định đã chốt"; chi tiết ở `tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 2 và `tests/design/phan-tich-cach-viet_v1.4.md` mục 3.
- Ngôn ngữ file TC: quyết định 05/10 ghi tiếng Anh; sheet Scopes viết tiếng Việt, Hanna đã đổi nốt 6 tên case tiếng Anh sang tiếng Việt.
- Dòng đăng nhập ở Pre-condition: quyết định 05/10 ghi `Logged in as <role>`; file ghi "Đăng nhập account Customer Admin".
- Giá trị tính toán: quyết định 05/10 ghi không ghi cách tính trong TC; Hanna ghi phép tính và kết quả ở các case Evidence coverage, kể cả case biên (FB-048).
- Expected theo hệ thống đang chạy kèm câu hỏi: Hanna làm ở 18 TC; `rules/tc-authoring.md` rule 1 và rule 13 đang ghi ngược lại (FB-050). → Đã chốt 14/10: theo web khi hợp lý, không cần câu hỏi (Quy tắc 3, FB-070).
- Dòng đăng nhập ở Pre-condition → Đã chốt 14/10: `Login acc <role> (<tên>) …` (Quy tắc 7, FB-070).
