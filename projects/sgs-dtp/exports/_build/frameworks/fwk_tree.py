# -*- coding: utf-8 -*-
"""Cây case cha của sheet Frameworks (module 04). Đếm số case IV bằng code, không đếm tay.

Trạng thái mỗi nhóm III:
  V   viết được: Figma và hệ thống khớp nhau (hoặc chỉ cần một nguồn đã kiểm)
  VQ  viết được phần thao tác; Expected (một phần hoặc toàn bộ) để trống kèm câu hỏi Q-F
  C   chờ: chưa có thiết kế ở Figma và hệ thống, hoặc thiếu dữ liệu để chạy; chưa viết case
"""

# (I, II, III, [case IV...], UC, trạng thái, căn cứ, câu hỏi)
P = []


def add(i, ii, iii, items, uc, st, src, q=""):
    P.append(dict(I=i, II=ii, III=iii, items=items, uc=uc, st=st, src=src, q=q))


R1 = "Điều hướng - Redirect"
add(R1, "Vào danh sách - Framework list", "Từ menu",
    ["Bấm Frameworks ở menu trái"], "FWK-01", "V", "HT /ops/frameworks")
add(R1, "Vào chi tiết - Framework detail", "Từ danh sách",
    ["Bấm tên framework Active (mở tab Overview)", "Bấm tên framework Draft (mở màn Draft preview)"],
    "FWK-02", "V", "HT; Figma Detail, Draft preview")
add(R1, "Quay lại - Back", "Từ chi tiết",
    ["Bấm nút mũi tên quay lại ở chi tiết framework Active", "Bấm nút mũi tên quay lại ở Draft preview"],
    "FWK-02", "V", "HT")

L = "Danh sách framework - Framework list"
add(L, "Tiêu đề trang - Page header", "Hiển thị",
    ["Breadcrumb, tiêu đề và dòng mô tả", "Nút Download template", "Nút Import framework"],
    "FWK-01, FWK-03", "V", "Figma List; HT")
add(L, "Thanh công cụ - Toolbar", "Hiển thị",
    ["Dòng đếm \"<n> frameworks\"", "Ô tìm kiếm và chữ gợi ý"], "FWK-01", "V", "Figma List; HT")
add(L, "Thanh công cụ - Toolbar", "Tìm kiếm",
    ["Tìm theo mã (code)", "Tìm theo tên (name)", "Không có kết quả", "Xoá chữ tìm, danh sách trở lại đủ dòng"],
    "FWK-01", "VQ", "Figma List (\"Search code or name\"); HT (\"No results for\")",
    "Q-F-12 (kết quả tìm theo mã, theo tên: chưa kiểm trên hệ thống)")
add(L, "Bảng danh sách - Table", "Hiển thị cột",
    ["Tiêu đề cột và thứ tự: Framework, Version, Issued by, Tiers, Requirements, Status, Updated"],
    "FWK-01", "V", "Figma List; HT")
add(L, "Bảng danh sách - Table", "Hiển thị dòng theo loại",
    ["Framework Active có tier", "Framework Active không tier (cột Tiers hiện \"—\")",
     "Framework Draft (chip \"Draft · not active\", Updated dạng \"Today, hh:mm\")",
     "Hai phiên bản của cùng một mã hiện thành hai dòng"],
    "FWK-01", "V", "Figma List; HT")
add(L, "Bảng danh sách - Table", "Sắp xếp",
    ["Sắp xếp cột Framework", "Sắp xếp cột Version", "Sắp xếp cột Issued by", "Sắp xếp cột Requirements"],
    "FWK-01", "VQ", "HT (có mũi tên sắp xếp ở 4 cột); Figma List chưa vẽ",
    "Q-F-13 (thứ tự mặc định và kết quả sắp xếp chưa kiểm)")
add(L, "Bảng danh sách - Table", "Cột UC nêu mà màn chưa có",
    ["Cột Content level (Full / Identity only)", "Cột affiliates của framework Bulk", "Trạng thái Withdrawn"],
    "FWK-01", "C", "Chỉ có ở UC; Figma List và HT không có", "Q-F-01, Q-F-02")
add(L, "Bảng danh sách - Table", "Biểu tượng tải ở mỗi dòng",
    ["Bấm biểu tượng tải ở một dòng"], "[NGOÀI UC]", "VQ", "Figma List; HT (không kiểm tải thật)", "Q-F-11")
