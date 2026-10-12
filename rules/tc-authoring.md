# Rule — Viết test case (tc-authoring)

Phiên bản: v0.8 · Nạp cùng `rules/common.md`, `rules/feedback.md`, `rules/tester.md` khi viết hoặc sửa file test case. Quy trình chi tiết: skill `tc-authoring`.

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

8. **Xếp case sao cho cùng nhóm kết quả nằm liền nhau.** Xen kẽ thì không gộp ô được, và người đọc mất mạch.
    - Case mà bước cuối là bấm nút gửi (vd `Create scope`, `Save`, `Link and create workspace`) nhưng **không lưu được** — bỏ trống trường bắt buộc, chỉ có khoảng trắng, trùng tên, quá giới hạn — nằm trong nhóm **Không thành công** của khu vực, cùng các case Cancel, ×, Esc. Không lập nhóm Kiểm tra dữ liệu riêng cho các case đó.
    - Trong một khu vực, nhóm Không thành công đứng trước nhóm Thành công, theo bản `SGS-DTP_TestCase1_v1.4` do Hanna sửa. Câu cũ của rule ghi ngược lại ("Thành công hết rồi mới tới Không thành công"): **chờ Hanna chọn** thứ tự chuẩn.
9. **Kết quả của một hành động kiểm ở nơi hành động trả về**, vd tạo scope xong về danh sách thì kiểm dòng vừa tạo ở danh sách.
    - Nơi hiển thị khác **trong cùng sheet** đã có khu vực riêng (vd màn chi tiết) thì kiểm ở khu vực đó; không lặp lại ở khu vực của hành động.
    - Nơi hiển thị ở **màn khác, sheet khác** hoặc với vai trò khác thì theo rule 27.
    - Chỗ nào hiển thị khác nhau theo **loại** (vd Type: Organization, Product, System) thì mỗi loại một case.
    - Không gộp nhiều nơi vào một ô kết quả mong đợi.

## D. Nội dung một dòng

10. Mỗi TC có đúng một `UC_ID`. Không map được thì ghi `[NGOÀI UC]` kèm lý do, không để trống.
11. `TVP_ID` duy nhất trong sheet, theo mẫu `TC_nnn`. Tham chiếu từ ngoài dùng `<tên sheet>_TC_nnn`. ID đã bỏ không dùng lại.
    - **Chờ duyệt** (theo cách Hanna làm ở bản v1.4): sheet chưa có kết quả chạy nào ở cột Result thì được đánh lại `No.` và `TVP_ID` cho liền mạch theo thứ tự trên sheet, kèm bảng đối chiếu số cũ → số mới và sửa mọi chỗ trỏ tới số cũ. Đã có kết quả chạy thì không đánh lại; case mới lấy số kế tiếp.
12. Kết quả mong đợi phải **quan sát được**: text nguyên văn, màn hình đích, trạng thái, dữ liệu thay đổi. Cấm "hoạt động bình thường", "hiển thị đúng", "thành công" mà không nói thấy gì; tiếng Anh cũng vậy, vd "works normally", "displays correctly", "as expected".
    - Ghi thẳng trong ô: không trỏ sang TC khác ("giống TC_006"), không ghi "ở cả hai màn" mà không nêu tên từng màn.
    - Từ hai mục trở lên (cột, trường, lựa chọn, nút) thì mỗi mục một dòng `- <mục>`, không nối bằng " · "; chỉ giữ " · " khi đó là chữ thật trên giao diện.
13. **Chưa có căn cứ thì để trống kết quả mong đợi**, ghi câu hỏi vào cột `Open question`, tô đỏ dòng đó. Tự đặt text chưa ai duyệt sẽ tạo bug giả: tester báo lỗi, dev trả lời "đúng thiết kế", bộ test mất uy tín.
    - Kết quả do người viết **suy ra** mà UC, Figma không nêu (vd dữ liệu vừa tạo sẽ có trong một danh sách chọn, tên mới sẽ hiện ở một màn khác) cũng là chưa có căn cứ: không viết thành câu khẳng định. Để trống và hỏi, hoặc bỏ case nếu nơi hiển thị đó đã có case riêng.
    - Expected có nội dung nhưng dựa trên điều **chưa kiểm chứng** (chỉ đọc ở mã nguồn prototype, chưa bấm thử, hoặc khác với hệ thống đang chạy) thì phải kèm câu hỏi tương ứng ở `Open question`; không để case trông như đã kiểm xong.
    - **Câu hỏi đã có trả lời thì xoá câu hỏi**: người dùng đã trả lời, nguồn khác đã nêu, hoặc case khác đã kiểm ra kết quả. Xoá chữ ở `Open question`, bỏ tô màu ô, điền Expected theo câu trả lời. Cột `Open question` chỉ còn câu hỏi chưa có trả lời.
