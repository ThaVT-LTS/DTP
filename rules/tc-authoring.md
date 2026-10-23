# Rule — Viết test case (tc-authoring)

Phiên bản: v0.11 · Nạp cùng `rules/common.md`, `rules/feedback.md`, `rules/tester.md` khi viết hoặc sửa file test case. Quy trình chi tiết: skill `tc-authoring`.

Rule này nói về **file test case bàn giao được**: tổ chức, nội dung, và định dạng. Phần kỹ thuật thiết kế (phân vùng tương đương, bảng quyết định, chuyển trạng thái) vẫn ở `rules/tester.md` và skill `test-design`.

## A. Nguồn chân lý

1. **Thứ tự ưu tiên khi các nguồn lệch nhau:** (1) quyết định chốt của khách hàng (Final Confirmation, decision log) > (2) UC > (3) tiêu chí chấp nhận của user story > (4) Figma bản mới nhất > (5) web demo / hệ thống đang chạy.
    - Web đã hiện hành vi và hợp lý, không trái các nguồn trên → ghi theo web, không đặt câu hỏi.
    - Web có nhiều chức năng hơn UC → vẫn viết theo web; UC xếp chức năng đó vào Phase 2 thì cột UC ghi mã `P2-…`.
    - UC có mà web và Figma chưa có → vẫn viết case, theo rule 40.
    - Web sai rõ ràng (lỗi chính tả, dữ liệu hai chỗ lệch nhau, phi logic) → Expected ghi điều đúng; case sẽ fail và thành bug.
    - **Dev hoặc dự án đã bỏ, đổi có chủ đích** một chi tiết của Figma (có người xác nhận, ngày, commit) → Expected theo web, ghi căn cứ ở Remark; không đánh Failed. Vd 19/10: dòng `Your affiliate. New customers always belong to it.` dev bỏ ở commit 48e50cb (FB-095).
    - **Nghiệp vụ cấm một thao tác** (dev hoặc dự án xác nhận) mà web **ẩn hẳn nút** của thao tác đó, còn spec chỉ ghi "bị từ chối" chứ không bắt hiện nút rồi báo lý do → ẩn nút là đúng nghiệp vụ: Expected ghi "không có button …", không đánh Failed vì thiếu thông báo lý do. Case gọi API trực tiếp vẫn giữ (phải trả lỗi, không đổi dữ liệu). Vd 21/10: workspace có evidence / service request không cho xoá → không có nút Delete; WS-BUG-02 rút lại (FB-099).
2. Lệch nhau mà **không áp được rule 1** thì ghi thành câu hỏi `Q-<mã màn>-nn` (rule 13, 23), không tự chọn bên nào.

## B. Tổ chức file

3. **Một màn hình một sheet.** Màn hình tính theo mục menu: danh sách, chi tiết, hộp thoại, panel mở từ cùng một mục menu mặc định nằm chung một sheet, như sheet `Scopes` gồm cả Danh sách và Chi tiết; phần nào đủ lớn thì tách (rule 25). Tên sheet lấy đúng tên mục menu của hệ thống, không dịch, không viết tắt; sheet tách ra thì lấy tên màn như trên giao diện. Vai trò, gộp và tách: mục G.
    - **Không thêm sheet mới vào file TC** khi người dùng không yêu cầu. Báo cáo rà soát, kết quả chạy có ảnh, danh sách bug để ở file riêng (FB-085).
4. Trong sheet, TC xếp theo **khu vực**; thứ tự khu vực theo mắt đọc: trên → dưới trong một cột, hết cột trái sang cột phải. Màn có danh sách thì xếp theo vòng đời dữ liệu trước: mở màn → trạng thái rỗng (Empty state) → tạo mới → các khu vực cần có dữ liệu (bảng, tìm kiếm, lọc, phân trang); trong từng chặng vẫn theo mắt đọc.
5. **Luồng nghiệp vụ xuyên màn** có sheet riêng `FLOW-nn`, không nhét vào sheet màn hình. Mỗi bước trong luồng ghi rõ màn hình thực hiện.
6. Đầu mỗi sheet có khối thông tin: tên chức năng · tên màn · người viết · ngày tạo · nguồn tham chiếu.
    - **Người viết** (ô `Creator` ở mọi sheet và trên Cover, cả thuộc tính tác giả `docProps/core.xml`) là người chịu trách nhiệm, lấy từ `profile.md` (SGS DTP: Hanna); không ghi tên AI hay công cụ. Script dựng sheet nhận `--creator`, không có giá trị mặc định.
    - Dòng Function Name, Screen Name, Reference đủ cao để không cắt chữ. Reference ghi đủ nguồn đã dùng (rule 36).

## C. Bốn cấp Classification

7. Bốn cột, đúng thứ tự, không đổi nghĩa giữa các sheet:

| Cấp | Nội dung | Ví dụ |
|---|---|---|
| **I** | Feature — khối chức năng người dùng gọi tên được | `Login` |
| **II** | Khu vực trên màn, hoặc nhóm kiểm | `Email` · `Security` |
| **III** | Mục kiểm, hoặc nhóm kết quả | `Success` · `Failure` · `Validation` |
| **IV** | Case cụ thể, mỗi dòng một case | `Empty` · `Invalid format` |

Ví dụ trên là file TC tiếng Anh. Mỗi ô ghi một thứ tiếng theo ngôn ngữ của file (rule 16), vd `Login`, không ghi `Đăng nhập - Login`. Tên nhóm kiểm dùng bảng từ cố định ở `references/format.md` §7.

**Hộp thoại, wizard nhiều bước** (FB-088): mọi case của nó nằm liền một khối dưới cùng cấp I; cấp II là **tên bước như trên giao diện** (vd `Bước 1 · Account`, `Bước 2 · Invite initial Customer Admin`), thêm nhóm `Sau khi tạo` cho các case kiểm ở nơi hành động trả về. Case Hiển thị của mỗi bước kiểm trạng thái thanh bước (bước đang làm, đã xong, chưa tới; bấm tên bước có chuyển bước không). Các case validation của bước nào đặt ở bước đó.

8. **Xếp case sao cho cùng nhóm kết quả nằm liền nhau.** Xen kẽ thì không gộp ô được, và người đọc mất mạch.
    - Case mà bước cuối là bấm nút gửi (vd `Create scope`, `Save`, `Link and create workspace`) nhưng **không lưu được** — bỏ trống trường bắt buộc, chỉ có khoảng trắng, trùng tên, quá giới hạn — nằm trong nhóm **Không thành công** của khu vực, cùng các case Cancel, ×, Esc. Không lập nhóm Kiểm tra dữ liệu riêng cho các case đó.
    - Thứ tự trong một khu vực: **Hiển thị → Nhập liệu → Không thành công → Thành công** (Hanna 15/10).
    - **Case mới chèn vào đúng nhóm Classification của nó**, không thêm ở cuối sheet; một khu vực không bị tách làm hai nơi. Dùng `tc_rows.py` để chèn, xoá mà giữ cụm gộp và mã TC.
    - Test_Report dựng lại theo nhóm (I, II); mỗi khối sheet có dòng Total; **tổng cuối bảng gồm mọi khối**. Không có dòng "Case bổ sung" nằm ngoài tổng.
9. **Kết quả của một hành động kiểm ở nơi hành động trả về**, vd tạo scope xong về danh sách thì kiểm dòng vừa tạo ở danh sách.
    - Nơi hiển thị khác **trong cùng sheet** đã có khu vực riêng (vd màn chi tiết) thì kiểm ở khu vực đó; không lặp lại ở khu vực của hành động.
    - Nơi hiển thị ở **màn khác, sheet khác** hoặc với vai trò khác thì theo rule 27.
    - Chỗ nào hiển thị khác nhau theo **loại** (vd Type: Organization, Product, System) thì mỗi loại một case.
    - Không gộp nhiều nơi vào một ô kết quả mong đợi.

## D. Nội dung một dòng

10. Mỗi TC có đúng một `UC_ID`. Không map được thì ghi `[NGOÀI UC]` kèm lý do, không để trống. Case `[Phase 2]` giữ mã UC gốc (rule 40); case lỗi thời bị xoá khỏi file, không còn tiền tố `[OUT]` (rule 40, FB-083).
11. `TVP_ID` duy nhất **trong cả file**, theo mẫu `<MÃ MÀN>_nnn` (FB-102, 21/10): tiền tố 2 chữ theo màn, cùng bộ tiền tố với mã bug — vd Documents `DC_001`, Login `LG_`, Customers `CU_`, Users `US_`, Frameworks `FW_`, Scopes `SC_`, Workspaces `WS_`, Workspace detail `WD_`, Profile `PF_`, Bulk upload `BU_`. Màn chưa có tiền tố thì chọn 2 chữ chưa dùng và ghi vào bảng tiền tố của dự án. Không dùng `TC_nnn` trùng giữa các sheet.
    - **Mã TC đồng nhất với cột No.**: `TC_` + số No. 3 chữ số (FB-086, thay quy định "không đánh lại mã" của FB-081). Đánh lại mã thì cập nhật mọi tham chiếu: sheet `Cần xác nhận`, file bug, file E2E. **Chờ chốt** cách làm khi thêm case: (a) chèn đúng nhóm rồi đánh lại toàn bộ, hay (b) nối case mới vào cuối sheet để mã cũ không đổi (cách đã dùng cho TC_100 sheet Customers, 20/10).
    - **Mã TC không bao giờ đánh lại** sau khi file đã giao cho người dùng hoặc đã đưa lên Azure DevOps. Case mới lấy mã kế tiếp; case bỏ đi không xoá, không dùng lại mã mà đánh dấu `[OUT]` (rule 40).