add(L, "Phân trang - Pagination", "Hiển thị",
    ["Dòng \"1–<n> of <n> items\" và \"1 of 1 page\"", "Chọn Items per page: 10, 25, 50, 100"],
    "FWK-01", "V", "HT; Figma List")
add(L, "Phân trang - Pagination", "Nhiều trang",
    ["Chuyển sang trang 2 khi có hơn 10 framework"], "FWK-01", "C",
    "Cần dữ liệu từ 11 framework trở lên; hệ thống hiện có 8", "")

D = "Chi tiết framework - Framework detail"
add(D, "Phần đầu - Header", "Hiển thị",
    ["Framework Active: tên, chip Active, dòng \"code · version · issuing body\", nút quay lại, nút ba chấm",
     "Framework Draft: chip \"Draft · not active\", nút Discard draft và Activate (không có nút ba chấm)"],
    "FWK-02", "V", "Figma Detail, Draft preview; HT")
add(D, "Menu ba chấm - More menu", "Mở menu",
    ["Mở menu ở framework Active, chỉ có mục \"Import new version\""], "FWK-02, FWK-03", "VQ",
    "HT; Figma Detail vẽ nút, chưa vẽ nội dung menu", "Q-F-05 (mục này mở hộp thoại nào chưa kiểm)")
add(D, "Điều hướng trong màn - In-page tabs", "Chuyển tab",
    ["Framework Active có 3 mục: Overview, Requirements, Other versions; mặc định Overview",
     "Framework Draft có 3 mục: Framework, Tiers, Requirements"], "FWK-02", "V", "Figma; HT")
add(D, "Điều hướng trong màn - In-page tabs", "Tab UC nêu mà màn chưa có",
    ["Tab Bulk settings (CFG-01 đến CFG-03)", "Tab History"], "FWK-02", "C",
    "Chỉ có ở UC; Figma và HT không có", "Q-F-03")
add(D, "Tổng quan - Overview", "Hiển thị khối Framework",
    ["Framework Active: Code, Issued by, Version, Effective date, Description"], "FWK-02", "V", "Figma Detail; HT")
add(D, "Tổng quan - Overview", "Hiển thị khối Tiers",
    ["Framework có tier: bảng Code, Tier, Rank, New at this tier, Total to meet",
     "Framework không tier: không có khối Tiers"], "FWK-02", "V", "HT (ISO/IEC 27001 · 2022); Figma Detail")
add(D, "Tổng quan - Overview", "Giá trị tính toán: Total to meet",
    ["Tier Basic: New at this tier 44, Total to meet 44", "Tier Medium: New 17, Total 61",
     "Tier High: New 15, Total 76"], "FWK-02", "VQ",
    "HT (Appendix 10 · 2022). Figma Detail ghi High là 18 và 79, lệch với 76 ở khối Content",
    "Q-F-10, chờ chọn A hoặc B ở FB-048")
add(D, "Tổng quan - Overview", "Hiển thị khối Content theo loại",
    ["Framework có tier: Dimensions, Control measures, Requirements, Expected evidence items",
     "Framework không tier: Clauses, Requirements, Expected evidence items"], "FWK-02", "V",
    "HT (Appendix 10 · 2022 và ISO/IEC 27001 · 2022); Figma Detail (loại có tier)")
add(D, "Yêu cầu - Requirements", "Hiển thị",
    ["Tiêu đề và dòng tóm tắt \"… Read only — import a new version to change them.\"",
     "Cây: dimension kèm số, mở ra thấy requirement kèm chip Basic, From Medium, From High",
     "Chọn một requirement: khung bên phải hiện code, tiêu đề, mô tả, Applies to, Not required for, Sort order, Source, Expected evidence"],
    "FWK-02", "V", "Figma Requirements; HT")
add(D, "Yêu cầu - Requirements", "Chỉ đọc",
    ["Không có nút thêm, sửa hoặc retire requirement"], "FWK-02", "V", "Figma Requirements; HT; ghi chú của UC")
add(D, "Yêu cầu - Requirements", "Tìm kiếm",
    ["Tìm theo mã requirement", "Tìm theo tiêu đề", "Không có kết quả"], "FWK-02", "VQ",
    "Figma, HT có ô \"Search requirements\"; kết quả chưa kiểm", "Q-F-12")