14. **Viết bằng chữ, cho Tester đọc là chạy được.**
    - Dòng đăng nhập ở Pre-condition: file TC tiếng Anh ghi `Logged in as <role>`, vd `Logged in as Customer Admin`; màn không cần đăng nhập ghi `Not logged in`. File TC tiếng Việt ghi `Đăng nhập với acc <vai trò>` và `Chưa đăng nhập`.
    - **Pre-condition chỉ ghi trạng thái cần có trước khi vào màn hình đang test** (đăng nhập bằng vai trò nào, dữ liệu đã dựng). Không ghi "mở màn hình đang test" vào Pre-condition: việc đó là **Step 1**. Một sheet test một màn hình, nên TC chỉ tập trung vào màn đó. Ví dụ sheet Scopes: Pre-condition `Logged in as Customer Admin`; Step 1 `Open the Scopes screen`.
    - Muốn tới màn B mà phải làm nhiều thao tác dữ liệu ở màn A (tạo dữ liệu, chọn, gắn…) thì Pre-condition mới ghi các thao tác ở màn A, **liệt kê từng thao tác kèm giá trị cụ thể** (vd `On Scopes, create scope: Type Organization, Name abc, What is in scope abc`). Step vẫn bắt đầu bằng mở màn B, rồi các thao tác tiếp theo trên màn B.
    - Dữ liệu ghi ngay trong ô của TC, nhãn giao diện ghi đúng nguyên văn. Không dùng dạng `{{…}}`.
        - Dữ liệu **tester tự nhập** thì ghi giá trị cụ thể, vd `Name: abc`.
        - Dữ liệu **phải có sẵn trên hệ thống mà dự án chưa xác định** (tên một scope có sẵn, tên khách hàng, người dùng, framework…) thì viết chung chung, tên đặt trong ngoặc vuông, vd `Belongs to organisation: [Organization]`, `Belongs to product (optional): [Product]`. Một tên ngoặc vuông dùng cùng một nghĩa trong cả sheet.
        - Nhập hoặc chọn nhiều trường trong một bước thì mỗi trường một dòng `- <nhãn>: <giá trị>` dưới dòng `Nhập` (hoặc `Chọn`). Expected có ý con thì dùng `+ <ý con>` dưới dòng `- <ý>`.
        - Text nguyên văn của giao diện (lỗi, thông báo, mô tả) đặt riêng một dòng, trong ngoặc kép, sau dòng dẫn, vd `- Hiện lỗi tại Name:` rồi `"Enter a name."`.
    - Step là thao tác cụ thể, vd `1. Click a scope in the list`, `2. Observe the scope detail`; không ghi chung chung kiểu "Mở …". Chưa biết thao tác hay kết quả thì để trống và ghi câu hỏi (rule 13).
15. Mỗi khu vực có thao tác ghi dữ liệu phải có đủ: ít nhất một case Thành công, một case Không thành công, một case Phân quyền, một case Bảo mật (file tiếng Anh: Success, Failure, Permission, Security). Case Bảo mật là case tester làm được trên giao diện hoặc trình duyệt; case cần gọi thẳng API theo rule 29.

## E. Đa ngôn ngữ

16. **Ngôn ngữ của file TC theo dòng "Ngôn ngữ viết file TC" trong `profile.md` của dự án**, áp cho mọi sheet, mọi cột; phần ngoại lệ (vd cột `Open question` và sheet `Cần xác nhận` viết tiếng Việt) cũng ghi ở dòng đó. Nhãn giao diện luôn ghi đúng nguyên văn theo ngôn ngữ hệ thống đang chạy, kể cả chữ hoa chữ thường, vd `Create scope`. Khi chuyển ngôn ngữ cho bộ TC có sẵn:
    - chỉ dịch chuỗi **có căn cứ** — bảng đối chiếu thật, hoặc danh sách phần tử đã duyệt;
    - chuỗi chưa có bản dịch chính thức thì **giữ nguyên gốc**, tô đỏ, ghi vào cột `Open question`;
    - dịch theo thứ tự **chuỗi dài trước, chuỗi ngắn sau**, nếu không chuỗi ngắn sẽ cắt nát chuỗi dài.
