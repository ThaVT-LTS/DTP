# Phân tích BA — Quan_ly_tai_lieu_mockup5.pdf (mockup bản 5)

> Phiên bản: v0.2 · Trạng thái: BẢN NHÁP — dừng ở bước 3. Chờ Cổng 1: bạn trả lời 4 câu CHẶN (Q-01 → Q-04) trong `questions.md`. Mới ở v0.2: §7 Tạo mới folder.

| | |
|---|---|
| Nguồn | `docs/source/Quan_ly_tai_lieu_mockup5.pdf` · 15 trang = 15 màn · 680.330 byte · từ v0.2 thêm `docs/source/FEEC_PM_IT_Test_Case_Document_v3.xlsx` (bộ TC cũ, dùng làm đặc tả ngược cho §7 — FB-021) |
| Quy trình | skill ba-analysis v0.2 — chế độ A (phân tích mới), nhánh tài liệu thiết kế/mockup (bước 0 mục 6) · rule common v0.3, ba v0.1, feedback v0.1, tc-authoring v0.2 (rà bộ TC cũ) |
| FB đã nạp | FB-001, FB-010 → FB-016 áp dụng như rule (đang chờ bạn duyệt). FB-002 → FB-009 là đề xuất của AI, chưa áp dụng. Mới ở v0.2: FB-021, FB-022 |
| Ngày | 2026-10-02 |
| Đi kèm | `uc-inventory.md` (lượt 1 của mockup) · `tc-inventory-tao-thu-muc.md` (lượt 1 của bộ TC, phần Tạo mới folder) · `questions.md` |

Quy ước: `«…»` là text chép nguyên văn từ PDF. `「…」` là text chép nguyên văn từ bộ TC FEEC (§7). `K1`–`K4`, `tr.N` và số thứ tự `#n` trỏ tới `uc-inventory.md`; `TC_nnn` và ô như `K94` trỏ tới sheet Document của bộ TC.

---

## 0. Mục đích sản phẩm