add(D, "Yêu cầu - Requirements", "Lọc theo tier",
    ["Chọn Basic", "Chọn Medium", "Chọn High", "Chọn All tiers"], "FWK-02", "VQ",
    "HT (4 lựa chọn: All tiers, Basic, Medium, High); kết quả lọc chưa kiểm", "Q-F-12")
add(D, "Yêu cầu - Requirements", "Giá trị tính toán: số đếm theo dimension",
    ["Cộng số của 7 dimension bằng số Requirements (76)", "Cùng kiểm với framework có 79 requirement (bản Draft)"],
    "FWK-02", "VQ", "HT: 14+14+7+11+14+7+9 = 76 và 14+14+8+11+15+7+10 = 79", "Chờ chọn A hoặc B ở FB-048")
add(D, "Yêu cầu - Requirements", "Trạng thái requirement",
    ["Hiển thị trạng thái của requirement (UC nêu \"status\")"], "FWK-02", "C",
    "Chỉ thấy chip tier; ô lọc tên \"Filter by status\" nhưng chữ hiện \"All tiers\"", "Q-F-09")
add(D, "Phiên bản khác - Other versions", "Hiển thị",
    ["Bảng Version, Status, Imported by, Activated"], "[NGOÀI UC]", "C",
    "HT ghi \"No design yet\"; Figma không có khung", "Q-F-03")

I = "Nhập framework - Import framework"
add(I, "Hộp thoại Import - Import dialog", "Mở hộp thoại",
    ["Mở từ nút Import framework ở danh sách", "Mở từ mục \"Import new version\" ở chi tiết framework Active"],
    "FWK-03", "VQ", "Figma Import; HT (mới mở từ danh sách)", "Q-F-05")
add(I, "Hộp thoại Import - Import dialog", "Hiển thị nội dung",
    ["Tiêu đề, bước 1 \"Download the template and fill it in\", bước 2 \"Upload the completed file\"",
     "Vùng kéo thả và dòng \"Excel (.xlsx) · up to 20 MB · checked before anything is saved\"",
     "Nút Cancel và Check file khi chưa chọn file"], "FWK-03", "VQ", "Figma Import; HT",
    "Q-F-14 (trạng thái nút Check file khi chưa chọn file)")
add(I, "Hộp thoại Import - Import dialog", "Tải file mẫu",
    ["Bấm Download template (.xlsx) trong hộp thoại", "Bấm Download template ở đầu danh sách"],
    "[NGOÀI UC]", "VQ", "Figma Import, List; HT (không tải thật)", "Q-F-11")
add(I, "Chọn file - File picker", "Hiển thị",
    ["Chọn file .xlsx hợp lệ: thẻ file có tên, dung lượng, dấu tích, nút ×", "Bấm × để bỏ file đã chọn"],
    "FWK-03", "V", "Figma Import")
add(I, "Chọn file - File picker", "Không thành công",
    ["Chọn file không phải .xlsx", "Chọn file lớn hơn 20 MB"], "FWK-03", "VQ",
    "Giới hạn có ở Figma Import; thông báo lỗi chưa có", "Q-F-14")
add(I, "Kiểm tra file - Check file", "Không thành công",
    ["Mã cha không tồn tại (parent_requirement_code)", "Mã requirement bị trùng (requirement_code)",
     "Expected evidence trỏ vào dòng nhóm (is_assessable = FALSE)", "Banner \"<n> errors in <tên file>\" và dòng \"Nothing was imported\"",
     "Tải file đã sửa ở ô \"Corrected file\" rồi Check file", "Bấm Cancel khi đang có lỗi",
     "Bấm × khi đang có lỗi", "Bấm Esc khi đang có lỗi",
     "Hai dòng ở sheet Framework", "Thiếu framework_code, framework_name hoặc version",
     "Requirement tự là cha của chính nó", "Cha con tạo vòng lặp", "is_assessable không phải TRUE hoặc FALSE",
     "Mã expected evidence bị trùng", "mandatory không phải TRUE hoặc FALSE"],
    "FWK-03", "VQ", "Figma Import errors (3 lỗi đầu có chữ nguyên văn); 7 lỗi sau theo sheet Validation_Rules của file mẫu ver 1",
    "Q-F-06, Q-F-14 (chữ báo lỗi của 7 lỗi sau chưa có)")
