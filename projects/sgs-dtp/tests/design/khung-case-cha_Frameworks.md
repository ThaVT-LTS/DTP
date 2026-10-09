# Khung case cha — sheet Frameworks (module 04 Framework Content Management)

v0.1 · 2026-10-08 · Đề xuất để Hanna duyệt; chưa có TC nào được viết. Làm theo `FB-052`. Số case IV bên dưới do script đếm từ danh sách trong bảng, là số **dự kiến** của AI, chưa phải số chốt.

Nguồn đối chiếu: (1) 7 dòng UC FWK-01 → FWK-07 Hanna dán lúc 19:55 ngày 07/10 (`docs/analysis/uc-fwk_v4-dong-dan.md`); (2) Figma `SGS DTP DS`, trang `Screens · 04 Frameworks`, 7 khung đọc ngày 08/10; (3) hệ thống thực tế `sgs-dtp-ds-demo-prototype.vercel.app`, vào bằng bộ chọn vai trò Demo, đọc ngày 08/10; (4) file mẫu import `docs/source/SGS_DTP_Framework_Import_Template ver 1.xlsx` (SharePoint, 18/09). Thứ tự khi ba nguồn mâu thuẫn theo `rules/tc-authoring.md` rule 1: UC > Figma > hệ thống; mọi điểm lệch thành câu hỏi `Q-F-nn`, AI không tự chọn.

## 1. Tóm tắt

- Module này một sheet `Frameworks`, đúng dòng đã ghi ở `tests/design/bo-cuc-sheet_uc-v4.md`. Có **57 nhóm cấp III** thuộc **11 khối cấp I**, dự kiến **131 case IV**: 41 case viết được ngay, 77 case viết nhưng có ý Expected chưa có căn cứ, 13 case chờ.
- **Ba UC chưa có màn ở Figma lẫn hệ thống: FWK-04 Tạo framework, FWK-05 Sửa metadata, FWK-07 Rút framework.** Trang danh sách chỉ có hai nút `Download template` và `Import framework`; menu ba chấm ở chi tiết chỉ có một mục `Import new version`. Ba khối này chỉ được giữ chỗ ở cấp I, không có case nào (xem câu hỏi Q-F-15).
- **Điểm UC lệch với màn nhiều nhất:** UC nói import là *cập nhật* framework có sẵn (content_version phải tăng, dòng cũ chuyển trạng thái retired) và tách `standard edition` với `content version`; Figma, hệ thống và file mẫu import đều chỉ có một cột `Version`, và hộp thoại Import ghi "A new version of an existing framework (same code, different version) is added as its own entry". Ảnh hưởng tới nhóm Nhập framework (Q-F-04).
- **Một chỗ Figma và hệ thống nói ngược nhau** ở hộp thoại Activate: Figma ghi "SGS assigns each scope a tier: Basic, Medium or High", hệ thống ghi "Each customer chooses the tier of their scope: Basic, Medium or High" (Q-F-07).

## 2. Điều học từ sheet Scopes và cách áp vào đây

| # | Điều học từ Scopes v1.5 | Áp vào Frameworks |
|---|---|---|
| 1 | Cấp I là khối của màn: Điều hướng · Danh sách · Chi tiết · Phân quyền · Bảo mật | Giữ năm khối đó; thêm khối theo từng thao tác của module: Nhập, Bản nháp, Kích hoạt, và ba khối giữ chỗ (Rút, Tạo, Sửa) |
| 2 | Cấp II là khu vực hoặc hộp thoại, cấp III là nhóm: Hiển thị · Mở hộp thoại · Không thành công · Thành công · Tìm kiếm · Sắp xếp | Cùng tên nhóm; ví dụ Hộp thoại Import có Mở hộp thoại · Hiển thị nội dung · Không thành công · Thành công |
| 3 | Case bấm nút gửi mà không lưu được, và Cancel, ×, Esc, nằm ở **Không thành công**; nhóm này đứng **trước** Thành công | Áp cho Import, Activate, Discard draft. Thứ tự này còn **chờ Hanna chọn** (rule 8) |
| 4 | Kết quả kiểm ở nơi hành động trả về; nơi khác trong cùng sheet kiểm ở khu vực của nơi đó | Dòng Draft trong danh sách kiểm ở khu vực Bảng danh sách, không lặp lại ở nhóm Thành công của Import |
| 5 | Chỗ hiển thị khác nhau theo loại thì mỗi loại một case | Theo loại framework: có tier / không tier; theo trạng thái: Active / Draft |
| 6 | Điểm hiển thị ở màn khác hay vai trò khác đặt ở sheet của hành động (rule 27) | Sau Activate, Customer Admin thấy framework trong danh sách chọn của Link a framework: đặt ở khối Kích hoạt |
| 7 | Giá trị tính toán có nhiều case với số cụ thể (FB-048) | `Total to meet` của bảng Tiers và số đếm theo dimension; cách ghi Expected còn **chờ Hanna chọn A hoặc B** |
| 8 | Chưa có căn cứ thì để trống Expected và ghi câu hỏi; UC nêu mà màn chưa có thì không viết case giữ chỗ (như Scope_108 Hanna đã bỏ) | Nhóm trạng thái `Chờ`: chỉ ghi ở đây và ở bảng UC → sheet của Cover, chưa viết case |
| 9 | Pre-condition chỉ là vai trò đăng nhập; mở màn là Step 1 (FB-040) | Mọi case ghi vai trò; thao tác dữ liệu ở màn khác chỉ ghi khi cần |
| 10 | Không viết case gọi API (FB-039); tải file qua giao diện vẫn là thao tác giao diện | Không có case API; tải file mẫu kiểm bằng nút trên giao diện |