12. Kết quả mong đợi phải **quan sát được**: text nguyên văn, màn hình đích, trạng thái, dữ liệu thay đổi. Cấm "hoạt động bình thường", "hiển thị đúng", "thành công" mà không nói thấy gì; tiếng Anh cũng vậy, vd "works normally", "displays correctly", "as expected".
    - Ghi thẳng trong ô: không trỏ sang TC khác ("giống TC_006"), không ghi "ở cả hai màn" mà không nêu tên từng màn.
    - Từ hai mục trở lên (cột, trường, lựa chọn, nút) thì mỗi mục một dòng `- <mục>`, không nối bằng " · "; chỉ giữ " · " khi đó là chữ thật trên giao diện.
13. **Open question tinh gọn.** Chỉ đặt câu hỏi khi các nguồn mâu thuẫn mà không áp được rule 1, hoặc khi đọc hết các nguồn đang có (rule 36) vẫn chưa có căn cứ để viết Expected. Khi đó **để trống Expected**, ghi câu hỏi vào `Open question` và **tô màu ô** theo bảng màu. Tự đặt text chưa ai duyệt sẽ tạo bug giả.
    - Kết quả **suy ra** mà không nguồn nào nêu thì không viết thành câu khẳng định: để trống và hỏi, hoặc viết theo dạng **đề xuất**: tô **vàng `FFF2CC`** ô UC, giữ câu hỏi ở Open question, đưa vào sheet `Cần xác nhận` kèm "Đề xuất mặc định" (rule 23). Tester chạy theo đề xuất; BA chỉ cần xác nhận hoặc sửa.
    - **Câu đã có trả lời** (người dùng trả lời, nguồn khác đã nêu, case khác đã kiểm ra, web đã hiện): ghi câu trả lời vào Expected, xoá câu hỏi ở case và **xoá dòng ở sheet `Cần xác nhận`**, bỏ tô màu. Áp cả khi rà soát hàng loạt: câu kết luận Đóng thì xoá dòng (FB-084).
    - **Câu người dùng đã xoá là đã xử lý**: khi viết lại hay soát chéo không thêm lại, không tô lại.
    - **Chữ báo lỗi chưa thấy trên web** ghi theo mẫu của ứng dụng, không đặt câu hỏi; đoán không chắc thì chỉ ghi hành vi (không lưu, ô viền đỏ, có lỗi dưới ô). Ô Reference ghi "chạy thấy khác thì sửa theo web". Mẫu:

| Tình huống | Mẫu |
|---|---|
| Bỏ trống ô nhập chữ | `Enter a/the <trường>.` |
| Bỏ trống ô chọn, ngày, file | `Choose a <thứ cần chọn>.` |
| Sai định dạng | `Enter a valid <…>, e.g. <ví dụ>.` |
| Trùng | `A <đối tượng> with this name already exists.` |

14. **Viết bằng chữ, cho Tester đọc là chạy được.**
    - **Dòng đăng nhập ở Pre-condition:** `Login acc <vai trò> (<tên tài khoản>) <điều kiện>`, **không dùng dấu `;` sau vai trò**. Điều kiện bắt đầu bằng có, chưa có, được, đã… thì viết liền sau, vd `Login acc Customer Admin (Linh Tran) chưa có sự kiện nào`, `Login acc Customer Viewer (Iris Huang) được gán scope [System], không được gán scope [Organization]`; điều kiện khác nối bằng dấu phẩy, vd `Login acc Customer Admin của Formosa Chips Inc. (Chen Wei-Ting), ABC Trading Co., Ltd. có evidence …`. Màn không cần đăng nhập ghi `Chưa đăng nhập`. (File TC tiếng Anh: `Logged in as <role>`, `Not logged in`.)
    - **Pre-condition dạng đánh số, nêu rõ môi trường và tài khoản** (FB-089; áp cho sheet E2E; sheet màn hình **chờ Hanna chốt** có đổi sang dạng này không):
      `1. Vào môi trường: <URL đăng nhập>` → mỗi tài khoản một dòng `2. Login acc <vai trò> (<tên>): <email> / <mật khẩu>` → các điều kiện dữ liệu → `n. Hộp thư test: <URL>`. Tài khoản tạo trong luồng ghi `— tạo trong luồng, đăng nhập sau khi kích hoạt`. Sheet E2E có thêm bảng Tài khoản test (vai trò · nhân vật, mật khẩu, link đăng nhập, email · nguồn).
    - **Pre-condition chỉ ghi trạng thái cần có trước khi vào màn hình đang test** (đăng nhập bằng vai trò nào, dữ liệu đã dựng). Không ghi "mở màn hình đang test" vào Pre-condition: việc đó là **Step 1**. Một sheet test một màn hình, nên TC chỉ tập trung vào màn đó. Ví dụ sheet Scopes: Pre-condition `Login acc Customer Admin (Linh Tran)`; Step 1 `Bấm Scopes ở menu trái`.
    - Muốn tới màn B mà phải làm nhiều thao tác dữ liệu ở màn A (tạo dữ liệu, chọn, gắn…) thì Pre-condition mới ghi các thao tác ở màn A, **liệt kê từng thao tác kèm giá trị cụ thể** (vd `On Scopes, create scope: Type Organization, Name abc, What is in scope abc`). Step vẫn bắt đầu bằng mở màn B, rồi các thao tác tiếp theo trên màn B.
    - Dữ liệu ghi ngay trong ô của TC, nhãn giao diện ghi đúng nguyên văn. **Không còn `{{…}}` ở bất kỳ ô nào của file giao**: người dùng → dòng đăng nhập; địa chỉ → `[URL …]`, định nghĩa ở ô Reference.
        - Dữ liệu **tester tự nhập** thì ghi giá trị cụ thể, vd `Name: abc`.
        - Dữ liệu **phải có sẵn trên hệ thống mà dự án chưa xác định** (tên một scope có sẵn, tên khách hàng, người dùng, framework…) thì viết chung chung, tên đặt trong ngoặc vuông, vd `Belongs to organisation: [Organization]`, `Belongs to product (optional): [Product]`. Một tên ngoặc vuông dùng cùng một nghĩa trong cả sheet.
        - Nhập hoặc chọn nhiều trường trong một bước thì mỗi trường một dòng `- <nhãn>: <giá trị>` dưới dòng `Nhập` (hoặc `Chọn`). Expected có ý con thì dùng `+ <ý con>` dưới dòng `- <ý>`.
        - Text nguyên văn của giao diện (lỗi, thông báo, mô tả) đặt riêng một dòng, trong ngoặc kép, sau dòng dẫn, vd `- Hiện lỗi tại Name:` rồi `"Enter a name."`.
    - **Step ghi rõ thao tác:** bước 1 là nhập URL vào thanh địa chỉ hoặc bấm mục ở menu trái; mỗi bước một thao tác cụ thể (bấm vào đâu, nhập giá trị gì); tên nút ghi `button [Tên]`; case chỉ kiểm hiển thị ghi `Nhìn <vùng>`. **Không** ghi "Kiểm tra …" hay "Mở màn …" trong Step. Một case có nhiều kết quả theo bước thì Expected ghi `Sau bước n: …`. Chưa biết thao tác hay kết quả thì để trống và ghi câu hỏi (rule 13).
