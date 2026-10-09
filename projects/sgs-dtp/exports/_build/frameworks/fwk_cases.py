# -*- coding: utf-8 -*-
"""Nội dung 118 case IV (V + VQ) của sheet Frameworks. Thứ tự đúng thứ tự non-C trong fwk_tree.P.
Mỗi case: (Pri, Name, Step, Expected, Open question, UC hoặc None = lấy UC đầu của nhóm, Pre bổ sung)
Expected để trống '' khi chưa có căn cứ (rule 13)."""
H, M, L = "High", "Medium", "Low"
DR = "Có sẵn một framework Draft: [Framework Draft]"
AC = "Có sẵn một framework Active: [Framework Active]"
ACT = "Có sẵn một framework Active có tier: [Framework Active có tier]"
ACN = "Có sẵn một framework Active không tier: [Framework Active không tier]"
LIST = "1. Mở màn Frameworks"
C = []
def c(pri, name, step, exp, wait="", uc=None, pre=""):
    C.append((pri, name, step, exp, wait, uc, pre))

# --- Điều hướng ---
c(H, "Kiểm tra vào màn Frameworks từ menu trái", "1. Bấm mục Frameworks ở menu trái",
  "- Chuyển sang màn Frameworks\n- Breadcrumb: Frameworks\n- Mục Frameworks ở menu trái được tô nền")
c(H, "Kiểm tra mở chi tiết framework Active từ danh sách", LIST + "\n2. Bấm tên một framework Active",
  "- Chuyển sang màn chi tiết framework, mở tab Overview\n- Hiển thị chip Active cạnh tên framework", pre=AC)
c(H, "Kiểm tra mở màn Draft preview từ danh sách", LIST + "\n2. Bấm tên một framework Draft",
  "- Chuyển sang màn Draft preview\n- Hiển thị chip Draft · not active cạnh tên framework", pre=DR)
c(M, "Kiểm tra nút quay lại ở chi tiết framework Active", LIST + "\n2. Bấm tên một framework Active\n3. Bấm nút mũi tên quay lại",
  "- Quay về màn Frameworks", pre=AC)
c(M, "Kiểm tra nút quay lại ở Draft preview", LIST + "\n2. Bấm tên một framework Draft\n3. Bấm nút mũi tên quay lại",
  "- Quay về màn Frameworks", pre=DR)

# --- Danh sách ---
c(H, "Kiểm tra breadcrumb, tiêu đề và dòng mô tả của màn Frameworks", LIST + "\n2. Kiểm tra phần đầu trang",
  "- Breadcrumb: Frameworks\n- Tiêu đề: Frameworks\n- Dòng mô tả: Frameworks customers can activate on their scopes. Import one from the Excel template.")
c(M, "Kiểm tra nút Download template ở đầu danh sách", LIST + "\n2. Kiểm tra phần đầu trang, bên phải",
  "- Có nút Download template (không nền)", uc="[NGOÀI UC] Tải file mẫu: UC FWK-03 chỉ nêu file XLSX, không nêu nút tải mẫu")
c(H, "Kiểm tra nút Import framework", LIST + "\n2. Kiểm tra phần đầu trang, bên phải",
  "- Có nút Import framework (nền màu chính)", uc="FWK-03")
c(M, "Kiểm tra dòng đếm số framework", LIST + "\n2. Kiểm tra dòng phía trên bảng, bên trái",
  "- Hiển thị <n> frameworks, n bằng tổng số framework trong bảng")
c(L, "Kiểm tra ô tìm kiếm", LIST + "\n2. Kiểm tra phía trên bảng, bên phải",
  "- Ô tìm kiếm có icon kính lúp, placeholder: Search code or name")
c(H, "Kiểm tra tìm theo mã framework", LIST + "\n2. Nhập [mã framework] vào ô tìm kiếm", "",
  "Q-F-12: kết quả tìm theo mã chưa kiểm trên hệ thống; chưa rõ có tìm theo Version hay Issued by không")
c(H, "Kiểm tra tìm theo tên framework", LIST + "\n2. Nhập [một phần tên framework] vào ô tìm kiếm", "",
  "Q-F-12: kết quả tìm theo tên chưa kiểm")
c(M, "Kiểm tra tìm không có kết quả", LIST + "\n2. Nhập zzz vào ô tìm kiếm",
  "- Bảng không có dòng nào\n- Hiển thị \"No results for “zzz”\"\n- Hiển thị \"Try a different search term.\"",
  "Q-F-12: dòng đếm \"<n> frameworks\" có đổi theo kết quả không (prototype giữ nguyên tổng)")