## 3. Ba nguồn nói gì, theo từng UC

| UC | UC v4 nói | Figma có | Hệ thống có | Điểm lệch → câu hỏi |
|---|---|---|---|---|
| FWK-01 Xem danh sách | Cột: code, standard edition, content version, content level (Full / Identity only), status (Draft / Active / Withdrawn), affiliates của Bulk. Framework đầu tiên: ISO/IEC 27001, 42001, CSMA (Appendix 10) | Khung `Frameworks / List`: Framework (tên + mã), Version, Issued by, Tiers, Requirements, Status (Draft · not active, Active), Updated, biểu tượng tải; ô tìm "Search code or name"; nút Download template, Import framework; "6 frameworks" | Giống Figma; 8 framework (có thêm ISO 22301, ISO/IEC 27701, TISAX; 27001 và Appendix 10 mỗi mã hai phiên bản); mũi tên sắp xếp ở 4 cột; "Items per page" 10 · 25 · 50 · 100; tìm không có kết quả hiện "No results for “…”" | Không có cột content level, affiliates, trạng thái Withdrawn (Q-F-01, Q-F-02). Có thêm cột Tiers, Requirements, Updated, Issued by, biểu tượng tải, sắp xếp mà UC không nêu (Q-F-11, Q-F-13) |
| FWK-02 Xem chi tiết | Tab: Overview (metadata, status, tiers, applicability read-only), Requirements (cây chỉ đọc kèm tier, expected evidence, status), Bulk settings (CFG-01 đến 03), History. Không có thêm, sửa, retire requirement | `Framework / Detail`: tab Overview, Requirements, Other versions; ba khối Framework, Tiers, Content. `Framework / Requirements`: cây, ô tìm, lọc All tiers, khung chi tiết requirement | Giống Figma. Tab Other versions có nhãn "No design yet". Framework không tier: không có khối Tiers, khối Content ghi Clauses thay cho Dimensions và Control measures. Không có nút thêm, sửa, retire | Không có Bulk settings, History (Q-F-03); không thấy trạng thái requirement, chỉ có chip tier (Q-F-09); Figma Detail ghi tier High là 18 mới / 79 tổng nhưng Content ghi 76 requirement, hệ thống ghi 15 / 76 (Q-F-10) |
| FWK-03 Import | Tải file XLSX (Framework, Tiers, Requirements, Expected_Evidence; EN và ZH) để tạo hoặc cập nhật; có báo cáo kiểm tra và bảng tóm tắt thay đổi (added, updated, retired) trước khi xác nhận. Chặn khi ERROR, hiện WARNING và INFO. Cập nhật: content_version phải tăng, mã cũ giữ liên kết evidence, dòng bị retire bằng status, mã retire không dùng lại | `Frameworks / Import`: 2 bước (tải file mẫu, tải file đã điền), giới hạn 20 MB, nút Cancel, Check file; `Import errors`: banner "3 errors in bcm-2019.xlsx", bảng Sheet · Row · Column · Problem, ô Corrected file; `Framework / Draft preview`: "File check passed" | Hộp thoại Import giống Figma. Hộp thoại mô tả: "One file = one framework version. A new version of an existing framework (same code, different version) is added as its own entry. Sheets: Framework (one row), Tiers (leave empty if the framework has no tiers), Requirements, Expected_Evidence." Chưa bấm Check file trên hệ thống | Không có bảng tóm tắt thay đổi, không có WARNING và INFO, không thấy content_version (Q-F-04, Q-F-06). File mẫu ver 1 chỉ có sheet Framework, Requirements, Expected_Evidence, không có Tiers, không có cột tiếng Trung, không có content_version (Q-F-06) |
| FWK-04 Tạo framework | Tạo chỉ có định danh (code, tên EN/ZH, standard edition, issuing body, description, effective date); code không đổi được | Không có | Không có nút | Chưa có thiết kế (Q-F-15) |
| FWK-05 Sửa metadata | Sửa tên, mô tả, standard edition, issuing body, effective date; code và content version không sửa được; có ghi vết | Không có | Không có (menu ba chấm chỉ có Import new version) | Chưa có thiết kế (Q-F-15) |
| FWK-06 Kích hoạt | Chuyển Draft sang Active; chỉ kích hoạt khi có Active retention policy (CFG-01); framework identity-only chỉ dành cho Bulk | `Framework / Activate`: hộp thoại với 3 gạch đầu dòng, Cancel, Activate framework | Hộp thoại Activate; gạch thứ hai khác Figma. Trang Settings ghi "This page has no design yet" (UC-CFG-001) | Không có kiểm tra retention policy ở cả hai (Q-F-07); ai chọn tier (Q-F-07); chưa thấy kết quả sau khi bấm Activate framework (Q-F-08) |
| FWK-07 Rút khỏi sử dụng mới | Chặn khách tạo workspace mới với framework; workspace cũ vẫn dùng; không tạo workspace Bulk mới | Không có | Không có nút, không có trạng thái Withdrawn | Chưa có thiết kế (Q-F-02, Q-F-15) |

Ghi chú: ngoài bảng, màn có hai chức năng UC không nêu: **Discard draft** (nút ở Draft preview và hộp thoại "Discard draft?") và **Download template**. Hai chỗ này được gắn nhãn `[NGOÀI UC]` như bốn case Đổi tier ở sheet Scopes (Q-F-11).