15. Mỗi khu vực có thao tác ghi dữ liệu phải có đủ: ít nhất một case Thành công, một case Không thành công, một case Phân quyền, một case Bảo mật (file tiếng Anh: Success, Failure, Permission, Security). Case Bảo mật là case tester làm được trên giao diện hoặc trình duyệt; case cần gọi thẳng API theo rule 29.
    - **Bộ case abnormal cho mỗi ô nhập có giới hạn** (FB-087): (1) đúng giới hạn — tạo được, lưu đủ, chữ dài không tràn khung; (2) vượt 1 ký tự — chặn ngay ở bước đang nhập, lỗi dưới đúng ô; (3) chỉ dấu cách; (4) dấu cách đầu, cuối — lưu đã cắt; (5) ký tự đặc biệt, emoji, HTML/script — hiện đúng như văn bản; (6) sai định dạng — gom nhiều giá trị a, b, c… trong một case, mỗi giá trị bấm nút một lần. Pre-condition ghi cách tạo chuỗi bằng công thức Excel (vd `=REPT("A",201)`, kiểm `=LEN(...)`); giới hạn lấy từ tài liệu, không có thì từ schema API của hệ thống (ghi nguồn). Hai lỗi cùng lúc (vd Name trống và Email sai) có một case riêng.
    - **Priority:** Critical · High · Medium · Low. **Critical** dành cho case bảo mật và phân quyền phải qua trước UAT (vd consultant chưa được duyệt mở workspace bằng URL, dữ liệu nháp lộ sang khách hàng). Hanna đồng ý 15/10.

## E. Đa ngôn ngữ

16. **Ngôn ngữ của file TC theo dòng "Ngôn ngữ viết file TC" trong `profile.md` của dự án**, áp cho mọi sheet, mọi cột; phần ngoại lệ (vd cột `Open question` và sheet `Cần xác nhận` viết tiếng Việt) cũng ghi ở dòng đó. Nhãn giao diện luôn ghi đúng nguyên văn theo ngôn ngữ hệ thống đang chạy, kể cả chữ hoa chữ thường, vd `Create scope`. Khi chuyển ngôn ngữ cho bộ TC có sẵn:
    - chỉ dịch chuỗi **có căn cứ** — bảng đối chiếu thật, hoặc danh sách phần tử đã duyệt;
    - chuỗi chưa có bản dịch chính thức thì **giữ nguyên gốc**, tô đỏ, ghi vào cột `Open question`;
    - dịch theo thứ tự **chuỗi dài trước, chuỗi ngắn sau**, nếu không chuỗi ngắn sẽ cắt nát chuỗi dài.
17. Dịch chỉ đổi **ngôn ngữ**, không đổi **hành vi**. TC nào sai hành vi so với thiết kế mới thì dịch xong vẫn sai — phải liệt kê riêng.

