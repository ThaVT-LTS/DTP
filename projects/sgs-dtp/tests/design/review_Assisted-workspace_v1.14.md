# Review sheet Assisted workspace — SGS-DTP_TestCase1_v1.14_Assisted-workspace.xlsx

v0.1 · 09/10/2026 · Opus review, chỉ liệt kê lỗi, không sửa (Sonnet sửa khi Hanna bảo "làm lại").
Phạm vi: sheet Assisted workspace (122 TC, Assisted workspace_001 → _122), `khung-case-cha_Evidence-Assisted.md`, `cau-hoi_Assisted-workspace.md`, FB-065, FB-066.
Đối chiếu: 36 mục của `review_Assisted-workspace_v1.13.md`, sheet Workspaces và Scopes của cùng file. Lần này không mở lại UC, Figma, hệ thống.
Số TC trong ngoặc là 3 số cuối của TVP_ID theo bản v1.14 (số đã đổi so với v1.13).

**Phân loại 18 mục (rule 39, bổ sung sau nhận xét của Hanna 17:28):** chưa sửa hết 4 (mục 1, 2, 3, 4) · phát sinh do bản sửa 6 (mục 6, 13, 15, 16, 17, 18) · sót từ vòng trước 8 (mục 5, 7, 8, 9, 10, 11, 12, 14 — các lỗi này đã có ở v1.13, vòng review trước lẽ ra phải báo).

## A. Mục của review v1.13 chưa sửa hết

1. Mục 7 (Expected "from Medium" không có nguồn) lặp lại ở (104): Expected "Cây có requirement nhãn from Basic và from Medium", trong khi (034) đã để trống vì Q-EA-08 chưa trả lời.
2. Mục 28 (Expected "như Customer Admin" không kiểm được bằng mắt) mới sửa ở (111). Case Customer Viewer (115) vẫn ghi "Hiển thị cây requirement và chi tiết requirement".
3. Mục 35 (cột UC theo thao tác) còn (072): kiểm coverage ở màn Workspaces sau khi upload nhưng cột UC là UC-WSP-02, trong khi (073), (092), (096) đã đổi sang mã của thao tác.
4. Mục 15 (nhóm 1 có 11 hay 6 requirement): Q-EA-45 chỉ gắn ở (071), (091). Ba case (011), (012), (013) cũng dựng dữ liệu "nhóm 1 Access Control (11 requirement)" mà không gắn câu hỏi.
5. Mục 22, 23 (một mã gộp nhiều câu hỏi, mỗi case chỉ cần một vế): đã tách Q-EA-25, 27, 34, nhưng cùng kiểu lỗi còn ở:
   - Q-EA-20 (độ dài Name; Name chỉ có khoảng trắng): (059) chỉ cần vế 2, (060) chỉ cần vế 1.
   - Q-EA-21 (file đúng 20 MB; câu báo lỗi khi lớn hơn 20 MB): (062) chỉ cần vế 1, (063) chỉ cần vế 2.
   - Q-EA-31 (có hộp thoại xác nhận; thông báo sau khi gỡ): (097) cần vế 1, (093) cần cả hai.

## B. Lỗi mới hoặc review v1.13 bỏ sót