## 4. Cây case cha

Cột `Trạng thái`: **V** viết được ngay · **VQ** viết, có ý Expected để trống kèm câu hỏi · **C** chờ, chưa viết case. Số trong ngoặc ở tên khối là số case IV dự kiến.

### Điều hướng - Redirect (5)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Vào danh sách - Framework list | Từ menu (1) | 1. Bấm Frameworks ở menu trái | FWK-01 | V | HT /ops/frameworks | — |
| Vào chi tiết - Framework detail | Từ danh sách (2) | 1. Bấm tên framework Active (mở tab Overview)<br>2. Bấm tên framework Draft (mở màn Draft preview) | FWK-02 | V | HT; Figma Detail, Draft preview | — |
| Quay lại - Back | Từ chi tiết (2) | 1. Bấm nút mũi tên quay lại ở chi tiết framework Active<br>2. Bấm nút mũi tên quay lại ở Draft preview | FWK-02 | V | HT | — |

### Danh sách framework - Framework list (25)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Tiêu đề trang - Page header | Hiển thị (3) | 1. Breadcrumb, tiêu đề và dòng mô tả<br>2. Nút Download template<br>3. Nút Import framework | FWK-01, FWK-03 | V | Figma List; HT | — |
| Thanh công cụ - Toolbar | Hiển thị (2) | 1. Dòng đếm "<n> frameworks"<br>2. Ô tìm kiếm và chữ gợi ý | FWK-01 | V | Figma List; HT | — |
|  | Tìm kiếm (4) | 1. Tìm theo mã (code)<br>2. Tìm theo tên (name)<br>3. Không có kết quả<br>4. Xoá chữ tìm, danh sách trở lại đủ dòng | FWK-01 | VQ | Figma List ("Search code or name"); HT ("No results for") | Q-F-12 (kết quả tìm theo mã, theo tên: chưa kiểm trên hệ thống) |
| Bảng danh sách - Table | Hiển thị cột (1) | 1. Tiêu đề cột và thứ tự: Framework, Version, Issued by, Tiers, Requirements, Status, Updated | FWK-01 | V | Figma List; HT | — |
|  | Hiển thị dòng theo loại (4) | 1. Framework Active có tier<br>2. Framework Active không tier (cột Tiers hiện "—")<br>3. Framework Draft (chip "Draft · not active", Updated dạng "Today, hh:mm")<br>4. Hai phiên bản của cùng một mã hiện thành hai dòng | FWK-01 | V | Figma List; HT | — |
|  | Sắp xếp (4) | 1. Sắp xếp cột Framework<br>2. Sắp xếp cột Version<br>3. Sắp xếp cột Issued by<br>4. Sắp xếp cột Requirements | FWK-01 | VQ | HT (có mũi tên sắp xếp ở 4 cột); Figma List chưa vẽ | Q-F-13 (thứ tự mặc định và kết quả sắp xếp chưa kiểm) |
|  | Cột UC nêu mà màn chưa có (3) | 1. Cột Content level (Full / Identity only)<br>2. Cột affiliates của framework Bulk<br>3. Trạng thái Withdrawn | FWK-01 | C | Chỉ có ở UC; Figma List và HT không có | Q-F-01, Q-F-02 |
|  | Biểu tượng tải ở mỗi dòng (1) | 1. Bấm biểu tượng tải ở một dòng | [NGOÀI UC] | VQ | Figma List; HT (không kiểm tải thật) | Q-F-11 |
| Phân trang - Pagination | Hiển thị (2) | 1. Dòng "1–<n> of <n> items" và "1 of 1 page"<br>2. Chọn Items per page: 10, 25, 50, 100 | FWK-01 | V | HT; Figma List | — |
|  | Nhiều trang (1) | 1. Chuyển sang trang 2 khi có hơn 10 framework | FWK-01 | C | Cần dữ liệu từ 11 framework trở lên; hệ thống hiện có 8 | — |