## F. Định dạng file

18. **Phông chữ: Times New Roman, cỡ 10** cho **mọi ô của mọi sheet**: ô có chữ, ô trống đã kẻ khung, ô nằm trong cụm gộp, và kiểu mặc định của cột (để gõ vào ô mới vẫn ra đúng phông). Kiểm ở **mức XML**: phông mặc định (font 0), mọi phông trong `styles.xml`, phông theme major và minor; không còn thẻ `scheme`; cỡ ghi `10` (không ghi `10.000000`). `tc_fix_xlsx.py` sửa và kiểm.
19. **Mọi ô chữ của bảng TC: xuống dòng (wrap text), căn giữa theo chiều dọc, căn trái**, để chữ dài không bị che. Áp cho cả ô neo của cụm gộp ở bốn cột Classification (B–E), và các cột Name, Pre-condition, Step, Expected, Open question. Cột No. theo file mẫu (căn giữa). Script dựng sheet phải đặt sẵn; `tc_check.py` báo lỗi ô sai (ô trong cụm gộp không phải ô neo thì bỏ qua, vì Excel lấy căn lề của ô neo).
20. **Quy tắc gộp ô** cho bốn cột Classification:
    - gộp các dòng **liền nhau có cùng giá trị**; ô trống nghĩa là "giống dòng trên";
    - cụm con **không được vượt ranh giới cụm cha** — cột III đổi cụm thì cột IV phải cắt theo;
    - cụm chỉ một dòng thì không gộp;
    - chỉ ô neo giữ giá trị, các ô còn lại để trống.
21. Người viết làm việc trên **bảng phẳng** (giá trị lặp lại ở mọi dòng); việc gộp ô do script làm lúc xuất file. Không sửa tay trên file đã gộp — ô gộp không lọc được, không sort được, copy xuống là vỡ.

22. **Định dạng đồng nhất toàn bộ.** Mọi sheet trong một file và mọi file test case của dự án dùng **một** phông (Times New Roman 10) và **một** bảng màu khai ở `references/format.md` §4: màu hàng tiêu đề, màu nhãn, màu dòng còn câu hỏi mở, màu đường kẻ. Không dùng màu hay phông ngoài bảng đó; cần thêm thì sửa bảng màu và script trước. Sheet phụ (`Cover`, `Hướng dẫn`, `FLOW-nn`, `Test_Report`) theo cùng quy ước với sheet màn hình.
23. Cột ghi chuỗi hoặc câu hỏi còn thiếu của một dòng tên là **`Open question`** (trước đây: `Chờ text`). Nội dung ghi mã câu hỏi `Q-<mã màn>-nn` kèm tóm tắt điều cần xác nhận.
    - Mỗi phần trong ô là **một câu hỏi thật**, ngắn: kết thúc bằng dấu `?`, nói rõ cần quyết điều gì, một mã Q. Mẫu: `<câu hỏi>? (<nguồn>) → Q-<mã màn>-nn`; nhiều câu thì nối bằng `;`.
    - **Mọi câu hỏi ở sheet `Cần xác nhận` có cột "Đề xuất mặc định"**: phương án nên chọn kèm lý do ngắn, vd Q-L-24: "Bỏ checkbox Keep me signed in ở Phase 1, phiên do Microsoft Entra quản lý".
    - Không ghi cụm từ ("Chữ của dòng lỗi"), ghi chú, hay điều nguồn nói / hệ thống làm mà không hỏi gì ("UC ghi…, hệ thống ghi…"). Nguồn chênh nhau thì hỏi "theo bên nào?".
    - Ghi đúng nguồn: chữ chỉ có ở Figma hoặc hệ thống thì không gán cho UC, và ngược lại.
24. **Form theo file mẫu của dự án.** Dự án có file TC mẫu (ghi ở `profile.md`, dòng "File TC mẫu của dự án") thì file bàn giao là chính file đó: sheet mới được **thêm vào file mẫu, ngay cạnh một sheet TC đã duyệt, bằng cách nhân bản form của sheet ấy** — khối thông tin, khối tổng kết, hàng tiêu đề, độ rộng cột, căn lề, đường kẻ, dropdown, trang in. Không dựng lại form bằng script tự vẽ.
    - Bố cục của file mẫu khác rule 18–19 hoặc `references/format.md` §1–§3 ở đâu thì **theo file mẫu**, và ghi điểm khác thành câu hỏi cho người dùng.
    - Phông và màu vẫn theo rule 22. Bảng màu lấy **một** màu nền tiêu đề của file mẫu; file mẫu có ô lệch (màu khác, phông khác) thì đưa cả file mẫu về chuẩn trước khi dùng làm mẫu.
    - Dự án chưa có file mẫu thì hỏi người dùng trước khi bàn giao; file dựng bằng form mặc định chỉ là bản tạm.

## G. Chia sheet

