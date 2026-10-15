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
- Nguồn thiết kế: Figma DTP-P1 (file key `jluZdAkgifmZndi5hD12tt`; trước đây "SGS DTP DS" `KM5Oc1DaB78FXOMimDyB0U`); tài liệu yêu cầu: SGS DTP Use Case List v5.4 (13/10/2026)
## Quy ước riêng của dự án (15/10/2026)
Bảy quy tắc ngày 14/10 (FB-070) đã thành rule chung ở `rules/tc-authoring.md` v0.10 (rule 1, 13, 14, 40); mục này chỉ còn quy ước riêng của SGS DTP.
- Người viết (ô Creator, tác giả file): **Hanna**.
- Tài khoản demo (đổi bằng menu Demo, mật khẩu chung của hệ thống demo; reset dữ liệu trước khi chạy test): Customer Admin = Linh Tran (ABC Trading Co., Ltd.); Customer User = Wei Chen; Customer Viewer = Iris Huang; SGS Admin = Minh Nguyen (SGS Taiwan); Customer Admin tổ chức khác = Chen Wei-Ting (Formosa Chips Inc.) hoặc Quang Le (Saigon Foods JSC).
- Tên tier hiện kèm tiếng Trung: `Medium · 中`.
- Mở bằng URL scope hoặc workspace không có quyền hay không tồn tại: hiện `This scope doesn’t exist` / `This workspace doesn’t exist`, dòng dưới `It may have been removed, or it belongs to an organisation you can’t see.`
- Mô hình consultant (v5.4, D56): đồng nghiệp cùng công ty là Customer User; consultant do khách hàng thuê là guest trong Customer Portal; consultant do SGS giới thiệu dùng Consultant Portal. Giao diện chỉ ghi "Consultant".
- SGS Admin chỉ xem thông tin cơ bản của yêu cầu tư vấn, không duyệt hay từ chối (D57).
- "Documents" đổi thành "Evidence Library" (D70).
- Giới hạn upload: 20 file mỗi lần, mỗi file 100 MB (D63).
- Wave của Phase 1 (phân chia 14/10):
  - **Wave 1** (onboarding, setup, evidence): AUTH, ACC, USR, ROL, FWK, SCP, WSP, EVA, EVC, PRF-01, NTF-02, NTF-03.
  - **Wave 2** (Bulk, NirmatAI, Certification, Training): BLK, INT, CFG, CRT, TRN, NTF-04.
  - **Wave 3** (Consulting, Gap Analysis, Cockpit, Audit, Retention): SRQ, GAP, CKP, AUD, RET, MKT, NTF-01.
- Nguồn hiện hành (15/10): UC List v5.4 (13/10); Open Questions Final Confirmation (13/10); Change Management (13/10); Figma DTP-P1 (file key `jluZdAkgifmZndi5hD12tt`); web demo `sgs-dtp-ds-demo-prototype.vercel.app`.
- Đánh dấu Phase 2: theo rule 40 (tiền tố `[Phase 2]` ở tên case). Cách ghi `Phase 2` ở cột V (FB-071) chỉ áp cho file `v0.2_Phase1`; **chờ Hanna xác nhận** bỏ cách này.

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
