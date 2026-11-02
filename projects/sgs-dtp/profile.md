# Hồ sơ dự án: sgs-dtp
- Khách hàng / sản phẩm: SGS DTP
- Ngôn ngữ giao diện của hệ thống (TC viết theo nhãn ngôn ngữ này): tiếng Anh (Figma "SGS DTP DS")
- Ngôn ngữ viết file TC: tiếng Anh, trừ cột Open question và sheet Cần xác nhận viết tiếng Việt
- Tester được gọi API: Không
- Dạng ID UC của tài liệu gốc: `<MODULE>-nn`, vd `SCP-01` (UC List v4); khác `UC-<MODULE>-<số>` nên phải sửa `ID_RE` trong extract_uc_list.py nếu chạy script đó
- File TC mẫu của dự án:              `exports/SGS-DTP_TestCase.xlsx`, sheet TC mẫu `Login` (file bàn giao phải đúng form mẫu). Form do người dùng gửi 01/10/2026; ngày 02/10/2026 đưa về một màu, một phông theo FB-019 — chờ người dùng xem lại. Nội dung hai sheet Login, Scopes là bản nháp viết trước khi có baseline và test basis.; từ 05/10/2026 form mẫu là `SGS-DTP_TestCase1.xlsx` (Hanna điền đường dẫn)
- File TC hiện tại (14/10/2026): `exports/SGS-DTP_TestCase_v0.2_Phase1.xlsx` (dấu Phase 2 ở cột V, FB-071), dựng từ `exports/SGS-DTP_TestCase_v0.1_Phase1.xlsx` — bản tài khoản web dựng (23 sheet, theo UC v5.3), chép từ Downloads\SGS ngày 14/10; bản trước của nhánh đó và nhánh `SGS-DTP_TestCase1_v1.x` (tới v1.15) đã vào `_luu-tru/sgs-dtp-exports-cu/`, không dựng tiếp. Kế hoạch test và báo cáo phần thiếu TC: `tests/plan/`. UC baseline: `docs/source/00 Use case list/SGS DTP Use Case List v5.3.xlsx`
- Hanna mở và sửa file TC bằng ONLYOFFICE (thấy trên ảnh chụp ngày 07/10)
- Môi trường test / URL (19/10/2026, FB-096): **chỉ chạy trên localhost**, không test trên `dtp.ltsgroup.tech` (server chạy nhánh `feat/vietvk/dev-c`, cũ hơn `main`). Code: repo `CORP-BA-DTP` (`C:\Users\thavt\Documents\DTP\CORP-BA-DTP`), nhánh `main`; bản đã chạy 19–20/10: `b5cb690` (19/10/2026). Mỗi lượt báo commit và số commit chậm so với `origin/main`.
  - Web: `http://localhost:3000` · Operations Console `/ops/login` · Customer Portal `/login` · Consultant Portal `/consultant/login` · Hộp thư test (Mailpit): `http://localhost:8025` · DB: Postgres `localhost:5432` (container `corp-ba-dtp-postgres-1`).
  - Tài khoản seed (mật khẩu chung `password`): SGS Admin `lin.mei@example.com` (SGS Taiwan) · Customer Admin `kevin.lin@example.com` (Development organisation) · Customer User `jason.chen@example.com` · Customer Viewer `peggy.lai@example.com` · Consultant `chen.wei@example.com`. Nhân vật trong file TC (Minh Nguyen, Linh Tran, 張雅婷…) chạy bằng các tài khoản này hoặc tài khoản tạo mới trong lượt.
  - Dựng lại: `pnpm install` → build `packages/api-contracts` → `apps/backend: pnpm db:reset` (xoá sạch, seed lại) → `pnpm dev` (web + backend + worker). Điều đã gặp: `rules/automation.md` rule 26.
  - Kết quả và file đã giao 19–20/10 (ở `C:\Users\thavt\Documents\DTP\review-testcase-2026-10-15\`): `SGS-DTP_TestCase_v0.3_Phase1.xlsx` (rà soát Wave 1 đã áp; sheet Customers Round 1: 100 case, 65 Passed · 24 Failed · 11 Pending), `Ra-soat-TC-Wave1_v0.1.xlsx`, `Customers_Bug-Round1_kem-anh.xlsx` (15 bug, ảnh gốc ở `evidence/customers-round1/`), `SGS-DTP_E2E_Phase1_v0.7_Wave1_full.xlsx` (15 luồng E2E Wave 1, chạy trên `4be5d13` trước khi pull).
  - Kế hoạch theo UC (wave, trạng thái Done / In progress / Not started): `SGS_DTP_Detailed_Plan_v3.0.xlsx`, sheet "Plan by UC" — dùng để ghi Pending / Blocked (`rules/automation.md` rule 19).
  - **Chờ Hanna chốt (FB-098):** trang 404 scope / workspace (quy ước bên dưới ghi `This scope doesn’t exist`, web hiện `Page not found`) và tên "Documents" / "Evidence Library" (D70); lượt rà soát 19/10 đã sửa một số Expected theo web.
- Nguồn thiết kế: Figma DTP-P1 (file key `jluZdAkgifmZndi5hD12tt`; trước đây "SGS DTP DS" `KM5Oc1DaB78FXOMimDyB0U`); tài liệu yêu cầu: SGS DTP Use Case List v5.4 (13/10/2026)
## Cập nhật 27–30/10/2026 (thay các dòng cũ khi khác)
- **Môi trường**: chạy chính trên web test `https://dtp.ltsgroup.tech`, ghi build lấy từ Portainer (`tests/tools/pw/portainer-ps.js`). Local (`localhost:3000`, mock NirmatAI `:4010`) chỉ dùng để giả lập (rule 39 của `automation.md`). Web test gửi **mọi mail vào Mailpit** của chính nó (`SMTP_HOST=mailpit`), không tới hộp thư thật; đọc mail qua Portainer exec.
- **Nơi làm việc QA**: `DTP/dts-agent-workspace/tests`
  - `cases`: file TC `SGS-DTP_TestCase_v0.4_Phase1.xlsx`;
  - `input`: Plan v3.0, UC List v6.3 XV_TW, tài liệu NirmatAI;
  - `reports`, `evidence`, `tools`.

  Bug là ticket `tasks/tickets/TICKET-FIX-*.md`; `tasks/bugs.md` do `scripts/bug-sync.py` sinh ra. Decision log: `knowledge/L1-domain/decision-log.md` (D71–D85 thêm ngoài file UC; D84/D85 về retention đè UC v6.3).
- **Cách gọi các bên** (người dùng chốt 30/10):
  - **khách hàng** = bên NirmatAI, người quản lý NirmatAI và bật / tắt standard bên đó;
  - **Customer Admin** = người dùng ở Customer Portal (`/login`);
  - **SGS Admin** = người dùng ở SGS Portal (`/ops/login`);
  - phía SGS duyệt nghiệp vụ = **SGS / Xavier**.

  Không gọi Customer Admin là "khách".
- **NirmatAI — hành vi đã kiểm (code 6ab6689c, local 30/10)**:
  - **Approve and send bị chặn khi**: toggle kết nối NirmatAI tắt (`INTEGRATION_OFF`); standard không còn bên NirmatAI, tức Inactive sau Sync (`STANDARD_UNAVAILABLE`); chưa link client (`NOT_LINKED`); có file chưa sẵn sàng (`FILES_UNAVAILABLE`); request không ở Waiting for approval.
  - **SGS Admin Deactivate framework trong DTP** chỉ chặn tạo Bulk workspace mới. Workspace đang làm vẫn gửi được (BU_133). Khách hàng tắt standard bên NirmatAI thì chặn mọi lần gửi mới tới khi bật lại và Sync (BU_134).
  - Người dùng chốt 30/10: luồng **không xét việc bật / tắt framework**. Chỉ ghi lại hành vi, không hỏi QnA, không log bug về việc này.
  - **Mỗi scope + standard chỉ có một workspace Active.** Muốn tạo lại thì Archive trước. Một standard dùng chung được cho nhiều scope.
  - Link framework ở màn Scope chỉ tạo workspace Assisted. Bulk tạo ở Workspaces › Create Bulk workspace.
  - Cột Customer ở SGS Portal › Bulk workspaces là tên Customer Account (`tenant.name`).
- **Trạng thái**:
  - Workspace: Not started → In progress (có file) → Archived → Deleted.
  - Audit Bulk phía Customer Admin: Draft → Requested → Under review → Closed.
  - Các tab SGS Portal: Waiting for approval / Sending / Needs action / Under review / All.
- **Đăng nhập dev (mock)**: tài khoản thuộc 2 tổ chức bị API trả 409 `ORGANISATION_CHOICE_REQUIRED`, nhưng màn hình báo "Incorrect email or password". Chỉ ghi chú dưới CU-BUG-27 (team đang thương lượng không cho một user thuộc 2 tenant).

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