### Chi tiết framework - Framework detail (30)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Phần đầu - Header | Hiển thị (2) | 1. Framework Active: tên, chip Active, dòng "code · version · issuing body", nút quay lại, nút ba chấm<br>2. Framework Draft: chip "Draft · not active", nút Discard draft và Activate (không có nút ba chấm) | FWK-02 | V | Figma Detail, Draft preview; HT | — |
| Menu ba chấm - More menu | Mở menu (1) | 1. Mở menu ở framework Active, chỉ có mục "Import new version" | FWK-02, FWK-03 | VQ | HT; Figma Detail vẽ nút, chưa vẽ nội dung menu | Q-F-05 (mục này mở hộp thoại nào chưa kiểm) |
| Điều hướng trong màn - In-page tabs | Chuyển tab (2) | 1. Framework Active có 3 mục: Overview, Requirements, Other versions; mặc định Overview<br>2. Framework Draft có 3 mục: Framework, Tiers, Requirements | FWK-02 | V | Figma; HT | — |
|  | Tab UC nêu mà màn chưa có (2) | 1. Tab Bulk settings (CFG-01 đến CFG-03)<br>2. Tab History | FWK-02 | C | Chỉ có ở UC; Figma và HT không có | Q-F-03 |
| Tổng quan - Overview | Hiển thị khối Framework (1) | 1. Framework Active: Code, Issued by, Version, Effective date, Description | FWK-02 | V | Figma Detail; HT | — |
|  | Hiển thị khối Tiers (2) | 1. Framework có tier: bảng Code, Tier, Rank, New at this tier, Total to meet<br>2. Framework không tier: không có khối Tiers | FWK-02 | V | HT (ISO/IEC 27001 · 2022); Figma Detail | — |
|  | Giá trị tính toán: Total to meet (3) | 1. Tier Basic: New at this tier 44, Total to meet 44<br>2. Tier Medium: New 17, Total 61<br>3. Tier High: New 15, Total 76 | FWK-02 | VQ | HT (Appendix 10 · 2022). Figma Detail ghi High là 18 và 79, lệch với 76 ở khối Content | Q-F-10, chờ chọn A hoặc B ở FB-048 |
|  | Hiển thị khối Content theo loại (2) | 1. Framework có tier: Dimensions, Control measures, Requirements, Expected evidence items<br>2. Framework không tier: Clauses, Requirements, Expected evidence items | FWK-02 | V | HT (Appendix 10 · 2022 và ISO/IEC 27001 · 2022); Figma Detail (loại có tier) | — |
| Yêu cầu - Requirements | Hiển thị (3) | 1. Tiêu đề và dòng tóm tắt "… Read only — import a new version to change them."<br>2. Cây: dimension kèm số, mở ra thấy requirement kèm chip Basic, From Medium, From High<br>3. Chọn một requirement: khung bên phải hiện code, tiêu đề, mô tả, Applies to, Not required for, Sort order, Source, Expected evidence | FWK-02 | V | Figma Requirements; HT | — |
|  | Chỉ đọc (1) | 1. Không có nút thêm, sửa hoặc retire requirement | FWK-02 | V | Figma Requirements; HT; ghi chú của UC | — |
|  | Tìm kiếm (3) | 1. Tìm theo mã requirement<br>2. Tìm theo tiêu đề<br>3. Không có kết quả | FWK-02 | VQ | Figma, HT có ô "Search requirements"; kết quả chưa kiểm | Q-F-12 |
|  | Lọc theo tier (4) | 1. Chọn Basic<br>2. Chọn Medium<br>3. Chọn High<br>4. Chọn All tiers | FWK-02 | VQ | HT (4 lựa chọn: All tiers, Basic, Medium, High); kết quả lọc chưa kiểm | Q-F-12 |
|  | Giá trị tính toán: số đếm theo dimension (2) | 1. Cộng số của 7 dimension bằng số Requirements (76)<br>2. Cùng kiểm với framework có 79 requirement (bản Draft) | FWK-02 | VQ | HT: 14+14+7+11+14+7+9 = 76 và 14+14+8+11+15+7+10 = 79 | Chờ chọn A hoặc B ở FB-048 |
|  | Trạng thái requirement (1) | 1. Hiển thị trạng thái của requirement (UC nêu "status") | FWK-02 | C | Chỉ thấy chip tier; ô lọc tên "Filter by status" nhưng chữ hiện "All tiers" | Q-F-09 |
| Phiên bản khác - Other versions | Hiển thị (1) | 1. Bảng Version, Status, Imported by, Activated | [NGOÀI UC] | C | HT ghi "No design yet"; Figma không có khung | Q-F-03 |

### Nhập framework - Import framework (33)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Hộp thoại Import - Import dialog | Mở hộp thoại (2) | 1. Mở từ nút Import framework ở danh sách<br>2. Mở từ mục "Import new version" ở chi tiết framework Active | FWK-03 | VQ | Figma Import; HT (mới mở từ danh sách) | Q-F-05 |
|  | Hiển thị nội dung (3) | 1. Tiêu đề, bước 1 "Download the template and fill it in", bước 2 "Upload the completed file"<br>2. Vùng kéo thả và dòng "Excel (.xlsx) · up to 20 MB · checked before anything is saved"<br>3. Nút Cancel và Check file khi chưa chọn file | FWK-03 | VQ | Figma Import; HT | Q-F-14 (trạng thái nút Check file khi chưa chọn file) |
|  | Tải file mẫu (2) | 1. Bấm Download template (.xlsx) trong hộp thoại<br>2. Bấm Download template ở đầu danh sách | [NGOÀI UC] | VQ | Figma Import, List; HT (không tải thật) | Q-F-11 |
| Chọn file - File picker | Hiển thị (2) | 1. Chọn file .xlsx hợp lệ: thẻ file có tên, dung lượng, dấu tích, nút ×<br>2. Bấm × để bỏ file đã chọn | FWK-03 | V | Figma Import | — |
|  | Không thành công (2) | 1. Chọn file không phải .xlsx<br>2. Chọn file lớn hơn 20 MB | FWK-03 | VQ | Giới hạn có ở Figma Import; thông báo lỗi chưa có | Q-F-14 |
| Kiểm tra file - Check file | Không thành công (15) | 1. Mã cha không tồn tại (parent_requirement_code)<br>2. Mã requirement bị trùng (requirement_code)<br>3. Expected evidence trỏ vào dòng nhóm (is_assessable = FALSE)<br>4. Banner "<n> errors in <tên file>" và dòng "Nothing was imported"<br>5. Tải file đã sửa ở ô "Corrected file" rồi Check file<br>6. Bấm Cancel khi đang có lỗi<br>7. Bấm × khi đang có lỗi<br>8. Bấm Esc khi đang có lỗi<br>9. Hai dòng ở sheet Framework<br>10. Thiếu framework_code, framework_name hoặc version<br>11. Requirement tự là cha của chính nó<br>12. Cha con tạo vòng lặp<br>13. is_assessable không phải TRUE hoặc FALSE<br>14. Mã expected evidence bị trùng<br>15. mandatory không phải TRUE hoặc FALSE | FWK-03 | VQ | Figma Import errors (3 lỗi đầu có chữ nguyên văn); 7 lỗi sau theo sheet Validation_Rules của file mẫu ver 1 | Q-F-06, Q-F-14 (chữ báo lỗi của 7 lỗi sau chưa có) |
|  | Không thành công theo UC mà Figma chưa có (2) | 1. content_version không tăng khi cập nhật<br>2. Dùng lại mã requirement đã retire | FWK-03 | C | Chỉ có ở UC | Q-F-04 |
|  | Thành công (2) | 1. Import file hợp lệ của framework mới (mã chưa có)<br>2. Import file hợp lệ là phiên bản mới của mã đã có (Version khác) | FWK-03 | VQ | Figma Draft preview, Import (câu "added as its own entry"); chưa bấm Check file trên hệ thống | Q-F-04, Q-F-08 |
|  | Thành công theo UC mà Figma chưa có (3) | 1. Bảng tóm tắt thay đổi added, updated, retired<br>2. Cảnh báo WARNING và INFO<br>3. Import vào framework identity-only | FWK-03 | C | Chỉ có ở UC | Q-F-04, Q-F-06 |

