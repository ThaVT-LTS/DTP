# Rule — Viết test case (tc-authoring)

Phiên bản: v0.3 · Nạp cùng `rules/common.md`, `rules/feedback.md`, `rules/tester.md` khi viết hoặc sửa file test case. Quy trình chi tiết: skill `tc-authoring`.

Rule này nói về **file test case bàn giao được**: tổ chức, nội dung, và định dạng. Phần kỹ thuật thiết kế (phân vùng tương đương, bảng quyết định, chuyển trạng thái) vẫn ở `rules/tester.md` và skill `test-design`.

## A. Nguồn chân lý

1. Thứ tự ưu tiên khi ba nguồn mâu thuẫn: **tài liệu yêu cầu (UC/SRS) > bản thiết kế đã duyệt (Figma) > hệ thống đang chạy**. Prototype chỉ dùng để biết *màn nào tồn tại, nút nào tồn tại, nhãn đang dùng*; **không bao giờ** lấy hành vi của prototype làm kết quả mong đợi.
2. Mọi mâu thuẫn giữa ba nguồn phải được ghi thành câu hỏi `Q-<mã màn>-nn`, không tự chọn bên nào đúng.

## B. Tổ chức file

3. **Một màn hình một sheet.** Màn hình tính theo mục menu: danh sách, chi tiết, hộp thoại, panel mở từ cùng một mục menu mặc định nằm chung một sheet, như sheet `Scopes` gồm cả Danh sách và Chi tiết; phần nào đủ lớn thì tách (rule 25). Tên sheet lấy đúng tên mục menu của hệ thống, không dịch, không viết tắt; sheet tách ra thì lấy tên màn như trên giao diện. Vai trò, gộp và tách: mục G.
4. Trong sheet, TC xếp theo **khu vực**; thứ tự khu vực theo mắt đọc: trên → dưới trong một cột, hết cột trái sang cột phải. Màn có danh sách thì xếp theo vòng đời dữ liệu trước: mở màn → trạng thái rỗng (Empty state) → tạo mới → các khu vực cần có dữ liệu (bảng, tìm kiếm, lọc, phân trang); trong từng chặng vẫn theo mắt đọc.
5. **Luồng nghiệp vụ xuyên màn** có sheet riêng `FLOW-nn`, không nhét vào sheet màn hình. Mỗi bước trong luồng ghi rõ màn hình thực hiện.
6. Đầu mỗi sheet có khối thông tin: tên chức năng · tên màn · người viết · ngày tạo · nguồn tham chiếu.

## C. Bốn cấp Classification

7. Bốn cột, đúng thứ tự, không đổi nghĩa giữa các sheet:

| Cấp | Nội dung | Ví dụ |
|---|---|---|
| **I** | Feature — khối chức năng người dùng gọi tên được | `Login` |
| **II** | Khu vực trên màn, hoặc nhóm kiểm | `Email` · `Security` |
| **III** | Mục kiểm, hoặc nhóm kết quả | `Success` · `Failure` · `Validation` |
| **IV** | Case cụ thể, mỗi dòng một case | `Empty` · `Invalid format` |

Ví dụ trên là file TC tiếng Anh. Mỗi ô ghi một thứ tiếng theo ngôn ngữ của file (rule 16), vd `Login`, không ghi `Đăng nhập - Login`. Tên nhóm kiểm dùng bảng từ cố định ở `references/format.md` §7.

8. **Xếp case sao cho cùng nhóm kết quả nằm liền nhau.** Thành công hết rồi mới tới Không thành công. Xen kẽ thì không gộp ô được, và người đọc mất mạch.
9. Một hành động hiện ở n nơi thì viết **n case riêng**, cùng tiền điều kiện, khác các bước. Không gộp nhiều nơi vào một ô kết quả mong đợi.

## D. Nội dung một dòng