c(M, "Kiểm tra xoá chữ tìm", LIST + "\n2. Nhập zzz vào ô tìm kiếm\n3. Xoá chữ trong ô tìm kiếm", "",
  "Q-F-12: chưa kiểm trên hệ thống")
c(H, "Kiểm tra tiêu đề cột của bảng", LIST + "\n2. Kiểm tra hàng tiêu đề của bảng",
  "- Các cột theo thứ tự: Framework, Version, Issued by, Tiers, Requirements, Status, Updated\n- Cột cuối là cột icon tải, không có tiêu đề")
c(H, "Kiểm tra dòng framework Active có tier", LIST + "\n2. Kiểm tra dòng của framework Active có tier",
  "- Framework: tên và mã (code)\n- Version, Issued by, Requirements có giá trị\n- Tiers: hiển thị các tier của framework\n- Status: chip Active\n- Updated: ngày cập nhật", pre=ACT)
c(H, "Kiểm tra dòng framework Active không tier", LIST + "\n2. Kiểm tra dòng của framework Active không tier",
  "- Cột Tiers hiển thị —\n- Status: chip Active", pre=ACN)
c(H, "Kiểm tra dòng framework Draft", LIST + "\n2. Kiểm tra dòng của framework Draft",
  "- Status: chip Draft · not active\n- Updated: dạng Today, hh:mm", pre=DR)
c(M, "Kiểm tra hai phiên bản của cùng một mã", LIST + "\n2. Kiểm tra các dòng có cùng mã framework, khác Version",
  "- Mỗi phiên bản một dòng riêng, cột Version khác nhau",
  pre="Có hai phiên bản của cùng một mã: [Framework hai phiên bản]")
for col in ("Framework", "Version", "Issued by", "Requirements"):
    c(M, f"Kiểm tra sắp xếp theo cột {col}", LIST + f"\n2. Bấm tiêu đề cột {col}\n3. Bấm tiêu đề cột {col} lần nữa", "",
      "Q-F-13: thứ tự mặc định và kết quả sắp xếp chưa kiểm; Figma List chưa vẽ mũi tên sắp xếp")
c(L, "Kiểm tra biểu tượng tải ở một dòng", LIST + "\n2. Bấm icon tải ở cuối một dòng", "",
  "Q-F-11: icon tải ở mỗi dòng không có trong UC; chưa rõ tải file gì", uc="[NGOÀI UC] Icon tải ở mỗi dòng: UC FWK-01 không nêu")
c(M, "Kiểm tra dòng phân trang", LIST + "\n2. Kiểm tra phần dưới bảng",
  "- Hiển thị 1–<n> of <n> items\n- Hiển thị Page 1 of 1 khi chỉ có một trang")
c(L, "Kiểm tra chọn Items per page", LIST + "\n2. Bấm ô Items per page\n3. Kiểm tra các lựa chọn",
  "- Có 4 lựa chọn: 10, 25, 50, 100")

# --- Chi tiết ---
c(H, "Kiểm tra phần đầu chi tiết framework Active", LIST + "\n2. Bấm tên một framework Active\n3. Kiểm tra phần đầu trang",
  "- Nút mũi tên quay lại\n- Tên framework, chip Active\n- Dòng \"mã · version · issuing body\"\n- Nút ba chấm", pre=AC)
c(H, "Kiểm tra phần đầu Draft preview", LIST + "\n2. Bấm tên một framework Draft\n3. Kiểm tra phần đầu trang",
  "- Tên framework, chip Draft · not active\n- Dòng \"mã · version · issuing body\"\n- Nút Discard draft và nút Activate\n- Không có nút ba chấm", pre=DR, uc="FWK-06")
c(M, "Kiểm tra menu ba chấm của framework Active", LIST + "\n2. Bấm tên một framework Active\n3. Bấm nút ba chấm",
  "- Menu có một mục: Import new version", "Q-F-05: mục Import new version mở hộp thoại nào chưa kiểm", uc="FWK-03", pre=AC)
c(H, "Kiểm tra các mục của framework Active", LIST + "\n2. Bấm tên một framework Active\n3. Kiểm tra thanh mục",
  "- Có 3 mục: Overview, Requirements, Other versions\n- Mặc định mở Overview", pre=AC)
c(H, "Kiểm tra các mục của Draft preview", LIST + "\n2. Bấm tên một framework Draft\n3. Kiểm tra cột mục bên trái",
  "- Có 3 mục: Framework, Tiers, Requirements", pre=DR)
