# Cách viết TC của Hanna ở bản v1.4 — sheet Scopes, No. 1–67

- Ngày: 07/10/2026 · Nguồn góp ý: FB-047 (và FB-042 → FB-049) trong `feedback/log.md`.
- File: `exports/SGS-DTP_TestCase1_v1.4.xlsx` (Hanna gửi 07/10), so từng ô với `exports/SGS-DTP_TestCase1_v1.3.xlsx` (06/10).
- Phạm vi: dòng 13–69 của v1.4 (Điều hướng và Danh sách scope). Số TC ghi theo bản v1.5; bảng đối chiếu số cũ → số mới ở `so-sanh_v1.4-v1.5.md` mục 5.
- Mọi con số do script đếm. Phần "AI hiểu là" là cách hiểu của AI, chờ Hanna xác nhận.

## 1. Tám điểm trong cách viết

| # | Hanna làm gì | Dẫn chứng (số TC của v1.5) | Áp cho phần dưới ở v1.5 |
|---|---|---|---|
| 1 | Bỏ dạng `{{khoá}}`. Dữ liệu tester tự nhập ghi giá trị cụ thể (`Name: abc`). Dữ liệu phải có sẵn trên hệ thống mà chưa xác định thì viết chung chung, tên đặt trong ngoặc vuông | Scope_025: `Name: abc`. Scope_020: "Nhập Name trùng tên [Organization]". Scope_027: `Belongs to organisation: [Organization]`. Scope_006: `[tenant.short]`. Scope_004: "Mở url đúng định dạng" | 68 ô còn `{{…}}` ở v1.4 về 0. Bảng tên ngoặc vuông ở mục 4 |
| 2 | Nhập nhiều trường thì mỗi trường một dòng dưới bước "Nhập"; Expected có ý con thì dùng dấu `+` dưới dòng `-` | Scope_025 Step: "4. Nhập / - Name: abc / - What is in scope: abc / …". Scope_026 Expected: "- Danh sách có dòng với / + Name: abc / + Nhãn loại: Product". Scope_058: "+ 10 items / + 25 items…" | Scope_083 (Sửa), Scope_105 (Chọn), Scope_085, Scope_115 (Bảng n cột theo thứ tự), Scope_118, Scope_129 |
| 3 | Chỗ nào hiển thị khác nhau theo loại thì mỗi loại một case | Tạo scope ▸ Thành công: Organization, Product, System (Scope_025 → 027). Cột Belongs to: 1 case thành 4 (Scope_037 → 040). Dòng phụ ở màn chi tiết: 3 case (Scope_063 → 065) | Khối Overview mỗi loại một case, đủ từng dòng thông tin (Scope_071 → 073). Cột Tier tách 2 case (Scope_087, 088). Gắn framework ▸ Thành công mỗi loại framework một case (Scope_105, 106) |
| 4 | Case bấm nút gửi mà không lưu được (bỏ trống trường bắt buộc, chỉ có khoảng trắng, trùng tên, quá giới hạn) nằm chung nhóm **Không thành công** với Cancel, ×, Esc. Nhóm này đứng **trước** nhóm Thành công | Tạo scope ở v1.3: Kiểm tra dữ liệu 7 · Thành công 10 · Không thành công 3. Ở v1.4: Không thành công 10 · Thành công 3 (Scope_015 → 027) | Sửa scope: 3 case Kiểm tra dữ liệu vào Không thành công (Scope_076 → 078). Gắn framework: 2 case (Scope_101, 102). Cả sheet không còn nhóm Kiểm tra dữ liệu; nhóm Không thành công đứng trước Thành công ở Sửa scope, Gắn framework, Đổi tier, Gán người dùng |
| 5 | Nhóm Thành công chỉ kiểm ở nơi hành động trả về. Nơi hiển thị khác đã có khu vực riêng thì kiểm ở khu vực đó. Bỏ case hệ quả do suy ra | Tạo scope ▸ Thành công: 10 case còn 3, đều kiểm dòng vừa tạo ở danh sách. Đã bỏ: hiện ở màn chi tiết (3 case), hiện ở Belongs to organisation, Belongs to product, hiện ở scope cha, Out of scope để trống | Bỏ 5 case (so-sanh mục 3): tên mới ở Overview của scope con, ở cột Belongs to; framework vừa gắn ở danh sách Scopes, ở Summary; cột Users sau khi gán. Case hệ quả ở **màn khác** (Workspaces, chi tiết người dùng) giữ ở sheet Scopes theo rule 27 |
| 6 | Text nguyên văn của giao diện đặt riêng một dòng, trong ngoặc kép, sau dòng dẫn | Scope_015: "- Hiện lỗi tại Type: / "Choose the type of scope."". Scope_005, Scope_007 | Scope_076 → 078, Scope_080, Scope_096, Scope_110, Scope_118, Scope_128 |
| 7 | Giá trị tính toán có nhiều case với số cụ thể; Expected ghi phép tính và kết quả | Cột Evidence coverage: 1 case (Expected trống) thành 6 case, vd Scope_044: "(74+6+0)/(116+31+78) × 100 = 35.56% → 36%" | Cột Coverage ở khối Frameworks: 1 case thành 4 (Scope_089 → 092), cùng kiểu, kèm câu hỏi Q-S-11. Thêm 4 case biên cho Evidence coverage, Expected để trống (Scope_050 → 053) |
| 8 | Expected được điền theo hệ thống đang chạy, và **vẫn giữ** câu hỏi ở cột Open question | 8 case có Expected trống ở v1.3 được điền ở v1.4, cả 8 còn câu hỏi: Scope_005, 007, 017, 020, 024, 054, 057, 059 | **Chưa áp** (trái rule 1, 13 — xem mục 3). Ở phần dưới, chỗ chưa có căn cứ vẫn để trống Expected, điều prototype đang làm ghi ở cột Open question |