10. Mỗi TC có đúng một `UC_ID`. Không map được thì ghi `[NGOÀI UC]` kèm lý do, không để trống.
11. `TVP_ID` duy nhất trong sheet, theo mẫu `TC_nnn`. Tham chiếu từ ngoài dùng `<tên sheet>_TC_nnn`. ID đã bỏ không dùng lại.
12. Kết quả mong đợi phải **quan sát được**: text nguyên văn, màn hình đích, trạng thái, dữ liệu thay đổi. Cấm "hoạt động bình thường", "hiển thị đúng", "thành công" mà không nói thấy gì; tiếng Anh cũng vậy, vd "works normally", "displays correctly", "as expected".
    - Ghi thẳng trong ô: không trỏ sang TC khác ("giống TC_006"), không ghi "ở cả hai màn" mà không nêu tên từng màn.
    - Từ hai mục trở lên (cột, trường, lựa chọn, nút) thì mỗi mục một dòng `- <mục>`, không nối bằng " · "; chỉ giữ " · " khi đó là chữ thật trên giao diện.
13. **Chưa có căn cứ thì để trống kết quả mong đợi**, ghi câu hỏi vào cột `Open question`, tô đỏ dòng đó. Tự đặt text chưa ai duyệt sẽ tạo bug giả: tester báo lỗi, dev trả lời "đúng thiết kế", bộ test mất uy tín.
14. **Viết bằng chữ, cho Tester đọc là chạy được.**
    - Dòng đăng nhập ở Pre-condition: file TC tiếng Anh ghi `Logged in as <role>`, vd `Logged in as Customer Admin`; màn không cần đăng nhập ghi `Not logged in`. File TC tiếng Việt ghi `Đăng nhập với acc <vai trò>` và `Chưa đăng nhập`.
    - Dữ liệu ghi thẳng giá trị cụ thể, nhãn giao diện ghi đúng nguyên văn, ngay trong ô của TC.
    - Step là thao tác cụ thể, vd `1. Click a scope in the list`, `2. Observe the scope detail`; không ghi chung chung kiểu "Mở …". Chưa biết thao tác hay kết quả thì để trống và ghi câu hỏi (rule 13).
15. Mỗi khu vực có thao tác ghi dữ liệu phải có đủ: ít nhất một case Thành công, một case Không thành công, một case Phân quyền, một case Bảo mật (file tiếng Anh: Success, Failure, Permission, Security). Case Bảo mật là case tester làm được trên giao diện hoặc trình duyệt; case cần gọi thẳng API theo rule 29.

## E. Đa ngôn ngữ

16. **Ngôn ngữ của file TC theo dòng "Ngôn ngữ viết file TC" trong `profile.md` của dự án**, áp cho mọi sheet, mọi cột; phần ngoại lệ (vd cột `Open question` và sheet `Cần xác nhận` viết tiếng Việt) cũng ghi ở dòng đó. Nhãn giao diện luôn ghi đúng nguyên văn theo ngôn ngữ hệ thống đang chạy, kể cả chữ hoa chữ thường, vd `Create scope`. Khi chuyển ngôn ngữ cho bộ TC có sẵn:
    - chỉ dịch chuỗi **có căn cứ** — bảng đối chiếu thật, hoặc danh sách phần tử đã duyệt;
    - chuỗi chưa có bản dịch chính thức thì **giữ nguyên gốc**, tô đỏ, ghi vào cột `Open question`;
    - dịch theo thứ tự **chuỗi dài trước, chuỗi ngắn sau**, nếu không chuỗi ngắn sẽ cắt nát chuỗi dài.
17. Dịch chỉ đổi **ngôn ngữ**, không đổi **hành vi**. TC nào sai hành vi so với thiết kế mới thì dịch xong vẫn sai — phải liệt kê riêng.

## F. Định dạng file

18. **Phông chữ: Times New Roman, cỡ 10** cho toàn bộ vùng dữ liệu.
19. **Căn lề trái** cho mọi ô. Ô đã gộp và ô dữ liệu căn giữa theo chiều dọc, như file TC mẫu.
20. **Quy tắc gộp ô** cho bốn cột Classification:
    - gộp các dòng **liền nhau có cùng giá trị**; ô trống nghĩa là "giống dòng trên";
    - cụm con **không được vượt ranh giới cụm cha** — cột III đổi cụm thì cột IV phải cắt theo;
    - cụm chỉ một dòng thì không gộp;
    - chỉ ô neo giữ giá trị, các ô còn lại để trống.