c(H, "Kiểm tra khối Framework của framework Active", LIST + "\n2. Bấm tên một framework Active\n3. Kiểm tra khối Framework ở tab Overview",
  "- Hiển thị Code, Issued by, Version, Effective date, Description", pre=AC)
c(H, "Kiểm tra khối Tiers của framework có tier", LIST + "\n2. Bấm tên một framework Active có tier\n3. Kiểm tra khối Tiers ở tab Overview",
  "- Bảng có các cột Code, Tier, Rank, New at this tier, Total to meet\n- Mỗi tier một dòng", pre=ACT)
c(M, "Kiểm tra framework không tier không có khối Tiers", LIST + "\n2. Bấm tên một framework Active không tier\n3. Kiểm tra tab Overview",
  "- Không có khối Tiers", pre=ACN)
c(H, "Kiểm tra Total to meet của tier Basic", LIST + "\n2. Bấm tên framework Appendix 10 · 2022 (Active)\n3. Kiểm tra khối Tiers dòng Basic",
  "- New at this tier: 44\n- Total to meet: 44", "Chờ Hanna chọn cách ghi giá trị tính toán (FB-048, phương án A hoặc B)", pre="Có framework Appendix 10 · 2022 (Active)")
c(H, "Kiểm tra Total to meet của tier Medium", LIST + "\n2. Bấm tên framework Appendix 10 · 2022 (Active)\n3. Kiểm tra khối Tiers dòng Medium",
  "- New at this tier: 17\n- Total to meet: 61 (44 + 17)", "Chờ Hanna chọn cách ghi giá trị tính toán (FB-048, phương án A hoặc B)", pre="Có framework Appendix 10 · 2022 (Active)")
c(H, "Kiểm tra Total to meet của tier High", LIST + "\n2. Bấm tên framework Appendix 10 · 2022 (Active)\n3. Kiểm tra khối Tiers dòng High", "",
  "Q-F-10: Figma Detail ghi 18 và 79, khối Content cùng màn ghi 76 requirement; hệ thống ghi 15 và 76. Chưa biết số nào đúng", pre="Có framework Appendix 10 · 2022 (Active)")
c(M, "Kiểm tra khối Content của framework có tier", LIST + "\n2. Bấm tên một framework Active có tier\n3. Kiểm tra khối Content ở tab Overview",
  "- Hiển thị Dimensions, Control measures, Requirements, Expected evidence items", pre=ACT)
c(M, "Kiểm tra khối Content của framework không tier", LIST + "\n2. Bấm tên một framework Active không tier\n3. Kiểm tra khối Content ở tab Overview",
  "- Hiển thị Clauses, Requirements, Expected evidence items\n- Không có Dimensions và Control measures", pre=ACN)
c(H, "Kiểm tra phần đầu tab Requirements", LIST + "\n2. Bấm tên một framework Active\n3. Bấm tab Requirements",
  "- Tiêu đề và dòng tóm tắt dạng \"<n> dimensions · <n> control measures · <n> requirements. Read only — import a new version to change them.\"", pre=AC)
c(H, "Kiểm tra cây requirement", LIST + "\n2. Bấm tên một framework Active có tier\n3. Bấm tab Requirements\n4. Mở một dimension",
  "- Mỗi dimension hiển thị tên kèm số\n- Mở ra thấy control measure và requirement\n- Mỗi requirement kèm chip Basic, From Medium hoặc From High", pre=ACT)
c(H, "Kiểm tra khung chi tiết requirement", LIST + "\n2. Bấm tên một framework Active có tier\n3. Bấm tab Requirements\n4. Bấm một requirement",
  "- Khung bên phải hiển thị code, tiêu đề, mô tả\n- Có Applies to, Not required for, Sort order, Source\n- Có Expected evidence kèm số lượng và chip Mandatory", pre=ACT)
c(H, "Kiểm tra requirement chỉ đọc", LIST + "\n2. Bấm tên một framework Active\n3. Bấm tab Requirements\n4. Kiểm tra màn và khung chi tiết requirement",
  "- Không có nút thêm, sửa hoặc retire requirement", pre=AC)
c(H, "Kiểm tra tìm requirement theo mã", LIST + "\n2. Bấm tên một framework Active\n3. Bấm tab Requirements\n4. Nhập [mã requirement] vào ô Search", "",
  "Q-F-12: kết quả tìm requirement chưa kiểm", pre=AC)