Hai việc khác thấy trong file:

- Hanna tự thêm dấu nháy đơn đầu ô cho 36 ô Expected đã sửa (để ô bắt đầu bằng `-` không bị hiểu là công thức) → v1.5 làm cho cả 216 ô của 4 sheet TC (FB-049).
- Hanna tự đánh lại TVP_ID cho liền mạch sau khi thêm, bớt dòng (từ dòng 50 trở xuống số tăng 1 đến 2 so với v1.3) → v1.5 đánh lại cả No. và TVP_ID, có bảng đối chiếu.

## 2. Dẫn chứng trước → sau (v1.3 → v1.4)

| TC (v1.5) | Cột | v1.3 | v1.4 (Hanna) |
|---|---|---|---|
| Scope_003 | Expected | - Chuyển sang màn chi tiết, URL dạng {{url.app}}/scopes/&lt;mã scope&gt;<br>- Tiêu đề trang là tên {{scope.org}} | - Chuyển sang màn chi tiết, đúng dạng URL<br>- Tiêu đề trang đúng định dạng |
| Scope_004 | Step | 1. Mở {{url.app}}/scopes/&lt;mã của {{scope.org}}&gt; | 1. Mở url đúng định dạng |
| Scope_005 | Expected | (trống) | - Hiển thị lỗi:<br>"This scope doesn’t exist<br>It may have been removed, or it belongs to an organisation you can’t see." |
| Scope_006 | Expected | … The parts of {{tenant.short}} you prepare … | … The parts of [tenant.short] you prepare … |
| Scope_015 | III · Expected | Kiểm tra dữ liệu · "- Hiện lỗi tại Type" | Không thành công · "- Hiện lỗi tại Type:<br>"Choose the type of scope."" |
| Scope_019 | cả dòng | case "System chưa chọn Belongs to organisation" | thay bằng case "What is in scope chỉ có khoảng trắng" |
| Scope_020 | Step · Expected | Nhập Name trùng tên {{scope.org}} · (trống) | Nhập Name trùng tên [Organization] · "A scope with this name already exists." |
| Scope_025 | Step | 4. Nhập Name: abc; What is in scope: abc; What is out of scope (optional): abc | 4. Nhập<br>- Name: abc<br>- What is in scope: abc<br>- What is out of scope (optional): abc |
| Scope_027 | Step | Name: sys-abc … Chọn Belongs to organisation {{scope.org}}, Belongs to product {{scope.prd}} | Name: abc … 5. Chọn<br>- Belongs to organisation: [Organisation]<br>- Belongs to product (optional): [Production] |
| Scope_037 → 040 | số case | 1 case "Kiểm tra cột Belongs to" | 4 case: Organization, Product, System có chọn, System bỏ trống cả hai |
| Scope_040 | Expected | (chưa có case) | System bỏ trống Belongs to organisation và Belongs to product: "- Hiển thị Belongs to: —" |
| Scope_044 → 049 | số case | 1 case, Expected trống, câu hỏi Q-S-11 | 6 case có số cụ thể và phép tính |
| Scope_054 | Expected | (trống) | - Hiển thị theo thứ tự thời gian cũ nhất xuống mới nhất |
| Scope_058 | cả dòng | (chưa có) | case mới: các giá trị của Items per page: 10, 25, 50, 100 items |