21. Người viết làm việc trên **bảng phẳng** (giá trị lặp lại ở mọi dòng); việc gộp ô do script làm lúc xuất file. Không sửa tay trên file đã gộp — ô gộp không lọc được, không sort được, copy xuống là vỡ.

22. **Định dạng đồng nhất toàn bộ.** Mọi sheet trong một file và mọi file test case của dự án dùng **một** phông (Times New Roman 10) và **một** bảng màu khai ở `references/format.md` §4: màu hàng tiêu đề, màu nhãn, màu dòng còn câu hỏi mở, màu đường kẻ. Không dùng màu hay phông ngoài bảng đó; cần thêm thì sửa bảng màu và script trước. Sheet phụ (`Cover`, `Hướng dẫn`, `FLOW-nn`, `Test_Report`) theo cùng quy ước với sheet màn hình.
23. Cột ghi chuỗi hoặc câu hỏi còn thiếu của một dòng tên là **`Open question`** (trước đây: `Chờ text`). Nội dung ghi mã câu hỏi `Q-<mã màn>-nn` kèm tóm tắt điều cần xác nhận.
24. **Form theo file mẫu của dự án.** Dự án có file TC mẫu (ghi ở `profile.md`, dòng "File TC mẫu của dự án") thì file bàn giao là chính file đó: sheet mới được **thêm vào file mẫu, ngay cạnh một sheet TC đã duyệt, bằng cách nhân bản form của sheet ấy** — khối thông tin, khối tổng kết, hàng tiêu đề, độ rộng cột, căn lề, đường kẻ, dropdown, trang in. Không dựng lại form bằng script tự vẽ.
    - Bố cục của file mẫu khác rule 18–19 hoặc `references/format.md` §1–§3 ở đâu thì **theo file mẫu**, và ghi điểm khác thành câu hỏi cho người dùng.
    - Phông và màu vẫn theo rule 22. Bảng màu lấy **một** màu nền tiêu đề của file mẫu; file mẫu có ô lệch (màu khác, phông khác) thì đưa cả file mẫu về chuẩn trước khi dùng làm mẫu.
    - Dự án chưa có file mẫu thì hỏi người dùng trước khi bàn giao; file dựng bằng form mặc định chỉ là bản tạm.

## G. Chia sheet

24. **Không chia sheet theo vai trò.** Màn nhiều vai trò dùng, hoặc có ở nhiều portal, vẫn là một sheet. Vai trò nằm trong sheet:
    - Pre-condition của mọi TC mở đầu bằng dòng đăng nhập theo rule 14 (`Logged in as <role>` hoặc `Not logged in`; file tiếng Việt: `Đăng nhập với acc <vai trò>`, `Chưa đăng nhập`), kể cả khi đã có điều kiện dữ liệu. Lọc cột Pre-condition theo tên vai trò là ra danh sách chạy của vai trò đó, nên tên vai trò ghi đúng như tài liệu yêu cầu.
    - Khác biệt giữa các vai trò viết ở nhóm Phân quyền cuối sheet (rule 15).
    - Chức năng có màn ở nhiều portal thì thêm tên portal vào đầu Classification I, vd `[SGS] Certification list`.
    - Ngoại lệ: màn mà mỗi vai trò thấy một nội dung khác hẳn, vd dashboard theo vai trò, thì Classification I là vai trò.
25. **Gộp, tách theo màn hình, không theo module của UC list.** Module chỉ để tham khảo; việc nối TC về UC do cột UC của từng dòng đảm nhận.
    - Hai module nằm trên cùng một màn thì gộp một sheet. Một module trải qua nhiều màn lớn thì tách theo màn.
    - UC do System thực hiện mà không có màn riêng thì không có sheet riêng; kiểm ở nơi kết quả hiện ra, vd ghi vết kiểm ở nhóm Ghi vết của sheet có hành động.
    - Màn chưa có thiết kế thì chưa tạo sheet. UC chưa chốt có làm hay không thì chưa viết TC. UC đã chốt nhưng còn câu hỏi chi tiết thì vẫn viết, phần còn mở ghi `Open question` (rule 13).
    - Sheet nhỏ không sao; sheet trộn nhiều màn không liên quan thì tách.