c(M, "Kiểm tra tìm requirement theo tiêu đề", LIST + "\n2. Bấm tên một framework Active\n3. Bấm tab Requirements\n4. Nhập [một phần tiêu đề] vào ô Search", "",
  "Q-F-12: kết quả tìm requirement chưa kiểm", pre=AC)
c(M, "Kiểm tra tìm requirement không có kết quả", LIST + "\n2. Bấm tên một framework Active\n3. Bấm tab Requirements\n4. Nhập zzz vào ô Search", "",
  "Q-F-12: chữ báo không có kết quả ở tab Requirements chưa kiểm", pre=AC)
for t in ("Basic", "Medium", "High", "All tiers"):
    c(M, f"Kiểm tra lọc requirement: {t}", LIST + f"\n2. Bấm tên một framework Active có tier\n3. Bấm tab Requirements\n4. Chọn {t} ở ô lọc tier", "",
      "Q-F-12: kết quả lọc theo tier chưa kiểm (ô lọc có 4 lựa chọn: All tiers, Basic, Medium, High)", pre=ACT)
c(H, "Kiểm tra tổng số requirement của framework Appendix 10 · 2022", LIST + "\n2. Bấm tên framework Appendix 10 · 2022 (Active)\n3. Bấm tab Requirements\n4. Cộng số của 7 dimension",
  "- Số của 7 dimension lần lượt: 14, 14, 7, 11, 14, 7, 9\n- Tổng bằng 76\n- Bằng số Requirements ở tab Overview",
  "Chờ Hanna chọn cách ghi giá trị tính toán (FB-048, phương án A hoặc B)", pre="Có framework Appendix 10 · 2022 (Active)")
c(M, "Kiểm tra tổng số requirement của bản Draft Appendix 10 amended", LIST + "\n2. Bấm tên framework Appendix 10 amended (Draft)\n3. Bấm mục Requirements\n4. Cộng số của 7 dimension",
  "- Số của 7 dimension lần lượt: 14, 14, 8, 11, 15, 7, 10\n- Tổng bằng 79\n- Bằng số requirement ở khối Requirements",
  "Chờ Hanna chọn cách ghi giá trị tính toán (FB-048, phương án A hoặc B)", pre="Có framework Appendix 10 amended (Draft)")

# --- Nhập framework ---
c(H, "Kiểm tra mở hộp thoại Import từ danh sách", LIST + "\n2. Bấm Import framework",
  "- Mở hộp thoại Import a framework", "Q-F-05: hộp thoại có giống khi mở từ Import new version không")
c(M, "Kiểm tra mở hộp thoại Import từ Import new version", LIST + "\n2. Bấm tên một framework Active\n3. Bấm nút ba chấm\n4. Bấm Import new version", "",
  "Q-F-05: chưa bấm thử mục này; chưa rõ hộp thoại mở ra và có điền sẵn mã framework không", pre=AC)
c(H, "Kiểm tra bước 1 và bước 2 của hộp thoại Import", LIST + "\n2. Bấm Import framework\n3. Kiểm tra nội dung hộp thoại",
  "- Tiêu đề: Import a framework\n- Bước 1: Download the template and fill it in, kèm đoạn mô tả và nút Download template (.xlsx)\n- Bước 2: Upload the completed file, kèm ô Framework file *",
  "Q-F-06: đoạn mô tả liệt kê sheet Tiers; file mẫu ver 1 không có sheet Tiers")
c(M, "Kiểm tra vùng kéo thả file", LIST + "\n2. Bấm Import framework\n3. Kiểm tra ô Framework file *",
  "- Dòng: Drag files here or browse.\n- Dòng: Excel (.xlsx) · up to 20 MB · checked before anything is saved")
c(M, "Kiểm tra nút khi chưa chọn file", LIST + "\n2. Bấm Import framework\n3. Kiểm tra các nút ở cuối hộp thoại",
  "- Có nút Cancel và nút Check file", "Q-F-14: nút Check file có bị khoá khi chưa chọn file không")
c(L, "Kiểm tra nút Download template (.xlsx) trong hộp thoại", LIST + "\n2. Bấm Import framework\n3. Bấm Download template (.xlsx)", "",
  "Q-F-11: tên file tải về và nội dung chưa kiểm (không tải thật)", uc="[NGOÀI UC] Tải file mẫu: UC FWK-03 không nêu nút tải mẫu")
c(L, "Kiểm tra nút Download template ở đầu danh sách", LIST + "\n2. Bấm Download template", "",
  "Q-F-11: tên file tải về và nội dung chưa kiểm (không tải thật)", uc="[NGOÀI UC] Tải file mẫu: UC FWK-03 không nêu nút tải mẫu")