6. Q-EA-03 vẫn lấy căn cứ "Partial tính 0,5 chia 6 requirement" (Figma 6 dòng), trong khi sheet đã chuyển sang nhóm 1 có 11 requirement, và Q-EA-45 lại hỏi đúng điều này. Hai câu đang dựa vào hai số khác nhau cho cùng một nhóm.
7. (099) Expected "Danh sách chỉ có người được vào scope [System] (Linh Tran)" mâu thuẫn với dữ liệu ở case khác: (101) có Wei Chen cũng được gán scope [System], và (115) → (119) có Customer Viewer được gán scope [System]. Expected cũng phụ thuộc Q-EA-34 (Customer Viewer có trong danh sách không). Pre-condition chưa nói rõ những ai được gán scope [System].
8. Tài khoản Customer User không được nêu tên ở (111) → (114), (120). Cả Wei Chen và Mei Lin đều là Customer User, mà (099) lại dựng dữ liệu "Mei Lin không được gán scope [System]". Nếu dùng Mei Lin thì Pre-condition "được gán scope [System]" của (111) → (114) sai.
9. Q-EA-31 (có hộp thoại xác nhận trước khi gỡ không) làm đổi bước và Expected của mọi case gỡ liên kết (094), (095), (096), nhưng chỉ gắn ở (093) và (097).
10. (112) Bước 2 chỉ "Kiểm tra khối Expected evidence", nhưng Expected có thêm "Mở chi tiết evidence có nút Unlink from <requirement>" (không có bước mở chi tiết evidence). Case cũng gộp ba thao tác Upload, Link, Gỡ (rule 9, 12).
11. (113), (118) "Ô Owner màu xám, không mở được danh sách chọn" chỉ lấy từ hệ thống, Figma không có ô Owner (Q-EA-33). Đây cùng kiểu với lỗi (079) "nút Link xám" của bản 1.13 (nay đã có Q-EA-43), nhưng hai case này chưa gắn câu hỏi.
12. Q-EA-33 hỏi "có ô Owner không và chưa gán thì hiện gì", tức là làm đổi Expected của mọi case Owner (100), (101), (113), (114), (118), (119), nhưng chỉ gắn ở (098). (098) Expected "chưa chọn người nào" bỏ mất chữ "Nobody yet" mà hệ thống đang hiện (ghi ngay trong Q-EA-33).
13. (109) Bước 2 "Bấm icon mắt ở dòng evidence dưới một expected evidence": không có dữ liệu cụ thể (rule 31), Pre-condition chỉ ghi "đã có evidence".
14. (085) Expected để trống, nhưng câu hỏi kèm (Q-EA-32) chỉ hỏi tên gọi của dòng phụ. Việc evidence đã gỡ có hiện trong danh sách hay không thì hệ thống đã cho thấy ("not linked yet"), nên phần này viết được Expected, không cần để trống cả case (rule 13).
15. Mã câu hỏi được dùng lại với nghĩa mới: ở v1.13, Q-EA-38 là "Not mapped hay Not linked ở danh sách Link", sang v1.14 là "chữ hoa ở ô tìm kiếm". Q-EA-27 cũng đổi nghĩa. Hanna đã đọc bản v1.13 sẽ hiểu sai nếu trả lời theo mã cũ. File câu hỏi có ghi lại, nhưng sheet và Cover thì không.

## C. Khung case cha, FB

16. `khung-case-cha_Evidence-Assisted.md` mục 2, dòng Workspaces Q-W-11 ghi "Q-W-11 vẫn còn ở case Gắn framework theo vai trò (sheet Scopes)". Thực tế Q-W-11 nằm ở Workspaces_041 (sheet Workspaces, "Customer Admin thấy workspace của mọi scope"), không có ở sheet Scopes.
17. Rule 38 (tự soát trước khi giao): FB-066 và khung case cha không ghi đã chạy checklist tự soát. Các lỗi 1 → 4 thuộc đúng loại "sửa một chỗ, không rà các case cùng kiểu" mà checklist dùng để bắt.
18. Bảng ba nguồn ghi "Hệ thống chỉ có workspace Appendix 10 · 2022 · Medium (61 requirement) và Basic (44)", nhưng (035) dùng [Workspace ISO] ISO/IEC 27001 · 2022 và Q-EA-01 ghi hệ thống có workspace "6 of 31" (ISO 22301). Câu "chỉ có" không đúng, nên ghi hệ thống có những workspace nào.

## Đã kiểm, không có lỗi
- tc_check: 2 sheet, 0 lỗi, 0 cảnh báo (Sonnet đã chạy; Opus đọc kết quả, không chạy lại).
- 31 TC để trống Expected đều có Open question; 48 mã Q-EA đều có ít nhất một TC.
- Các mục 1, 2, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 29, 30, 31, 32, 33, 36 của review v1.13 đã sửa hoặc đã ghi lại; mục 3, 4, 34 được ghi là chưa làm ở `docs/VIEC-CON-MO.md`.
- Phép tính mới: 3/11 = 27,3% → 27% (011); 11/11 → 100% (012).
- Sheet Assisted workspace đã nằm sau Workspaces; Cover có dòng 1.14 dẫn FB-066; FB-065, FB-066 có trong `feedback/log.md` và bảng tra nhanh.