### Bản nháp - Draft preview (12)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Phần đầu - Header | Hiển thị (2) | 1. Tên, chip "Draft · not active", dòng "code · version · issuing body"<br>2. Nút Discard draft và Activate | FWK-03, FWK-06 | V | Figma Draft preview; HT | — |
| Nội dung bản nháp - Draft content | Hiển thị (3) | 1. Khối Framework: Code, Issued by, Version, Effective date "Not set", Description<br>2. Khối Tiers: Basic 44/44, Medium 17/61, High 18/79<br>3. Khối Requirements: "7 dimensions · 27 control measures · 79 requirements · 79 expected evidence items" | FWK-02, FWK-03 | V | Figma Draft preview; HT (/ops/frameworks/fw-a10-amended) | — |
| Khung Import bên phải - Import panel | Hiển thị (2) | 1. "File check passed" và dòng "No errors. The draft is ready to activate."<br>2. Khung "After activation" | FWK-03, FWK-06 | VQ | Figma và HT; câu về ai chọn tier khác nhau | Q-F-07 |
| Huỷ bản nháp - Discard draft | Mở hộp thoại (1) | 1. Bấm Discard draft: hộp thoại "Discard draft?" kèm câu "Customers never saw it. You can import the file again later." | [NGOÀI UC] | V | HT; Figma chưa vẽ hộp thoại | Q-F-11 |
|  | Không thành công (3) | 1. Bấm Cancel<br>2. Bấm ×<br>3. Bấm Esc | [NGOÀI UC] | VQ | HT (Cancel, ×); kết quả chưa kiểm | Q-F-11 |
|  | Thành công (1) | 1. Bấm Discard draft trong hộp thoại | [NGOÀI UC] | VQ | HT (chưa bấm xác nhận) | Q-F-08, Q-F-11 |

### Kích hoạt framework - Activate framework (9)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Hộp thoại Activate - Activate dialog | Mở hộp thoại (1) | 1. Bấm Activate ở Draft preview: tiêu đề, câu hỏi "Activate <tên> · <version>?", ba gạch đầu dòng | FWK-06 | VQ | Figma Activate; HT. Gạch thứ hai khác nhau giữa hai nguồn | Q-F-07 |
|  | Không thành công (4) | 1. Bấm Cancel<br>2. Bấm ×<br>3. Bấm Esc<br>4. Kích hoạt khi chưa có Active retention policy (CFG-01) | FWK-06 | VQ | Cancel và × có ở Figma, HT; trường hợp retention policy: Settings ghi "No design yet" | Q-F-07 |
|  | Thành công (2) | 1. Kích hoạt framework có tier<br>2. Kích hoạt framework không tier | FWK-06 | VQ | Figma Activate; chưa bấm xác nhận trên HT. Chưa có bản nháp không tier để kích hoạt | Q-F-08 |
| Hiển thị với khách hàng - Customer view | Sau khi kích hoạt (2) | 1. Customer Admin mở hộp thoại Link a framework: framework vừa kích hoạt có trong danh sách chọn<br>2. Framework Draft chưa kích hoạt không có trong danh sách chọn | FWK-06 | VQ | HT: danh sách chọn có 6 mục gộp theo mã, không thấy chọn phiên bản; theo rule 27 đặt ở sheet của hành động | Q-F-08 |

### Rút framework - Withdraw framework (0)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Rút khỏi sử dụng mới | Chờ thiết kế (0) | 1. (chưa viết case) | FWK-07 | C | Không có nút, hộp thoại hay trạng thái Withdrawn ở Figma và hệ thống | Q-F-02, Q-F-15 |

### Tạo framework - Create framework (0)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Tạo framework chỉ có định danh | Chờ thiết kế (0) | 1. (chưa viết case) | FWK-04 | C | Không có nút hay form ở Figma và hệ thống | Q-F-15 |

### Sửa thông tin framework - Edit framework (0)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Sửa metadata | Chờ thiết kế (0) | 1. (chưa viết case) | FWK-05 | C | Không có nút hay form ở Figma và hệ thống; menu ba chấm chỉ có Import new version | Q-F-15 |