c(H, "Kiểm tra chọn file .xlsx hợp lệ", LIST + "\n2. Bấm Import framework\n3. Chọn file [file framework hợp lệ].xlsx",
  "- Hiển thị thẻ file gồm tên file, dung lượng, dấu tích và nút ×")
c(M, "Kiểm tra bỏ file đã chọn", LIST + "\n2. Bấm Import framework\n3. Chọn file [file framework hợp lệ].xlsx\n4. Bấm × trên thẻ file",
  "- Thẻ file biến mất, vùng kéo thả hiển thị lại")
c(H, "Kiểm tra chọn file không phải .xlsx", LIST + "\n2. Bấm Import framework\n3. Chọn file [file .pdf]", "",
  "Q-F-14: chưa có chữ báo lỗi cho file sai định dạng")
c(H, "Kiểm tra chọn file lớn hơn 20 MB", LIST + "\n2. Bấm Import framework\n3. Chọn file .xlsx lớn hơn 20 MB", "",
  "Q-F-14: chưa có chữ báo lỗi cho file quá dung lượng")

CHK = LIST + "\n2. Bấm Import framework\n3. Chọn file [file có lỗi: %s]\n4. Bấm Check file"
ERR = "- Hiển thị bảng lỗi gồm các cột Sheet, Row, Column, Problem\n- Dòng lỗi: %s"
c(H, "Kiểm tra lỗi mã cha không tồn tại", CHK % "parent_requirement_code là R.9.9, không có trong sheet Requirements",
  "- Hiển thị bảng lỗi gồm các cột Sheet, Row, Column, Problem\n- Dòng lỗi: Requirements · <dòng> · parent_requirement_code · \"R.9.9\" does not exist in this sheet.")
c(H, "Kiểm tra lỗi mã requirement bị trùng", CHK % "requirement_code R.9.4.2 xuất hiện hai lần",
  "- Hiển thị bảng lỗi gồm các cột Sheet, Row, Column, Problem\n- Dòng lỗi: Requirements · <dòng> · requirement_code · \"R.9.4.2\" is used twice (rows <dòng 1> and <dòng 2>).")
c(H, "Kiểm tra lỗi expected evidence trỏ vào dòng nhóm", CHK % "Expected_Evidence trỏ vào R.4 là dòng nhóm (is_assessable = FALSE)",
  "- Hiển thị bảng lỗi gồm các cột Sheet, Row, Column, Problem\n- Dòng lỗi: Expected_Evidence · <dòng> · requirement_code · \"R.4\" is a grouping row. Evidence must point to an assessable requirement.")
c(H, "Kiểm tra banner khi file có lỗi", CHK % "3 lỗi trên, tên file bcm-2019.xlsx",
  "- Banner: 3 errors in bcm-2019.xlsx\n- Dòng: Nothing was imported. Fix these rows in Excel and upload the file again.\n- Không có framework mới nào trong danh sách ở màn Frameworks")
c(H, "Kiểm tra tải file đã sửa ở ô Corrected file", CHK % "3 lỗi trên" + "\n5. Chọn file đã sửa hết lỗi ở ô Corrected file\n6. Bấm Check file", "",
  "Q-F-08: chưa bấm Check file nên chưa biết kết quả sau khi tải file đã sửa")
c(M, "Kiểm tra bấm Cancel khi đang có lỗi", CHK % "3 lỗi trên" + "\n5. Bấm Cancel", "",
  "Q-F-08: kết quả sau Cancel khi đang có lỗi chưa kiểm")
c(M, "Kiểm tra bấm × khi đang có lỗi", CHK % "3 lỗi trên" + "\n5. Bấm ×", "",
  "Q-F-08: kết quả sau × chưa kiểm")
c(M, "Kiểm tra bấm Esc khi đang có lỗi", CHK % "3 lỗi trên" + "\n5. Bấm phím Esc", "",
  "Q-F-08: kết quả sau Esc chưa kiểm")
for nm, what in (
    ("hai dòng ở sheet Framework", "sheet Framework có hai dòng"),
    ("thiếu framework_code, framework_name hoặc version", "thiếu framework_code"),
    ("requirement tự là cha của chính nó", "parent_requirement_code trùng requirement_code của chính dòng đó"),
    ("cha con tạo vòng lặp", "R.1 là cha của R.2 và R.2 là cha của R.1"),
    ("is_assessable không phải TRUE hoặc FALSE", "is_assessable là Maybe"),
    ("mã expected evidence bị trùng", "hai dòng Expected_Evidence cùng mã"),
    ("mandatory không phải TRUE hoặc FALSE", "mandatory là Maybe")):
    c(M, f"Kiểm tra lỗi: {nm}", CHK % what, "",
      "Q-F-14: chữ báo lỗi chưa có (sheet Validation_Rules của file mẫu chỉ nêu quy tắc, không nêu chữ hiển thị)")