add(I, "Kiểm tra file - Check file", "Không thành công theo UC mà Figma chưa có",
    ["content_version không tăng khi cập nhật", "Dùng lại mã requirement đã retire"], "FWK-03", "C",
    "Chỉ có ở UC", "Q-F-04")
add(I, "Kiểm tra file - Check file", "Thành công",
    ["Import file hợp lệ của framework mới (mã chưa có)",
     "Import file hợp lệ là phiên bản mới của mã đã có (Version khác)"],
    "FWK-03", "VQ", "Figma Draft preview, Import (câu \"added as its own entry\"); chưa bấm Check file trên hệ thống",
    "Q-F-04, Q-F-08")
add(I, "Kiểm tra file - Check file", "Thành công theo UC mà Figma chưa có",
    ["Bảng tóm tắt thay đổi added, updated, retired", "Cảnh báo WARNING và INFO", "Import vào framework identity-only"],
    "FWK-03", "C", "Chỉ có ở UC", "Q-F-04, Q-F-06")

B = "Bản nháp - Draft preview"
add(B, "Phần đầu - Header", "Hiển thị",
    ["Tên, chip \"Draft · not active\", dòng \"code · version · issuing body\"", "Nút Discard draft và Activate"],
    "FWK-03, FWK-06", "V", "Figma Draft preview; HT")
add(B, "Nội dung bản nháp - Draft content", "Hiển thị",
    ["Khối Framework: Code, Issued by, Version, Effective date \"Not set\", Description",
     "Khối Tiers: Basic 44/44, Medium 17/61, High 18/79",
     "Khối Requirements: \"7 dimensions · 27 control measures · 79 requirements · 79 expected evidence items\""],
    "FWK-02, FWK-03", "V", "Figma Draft preview; HT (/ops/frameworks/fw-a10-amended)")
add(B, "Khung Import bên phải - Import panel", "Hiển thị",
    ["\"File check passed\" và dòng \"No errors. The draft is ready to activate.\"",
     "Khung \"After activation\""], "FWK-03, FWK-06", "VQ",
    "Figma và HT; câu về ai chọn tier khác nhau", "Q-F-07")
add(B, "Huỷ bản nháp - Discard draft", "Mở hộp thoại",
    ["Bấm Discard draft: hộp thoại \"Discard draft?\" kèm câu \"Customers never saw it. You can import the file again later.\""],
    "[NGOÀI UC]", "V", "HT; Figma chưa vẽ hộp thoại", "Q-F-11")
add(B, "Huỷ bản nháp - Discard draft", "Không thành công",
    ["Bấm Cancel", "Bấm ×", "Bấm Esc"], "[NGOÀI UC]", "VQ", "HT (Cancel, ×); kết quả chưa kiểm", "Q-F-11")
add(B, "Huỷ bản nháp - Discard draft", "Thành công",
    ["Bấm Discard draft trong hộp thoại"], "[NGOÀI UC]", "VQ", "HT (chưa bấm xác nhận)", "Q-F-08, Q-F-11")

A = "Kích hoạt framework - Activate framework"
add(A, "Hộp thoại Activate - Activate dialog", "Mở hộp thoại",
    ["Bấm Activate ở Draft preview: tiêu đề, câu hỏi \"Activate <tên> · <version>?\", ba gạch đầu dòng"],
    "FWK-06", "VQ", "Figma Activate; HT. Gạch thứ hai khác nhau giữa hai nguồn", "Q-F-07")
add(A, "Hộp thoại Activate - Activate dialog", "Không thành công",
    ["Bấm Cancel", "Bấm ×", "Bấm Esc", "Kích hoạt khi chưa có Active retention policy (CFG-01)"],
    "FWK-06", "VQ", "Cancel và × có ở Figma, HT; trường hợp retention policy: Settings ghi \"No design yet\"",
    "Q-F-07")
add(A, "Hộp thoại Activate - Activate dialog", "Thành công",
    ["Kích hoạt framework có tier", "Kích hoạt framework không tier"], "FWK-06", "VQ",
    "Figma Activate; chưa bấm xác nhận trên HT. Chưa có bản nháp không tier để kích hoạt",
    "Q-F-08")
add(A, "Hiển thị với khách hàng - Customer view", "Sau khi kích hoạt",
    ["Customer Admin mở hộp thoại Link a framework: framework vừa kích hoạt có trong danh sách chọn",
     "Framework Draft chưa kích hoạt không có trong danh sách chọn"], "FWK-06", "VQ",
    "HT: danh sách chọn có 6 mục gộp theo mã, không thấy chọn phiên bản; theo rule 27 đặt ở sheet của hành động",
    "Q-F-08")

