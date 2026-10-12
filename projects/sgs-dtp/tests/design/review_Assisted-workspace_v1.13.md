# Review sheet Assisted workspace — SGS-DTP_TestCase1_v1.13_Assisted-workspace.xlsx

v0.1 · 09/10/2026 · Opus review, chỉ liệt kê lỗi, không sửa (Sonnet sửa khi Hanna bảo "làm lại").
Phạm vi: sheet Assisted workspace (114 TC, Assisted workspace_001 → _114) và 1 ô đổi ở sheet Workspaces (dòng 55, case Customer Viewer).
Nguồn đối chiếu: UC v5.3 (P1 Use Cases R40–R47, R39; Decision log D5, D7, D8, D21, D41, D43, D44; Open Questions), Figma SGS-DTP-DS trang "Screens · 05 Workspaces & Evidence" (6 frame), prototype với Customer Admin, Customer User, Customer Viewer.
Số TC trong ngoặc là 3 số cuối của TVP_ID.

## A. Quy trình (CLAUDE.md, rule 35–38)

1. Chưa có bản ghi FB-065 trong `feedback/log.md`, nhưng Cover dòng 1.13 (hai dòng) đã dẫn FB-065 (rule 35).
2. Chưa có file khung case cha cho module 07: thiếu bảng "ba nguồn nói gì" (rule 36) và bảng "màn đã làm bị ảnh hưởng" (rule 37). Sheet đã giao trước khi có hai bảng này.
3. Rule 36: sheet "Changes vs Source" của UC v5.3 chưa đọc, và cũng chưa ghi lại là "chưa đọc".
4. Rule 37, chưa rà các màn đã làm:
   - Workspaces: Q-W-08 (chi tiết workspace kiểm ở sheet nào) nay đã có sheet Assisted workspace nhưng câu hỏi vẫn để nguyên; Q-W-11 đã bỏ ở case Customer Viewer nhưng chưa ghi lại ở danh sách câu hỏi hay sheet Cần xác nhận.
   - Scopes: Scope_107 với Q-S-20 (workspace mới hiện ở màn Workspaces) chưa đối chiếu với case 007 (workspace mới 0 of 61, mọi requirement Missing).
   - Users / Scopes: UC D43 (người mất quyền vào scope thì requirement và evidence họ sở hữu được giao lại hoặc bỏ trống) không có case ở đâu và cũng chưa ghi là sẽ kiểm ở sheet Users.
   - Prototype có nút Request certification ở chi tiết workspace (chỉ Customer Admin), UC WSP-03 có "Request support"; cả hai chưa được ghi là kiểm ở sheet nào.
5. Thứ tự sheet: Assisted workspace nằm trước Workspaces, ngược với thứ tự đi màn (Workspaces → chi tiết).
6. 39 câu hỏi Q-EA chưa được đưa vào sheet Cần xác nhận hay một file câu hỏi (các module trước có `cau-hoi_Scopes.md`, mục câu hỏi ở khung case cha).

## B. Expected viết khi chưa có nguồn hoặc mâu thuẫn với câu hỏi đang mở (rule 1, 13)

7. (034) Expected "from Medium" không có nguồn nào: Figma và hệ thống chỉ có "from Basic", mà Q-EA-08 lại hỏi đúng điều này.
8. (029) Expected "Cây chỉ còn R.1.1.4 (chip Partial)", trong khi (016) và (013) để trống vì chưa biết khi nào Partial (Q-EA-03). Dữ liệu "R.1.1.4 có hai expected evidence bắt buộc" (016, 043) là tự đặt ra, không nguồn nào cho thấy.
9. (101) Expected "không có requirement chỉ thuộc tier High" chính là câu trả lời cho Q-EA-04 (ẩn hay hiện Out of scope), trong khi (017) để trống và gắn cùng câu hỏi đó. Bước của (017) "tìm trong cây một requirement chỉ thuộc tier High" mâu thuẫn với Expected của (101).
10. (085) Expected "không có evidence của workspace khác dù cùng scope" theo câu chữ Figma, nhưng UC EVC-09 gắn evidence với scope; xung đột này nằm trong Q-EA-27 mà (085) không gắn câu hỏi.
11. (062) Expected "File không được nhận, không có dòng file" là tự suy đoán: không nguồn nào nói file quá 20 MB bị chặn ngay lúc chọn hay lúc bấm Upload.
12. (079) "Nút Link màu xám" chỉ lấy từ hệ thống, Figma không có trạng thái này và không có câu hỏi kèm.
13. (060) Định dạng "big-ok.pdf · 19.99 MB" chưa có nguồn: Figma chỉ có dòng "Scanning for viruses… · 402 KB", và Expected bỏ mất phần "Scanning for viruses…".

## C. Dữ liệu và con số (rule 31)