26. **Một form chỉ test đầy đủ ở một sheet**, là sheet của màn chủ của form. Đường vào form từ màn khác chỉ kiểm mở đúng form và giá trị điền sẵn.
27. **TC điểm hiển thị đặt ở sheet của hành động** (rule 9), kể cả khi điểm đó ở màn khác hay vai trò khác: làm bằng vai trò A, tải lại trang, kiểm bằng vai trò B (pattern P5). Chuỗi nhiều hành động qua nhiều chức năng, dữ liệu tạo ngay trong luồng, thì đưa vào `FLOW-nn` (rule 5).
28. **Cover có bảng UC → sheet.** Mỗi UC của baseline đúng một dòng; cột Sheet ghi một trong ba: tên sheet · `Chờ: <lý do>` · `Kiểm ở: <sheet>`. Cột UC của TC dùng ID của baseline hiện hành, không dùng ID của nguồn cũ; baseline đổi ID thì đổi theo trước khi chia lại sheet.
29. **TC chỉ viết những gì tester làm được bằng công cụ đang có.** TC gọi thẳng API chỉ viết khi `profile.md` của dự án ghi tester được gọi API, và đặt ở sheet `API` riêng, không trộn vào sheet màn hình. Mở trang bằng URL, xem mã trang hay xem tab Network trên trình duyệt vẫn tính là thao tác giao diện. TC bảo mật làm được trên giao diện giữ ở cuối sheet màn hình.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.3 | 2026-10-05 | Rule 3: "màn hình" tính theo mục menu. Rule 4: màn có danh sách xếp theo vòng đời dữ liệu, trạng thái rỗng trước. Rule 7: ví dụ tiếng Anh, mỗi ô một thứ tiếng, tên nhóm kiểm theo bảng từ. Rule 12: không trỏ sang TC khác, mỗi mục một dòng. Rule 14 viết lại theo góc nhìn Tester: dòng đăng nhập `Logged in as <role>`, dữ liệu và nhãn ghi thẳng trong ô, Step là thao tác cụ thể. Rule 15: tên nhóm tiếng Anh, case Bảo mật làm được trên giao diện. Rule 16: ngôn ngữ file TC theo `profile.md`. Rule 22 bỏ sheet `_Data`, `_Labels`. Thêm mục G: chia sheet (rule 24–28) và rule 29 — TC gọi API chỉ khi tester được gọi API, ở sheet `API` riêng. Hanna duyệt 05/10, trừ phần **chờ duyệt**: rule 3 và 24–28 (chia sheet), rule 19 (căn giữa theo chiều dọc như file mẫu, đề xuất của AI). | FB-???[chia-sheet] · FB-???[gop-tach-sheet] · FB-???[pre-condition] · FB-???[tieng-anh] · FB-???[rong-truoc] · FB-???[khong-lung-lo] · FB-???[moi-dong] · FB-???[api] · FB-013 |
| v0.3 | 2026-10-02 | Thêm rule 24: form theo file mẫu của dự án — sheet mới thêm vào file mẫu bằng cách nhân bản một sheet TC đã duyệt; bố cục theo file mẫu, phông và màu theo rule 22 với bảng màu lấy một màu nền tiêu đề của file mẫu; chưa có file mẫu thì hỏi. **Chờ duyệt.** | FB-019 · FB-016 |
| v0.2 | 2026-10-02 | Đổi tên cột `Chờ text` → `Open question` (rule 13, 16, 23). Thêm rule 22: định dạng đồng nhất toàn bộ — một phông, một bảng màu cho mọi sheet và mọi file. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: thứ tự nguồn chân lý, một màn một sheet, bốn cấp Classification, quy tắc chưa có căn cứ thì để trống, quy tắc chuyển ngôn ngữ, và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô). | FB-010 · FB-011 · FB-012 · FB-013 |
