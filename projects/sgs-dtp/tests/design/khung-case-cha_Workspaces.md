# Khung case cha — sheet Workspaces (module 06 Workspace Management)

v0.1 · 2026-10-09 · Hanna chốt viết TC ngay (FB-062): sheet Workspaces dựng ở file v1.11, gồm màn danh sách, điều hướng, phân quyền, bảo mật; Gắn framework và Change tier ở sheet Scopes. Bản 1.11 dựng 35 case; bản 1.12 (FB-063) làm lại theo review Opus còn 45 case; mục 4 và 5 dưới đây là khung ban đầu, mục 7 là khung đúng với file 1.12. Làm theo `FB-052`, đổi luồng theo `FB-061`.

Nguồn đối chiếu: (1) UC v5.3 (SharePoint, đọc trực tiếp ngày 09/10, các dòng WSP-01 → WSP-06; câu chữ UC dưới đây là phần tóm lược, khi viết TC phải trích lại đúng dòng); (2) Figma `SGS DTP DS`, trang Screens · 05 Workspace & Evidence — **chưa đọc trong lượt này** (trang chỉ mở được ở khung nhỏ, sẽ đọc bằng Chrome ở bước sau); (3) hệ thống `sgs-dtp-ds-demo-prototype.vercel.app`, vai trò Customer Admin (Linh Tran), đọc ngày 09/10. Khi ba nguồn mâu thuẫn: UC > Figma > hệ thống (rule 1); mỗi điểm lệch là một câu hỏi `Q-W-nn`, AI không tự chọn.

## 1. Tóm tắt

- **Luồng tạo workspace đã đổi** (Hanna 09:15): không tạo từ màn Workspaces nữa; tạo từ **Scope chi tiết › khu Frameworks › nút Link framework › hộp thoại "Link a framework" › nút "Link and create workspace"**. Màn Workspaces (menu trái) chỉ là danh sách: tiêu đề, dòng mô tả, đếm "<n> workspaces", ô tìm kiếm, bảng Workspace · Tier · Evidence coverage · Status; không có nút tạo, không thấy bộ lọc (Q-W-02).
- Hộp thoại Link a framework trên hệ thống: ô **Framework** (6 lựa chọn: Appendix 10, ISO/IEC 27001, 42001, 27701, ISO 22301, TISAX); khi chọn thì hiện ô **Version** ("Only active versions are listed."); framework có tier thì hiện thêm **Protection tier of this organization** (radio, kèm số requirement: TISAX Normal 52 · High 70 · Very high 78); ghi chú "A workspace is created for this scope with the requirements of the chosen tier. You can change the tier later; uploaded evidence stays."; hai nút Cancel, Link and create workspace. **Không thấy** ô chọn mode (Assisted / Bulk), tên workspace, hay chu kỳ chứng nhận (Q-W-03).
- Với phiên bản đã gắn rồi, ô Version ghi "<tên> · already linked" (Appendix 10 · 2022). Chưa thử chọn (Q-W-05).
- Ở khu Frameworks của Scope, mỗi workspace là một dòng: Framework · version, Tier, Coverage (% và x / n), Status (Preparing), liên kết "Change tier". Hộp thoại **Change tier** liệt kê tier kèm số requirement (Appendix 10: Basic 44 · Medium 61 · High 76), nút Change tier tắt cho tới khi chọn tier khác. UC v5.3 chưa thấy dòng nào cho Đổi tier (Q-W-04).
- Chi tiết workspace (`/workspaces/ws-…`) là màn requirement của Assisted workspace: cây requirement theo nhóm, Owner, Expected evidence, nút Evidence library, Request certification. Màn này thuộc sheet Assisted workspace (làm sau), **không** thuộc sheet Workspaces.
- Chưa thấy nút Archive, Delete (UC WSP-04, WSP-05) trên danh sách, trên chi tiết Scope hay hộp thoại (Q-W-06).

## 2. Điều học từ Opus và áp vào đây