W = "Rút framework - Withdraw framework"
add(W, "Rút khỏi sử dụng mới", "Chờ thiết kế", ["(chưa viết case)"], "FWK-07", "C",
    "Không có nút, hộp thoại hay trạng thái Withdrawn ở Figma và hệ thống", "Q-F-02, Q-F-15")
Cr = "Tạo framework - Create framework"
add(Cr, "Tạo framework chỉ có định danh", "Chờ thiết kế", ["(chưa viết case)"], "FWK-04", "C",
    "Không có nút hay form ở Figma và hệ thống", "Q-F-15")
Ed = "Sửa thông tin framework - Edit framework"
add(Ed, "Sửa metadata", "Chờ thiết kế", ["(chưa viết case)"], "FWK-05", "C",
    "Không có nút hay form ở Figma và hệ thống; menu ba chấm chỉ có Import new version", "Q-F-15")

PM = "Phân quyền - Permission"
add(PM, "SGS Admin", "Quyền theo vai trò",
    ["Thấy menu Frameworks, nút Download template và Import framework ở danh sách",
     "Thấy Discard draft và Activate ở Draft preview", "Thấy nút ba chấm ở framework Active"],
    "FWK-01 đến FWK-06", "V", "HT (Minh Nguyen · SGS Admin)")
add(PM, "SGS User", "Quyền theo vai trò",
    ["Thấy menu Frameworks và danh sách, không có nút Download template và Import framework",
     "Mở Draft preview, không có nút Discard draft và Activate"], "FWK-01, FWK-02", "VQ",
    "HT (Grace Lin · SGS User); UC chỉ nêu SGS Admin", "Q-F-16")
add(PM, "SGS Consultant", "Quyền theo vai trò",
    ["Thấy menu Frameworks và danh sách, không có nút Download template và Import framework"],
    "FWK-01", "VQ", "HT (Anna Lee · SGS Consultant); chưa mở chi tiết", "Q-F-16")
add(PM, "SGS Auditor/Certification", "Quyền theo vai trò",
    ["Menu không có Frameworks", "Mở thẳng địa chỉ của danh sách"], "FWK-01", "VQ",
    "HT (David Wu); menu đã kiểm, vào bằng địa chỉ chưa kiểm", "Q-F-16")
add(PM, "Vai trò Customer", "Quyền theo vai trò",
    ["Customer Admin: menu không có Frameworks", "Customer User: menu không có Frameworks",
     "Customer Viewer: menu không có Frameworks", "Customer Admin mở thẳng địa chỉ của danh sách"],
    "FWK-01", "VQ", "HT (Linh Tran · Customer Admin đã kiểm menu; User, Viewer chưa kiểm)", "Q-F-16")

S = "Bảo mật - Security"
add(S, "Dữ liệu trong file import - Imported data", "Hiển thị nguyên văn",
    ["Ô bắt đầu bằng dấu = trong file hiện nguyên văn trên bản nháp",
     "Thẻ <script> trong Description hiện nguyên văn trên bản nháp"], "FWK-03", "VQ",
    "Chưa kiểm trên hệ thống", "Q-F-14")
add(S, "Ghi vết - Audit log", "Hành động được ghi",
    ["Import ghi một dòng ở Audit Logs", "Kích hoạt ghi một dòng ở Audit Logs", "Huỷ bản nháp ghi một dòng ở Audit Logs"],
    "FWK-03, FWK-06", "VQ", "Menu Audit Logs có ở SGS Admin; nội dung dòng ghi vết chưa kiểm", "Q-F-17")


def summary():
    from collections import OrderedDict
    by = OrderedDict()
    for p in P:
        by.setdefault(p["I"], []).append(p)
    return by


if __name__ == "__main__":
    by = summary()
    tot = {"V": 0, "VQ": 0, "C": 0}
    for p in P:
        tot[p["st"]] += len(p["items"])
    print("nhóm III:", len(P), "| case IV theo trạng thái:", tot, "| tổng:", sum(tot.values()))
    for i, ps in by.items():
        n = sum(len(p["items"]) for p in ps)
        print(f"{i}: {len(ps)} nhóm III, {n} case IV, II={len(set(p['II'] for p in ps))}")