24. **Không chia sheet theo vai trò.** Màn nhiều vai trò dùng, hoặc có ở nhiều portal, vẫn là một sheet. Vai trò nằm trong sheet:
    - Pre-condition của mọi TC mở đầu bằng dòng đăng nhập theo rule 14 (`Login acc <vai trò> (<tên>) …` hoặc `Chưa đăng nhập`), kể cả khi đã có điều kiện dữ liệu. Lọc cột Pre-condition theo tên vai trò là ra danh sách chạy của vai trò đó, nên tên vai trò ghi đúng như tài liệu yêu cầu.
    - Khác biệt giữa các vai trò viết ở nhóm Phân quyền cuối sheet (rule 15).
    - Chức năng có màn ở nhiều portal thì thêm tiền tố vào đầu Classification I: phía SGS `[SGS] …`, phía consultant `[Consultant] …`, vd `[SGS] Certification list`. Kết quả hiện ở portal kia (vd khách hàng thấy yêu cầu đã được nhận) kiểm trong cùng case với hành động (rule 27).
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
35. **Một số phiên bản duy nhất:** tên file, ô Version trên Cover và dòng cuối Record of change ghi cùng một số; mỗi lần giao thêm một dòng, không nhảy số; đánh số lại thì ghi một dòng giải thích. **Cover: mỗi dòng Record of change dẫn đúng FB của chính phiên bản đó**; dựng bản mới thì giữ đủ các dòng của bản trước (dựng từ file mới nhất, không từ nền cũ). Hồ sơ đi kèm (khung case cha, câu hỏi) ghi đúng số case, số thứ tự của bản mà nó nói tới.

36. **Đọc đủ các nguồn rồi mới viết.** Trước khi viết TC của một màn: đã đọc quyết định chốt (Final Confirmation, decision log), UC (bản hiện hành, đọc trực tiếp, ghi số bản và ngày), tiêu chí chấp nhận của user story, Figma (trang và khung của màn, ghi tên khung) và hệ thống đang chạy (vai trò nào, ngày nào). Thiếu nguồn nào thì ghi ở đầu khung "chưa đọc <nguồn>" và hỏi người dùng link hoặc quyền truy cập; **không viết Expected thay cho nguồn chưa đọc**, và không coi hệ thống là căn cứ duy nhất (rule 1). Ghi tên nguồn đã đọc vào cột Reference của sheet.
37. **Khi luồng, UC hoặc thiết kế đổi, hoặc đọc ra điều mới, phải rà lại các màn đã làm.** Lập bảng "màn đã làm bị ảnh hưởng" trong khung case cha (hoặc file thiết kế của lượt đó): sheet · case (No., TVP_ID) · điều lệch · cách xử lý. Case của AI thì sửa; case có chữ của người dùng (rule 34) thì không sửa, nêu thành câu hỏi hoặc báo trong chat. Báo người dùng đã rà những sheet nào trước khi giao, kể cả khi không có lệch.
38. **Cổng trước khi giao.** Chạy `tc_fix_xlsx.py --fix --creator <người viết>`, rồi `tc_check.py --creator <người viết>`; cả hai **0 lỗi** mới giao; sau đó mở file bằng Excel hoặc OnlyOffice, xem qua một sheet mới và một sheet cũ. `tc_check.py` chỉ kiểm định dạng và một phần nội dung; phải tự soát thêm theo `references/tu-soat.md` và danh sách dưới đây, quét hết sheet bằng script khi làm được:
    - Expected có nguồn UC hoặc Figma đã đọc; chỉ có hệ thống thì kèm câu hỏi (rule 1, 13). Không có chữ mơ hồ kiểu "đúng định dạng", "như bình thường" (rule 12).
    - Mỗi Pre-condition dựng được trên môi trường thật (dữ liệu, số lượng có thật); số tính toán thử lại bằng phép tính trên số thật của Figma, hệ thống (rule 31).
    - Mỗi câu hỏi nằm ở case mà câu trả lời làm đổi Expected của case đó; là câu hỏi thật có `?` và nguồn đúng (rule 23); không mượn mã Q của sheet khác mà không hỏi "áp chung được không".
    - Mỗi loại (loại scope, tier, vai trò) một case, không gộp (rule 9); bước và Expected khớp Pre-condition (rule 31).
    - Case của sheet đã làm bị ảnh hưởng đã xử lý theo rule 37.
    - Số báo trong chat (số case, số câu hỏi, số lỗi) lấy từ script (`rules/feedback.md` rule 16); hồ sơ đi kèm và Cover khớp file (rule 35).
39. **Soát chéo: gửi đủ lỗi trong một lần.** Bên soát (vd Opus) quét toàn bộ sheet theo danh sách rule 38 và các loại lỗi đã gặp trước đó, mỗi lỗi thì quét hết case cùng kiểu, rồi mới gửi một file review. Vòng soát lại chỉ báo mục chưa sửa hết và lỗi do bản sửa sinh ra; lỗi có từ bản trước mà vòng trước bỏ sót thì vẫn báo, ghi `sót từ vòng trước` và đếm riêng ở đầu file review. Chi tiết: skill `tc-authoring`, chế độ soát chéo, bước 2b. Hanna 09/10. **Chờ duyệt.**