### Phân quyền - Permission (12)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| SGS Admin | Quyền theo vai trò (3) | 1. Thấy menu Frameworks, nút Download template và Import framework ở danh sách<br>2. Thấy Discard draft và Activate ở Draft preview<br>3. Thấy nút ba chấm ở framework Active | FWK-01 đến FWK-06 | V | HT (Minh Nguyen · SGS Admin) | — |
| SGS User | Quyền theo vai trò (2) | 1. Thấy menu Frameworks và danh sách, không có nút Download template và Import framework<br>2. Mở Draft preview, không có nút Discard draft và Activate | FWK-01, FWK-02 | VQ | HT (Grace Lin · SGS User); UC chỉ nêu SGS Admin | Q-F-16 |
| SGS Consultant | Quyền theo vai trò (1) | 1. Thấy menu Frameworks và danh sách, không có nút Download template và Import framework | FWK-01 | VQ | HT (Anna Lee · SGS Consultant); chưa mở chi tiết | Q-F-16 |
| SGS Auditor/Certification | Quyền theo vai trò (2) | 1. Menu không có Frameworks<br>2. Mở thẳng địa chỉ của danh sách | FWK-01 | VQ | HT (David Wu); menu đã kiểm, vào bằng địa chỉ chưa kiểm | Q-F-16 |
| Vai trò Customer | Quyền theo vai trò (4) | 1. Customer Admin: menu không có Frameworks<br>2. Customer User: menu không có Frameworks<br>3. Customer Viewer: menu không có Frameworks<br>4. Customer Admin mở thẳng địa chỉ của danh sách | FWK-01 | VQ | HT (Linh Tran · Customer Admin đã kiểm menu; User, Viewer chưa kiểm) | Q-F-16 |

### Bảo mật - Security (5)

| II · Khu vực | III · Nhóm | Case IV dự kiến | UC | TT | Căn cứ | Câu hỏi |
|---|---|---|---|---|---|---|
| Dữ liệu trong file import - Imported data | Hiển thị nguyên văn (2) | 1. Ô bắt đầu bằng dấu = trong file hiện nguyên văn trên bản nháp<br>2. Thẻ <script> trong Description hiện nguyên văn trên bản nháp | FWK-03 | VQ | Chưa kiểm trên hệ thống | Q-F-14 |
| Ghi vết - Audit log | Hành động được ghi (3) | 1. Import ghi một dòng ở Audit Logs<br>2. Kích hoạt ghi một dòng ở Audit Logs<br>3. Huỷ bản nháp ghi một dòng ở Audit Logs | FWK-03, FWK-06 | VQ | Menu Audit Logs có ở SGS Admin; nội dung dòng ghi vết chưa kiểm | Q-F-17 |

Tổng: **57** nhóm cấp III, **131** case IV dự kiến (V 41 · VQ 77 · C 13).

## 5. Mỗi UC nằm ở đâu

| UC | Khối cấp I | Còn chờ |
|---|---|---|
| FWK-01 | Điều hướng · Danh sách framework · Phân quyền | Cột content level, affiliates, trạng thái Withdrawn (Q-F-01, Q-F-02) |
| FWK-02 | Điều hướng · Chi tiết framework · Bản nháp | Tab Bulk settings, History, trạng thái requirement (Q-F-03, Q-F-09) |
| FWK-03 | Nhập framework · Bản nháp · Bảo mật | Bảng tóm tắt thay đổi, WARNING và INFO, content_version, identity-only (Q-F-04, Q-F-06) |
| FWK-04 | Tạo framework | Cả UC (Q-F-15) |
| FWK-05 | Sửa thông tin framework | Cả UC (Q-F-15) |
| FWK-06 | Kích hoạt framework | Kiểm tra retention policy, kết quả sau khi kích hoạt (Q-F-07, Q-F-08) |
| FWK-07 | Rút framework | Cả UC (Q-F-02, Q-F-15) |

Quy ước của Hanna "ít nhất 1 TC cho 1 UC": ba UC FWK-04, FWK-05, FWK-07 hiện chưa đạt vì chưa có màn để viết bước và kết quả. Nếu viết case giữ chỗ thì Step và Expected đều phải để trống, giống ba case Hanna ghi là "chưa hiểu ý" ở FB-051 và case Scope_108 Hanna đã bỏ. AI đề xuất không viết case giữ chỗ, chờ Hanna chọn (Q-F-15).

## 6. Câu hỏi cho Hanna