c(H, "Kiểm tra import framework có mã chưa có", LIST + "\n2. Bấm Import framework\n3. Chọn file [file hợp lệ, framework_code chưa có trong danh sách]\n4. Bấm Check file", "",
  "Q-F-08: chưa bấm Check file; chưa biết màn đến sau Check file thành công. Q-F-04: có bảng tóm tắt thay đổi (added) hay không")
c(H, "Kiểm tra import phiên bản mới của mã đã có", LIST + "\n2. Bấm Import framework\n3. Chọn file [file hợp lệ, framework_code đã có, Version khác]\n4. Bấm Check file", "",
  "Q-F-04: UC nói cập nhật framework có sẵn và content_version phải tăng; Figma và hộp thoại nói thêm thành một bản riêng. Chưa rõ kết quả")

# --- Draft preview ---
c(H, "Kiểm tra tên và chip của Draft preview", LIST + "\n2. Bấm tên một framework Draft\n3. Kiểm tra phần đầu trang",
  "- Tên: Security Baselines for ICT Systems (Appendix 10)\n- Chip: Draft · not active\n- Dòng: TW_ISRM_ANNEX10_EN · Appendix 10 per Article 11 – amended version · MODA", pre="Có framework Draft Appendix 10 amended")
c(H, "Kiểm tra nút Discard draft và Activate", LIST + "\n2. Bấm tên một framework Draft\n3. Kiểm tra góc phải phần đầu trang",
  "- Có nút Discard draft và nút Activate", pre=DR, uc="FWK-06")
c(H, "Kiểm tra khối Framework của bản Draft", LIST + "\n2. Bấm tên framework Appendix 10 amended (Draft)\n3. Kiểm tra khối 1 Framework",
  "- Ghi chú: From the Framework sheet\n- Code, Issued by: MODA, Version\n- Effective date: Not set\n- Description", pre="Có framework Draft Appendix 10 amended")
c(H, "Kiểm tra khối Tiers của bản Draft", LIST + "\n2. Bấm tên framework Appendix 10 amended (Draft)\n3. Kiểm tra khối 2 Tiers",
  "- Ghi chú: Higher tiers include every requirement of the tiers below\n- P Basic, Rank 1: New 44, Total 44\n- M Medium, Rank 2: New 17, Total 61\n- H High, Rank 3: New 18, Total 79", "Chờ Hanna chọn cách ghi giá trị tính toán (FB-048, phương án A hoặc B)", pre="Có framework Draft Appendix 10 amended")
c(H, "Kiểm tra khối Requirements của bản Draft", LIST + "\n2. Bấm tên framework Appendix 10 amended (Draft)\n3. Kiểm tra khối 3 Requirements",
  "- 7 dimensions · 27 control measures · 79 requirements · 79 expected evidence items", pre="Có framework Draft Appendix 10 amended")
c(M, "Kiểm tra khung Import: File check passed", LIST + "\n2. Bấm tên một framework Draft\n3. Kiểm tra khung bên phải mục Import",
  "- File check passed\n- No errors. The draft is ready to activate.",
  "Q-F-07: khung After activation khác nhau giữa Figma và hệ thống (xem case kế)", pre=DR, uc="FWK-03")
c(M, "Kiểm tra khung After activation", LIST + "\n2. Bấm tên một framework Draft\n3. Kiểm tra khung After activation", "",
  "Q-F-07: Figma ghi SGS gán tier cho từng scope; hệ thống ghi khách chọn tier của scope. Chưa rõ bên nào đúng", pre=DR, uc="FWK-06")
c(H, "Kiểm tra mở hộp thoại Discard draft", LIST + "\n2. Bấm tên một framework Draft\n3. Bấm Discard draft",
  "- Hộp thoại Discard draft?\n- Nội dung: The imported draft of <tên framework> is removed. Customers never saw it. You can import the file again later.\n- Có nút Cancel và Discard draft", "Q-F-11: Discard draft không có trong UC, Figma chưa vẽ hộp thoại", pre=DR, uc="[NGOÀI UC] Discard draft: UC FWK-03 và FWK-06 không nêu")
