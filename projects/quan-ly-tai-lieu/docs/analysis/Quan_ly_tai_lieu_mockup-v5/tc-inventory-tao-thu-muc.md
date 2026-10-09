# Inventory — FEEC_PM_IT_Test_Case_Document_v3.xlsx · phần Tạo mới folder · lượt 1: trích xuất nguyên văn

> Trạng thái: BẢN NHÁP v0.1. Sinh bằng script từ file xlsx, không chép tay. Đi kèm `analysis.md` §7.

| | |
|---|---|
| Nguồn | `docs/source/FEEC_PM_IT_Test_Case_Document_v3.xlsx` · 181.524 byte · 3 sheet |
| Sheet | `Cover` (A1:I31, 1 ảnh) · `Test_Report` (A1:AB1004, 918 công thức) · `Document` (A1:AC1063; dữ liệu TC ở hàng 13–162, 150 TC) |
| Phạm vi | 8 TC của Tạo mới folder (mục B) và 8 TC tham chiếu (mục C) |
| Cách lấy | openpyxl, đọc giá trị đã lưu; ô gộp lấy giá trị của ô neo và ghi dải gộp |
| Ngày | 2026-10-02 |

**Quy ước:** 「…」 là nguyên văn của ô. Xuống dòng trong ô ghi là ⏎. Ký tự lạ (dấu thừa, chữ ở dạng tổ hợp) được giữ nguyên. Tên cột trong bảng lấy theo vị trí cột của hàng tiêu đề 11–12; cột Q, R, S, T ghi đúng tên tiêu đề kể cả khi dữ liệu nằm lệch cột (xem `analysis.md` §7.8).

## A. Khung sheet Document (hàng 3–12)

| Ô | Nội dung | Nguyên văn |
|---|---|---|
| B3 / C3 | Function Name | 「DM-L0001_図書管理」 |
| B4 / C4 | Screen Name | 「Quản lý thư viện」 |
| B5 / C5 | Creator | 「ThaVT」 |
| B6 / C6 | Created date | 2026-01-09 |
| B7 / C7 | Reference | (trống) |
| K4:R5 | Tổng kết Round 1 (giá trị đã lưu) | Total 150 · Passed 33 · Failed 30 · Pending 73 · Blocked 0 · NA 2 · Not execute 12 |
| K6:R7 | Tổng kết Round 2 (giá trị đã lưu) | Total 150 · Passed 0 · Failed 0 · Pending 0 · Blocked 0 · NA 0 · Not execute 150 |
| M4 | Công thức đếm Round 1 | 「=COUNTIF($M$25:$M994,M3)」 — bắt đầu từ hàng 25 |
| M6 | Công thức đếm Round 2 | 「=COUNTIF($R$25:$R$168,M3)」 — bắt đầu từ hàng 25 |
| L4, L6 | Công thức Total | 「=COUNTA($G$13:$G$165)」 — bắt đầu từ hàng 13 |
| Hàng 11–12 | Tiêu đề cột | A No. · B–E Classification I–IV · F Priority · G TVP_ID · H Test case name/ Test view point · I Pre-condition · J Step · K Expected result · L Dev test · M–Q Round 1 (Result, Test person, Test date, Bug_ID, Remark) · R–V Round 2 (như trên) · W Open question · X UC |

## B. TC thuộc phạm vi (8)

### TC_021 · Document!R33

| Ô | Cột | Nguyên văn |
|---|---|---|
| A33 | No. | 「21」 |
| B33 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C33 (ô neo của dải gộp C33:C36) | II | 「+ Tạo mới」 |
| D33 | III | (trống) |
| E33 | IV | (trống) |
| F33 | Priority | 「Medium」 |
| G33 | TVP_ID | 「TC_021」 |
| H33 | Test case name/ Test view point | 「Kiểm tra hiển thị khi click vào button [+ + Tạo mới]」 |
| I33 | Pre-condition | (trống) |
| J33 | Step | 「1. Click vào button [++ Tạo mới] ⏎ 2. Kiểm tra hiển thị」 |
| K33 | Expected result | 「Hiển thị popover: ⏎ - Tạo thư mục mới ⏎ - Tải tệp lên」 |
| L33 | Dev test | (trống) |
| M33 | Result (R1) | 「Passed」 |
| N33 | Test person (R1) | 「ThaVT」 |
| O33 | Test date (R1) | 「20/05/2026」 |
| P33 | Bug_ID (R1) | (trống) |
| Q33 | Remark (R1) | 「Passed」 |
| R33 | Result (R2) | 「ThaVT」 |
| S33 | Test person (R2) | 「22/05/2026」 |
| T33 | Test date (R2) | 「2026-05-22」 |
| U33 | Bug_ID (R2) | (trống) |
| V33 | Remark (R2) | (trống) |
| W33 | Open question | (trống) |
| X33 | UC | (trống) |