Ghi nhận từ Scope_040: Hanna đã xác định tạo được scope System khi bỏ trống Belongs to organisation. Phần 1 của câu Q-S-04 (trường này có bắt buộc không) coi như có câu trả lời theo hệ thống đang chạy; chờ SGS xác nhận.

## 3. Chỗ cách viết này khác rule đang có — cần Hanna chọn

| # | Rule đang ghi | Bản v1.4 làm | v1.5 đang theo | Cần Hanna chọn |
|---|---|---|---|---|
| 1 | `rules/tc-authoring.md` rule 8: "Thành công hết rồi mới tới Không thành công" | Không thành công đứng trước Thành công (Tạo scope) | Theo v1.4, cả sheet | Thứ tự nào là chuẩn? Đổi lại chỉ là xếp lại dòng |
| 2 | Rule 1, rule 13, `common.md` rule 9: không lấy hành vi của prototype làm Expected; chưa có căn cứ thì để trống và ghi câu hỏi | 8 case điền Expected theo hệ thống đang chạy, giữ câu hỏi | Phần Hanna sửa: giữ nguyên. Phần dưới: theo rule | Có cho phép "Expected tạm theo hệ thống đang chạy, kèm câu hỏi" không? Nếu có, AI điền tiếp phần dưới theo prototype |
| 3 | Quyết định 05/10 trong `profile.md` (FB-037 bị bác): giá trị tính toán không ghi cách tính trong TC | 6 case Evidence coverage ghi phép tính; 5 case không kèm câu hỏi | Giữ của Hanna; 4 case Coverage ở khối Frameworks viết cùng kiểu, kèm câu hỏi Q-S-11 | A: theo v1.4 (ghi phép tính, kèm câu hỏi cho tới khi SGS xác nhận công thức). B: giữ quyết định 05/10 (để trống tới khi có công thức) |
| 4 | `profile.md`, FB-031: file TC viết tiếng Anh | Sheet Scopes viết tiếng Việt; riêng 6 tên case Evidence coverage viết tiếng Anh | Giữ tiếng Việt; case AI thêm viết tiếng Việt | File TC SGS DTP viết tiếng nào? |
| 5 | Rule 9, rule 30, pattern P7: hành động hiện ở n nơi thì n case; mỗi loại một TC, mỗi nơi hiển thị một TC | Mỗi loại một case, kiểm ở nơi hành động trả về; nơi khác kiểm ở khu vực của nó | Cùng sheet: theo v1.4. Màn khác: giữ theo rule 27 | Case hệ quả ở màn khác (Workspaces, chi tiết người dùng) để ở sheet Scopes hay chuyển sang sheet của màn đó? |
| 6 | Rule 11: TVP_ID theo mẫu `TC_nnn`, ID đã bỏ không dùng lại | Sheet Scopes dùng `Scope_nnn`; Hanna đánh lại số cho liền mạch | Đánh lại liền mạch `Scope_001` → `Scope_137`, có bảng đối chiếu | Khi chưa có kết quả chạy thì được đánh lại số — đúng ý Hanna không? |
| 7 | Rule 14: dòng đăng nhập ghi "Đăng nhập với acc &lt;vai trò&gt;" | "Đăng nhập account Customer Admin" | Theo file | Không cần chọn nếu Hanna thấy hai cách như nhau; khi đó sửa câu mẫu trong rule theo file |