17. Dịch chỉ đổi **ngôn ngữ**, không đổi **hành vi**. TC nào sai hành vi so với thiết kế mới thì dịch xong vẫn sai — phải liệt kê riêng.

## F. Định dạng file

18. **Phông chữ: Times New Roman, cỡ 10** cho **mọi ô của mọi sheet**: ô có chữ, ô trống đã kẻ khung, ô nằm trong cụm gộp, và kiểu mặc định của cột (để gõ vào ô mới vẫn ra đúng phông).
19. **Mọi ô chữ của bảng TC: xuống dòng (wrap text), căn giữa theo chiều dọc, căn trái**, để chữ dài không bị che. Áp cho cả ô neo của cụm gộp ở bốn cột Classification (B–E), và các cột Name, Pre-condition, Step, Expected, Open question. Cột No. theo file mẫu (căn giữa). Script dựng sheet phải đặt sẵn; `tc_check.py` báo lỗi ô sai (ô trong cụm gộp không phải ô neo thì bỏ qua, vì Excel lấy căn lề của ô neo).
20. **Quy tắc gộp ô** cho bốn cột Classification:
    - gộp các dòng **liền nhau có cùng giá trị**; ô trống nghĩa là "giống dòng trên";
    - cụm con **không được vượt ranh giới cụm cha** — cột III đổi cụm thì cột IV phải cắt theo;
    - cụm chỉ một dòng thì không gộp;
    - chỉ ô neo giữ giá trị, các ô còn lại để trống.
21. Người viết làm việc trên **bảng phẳng** (giá trị lặp lại ở mọi dòng); việc gộp ô do script làm lúc xuất file. Không sửa tay trên file đã gộp — ô gộp không lọc được, không sort được, copy xuống là vỡ.

22. **Định dạng đồng nhất toàn bộ.** Mọi sheet trong một file và mọi file test case của dự án dùng **một** phông (Times New Roman 10) và **một** bảng màu khai ở `references/format.md` §4: màu hàng tiêu đề, màu nhãn, màu dòng còn câu hỏi mở, màu đường kẻ. Không dùng màu hay phông ngoài bảng đó; cần thêm thì sửa bảng màu và script trước. Sheet phụ (`Cover`, `Hướng dẫn`, `FLOW-nn`, `Test_Report`) theo cùng quy ước với sheet màn hình.
23. Cột ghi chuỗi hoặc câu hỏi còn thiếu của một dòng tên là **`Open question`** (trước đây: `Chờ text`). Nội dung ghi mã câu hỏi `Q-<mã màn>-nn` kèm tóm tắt điều cần xác nhận.
    - Mỗi phần trong ô là **một câu hỏi thật**: kết thúc bằng dấu `?`, nói rõ cần quyết điều gì (theo nguồn nào, có giữ không, giá trị là gì). Mẫu: `<câu hỏi>? (<ghi chú nguồn>) → Q-<mã màn>-nn`; nhiều câu thì nối bằng `;`.
    - Không ghi cụm từ ("Chữ của dòng lỗi"), ghi chú, hay điều nguồn nói / hệ thống làm mà không hỏi gì ("UC ghi…, hệ thống ghi…"). Nguồn chênh nhau thì hỏi "theo bên nào?".
    - Ghi đúng nguồn: chữ chỉ có ở Figma hoặc hệ thống thì không gán cho UC, và ngược lại.
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

30. **Case kiểm hiển thị sau khi tạo.** Mỗi chức năng tạo có ít nhất một TC kiểm **từng thông tin vừa nhập hiển thị đúng** ở nơi hành động trả về (vd danh sách), mỗi **loại** (vd Type: Organization, Product, System) **đúng một TC**, kiểm ở nơi hành động trả về (rule 9); không thêm TC lặp cùng một loại chỉ để kiểm ở nơi hiển thị khác. TC này mô tả đủ mọi thông tin của form trong cùng một TC: Step liệt kê từng trường với giá trị cụ thể rồi bấm nút tạo; Expected liệt kê từng thông tin tương ứng. Trường nào không hiện ở nơi đó thì ghi rõ trong Expected là không hiện (hoặc để trống và ghi câu hỏi, rule 13). Ví dụ (sheet Scopes, danh sách):
    - Step: 1. Open the Scopes screen. 2. Click Create scope. 3. Select Type: Organization. 4. Enter Name: abc. 5. Enter What is in scope: abc. 6. Enter What is out of scope (optional): abc. 7. Click Create scope. 8. Check the new scope in the list.
    - Expected: the new scope is created; the list shows Type: Organization; Name: abc; What is in scope: abc; What is out of scope: abc.