40. **Phạm vi: viết theo danh sách UC, theo wave, có đánh dấu Phase.**
    - Trước khi viết, lập **bảng độ phủ**: mỗi UC Phase 1 của UC List hiện hành có bao nhiêu case chạy được. Mỗi UC phải có **ít nhất một case chạy được** (có Expected, không mang tiền tố `[Phase 2]`, `[OUT]`). Wave của dự án ghi ở `profile.md`.
    - Chức năng chưa có thiết kế, hoặc chưa làm ở Phase 1: tên case bắt đầu `[Phase 2]`, cột UC ghi mã UC gốc, Expected ghi `- Chưa viết Expected: thuộc Phase 2 (<lý do>)`. Quyết định ghi rõ "không thuộc Phase 1" thì dùng `[Ngoài Phase 1]`.
    - **Case lỗi thời bị xoá khỏi file** (FB-083, thay quy định "giữ lại với tiền tố `[OUT]`" ngày 15/10): trước khi xoá, ghi lý do và căn cứ vào báo cáo rà soát (file riêng, skill `tc-review`), vd `Xoá: D57, SGS Admin không còn duyệt yêu cầu`. File giao không còn case `[OUT]`; Test_Report cập nhật theo số case còn lại.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.11 | 2026-10-20 | Gộp góp ý 19–20/10 (chạy sheet Customers, E2E Wave 1) vào rule có sẵn, không thêm số: rule 1 quyết định của dev đè Figma; rule 3 không thêm sheet; rule 7 hộp thoại nhiều bước nhóm theo bước; rule 10, 40 xoá case lỗi thời (bỏ `[OUT]`, thay FB-081); rule 11 mã TC = No. (chờ chốt cách thêm case); rule 13 câu Đóng xoá khỏi sheet Cần xác nhận; rule 14 Pre-condition đánh số (E2E; sheet màn hình chờ chốt); rule 15 bộ case abnormal. **Chờ duyệt.** | FB-083 · FB-084 · FB-085 · FB-086 · FB-087 · FB-088 · FB-089 · FB-095 |