| # | Điều học | Áp vào Workspaces |
|---|---|---|
| 1 | Open question là câu hỏi thật có dấu ?, ghi nguồn, mã Q (rule 23) | Mọi Q-W-nn bên dưới viết dạng câu hỏi, ghi nguồn ngắn |
| 2 | Expected dựa vào điều chưa xác minh thì phải kèm câu hỏi (rule 31) | Case Archive/Delete, mode, chu kỳ: Expected để trống, hỏi |
| 3 | Giá trị tính toán: hiểu logic trước (rule 19/FB-057) | Số requirement theo tier (44/61/76, 52/70/78): kiểm bằng cách đếm trong cây requirement của framework, không nhập số từ màn một cách máy móc (Q-W-07) |
| 4 | Không viết case cho điều chưa có màn (FB-051) | Archive, Delete, bộ lọc, mode: nhóm trạng thái C, chưa viết |
| 5 | Giữ chữ của Hanna, dựng từ file mới nhất (rule 34/35) | Khi viết TC sẽ dựng từ file `v1.10` mới nhất, Cover ghi đúng FB |
| 6 | Một chức năng một sheet (rule 26) | Q-W-01 hỏi form tạo nằm sheet nào |

## 3. Ba nguồn nói gì, theo từng UC

| UC | UC v5.3 nói (tóm lược) | Figma | Hệ thống | Lệch → câu hỏi |
|---|---|---|---|---|
| WSP-01 Tạo workspace | Từ danh sách hoặc từ Scope, hai đường mở cùng một form; chọn framework, version, tier | Chưa đọc | Chỉ có đường từ Scope (hộp thoại Link a framework); danh sách Workspaces không có nút tạo | Q-W-01, Q-W-03 |
| WSP-02 Xem danh sách | Bộ lọc Active / Archived / đã xóa | Chưa đọc | Chỉ ô tìm kiếm, đếm "<n> workspaces"; cột Workspace, Tier, Evidence coverage, Status | Q-W-02 |
| WSP-03 Xem chi tiết / đổi tier | UC không có dòng Đổi tier; D11: một workspace hoạt động cho mỗi scope + standard, chu kỳ mới thì chuyển workspace cũ sang Archived sau khi xác nhận | Chưa đọc | Change tier có ở khu Frameworks của Scope; chi tiết workspace là màn requirement | Q-W-04, Q-W-05 |
| WSP-04 Archive | Chặn khi còn consulting request mở hoặc đã gửi tài liệu (D39, D54) | Chưa đọc | Không thấy nút | Q-W-06 |
| WSP-05 Xóa workspace rỗng | Chỉ xóa được workspace rỗng | Chưa đọc | Không thấy nút | Q-W-06 |
| WSP-06 Phạm vi hiệu lực | Tính phạm vi hiệu lực (effective scope) của workspace; theo bố cục v4 thuộc sheet Assisted workspace | Chưa đọc | Chưa tìm thấy | Làm ở sheet Assisted workspace |

## 4. Cây case cha

Trạng thái: **V** viết được ngay · **VQ** viết, Expected để trống kèm câu hỏi · **C** chờ, chưa viết. Số case IV là số dự kiến, chưa chốt.

### Điều hướng - Redirect

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Vào danh sách - Workspace list | Từ menu | 1. Bấm Workspaces ở menu trái | WSP-02 | V | HT /workspaces | — |
| Vào chi tiết - Workspace detail | Từ danh sách | 1. Bấm tên workspace trong bảng (mở màn requirement) | WSP-03 | V | HT | Q-W-08 |
| Vào chi tiết - Workspace detail | Từ Scope | 1. Bấm tên workspace ở khu Frameworks của Scope | WSP-03 | V | HT | — |

### Danh sách workspace - Workspace list

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Tiêu đề trang - Page header | Hiển thị | 1. Breadcrumb, tiêu đề, dòng mô tả "…not a compliance decision." | WSP-02 | V | HT | — |
| Thanh công cụ - Toolbar | Hiển thị | 1. Dòng đếm "<n> workspaces"<br>2. Ô tìm kiếm và chữ gợi ý | WSP-02 | V | HT | — |
| Bảng - Table | Hiển thị | 1. Cột Workspace (tên framework · version, scope · loại scope)<br>2. Cột Tier (có tier / "No tiers")<br>3. Cột Evidence coverage (% và "x of n requirements")<br>4. Cột Status (Preparing) | WSP-02 | VQ | HT | Q-W-09 |
| Tìm kiếm - Search | Tìm kiếm | 1. Tìm theo tên framework<br>2. Tìm theo tên scope<br>3. Không có kết quả | WSP-02 | VQ | HT | Q-W-10 |
| Bộ lọc - Filter | Chờ thiết kế | (chưa viết case) | WSP-02 | C | UC nêu Active / Archived / đã xóa; HT không có | Q-W-02 |
| Phân quyền - Permission | Theo vai trò | 1. Customer Admin thấy workspace của mọi scope của tổ chức<br>2. Vai trò khác chỉ thấy workspace của scope được gán | WSP-02 | VQ | HT; UC | Q-W-11 |