31. **Giá trị tính toán hiển thị trên màn** (tỉ lệ, tổng, số đếm) có một nhóm TC với **bộ số cụ thể**: nhiều thành phần, một thành phần, 0%, 100%, kết quả phải làm tròn lên, kết quả phải làm tròn xuống. Biên chưa có căn cứ (phần thập phân đúng bằng .5, trên 0% mà dưới 1%, trên 99% mà chưa đủ, chưa có thành phần nào) thì vẫn viết TC, để trống Expected và ghi câu hỏi (rule 13).
    - **Hiểu logic trước khi viết, không viết bừa.** Trước khi viết TC cho một giá trị tính toán, ghi vào file thiết kế (vd khung case cha): mỗi con số nghĩa là gì, cách tính, căn cứ của từng phần (UC, nhãn và dòng phụ trên Figma, file mẫu import, hệ thống đang chạy). Thử lại cách tính trên số thật đang có (số trên Figma, trên hệ thống); khớp hết mới dùng. Nguồn cho số khác nhau thì ghi câu hỏi, không chọn bên nào.
    - Pre-condition dựng dữ liệu đủ để tính được; Step đi tới đúng chỗ thấy số; Expected khớp với dữ liệu ở Pre và các bước ở Step. Chưa nói được vì sao ra số đó thì chưa viết Expected. **Chờ Hanna chọn** cách ghi Expected khi công thức mới chỉ thấy ở hệ thống đang chạy: ghi phép tính và kết quả như bản v1.4 (vd `(74+6+0)/(116+31+78) × 100 = 35.56% → 36%`, kèm câu hỏi), hay để trống theo quyết định ngày 05/10 trong `profile.md`.
32. **Ô văn bản bắt đầu bằng `-`, `+`, `=` hoặc `@` phải có dấu nháy đơn ở đầu** (thuộc tính quotePrefix của kiểu ô), ở mọi sheet. Không có thì khi sửa ô trong Excel, nội dung bị hiểu là công thức. Script đặt dấu nháy lúc dựng file; không gõ thêm ký tự `'` vào nội dung.
33. **Chữ tiếng Việt lưu ở dạng dựng sẵn (NFC).** Chữ gõ ở dạng tổ hợp (dấu thanh là ký tự riêng) nhìn giống hệt nhưng script coi là chuỗi khác, vd nhóm `Không thành công` gõ hai dạng bị tính là hai nhóm. Script chuẩn hoá lúc dựng file và lúc kiểm. Đề xuất của AI — **chờ duyệt**.

34. **Chữ người dùng đã sửa trong file thì giữ nguyên.** File người dùng gửi lại sau khi tự sửa:
    - lưu nguyên file, tên kèm ngày giờ gửi, vd `…_Hanna-sua-0810-1516.xlsx`; bản kế tiếp dựng từ file đó, không dựng từ bản cũ của AI;
    - ô người dùng đã sửa giữ nguyên chữ, kể cả Expected và tên case. AI thấy cần sửa (lệch hệ thống, thiếu căn cứ, gõ nhầm) thì hỏi trong chat hoặc ghi câu hỏi, nói rõ điểm lệch; không tự đổi, không tự xoá;
    - trước khi giao, so từng ô bằng script với file người dùng, liệt kê ô AI đã chạm vào.
35. **Cover: mỗi dòng Record of change dẫn đúng FB của chính phiên bản đó**; dựng bản mới thì giữ đủ các dòng của bản trước (dựng từ file mới nhất, không từ nền cũ). Hồ sơ đi kèm (khung case cha, câu hỏi) ghi đúng số case, số thứ tự của bản mà nó nói tới.