| v0.10 | 2026-10-15 | Gộp bản tổng hợp 15/10 (rule 36–56 của phiên chat) vào rule có sẵn, không thêm số: rule 1–2 thứ tự 5 nguồn và cách xử lý lệch; 6 người viết là Hanna; 8 thứ tự Hiển thị → Nhập liệu → Không thành công → Thành công, chèn case đúng nhóm, Test_Report theo nhóm; 10–11 mã TC không đánh lại, `[OUT]`; 13 Open question tinh gọn, Expected đề xuất tô vàng, mẫu chữ báo lỗi (gộp rule 40 cũ); 14 dòng `Login acc`, không `{{…}}`, Step `button [Tên]`, `Nhìn <vùng>`; 15 Priority Critical; 18 phông mức XML; 23 Đề xuất mặc định; 24 `[SGS]`, `[Consultant]`; 35 một số phiên bản; 36 thêm quyết định chốt và tiêu chí chấp nhận; 38 cổng `tc_fix_xlsx` + `tc_check`; 40 viết rule mới: độ phủ UC theo wave, `[Phase 2]`, `[Ngoài Phase 1]`, `[OUT]`. Bỏ ngoại lệ theo `profile.md` ở rule 1, 2, 13, 14 vì đã thành rule chung. | FB-074 · FB-075 · FB-076 · FB-077 · FB-078 · FB-079 · FB-080 · FB-081 · FB-082 |
| v0.9 | 2026-10-14 | Rule 1, 2, 13, 14: thêm ngoại lệ theo mục "Quy tắc viết TC của dự án" trong `profile.md` (SGS DTP: theo web khi hợp lý, thông báo lỗi theo mẫu app, không đặt câu hỏi). Thêm rule 40 (câu hỏi người dùng đã xoá là đã giải quyết). **Chờ duyệt.** | FB-070 |
| v0.8 | 2026-10-09 | Thêm rule 39 (soát chéo gửi đủ lỗi một lần; lỗi sót từ vòng trước đánh dấu, đếm riêng). **Chờ duyệt.** | FB-067 |
| v0.7 | 2026-10-09 | Thêm rule 36 (đọc đủ UC, Figma, hệ thống rồi mới viết; thiếu nguồn thì ghi và hỏi), rule 37 (rà lại màn đã làm khi luồng, UC, thiết kế đổi; bảng màn bị ảnh hưởng), rule 38 (danh sách tự soát nội dung trước khi giao). Rút từ review sheet Workspaces v1.11. **Chờ duyệt.** | FB-064 |
| v0.6 | 2026-10-08 | Theo góp ý của Hanna ngày 08/10 trên sheet Frameworks. Rule 13: Expected dựa trên điều chưa kiểm chứng phải kèm câu hỏi; câu hỏi đã có trả lời thì xoá, bỏ tô màu. Rule 19 viết lại: mọi ô chữ của bảng TC xuống dòng, căn giữa dọc, căn trái, kể cả ô neo Classification; `tc_check.py` kiểm. Rule 23: Open question là câu hỏi thật, có dấu `?`, ghi đúng nguồn. Rule 31: hiểu logic của giá trị tính toán trước khi viết; Pre, Step, Expected khớp nhau. Thêm rule 34 (giữ chữ người dùng sửa, dựng từ file của họ) và 35 (Cover dẫn đúng FB, hồ sơ đúng số). **Chờ duyệt.** | FB-054 · FB-055 · FB-056 · FB-057 |
| v0.5 | 2026-10-07 | Theo góp ý của Hanna ngày 06/10, 07/10 và cách viết ở bản `SGS-DTP_TestCase1_v1.4`. Rule 8: case bấm nút gửi mà không lưu được vào nhóm Không thành công; nhóm Không thành công đứng trước Thành công (ngược câu cũ). Rule 9 viết lại: kết quả kiểm ở nơi hành động trả về, nơi khác trong cùng sheet kiểm ở khu vực của nó, mỗi loại một case (thay câu cũ "hiện ở n nơi thì n case"). Rule 11: được đánh lại số khi chưa có kết quả chạy. Rule 13: kết quả suy ra cũng là chưa có căn cứ. Rule 14: bỏ `{{…}}`; dữ liệu tester nhập ghi cụ thể, dữ liệu có sẵn chưa xác định ghi `[tên]`; mỗi trường một dòng; text nguyên văn trong ngoặc kép. Rule 18: Times New Roman 10 cho mọi ô, kể cả ô trống và kiểu mặc định của cột. Rule 30: mỗi loại đúng một TC, bỏ "mỗi nơi hiển thị một TC". Thêm rule 31 (giá trị tính toán), 32 (dấu nháy đơn đầu ô), 33 (chữ dạng NFC). Tất cả **chờ duyệt**; ba chỗ còn **chờ Hanna chọn**: thứ tự hai nhóm ở rule 8, cách ghi Expected ở rule 31, việc đánh lại số ở rule 11. | FB-042 · FB-043 · FB-044 · FB-045 · FB-046 · FB-047 · FB-048 · FB-049 · FB-016 |
| v0.4 | 2026-10-06 | Rule 14: Pre-condition không ghi mở màn hình đang test (đó là Step 1); muốn tới màn B qua nhiều thao tác ở màn A thì liệt kê thao tác ở Pre-condition. Thêm rule 30: case kiểm hiển thị sau khi tạo, mỗi loại một TC, đủ mọi thông tin của form. Đề xuất của AI theo góp ý của Hanna — **chờ duyệt** | FB-040, FB-041 |
| v0.3 | 2026-10-05 | Rule 3: "màn hình" tính theo mục menu. Rule 4: màn có danh sách xếp theo vòng đời dữ liệu, trạng thái rỗng trước. Rule 7: ví dụ tiếng Anh, mỗi ô một thứ tiếng, tên nhóm kiểm theo bảng từ. Rule 12: không trỏ sang TC khác, mỗi mục một dòng. Rule 14 viết lại theo góc nhìn Tester: dòng đăng nhập `Logged in as <role>`, dữ liệu và nhãn ghi thẳng trong ô, Step là thao tác cụ thể. Rule 15: tên nhóm tiếng Anh, case Bảo mật làm được trên giao diện. Rule 16: ngôn ngữ file TC theo `profile.md`. Rule 22 bỏ sheet `_Data`, `_Labels`. Thêm mục G: chia sheet (rule 24–28) và rule 29 — TC gọi API chỉ khi tester được gọi API, ở sheet `API` riêng. Hanna duyệt 05/10, trừ phần **chờ duyệt**: rule 3 và 24–28 (chia sheet), rule 19 (căn giữa theo chiều dọc như file mẫu, đề xuất của AI). | FB-029 · FB-030 · FB-035 · FB-031 · FB-032 · FB-034 · FB-036 · FB-039 · FB-013 |
| v0.3 | 2026-10-02 | Thêm rule 24: form theo file mẫu của dự án — sheet mới thêm vào file mẫu bằng cách nhân bản một sheet TC đã duyệt; bố cục theo file mẫu, phông và màu theo rule 22 với bảng màu lấy một màu nền tiêu đề của file mẫu; chưa có file mẫu thì hỏi. **Chờ duyệt.** | FB-019 · FB-016 |
| v0.2 | 2026-10-02 | Đổi tên cột `Chờ text` → `Open question` (rule 13, 16, 23). Thêm rule 22: định dạng đồng nhất toàn bộ — một phông, một bảng màu cho mọi sheet và mọi file. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: thứ tự nguồn chân lý, một màn một sheet, bốn cấp Classification, quy tắc chưa có căn cứ thì để trống, quy tắc chuyển ngôn ngữ, và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô). | FB-010 · FB-011 · FB-012 · FB-013 |
