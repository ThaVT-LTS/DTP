# Câu hỏi làm rõ — Quan_ly_tai_lieu_mockup5.pdf

> Phiên bản: v0.2 · Trạng thái: chờ trả lời. Cổng 1 mở khi 4 câu CHẶN (Q-01 → Q-04) có câu trả lời.
> Cách trả lời: ghi vào dòng **Trả lời** của từng câu, hoặc nhắn trong chat, ví dụ "Q-03: đồng ý đề xuất", "Q-10: (2) cấm thêm dấu #".

Vị trí `K1`–`K4`, `tr.N`, `#n` trỏ tới `uc-inventory.md`; `F-nn` trỏ tới `analysis.md` §5. `«…»` là text nguyên văn của mockup.

| Mức | Số câu | Câu | Đã trả lời một phần |
|---|---|---|---|
| CHẶN | 4 | Q-01 → Q-04 | — |
| QUAN TRỌNG | 15 | Q-05 → Q-19 | Q-06, Q-08, Q-10, Q-13 (02/10) |
| NHỎ | 1 | Q-20 | — |

---

## CHẶN

### Q-01 · Nguồn yêu cầu và trạng thái duyệt của mockup bản 5
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-01
- **Vị trí:** toàn bộ `Quan_ly_tai_lieu_mockup5.pdf` (15 trang)
- **Vấn đề:**
  - Mới chỉ có mockup, không có UC hay SRS đi kèm.
  - Chưa biết bản 5 đã được khách hàng hoặc PO duyệt chưa.
  - Không có các bản trước, nên không biết bản này đã đổi gì.
- **Ảnh hưởng:** theo `rules/common.md` rule 9, kết quả mong đợi phải dẫn về tài liệu yêu cầu hoặc bản thiết kế đã duyệt. Mockup chưa duyệt thì cả test basis không có căn cứ.
- **Đề xuất mặc định:**
  - Coi mockup bản 5 là bản thiết kế đã duyệt và là nguồn duy nhất.
  - Mọi hành vi không được vẽ ghi `[CHỜ Q-nn]`, không tự đặt.
  - Khi có UC hoặc SRS: chạy lại ba-analysis ở chế độ B.
  - PDF này được in từ Chromium. Nếu có bản HTML gốc, bạn gửi kèm để mình đọc các trạng thái tương tác.
- **Trả lời:**

### Q-02 · Dự án, khách hàng và ngôn ngữ giao diện của hệ thống thật
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-02
- **Vị trí:** K1 #1 «F», K1 #9 «Quản lý dự án › LTS › Quản lý tài liệu»; toàn bộ text đang là tiếng Việt
- **Vấn đề:**
  - Mockup không ghi tên dự án hay khách hàng.
  - Chưa biết hệ thống thật chạy ngôn ngữ nào.
  - [SUY LUẬN] Logo «F» và cấu trúc «Quản lý dự án» › … › «Quản lý tài liệu» giống bộ TC `FEEC_PM_IT_Test_Case.xlsx` mà sổ FB nhắc tới. Bộ đó có sheet DM-L0001 là module quản lý tài liệu.
- **Ảnh hưởng:**
  - `rules/ba.md` rule 5: nhãn, nút và thông báo phải chép nguyên văn vào test basis, để làm kết quả mong đợi và làm locator.
  - `rules/tc-authoring.md` rule 16: TC viết theo ngôn ngữ mà hệ thống chạy.
  - Sai ngôn ngữ thì toàn bộ text mong đợi đều sai.
- **Đề xuất mặc định:**
  - Hệ thống chạy tiếng Việt, đúng như mockup.
  - Thư mục dự án đặt là `projects/quan-ly-tai-lieu/`.
  - `profile.md` điền theo câu trả lời của bạn.
- **Trả lời:**
- **Cập nhật 02/10 (gợi ý, câu hỏi vẫn mở):** bạn đã chỉ định bộ TC `FEEC_PM_IT_Test_Case_Document_v3.xlsx` (Function Name 「DM-L0001_図書管理」) làm nguồn cho module này (FB-021), và yêu cầu chuyển thông báo tiếng Nhật sang tiếng Việt (FB-022). [SUY LUẬN: đây là module quản lý tài liệu của dự án FEEC, và hệ thống mới chạy tiếng Việt.] Câu này đóng khi bạn xác nhận.