### Tạo workspace từ Scope — hộp thoại Link a framework (thuộc sheet nào: Q-W-01)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Mở hộp thoại - Open dialog | Mở hộp thoại | 1. Bấm Link framework ở khu Frameworks của Scope | WSP-01 | V | HT | Q-W-01 |
| Hộp thoại - Dialog | Hiển thị | 1. Tiêu đề, ô Framework bắt buộc, ghi chú "A workspace is created…", Cancel, Link and create workspace<br>2. Danh sách 6 framework kèm nhóm (ISO / IEC, ISO) và ghi chú tier | WSP-01 | V | HT | Q-W-12 |
| Chọn framework - Framework | Có tier | 1. Chọn TISAX: hiện Version, "Protection tier of this organization" với 3 tier kèm số requirement | WSP-01 | VQ | HT | Q-W-07 |
| Chọn framework - Framework | Không tier | 1. Chọn ISO/IEC 27001: hiện Version, không có khối tier | WSP-01 | VQ | HT | Q-W-03 |
| Version | Hiển thị | 1. Ghi chú "Only active versions are listed."<br>2. Phiên bản đã gắn ghi "already linked" | WSP-01 | VQ | HT | Q-W-05 |
| Không thành công - Failure | Không thành công | 1. Bấm Link and create workspace khi chưa chọn framework<br>2. Chưa chọn tier (framework có tier)<br>3. Cancel / × / Esc: không tạo workspace | WSP-01 | VQ | HT | Q-W-13 |
| Thành công - Success | Thành công | 1. Tạo workspace framework không tier<br>2. Tạo workspace framework có tier<br>3. Workspace mới hiện ở khu Frameworks của Scope (Preparing, 0%) và trong danh sách Workspaces | WSP-01 | VQ | HT; không bấm xác nhận khi đọc | Q-W-03, Q-W-14 |
| Trùng - Duplicate | Phiên bản đã gắn | 1. Chọn phiên bản "already linked" rồi tạo | WSP-01 | C | D11 vs HT chưa thử | Q-W-05 |
| Mode - Assisted / Bulk | Chọn mode | (chưa viết case) | WSP-01 | C | D20; HT không có ô mode | Q-W-03 |

### Đổi tier — Change tier (câu hỏi sheet: Q-W-01, UC: Q-W-04)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Mở hộp thoại | Mở hộp thoại | 1. Bấm Change tier ở dòng workspace | [NGOÀI UC] | VQ | HT | Q-W-04 |
| Hộp thoại | Hiển thị | 1. Tiêu đề "<scope> · <framework> · currently <tier>", 3 tier kèm số requirement<br>2. Tier hiện tại chọn sẵn, nút Change tier tắt | [NGOÀI UC] | VQ | HT | Q-W-04, Q-W-07 |
| Không thành công | Không thành công | 1. Cancel / × / Esc: giữ nguyên tier | [NGOÀI UC] | VQ | HT | Q-W-04 |
| Thành công | Thành công | 1. Đổi lên tier cao hơn: số requirement tăng, evidence đã tải giữ nguyên<br>2. Đổi xuống tier thấp hơn | [NGOÀI UC] | VQ | Ghi chú hộp thoại "uploaded evidence stays" | Q-W-15 |

### Archive và Delete

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Archive | Chờ thiết kế | (chưa viết case) | WSP-04 | C | UC D39, D54; HT không có nút | Q-W-06 |
| Delete | Chờ thiết kế | (chưa viết case) | WSP-05 | C | UC; HT không có nút | Q-W-06 |