### TC_022 · Document!R34

| Ô | Cột | Nguyên văn |
|---|---|---|
| A34 | No. | 「22」 |
| B34 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C34 (ô gộp C33:C36, giá trị ở ô neo) | II | 「+ Tạo mới」 |
| D34 | III | 「Tạo thư mục mới」 |
| E34 | IV | (trống) |
| F34 | Priority | 「Medium」 |
| G34 | TVP_ID | 「TC_022」 |
| H34 | Test case name/ Test view point | 「Kiểm tra hiển thị khi click vào item [Tạo thư mục mới]」 |
| I34 | Pre-condition | (trống) |
| J34 | Step | 「1. Click vào item [Tạo thư mục mới] ⏎ 2. Kiểm tra hiển thị」 |
| K34 | Expected result | 「- Hiển thị màn hình: PM0035」 |
| L34 | Dev test | (trống) |
| M34 | Result (R1) | 「Passed」 |
| N34 | Test person (R1) | 「ThaVT」 |
| O34 | Test date (R1) | 「20/05/2026」 |
| P34 | Bug_ID (R1) | (trống) |
| Q34 | Remark (R1) | 「Passed」 |
| R34 | Result (R2) | 「ThaVT」 |
| S34 | Test person (R2) | 「22/05/2026」 |
| T34 | Test date (R2) | 「2026-05-22」 |
| U34 | Bug_ID (R2) | (trống) |
| V34 | Remark (R2) | (trống) |
| W34 | Open question | (trống) |
| X34 | UC | (trống) |

### TC_079 · Document!R91

| Ô | Cột | Nguyên văn |
|---|---|---|
| A91 | No. | 「79」 |
| B91 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C91 (ô neo của dải gộp C91:C162) | II | 「Chức năng tệp - File function 」 |
| D91 (ô neo của dải gộp D91:D95) | III | 「Tạo Folder manual」 |
| E91 | IV | (trống) |
| F91 | Priority | 「High」 |
| G91 | TVP_ID | 「TC_079」 |
| H91 | Test case name/ Test view point | 「Kiểm tra tạo 1 folder có tên dưới 255 ký tự」 |
| I91 | Pre-condition | (trống) |
| J91 | Step | 「1. Click vào button [+ + Tạo mới] ⏎ 2. Tạo Folder mới tên [Folder 1] ⏎ 3. Kiểm tra hiển thị 」 |
| K91 | Expected result | 「- Cho phép tạo thành công và hiển thị folder tên [Folder 1]」 |
| L91 | Dev test | (trống) |
| M91 | Result (R1) | 「Pending」 |
| N91 | Test person (R1) | 「ThaVT」 |
| O91 | Test date (R1) | 「20/05/2026」 |
| P91 | Bug_ID (R1) | (trống) |
| Q91 | Remark (R1) | 「Passed」 |
| R91 | Result (R2) | 「ThaVT」 |
| S91 | Test person (R2) | 「22/05/2026」 |
| T91 | Test date (R2) | 「2026-05-22」 |
| U91 | Bug_ID (R2) | (trống) |
| V91 | Remark (R2) | (trống) |
| W91 | Open question | (trống) |
| X91 | UC | (trống) |

### TC_080 · Document!R92