1. **Ai dùng.** Thành viên của một dự án trong hệ thống quản lý dự án. Module nằm bên trong từng dự án: breadcrumb «Quản lý dự án › LTS › Quản lý tài liệu», menu bên «Chi tiết dự án» · «Quản lý tài liệu» · «Quản lý báo giá» (K1 #6–#9) [SUY LUẬN: «LTS» là tên hoặc mã của một dự án].
2. **Vấn đề nghiệp vụ.** Gom tài liệu kỹ thuật của dự án về một chỗ, có cấu trúc thư mục. Dữ liệu mẫu gồm bản vẽ đấu nối và mặt bằng trạm biến áp (PDF, DWG), bảng khối lượng và dự toán (XLSX), biên bản họp (DOCX), ảnh khảo sát hiện trường (K3; tr.15) [SUY LUẬN: dự án điện hoặc xây lắp].
3. **Giá trị cốt lõi.** Mỗi giá trị đều có màn minh hoạ:
   - Tìm đúng tài liệu: tìm theo tên, lọc theo bước, lọc theo phạm vi (K1 #11–#14; tr.6).
   - Xem nhanh, không cần tải về: trình xem có phóng to, vừa khung, xoay, chuyển tệp (tr.12).
   - Giữ lịch sử bản sửa của cùng một tệp: «Phiên bản 2» mang nhãn «Hiện tại», «Phiên bản 1» vẫn tải được (tr.13).
   - Không mất tài liệu vì xoá nhầm: «Thùng rác» có «Khôi phục» và «Xoá vĩnh viễn» (tr.14–15).
4. **Ràng buộc định hình thiết kế.**
   - Tệp lớn, nhiều tệp một lúc: tải lên được cả thư mục hoặc tệp ZIP, «Dung lượng tối đa 5 GB» (tr.8).
   - Tài liệu cũ phải giữ nguyên: «Thư mục công trình cũ» mang nhãn «Thư mục hệ thống», không xoá, đổi tên hay di chuyển được (tr.1, tr.5) [SUY LUẬN: tài liệu chuyển sang từ công trình hoặc hệ thống trước].
   - Tài liệu gắn với tiến trình dự án: có bộ lọc «Tất cả các bước» (K1 #13) [SUY LUẬN].
5. **Vì sao cấu trúc như vậy.**
   - Dùng mô hình trình quản lý tệp quen thuộc (cây thư mục, menu «⋮», chọn hàng loạt, thùng rác), để người dùng không phải học lại [SUY LUẬN].
   - Lên phiên bản mà giữ nguyên tên tệp («Tên tệp sẽ không thay đổi.» — tr.13), để liên kết đã chia sẻ không bị gãy [SUY LUẬN: đi cùng nút «Sao chép liên kết» — tr.12].

### Soát ngược — chỗ đi ngược mục đích vừa nêu

Mỗi chỗ thành một phát hiện và một câu hỏi. AI không kết luận đó là lỗi.

| # | Mục đích bị ảnh hưởng | Chỗ đi ngược | Phát hiện | Câu hỏi |
|---|---|---|---|---|
| 1 | Giữ lịch sử bản sửa | Dữ liệu mẫu vẫn lưu bản sửa thành tệp riêng có hậu tố "_rev". Tệp «Bản vẽ sơ đồ đấu nối CT-VT_rev1.pdf» nằm trong thùng rác (tr.15), trong khi tệp «Bản vẽ sơ đồ đấu nối CT-VT_rev2.pdf» đã có «Phiên bản 1» (tr.13). Tên tệp không đổi khi lên phiên bản, nên hậu tố "rev2" sẽ lệch với số phiên bản. | F-27 | Q-17 |
| 2 | Tìm đúng tài liệu | Chỉ tìm được theo tên («Tìm theo tên tệp…»). Chưa rõ tìm trong thư mục hiện tại hay cả dự án, có tìm vào thư mục con không. | F-10 | Q-07 |
| 3 | Tài liệu gắn với tiến trình | Hộp thoại tạo thư mục (tr.7) và tải thư mục lên (tr.8) không có chỗ chọn bước. Vậy chưa biết bộ lọc «Tất cả các bước» dựa vào đâu để lọc. | F-06 | Q-05 |
| 4 | Bảo vệ tài liệu cũ | Đang lọc «Tài liệu dự án» vẫn thấy «Thư mục công trình cũ». Chưa rõ tệp bên trong có được bảo vệ như chính thư mục không. | F-08, F-09 | Q-06 |
| 5 | Không mất tài liệu vì xoá nhầm | Mockup không có bước xác nhận trước «Xoá» (tr.3, 4, 5, 11) và trước «Xoá vĩnh viễn» (tr.15). | F-20, F-28 | Q-13, Q-18 |

---

## 1. Kiểm kê nguồn

- **Đã đọc:** 15/15 trang. Mỗi trang đọc cả ảnh trang lẫn lớp chữ. Sản phẩm lượt 1 là `uc-inventory.md`, gồm:
  - A: 4 khối dùng chung;
  - B: 15 màn;
  - C: 22 chức năng suy ra;
  - D: ma trận thao tác × lối vào;
  - E: phần không đọc được.
- **Loại tài liệu:** bản thiết kế / mockup, nên áp bước 0 mục 6 của skill. Đây không phải danh sách UC (a), cũng không phải UC spec (b). Mockup cho biết màn nào có, phần tử nào có và nhãn đang dùng. Còn hầu hết luồng, business rule, quy tắc validation và thông báo thì không có (§5).
- **Độ phủ hai chiều** (lượt 2, chạy script, không tự khai):

| Kiểm | Kết quả |
|---|---|
| Chiều ngược: cụm chữ trong PDF có trong inventory | 888 / 888 |
| Chiều xuôi: chuỗi «…» của inventory có thật trong PDF, đúng trang đã khai | 272 / 272 |
| Chuỗi «…» trích trong `analysis.md` và `questions.md` có thật trong PDF | 333 / 333 |

Lệnh, chạy từ gốc qa-pipeline:

```
python .claude/skills/ba-analysis/scripts/pdf_text_coverage.py \
  projects/quan-ly-tai-lieu/docs/source/Quan_ly_tai_lieu_mockup5.pdf \
  projects/quan-ly-tai-lieu/docs/analysis/Quan_ly_tai_lieu_mockup-v5/uc-inventory.md \
  --also projects/quan-ly-tai-lieu/docs/analysis/Quan_ly_tai_lieu_mockup-v5/analysis.md \
         projects/quan-ly-tai-lieu/docs/analysis/Quan_ly_tai_lieu_mockup-v5/questions.md
```

Script này mới. AI viết nó trong lần chạy này, vì `extract_uc_list.py` chỉ đọc được bảng xlsx — [ĐỀ XUẤT], chờ duyệt (xem §6).

- **Không đọc được** (chi tiết ở inventory §E):
  - biểu tượng không có chữ ở thanh bên trái;
  - nghĩa của 6 nút ký hiệu trong trình xem;
  - một dòng bị cắt ở tr.15;
  - các trạng thái tương tác mà PDF tĩnh không giữ được;
  - nội dung tệp minh hoạ trong khung xem.

  10 ảnh nhúng trong PDF chỉ là bóng đổ, không có nội dung.
- **Tài liệu được dẫn chiếu nhưng vắng mặt** [CHƯA KIỂM CHỨNG]:
  - các bản mockup trước bản 5;
  - tài liệu yêu cầu của module;
  - các màn «Chi tiết dự án» và «Quản lý báo giá»;
  - hồ sơ dự án «LTS».
- **Dữ liệu minh hoạ:** tr.10, 11, 15 có huy hiệu «Dữ liệu mẫu»; chú thích tr.10 và tr.15 ghi «dữ liệu minh hoạ»; khung xem ở tr.12 ghi «Bản vẽ minh hoạ».
  - Tên người, ngày giờ, dung lượng ở các trang này không dùng làm kết quả mong đợi.
  - Chúng chỉ dùng để suy ra quy tắc hiển thị, và mọi suy ra như vậy đều gắn [SUY LUẬN].

---

## 2. Đối soát số liệu

Mockup không có bảng tổng hợp. Mọi con số tự ghi trên mockup đều được đếm lại từ lớp chữ bằng `pdf_text_coverage.py --count`.

| Hạng mục | Mockup ghi | Đếm lại | Lệch |
|---|---|---|---|
| Lựa chọn khi bấm «Tạo mới» (tr.2) | chú thích «3 lựa chọn» | 3: «Tạo thư mục mới», «Tải tệp lên», «Tải thư mục lên» | Không |
| Mục đã chọn (tr.4) | «1» «mục đã chọn» | 1 dấu «✓» ở dòng; checkbox tiêu đề «–» | Không |
| Chọn tất cả (tr.5) | «2» «mục đã chọn»; chú thích «chọn tất cả 2 mục» | 3 dấu «✓» = 1 ở tiêu đề + 2 ở dòng; dòng thứ ba không có checkbox | Không |
| Bộ đếm ký tự (tr.7) | «Còn 255 ký tự (tối đa 255)» | Ô rỗng: 255 − 0 = 255 | Không |
| Lựa chọn thêm của menu tệp so với menu thư mục (tr.11 so với tr.3) | chú thích «Xem trước, Tải xuống, Sao chép» | Menu tệp có 6 mục, menu thư mục có 3; phần chênh: «Xem trước», «Tải xuống», «Sao chép» | Không |
| Phiên bản hiện tại (tr.13) so với dòng 2 của K3 | «2,4 MB» · «30/09/2026 14:12 · Nguyễn Văn A» | Dòng 2: «2,4 MB», «Nguyễn Văn A», «30/09/2026 14:12» | Không |
| Thùng rác trống (tr.14) | «0 mục» | 0 dòng | Không |
| Thùng rác có mục (tr.15) | «Đã chọn 2 / 3 mục» | 3 dòng; 2 dấu «✓» ở dòng, checkbox tiêu đề «–» | Không |
| Định dạng so với phần mở rộng (K3) | 4 tệp | 4/4 khớp: PDF/.pdf, XLSX/.xlsx, DWG/.dwg, DOCX/.docx (soát trên ảnh tr.10) | Không |
| Số tờ của tệp đang xem (tr.12) | «Rev.2 · Tờ 1/3» | Không có điều khiển chuyển tờ để kiểm 3 tờ | Không kiểm được → F-23 |
| Phân trang (tr.1) | trang «1», «50 dòng / trang» | 3 dòng → 1 trang | Không |

Lệnh đếm:

```
python .claude/skills/ba-analysis/scripts/pdf_text_coverage.py <pdf> <uc-inventory.md> \
  --count "✓" --count "–" --count "Tạo thư mục mới" --count "Tải tệp lên" --count "Tải thư mục lên" \
  --count "Đổi tên" --count "Di chuyển" --count "Xoá" --count "Xem trước" --count "Tải xuống" --count "Sao chép" --count "⋮"
```

---

## 3. Phân loại phạm vi

Quy tắc phân nhóm [GIẢ ĐỊNH – chờ Q-04]:

- **Trong phạm vi:** chức năng có màn hoặc trạng thái được vẽ đủ để biết đường vào, các phần tử và ít nhất một kết quả quan sát được. Phần còn thiếu ghi `[CHỜ Q-nn]` trong test basis.
- **Chưa đủ thông tin:** chỉ có lối vào (mục menu, nút) mà không có màn kết quả, hoặc chưa biết hành vi.
- **Ngoài phạm vi:** phần của hệ thống mà mockup không mô tả.

| Nhóm | Số | Chức năng | Xử lý test |
|---|---|---|---|
| Trong phạm vi | 9 | UC-DOC-001, 002, 006, 007, 009, 015, 016, 018, 020 | Thiết kế test sau Cổng 1; phần thiếu ghi `[CHỜ Q-nn]` [GIẢ ĐỊNH – chờ Q-04] |
| Chưa đủ thông tin | 13 | UC-DOC-003, 004, 005, 008, 010, 011, 012, 013, 014, 017, 019, 021, 022 | Giữ trong danh sách; chỉ thiết kế khi có câu trả lời Q-05 → Q-19 [GIẢ ĐỊNH – chờ Q-04] |
| Ngoài phạm vi | 3 mục, không đặt ID | Thanh biểu tượng bên trái (K1 #1–#5) · «Chi tiết dự án» · «Quản lý báo giá» | Không test ở đợt này [GIẢ ĐỊNH – chờ Q-04] |

Tổng: 9 + 13 = 22 chức năng, khớp với inventory §C. Ma trận vai trò × chức năng chưa lập được vì mockup không có vai trò nào (Q-03).

---

## 4. Read-back — cách AI đang hiểu

**Luồng nghiệp vụ chính**

1. Người dùng mở «Quản lý tài liệu» từ menu bên của một dự án và thấy danh sách thư mục gốc (UC-DOC-001).
2. Gốc có các thư mục thường và một thư mục hệ thống «Thư mục công trình cũ». Thư mục hệ thống không chọn được, không có menu «⋮» (UC-DOC-001, UC-DOC-015).
3. Bấm vào tên thư mục để vào bên trong. Tiêu đề trang đổi thành đường dẫn, ví dụ «Quản lý tài liệu › Quản lý rủi ro» (UC-DOC-002).
4. Danh sách thu hẹp được theo nhiều cách:
   - tìm theo tên, lọc theo bước, lọc theo phạm vi tài liệu;
   - sắp xếp theo từng cột;
   - phân trang mặc định 50 dòng (UC-DOC-003 → UC-DOC-006).
5. Nút «Tạo mới» có ba việc (UC-DOC-007 → UC-DOC-009):
   - tạo thư mục: tên bắt buộc, tối đa 255 ký tự;
   - tải tệp lên;
   - tải thư mục lên: thư mục hoặc ZIP, tối đa 5 GB.
6. Mỗi dòng có menu «⋮» (UC-DOC-010 → UC-DOC-014, UC-DOC-016):
   - thư mục: đổi tên, di chuyển, xoá;
   - tệp: thêm xem trước, tải xuống, sao chép.
7. Chọn nhiều dòng bằng checkbox để tải xuống, di chuyển hoặc xoá cùng lúc (UC-DOC-015, UC-DOC-011, UC-DOC-013, UC-DOC-014).
8. Bấm tên tệp hoặc «Xem trước» thì trình xem mở toàn màn (UC-DOC-016, UC-DOC-017, UC-DOC-014). Trong trình xem có:
   - phóng to, thu nhỏ, vừa khung, xoay;
   - chuyển sang tệp trước hoặc sau;
   - sao chép liên kết, tải xuống.
9. Từ trình xem mở «Quản lý phiên bản» (UC-DOC-018, UC-DOC-019):
   - xem các phiên bản, bản mới nhất mang nhãn «Hiện tại»;
   - tải từng phiên bản;
   - tải lên phiên bản mới cùng định dạng, tên tệp giữ nguyên.
10. Mục bị xoá vào «Thùng rác», kèm vị trí ban đầu, người xoá và thời gian xoá (UC-DOC-020 → UC-DOC-022).
    - Thùng rác có vẻ là của cả dự án [SUY LUẬN].
    - Từ đó chọn một hoặc nhiều mục để khôi phục hoặc xoá vĩnh viễn.

**Vai trò làm được gì:** mockup không phân vai trò; mọi thao tác được vẽ cho một người dùng duy nhất — chờ Q-03.

**Ngoài phạm vi:** thanh biểu tượng bên trái, «Chi tiết dự án», «Quản lý báo giá» [GIẢ ĐỊNH – chờ Q-04].

**Chỗ AI chưa chắc:**
- "bước" là gì và vì sao hai thư mục gốc có cùng thời điểm (Q-05);
- quan hệ giữa bộ lọc phạm vi và thư mục hệ thống (Q-06);
- xoá có đưa mục vào thùng rác ngay hay không (Q-13).

---

## 5. Phát hiện

| ID | Loại | Vị trí | Phát hiện | Câu hỏi |
|---|---|---|---|---|
| F-01 | Phạm vi | Toàn tài liệu | Nguồn duy nhất là mockup bản 5. Không có tài liệu yêu cầu, không có các bản trước để so thay đổi, chưa biết bản này đã được duyệt chưa. Theo `rules/common.md` rule 9, mockup chỉ là căn cứ khi đã được duyệt và đứng sau tài liệu yêu cầu. | Q-01 |
| F-02 | Phạm vi | K1 #1 «F»; K1 #9 «Quản lý dự án › LTS › Quản lý tài liệu»; toàn bộ text tiếng Việt | Mockup không ghi dự án, khách hàng hay ngôn ngữ của hệ thống thật. [SUY LUẬN: logo «F» và cấu trúc «Quản lý dự án» › … › «Quản lý tài liệu» giống bộ TC `FEEC_PM_IT_Test_Case.xlsx` mà sổ FB nhắc tới, trong đó sheet DM-L0001 là module quản lý tài liệu.] Nếu đúng là dự án đó, nhãn trên hệ thống thật có thể không phải tiếng Việt. | Q-02 |
| F-03 | Thiếu luồng | tr.1–15; một góc nhìn người dùng «Fe» (K1 #5) | Không có vai trò hay phân quyền. Chưa biết ai được tạo, tải lên, đổi tên, di chuyển, sao chép, xoá, khôi phục, xoá vĩnh viễn, tải lên phiên bản mới; người không thuộc dự án thấy gì. | Q-03 |
| F-04 | Phạm vi | inventory §C | 22 chức năng suy ra, trong đó 13 chưa đủ thông tin; chưa có tiêu chí phạm vi từ bạn. | Q-04 |
| F-05 | Phạm vi | K1 #1–#8 | Thanh biểu tượng bên trái, «Chi tiết dự án», «Quản lý báo giá» thuộc phần khác của hệ thống; mockup không mô tả. | Q-04 |
| F-06 | Mơ hồ | K1 #13 «Tất cả các bước»; không trang nào mở danh sách này | Chưa biết danh sách các bước, và tệp hay thư mục được gắn với bước bằng cách nào: hộp thoại tạo thư mục (tr.7) và tải lên (tr.8) không có trường bước. | Q-05 |
| F-07 | Phụ thuộc | K2 dòng 1–2: «Quản lý rủi ro», «Xem xét chi phí» cùng «19/08/2026 20:37», cột «Người cập nhật cuối ⇅» là «—»; tr.3 cho «Đổi tên», «Di chuyển», «Xoá» | [SUY LUẬN: cùng một thời điểm tạo + không có người cập nhật + có bộ lọc theo bước] Hai thư mục gốc có thể do hệ thống tạo theo bước của dự án. Nếu vậy, đổi tên hoặc xoá chúng có thể ảnh hưởng tới việc lọc theo bước. | Q-05 |
| F-08 | Mâu thuẫn | tr.6 «Tài liệu dự án ✓» đang chọn; K2 dòng 3 «Thư mục công trình cũ» vẫn hiện | Bộ lọc có lựa chọn riêng «Thư mục công trình cũ», nhưng đang lọc «Tài liệu dự án» thì thư mục đó vẫn nằm trong danh sách. Chưa biết chọn lựa chọn thứ hai thì danh sách hiện gì. | Q-06 |
| F-09 | Thuật ngữ | K2 dòng 3 nhãn «Thư mục hệ thống»; tr.5 ô chú giải «Thư mục đặc biệt: không thể xoá, đổi tên hay di chuyển — nên không có checkbox và nút ⋮» | Hai tên cho một khái niệm. Chưa rõ: mở được không, bên trong có gì, tạo hay tải lên bên trong được không, quy tắc bảo vệ có chặn ở máy chủ không (ẩn nút chưa phải là phân quyền). | Q-06 |
| F-10 | Thiếu luồng | K1 #11 «Tìm theo tên tệp…», #12 «Tìm kiếm» | Không có màn kết quả, không có màn "không có kết quả". Chưa biết phạm vi tìm (thư mục hiện tại, cả dự án, thư mục con, tên thư mục), cách khớp (một phần, hoa thường, dấu), có tìm bằng Enter không, giới hạn ký tự. | Q-07 |
| F-11 | Mơ hồ | K1 #15 «Xoá lọc» nhạt ở cả 15 trang | Chưa biết khi nào nút bật, có xoá cả từ khoá tìm kiếm không; từ khoá và bộ lọc có giữ khi mở thư mục con hay đổi trang không. | Q-07 |
| F-12 | Thiếu luồng | tr.9–13 tiêu đề «Quản lý tài liệu › Quản lý rủi ro»; K1 #9 breadcrumb không đổi; tr.7 «Thư mục mới sẽ được tạo tại: Quản lý tài liệu» | Đường dẫn thư mục hiện ở tiêu đề, còn breadcrumb phía trên giữ nguyên. Chưa biết bấm «Quản lý tài liệu» trong tiêu đề có về gốc không, thư mục nhiều cấp hiển thị thế nào, có giới hạn số cấp không, ở thư mục con thì dòng "sẽ được tạo tại" hiện gì. | Q-08 |
| F-13 | Mơ hồ | K1 #19–#23, các cột có «⇅» | Không có thứ tự sắp xếp mặc định. [SUY LUẬN từ K3: thư mục đứng trước, tệp xếp theo «Cập nhật lần cuối ⇅» giảm dần.] Chưa biết khi sắp xếp theo cột thư mục có còn ở trên không, cột «Dung lượng ⇅» xử lý dòng «—» thế nào. | Q-09 |
| F-14 | Thiếu luồng | K1 #24–#27 | Chưa có danh sách lựa chọn của «50 dòng / trang». «‹ Trước» và «Sau ›» cùng màu xám ở mọi trang, nên không biết trạng thái tắt ở trang đầu và trang cuối. tr.9 danh sách rỗng vẫn hiện trang «1». | Q-09 |
| F-15 | Lỗi dữ liệu | K2 dòng 1–3 so với K3 dòng 1 | Thư mục gốc có «Cập nhật lần cuối ⇅» nhưng «Người cập nhật cuối ⇅» là «—»; thư mục hệ thống trống cả hai cột; thư mục con «Tài liệu tham khảo» có đủ hai cột. Chưa rõ quy tắc điền hai cột này cho thư mục. | Q-09 |
| F-16 | Khó test | K2, K3, tr.13, tr.15: «19/08/2026 20:37», «2,4 MB», «186 KB» | Chưa biết múi giờ hiển thị, đơn vị và cách làm tròn dung lượng (1 MB = 1000 hay 1024 KB), dấu thập phân. | Q-09 |
| F-17 | Thiếu luồng | tr.7 «Tên thư mục *», «Còn 255 ký tự (tối đa 255)», «Lưu» | Có giới hạn 255 ký tự nhưng chưa có: text lỗi khi để trống hoặc chỉ có khoảng trắng; ký tự không cho phép; quy tắc trùng tên trong cùng thư mục cha; quá 255 thì chặn gõ hay báo lỗi; «Lưu» có tắt khi ô rỗng không (mockup vẽ đang bật); lưu xong thấy gì. | Q-10 |
| F-18 | Thiếu luồng | tr.2 «Tải tệp lên» | Có mục menu nhưng không có màn tiếp theo. Chưa biết loại tệp cho phép, dung lượng tối đa mỗi tệp, số tệp mỗi lần, xử lý khi trùng tên, tiến trình, huỷ giữa chừng, lỗi. | Q-11 |
| F-19 | Mơ hồ | tr.8 «Dung lượng tối đa 5 GB»; «Kéo & thả thư mục hoặc tệp ZIP vào đây, hoặc chọn bằng các nút bên dưới.» | Chưa biết 5 GB tính cho cả lần tải hay cho từng tệp; ZIP có được giải nén thành cây thư mục không; trùng tên thư mục đã có thì sao; số cấp tối đa; loại tệp bên trong có bị chặn không; tiến trình và kết quả; bấm «Đóng» khi đang tải thì sao. | Q-12 |
| F-20 | Thiếu luồng | tr.3 «Đổi tên», «Di chuyển», «Xoá»; tr.11 «Sao chép»; tr.4–5 thanh hàng loạt | Không có hộp thoại Đổi tên, Di chuyển (chọn thư mục đích), Sao chép, xác nhận Xoá; không có thông báo kết quả. Chưa rõ ràng buộc: di chuyển vào chính nó hoặc vào thư mục con của nó, trùng tên ở đích, đổi tên tệp có sửa được phần mở rộng không, bản sao nằm ở đâu, xoá có vào «Thùng rác» ngay không. | Q-13 |
| F-21 | Mâu thuẫn | tr.3 (menu thư mục không có «Tải xuống») so với tr.4–5 (chỉ chọn thư mục mà thanh hàng loạt có «Tải xuống»); tr.11 («Sao chép» chỉ có ở menu tệp) | Bộ thao tác không khớp giữa menu từng dòng và thanh hàng loạt. Thư mục tải xuống được khi chọn hàng loạt nhưng không tải được từ menu. Sao chép không có cho thư mục và không có trong thanh hàng loạt. Tải xuống nhiều mục ra định dạng gì cũng chưa rõ. | Q-14 |
| F-22 | Mơ hồ | tr.4 «1» «mục đã chọn» «×»; chú thích tr.5 «chọn tất cả 2 mục»; tr.9 checkbox tiêu đề vẫn hiện khi danh sách rỗng | Chưa rõ: chọn tất cả là trang hiện tại hay mọi trang; lựa chọn có giữ khi đổi trang, lọc, mở thư mục không; «×» có bỏ chọn hết không; chọn lẫn tệp và thư mục thì thanh có những nút nào; bấm checkbox tiêu đề khi danh sách rỗng thì sao. | Q-14 |
| F-23 | Thiếu luồng | K4 #8 «−» «+» «⇔» «⇕» «↺» «↻»; K4 #10 «Rev.2 · Tờ 1/3» | Các nút chỉ có ký hiệu, chưa có nghĩa chính thức. Không có mức phóng hiện tại, giới hạn phóng hay nút đặt lại. Tệp nhiều tờ («Tờ 1/3») chưa biết chuyển tờ bằng cách nào. | Q-15 |
| F-24 | Thiếu luồng | K3 có PDF, XLSX, DWG, DOCX; tr.12 chỉ vẽ ví dụ PDF; K4 #6–#7, #9 | Chưa biết định dạng nào xem trước được, định dạng không xem được thì hiện gì. «‹» / «›» và phím mũi tên chuyển qua những mục nào: có bỏ qua thư mục, có quay vòng ở đầu và cuối, có theo thứ tự đang sắp xếp và lọc không. Chưa có trường hợp tệp hỏng hoặc rất lớn. | Q-15 |
| F-25 | Thiếu luồng | K4 #2 «Sao chép liên kết» | Chưa biết liên kết trỏ tới đâu, ai mở được, có thông báo đã sao chép không, liên kết có còn dùng được khi tệp bị đổi tên, di chuyển, xoá hoặc lên phiên bản mới không. | Q-16 |
| F-26 | Thiếu luồng | tr.13 «Tải lên phiên bản mới»; «Tên tệp sẽ không thay đổi. Vui lòng chọn tệp cùng định dạng.» | Chưa có text lỗi khi chọn tệp khác định dạng. Chưa biết "cùng định dạng" xét theo phần mở rộng hay theo nội dung tệp, giới hạn dung lượng là bao nhiêu. [SUY LUẬN từ tr.13 so với K3 dòng 2: dòng trong danh sách lấy thông tin theo phiên bản hiện tại.] | Q-17 |
| F-27 | Thiếu luồng | tr.13 «Phiên bản 1» chỉ có «Tải xuống»; bảng không có nút đóng riêng; dữ liệu mẫu tr.13 và tr.15 | Không có khôi phục phiên bản cũ, xoá phiên bản, giới hạn số phiên bản; chưa biết đóng bảng bằng cách nào. Tên tệp có số bản sửa ("rev2") sẽ lệch với số phiên bản (xem soát ngược #1). | Q-17 |
| F-28 | Thiếu luồng | tr.14–15 | Chưa có: hộp thoại xác nhận «Xoá vĩnh viễn»; thông báo sau khi khôi phục; cách khôi phục khi vị trí ban đầu đã bị xoá hoặc di chuyển, hoặc khi ở đó đã có mục trùng tên; thời hạn giữ trong thùng rác; xoá thư mục thì hiện một dòng hay từng tệp; tìm kiếm, sắp xếp, phân trang. Phạm vi thùng rác [SUY LUẬN: cả dự án, vì tr.15 có mục từ «Quản lý rủi ro» và «Xem xét chi phí»]. | Q-18 |
| F-29 | Khó test | tr.15 dòng 3 «Ảnh khảo sát hiện trường» | Tên không có phần mở rộng, bảng không có cột loại hay biểu tượng, nên không phân biệt được tệp hay thư mục. | Q-18 |
| F-30 | Thiếu luồng | tr.1–15 | Không màn nào có thông báo kết quả sau thao tác ghi, trạng thái đang tải, lỗi mạng hoặc lỗi máy chủ, hết phiên, hay tình huống hai người cùng thao tác trên một mục. | Q-19 |
| F-31 | Thuật ngữ | tr.2 «Tạo thư mục mới» so với tr.7 «Tạo thư mục» | Hai nhãn cho cùng một chức năng. | Q-20 |
| F-32 | Thuật ngữ | K1 #19 «Tên tệp ⇅», cột chứa cả thư mục; tr.9 «Chưa có tệp nào» | Chữ "tệp" được dùng cho cả thư mục. Chưa rõ trạng thái rỗng ở tr.9 hiện khi không có tệp nào hay khi không có mục nào. | Q-20 |
| F-33 | Mơ hồ | tr.5 ô chú giải; tr.10, 11, 15 «Dữ liệu mẫu» | Không rõ ô chú giải ở tr.5 và huy hiệu «Dữ liệu mẫu» là giao diện thật hay chú thích của người thiết kế. | Q-20 |
| F-34 | Lỗi dữ liệu | tr.15 «Đã chọn 2 / 3 mục» | Dòng chữ bị mép dưới hộp thoại cắt mất một phần, có thể là lỗi của bản vẽ. | Q-20 |
| F-35 | Mơ hồ | TC_080 (H92, J92); trả lời 02/10 ý 2 | Cách đếm cấp chưa rõ. Các bước của TC_080 coi thư mục nằm ngay ở gốc là cấp 1 (Folder 1 → Folder 10 là 10 cấp), nhưng tiêu đề lại ghi 「10 folder cấp con trong 1 folder cha」. Chưa biết «Tài liệu dự án» và «Thư mục công trình cũ» có tính là một cấp không, và lỗi ở cấp 21 hiện lúc mở hộp thoại hay lúc bấm «Lưu». | Q-08 |
| F-36 | Mâu thuẫn | TC_082 (K94) | Kết quả ghi 「Hệ thống tự cắt ký tự và báo lỗi」. Nếu hệ thống đã tự cắt về 255 ký tự thì không còn tên quá dài để báo lỗi, nên phải chọn một trong hai hành vi. | Q-10 |
| F-37 | Mơ hồ | Trả lời 02/10 ý 1 | "Không quá 255 ký tự, kể cả Full-width hay Half-width" chưa nói cách đếm chữ có dấu ở dạng tổ hợp (một chữ thành hai mã) và emoji. Trường hợp này có thật: chính bộ TC có 378 ô chữ ở dạng tổ hợp. | Q-10 |
| F-38 | Mâu thuẫn | TC_143 (K155), TC_144 (K156), TC_146 (K158) | Trùng tên cho ra ba hành vi khác nhau: tạo thì 「- Hiển thị thêm Số thứ tự」; đổi tên thì 「- Không cho phép tạo folder trùng tên và báo lỗi」; di chuyển thì thêm số thứ tự. Theo pattern P6, đây là dấu hiệu thiết kế không nhất quán. Định dạng số thứ tự cũng chưa có. | Q-10 |
| F-39 | Thiếu luồng | Trả lời 02/10 ý 3 | Đã biết không được chuyển thư mục qua lại giữa «Tài liệu dự án» và «Thư mục công trình cũ». Chưa biết chặn bằng cách nào (ẩn hoặc tắt thư mục đích, hay báo lỗi), text là gì, quy tắc có áp cho tệp không, và di chuyển hàng loạt có lẫn hai phạm vi thì sao. | Q-13 |
| F-40 | Phụ thuộc | Trả lời 02/10 ý 3; đề xuất mặc định cũ của Q-06 | Trả lời cho thấy thư mục bên trong «Thư mục công trình cũ» vẫn đổi tên và di chuyển được, trái với đề xuất mặc định cũ của Q-06 (chỉ xem). Chưa rõ có tạo thư mục, tải lên hay xoá bên trong được không. | Q-06 |
| F-41 | Phụ thuộc | 15 TC tải thư mục / ZIP lên còn ghi 10 cấp: TC_085, 088, 090, 093, 096, 098, 101, 107, 109, 113, 116, 118, 121, 124, 126 | Chưa biết giới hạn 20 cấp có áp cho việc tải thư mục và tệp ZIP lên không. | Q-12 |
| F-42 | Mâu thuẫn | TC_150 (K162) 「YYYY-MM-DD HH:MM」 so với K3 dòng 1 «30/09/2026 15:02» | Định dạng ngày giờ của bộ TC khác với mockup. | Q-09 |

Thống kê (đếm bằng script kiểm nhất quán, không đếm tay): 42 phát hiện — v0.1 có 34, v0.2 thêm F-35 → F-42 — gồm Thiếu luồng 15 · Mơ hồ 8 · Mâu thuẫn 5 · Phạm vi 4 · Phụ thuộc 3 · Thuật ngữ 3 · Lỗi dữ liệu 2 · Khó test 2. Số câu hỏi: 20, gồm 4 CHẶN, 15 QUAN TRỌNG, 1 NHỎ. Mọi F có câu hỏi; mọi liên kết F ↔ Q khớp hai chiều.

---

## 6. Bước tiếp theo

1. **Dừng ở Cổng 1.** Bạn cần trả lời 4 câu CHẶN:
   - Q-01: nguồn và trạng thái duyệt;
   - Q-02: dự án và ngôn ngữ;
   - Q-03: phân quyền;
   - Q-04: phạm vi.

   Câu QUAN TRỌNG và NHỎ: trả lời được thì tốt. Câu nào chưa trả lời, khi chốt baseline mình dùng đề xuất mặc định, gắn nhãn [GIẢ ĐỊNH] và báo lại cho bạn.
2. **Sau Cổng 1:** làm bước 4–5 của ba-analysis, tức chốt baseline v1.0 và xuất test basis theo khung Redirect / Validation / Function. Skill `design-check` (bước 2 của pipeline) chỉ chạy khi có tài liệu yêu cầu để đối chiếu với mockup.
3. **Để đóng câu hỏi nhanh hơn**, bạn gửi giúp:
   - bản HTML gốc của mockup, nếu có;
   - các màn còn thiếu: Tải tệp lên, Đổi tên, Di chuyển, Sao chép, xác nhận Xoá, Sao chép liên kết, Tải lên phiên bản mới, kết quả tìm kiếm.
4. **[ĐỀ XUẤT] Dùng bộ TC cũ làm nguồn tham khảo.** `references/patterns.md` của tc-authoring được rút từ một bộ TC thật của module quản lý tài liệu (150 TC).
   - Nếu module này kế thừa module đó, bộ TC cũ có thể trả lời một phần Q-10 → Q-12 và Q-15 (giới hạn, text lỗi).
   - Theo `rules/common.md` rule 9, bộ TC cũ không đứng trên mockup đã duyệt, nên mình chỉ dùng khi bạn đồng ý.
   - **Cập nhật 02/10:** bạn đã đồng ý dùng bộ TC FEEC cho phần Tạo mới folder (FB-021); kết quả ở §7.
5. **[ĐỀ XUẤT] Script mới.** Nếu bạn duyệt, mình đề nghị:
   - thêm `pdf_text_coverage.py` vào `.claude/skills/ba-analysis/scripts/`;
   - thêm một dòng vào bước 1 của SKILL.md: tài liệu là PDF in từ web (mockup) thì chạy script này để đối soát hai chiều.

   Đây là đề xuất của AI, chưa có FB làm nguồn, nên chưa sửa SKILL.md.

---

## 7. Tạo mới folder (UC-DOC-007) — cập nhật v0.2

Phần này cập nhật chức năng Tạo thư mục, đi từ bộ TC FEEC như bạn yêu cầu ngày 02/10 (FB-021). Ký hiệu dùng trong phần này:

- «…»: text của mockup.
- 「…」: text của bộ TC.
- [DỊCH TẠM]: bản tiếng Việt AI dịch đại khái theo FB-022, chưa phải text chính thức.

### 7.1 Nguồn và thứ tự ưu tiên

| # | Nguồn | Dùng cho | Khi lệch nhau |
|---|---|---|---|
| 1 | Trả lời của bạn trong chat ngày 02/10, đã ghi vào `questions.md` (Q-06, Q-08, Q-10, Q-13) | 255 ký tự cho cả Full-width và Half-width; tối đa 20 cấp; chỉ đổi tên và di chuyển trong cùng phạm vi | Ưu tiên cao nhất, vì đây là yêu cầu |
| 2 | Mockup bản 5, tr.2 và tr.7 | Lối vào, hộp thoại, nhãn, bộ đếm | Đứng sau yêu cầu (`rules/common.md` rule 9); mockup vẫn chờ duyệt (Q-01) |
| 3 | Bộ TC FEEC, sheet Document, 8 TC: TC_021, TC_022, TC_079 → TC_083, TC_143. Nguyên văn ở `tc-inventory-tao-thu-muc.md` | Quy tắc chi tiết, text lỗi tiếng Nhật | Đặc tả ngược, đã lỗi thời (FB-021). Lệch với nguồn 1 thì theo nguồn 1; lệch với nguồn 2 thì thành câu hỏi |

### 7.2 Bộ bảng đề xuất cho Tạo mới folder

Mỗi bảng phục vụ một nhóm TC của Tester, theo mẫu test basis (`skills/ba-analysis/references/test-basis-template.md`):

| Bảng | Trả lời câu hỏi | Nhóm TC dùng bảng | Mục |
|---|---|---|---|
| Đường vào / ra (NV) | Mở hộp thoại từ đâu, đóng thì về đâu | Redirect | 7.3 |
| Trường dữ liệu (FD) | Ô tên nhận gì, từ chối gì | Validation | 7.4 |
| Thông báo (MS) | Text của từng thông báo: tiếng Nhật gốc và tiếng Việt dịch tạm | Validation | 7.5 |
| Business rule (BR) | 255 ký tự, 20 cấp, trùng tên, phạm vi | Function | 7.6 |
| Luồng · tác động phụ · phân quyền | Đi đúng, rẽ nhánh, gặp lỗi; thư mục mới hiện ở đâu; ai được tạo | Function, Redirect | 7.7 |
| Rà soát bộ TC cũ | TC nào giữ, sửa, tách; lỗi logic, thứ tự, dữ liệu | Đầu vào cho Tester | 7.8 |
| Thứ tự đề xuất | Khung sắp xếp TC cho khu vực Tạo thư mục | Đầu vào cho Tester | 7.9 |

### 7.3 Đường vào / ra → Redirect

| ID | Từ đâu | Cách vào / ra | Kết quả | Nguồn |
|---|---|---|---|---|
| UC-DOC-007-NV-01 | Danh sách thư mục gốc, hoặc bên trong một thư mục | Bấm «Tạo mới» | Menu mở với 3 lựa chọn: «Tạo thư mục mới», «Tải tệp lên», «Tải thư mục lên» | tr.2. TC_021 chỉ ghi 2 lựa chọn — lỗi thời |
| UC-DOC-007-NV-02 | Menu «Tạo mới» | Bấm «Tạo thư mục mới» | Hộp thoại «Tạo thư mục» mở, gồm: <br>- dòng «Thư mục mới sẽ được tạo tại: Quản lý tài liệu», hiện tên thư mục đang đứng (chờ Q-08); <br>- nhãn «Tên thư mục *»; <br>- ô rỗng có placeholder «Nhập tên thư mục», đang focus; <br>- bộ đếm «Còn 255 ký tự (tối đa 255)»; <br>- các nút «Huỷ», «Lưu», «×» | tr.7. TC_022 chỉ ghi 「- Hiển thị màn hình: PM0035」 |
| UC-DOC-007-NV-03 | Thư mục trống (tr.9) | Làm theo hướng dẫn «Bấm + Tạo mới để tải tệp hoặc tạo thư mục con.» | Như NV-01 | tr.9 |
| UC-DOC-007-NV-04 | Bên trong «Thư mục công trình cũ» | «Tạo mới» → «Tạo thư mục mới» | Như NV-02 [SUY LUẬN từ trả lời 02/10 ý 3 — chờ Q-06] | Trả lời 02/10 |
| UC-DOC-007-NV-05 | Hộp thoại | Bấm «Lưu» khi tên thoả mọi quy tắc của FD-01 (BR-01 → BR-07) | Hộp thoại đóng; thư mục mới hiện trong danh sách của thư mục đang đứng (SE-01) | TC_079 「- Cho phép tạo thành công và hiển thị folder tên [Folder 1]」 |
| UC-DOC-007-NV-06 | Hộp thoại | Bấm «Huỷ» | [CHỜ Q-10] | Chưa có trong TC lẫn mockup |
| UC-DOC-007-NV-07 | Hộp thoại | Bấm «×», nhấn Esc, hoặc bấm ra ngoài hộp thoại | [CHỜ Q-10] | Chưa có trong TC lẫn mockup |
| UC-DOC-007-NV-08 | Danh sách | Người dùng ở vai trò không được tạo thư mục | [CHỜ Q-03] | — |

### 7.4 Trường dữ liệu → Validation

Chức năng chỉ có một trường nhập là UC-DOC-007-FD-01 «Tên thư mục *», nên bảng ghi theo từng thuộc tính:

| Thuộc tính | Giá trị | Nguồn |
|---|---|---|
| Kiểu | Text một dòng | tr.7 |
| Bắt buộc | Có, đánh dấu «*» màu đỏ. Text lỗi khi bỏ trống [CHỜ Q-10] | tr.7 |
| Độ dài | 1–255 ký tự. Ký tự Full-width và Half-width đều tính 1 ký tự. Cách đếm chữ tổ hợp và emoji [CHỜ Q-10] | Trả lời 02/10 ý 1 |
| Ký tự cho phép | Có thể dùng ký tự Full-width (dữ liệu thử 「ＮＲＴ０７８」). Ký tự bị cấm [CHỜ Q-10] | TC_083 |
| Mặc định | Ô rỗng, placeholder «Nhập tên thư mục», bộ đếm «Còn 255 ký tự (tối đa 255)» | tr.7 |
| Duy nhất | Trùng tên trong cùng thư mục cha vẫn tạo được; tên mới thêm số thứ tự. Định dạng số thứ tự [CHỜ Q-10] | TC_143 |
| Phụ thuộc | Thư mục cha phải ở cấp ≤ 19 (BR-02) | — |
| Thông báo | MS-01, MS-02, MS-03 | §7.5 |

### 7.5 Thông báo và text giao diện

Theo FB-022: cột "Text gốc" giữ nguyên văn tiếng Nhật; cột "Tiếng Việt" chỉ là bản dịch tạm.

| ID | Khi nào | Text gốc (nguyên văn) | Tiếng Việt [DỊCH TẠM] | Vị trí | Nguồn |
|---|---|---|---|---|---|
| UC-DOC-007-MS-01 | Tên dài hơn 255 ký tự | 「フォルダ名が長すぎます（最大255文字）」 | Tên thư mục quá dài (tối đa 255 ký tự). | [CHỜ Q-10] | TC_082 · K94, W94 |
| UC-DOC-007-MS-02 | Tạo thư mục con khi thư mục cha đã ở cấp 20 | 「フォルダの階層が上限（10階層）に達しているため、サブフォルダを作成できません。」 (số 10 đã lỗi thời) | Không thể tạo thư mục con vì số cấp thư mục đã đạt giới hạn (20 cấp). | [CHỜ Q-08] | TC_081 · K93, W93; số cấp theo trả lời 02/10 ý 2 |
| UC-DOC-007-MS-03 | Bỏ trống tên rồi bấm «Lưu» | Phần Tạo thư mục chưa có. Phần Đổi tên dùng 「ファイル名を入力してください」 (TC_055) | Vui lòng nhập tên tệp. (Chưa biết Tạo thư mục có dùng chung câu này không) | [CHỜ Q-10] | TC_055 · K67, W67 |
| UC-DOC-007-MS-04 | Placeholder của ô tên | «Nhập tên thư mục» (mockup, đã là tiếng Việt). Phần Đổi tên dùng 「ファイル名を入力」 (TC_054) | — | Trong ô | tr.7 · TC_054 · K66, W66 |
| UC-DOC-007-MS-05 | Bộ đếm ký tự | «Còn 255 ký tự (tối đa 255)» (mockup) | — | Dưới ô, căn phải | tr.7 |
| UC-DOC-007-MS-06 | Di chuyển thư mục sang phạm vi khác | Chưa có | [CHỜ Q-13] | — | Trả lời 02/10 ý 3 |

### 7.6 Business rule → Function

| ID | Rule | Điều kiện | Khi thoả | Khi vi phạm | Nguồn |
|---|---|---|---|---|---|
| UC-DOC-007-BR-01 | Tên thư mục dài tối đa 255 ký tự. Ký tự Full-width và Half-width đều tính 1 ký tự | Tên có độ dài ≤ 255 | Lưu được | Hiện MS-01. Hệ thống chặn không cho gõ thêm, hay cắt rồi báo lỗi: [CHỜ Q-10] | Trả lời 02/10 ý 1 · TC_082 · tr.7 |
| UC-DOC-007-BR-02 | Thư mục lồng nhau không quá 20 cấp | Thư mục cha đang ở cấp ≤ 19. Thư mục nằm ngay ở gốc tính là cấp 1 [SUY LUẬN từ TC_080, TC_081 — chờ Q-08] | Tạo được thư mục con; sâu nhất tới cấp 20 | Thư mục cha đã ở cấp 20: không tạo được, hiện MS-02 | Trả lời 02/10 ý 2 · TC_080, TC_081 (còn ghi 10 cấp, đã lỗi thời) |
| UC-DOC-007-BR-03 | Thư mục chỉ được đổi tên và di chuyển trong cùng một phạm vi, «Tài liệu dự án» hoặc «Thư mục công trình cũ». Không chuyển qua lại giữa hai phạm vi | Thư mục đích cùng phạm vi với thư mục đang chuyển | Di chuyển được | Thư mục đích ở phạm vi kia: bị chặn. Cách chặn và text [CHỜ Q-13] | Trả lời 02/10 ý 3. Áp cho cả UC-DOC-010 (Đổi tên) và UC-DOC-011 (Di chuyển) |
| UC-DOC-007-BR-04 | Tạo thư mục trùng tên trong cùng thư mục cha vẫn được; tên mới thêm số thứ tự | Thư mục cha đã có thư mục cùng tên | Thư mục mới được tạo, tên có thêm số thứ tự. Định dạng [CHỜ Q-10] | — | TC_143. Lệch với TC_144: đổi tên trùng thì báo lỗi (F-38) |
| UC-DOC-007-BR-05 | Tên là bắt buộc | Ô rỗng, hoặc chỉ có khoảng trắng | — | [CHỜ Q-10] | tr.7, dấu «*» |
| UC-DOC-007-BR-06 | Tên được chứa ký tự Full-width | Tên có ký tự Full-width | Tạo được; tên hiển thị đúng như đã nhập | — | TC_083 |
| UC-DOC-007-BR-07 | Tạo được thư mục ở cả hai phạm vi | Đang đứng bên trong «Thư mục công trình cũ» | Tạo được thư mục | — | [SUY LUẬN từ trả lời 02/10 ý 3 — chờ Q-06] |

### 7.7 Luồng, tác động phụ, phân quyền → Function

**Luồng**

- UC-DOC-007-MF-01: Ở danh sách (gốc hoặc trong một thư mục), bấm «Tạo mới» → menu có 3 lựa chọn (NV-01).
- UC-DOC-007-MF-02: Bấm «Tạo thư mục mới» → hộp thoại «Tạo thư mục» mở (NV-02).
- UC-DOC-007-MF-03: Nhập tên thoả FD-01 (BR-01 → BR-07); bộ đếm giảm theo số ký tự đã nhập [CHỜ Q-10].
- UC-DOC-007-MF-04: Bấm «Lưu» → hộp thoại đóng, thư mục mới hiện trong danh sách (SE-01).
- UC-DOC-007-AF-01 (rẽ từ MF-04): tên trùng với thư mục đã có → vẫn tạo, tên thêm số thứ tự (BR-04).
- UC-DOC-007-AF-02 (rẽ từ MF-02 hoặc MF-03): bấm «Huỷ» hoặc «×» → [CHỜ Q-10].
- UC-DOC-007-EF-01 (tại MF-03 hoặc MF-04): tên dài hơn 255 ký tự → hiện MS-01 (BR-01).
- UC-DOC-007-EF-02 (tại MF-02 hoặc MF-04): thư mục cha đã ở cấp 20 → không tạo được, hiện MS-02 (BR-02). Lỗi hiện ở bước nào [CHỜ Q-08].
- UC-DOC-007-EF-03 (tại MF-04): tên rỗng hoặc chỉ có khoảng trắng → [CHỜ Q-10] (BR-05).
- UC-DOC-007-EF-04 (tại MF-04): mất mạng, lỗi máy chủ, hoặc bấm «Lưu» hai lần → [CHỜ Q-19].

**Tác động phụ**

| ID | Sau hành động | Thấy ở đâu | Nội dung | Nguồn |
|---|---|---|---|---|
| UC-DOC-007-SE-01 | Tạo thành công | Danh sách của thư mục đang đứng | Có một dòng mới gồm: biểu tượng thư mục; tên đã nhập; «Định dạng» và «Dung lượng» là «—»; «Người cập nhật cuối» là người tạo; «Cập nhật lần cuối» là thời điểm tạo [SUY LUẬN từ K3 dòng 1 — chờ Q-09] | TC_079; tr.10 |
| UC-DOC-007-SE-02 | Tạo thành công | Vị trí của dòng mới trong danh sách | [CHỜ Q-09] | — |
| UC-DOC-007-SE-03 | Tạo thành công | Định dạng ngày giờ ở cột «Cập nhật lần cuối» | Mockup ghi «30/09/2026 15:02», còn TC_150 ghi 「YYYY-MM-DD HH:MM」. Hai nguồn lệch nhau (F-42) [CHỜ Q-09] | tr.10; TC_150 |
| UC-DOC-007-SE-04 | Tạo thành công | Người dùng ở vai trò khác, sau khi tải lại trang | [CHỜ Q-03]. Theo pattern P5: làm ở vai trò A, tải lại trang, rồi kiểm ở vai trò B | — |

**Phân quyền:** chưa có ma trận [CHỜ Q-03]. Bộ TC có nhắc tới vai trò: TC_139 và TC_141 ghi 「1. Tạo file trên role ES/PM」 [SUY LUẬN: dự án có hai vai trò ES và PM]. Mình đã ghi chi tiết này vào Q-03 để làm gợi ý.

### 7.8 Rà soát bộ TC cũ — logic, thứ tự, dữ liệu

**Từng TC**

| TC | Ô | Hiện tại | Vấn đề | Đề xuất |
|---|---|---|---|---|
| TC_021 | R33 | Kết quả liệt kê 2 lựa chọn | Lỗi thời: mockup tr.2 có 3 lựa chọn, TC thiếu «Tải thư mục lên». TC_024 trong cùng file lại kiểm lựa chọn 「Tải thư mục lên」, nên hai TC mâu thuẫn nhau. Tên nút ghi là 「[+ + Tạo mới]」 (H33) và 「[++ Tạo mới]」 (J33), khác nhãn «Tạo mới» | Sửa kết quả mong đợi cho đủ 3 lựa chọn (NV-01); ghi đúng nhãn «Tạo mới» |
| TC_022 | R34 | 「- Hiển thị màn hình: PM0035」 | Kết quả không quan sát được (`rules/tc-authoring.md` rule 12), vì chỉ có mã màn hình. Theo mockup, đây là hộp thoại chứ không phải màn hình | Sửa: liệt kê các phần tử của hộp thoại theo NV-02 |
| TC_079 | R91 | Tên thử là 「[Folder 1]」 | Tiêu đề là 「Kiểm tra tạo 1 folder có tên dưới 255 ký tự」 nhưng dữ liệu chỉ 8 ký tự, không phải ca biên. Bước 「2. Tạo Folder mới tên [Folder 1]」 gộp ba thao tác: chọn «Tạo thư mục mới», nhập tên, bấm «Lưu». Pre-condition để trống, chưa nói người test đang đứng ở đâu | Tách thành 3 ca: tên 1 ký tự; tên 255 ký tự Half-width; tên 255 ký tự Full-width (BR-01) |
| TC_080 | R92 | Tạo tới cấp 10 | Lỗi thời: nay là 20 cấp. Có hai bước cùng đánh số 「3.」. Tiêu đề 「10 folder cấp con trong 1 folder cha」 không khớp với các bước, vì Folder 1 → Folder 10 là 10 cấp đã tính cả thư mục cha (F-35) | Sửa: tạo tới cấp 20; ghi rõ cách đếm cấp sau khi có trả lời Q-08 |
| TC_081 | R93 | Tạo tới cấp 11; text lỗi ghi 10階層 | Lỗi thời: nay phải thử cấp 21. Chữ "thông báo" ở K93 có thêm một dấu sắc thừa. Text tiếng Nhật đang để ở cột Open question (W93) | Sửa: thử cấp 21; kết quả mong đợi dùng bản tiếng Việt [DỊCH TẠM] của MS-02; cột Open question ghi "MS-02 dịch tạm, chờ text chính thức" |
| TC_082 | R94 | 「Hệ thống tự cắt ký tự và báo lỗi」 | Kết quả tự mâu thuẫn (F-36). Dữ liệu 「Nhập quá 255 ký tự」 không cụ thể. Thiếu bước chọn «Tạo thư mục mới». Chỉ có ca Half-width | Tách thành: 256 ký tự Half-width; 256 ký tự Full-width; dán một chuỗi dài hơn 255 ký tự. Viết lại kết quả sau khi có trả lời Q-10 |
| TC_083 | R95 | 「- Cho phép tạo bình thường」 | Kết quả mơ hồ, trái rule 12. `tc_check.py` không bắt được lỗi này vì ô ở dạng chữ tổ hợp (FB-023). Tiêu đề có thêm một dấu nặng thừa ở chữ "tạo". Chỉ thử chữ và số Full-width | Sửa kết quả: thư mục 「ＮＲＴ０７８」 hiện trong danh sách, tên giữ nguyên ký tự Full-width, không bị đổi sang Half-width |
| TC_143 | R155 | 「- Hiển thị thêm Số thứ tự」 | Chưa có định dạng số thứ tự, nên chưa viết được assertion. TC nằm ở nhóm III 「Thông tin dữ liệu」, tên nhóm không khớp nội dung: đây thực ra là nhóm trùng tên theo pattern P6 (TC_143 → TC_146). Hành vi lệch với TC_144 (F-38). Tiêu đề có thêm một dấu nặng thừa ở chữ "tạo" | Giữ trong nhóm P6, nhưng đổi tên nhóm III thành "Trùng tên - Duplicate name"; ghi định dạng số thứ tự sau khi có trả lời Q-10 |

**Thứ tự**

- Các TC của Tạo thư mục nằm rải ở ba nơi:
  - II 「+ Tạo mới」 (R33–R34);
  - III 「Tạo Folder manual」 (R91–R95);
  - III 「Thông tin dữ liệu」 (R155).
- Trong R91–R95, ca thành công và ca thất bại nằm xen kẽ: thành công (TC_079, TC_080) → thất bại (TC_081, TC_082) → lại thành công (TC_083). Như vậy là trái `rules/tc-authoring.md` rule 8 (cùng nhóm kết quả phải nằm liền nhau), và không gộp ô được.
- TC_148 → TC_150 kiểm thông tin của bản ghi sau khi tạo, nhưng bị dải gộp E159:E162 kéo vào nhóm IV 「Upload file/folder/ZIP quá 255 ký tự」. Ba TC này cũng mới kiểm cho tệp, chưa có ca cho thư mục.
- Khung sắp xếp lại ở §7.9.

**Dữ liệu** (đếm bằng script)

| Kiểm | 8 TC của phần này | Cả sheet Document | Hệ quả |
|---|---|---|---|
| Kết quả Round 2 nằm lệch một cột: kết quả ở cột Q (cột Remark của Round 1), người test ở R, ngày ở S và T | 8 / 8 | 141 / 150 dòng. `tc_check.py` báo 142 dòng "Round 2 Result không hợp lệ"; dòng thêm là TC_144, có người test nhưng không có kết quả | Bảng tổng kết Round 2 hiện 150 TC "Not execute" dù đã chạy |
| Công thức tổng kết đếm từ hàng 25, còn Total đếm từ hàng 13 | — | 12 TC đầu (TC_001 → TC_012) | Round 1 luôn có 12 TC "Not execute" giả |
| Pre-condition để trống | 8 / 8 | 150 / 150 | TC_080 và TC_081 cần có sẵn chuỗi thư mục 19 hoặc 20 cấp (`rules/tester.md` rule 7) |
| Cột UC để trống | 8 / 8 | 150 / 150 | `rules/tc-authoring.md` rule 10 |
| Chữ ở dạng tổ hợp, không phải NFC | 20 / 96 ô chữ | 378 / 1.737 ô chữ | Tìm kiếm, lọc và so chuỗi bằng máy có thể trượt; `tc_check.py` bỏ sót 16 kết quả mơ hồ (FB-023) |
| Dấu thừa | 3 ô (K93, H95, H155) | 12 ô | Chữ hiển thị sai dấu |
| Text tiếng Nhật | 4 ô (K93, W93, K94, W94) | 129 ô trên 48 TC | Phần này đã dịch tạm (§7.5); các phần khác chưa dịch |

**Ngoài phạm vi, thấy khi rà** (ghi lại để không mất, chưa xử lý):

- TC_058 (R70): tiêu đề 「Kiểm tra hiển thị khi click vào button [Lưu]」 thuộc phần Đổi tên, nhưng bước lại bấm 「[削除する]」 và kết quả là xoá tệp. Có vẻ chép nhầm từ phần Xoá.
- TC_139 (R151) và TC_141 (R153): tiêu đề nói về thư mục, nhưng các bước lại thao tác trên tệp (「1. Tạo file trên role ES/PM」).
- Sheet Test_Report chỉ lưu giá trị lỗi (#NAME?, #VALUE!), vì trỏ tới sheet 「Home」 không có trong file.

### 7.9 Thứ tự đề xuất cho khu vực Tạo thư mục [ĐỀ XUẤT]

Thứ tự dựa trên:

- `rules/tc-authoring.md` rule 4 và rule 8;
- bước 5 của skill tc-authoring: hiển thị → nhập liệu → kiểm tra dữ liệu → thành công → không thành công → phân quyền → bảo mật;
- pattern P1 (popup có nhập liệu).

Cột "TC hiện có" cho biết TC cũ nào chuyển vào vị trí đó.

| # | II | III | IV | TC hiện có | Căn cứ |
|---|---|---|---|---|---|
| 1 | Tạo thư mục - Create folder | Hiển thị | Menu «Tạo mới» có 3 lựa chọn | TC_021 (sửa) | NV-01 |
| 2 | | Hiển thị | Mở hộp thoại «Tạo thư mục» | TC_022 (sửa) | NV-02 |
| 3 | | Nhập liệu | Bộ đếm giảm khi gõ | mới | MS-05 |
| 4 | | Nhập liệu | Xoá hết nội dung thì placeholder hiện lại | mới | P1 · mục 2 |
| 5 | | Thành công | Tên 1 ký tự | mới, tách từ TC_079 | BR-01 |
| 6 | | Thành công | Tên 255 ký tự Half-width | mới, tách từ TC_079 | BR-01 |
| 7 | | Thành công | Tên 255 ký tự Full-width | mới | BR-01 |
| 8 | | Thành công | Tên có ký tự Full-width | TC_083 (sửa) | BR-06 |
| 9 | | Thành công | Tạo ở cấp 20 | TC_080 (sửa) | BR-02 |
| 10 | | Thành công | Tạo bên trong «Thư mục công trình cũ» | mới | BR-07, chờ Q-06 |
| 11 | | Không thành công | Bỏ trống rồi bấm «Lưu» | mới | BR-05, chờ Q-10 |
| 12 | | Không thành công | Chỉ nhập khoảng trắng | mới | BR-05, chờ Q-10 |
| 13 | | Không thành công | Tên 256 ký tự Half-width | TC_082 (sửa) | BR-01, MS-01 |
| 14 | | Không thành công | Tên 256 ký tự Full-width | mới | BR-01, MS-01 |
| 15 | | Không thành công | Tên có ký tự không cho phép | mới | chờ Q-10 |
| 16 | | Không thành công | Tạo ở cấp 21 | TC_081 (sửa) | BR-02, MS-02 |
| 17 | | Huỷ | Bấm «Huỷ» | mới | P1 · mục 5, chờ Q-10 |
| 18 | | Huỷ | Bấm «×» hoặc nhấn Esc | mới | chờ Q-10 |
| 19 | | Phân quyền | Vai trò không được tạo: nút bị ẩn và API chặn | mới | `rules/tester.md` rule 5, chờ Q-03 |
| 20 | | Bảo mật | Tên chứa `<script>alert(1)</script>` hoặc một chuỗi SQL được lưu và hiển thị như chữ thường | mới | `rules/tc-authoring.md` rule 15 |

Ghi chú:

- **Ca trùng tên (TC_143):** giữ trong nhóm trùng tên cùng TC_144 → TC_146, để so bốn lối vào cạnh nhau theo pattern P6. Chỉ cần đổi tên nhóm III (§7.8).
- **Đổi tên và di chuyển trong cùng phạm vi (BR-03):** thuộc khu vực Đổi tên và Di chuyển, không đặt ở đây.
- **Rủi ro mất ID khi xếp lại.** Nếu xếp lại bằng `tc_build_xlsx.py`, script sẽ đánh lại toàn bộ TVP_ID theo thứ tự dòng (nó tự sinh `TC_%03d`).
  - Như vậy là trái `rules/tc-authoring.md` rule 11, và Bug_ID cũ sẽ mất liên kết. Ví dụ: TC_081 đang gắn bug 1.
  - Đề xuất: TC cũ giữ ID cũ, TC mới lấy số tiếp theo từ TC_151; hoặc sửa script để đọc ID từ dữ liệu (FB-024, chờ duyệt).

### 7.10 Câu hỏi được cập nhật ở v0.2

- **Q-06, Q-08, Q-10, Q-13:** đã ghi trả lời một phần của bạn ngày 02/10, kèm những phần còn mở.
- **Q-12:** thêm câu hỏi giới hạn 20 cấp có áp cho việc tải thư mục và ZIP lên không (F-41).
- **Q-09:** thêm mâu thuẫn về định dạng ngày giờ (F-42).
- **Q-02, Q-03:** thêm gợi ý lấy từ bộ TC (dự án FEEC; vai trò ES và PM). Hai câu này vẫn mở.

---

## Phụ lục A · Pattern dự kiến cho từng khu vực — đầu vào cho Tester [ĐỀ XUẤT]

Theo `rules/tester.md` rule 10 và `skills/tc-authoring/references/patterns.md`.

| Khu vực / chức năng | Pattern | Nguồn |
|---|---|---|
| Hộp thoại Tạo thư mục; Đổi tên (chưa có màn) | P1 · Popup có nhập liệu | tr.7 |
| Xoá; Xoá vĩnh viễn | P2 · Xoá có xác nhận | tr.3, 4, 5, 11, 15 |
| Di chuyển, Xoá, Tải xuống từ «⋮» thư mục, «⋮» tệp và thanh hàng loạt | P3 · Lặp theo lối vào | inventory §D |
| Tải tệp lên; Tải thư mục lên; Tải lên phiên bản mới | P4 · Upload | tr.2, 8, 13 |
| Mọi thao tác ghi | P5 · Kiểm chéo vai trò | chờ Q-03 |
| Tạo thư mục, đổi tên, tải lên, di chuyển, khôi phục khi trùng tên | P6 · Trùng tên theo mọi đường vào | chờ Q-10 → Q-13, Q-18 |
| Cột «Người cập nhật cuối ⇅», «Cập nhật lần cuối ⇅» sau khi tạo hoặc tải lên | P7 · Thông tin bản ghi sau khi tạo | K2, K3 |
| Trình xem | P8 · Xem trước | tr.12 |
| Phân trang | P9 · Phân trang | K1 #24–#27 |
| Ô tìm kiếm | P10 · Tìm kiếm | K1 #11–#12 |
| «Tất cả các bước», «Tài liệu dự án» | P11 · Bộ lọc dạng danh sách chọn | K1 #13–#14; tr.6 |
| Bảng danh sách; bảng trong thùng rác | P12 · Bảng dữ liệu | K1, K2, K3; tr.15 |

## Phụ lục B · Mô hình trạng thái sơ bộ [SUY LUẬN — chưa đưa vào baseline]

- **Mục (tệp hoặc thư mục):** Đang dùng → «Xoá» → Trong thùng rác → «Khôi phục» → Đang dùng. Từ Trong thùng rác → «Xoá vĩnh viễn» → không còn. Thư mục hệ thống không có chuyển trạng thái nào.
- **Phiên bản của một tệp:** bản mang nhãn «Hiện tại» trở thành phiên bản cũ khi có phiên bản mới được tải lên (Q-17).

## Phụ lục C · Thuật ngữ (nháp)

| Thuật ngữ | Nghĩa theo mockup | Không nhầm với |
|---|---|---|
| «Thư mục hệ thống» | Thư mục không xoá, đổi tên, di chuyển được; không có checkbox và nút «⋮» (tr.1, tr.5) | «Thư mục đặc biệt» — tên khác trong ô chú giải tr.5, chờ Q-20 |
| «Thư mục công trình cũ» | Tên của một thư mục hệ thống, đồng thời là một lựa chọn của bộ lọc phạm vi (tr.6) | «Tài liệu dự án» |
| «Tài liệu dự án» | Giá trị mặc định của bộ lọc phạm vi (K1 #14; tr.6) | — |
| «Thùng rác» | Nơi chứa mục đã xoá; từ đây khôi phục hoặc xoá vĩnh viễn (tr.14–15) | «Xoá vĩnh viễn» |
| «Phiên bản» · «Hiện tại» | Các lần tải lên của cùng một tệp; bản mới nhất mang nhãn «Hiện tại» (tr.13) | Tệp riêng có hậu tố "_rev" trong tên |
| mục | Một tệp hoặc một thư mục («mục đã chọn» tr.4–5; «0 mục» tr.14) | tệp — cột «Tên tệp ⇅» chứa cả thư mục, chờ Q-20 |

---

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.2 | 2026-10-02 | Thêm §7 Tạo mới folder (UC-DOC-007): nguồn bộ TC FEEC; bảng NV, FD, MS (tiếng Nhật gốc + tiếng Việt dịch tạm), BR, luồng, tác động phụ; rà soát 8 TC (logic, thứ tự, dữ liệu); thứ tự đề xuất. Thêm F-35 → F-42. Thêm nguồn và quy ước 「…」 ở đầu file | FB-021 · FB-022 · trả lời của Hanna 02/10 |
| v0.1 | 2026-10-02 | Bản đầu: ba-analysis bước 0–3 trên mockup bản 5 | — |