| Mã | Mức | Vấn đề | Ba nguồn nói gì | Ảnh hưởng | Cần Hanna |
|---|---|---|---|---|---|
| Q-F-01 | QUAN TRỌNG | Danh sách thiếu hai cột UC FWK-01 nêu | UC FWK-01 có cột content level (Full / Identity only) và affiliates của Bulk; Figma `Frameworks / List` và hệ thống không có hai cột này, và không có framework identity-only nào để xem. | Nhóm "Cột UC nêu mà màn chưa có" (3 case) | Chờ Figma bổ sung, hay đã bỏ khỏi MVP? |
| Q-F-02 | QUAN TRỌNG | Trạng thái Withdrawn | UC FWK-01 và FWK-07 có Withdrawn; Figma và hệ thống chỉ có Draft · not active và Active. | Nhóm Withdrawn ở danh sách; khối Rút framework | Withdrawn có làm ở MVP không, hiện ở đâu? |
| Q-F-03 | QUAN TRỌNG | Tab của màn chi tiết | UC FWK-02: Overview, Requirements, Bulk settings, History. Figma và hệ thống: Overview, Requirements, Other versions; hệ thống ghi "No design yet" ở Other versions. | Hai nhóm tab; khối Phiên bản khác | Other versions có phải History của UC không? Bulk settings chờ thiết kế Bulk? |
| Q-F-04 | CHẶN | Import là cập nhật hay thêm phiên bản riêng | UC FWK-03: cập nhật framework có sẵn, content_version phải tăng, dòng cũ retire bằng status, có bảng tóm tắt added/updated/retired. Figma Import và file mẫu ver 1: một file là một phiên bản, phiên bản mới của cùng mã "is added as its own entry"; Draft preview không có bảng tóm tắt. | Nhóm Thành công của Check file (2 case) và 3 case chờ | Hướng nào đúng? Nếu theo UC, màn nào hiện bảng tóm tắt? |
| Q-F-05 | NHỎ | Mục "Import new version" ở menu ba chấm | Hệ thống chỉ có mục này trong menu của framework Active; chưa bấm thử. Có mở hộp thoại Import giống nút ở danh sách, và có điền sẵn mã framework không? | Nhóm Mở hộp thoại Import và Mở menu ba chấm | Mở hộp thoại nào, nội dung có khác không? |
| Q-F-06 | QUAN TRỌNG | Mẫu import và mức cảnh báo | UC: sheet Framework, Tiers, Requirements, Expected_Evidence, có EN và ZH; hiện ERROR, WARNING, INFO. Hộp thoại Import ở Figma và hệ thống có sheet Tiers. File mẫu ver 1 (18/09) không có Tiers, không có cột tiếng Trung, không có content_version; sheet Validation_Rules có ERROR, WARNING, INFO. Figma Import errors chỉ hiện lỗi ERROR. | Nhóm Không thành công của Check file (7 case lấy từ Validation_Rules); nhóm chờ | Có file mẫu bản mới hơn ver 1 không? WARNING và INFO hiện ở đâu trên màn? |
| Q-F-07 | QUAN TRỌNG | Hộp thoại Activate | Figma: "SGS assigns each scope a tier: Basic, Medium or High." Hệ thống: "Each customer chooses the tier of their scope: Basic, Medium or High." Cùng khác ở khung "After activation" của Draft preview. UC FWK-06 còn nêu điều kiện Active retention policy (CFG-01); hai nguồn không có bước này, trang Settings chưa có thiết kế. | Nhóm Mở hộp thoại Activate, khung Import bên phải, case retention policy | Ai chọn tier? Kích hoạt khi chưa có retention policy thì màn báo gì? |
| Q-F-08 | CHẶN | Kết quả sau Check file, Activate, Discard draft | AI chưa bấm nút xác nhận nào trên hệ thống nên chưa biết: sau Check file thành công đi tới màn nào; sau Activate framework hiện thông báo gì, chip và cột Updated đổi ra sao; sau Discard draft về đâu. Figma không có khung cho các màn đó. Danh sách chọn của khách hàng hiện 6 mục gộp theo mã, không thấy chọn phiên bản. | Các nhóm Thành công (Import, Discard, Activate) và Hiển thị với khách hàng | Cho AI bấm xác nhận trong prototype (có nút Reset), hay Hanna cung cấp kết quả? |
| Q-F-09 | NHỎ | Trạng thái requirement | UC FWK-02: cây có tier, expected evidence và status. Hệ thống chỉ có chip tier (Basic, From Medium, From High); ô lọc có tên truy cập "Filter by status" nhưng chữ hiện "All tiers" và 4 lựa chọn là tier. | Nhóm Trạng thái requirement | Requirement có trạng thái (Active, Retired) hiện ở đâu? |
| Q-F-10 | NHỎ | Số liệu khối Tiers ở Figma Detail | Figma Detail của Appendix 10 · 2022: tier High 18 mới, 79 tổng; khối Content ngay dưới ghi 76 requirement. Hệ thống ghi 15 mới, 76 tổng. Figma Draft preview (bản amended) ghi 18 và 79, khớp với 79 requirement. | Nhóm Giá trị tính toán: Total to meet | Số trên Figma Detail là nhầm khung? |
| Q-F-11 | NHỎ | Chức năng có ở màn mà UC không nêu | Discard draft (nút và hộp thoại), Download template (đầu danh sách và trong hộp thoại Import), biểu tượng tải ở mỗi dòng của danh sách. Chưa biết biểu tượng ở mỗi dòng tải file nào. | 4 nhóm gắn [NGOÀI UC] | Thuộc UC nào, hay giữ [NGOÀI UC]? Tải ra file tên gì? |
| Q-F-12 | NHỎ | Tìm kiếm và lọc | Danh sách có chữ gợi ý "Search code or name"; chưa biết tìm theo Version hay Issued by có ra kết quả không. Ô tìm và lọc tier ở tab Requirements chưa kiểm kết quả. | Nhóm Tìm kiếm ở danh sách và Requirements | Tìm theo những trường nào? |
| Q-F-13 | NHỎ | Thứ tự mặc định và sắp xếp | Hệ thống xếp bản Draft lên đầu, các dòng sau không theo tên cũng không theo ngày Updated (Appendix 10 · 2022 ở cuối dù Updated là 14 Aug 2025). Chưa kiểm kết quả khi bấm mũi tên ở 4 cột. | Nhóm Sắp xếp | Thứ tự mặc định là gì? |
| Q-F-14 | QUAN TRỌNG | Thông báo lỗi khi chọn và kiểm file | Chưa có chữ nguyên văn cho: file không phải .xlsx, file lớn hơn 20 MB, 7 lỗi từ Validation_Rules; chưa biết nút Check file có bấm được khi chưa chọn file. Ô công thức hoặc thẻ script trong file hiện ra sao ở bản nháp chưa kiểm. | Các nhóm Không thành công của Import; nhóm Dữ liệu trong file import | Chữ lỗi nguyên văn là gì? |
| Q-F-15 | CHẶN | FWK-04, FWK-05, FWK-07 chưa có màn | Figma và hệ thống không có nút, form hay trạng thái cho ba UC này. Quy ước "ít nhất 1 TC cho 1 UC" chưa đạt. | 3 khối giữ chỗ | (A) chờ thiết kế, ghi ở bảng UC → sheet, không viết case; hay (B) viết 1 case mỗi UC, Step và Expected để trống? |
| Q-F-16 | QUAN TRỌNG | Quyền xem Frameworks | UC chỉ nêu SGS Admin. Hệ thống: SGS User và SGS Consultant vào được danh sách (không có nút Import, Download template; SGS User mở được Draft preview, không có Activate, Discard draft); SGS Auditor/Certification và vai trò Customer không có menu Frameworks. Chưa kiểm: mở thẳng địa chỉ, Customer User và Customer Viewer. | Khối Phân quyền (12 case) | SGS User và SGS Consultant được xem Frameworks là đúng thiết kế? |
| Q-F-17 | NHỎ | Ghi vết | UC FWK-05 ghi "Changes are audited"; menu Audit Logs có ở SGS Admin nhưng nội dung dòng ghi vết cho import, kích hoạt, huỷ bản nháp chưa kiểm. Tên màn nhật ký ở ba sheet cũ ghi ba kiểu khác nhau (FB-051); lần này thấy menu tên "Audit Logs". | Nhóm Ghi vết | Dòng ghi vết có những cột nào, ghi gì? |