| Ô | Cột | Nguyên văn |
|---|---|---|
| A92 | No. | 「80」 |
| B92 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C92 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D92 (ô gộp D91:D95, giá trị ở ô neo) | III | 「Tạo Folder manual」 |
| E92 | IV | (trống) |
| F92 | Priority | 「High」 |
| G92 | TVP_ID | 「TC_080」 |
| H92 | Test case name/ Test view point | 「Kiểm tra tạo 10 folder cấp con trong 1 folder cha」 |
| I92 | Pre-condition | (trống) |
| J92 | Step | 「1. Trong folder [Folder 1] > Tạo folder cấp con [Folder 2]  ⏎ 2. Trong folder [Folder 2] > Tạo folder cấp con [Folder 3]  ⏎ 3. Tiếp tục tạo đến folder cấp 10 > [Folder 10] ⏎ 3. Kiểm tra hiển thị」 |
| K92 | Expected result | 「- Cho phép tạo thành công 10 thư mục cấp con trong 1 thư mục cha」 |
| L92 | Dev test | (trống) |
| M92 | Result (R1) | 「Pending」 |
| N92 | Test person (R1) | 「ThaVT」 |
| O92 | Test date (R1) | 「20/05/2026」 |
| P92 | Bug_ID (R1) | (trống) |
| Q92 | Remark (R1) | 「Passed」 |
| R92 | Result (R2) | 「ThaVT」 |
| S92 | Test person (R2) | 「22/05/2026」 |
| T92 | Test date (R2) | 「2026-05-22」 |
| U92 | Bug_ID (R2) | (trống) |
| V92 | Remark (R2) | (trống) |
| W92 | Open question | (trống) |
| X92 | UC | (trống) |

### TC_081 · Document!R93

| Ô | Cột | Nguyên văn |
|---|---|---|
| A93 | No. | 「81」 |
| B93 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C93 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D93 (ô gộp D91:D95, giá trị ở ô neo) | III | 「Tạo Folder manual」 |
| E93 | IV | (trống) |
| F93 | Priority | 「High」 |
| G93 | TVP_ID | 「TC_081」 |
| H93 | Test case name/ Test view point | 「Kiểm tra tạo 11 folder cấp con trong 1 folder cha」 |
| I93 | Pre-condition | (trống) |
| J93 | Step | 「1. Tạo 10 cấp thư mục con ⏎ 2. Tiếp tục tạo đến folder cấp 11 > [Folder 11] ⏎ 3. Kiểm tra hiển thị」 |
| K93 | Expected result | 「- Hiển thị thông bá́o lỗi: フォルダの階層が上限（10階層）に達しているため、サブフォルダを作成できません。」 |
| L93 | Dev test | (trống) |
| M93 | Result (R1) | 「Failed」 |
| N93 | Test person (R1) | 「ThaVT」 |
| O93 | Test date (R1) | 「20/05/2026」 |
| P93 | Bug_ID (R1) | 「1」 |
| Q93 | Remark (R1) | 「Passed」 |
| R93 | Result (R2) | 「ThaVT」 |
| S93 | Test person (R2) | 「22/05/2026」 |
| T93 | Test date (R2) | 「2026-05-22」 |
| U93 | Bug_ID (R2) | (trống) |
| V93 | Remark (R2) | (trống) |
| W93 | Open question | 「フォルダの階層が上限（10階層）に達しているため、サブフォルダを作成できません。」 |
| X93 | UC | (trống) |

### TC_082 · Document!R94

| Ô | Cột | Nguyên văn |
|---|---|---|
| A94 | No. | 「82」 |
| B94 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C94 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D94 (ô gộp D91:D95, giá trị ở ô neo) | III | 「Tạo Folder manual」 |
| E94 | IV | (trống) |
| F94 | Priority | 「High」 |
| G94 | TVP_ID | 「TC_082」 |
| H94 | Test case name/ Test view point | 「Kiểm tra đặt tên folder quá 255 ký tự」 |
| I94 | Pre-condition | (trống) |
| J94 | Step | 「1. Click vào button [+ + Tạo mới] ⏎ 2. Nhập quá 255 ký tự  ⏎ 3. Kiểm tra hiển thị」 |
| K94 | Expected result | 「- Hệ thống tự cắt ký tự và báo lỗi: フォルダ名が長すぎます（最大255文字）」 |
| L94 | Dev test | (trống) |
| M94 | Result (R1) | 「Pending」 |
| N94 | Test person (R1) | 「ThaVT」 |
| O94 | Test date (R1) | 「20/05/2026」 |
| P94 | Bug_ID (R1) | (trống) |
| Q94 | Remark (R1) | 「Passed」 |
| R94 | Result (R2) | 「ThaVT」 |
| S94 | Test person (R2) | 「22/05/2026」 |
| T94 | Test date (R2) | 「2026-05-22」 |
| U94 | Bug_ID (R2) | (trống) |
| V94 | Remark (R2) | (trống) |
| W94 | Open question | 「フォルダ名が長すぎます（最大255文字）」 |
| X94 | UC | (trống) |

