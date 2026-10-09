# Bố cục sheet — SGS DTP · UC List v4

v0.1 · 2026-10-05 · Áp `rules/tc-authoring.md` mục G (chờ duyệt) cho `SGS DTP Use Case List v4.xlsx` (bản 02/10/2026), sheet P1 Use Cases; số R là số hàng trong sheet đó. Đếm bằng script: 105 UC → 16 sheet viết được ngay (75 UC), 26 UC chờ, 4 UC kiểm ở nơi hiện ra; mỗi UC nằm đúng một chỗ.

## Bảng UC → sheet

| Sheet | UC | Ghi chú |
|---|---|---|
| Login | AUTH-01, AUTH-03 | Đã có; bổ sung màn kích hoạt tài khoản |
| Top bar | AUTH-02, NTF-02, PRF-01 | Chuông thông báo ở top bar (R114). Đăng xuất, đổi ngôn ngữ ở đây là [GIẢ ĐỊNH], xem lại Figma |
| Home | CKP-01..04 | Classification I là vai trò: mỗi vai trò một dashboard |
| Customer Accounts | ACC-01..06 | Phía SGS |
| Users | USR-01..05, ROL-02 | Cả hai portal |
| Frameworks | FWK-01..07 | |
| Scopes | SCP-01..04 | Đã có |
| Workspaces | WSP-01..05 | Form tạo workspace test đầy đủ ở đây; mở từ Scopes ("Link framework") chỉ kiểm mở form, scope điền sẵn (R35) |
| Assisted workspace | EVA-01..07, WSP-06 | Bên trong một Assisted workspace (R37, R42–R48); WSP-06 hiện ở cây requirement (R40, R43) |
| Evidence Library | EVC-01..08 | Thư viện across workspaces (R50); EVC-08 consultant chỉ xem, ở nhóm Phân quyền |
| Service Requests | SRQ-01..03, SRQ-06, SRQ-07 | Đổi consultant khi đang xử lý: chờ Q12 |
| Certifications | CRT-01..03 | Màn SGS và màn Customer chung một sheet |
| Marketplace | MKT-01..06 | |
| Training | TRN-01..03 | TRN-03 có cho gửi yêu cầu đào tạo không: chờ Q10 |
| Audit Log | AUD-02, AUD-03 | Màn SGS và màn Customer chung một sheet |
| Retention | RET-01..03 | Phải lùi ngày, chạy job; ngày xoá hiện ở hộp Archive thì test ở Workspaces (R38) |
| Chờ: chưa có thiết kế Bulk, NirmatAI | BLK-01..10, CFG-01..05, INT-01..06 | Changes vs Source: D4, D9. CFG-01..03 là tab Bulk settings của chi tiết framework (R23); có thiết kế thì vào sheet Frameworks |
| Chờ: chưa chốt có làm | SOA-01..02, RET-04..05, CKP-05 | Q5, Q6, Q9 |
| Kiểm ở: nơi hiện ra | NTF-01, NTF-03, AUD-01, ROL-01 | NTF-01 ở Service Requests và FLOW-03; NTF-03 ở Users, Customer Accounts, Login; AUD-01 ở nhóm Ghi vết mọi sheet; ROL-01 ở nhóm Phân quyền, Bảo mật mọi sheet |

Sheet thêm: `Phân quyền` (ma trận vai trò × UC, tuỳ chọn) và 4 sheet luồng:

- FLOW-01 Onboarding: ACC-03 → ACC-05 → AUTH-03 → SCP-03 → USR-03/05 → AUTH-03 → SCP-01
- FLOW-02 Certification: SCP-03 → CRT-01 → CRT-02, SCP-02
- FLOW-03 Service request: SRQ-01 → SRQ-06 → SRQ-07, kèm NTF-02
- FLOW-04 Consultant: ACC-06 → EVC-08 → AUD-03

## Vì sao tách 07 (Evidence – Assisted mode) và 08 (Evidence – Common)

- EVA diễn ra bên trong một Assisted workspace: cây requirement, chi tiết requirement, upload, map, gỡ evidence, gán owner (R42–R48); phần thân overview của Assisted workspace chính là cây requirement (R37).
- EVC là thư viện evidence "across workspaces, with filters by workspace, standard and scope" (R50) cùng các thao tác trên một evidence (R51–R55); Bulk cũng dùng evidence (BLK-08 · R69).
- Hai màn khác nhau nên tách. Chỗ nối đặt ở sheet của hành động (rule 27): upload ở requirement rồi kiểm trong thư viện → sheet Assisted workspace; xoá evidence trong thư viện rồi kiểm requirement đang map nó → sheet Evidence Library.

## Việc cần làm trên SGS-DTP_TestCase1.xlsx

- Đổi cột UC sang ID v4 qua cột Source ref: 175/181 TC đang ghi ID nguồn v2.1; một số số đã khác, vd UC-USR-006 → USR-05, UC-AUTH-005 → AUTH-03.
- Chuyển 13 TC trong Scopes sang sheet Workspaces: UC-SCP-006 → WSP-01 (11 TC "Gắn framework"), UC-EVD-003 → WSP-02 (1), UC-SCP-007 → WSP-04/05 (1 TC "Gỡ framework"). Scopes chỉ giữ TC bấm "Link framework" mở panel Create workspace với scope điền sẵn.
- 6 TC trỏ UC không còn ở P1: UC-RDN-004 (4, Scopes) và UC-AUTH-003 (1, Login) đã sang P2 (P2 Deferred!H40, H3); UC-ACC-009 (1, Login) không có trong v4.
- Viết lại cả file bằng tiếng Anh (rule 16, `profile.md`), trừ cột Open question và sheet Cần xác nhận; bỏ dạng `{{…}}`, dòng đăng nhập ghi `Logged in as <role>`, dữ liệu ghi giá trị cụ thể (rule 14; số lượng ở FB-???[pre-condition]).
- 18 TC chưa ghi vai trò ở Pre-condition (rule 24): Login TC_038, 039, 041, 050; Scopes TC_022, 023, 024, 026, 027, 049, 051, 052, 069, 070, 071, 090, 091, 092.
- Bỏ TC gọi API khỏi sheet màn hình (rule 29): 9 TC chỉ gọi API (Login TC_051; Scopes TC_119, 120, 126, 127; Users TC_054, 058, 059, 060), TVP_ID không dùng lại (rule 11); 3 TC bỏ bước gọi API, giữ phần giao diện (Scopes TC_123; Users TC_055, 056).
- Ô Scopes!C5 (Creator) đổi sang Times New Roman 10 (FB-016).

## Câu hỏi còn mở

- QUAN TRỌNG · SGS Admin có mở được chi tiết scope (SCP-02) không? ACC-02 (R8) cho SGS xem danh sách scope trong chi tiết khách hàng, còn SCP-01/02 chỉ ghi "assigned SGS users (read-only)" (R30–R31). Mặc định: theo cột Actor(s), SGS Admin không mở được.
- QUAN TRỌNG · Customer Viewer có mở được Scopes, Workspaces không? Viewer chỉ có ở CRT-02, AUD-03, CKP-05. Mặc định: theo cột Actor(s), không mở được.
- NHỎ · 6 TC "Đổi tier" đang ghi [NGOÀI UC]: v4 không có UC đổi tier, tier chỉ chọn lúc tạo workspace (R35). Nếu Figma vẫn có nút đổi tier thì đây là chỗ Figma lệch với UC.