14. (011), (012), (013) Pre-condition "nhóm [Group] có 4 requirement" thuộc Appendix 10 · 2022 · Medium chưa kiểm là có thật. Nhóm có 4 requirement mà hệ thống cho thấy là nhóm 4 của ISO 22301 · 2019, không phải Appendix 10. Nhóm 1 của Appendix 10 Medium trên hệ thống có 11 requirement.
15. (070), (089) dùng nhóm 1 có 11 requirement (số từ hệ thống), nhưng Figma (cùng workspace Appendix 10 · 2022 · Medium) chỉ cho thấy 6 dòng ở nhóm 1 với 58%. Chưa ghi nguồn của số 11 và chưa nêu hai nguồn lệch nhau.
16. (102) Con số 76 requirement cho tier High lấy từ sheet Frameworks, chưa thấy trên Figma hay hệ thống (hệ thống không có workspace High). Cần ghi nguồn hoặc thêm câu hỏi.
17. (103) Bước 1 mở [Workspace] (Appendix 10 Medium), nhưng Pre-condition lại là "workspace của framework có requirement retired", tức là workspace khác.

## D. Câu hỏi đặt sai chỗ, trùng hoặc gộp (rule 23)

18. Q-EA-16 (ở 052) có vế "Valid until trước Valid from thì báo lỗi gì", trùng hẳn với Q-EA-23 (ở 065).
19. Q-EA-38 (083) và Q-EA-32 (094) cùng hỏi chuyện "Not mapped" hay "Not linked".
20. Q-EA-27 gộp 4 câu hỏi (evidence Not mapped từ Library; evidence đã gắn requirement này; Blocked hoặc Scanning; một workspace hay một scope) nhưng chỉ gắn ở (084). Các vế còn lại làm đổi Expected của (083) và (085).
21. Q-EA-24 (gắn vào expected evidence nào của requirement kia) làm đổi Expected của (073), nhưng chỉ gắn ở (066).
22. Q-EA-34 gộp 3 câu hỏi (Customer Viewer có trong danh sách không; bỏ owner được không; có gửi thông báo không). Không có case nào cho việc bỏ owner hay thông báo, nên hai vế này không làm đổi Expected của case nào.
23. Q-EA-25 có hai câu hỏi trong một mã ("…bị chặn không? Test bằng scanner thật hay file mẫu nào?").
24. (022) dùng lại mã Q-S-07 của sheet Scopes với nội dung "có phân biệt chữ hoa không". Chưa kiểm câu Q-S-07 gốc ở Scopes hỏi gì. Sheet Workspaces cũng đã gắn Q-S-07 cho ba câu hỏi khác nhau (dòng đếm, chữ hoa, câu không có kết quả), nên một mã đang mang nhiều nghĩa.
25. Q-EA-06 có vế "không phân biệt chữ hoa" trùng với câu hỏi của (022).

## E. Step và Expected không khớp (rule 9, 12)

26. (075) Bước 4 kiểm "dòng evidence và chip requirement", nhưng Expected chỉ có dòng evidence.
27. (104) Một case gộp 4 thao tác (Upload, Link, Unlink, Owner) trong workspace Archived; theo rule 9 mỗi thao tác một case.
28. (105) Expected "như Customer Admin" không kiểm được bằng mắt; cần liệt kê điều thấy được.
29. (014) trùng một phần với (007) (cùng dữ liệu workspace rỗng, cùng kiểm chip Missing của mọi requirement).
30. (014), (015) Mô tả chip sai với Figma: chip Missing có icon tròn đỏ dấu "!", không phải "chấm đỏ".
31. (077) "Upload lại file đã có" đặt dưới Classification II "Trạng thái quét", không đúng nhóm.

## F. Thiếu phủ UC

32. UC EVA-02 ghi "Text, tier, source, owner, expected evidence and linked documents". Trường "source" không có case nào, cũng không có câu hỏi nó là gì (nhãn "from Basic" là tier).
33. EVA-02 với Customer User và Customer Viewer: chưa có case kiểm họ thấy tên owner đã gán (105–111 chỉ kiểm không đổi được).
34. UC D43 (xem mục 4): không có case, không có ghi chú chuyển sang sheet khác.

## G. Cột UC

35. Các case kiểm kết quả ở Evidence Library sau một thao tác của module 07 ghi UC-EVC-01: (072) upload, (090) link, (094) gỡ. Theo rule 27, case nằm ở sheet của thao tác thì cột UC nên là UC của thao tác (EVA-03, EVA-04, EVA-05).
36. Kiểu mã UC mới (UC-EVA-01, 2 chữ số) khác các sheet trước (UC-WSP-002, 3 chữ số), mà không có ghi chú lý do.

## Đã kiểm, không có lỗi
- tc_check: 2 sheet, 0 lỗi, 0 cảnh báo.
- Sheet Workspaces chỉ đổi đúng 2 ô K55 và W55 so với v1.12; các sheet khác không đổi ô nào.
- Các con số tính lại khớp: 38/61 = 62%, 1/61 → 2%, 2/61 → 3%, 1/11 → 9%, 2/11 → 18% (cách làm tròn giống 74/116 → 64% ở Workspaces).
- Văn bản lấy từ Figma (hộp thoại Upload, Link existing evidence, chi tiết evidence, Documents) khớp với frame.