### TC_083 · Document!R95

| Ô | Cột | Nguyên văn |
|---|---|---|
| A95 | No. | 「83」 |
| B95 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C95 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D95 (ô gộp D91:D95, giá trị ở ô neo) | III | 「Tạo Folder manual」 |
| E95 | IV | (trống) |
| F95 | Priority | 「Medium」 |
| G95 | TVP_ID | 「TC_083」 |
| H95 | Test case name/ Test view point | 「Kiểm tra tạ̣o folder với ký tự chứa Full-Width」 |
| I95 | Pre-condition | (trống) |
| J95 | Step | 「1. Tạo folder với ký tự: ⏎ - ＮＲＴ０７８ ⏎ 2. Kiểm tra hiển thị」 |
| K95 | Expected result | 「- Cho phép tạo bình thường」 |
| L95 | Dev test | (trống) |
| M95 | Result (R1) | 「Pending」 |
| N95 | Test person (R1) | 「ThaVT」 |
| O95 | Test date (R1) | 「20/05/2026」 |
| P95 | Bug_ID (R1) | (trống) |
| Q95 | Remark (R1) | 「Passed」 |
| R95 | Result (R2) | 「ThaVT」 |
| S95 | Test person (R2) | 「22/05/2026」 |
| T95 | Test date (R2) | 「2026-05-22」 |
| U95 | Bug_ID (R2) | (trống) |
| V95 | Remark (R2) | (trống) |
| W95 | Open question | (trống) |
| X95 | UC | (trống) |

### TC_143 · Document!R155

| Ô | Cột | Nguyên văn |
|---|---|---|
| A155 | No. | 「143」 |
| B155 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C155 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D155 (ô neo của dải gộp D155:D162) | III | 「Thông tin dữ liệu」 |
| E155 | IV | 「Tạo folder trùng tên」 |
| F155 | Priority | 「High」 |
| G155 | TVP_ID | 「TC_143」 |
| H155 | Test case name/ Test view point | 「Kiểm tra tạ̣o folder trùng tên」 |
| I155 | Pre-condition | (trống) |
| J155 | Step | 「1. Tạo 1 folder có tên A ⏎ 2. Tiếp tục tạo folder A ⏎ 3. Kiểm tra hiển thị」 |
| K155 | Expected result | 「- Hiển thị thêm Số thứ tự」 |
| L155 | Dev test | (trống) |
| M155 | Result (R1) | 「Pending」 |
| N155 | Test person (R1) | 「ThaVT」 |
| O155 | Test date (R1) | 「20/05/2026」 |
| P155 | Bug_ID (R1) | (trống) |
| Q155 | Remark (R1) | 「Passed」 |
| R155 | Result (R2) | 「ThaVT」 |
| S155 | Test person (R2) | 「09/06/2026」 |
| T155 | Test date (R2) | 「2026-06-09」 |
| U155 | Bug_ID (R2) | (trống) |
| V155 | Remark (R2) | (trống) |
| W155 | Open question | (trống) |
| X155 | UC | (trống) |

## C. TC tham chiếu — ngoài phạm vi, dùng để đối chiếu (8)

### TC_024 · Document!R36

| Ô | Cột | Nguyên văn |
|---|---|---|
| A36 | No. | 「24」 |
| B36 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C36 (ô gộp C33:C36, giá trị ở ô neo) | II | 「+ Tạo mới」 |
| D36 | III | 「Tải thư mục lên」 |
| E36 | IV | (trống) |
| F36 | Priority | 「Medium」 |
| G36 | TVP_ID | 「TC_024」 |
| H36 | Test case name/ Test view point | 「Kiểm tra hiển thị khi click vào item [Tải thư mục lên]」 |
| I36 | Pre-condition | (trống) |
| J36 | Step | 「1. Click vào item [Tải thư mục lên] ⏎ 2. Kiểm tra hiển thị」 |
| K36 | Expected result | 「- Hiển thị màn hình: Upload Folder/ZIP」 |
| L36 | Dev test | (trống) |
| M36 | Result (R1) | 「Passed」 |
| N36 | Test person (R1) | 「ThaVT」 |
| O36 | Test date (R1) | 「20/05/2026」 |
| P36 | Bug_ID (R1) | (trống) |
| Q36 | Remark (R1) | 「Passed」 |
| R36 | Result (R2) | 「ThaVT」 |
| S36 | Test person (R2) | 「22/05/2026」 |
| T36 | Test date (R2) | 「2026-05-22」 |
| U36 | Bug_ID (R2) | (trống) |
| V36 | Remark (R2) | (trống) |
| W36 | Open question | (trống) |
| X36 | UC | (trống) |