## 4. Tên trong ngoặc vuông đang dùng ở sheet Scopes

| Tên | Nghĩa | Ai đặt |
|---|---|---|
| `[Organization]`, `[Product]`, `[System]` | Tên một scope có sẵn thuộc loại đó | Hanna (tin nhắn 07/10) |
| `[Tên Organization]` | Tên khách hàng hiển thị ở dòng phụ màn chi tiết (trước là `{{tenant.name}}`) | Hanna |
| `[tenant.short]` | Tên ngắn của khách hàng ở mô tả trang (trước là `{{tenant.short}}`) | Hanna |
| `[từ khóa]` | Chuỗi nhập vào ô tìm kiếm | AI, theo Scope_034 của Hanna ("Nhập từ khóa") |
| `[What is in scope]`, `[What is out of scope]` | Nội dung đã lưu ở hai trường đó của scope đang xem | AI |
| `[Framework]` | Tên một framework | AI |
| `[Customer User]` | Tên một người dùng vai trò Customer User | AI |
| `[Tên scope]` | Tên của scope đang xem | AI |
| `[Mã audit]` | Mã của audit đang chạy | AI |

Trong sheet còn dạng `<…>` ở các ô mô tả khuôn hiển thị, vd `<tên framework> · <phiên bản>`, `<n> scopes`; Hanna giữ dạng này ở Scope_028, Scope_041, Scope_061 nên phần dưới cũng giữ.

## 5. Cách nhận ra ô Hanna đã gõ lại

57 ô ở sheet Scopes có chữ tiếng Việt ở dạng tổ hợp (dấu thanh là ký tự riêng, vd `a` + dấu huyền), khác dạng dựng sẵn của phần còn lại: 51 ô ở dòng 13–69 và 6 ô ở phần dưới (dòng 71–73, 79, 86, 87). Đây là dấu vết của bộ gõ, mắt thường không thấy khác. Hệ quả đã gặp: `tc_check.py` báo khu vực Tạo scope "có nhóm Thành công nhưng thiếu Không thành công", vì chữ "Không thành công" Hanna gõ khác mã với chữ script tìm. Bản v1.5 lưu mọi chuỗi ở dạng dựng sẵn (NFC); đề xuất sửa `tc_check.py` để tự chuẩn hoá trước khi so (tài liệu cập nhật 07/10).

53 ô Hanna tô nền vàng ở phần dưới (cột Pre-condition, Step, Expected của dòng 79, 80, 86–89, 113–120, 126–146) AI hiểu là chỗ cần sửa. Ở v1.5: 37 ô đã đổi chữ, 11 ô mất cùng case bị bỏ, 5 ô giữ nguyên chữ vì AI không thấy gì cần đổi (Step của Scope_072; Pre-condition "Đăng nhập account Customer Admin" của Scope_120, 121, 124, 126). Nền vàng đã bỏ ở cả 53 ô. Nếu 5 ô đó Hanna tô vì lý do khác thì báo AI.
