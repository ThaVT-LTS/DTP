# Khung case cha — sheet Assisted workspace (module 07 Evidence – Assisted mode)

v0.2 · 2026-10-09 · Viết bù sau review của Opus (`review_Assisted-workspace_v1.13.md`, mục A2, A3, A4); sheet dựng ở file v1.13, sửa ở v1.14 (FB-066) và v1.15 (FB-069, theo `review_Assisted-workspace_v1.14.md`). Phạm vi: màn chi tiết workspace (mở từ bảng ở màn Workspaces): cây requirement, chi tiết requirement, Upload evidence, Link existing evidence, gỡ liên kết, Owner, requirement theo tier, workspace Archived, phân quyền, bảo mật. Danh sách workspace thuộc sheet Workspaces; Evidence Library và chi tiết evidence ở màn Documents thuộc module Evidence Library (chưa có sheet).

## 1. Ba nguồn nói gì (rule 36)

| Nguồn | Đã đọc | Ghi chú |
|---|---|---|
| UC v5.3 — P1 Use Cases (EVA-01 → EVA-07, WSP-04, WSP-06, EVC-04, EVC-07, EVC-09), Decision log (D5, D7, D8, D21, D41, D43, D44), Open Questions | Có (09/10, đọc trên Excel online) | Mã UC dùng 2 chữ số (UC-EVA-01); các sheet cũ dùng 3 chữ số (UC-WSP-002). Không đổi mã đã giao, chờ Hanna chọn một kiểu. |
| UC v5.3 — sheet **Changes vs Source** | **Chưa đọc** | Ghi vào `docs/VIEC-CON-MO.md`; đọc trước lần viết sheet kế tiếp của module 07. |
| Figma SGS-DTP-DS, trang “Screens · 05 Workspaces & Evidence” (6 frame: Workspace / Requirement, Upload evidence, Link existing evidence, Evidence detail, Documents, Evidence library from workspace) | Có | Frame Workspace / Requirement chỉ vẽ nhóm 1 với 6 dòng và 58%, chưa khớp số requirement thật (Q-EA-45). |
| Hệ thống (prototype, Customer Admin, Customer User, Customer Viewer) | Có | Có workspace Appendix 10 · 2022 · Medium (61 requirement), Basic (44) và ISO 22301 · 2019 (6 of 31). Chưa có workspace ISO/IEC 27001, High, Archived, retired: các case dùng chúng (không tier, tier High, Archive, retired) dựng dữ liệu bằng Pre-condition, không kiểm được trên hệ thống hiện tại. Tài khoản dùng trong Pre-condition: Linh Tran (Customer Admin), Wei Chen (Customer User), Mei Lin (Customer User), Iris Huang (Customer Viewer). |

Chỗ ba nguồn lệch nhau (đã thành câu hỏi, Expected để trống hoặc kèm câu hỏi):

| Chỗ lệch | UC | Figma | Hệ thống | Câu hỏi |
|---|---|---|---|---|
| Evidence thuộc workspace hay scope | EVC-09 gắn với scope | “Each file belongs to one workspace”, danh sách Link “already in this workspace” | — | Q-EA-27 |
| Evidence không gắn requirement | Not mapped | Not linked | “Not linked to any requirement”, “not linked yet” | Q-EA-32 |
| Hết hạn | D7: chỉ hiện ngày | Documents có chip Expired, Expires soon | — | Q-EA-14 |
| Nhãn version trên requirement | D21: có nhãn version | không có nhãn | — | Q-EA-11 |
| Nhóm 1 Access Control Appendix 10 · Medium | — | 6 dòng, 58% | 11 requirement | Q-EA-45 |
| Định dạng ngày | — | “Sep 12, 2026” (dòng evidence) và “12 Sep 2026” (chi tiết) | — | Q-EA-12 |
| Ô Owner | EVA-06 | không có | có, “Nobody yet” | Q-EA-33 |

## 2. Bảng “màn đã làm bị ảnh hưởng” (rule 37)