### TC_054 · Document!R66

| Ô | Cột | Nguyên văn |
|---|---|---|
| A66 | No. | 「54」 |
| B66 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C66 (ô gộp C37:C73, giá trị ở ô neo) | II | 「Bảng dữ liệu - Table」 |
| D66 (ô gộp D45:D73, giá trị ở ô neo) | III | 「Content」 |
| E66 (ô gộp E65:E70, giá trị ở ô neo) | IV | 「Đổi tên」 |
| F66 | Priority | 「Medium」 |
| G66 | TVP_ID | 「TC_054」 |
| H66 | Test case name/ Test view point | 「Kiểm tra trạng thái của textbox tên file khi xóa toàn bộ text trong textbox」 |
| I66 | Pre-condition | (trống) |
| J66 | Step | 「1. Click vào button [Đổi tên] ⏎ 2. Xóa toàn bộ text trong textbox tên file ⏎ 3. Kiểm tra hiển thị của textbox tên file」 |
| K66 | Expected result | 「- Hiển thị placeholder: ファイル名を入力」 |
| L66 | Dev test | (trống) |
| M66 | Result (R1) | 「Passed」 |
| N66 | Test person (R1) | 「ThaVT」 |
| O66 | Test date (R1) | 「20/05/2026」 |
| P66 | Bug_ID (R1) | (trống) |
| Q66 | Remark (R1) | 「Passed」 |
| R66 | Result (R2) | 「ThaVT」 |
| S66 | Test person (R2) | 「22/05/2026」 |
| T66 | Test date (R2) | 「2026-05-22」 |
| U66 | Bug_ID (R2) | (trống) |
| V66 | Remark (R2) | (trống) |
| W66 | Open question | 「ファイル名を入力」 |
| X66 | UC | (trống) |

### TC_055 · Document!R67

| Ô | Cột | Nguyên văn |
|---|---|---|
| A67 | No. | 「55」 |
| B67 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C67 (ô gộp C37:C73, giá trị ở ô neo) | II | 「Bảng dữ liệu - Table」 |
| D67 (ô gộp D45:D73, giá trị ở ô neo) | III | 「Content」 |
| E67 (ô gộp E65:E70, giá trị ở ô neo) | IV | 「Đổi tên」 |
| F67 | Priority | 「High」 |
| G67 | TVP_ID | 「TC_055」 |
| H67 | Test case name/ Test view point | 「Kiểm tra hiển thị khi bỏ trống tên file 」 |
| I67 | Pre-condition | (trống) |
| J67 | Step | 「1. Click vào button [Đổi tên] ⏎ 2. Xóa toàn bộ text trong textbox tên file ⏎ 3. Click vào button [Lưu] ⏎ 4. Kiểm tra hiển thị」 |
| K67 | Expected result | 「- Hiển thị message cảnh báo đỏ:  ⏎ ファイル名を入力してください」 |
| L67 | Dev test | (trống) |
| M67 | Result (R1) | 「Passed」 |
| N67 | Test person (R1) | 「ThaVT」 |
| O67 | Test date (R1) | 「20/05/2026」 |
| P67 | Bug_ID (R1) | (trống) |
| Q67 | Remark (R1) | 「Passed」 |
| R67 | Result (R2) | 「ThaVT」 |
| S67 | Test person (R2) | 「22/05/2026」 |
| T67 | Test date (R2) | 「2026-05-22」 |
| U67 | Bug_ID (R2) | (trống) |
| V67 | Remark (R2) | (trống) |
| W67 | Open question | 「ファイル名を入力してください」 |
| X67 | UC | (trống) |

### TC_139 · Document!R151