36. **Đọc đủ ba nguồn rồi mới viết.** Trước khi viết TC của một màn: đã mở UC (bản hiện hành, đọc trực tiếp, ghi số bản và ngày), Figma (trang và khung của màn, ghi tên khung) và hệ thống đang chạy (vai trò nào, ngày nào). Thiếu nguồn nào thì ghi ở đầu khung "chưa đọc <nguồn>" và hỏi người dùng link hoặc quyền truy cập; **không viết Expected thay cho nguồn chưa đọc**, và không coi hệ thống là căn cứ duy nhất (rule 1). Ghi tên nguồn đã đọc vào cột Reference của sheet.
37. **Khi luồng, UC hoặc thiết kế đổi, hoặc đọc ra điều mới, phải rà lại các màn đã làm.** Lập bảng "màn đã làm bị ảnh hưởng" trong khung case cha (hoặc file thiết kế của lượt đó): sheet · case (No., TVP_ID) · điều lệch · cách xử lý. Case của AI thì sửa; case có chữ của người dùng (rule 34) thì không sửa, nêu thành câu hỏi hoặc báo trong chat. Báo người dùng đã rà những sheet nào trước khi giao, kể cả khi không có lệch.
38. **Tự soát trước khi giao, rồi mới báo xong.** `tc_check.py` chỉ kiểm định dạng; phải soát thêm nội dung theo danh sách dưới đây, quét hết sheet bằng script khi làm được:
    - Expected có nguồn UC hoặc Figma đã đọc; chỉ có hệ thống thì kèm câu hỏi (rule 1, 13). Không có chữ mơ hồ kiểu "đúng định dạng", "như bình thường" (rule 12).
    - Mỗi Pre-condition dựng được trên môi trường thật (dữ liệu, số lượng có thật); số tính toán thử lại bằng phép tính trên số thật của Figma, hệ thống (rule 31).
    - Mỗi câu hỏi nằm ở case mà câu trả lời làm đổi Expected của case đó; là câu hỏi thật có `?` và nguồn đúng (rule 23); không mượn mã Q của sheet khác mà không hỏi "áp chung được không".
    - Mỗi loại (loại scope, tier, vai trò) một case, không gộp (rule 9); bước và Expected khớp Pre-condition (rule 31).
    - Case của sheet đã làm bị ảnh hưởng đã xử lý theo rule 37.
    - Số báo trong chat (số case, số câu hỏi, số lỗi) lấy từ script (`rules/feedback.md` rule 16); hồ sơ đi kèm và Cover khớp file (rule 35).