## 7. Việc AI đã làm trên hệ thống thực tế (để Hanna biết dữ liệu có bị đổi không)

- Vào bằng bộ chọn vai trò Demo (không nhập mật khẩu), lần lượt: Minh Nguyen (SGS Admin), Grace Lin (SGS User), Anna Lee (SGS Consultant), David Wu (SGS Auditor/Certification), Linh Tran (Customer Admin). Không bấm nút Reset.
- Với SGS Admin: mở danh sách, hai chi tiết (Appendix 10 amended là Draft, Appendix 10 · 2022, ISO/IEC 27001 · 2022), các tab Overview, Requirements, Other versions, menu ba chấm, ô lọc tier; mở hộp thoại Import, Activate, Discard draft rồi bấm **Cancel**; gõ "zzz" vào ô tìm; mở trang Settings.
- Với Customer Admin: mở Scopes → chi tiết `Head office · Taipei` → hộp thoại Link a framework, mở danh sách chọn rồi đóng bằng Esc, **không** bấm Link and create workspace.
- **Không** bấm Check file, Activate framework, Discard draft (nút xác nhận), Import new version; không tải file nào; không chọn file nào. Dữ liệu trong prototype không đổi.

## 8. Những điều chưa kiểm

- Hai khung Figma `Frameworks / Import` và `Framework / Activate` đọc bằng ảnh phóng to; chữ "20 MB" ở khung Import đọc được, chữ nhỏ ở khung Draft preview đọc ở mức phóng to 2 lần.
- Chưa mở tab Requirements của framework không tier (ISO/IEC 27001 · 2022) nên chưa biết cây của loại này khác gì (dimension thay bằng clause?).
- Chưa biết hệ thống có phản hồi khác trên Excel/ONLYOFFICE; file mẫu import chỉ đọc 3 sheet đầu và sheet Validation_Rules.
- UC v4 chưa có trong `docs/source`; 7 dòng UC lấy từ tin nhắn của Hanna. Cột UC của sheet Scopes vẫn dùng mã v2.1; sheet này dùng mã v4 (`FWK-01`).

## 9. Đính chính 08/10/2026 15:50 (sau soát lỗi bản 1.7)
- Q-F-06: sheet Validation_Rules của file mẫu ver 1 có 11 dòng mức ERROR (10 kiểm + 1 kiểm "All or nothing" cho cả file; một số kiểm như "Only one framework version", "Required information" không phải kiểm một trường) và có cả WARNING, INFO. Mục 6 viết "7 case lấy từ Validation_Rules" là đúng với bản 1.6 lúc đó (Framework_072–078), nhưng 7 case ít hơn 10 kiểm ERROR nên còn thiếu; từ bản 1.7 sheet có 16 case lỗi file (số 024–039 là số của bản 1.9).
- Q-F-08: prototype không đọc nội dung file (chỉ kiểm đuôi .xlsx và tên có chữ bcm) và dữ liệu nằm ở localStorage từng trình duyệt; nên các case phụ thuộc nội dung file không kiểm được trên prototype dù có phép bấm.
- Q-F-11: nhãn icon tải đã biết ("Download source file of <tên ngắn> · <version>"); chỉ còn câu hỏi bản thật có tải file không.
- Q-F-13: thứ tự mặc định đã biết (Draft trước, rồi mã A–Z, cùng mã bản mới hơn trước); Hanna đang ghi là cũ nhất xuống mới nhất.
- Câu hỏi mới dùng ở file TC: Q-F-18 (chữ của các trạng thái không có ở Figma: không có kết quả, framework không tồn tại), Q-F-19 (đóng hộp thoại bằng ×, Esc, Cancel khi đã chọn file), Q-F-20 (phân trang: Items per page, nút chuyển trang; Figma ghi Page 1 of 1), Q-F-21 (framework không tier / một tier / tên nhóm Dimensions, Clauses, Chapters; Figma chỉ vẽ Appendix 10).