| Ô | Cột | Nguyên văn |
|---|---|---|
| A151 | No. | 「139」 |
| B151 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C151 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D151 | III | 「Đổi tên folder」 |
| E151 | IV | (trống) |
| F151 | Priority | 「High」 |
| G151 | TVP_ID | 「TC_139」 |
| H151 | Test case name/ Test view point | 「Kiểm tra hiển thị khi sửa folder」 |
| I151 | Pre-condition | (trống) |
| J151 | Step | 「1. Tạo file trên role ES/PM ⏎ 2. Sửa tên file ⏎ 3. Kiểm tra hiển thị trên role PM」 |
| K151 | Expected result | 「- Hiển thị đúng tên file sau khi sửa trên danh sách」 |
| L151 | Dev test | (trống) |
| M151 | Result (R1) | 「Failed」 |
| N151 | Test person (R1) | 「ThaVT」 |
| O151 | Test date (R1) | 「20/05/2026」 |
| P151 | Bug_ID (R1) | 「2」 |
| Q151 | Remark (R1) | 「Passed」 |
| R151 | Result (R2) | 「ThaVT」 |
| S151 | Test person (R2) | 「22/05/2026」 |
| T151 | Test date (R2) | 「2026-05-22」 |
| U151 | Bug_ID (R2) | (trống) |
| V151 | Remark (R2) | (trống) |
| W151 | Open question | (trống) |
| X151 | UC | (trống) |

### TC_141 · Document!R153

| Ô | Cột | Nguyên văn |
|---|---|---|
| A153 | No. | 「141」 |
| B153 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C153 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D153 | III | 「Chuyển folder」 |
| E153 | IV | (trống) |
| F153 | Priority | 「High」 |
| G153 | TVP_ID | 「TC_141」 |
| H153 | Test case name/ Test view point | 「Kiểm tra hiển thị khi chuyển folder」 |
| I153 | Pre-condition | (trống) |
| J153 | Step | 「1. Tạo file trên role ES/PM ⏎ 2. Chuyển folder ⏎ 3. Kiểm tra hiển thị trên role PM」 |
| K153 | Expected result | 「- Hiển thị đúng vị trí mới của folder trên danh sách」 |
| L153 | Dev test | (trống) |
| M153 | Result (R1) | 「Failed」 |
| N153 | Test person (R1) | 「ThaVT」 |
| O153 | Test date (R1) | 「20/05/2026」 |
| P153 | Bug_ID (R1) | 「6」 |
| Q153 | Remark (R1) | 「Passed」 |
| R153 | Result (R2) | 「ThaVT」 |
| S153 | Test person (R2) | 「22/05/2026」 |
| T153 | Test date (R2) | 「2026-05-22」 |
| U153 | Bug_ID (R2) | (trống) |
| V153 | Remark (R2) | (trống) |
| W153 | Open question | (trống) |
| X153 | UC | (trống) |

### TC_144 · Document!R156

| Ô | Cột | Nguyên văn |
|---|---|---|
| A156 | No. | 「144」 |
| B156 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C156 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D156 (ô gộp D155:D162, giá trị ở ô neo) | III | 「Thông tin dữ liệu」 |
| E156 | IV | 「Chỉnh sửa file/folder trùng tên」 |
| F156 | Priority | 「High」 |
| G156 | TVP_ID | 「TC_144」 |
| H156 | Test case name/ Test view point | 「Kiểm tra chỉnh sửa tên file/folder trùng tên」 |
| I156 | Pre-condition | (trống) |
| J156 | Step | 「1. Upload/Tạo 1 file/folder có tên A ⏎ 2. Chỉnh sửa tên file/folder có tên A ⏎ 3. Kiểm tra hiển thị」 |
| K156 | Expected result | 「- Không cho phép tạo folder trùng tên và báo lỗi」 |
| L156 | Dev test | (trống) |
| M156 | Result (R1) | 「Pending」 |
| N156 | Test person (R1) | 「ThaVT」 |
| O156 | Test date (R1) | 「20/05/2026」 |
| P156 | Bug_ID (R1) | (trống) |
| Q156 | Remark (R1) | (trống) |
| R156 | Result (R2) | 「ThaVT」 |
| S156 | Test person (R2) | 「09/06/2026」 |
| T156 | Test date (R2) | 「2026-06-09」 |
| U156 | Bug_ID (R2) | (trống) |
| V156 | Remark (R2) | (trống) |
| W156 | Open question | (trống) |
| X156 | UC | (trống) |

### TC_146 · Document!R158