### Q-03 · Vai trò và phân quyền
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-03
- **Vị trí:** toàn bộ; mockup vẽ cho một người dùng duy nhất («Fe», K1 #5)
- **Vấn đề:** không có vai trò nào. Chưa biết ai được:
  - xem, tạo thư mục, tải lên;
  - đổi tên, di chuyển, sao chép, xoá;
  - khôi phục, xoá vĩnh viễn;
  - tải lên phiên bản mới, sao chép liên kết.

  Cũng chưa biết người không thuộc dự án thì thấy gì.
- **Ảnh hưởng:**
  - `rules/tester.md` rule 5: mỗi hành động ghi phải có TC cho vai trò không được phép, gồm bị ẩn trên UI và bị chặn ở API.
  - `rules/tc-authoring.md` rule 15: mỗi khu vực ghi dữ liệu cần có case Phân quyền và case Bảo mật.
  - Không có ma trận phân quyền thì checklist "Sẵn sàng bàn giao" của test basis không qua được.
- **Đề xuất mặc định:**
  - Hai vai trò:
    1. Thành viên dự án: làm được mọi thao tác trên mockup, trừ «Xoá vĩnh viễn».
    2. Quản lý dự án: làm được mọi thao tác.
  - Người không thuộc dự án không thấy mục «Quản lý tài liệu»; mở URL trực tiếp thì bị chặn.
  - Không vai trò nào sửa được «Thư mục công trình cũ».
- **Trả lời:**
- **Cập nhật 02/10 (gợi ý, câu hỏi vẫn mở):** bộ TC có nhắc vai trò. TC_139 và TC_141 ghi 「1. Tạo file trên role ES/PM」 [SUY LUẬN: dự án có hai vai trò ES và PM]. Nếu đúng như vậy, cần bạn cho biết mỗi vai trò làm được những thao tác nào.

### Q-04 · Phạm vi test của module
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-04, F-05
- **Vị trí:** `uc-inventory.md` §C (22 chức năng do AI đặt ID); `analysis.md` §3
- **Vấn đề:** chưa có tiêu chí phạm vi. AI tạm chia như sau:
  - 9 chức năng trong phạm vi;
  - 13 chức năng chưa đủ thông tin;
  - ngoài phạm vi: thanh biểu tượng bên trái, «Chi tiết dự án», «Quản lý báo giá».
- **Ảnh hưởng:** `rules/ba.md` rule 3. Chưa chốt phạm vi thì chưa xuất được test basis.
- **Đề xuất mặc định:**
  - Chấp nhận cách chia ở `analysis.md` §3.
  - 13 chức năng chưa đủ thông tin vẫn giữ trong phạm vi, nhưng chỉ thiết kế test khi đã có câu trả lời của câu hỏi liên quan (Q-05 → Q-19).
  - Phần ngoài phạm vi không test ở đợt này.
- **Trả lời:**

---

## QUAN TRỌNG

### Q-05 · Thư mục gốc và bộ lọc «Tất cả các bước»
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-06, F-07
- **Vị trí:** K1 #13 «Tất cả các bước» «⌄» (không trang nào mở danh sách này); K2 dòng 1–2; tr.3
- **Vấn đề:**
  1. Danh sách các bước gồm những gì, lấy từ đâu?
  2. Tệp và thư mục được gắn với bước bằng cách nào? Hộp thoại tạo thư mục (tr.7) và tải lên (tr.8) đều không có trường bước.
  3. «Quản lý rủi ro» và «Xem xét chi phí» cùng một thời điểm «19/08/2026 20:37», và cột «Người cập nhật cuối ⇅» đều là «—». Có phải hệ thống tạo sẵn hai thư mục này theo bước không?
  4. Nếu đúng như vậy, thì đổi tên, di chuyển hay xoá chúng (tr.3 cho phép) có ảnh hưởng tới việc lọc theo bước không?
- **Ảnh hưởng:** chưa viết được TC cho bộ lọc theo bước (UC-DOC-004) và cho thao tác trên hai thư mục gốc.
- **Đề xuất mặc định:**
  - Mỗi tệp và thư mục có một thuộc tính bước, lấy từ danh sách bước của dự án. Chọn một bước thì chỉ hiện các mục của bước đó.
  - Hai thư mục gốc là thư mục thường, đổi tên, di chuyển, xoá được như tr.3.
  - Bộ lọc theo bước để ngoài phạm vi test cho tới khi có danh sách bước.
- **Trả lời:**

### Q-06 · Bộ lọc phạm vi và «Thư mục công trình cũ»
- **Mức:** QUAN TRỌNG · **Trạng thái:** Trả lời một phần · Hanna · 2026-10-02 · **Phát hiện:** F-08, F-09, F-40
- **Vị trí:** tr.6 «Tài liệu dự án ✓», «Thư mục công trình cũ»; K2 dòng 3 «Thư mục hệ thống»; ô chú giải ở tr.5
- **Vấn đề:**
  1. Chọn «Thư mục công trình cũ» trong bộ lọc thì danh sách hiện gì?
  2. Đang chọn «Tài liệu dự án», vì sao vẫn thấy dòng «Thư mục công trình cũ»?
  3. Thư mục hệ thống có mở được không, bên trong có gì? Có tạo, tải lên, đổi tên hay xoá tệp bên trong được không?
  4. Quy tắc "không thể xoá, đổi tên hay di chuyển" có chặn ở máy chủ không, hay chỉ ẩn nút?
- **Ảnh hưởng:**
  - UC-DOC-001 và UC-DOC-005.
  - Case bảo vệ thư mục hệ thống: ẩn nút chưa phải là phân quyền (tc-framework §1 R3).
- **Đề xuất mặc định:**
  - «Tài liệu dự án» hiện mọi mục của dự án, cùng dòng lối tắt «Thư mục công trình cũ».
  - Chọn «Thư mục công trình cũ» thì chỉ hiện nội dung của thư mục đó, ở chế độ chỉ xem.
  - Bên trong thư mục này không tạo, tải lên, đổi tên, di chuyển hay xoá được gì.
  - Thao tác ghi gọi thẳng API vào thư mục này đều bị từ chối.
- **Trả lời:** "Tạo folder chỉ được sửa tên, di chuyển trong: Tài liệu dự án, hoặc Thư mục công trình cũ > ko được switch cho nhau"
- **Cập nhật 02/10:**
  - **Đã rõ:** bên trong «Thư mục công trình cũ» có thư mục, và các thư mục đó đổi tên, di chuyển được trong phạm vi của nó (`analysis.md` §7, BR-03). Phần "chỉ xem" trong đề xuất mặc định cũ không còn đúng (F-40).
  - **Còn mở:**
    - (1) Chọn «Thư mục công trình cũ» trong bộ lọc thì danh sách hiện gì?
    - (2) Vì sao khi đang lọc «Tài liệu dự án» vẫn thấy dòng này?
    - (3) Bên trong thư mục này có tạo thư mục, tải lên, xoá được không?
    - (4) Quy tắc bảo vệ chính thư mục hệ thống có chặn ở API không?
  - **Đề xuất mặc định mới:**
    - Bên trong «Thư mục công trình cũ» làm được mọi thao tác như ở «Tài liệu dự án» (tạo, tải lên, đổi tên, di chuyển, xoá), nhưng chỉ trong phạm vi của nó.
    - Bản thân «Thư mục công trình cũ» thì không xoá, đổi tên hay di chuyển được, kể cả khi gọi thẳng API.

### Q-07 · Tìm kiếm và «Xoá lọc»
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-10, F-11
- **Vị trí:** K1 #11 «Tìm theo tên tệp…», #12 «Tìm kiếm», #15 «Xoá lọc»
- **Vấn đề:**
  1. Tìm trong thư mục hiện tại hay trong cả dự án? Có tìm vào thư mục con không? Có tìm theo tên thư mục không?
  2. Có khớp một phần không? Có phân biệt hoa thường, có phân biệt dấu không?
  3. Bấm Enter có tìm luôn không? Ô tìm giới hạn bao nhiêu ký tự?
  4. Kết quả tìm và trạng thái không có kết quả hiển thị thế nào? Hiện chưa có màn nào, nên cần text nguyên văn.
  5. Khi nào «Xoá lọc» bật? Bấm vào có xoá cả từ khoá không?
  6. Từ khoá và bộ lọc có được giữ khi mở thư mục con hoặc đổi trang không?
- **Ảnh hưởng:** UC-DOC-003 và UC-DOC-005. Pattern P10 cần text nguyên văn của trạng thái không có kết quả.
- **Đề xuất mặc định:**
  - Tìm trong thư mục hiện tại và mọi thư mục con, theo cả tên tệp và tên thư mục.
  - Khớp một phần, không phân biệt hoa thường, có phân biệt dấu.
  - Enter tương đương bấm «Tìm kiếm»; ô tìm tối đa 255 ký tự.
  - «Xoá lọc» bật khi có từ khoá hoặc khi một bộ lọc khác mặc định; bấm vào thì đưa cả từ khoá lẫn bộ lọc về mặc định.
  - Không có kết quả thì hiện trạng thái rỗng giống tr.9 (cần bạn cho text nguyên văn).
  - Mở thư mục con thì giữ từ khoá và bộ lọc.
- **Trả lời:**

### Q-08 · Điều hướng thư mục nhiều cấp
- **Mức:** QUAN TRỌNG · **Trạng thái:** Trả lời một phần · Hanna · 2026-10-02 · **Phát hiện:** F-12, F-35
- **Vị trí:** tr.9–13 tiêu đề «Quản lý tài liệu › Quản lý rủi ro»; K1 #9 breadcrumb; tr.7 «Thư mục mới sẽ được tạo tại: Quản lý tài liệu»
- **Vấn đề:**
  1. Bấm «Quản lý tài liệu» trong tiêu đề thì có về gốc không? Các đoạn «Quản lý dự án» và «LTS» của breadcrumb có bấm được không?
  2. Thư mục sâu 3–5 cấp thì tiêu đề hiển thị thế nào, có rút gọn không?
  3. Có giới hạn số cấp thư mục không?
  4. Ở thư mục con, dòng "sẽ được tạo tại" hiện tên thư mục cha hay cả đường dẫn?
  5. URL có đổi theo thư mục đang mở không, tức là mở lại hay chia sẻ được đúng thư mục đó không?
- **Ảnh hưởng:** nhóm Redirect của UC-DOC-002: đường vào và ra, deep link, quay lại.
- **Đề xuất mặc định:**
  - Mỗi đoạn trong tiêu đề đều bấm được để về đúng cấp đó.
  - Không giới hạn số cấp.
  - Dòng "sẽ được tạo tại" hiện cả đường dẫn.
  - URL chứa id của thư mục; mở thẳng URL vẫn vào được nếu có quyền.
- **Trả lời:** "Không được tạo quá 20 cấp folder > tức là folder trong folder không được quá 20 cấp" — trả lời ý (3)
- **Cập nhật 02/10:**
  - **Đã rõ:** tối đa 20 cấp thư mục lồng nhau (`analysis.md` §7, BR-02).
  - **Còn mở:** các ý (1), (2), (4), (5) ở trên, cùng hai ý mới:
    - (6) Đếm cấp thế nào? Thư mục nằm ngay ở gốc có tính là cấp 1 không? «Tài liệu dự án» và «Thư mục công trình cũ» có tính là một cấp không? (F-35)
    - (7) Lỗi vượt cấp hiện lúc nào: khi mở hộp thoại (nút bị tắt), hay khi bấm «Lưu»?
  - **Đề xuất mặc định cho (6), (7):** theo cách TC_080 và TC_081 đang đếm. Thư mục nằm ngay ở gốc là cấp 1; gốc của mỗi phạm vi không tính là một cấp; nên sâu nhất là cấp 20. Lỗi hiện khi bấm «Lưu», text là MS-02.

### Q-09 · Quy ước chung của danh sách
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-13, F-14, F-15, F-16, F-42
- **Vị trí:** K1 #19–#27; K2; K3; tr.13; tr.15
- **Vấn đề:**
  1. Thứ tự sắp xếp mặc định là gì?
  2. Khi sắp xếp theo một cột, thư mục có còn đứng trên tệp không? Cột «Dung lượng ⇅» xếp dòng «—» ở đâu?
  3. «50 dòng / trang» có những lựa chọn nào? «‹ Trước» và «Sau ›» hiển thị thế nào khi đang ở trang đầu hoặc trang cuối?
  4. Với thư mục, cột «Người cập nhật cuối ⇅» và «Cập nhật lần cuối ⇅» tính theo gì? Vì sao thư mục gốc có ngày nhưng không có người?
  5. Ngày giờ theo múi giờ nào? Dung lượng dùng đơn vị nào (1 MB = 1000 hay 1024 KB), làm tròn mấy chữ số, dấu thập phân là dấu gì?
- **Ảnh hưởng:**
  - Kết quả mong đợi của mọi TC hiển thị danh sách.
  - Các pattern P7, P9, P12.
  - Mục "Quy ước chung" của test basis.
- **Đề xuất mặc định:**
  - Mặc định thư mục đứng trước, tệp xếp theo «Cập nhật lần cuối ⇅» giảm dần [SUY LUẬN từ K3]. Sắp xếp theo cột nào thì thư mục vẫn ở trên; dòng «—» xếp cuối.
  - Lựa chọn 20, 50, 100 dòng; mặc định 50. «‹ Trước» tắt ở trang đầu, «Sau ›» tắt ở trang cuối.
  - Với thư mục, hai cột này ghi người và thời điểm của lần đổi tên, hoặc lần thêm/xoá mục ngay bên trong, gần nhất. Thư mục do hệ thống tạo thì cột người ghi «—».
  - Giờ Việt Nam (UTC+7). 1 MB = 1024 KB, giữ một chữ số thập phân, dấu thập phân là dấu phẩy.
- **Trả lời:**
- **Cập nhật 02/10:** thêm bằng chứng cho ý (5). TC_150 ghi 「YYYY-MM-DD HH:MM」, còn mockup ghi «30/09/2026 15:02» (F-42). Đề xuất mặc định: theo mockup, tức DD/MM/YYYY HH:mm.

### Q-10 · Quy tắc tên thư mục
- **Mức:** QUAN TRỌNG · **Trạng thái:** Trả lời một phần · Hanna · 2026-10-02 · **Phát hiện:** F-17, F-36, F-37, F-38
- **Vị trí:** tr.7 «Tên thư mục *», «Nhập tên thư mục», «Còn 255 ký tự (tối đa 255)», «Huỷ», «Lưu»
- **Vấn đề:**
  1. Để trống, hoặc chỉ nhập khoảng trắng, thì báo lỗi gì (text nguyên văn) và hiện ở đâu?
  2. Ký tự nào không được dùng?
  3. Có chặn trùng tên trong cùng thư mục cha không? Có phân biệt hoa thường, có bỏ khoảng trắng hai đầu khi so không? Text lỗi là gì?
  4. Nhập quá 255 ký tự thì chặn không cho gõ hay báo lỗi? Dán một chuỗi dài hơn thì sao? Bộ đếm có giảm theo từng ký tự khi gõ không?
  5. «Lưu» có tắt khi ô còn rỗng không? Mockup đang vẽ nút bật.
  6. Lưu xong thì hộp thoại đóng, có thông báo không, thư mục mới nằm ở đâu trong danh sách?
  7. Quy tắc này có dùng chung cho Đổi tên không?
- **Ảnh hưởng:** nhóm Validation của UC-DOC-007, và của UC-DOC-010 nếu dùng chung; các pattern P1 và P6.
- **Đề xuất mặc định:**
  - Tên bắt buộc, bỏ khoảng trắng hai đầu, dài 1–255 ký tự sau khi bỏ.
  - Cấm các ký tự / \ : * ? " < > |.
  - Không cho trùng tên trong cùng thư mục cha (không phân biệt hoa thường).
  - Đủ 255 ký tự thì không gõ thêm được; bộ đếm giảm theo từng ký tự.
  - «Lưu» luôn bật; bấm khi có lỗi thì lỗi hiện ngay dưới ô.
  - Lưu xong thì đóng hộp thoại, hiện thông báo thành công; thư mục mới nằm theo thứ tự sắp xếp hiện tại.
  - Dùng chung cho Đổi tên.
  - Text lỗi: cần bạn cho nguyên văn, mình không tự đặt.
- **Trả lời:** "Phần tạo mới đang chỉ cho tạo tên ko quá 255 ký tự, kể cả Full width hay half width" — trả lời một phần ý (4)
- **Cập nhật 02/10:**
  - **Đã rõ:** tên dài tối đa 255 ký tự; ký tự Full-width và Half-width đều tính 1 ký tự (`analysis.md` §7, BR-01).
  - **Bộ TC trả lời thêm, cần bạn xác nhận:**
    - Trùng tên thì tên mới thêm số thứ tự (TC_143). Nhưng đổi tên trùng lại báo lỗi (TC_144) (F-38).
    - Tên quá 255 ký tự: TC_082 ghi 「Hệ thống tự cắt ký tự và báo lỗi」 (F-36). Text lỗi là MS-01 (dịch tạm).
  - **Còn mở:**
    - (1) Text lỗi khi để trống hoặc chỉ nhập khoảng trắng.
    - (2) Ký tự nào bị cấm.
    - (3) Định dạng số thứ tự khi trùng tên. Vì sao đổi tên trùng lại báo lỗi? So trùng có phân biệt hoa thường không? "ＡＢＣ" (Full-width) và "ABC" có bị coi là trùng không?
    - (4) Quá 255 ký tự thì chặn không cho gõ thêm, hay cắt rồi báo lỗi? Dán một chuỗi dài hơn thì sao?
    - (5) Nút «Lưu» có tắt khi ô rỗng không?
    - (6) Lưu xong thì sao?
    - (7) Đổi tên có dùng chung quy tắc này không?
    - (8) Mới: đếm 255 ký tự thế nào? Chữ có dấu ở dạng tổ hợp và emoji tính 1 hay 2 ký tự? (F-37)
    - (9) Mới: bấm «Huỷ», «×», nhấn Esc hoặc bấm ra ngoài hộp thoại thì sao?
  - **Đề xuất mặc định mới cho (3), (8), (9):**
    - Trùng tên thì thêm hậu tố " (1)", " (2)"… So trùng không phân biệt hoa thường; Full-width và Half-width là hai ký tự khác nhau.
    - Đếm theo ký tự nhìn thấy: chữ có dấu tiếng Việt luôn tính 1, emoji tính 1.
    - «Huỷ», «×» và Esc đóng hộp thoại, không tạo thư mục; bấm ra ngoài hộp thoại thì không đóng.

### Q-11 · Tải tệp lên
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-18
- **Vị trí:** tr.2 «Tải tệp lên»; chưa có màn tiếp theo
- **Vấn đề:**
  1. Có hộp thoại riêng giống tr.8 không?
  2. Cho phép loại tệp nào? Mỗi tệp tối đa bao nhiêu? Mỗi lần tải được bao nhiêu tệp?
  3. Tệp trùng tên với tệp đã có thì ghi đè, thêm thành phiên bản mới, hay tự đổi tên?
  4. Có thanh tiến trình không? Huỷ giữa chừng hoặc mất mạng thì sao?
  5. Các text lỗi nguyên văn là gì?
- **Ảnh hưởng:** chưa thiết kế được UC-DOC-008. Pattern P4 là nhóm sinh nhiều TC nhất.
- **Đề xuất mặc định:**
  - Hộp thoại giống tr.8 nhưng chọn được nhiều tệp.
  - Cho mọi loại tệp, trừ tệp chạy được (ví dụ .exe, .bat); tối đa 5 GB mỗi lần tải.
  - Trùng tên thì hỏi người dùng chọn một trong hai: thêm thành phiên bản mới của tệp cũ, hoặc giữ cả hai (tệp mới thêm hậu tố số).
  - Có thanh tiến trình và nút huỷ. Mất mạng thì báo lỗi; tệp tải chưa xong thì không lưu.
- **Trả lời:**

### Q-12 · Tải thư mục lên
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-19, F-41
- **Vị trí:** tr.8 «Dung lượng tối đa 5 GB», «Chọn thư mục», «Chọn tệp ZIP», «Đóng»
- **Vấn đề:**
  1. 5 GB tính cho cả lần tải hay cho từng tệp?
  2. Tệp ZIP có được giải nén thành cây thư mục không? ZIP bị hỏng hoặc có mật khẩu thì sao?
  3. Thư mục trùng tên với một thư mục đã có thì gộp, ghi đè hay đổi tên?
  4. Có giới hạn số cấp, số tệp không?
  5. Tệp bên trong có bị chặn theo loại không?
  6. Tiến trình và kết quả hiển thị thế nào? Bấm «Đóng» hoặc «×» khi đang tải thì sao?
  7. Thư mục rỗng có được tạo không?
- **Ảnh hưởng:** UC-DOC-009, gồm Validation (biên 5 GB) và Abnormal (mất mạng, đóng giữa chừng).
- **Đề xuất mặc định:**
  - 5 GB cho cả một lần tải.
  - ZIP được giải nén, giữ nguyên cấu trúc thư mục.
  - Thư mục trùng tên thì thư mục mới thêm hậu tố số.
  - Không giới hạn số cấp.
  - Tệp chạy được bị bỏ qua và được liệt kê trong kết quả.
  - Đóng hộp thoại không huỷ việc tải; tiến trình chuyển xuống góc màn.
  - Thư mục rỗng vẫn được tạo.
- **Trả lời:**
- **Cập nhật 02/10:** thêm ý (8). Giới hạn 20 cấp (Q-08) có áp cho việc tải thư mục và tệp ZIP lên không? Hiện còn 15 TC tải lên ghi 10 cấp (F-41). Đề xuất mặc định: có, cùng giới hạn 20 cấp, và tính cả số cấp của thư mục đích.

### Q-13 · Đổi tên, Di chuyển, Sao chép, Xoá
- **Mức:** QUAN TRỌNG · **Trạng thái:** Trả lời một phần · Hanna · 2026-10-02 · **Phát hiện:** F-20, F-39
- **Vị trí:** tr.3 «Đổi tên», «Di chuyển», «Xoá»; tr.11 «Sao chép»; tr.4–5 «Di chuyển», «Xoá»
- **Vấn đề:** cả bốn thao tác đều chưa có màn.
  1. **Đổi tên:** dùng hộp thoại giống tr.7 không? Đổi tên tệp có sửa được phần mở rộng không?
  2. **Di chuyển:** chọn thư mục đích bằng cách nào? Có chặn di chuyển vào chính nó hoặc vào thư mục con của nó không? Ở đích đã có mục trùng tên thì sao?
  3. **Sao chép:** bản sao nằm ở đâu, tên là gì? Có chép theo các phiên bản cũ không?
  4. **Xoá:** có hộp thoại xác nhận không, text là gì? Xoá xong mục có vào «Thùng rác» ngay không? Xoá thư mục còn nội dung bên trong thì sao?
  5. Mỗi thao tác xong có thông báo gì?
- **Ảnh hưởng:** chưa thiết kế được UC-DOC-010 → UC-DOC-013; các pattern P1, P2, P3, P6.
- **Đề xuất mặc định:**
  - **Đổi tên:** hộp thoại và quy tắc như Q-10; không cho sửa phần mở rộng.
  - **Di chuyển:** hộp thoại hiện cây thư mục; không cho chọn chính nó hoặc thư mục con của nó; đích đã có mục trùng tên thì báo lỗi.
  - **Sao chép:** bản sao nằm cùng thư mục, tên thêm hậu tố; chỉ chép phiên bản hiện tại.
  - **Xoá:** luôn hỏi xác nhận, có hiện tên mục; xoá xong vào «Thùng rác» cùng toàn bộ nội dung bên trong.
  - Mỗi thao tác xong đều có thông báo.
  - Text của các hộp thoại: cần bạn cho nguyên văn.
- **Trả lời:** "Tạo folder chỉ được sửa tên, di chuyển trong: Tài liệu dự án, hoặc Thư mục công trình cũ > ko được switch cho nhau" — trả lời một phần ý (2)
- **Cập nhật 02/10:**
  - **Đã rõ:** không di chuyển được thư mục qua lại giữa «Tài liệu dự án» và «Thư mục công trình cũ»; đổi tên và di chuyển chỉ trong cùng phạm vi (`analysis.md` §7, BR-03).
  - **Còn mở:**
    - Chặn bằng cách nào: thư mục đích bị ẩn hoặc tắt, hay báo lỗi? Text là gì?
    - Quy tắc này có áp cho tệp không?
    - Chọn hàng loạt có lẫn hai phạm vi thì sao?
    - Các ý (1), (3), (4), (5) ở trên.
  - **Đề xuất mặc định:**
    - Hộp thoại chọn đích chỉ hiện cây thư mục của phạm vi hiện tại.
    - Gọi thẳng API để chuyển sang phạm vi kia thì bị từ chối.
    - Áp cho cả tệp.
    - Chọn lẫn hai phạm vi thì nút «Di chuyển» tắt.

### Q-14 · Chọn hàng loạt và thao tác theo loại mục
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-21, F-22
- **Vị trí:** tr.3 (menu thư mục), tr.4–5 (thanh hàng loạt), tr.11 (menu tệp); tr.9 (checkbox tiêu đề khi danh sách rỗng); `uc-inventory.md` §D
- **Vấn đề:**
  1. Thư mục có tải xuống được không? Thanh hàng loạt có «Tải xuống» khi chỉ chọn thư mục, nhưng menu «⋮» của thư mục thì không có.
  2. Tải xuống nhiều mục có gom thành một tệp ZIP không? Có giới hạn dung lượng không?
  3. «Sao chép» chỉ có cho tệp và không có trong thanh hàng loạt. Đó có phải chủ ý không?
  4. Chọn tất cả là chọn trang hiện tại hay mọi trang?
  5. Lựa chọn có được giữ khi đổi trang, lọc hoặc mở thư mục không?
  6. «×» có bỏ chọn hết không?
  7. Chọn lẫn cả tệp và thư mục thì thanh hiện những nút nào?
  8. Danh sách rỗng (tr.9) thì checkbox tiêu đề có bấm được không?
- **Ảnh hưởng:** UC-DOC-014 và UC-DOC-015; các pattern P3 (lặp theo lối vào) và P12.
- **Đề xuất mặc định:**
  - Thư mục tải xuống được ở cả hai nơi, tức là thêm «Tải xuống» vào menu thư mục. Nhiều mục thì tải về thành một tệp ZIP.
  - «Sao chép» chỉ cho tệp, và chỉ có trong menu «⋮».
  - Chọn tất cả là chọn các mục chọn được trong trang hiện tại.
  - Đổi trang, lọc hoặc mở thư mục thì bỏ hết lựa chọn.
  - «×» bỏ chọn hết và ẩn thanh.
  - Danh sách rỗng thì checkbox tiêu đề tắt.
- **Trả lời:**

### Q-15 · Xem trước
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-23, F-24
- **Vị trí:** tr.12–13 (K4)
- **Vấn đề:**
  1. Nghĩa chính thức, nhãn hoặc tooltip của «−» «+» «⇔» «⇕» «↺» «↻» là gì?
  2. Phóng nhỏ nhất và lớn nhất là bao nhiêu, mỗi lần bấm đổi bao nhiêu? Có hiện mức phóng (%) và có nút đặt lại không?
  3. Tệp nhiều tờ («Tờ 1/3») chuyển tờ bằng cách nào?
  4. Những định dạng nào xem trước được (PDF, ảnh, DOCX, XLSX, DWG)? Định dạng không xem được thì hiện gì (text nguyên văn)?
  5. «‹», «›» và phím mũi tên có bỏ qua thư mục không? Có quay vòng ở đầu và cuối danh sách không? Có theo thứ tự đang sắp xếp và lọc không? Có chỉ trong trang hiện tại không?
  6. Tệp hỏng hoặc tệp rất lớn thì sao?
- **Ảnh hưởng:** UC-DOC-016. Pattern P8 yêu cầu kiểm từng nút điều khiển và giới hạn phóng.
- **Đề xuất mặc định:**
  - «−» thu nhỏ và «+» phóng to, từ 25% đến 400%, mỗi bước 25%.
  - «⇔» vừa chiều ngang, «⇕» vừa chiều dọc.
  - «↺» và «↻» xoay 90°.
  - Tệp nhiều tờ thì cuộn dọc.
  - Xem trước được PDF và ảnh (JPG, PNG). Định dạng khác hiện thông báo không xem trước được, kèm nút tải xuống.
  - Chuyển tệp bỏ qua thư mục, theo đúng thứ tự đang hiện trong danh sách, không quay vòng.
- **Trả lời:**

### Q-16 · Sao chép liên kết
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-25
- **Vị trí:** K4 #2 «Sao chép liên kết» (tr.12–13)
- **Vấn đề:**
  1. Liên kết trỏ tới đâu: tới tệp, tới phiên bản hiện tại, hay tới trình xem?
  2. Ai mở được liên kết? Có cần đăng nhập và là thành viên dự án không?
  3. Bấm xong có thông báo đã sao chép không, text là gì?
  4. Liên kết có còn dùng được khi tệp bị đổi tên, di chuyển, xoá, khôi phục hoặc lên phiên bản mới không?
- **Ảnh hưởng:** UC-DOC-017; Redirect R1 (link chia sẻ) và R3 (người không có quyền mở link).
- **Đề xuất mặc định:**
  - Liên kết mở trình xem của tệp và luôn trỏ tới phiên bản hiện tại.
  - Cần đăng nhập và là thành viên dự án mới mở được.
  - Bấm xong có thông báo đã sao chép.
  - Đổi tên hoặc di chuyển tệp thì liên kết vẫn mở được; tệp nằm trong thùng rác thì liên kết báo không tìm thấy.
- **Trả lời:**

### Q-17 · Quản lý phiên bản
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-26, F-27
- **Vị trí:** tr.13 «Tải lên phiên bản mới», «Tên tệp sẽ không thay đổi. Vui lòng chọn tệp cùng định dạng.», «Phiên bản 2», «Hiện tại», «Phiên bản 1»
- **Vấn đề:**
  1. Chọn tệp khác định dạng thì báo lỗi gì (text nguyên văn)? "Cùng định dạng" xét theo phần mở rộng hay theo nội dung tệp?
  2. Mỗi phiên bản tối đa bao nhiêu dung lượng? Có giới hạn số phiên bản không?
  3. Tải lên xong, phiên bản mới có thành «Hiện tại» không? Dòng trong danh sách có cập nhật «Dung lượng ⇅», «Người cập nhật cuối ⇅», «Cập nhật lần cuối ⇅» theo phiên bản đó không? [SUY LUẬN từ tr.13 so với K3 dòng 2: có.]
  4. Có khôi phục một phiên bản cũ làm bản hiện tại, có xoá phiên bản được không?
  5. Đóng bảng phiên bản bằng cách nào? Bảng không có nút đóng riêng.
  6. Theo dữ liệu mẫu, tệp «Bản vẽ sơ đồ đấu nối CT-VT_rev2.pdf» đã có «Phiên bản 1», còn «Bản vẽ sơ đồ đấu nối CT-VT_rev1.pdf» lại là một tệp riêng đã bị xoá (tr.15). Tên tệp không đổi khi lên phiên bản, nên tên có "rev2" sẽ lệch với số phiên bản. Có quy ước đặt tên nào không?
- **Ảnh hưởng:** UC-DOC-018 và UC-DOC-019; Function (trạng thái phiên bản) và Validation (định dạng, dung lượng).
- **Đề xuất mặc định:**
  - So theo phần mở rộng, không phân biệt hoa thường.
  - Giới hạn dung lượng như khi tải tệp lên (Q-11); không giới hạn số phiên bản.
  - Phiên bản mới thành «Hiện tại»; dòng trong danh sách lấy theo phiên bản hiện tại.
  - Đợt này không có khôi phục hay xoá phiên bản.
  - Bấm lại nút «Quản lý phiên bản» để đóng bảng.
  - Không có quy ước đặt tên.
- **Trả lời:**

### Q-18 · Thùng rác
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-28, F-29
- **Vị trí:** tr.14–15 «Khôi phục», «Xoá vĩnh viễn», «Vị trí ban đầu», «Người xoá», «Thời gian xoá»
- **Vấn đề:**
  1. «Xoá vĩnh viễn» có hộp thoại xác nhận không, text là gì?
  2. Khôi phục xong có thông báo không? Mục có về đúng «Vị trí ban đầu» không?
  3. Vị trí ban đầu đã bị xoá hoặc di chuyển, hoặc ở đó đã có mục trùng tên, thì sao?
  4. Mục nằm trong thùng rác bao lâu? Có tự xoá sau một thời gian không?
  5. Thùng rác là của cả dự án hay của từng thư mục? [SUY LUẬN: của cả dự án, vì tr.15 có mục từ «Quản lý rủi ro» và từ «Xem xét chi phí».]
  6. Xoá một thư mục thì thùng rác hiện một dòng cho thư mục đó, hay hiện từng tệp bên trong?
  7. Làm sao phân biệt tệp với thư mục? Dòng «Ảnh khảo sát hiện trường» không có phần mở rộng, cũng không có biểu tượng.
  8. Khi có nhiều mục thì có tìm kiếm, sắp xếp, phân trang không? Thứ tự mặc định là gì?
- **Ảnh hưởng:** UC-DOC-020 → UC-DOC-022; pattern P2; trạng thái của mục (phụ lục B của `analysis.md`).
- **Đề xuất mặc định:**
  - «Xoá vĩnh viễn» luôn hỏi xác nhận, có ghi số mục sẽ xoá.
  - Khôi phục về đúng vị trí ban đầu và có thông báo.
  - Vị trí ban đầu không còn thì khôi phục về gốc «Quản lý tài liệu». Ở đó đã có mục trùng tên thì mục khôi phục thêm hậu tố số.
  - Giữ 30 ngày, sau đó tự xoá vĩnh viễn.
  - Thùng rác dùng chung cho cả dự án.
  - Xoá một thư mục thì hiện một dòng cho thư mục đó.
  - Có biểu tượng loại như danh sách chính.
  - Xếp theo «Thời gian xoá» giảm dần, phân trang 50 dòng.
- **Trả lời:**

### Q-19 · Thông báo kết quả, lỗi và thao tác đồng thời
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-30
- **Vị trí:** tr.1–15. Không màn nào có thông báo sau thao tác, trạng thái đang tải hay trạng thái lỗi.
- **Vấn đề:**
  1. Mỗi thao tác ghi thành công hay thất bại thì thông báo gì (text nguyên văn), hiện ở đâu?
  2. Trạng thái đang tải danh sách, lỗi mạng, lỗi máy chủ, hết phiên hiển thị thế nào?
  3. Hai người cùng thao tác trên một mục thì sao? Ví dụ cùng đổi tên một lúc, một người xoá khi người kia đang xem trước, hai người cùng tải lên phiên bản mới.
  4. Bấm «Lưu» hai lần liên tiếp thì sao?
- **Ảnh hưởng:**
  - Kết quả mong đợi của mọi TC thao tác ghi: `rules/tc-authoring.md` rule 12 yêu cầu phải quan sát được.
  - Nhóm Abnormal: tc-framework §3 F6.
- **Đề xuất mặc định:**
  - Mỗi thao tác ghi hiện một thông báo ngắn ở góc màn (cần bạn cho text nguyên văn).
  - Lỗi mạng hoặc lỗi máy chủ thì hiện thông báo chung, dữ liệu đang nhập vẫn giữ.
  - Hết phiên thì chuyển tới trang đăng nhập, đăng nhập xong quay lại đúng thư mục đang mở.
  - Thao tác trên một mục đã bị người khác xoá hoặc đổi thì báo lỗi và tải lại danh sách.
  - Bấm hai lần chỉ tạo một bản ghi.
- **Trả lời:**

---

## NHỎ

### Q-20 · Tên gọi và text cần xác nhận
- **Mức:** NHỎ · **Trạng thái:** Mở · **Phát hiện:** F-31, F-32, F-33, F-34
- **Vị trí:** tr.2 so với tr.7; K1 #19; tr.9; tr.5; tr.10, 11, 15; tr.15
- **Vấn đề:**
  1. Menu ghi «Tạo thư mục mới», tiêu đề hộp thoại ghi «Tạo thư mục». Giữ cả hai nhãn?
  2. Cột «Tên tệp ⇅» chứa cả thư mục, và trạng thái rỗng ở tr.9 ghi «Chưa có tệp nào». Có đổi chữ "tệp" thành "tên" hoặc "mục" không? Trạng thái rỗng hiện khi không có mục nào, hay khi chỉ không có tệp?
  3. «Thư mục hệ thống» và «Thư mục đặc biệt» có phải là một không? Nếu là một thì dùng tên nào?
  4. Ô chú giải ở tr.5 và huy hiệu «Dữ liệu mẫu» là giao diện thật hay chú thích của người thiết kế?
  5. Dòng «Đã chọn 2 / 3 mục» ở tr.15 bị mép dưới hộp thoại cắt. Đó có phải lỗi của bản vẽ không?
- **Ảnh hưởng:** text mong đợi trong TC, và locator khi tự động hoá.
- **Đề xuất mặc định:**
  - Giữ nguyên các nhãn như mockup.
  - Trạng thái rỗng ở tr.9 hiện khi thư mục không có mục nào.
  - Ô chú giải ở tr.5 là chú thích thiết kế, không phải giao diện; thư mục hệ thống chỉ mang nhãn «Thư mục hệ thống».
  - «Dữ liệu mẫu» là chú thích, không hiện trên hệ thống.
  - tr.15 là lỗi bản vẽ; trên hệ thống, chân hộp thoại hiện đủ dòng chữ.
- **Trả lời:**

---

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.2 | 2026-10-02 | Ghi trả lời một phần cho Q-06, Q-08, Q-10, Q-13; thêm ý mới cho Q-08 (cách đếm cấp, thời điểm báo lỗi), Q-10 (cách đếm ký tự, Huỷ / ×), Q-12 (20 cấp khi tải lên); thêm bằng chứng cho Q-02, Q-03, Q-09; nối thêm F-35 → F-42 | Trả lời của Hanna 02/10 · FB-021 · FB-022 |
| v0.1 | 2026-10-02 | Bản đầu: 20 câu hỏi từ mockup bản 5 | — |