for t, stp in (("Cancel", "Bấm Cancel"), ("×", "Bấm ×"), ("Esc", "Bấm phím Esc")):
    c(M, f"Kiểm tra huỷ hộp thoại Discard draft: {t}", LIST + f"\n2. Bấm tên một framework Draft\n3. Bấm Discard draft\n4. {stp}", "",
      "Q-F-11: kết quả sau khi đóng hộp thoại chưa kiểm", pre=DR, uc="[NGOÀI UC] Discard draft: UC FWK-03 và FWK-06 không nêu")
c(H, "Kiểm tra Discard draft", LIST + "\n2. Bấm tên một framework Draft\n3. Bấm Discard draft\n4. Bấm Discard draft trong hộp thoại", "",
  "Q-F-08: chưa bấm nút xác nhận trên hệ thống; chưa biết màn đến và dòng Draft còn trong danh sách không", pre=DR, uc="[NGOÀI UC] Discard draft: UC FWK-03 và FWK-06 không nêu")

# --- Kích hoạt ---
ACTS = LIST + "\n2. Bấm tên một framework Draft\n3. Bấm Activate"
c(H, "Kiểm tra mở hộp thoại Activate", ACTS,
  "- Tiêu đề: Activate framework\n- Câu hỏi: Activate <tên framework> · <version>?\n- Có nút Cancel và Activate framework\n- Gạch 1: Customers can activate it on their scopes.\n- Gạch 3: The content is locked. Changes need a new version.",
  "Q-F-07: gạch 2 khác nhau (Figma: SGS assigns each scope a tier: Basic, Medium or High. Hệ thống: Each customer chooses the tier of their scope: Basic, Medium or High.)", pre=DR)
c(M, "Kiểm tra huỷ Activate: Cancel", ACTS + "\n4. Bấm Cancel",
  "- Hộp thoại đóng, ở lại Draft preview\n- Framework vẫn là Draft", "Q-F-08: hành vi sau Cancel suy từ hộp thoại, chưa xác nhận", pre=DR)
c(M, "Kiểm tra huỷ Activate: ×", ACTS + "\n4. Bấm ×", "", "Q-F-08: chưa kiểm", pre=DR)
c(M, "Kiểm tra huỷ Activate: Esc", ACTS + "\n4. Bấm phím Esc", "", "Q-F-08: chưa kiểm", pre=DR)
c(H, "Kiểm tra Activate khi chưa có Active retention policy", ACTS + "\n4. Bấm Activate framework", "",
  "Q-F-07: UC FWK-06 chỉ cho kích hoạt khi có Active retention policy (CFG-01); Figma và hệ thống không có kiểm tra này, trang Settings ghi No design yet",
  pre=DR + "\nChưa có Active retention policy")
c(H, "Kiểm tra Activate framework có tier", ACTS + "\n4. Bấm Activate framework", "",
  "Q-F-08: chưa bấm nút xác nhận; chưa biết màn đến, chip Status và hiển thị trong danh sách", pre="Có framework Draft có tier: [Framework Draft có tier]")
c(H, "Kiểm tra Activate framework không tier", ACTS + "\n4. Bấm Activate framework", "",
  "Q-F-08: chưa có bản Draft không tier để kiểm; chưa biết kết quả", pre="Có framework Draft không tier: [Framework Draft không tier]")
c(H, "Kiểm tra framework vừa kích hoạt trong danh sách chọn của Customer Admin",
  "1. Đăng nhập account SGS Admin, bấm Activate framework cho [Framework Draft]\n2. Đăng xuất, đăng nhập account Customer Admin\n3. Mở Scopes, bấm một scope, bấm Link framework\n4. Mở danh sách chọn framework", "",
  "Q-F-08: chưa bấm Activate nên chưa kiểm; danh sách chọn hiện gộp theo mã (6 mục), không thấy chọn phiên bản", pre=DR)
c(M, "Kiểm tra framework Draft không có trong danh sách chọn của Customer Admin",
  "1. Mở Scopes, bấm một scope, bấm Link framework\n2. Mở danh sách chọn framework\n3. Tìm [Framework Draft]", "",
  "Q-F-08: chưa kiểm; ghi chú: hệ thống có 6 mục khi có 8 framework, chưa rõ Draft có bị loại không", pre=DR + "\nĐăng nhập account Customer Admin")