| Màn đã làm | Điểm liên quan | Kết quả rà |
|---|---|---|
| Workspaces — vào chi tiết (Q-W-08) | Q-W-08 hỏi màn chi tiết kiểm ở sheet nào | Sheet Assisted workspace làm màn này (một case mở bằng URL, các case khác mở bằng bấm tên workspace). Câu Q-W-08 còn mở ở sheet Workspaces, chờ Hanna đóng. |
| Workspaces — cột Status, coverage (Q-W-09) | Chip “Preparing” và % coverage ở chi tiết phải khớp danh sách | Các case chip trạng thái, coverage sau upload và coverage ở màn Workspaces dùng cùng số và chip với sheet Workspaces; Q-W-09 (trạng thái khác Preparing) vẫn mở. |
| Workspaces — phân quyền (Q-W-11) | Customer Viewer xem danh sách | Đã đổi 1 ô ở v1.13 (Expected case Customer Viewer; bỏ Q-W-11 ở case này). Q-W-11 còn ở sheet Workspaces (Workspaces_041, “Customer Admin thấy workspace của mọi scope”). Sheet Scopes không dùng mã Q-W-11. |
| Scopes — Scope_107, Q-S-20 | “Workspace mới hiện ở màn Workspaces”; workspace tạo ngay hay sau một khoảng; trạng thái ban đầu | Case “Workspace mới” (workspace mới, 0 of 61, mọi requirement Missing) mở workspace sau khi đã tạo, không phụ thuộc “tạo ngay hay sau”. Trạng thái ban đầu Preparing (case chip trạng thái) lấy từ hệ thống, vẫn chờ Q-S-20. Scope_107 không đổi. |
| Scopes — Change tier | Số requirement theo tier (44 / 61 / 76) | Ba case theo tier dùng 44 (hệ thống), 61 (hệ thống), 76 (chỉ sheet Frameworks, Q-EA-46). |
| Frameworks | Số requirement mỗi tier của Appendix 10 | Khớp với 44 và 61; 76 chưa kiểm được trên hệ thống. |
| Users — D43 | Người mất quyền vào scope thì requirement, evidence họ sở hữu được giao lại hoặc bỏ trống | Chưa có case ở sheet nào. Cần case ở sheet Users (mất quyền scope) hoặc Scopes (gỡ người khỏi scope); ghi vào `docs/VIEC-CON-MO.md`. |
| Request certification (nút ở chi tiết workspace, chỉ Customer Admin trên prototype), UC WSP-03 “Request support” | Nút thuộc phần đầu màn chi tiết | Chưa có case trong sheet nào (Q-W-08 gộp chung). Chờ Hanna chọn sheet, ghi vào `docs/VIEC-CON-MO.md`. |
| Evidence Library (Documents) | Chi tiết evidence, version, chip Expired, “Not mapped / Not linked” | Chưa có sheet. Case 002, 003 và các case kiểm kết quả ở Evidence Library sau upload, link, gỡ chỉ kiểm điều hướng và kết quả sau thao tác của module 07; cột UC của ba case sau dùng mã thao tác (EVA-03, EVA-04, EVA-05). |

## 3. Cấu trúc sheet (122 TC)

Điều hướng 3 · Phần đầu màn 4 · Cây requirement (nhóm, trạng thái, tìm kiếm, bộ lọc) 25 · Chi tiết requirement 20 · Upload evidence 28 · Link existing evidence 14 · Gỡ liên kết 6 · Owner 7 · Requirement theo tier 4 · Workspace Archived 4 · Phân quyền 11 · Bảo mật 3. Số này do script đếm lại từ `cases_ea.py` ở bản dựng v1.15; tổng 129.

## 4. Điều chưa có case (ghi lại để không mất)

- Thông báo gửi cho người được gán owner: UC EVA-06 không nói; chưa đặt câu hỏi.
- Cột Owner không có ở Figma Workspace / Requirement (Q-EA-33).
- Lọc “Clarification requested” (Q-EA-05) và yêu cầu làm rõ đang mở ở chi tiết requirement (Q-EA-15): Expected để trống.
- Request certification (nút ở chi tiết workspace, UC WSP-03 “Request support”): chưa có case; chờ Hanna chọn sheet.
- D43: đã có case hiển thị ô Owner khi owner bị gỡ quyền (blank Expected, Q-EA-57); thao tác gỡ quyền thuộc sheet Users, Scopes, chưa có case ở đó.

## 5. Câu hỏi

Toàn bộ Q-EA-01 → Q-EA-57 ở `cau-hoi_Assisted-workspace.md` (57 mã, 35 TC để trống Expected, 77 TC có Open question; bảng đổi mã so với bản cũ ở mục 2 của file đó).

## 6. Tự soát trước khi giao (rule 38) — bản v1.15

Quét bằng `quet-noi-dung_Assisted-workspace.py` (ở `exports/_build/v1.15/`, chạy trên `ea_flat.tsv` và `cases_ea.py` cùng thư mục), kết quả **0 phát hiện trên 129 case**. Các phép quét: Expected viết “from Medium/High”; Expected mơ hồ (“như Customer Admin”, “đúng định dạng”); case Expected trống mà không có câu hỏi; câu hỏi nhiều vế gắn ở từ hai case; Pre-condition nhóm 11 requirement không gắn Q-EA-45; case Owner không gắn Q-EA-33 hoặc Q-EA-56; case gỡ không gắn Q-EA-31; Pre-condition đăng nhập Customer User, Customer Viewer thiếu tên tài khoản; cột UC khác mã thao tác; Pre-condition và Step mở hai workspace khác nhau; dữ liệu requirement Partial tự đặt.
Chưa quét được bằng script (đã soát bằng mắt): Expected so với Figma; nguồn ghi trong câu hỏi.