### Phân quyền - Permission

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Danh sách / Link framework | Theo vai trò | 1. Customer Admin tạo được workspace<br>2. Vai trò khác: có thấy nút Link framework không | WSP-01 | VQ | HT chỉ thử Customer Admin | Q-W-11 |

## 5. Mỗi UC nằm ở đâu

| UC | Khối cấp I | Còn chờ |
|---|---|---|
| WSP-01 | Tạo workspace từ Scope | Mode, tên, chu kỳ, trùng phiên bản (Q-W-01, 03, 05) |
| WSP-02 | Danh sách workspace | Bộ lọc Active / Archived / đã xóa (Q-W-02) |
| WSP-03 | Điều hướng · Đổi tier | UC chưa có dòng Đổi tier (Q-W-04) |
| WSP-04 | Archive | Cả UC (Q-W-06) |
| WSP-05 | Delete | Cả UC (Q-W-06) |
| WSP-06 | Sheet Assisted workspace | Làm sau |

Quy ước "ít nhất 1 TC cho 1 UC": WSP-04, WSP-05 chưa đạt vì chưa có màn. Đề xuất không viết case giữ chỗ (như FB-051); chờ Hanna chọn (Q-W-06).

## 6. Câu hỏi cho Hanna

| Mã | Câu hỏi | Nguồn |
|---|---|---|
| Q-W-01 | **Đã trả lời 09/10 (FB-062): vẫn ở sheet Scopes.** Form tạo workspace giờ nằm ở Scope (hộp thoại Link a framework); có chuyển 11 case "Gắn framework" và hộp thoại tạo sang sheet Workspaces, hay giữ ở sheet Scopes và sheet Workspaces chỉ còn danh sách + Đổi tier + Archive/Delete? | UC WSP-01 nói "từ danh sách hoặc từ Scope, cùng một form"; HT chỉ có từ Scope; rule 26 |
| Q-W-02 | Danh sách Workspaces có bộ lọc Active / Archived / đã xóa như UC WSP-02 không? Hệ thống chỉ có ô tìm kiếm. | UC WSP-02; HT /workspaces |
| Q-W-03 | Hộp thoại Link a framework có ô chọn mode (Assisted / Bulk), tên workspace và chu kỳ chứng nhận không? Hệ thống chỉ có Framework, Version, tier. | UC D20, D11; HT |
| Q-W-04 | Đổi tier (Change tier) là chức năng chính thức không, và thuộc UC nào? UC v5.3 chưa thấy dòng nào; có nên giữ nhãn [NGOÀI UC]? | HT Change tier; UC |
| Q-W-05 | Chọn phiên bản đã "already linked" thì hệ thống chặn hay tạo chu kỳ mới (D11: workspace cũ chuyển Archived sau khi xác nhận)? | UC D11; HT ghi "already linked" |
| Q-W-06 | Archive (WSP-04) và Delete workspace rỗng (WSP-05) nằm ở đâu trên màn, và có khóa khi còn consulting request mở hoặc tài liệu đã gửi (D39, D54) như thế nào? | UC WSP-04, WSP-05; HT không có nút |
| Q-W-07 | Số requirement theo tier (Appendix 10: 44 / 61 / 76; TISAX: 52 / 70 / 78) lấy từ đâu và có khớp số đếm trong cây requirement của framework không? | HT hộp thoại; Frameworks Q-F-10 |
| Q-W-08 | Bấm vào dòng workspace mở màn requirement (Assisted) — màn này tính vào sheet Assisted workspace, đúng không? | HT; bố cục v4 |
| Q-W-09 | Cột Status chỉ có "Preparing" hay còn trạng thái khác (Archived…)? | HT; UC |
| Q-W-10 | Tìm kiếm trong danh sách Workspaces tìm theo trường nào (tên framework, tên scope, version)? | HT |
| Q-W-11 | Vai trò nào được thấy và được tạo workspace (Customer Admin, Scope user, vai trò SGS)? Mới thử Customer Admin. | UC; HT |
| Q-W-12 | Danh sách 6 framework trong hộp thoại lấy từ framework Active ở module Frameworks, đúng không? | HT; Frameworks FWK-06 |
| Q-W-13 | Khi chưa chọn framework hoặc chưa chọn tier thì nút Link and create workspace tắt hay báo lỗi? | HT chưa thử |
| Q-W-14 | Sau khi bấm Link and create workspace, hệ thống đóng hộp thoại và hiện thông báo gì, chuyển tới đâu? | HT chưa bấm xác nhận |
| Q-W-15 | Đổi tier xuống thấp hơn khi đã có evidence cho requirement chỉ thuộc tier cao: evidence xử lý thế nào? | HT ghi "uploaded evidence stays" |