# --- Phân quyền ---
c(H, "Kiểm tra SGS Admin thấy nút ở danh sách", LIST + "\n2. Kiểm tra phần đầu trang", "- Có nút Download template và Import framework", uc="FWK-01")
c(H, "Kiểm tra SGS Admin thấy nút ở Draft preview", LIST + "\n2. Bấm tên một framework Draft", "- Có nút Discard draft và Activate", pre=DR, uc="FWK-06")
c(M, "Kiểm tra SGS Admin thấy nút ba chấm ở framework Active", LIST + "\n2. Bấm tên một framework Active", "- Có nút ba chấm", pre=AC, uc="FWK-03")
c(H, "Kiểm tra SGS User ở danh sách", LIST + "\n2. Kiểm tra menu trái và phần đầu trang",
  "- Menu có Frameworks\n- Danh sách hiển thị\n- Không có nút Download template và Import framework", "Q-F-16: UC chỉ nêu SGS Admin, chưa rõ SGS User có được xem không", pre="Đăng nhập account SGS User (thay cho SGS Admin)")
c(H, "Kiểm tra SGS User ở Draft preview", LIST + "\n2. Bấm tên một framework Draft",
  "- Mở được Draft preview\n- Không có nút Discard draft và Activate", "Q-F-16: UC chỉ nêu SGS Admin", pre=DR + "\nĐăng nhập account SGS User (thay cho SGS Admin)", uc="FWK-02")
c(H, "Kiểm tra SGS Consultant ở danh sách", LIST + "\n2. Kiểm tra menu trái và phần đầu trang",
  "- Menu có Frameworks\n- Danh sách hiển thị\n- Không có nút Download template và Import framework", "Q-F-16: UC chỉ nêu SGS Admin; chưa mở chi tiết", pre="Đăng nhập account SGS Consultant (thay cho SGS Admin)")
c(H, "Kiểm tra SGS Auditor/Certification không thấy menu Frameworks", "1. Kiểm tra menu trái",
  "- Menu không có Frameworks", "Q-F-16", pre="Đăng nhập account SGS Auditor/Certification (thay cho SGS Admin)")
c(H, "Kiểm tra SGS Auditor/Certification mở thẳng địa chỉ danh sách", "1. Mở thẳng địa chỉ của màn Frameworks", "",
  "Q-F-16: vào bằng địa chỉ chưa kiểm", pre="Đăng nhập account SGS Auditor/Certification (thay cho SGS Admin)")
c(H, "Kiểm tra Customer Admin không thấy menu Frameworks", "1. Kiểm tra menu trái", "- Menu không có Frameworks", "Q-F-16",
  pre="Đăng nhập account Customer Admin (thay cho SGS Admin)")
c(H, "Kiểm tra Customer User không thấy menu Frameworks", "1. Kiểm tra menu trái", "", "Q-F-16: chưa kiểm vai trò này",
  pre="Đăng nhập account Customer User (thay cho SGS Admin)")
c(H, "Kiểm tra Customer Viewer không thấy menu Frameworks", "1. Kiểm tra menu trái", "", "Q-F-16: chưa kiểm vai trò này",
  pre="Đăng nhập account Customer Viewer (thay cho SGS Admin)")
c(H, "Kiểm tra Customer Admin mở thẳng địa chỉ danh sách", "1. Mở thẳng địa chỉ của màn Frameworks", "",
  "Q-F-16: vào bằng địa chỉ chưa kiểm", pre="Đăng nhập account Customer Admin (thay cho SGS Admin)")

# --- Bảo mật ---
c(M, "Kiểm tra ô bắt đầu bằng dấu = trong file import", LIST + "\n2. Bấm Import framework\n3. Chọn file [file hợp lệ, Description bắt đầu bằng =1+1]\n4. Bấm Check file", "",
  "Q-F-14: chưa kiểm; kết quả mong đợi: hiện nguyên văn =1+1 ở bản nháp")
c(M, "Kiểm tra thẻ script trong Description của file import", LIST + "\n2. Bấm Import framework\n3. Chọn file [file hợp lệ, Description là <script>alert(1)</script>]\n4. Bấm Check file", "",
  "Q-F-14: chưa kiểm; kết quả mong đợi: hiện nguyên văn, không chạy script")
for act in ("Import", "Kích hoạt", "Huỷ bản nháp"):
    c(M, f"Kiểm tra ghi vết: {act}", f"1. Thực hiện {act.lower()} một framework\n2. Đăng nhập account SGS Admin, bấm Audit Logs ở menu trái\n3. Tìm dòng mới nhất", "",
      "Q-F-17: nội dung dòng ghi vết chưa kiểm; chưa bấm nút xác nhận để tạo dòng ghi vết (Q-F-08)",
      pre=DR)