| Ô | Cột | Nguyên văn |
|---|---|---|
| A158 | No. | 「146」 |
| B158 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C158 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D158 (ô gộp D155:D162, giá trị ở ô neo) | III | 「Thông tin dữ liệu」 |
| E158 | IV | 「Di chuyển file/folder trùng tên」 |
| F158 | Priority | 「High」 |
| G158 | TVP_ID | 「TC_146」 |
| H158 | Test case name/ Test view point | 「Kiểm tra Di chuyển file/folder trùng tên」 |
| I158 | Pre-condition | (trống) |
| J158 | Step | 「1. Di chuyển file/folder trùng tên ⏎ 2. Kiểm tra hiển thị」 |
| K158 | Expected result | 「- Hiển thị thêm Số thứ tự」 |
| L158 | Dev test | (trống) |
| M158 | Result (R1) | 「Pending」 |
| N158 | Test person (R1) | 「ThaVT」 |
| O158 | Test date (R1) | 「20/05/2026」 |
| P158 | Bug_ID (R1) | (trống) |
| Q158 | Remark (R1) | 「Passed」 |
| R158 | Result (R2) | 「ThaVT」 |
| S158 | Test person (R2) | 「09/06/2026」 |
| T158 | Test date (R2) | 「2026-06-09」 |
| U158 | Bug_ID (R2) | (trống) |
| V158 | Remark (R2) | (trống) |
| W158 | Open question | (trống) |
| X158 | UC | (trống) |

### TC_150 · Document!R162

| Ô | Cột | Nguyên văn |
|---|---|---|
| A162 | No. | 「150」 |
| B162 (ô gộp B14:B162, giá trị ở ô neo) | I | 「Quản lý tài liệu - Library Management」 |
| C162 (ô gộp C91:C162, giá trị ở ô neo) | II | 「Chức năng tệp - File function 」 |
| D162 (ô gộp D155:D162, giá trị ở ô neo) | III | 「Thông tin dữ liệu」 |
| E162 (ô gộp E159:E162, giá trị ở ô neo) | IV | 「Upload file/folder/ZIP quá 255 ký tự」 |
| F162 | Priority | 「High」 |
| G162 | TVP_ID | 「TC_150」 |
| H162 | Test case name/ Test view point | 「Kiểm tra hiển thị thông tin thời gian tạo của dữ liệu」 |
| I162 | Pre-condition | (trống) |
| J162 | Step | 「1. Tạo file mới thành công ⏎ 2. Kiểm tra thông tin: Thời gian tạo」 |
| K162 | Expected result | 「- Hiển thị đúng thời gian đã tạo ⏎ YYYY-MM-DD HH:MM」 |
| L162 | Dev test | (trống) |
| M162 | Result (R1) | 「Pending」 |
| N162 | Test person (R1) | 「ThaVT」 |
| O162 | Test date (R1) | 「20/05/2026」 |
| P162 | Bug_ID (R1) | (trống) |
| Q162 | Remark (R1) | 「Passed」 |
| R162 | Result (R2) | 「ThaVT」 |
| S162 | Test person (R2) | 「22/05/2026」 |
| T162 | Test date (R2) | 「2026-05-22」 |
| U162 | Bug_ID (R2) | (trống) |
| V162 | Remark (R2) | (trống) |
| W162 | Open question | (trống) |
| X162 | UC | (trống) |
## D. Phần không đọc được hoặc cần lưu ý

1. openpyxl bỏ phần mở rộng Conditional Formatting và Data Validation của file khi đọc. Danh sách chọn (ví dụ cột Result) và màu tô theo điều kiện không đọc được.
2. Sheet `Cover` có 1 ảnh, chưa đọc nội dung ảnh.
3. Sheet `Test_Report` lưu giá trị lỗi `#NAME?` / `#VALUE!`: ô B4 trỏ tới sheet 「Home」, không có trong file này; nhãn phân loại ở đó là tiếng Nhật của một module khác.
4. Chuẩn Unicode không đồng nhất: 378 / 1.737 ô chữ ở hàng 13–162 không ở dạng NFC (chữ có dấu bị tách thành chữ gốc + dấu tổ hợp). Hiển thị giống nhau nhưng tìm kiếm, lọc và so chuỗi bằng máy có thể trượt. Ngoài ra có 12 ô bị dấu thừa (ví dụ 「thông bá́o」).
5. Tài liệu được dẫn chiếu nhưng không có: màn 「PM0035」 (K34) và màn 「Upload Folder/ZIP」 (K36).