39. **Soát chéo: gửi đủ lỗi trong một lần.** Bên soát (vd Opus) quét toàn bộ sheet theo danh sách rule 38 và các loại lỗi đã gặp trước đó, mỗi lỗi thì quét hết case cùng kiểu, rồi mới gửi một file review. Vòng soát lại chỉ báo mục chưa sửa hết và lỗi do bản sửa sinh ra; lỗi có từ bản trước mà vòng trước bỏ sót thì vẫn báo, ghi `sót từ vòng trước` và đếm riêng ở đầu file review. Chi tiết: skill `tc-authoring`, chế độ soát chéo, bước 2b. Hanna 09/10. **Chờ duyệt.**

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.8 | 2026-10-09 | Thêm rule 39 (soát chéo gửi đủ lỗi một lần; lỗi sót từ vòng trước đánh dấu, đếm riêng). **Chờ duyệt.** | FB-067 |
| v0.7 | 2026-10-09 | Thêm rule 36 (đọc đủ UC, Figma, hệ thống rồi mới viết; thiếu nguồn thì ghi và hỏi), rule 37 (rà lại màn đã làm khi luồng, UC, thiết kế đổi; bảng màn bị ảnh hưởng), rule 38 (danh sách tự soát nội dung trước khi giao). Rút từ review sheet Workspaces v1.11. **Chờ duyệt.** | FB-064 |
| v0.6 | 2026-10-08 | Theo góp ý của Hanna ngày 08/10 trên sheet Frameworks. Rule 13: Expected dựa trên điều chưa kiểm chứng phải kèm câu hỏi; câu hỏi đã có trả lời thì xoá, bỏ tô màu. Rule 19 viết lại: mọi ô chữ của bảng TC xuống dòng, căn giữa dọc, căn trái, kể cả ô neo Classification; `tc_check.py` kiểm. Rule 23: Open question là câu hỏi thật, có dấu `?`, ghi đúng nguồn. Rule 31: hiểu logic của giá trị tính toán trước khi viết; Pre, Step, Expected khớp nhau. Thêm rule 34 (giữ chữ người dùng sửa, dựng từ file của họ) và 35 (Cover dẫn đúng FB, hồ sơ đúng số). **Chờ duyệt.** | FB-054 · FB-055 · FB-056 · FB-057 |
| v0.5 | 2026-10-07 | Theo góp ý của Hanna ngày 06/10, 07/10 và cách viết ở bản `SGS-DTP_TestCase1_v1.4`. Rule 8: case bấm nút gửi mà không lưu được vào nhóm Không thành công; nhóm Không thành công đứng trước Thành công (ngược câu cũ). Rule 9 viết lại: kết quả kiểm ở nơi hành động trả về, nơi khác trong cùng sheet kiểm ở khu vực của nó, mỗi loại một case (thay câu cũ "hiện ở n nơi thì n case"). Rule 11: được đánh lại số khi chưa có kết quả chạy. Rule 13: kết quả suy ra cũng là chưa có căn cứ. Rule 14: bỏ `{{…}}`; dữ liệu tester nhập ghi cụ thể, dữ liệu có sẵn chưa xác định ghi `[tên]`; mỗi trường một dòng; text nguyên văn trong ngoặc kép. Rule 18: Times New Roman 10 cho mọi ô, kể cả ô trống và kiểu mặc định của cột. Rule 30: mỗi loại đúng một TC, bỏ "mỗi nơi hiển thị một TC". Thêm rule 31 (giá trị tính toán), 32 (dấu nháy đơn đầu ô), 33 (chữ dạng NFC). Tất cả **chờ duyệt**; ba chỗ còn **chờ Hanna chọn**: thứ tự hai nhóm ở rule 8, cách ghi Expected ở rule 31, việc đánh lại số ở rule 11. | FB-042 · FB-043 · FB-044 · FB-045 · FB-046 · FB-047 · FB-048 · FB-049 · FB-016 |
| v0.4 | 2026-10-06 | Rule 14: Pre-condition không ghi mở màn hình đang test (đó là Step 1); muốn tới màn B qua nhiều thao tác ở màn A thì liệt kê thao tác ở Pre-condition. Thêm rule 30: case kiểm hiển thị sau khi tạo, mỗi loại một TC, đủ mọi thông tin của form. Đề xuất của AI theo góp ý của Hanna — **chờ duyệt** | FB-040, FB-041 |
| v0.3 | 2026-10-05 | Rule 3: "màn hình" tính theo mục menu. Rule 4: màn có danh sách xếp theo vòng đời dữ liệu, trạng thái rỗng trước. Rule 7: ví dụ tiếng Anh, mỗi ô một thứ tiếng, tên nhóm kiểm theo bảng từ. Rule 12: không trỏ sang TC khác, mỗi mục một dòng. Rule 14 viết lại theo góc nhìn Tester: dòng đăng nhập `Logged in as <role>`, dữ liệu và nhãn ghi thẳng trong ô, Step là thao tác cụ thể. Rule 15: tên nhóm tiếng Anh, case Bảo mật làm được trên giao diện. Rule 16: ngôn ngữ file TC theo `profile.md`. Rule 22 bỏ sheet `_Data`, `_Labels`. Thêm mục G: chia sheet (rule 24–28) và rule 29 — TC gọi API chỉ khi tester được gọi API, ở sheet `API` riêng. Hanna duyệt 05/10, trừ phần **chờ duyệt**: rule 3 và 24–28 (chia sheet), rule 19 (căn giữa theo chiều dọc như file mẫu, đề xuất của AI). | FB-029 · FB-030 · FB-035 · FB-031 · FB-032 · FB-034 · FB-036 · FB-039 · FB-013 |
| v0.3 | 2026-10-02 | Thêm rule 24: form theo file mẫu của dự án — sheet mới thêm vào file mẫu bằng cách nhân bản một sheet TC đã duyệt; bố cục theo file mẫu, phông và màu theo rule 22 với bảng màu lấy một màu nền tiêu đề của file mẫu; chưa có file mẫu thì hỏi. **Chờ duyệt.** | FB-019 · FB-016 |
| v0.2 | 2026-10-02 | Đổi tên cột `Chờ text` → `Open question` (rule 13, 16, 23). Thêm rule 22: định dạng đồng nhất toàn bộ — một phông, một bảng màu cho mọi sheet và mọi file. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: thứ tự nguồn chân lý, một màn một sheet, bốn cấp Classification, quy tắc chưa có căn cứ thì để trống, quy tắc chuyển ngôn ngữ, và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô). | FB-010 · FB-011 · FB-012 · FB-013 |