Việc chưa làm: đọc Figma trang 05 Workspace & Evidence (và 05 Workspaces (Customer Admin), Bulk upload); đối chiếu lại câu chữ từng dòng UC v5.3.

## 7. Khung đúng với file v1.12 (sheet Workspaces, 45 case, 11 case trống Expected, 25 case có câu hỏi)

Nguồn đã đọc thêm ngày 09/10: Figma Screens · 05 Workspaces & Evidence (khung `Workspaces / List`, `Workspace / Requirement`) và Screens · 05 Workspaces (Customer Admin) (khung `Workspaces / List (Customer Admin)`, `Workspace created`).

Sheet này chỉ có màn danh sách và những gì quanh nó. Tạo workspace (Link a framework) và Change tier ở sheet Scopes (Q-W-01, Hanna 09/10). Màn chi tiết workspace (cây requirement, Evidence library) thuộc sheet Assisted workspace.

| Khối cấp I | Khu vực (cấp II) | Số case |
|---|---|---|
| Điều hướng | Vào danh sách · Vào chi tiết · Quay lại | 4 |
| Danh sách workspace | Tiêu đề trang · Trạng thái rỗng · Thanh công cụ · Bộ lọc · Bảng · Menu thao tác · Phân trang | 36 |
| Phân quyền | Customer Admin · Customer User · Customer Viewer | 3 |
| Bảo mật | Cách ly tenant | 2 |

**Logic Evidence coverage (rule 31).** Mỗi dòng workspace hiện `<x> of <n> requirements` và phần trăm. x là số requirement đã có evidence bắt buộc; n là số requirement của tier đã chọn (hộp thoại Link a framework và Change tier ghi cùng số: Appendix 10 Basic 44, Medium 61, High 76; TISAX Normal 52, High 70, Very high 78). Phần trăm = x / n × 100, làm tròn về số nguyên. Thử trên số Figma: 38/61 = 62.30% hiện 62%; 74/116 = 63.79% hiện 64%; 6/52 = 11.54% hiện 12%. Cùng một phép tính này, làm tròn lên hay xuống cho kết quả khác nhau ở 62.30 (lên sẽ ra 63), nên Figma cho thấy làm tròn thường ở các số này. Hệ thống: 8/76 = 10.53% hiện 11%. Chưa có số nào ở phần thập phân đúng .5, dưới 0.5%, hay từ 99.5%; ba case biên để trống Expected và hỏi theo Q-S-11. Framework hiện có chỉ có 44 đến 116 requirement nên chưa dựng được n = 8 hay 250; điều này nằm trong câu hỏi của ba case biên. Q-W-07 còn hỏi n có khớp cây requirement của framework không.

**Điểm ba nguồn khác nhau.**
- Nút "+ New workspace" và menu ba chấm ở mỗi dòng: có ở Figma Customer Admin, không có ở hệ thống; Hanna đã chuyển việc tạo sang Scopes nên case "Không có nút tạo workspace" theo lời Hanna; menu ba chấm hỏi ở Q-W-06.
- Dòng mô tả trang: ba bản khác nhau (Q-W-17).
- Trạng thái workspace mới tạo: Figma "New · no evidence yet", hệ thống "Preparing" (Q-W-09).
- Phân trang: Figma "‹ Page 1 of 1 ›", hệ thống có Items per page và số trang (Q-W-18).
- Ô tìm kiếm của hệ thống tìm được cả tier và status (Q-W-10).

**Câu hỏi.** Q-W-01 đã trả lời. Có ở file: Q-W-02, 03, 04, 06, 07, 08, 09, 10, 11, 16, 17, 18, 19, 20; Q-S-07, Q-S-11, Q-S-26 dùng lại của Scopes. Chưa có ở file: Q-W-05, Q-W-12, 13, 14, 15 (thuộc case Gắn framework ở Scopes, chờ Hanna quyết nơi ghi).
