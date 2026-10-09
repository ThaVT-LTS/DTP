# Rà soát bản Word "Tạo thư mục mới" và mockup bản 5

Phiên bản v0.1 · 02/10/2026 · Người rà: Claude (phiên khác với phiên đã soạn tài liệu)

**Đã đọc**

| # | File | Ghi chú |
|---|---|---|
| 1 | `Tạo thư mục mới — nghiệp vụ, câu hỏi, SRS US UC.docx` | Gửi 2 lần, hai file giống nhau từng byte. Xuất từ Claude Docs, bản sửa lần 10. Có 1 hình (sơ đồ luồng) |
| 2 | `Quan_ly_tai_lieu_mockup5.pdf` | 15 trang, mỗi trang 1 màn. Trùng từng byte với bản trong `docs/source/` |
| 3 | `FEEC_PM_IT_Test_Case_Document_v3.xlsx`, sheet Document | Lấy từ `docs/source/` để kiểm các chỗ bản Word trích TC |
| 4 | `tao-thu-muc_nghiep-vu-srs-us-uc.md` trong `docs/analysis/Quan_ly_tai_lieu_mockup-v5/` | Bản đang nằm trong thư mục, dùng để so với bản Word |

Không có phần nào không đọc được.

---

## 1. Kết luận

1. **Bản Word là bản cũ.** Trong bản Word cả 12 câu hỏi còn ghi «Chờ trả lời». Bản trong thư mục `qa-pipeline` đã ghi đủ trả lời của Hanna ngày 02/10 cho 12 câu, cộng thêm C2, C3. Bản Word có 15 AC, bản trong thư mục có 23 AC.
2. **10/12 đề xuất mặc định trong bản Word khác với trả lời thật.** Chỉ Q5 và Q11 khớp. Ai viết test theo bản Word sẽ sai ở 10 chỗ đó (bảng ở mục 3).
3. **Phần bản Word trích từ mockup và từ bộ TC cũ thì đúng.** Mình kiểm lại từng chỗ, chỉ có 1 chỗ trích thiếu nửa câu (mục 4).
4. **Mockup bản 5 chỉ vẽ 2 màn cho việc tạo thư mục** (tr.2 và tr.7). Các trạng thái đã chốt qua trả lời đều chưa có hình (mục 5).
5. **Còn 6 điểm chưa bản nào hỏi tới** (mục 6). Đáng chú ý nhất: tên dài 255 ký tự bị trùng thì thêm " (1)" sẽ thành 259 ký tự.

---

## 2. Mục đích của phần này

- **Ai dùng:** thành viên dự án trong hệ thống quản lý dự án FEEC. File TC ghi màn hình là "DM-L0001_図書管理", tên màn "Quản lý thư viện" `[FEEC xlsx · Document!C1:C2]`. Mockup ghi «Quản lý dự án › LTS › Quản lý tài liệu» `[mockup5 tr.1]`.
- **Để làm gì:** người dùng tự dựng cây thư mục cho tài liệu của một dự án, bên cạnh các thư mục có sẵn («Quản lý rủi ro», «Xem xét chi phí») và thư mục hệ thống «Thư mục công trình cũ» `[mockup5 tr.1]`.
- **Ràng buộc định hình thiết kế:** thư mục có thể được tải xuống máy người dùng. `[SUY LUẬN: thanh hàng loạt có «Tải xuống» ở tr.5 + bộ ký tự cấm trùng với ký tự Windows không cho dùng trong tên + có giới hạn tổng độ dài đường dẫn]` Vì vậy các quy tắc về tên (ký tự cấm, dấu cách đầu cuối, 255 ký tự, 20 cấp, độ dài đường dẫn) đều nhằm giữ cho cây thư mục tải về được và mở được trên máy.
- **Soát ngược:** quy tắc "trùng tên thì tự thêm số" đi ngược ràng buộc trên ở một chỗ: tên đã dài sát giới hạn thì thêm số sẽ vượt giới hạn. Xem N1 ở mục 6.

---

## 3. Bản Word so với trả lời đã ghi trong thư mục

Cột "Trả lời đã ghi" lấy từ `tao-thu-muc_nghiep-vu-srs-us-uc.md`, mục "Câu hỏi và trả lời".

| Câu | Đề xuất mặc định trong bản Word | Trả lời đã ghi (Hanna, 02/10) | Kết quả |
|---|---|---|---|
| Q1 | «Thư mục công trình cũ» là cấp 1. Ở cấp 20, hộp thoại vẫn mở, bấm «Lưu» mới báo lỗi | «Thư mục công trình cũ» không tính là cấp, bên trong được đủ 20 cấp. Ở cấp 20, mở hộp thoại là thấy cảnh báo vàng, nút lưu bị tắt (C3) | **Khác** |
| Q2 | Giữ 255 ký tự đầu và báo lỗi tên quá dài dưới ô | Tự cắt, không báo lỗi | **Khác** |
| Q3 | Báo "Vui lòng nhập tên thư mục."; tự cắt khoảng trắng đầu, cuối | Báo "Vui lòng nhập tên tệp."; không tự cắt, có dấu cách ở đầu hoặc cuối thì báo lỗi | **Khác** |
| Q4 | Chỉ so với thư mục; có phân biệt Full-width và Half-width | So với cả thư mục lẫn tệp, kể cả mục trong «Thùng rác»; khác hoa thường hay Full/Half-width vẫn tính là trùng; có câu thông báo tên mới | **Khác** |
| Q5 | Tạo được bên trong «Thư mục công trình cũ» | Được | Khớp |
| Q6 | ES và PM tạo được; vai trò khác không thấy «Tạo mới» | Tạm bỏ qua phân quyền, màn này tính là có toàn quyền | **Khác** |
| Q7 | Cấm `\ / : * ? " < >`, dấu gạch đứng, và tên chỉ gồm dấu chấm | Cấm đúng 8 ký tự `\ / : * ? " < >`. Dấu gạch đứng và tên chỉ gồm dấu chấm: còn mở (C5), mặc định mới là không cấm | **Khác** |
| Q8 | Chữ có dấu luôn tính 1 ký tự | "Tại sảo" tính là 9 ký tự: mỗi dấu tính thêm 1 | **Ngược lại** |
| Q9 | Báo "Đã tạo thư mục." | Báo "Tôi đã tạo một thư mục." | **Khác câu chữ** |
| Q10 | Dòng vị trí hiện tên thư mục đang đứng | Hiện cả đường dẫn, bấm được vào từng thư mục | **Khác** |
| Q11 | «Huỷ», «×», Esc đóng ngay, không hỏi lại | Esc đóng, không hỏi lại | Khớp |
| Q12 | Báo "Không thể tạo thư mục. Vui lòng thử lại." | Báo "Không thể tạo thư mục."; thêm quy tắc mới: tổng độ dài đường dẫn có giới hạn | **Khác câu chữ + thêm quy tắc** |

**Hệ quả với nội dung bản Word**

- AC viết theo mặc định cũ, nay sai: AC-02, AC-06, AC-07, AC-08, AC-09, AC-11, AC-15.
- MSG-01 (tên quá dài) đã bị bỏ. MSG-03, MSG-04, MSG-05, MSG-06 đổi câu chữ.
- Sơ đồ luồng trong bản Word kiểm theo thứ tự "Tên hợp lệ? → Cấp mới ≤ 20? → Trùng tên?" sau khi bấm «Lưu». Theo C3, số cấp được kiểm ngay khi mở hộp thoại. Hình trong thư mục (`tao-thu-muc_so-do-luong.png`) là file khác với hình trong bản Word.
- Bản Word thiếu hẳn: giới hạn đường dẫn (BR-08), quy tắc dấu cách (BR-02), trùng với tệp và với mục trong «Thùng rác».

---

## 4. Bản Word so với mockup bản 5 và bộ TC cũ

### 4.1 Trích từ mockup

| Chỗ bản Word trích | Mockup bản 5 | Kết quả |
|---|---|---|
| Menu «Tạo mới» 3 mục: «Tạo thư mục mới», «Tải tệp lên», «Tải thư mục lên» | tr.2 | Khớp |
| Hộp thoại: «Tạo thư mục», «Thư mục mới sẽ được tạo tại: Quản lý tài liệu», «Tên thư mục *», «Nhập tên thư mục», «Còn 255 ký tự (tối đa 255)», «Huỷ», «Lưu», «×» | tr.7 | Khớp |
| Nút «Lưu» trông vẫn bấm được khi ô rỗng | tr.7: nút nền đậm | Khớp |
| «Thư mục công trình cũ» là thư mục hệ thống | tr.1 nhãn «Thư mục hệ thống»; tr.5 «Thư mục đặc biệt: không thể xoá, đổi tên hay di chuyển — nên không có checkbox và nút ⋮» | Khớp |
| Hai phạm vi «Tài liệu dự án», «Thư mục công trình cũ» | tr.6 | Khớp |
| Thư mục có «Định dạng», «Dung lượng» là «—»; ngày giờ «30/09/2026 15:02» | tr.10, dòng «Tài liệu tham khảo» | Khớp |
| «Bấm + Tạo mới để tải tệp hoặc tạo thư mục con.» | tr.9 ghi đủ là: tiêu đề «Chưa có tệp nào», dòng «Thư mục này chưa có tệp được tải lên. Bấm + Tạo mới để tải tệp hoặc tạo thư mục con.» | **Trích thiếu** nửa đầu câu và tiêu đề |

Bản trong thư mục cũng trích thiếu như vậy ở FR-07 và AC-22.

### 4.2 Trích từ bộ TC cũ

Mình mở lại 14 TC bản Word nhắc tới (TC_021, 022, 055, 079 → 083, 139, 141, 143, 144, 146, 150). Mọi chỗ trích đều đúng, gồm:

- TC_021 chỉ ghi 2 mục `[Document!K33]`.
- TC_022 ghi "Hiển thị màn hình: PM0035" `[K34]`.
- TC_080 có hai bước cùng đánh số 3 `[J92]`.
- TC_081 còn ghi 10階層 `[K93]`.
- Kết quả Round 2 nằm lệch sang cột Remark của Round 1 (cột Q).
- 378 ô chữ ở dạng tổ hợp (mình đếm lại bằng script, ra đúng 378).

Các con số bản Word tự ghi cũng đúng: 15 điểm nghiệp vụ (4 đủ, 11 thiếu), 12 câu hỏi, 8 FR, 9 BR, 6 thông báo, 15 AC, 7 AC chưa có TC.

---

## 5. Mockup bản 5 chưa vẽ gì

Theo thứ tự ưu tiên nguồn (trả lời của Hanna > mockup > hệ thống đang chạy), các trạng thái sau đã có quy tắc nhưng mockup chưa có hình. Người viết test không có nhãn nguyên văn và vị trí hiển thị để đối chiếu.

| # | Trạng thái | Căn cứ quy tắc | Mockup |
|---|---|---|---|
| D1 | Cảnh báo vàng ở đầu hộp thoại khi đang ở cấp 20, nút lưu bị tắt | C3 | Chưa vẽ |
| D2 | Cảnh báo vàng khi đường dẫn hết chỗ, bộ đếm "Còn 0 ký tự (tối đa 0 ký tự)" | Q12, ảnh 3 | Chưa vẽ |
| D3 | Câu báo lỗi của ô tên: tên rỗng, dấu cách đầu cuối, ký tự cấm. Hiện ở đâu, màu gì | Q3, Q7 | Chưa vẽ |
| D4 | Thông báo sau khi tạo: "Tôi đã tạo một thư mục." và câu báo tên mới khi trùng. Dạng toast hay hộp thoại, tự tắt hay phải bấm | Q9, Q4 | Chưa vẽ |
| D5 | Dòng vị trí dạng đường dẫn bấm được | Q10, ảnh 2 | tr.7 chỉ vẽ lúc đứng ở gốc, là chữ thường «Quản lý tài liệu» |
| D6 | Hộp thoại khi đứng trong thư mục con và trong «Thư mục công trình cũ» | Q5 | Chưa vẽ |
| D7 | Nút «Lưu» khi ô rỗng | Q3: bấm được, rồi báo lỗi | tr.7 khớp |

Bản trong thư mục đã ghi: nhãn trên hệ thống đang chạy khác mockup ("Tạo một thư mục", "Nhập tên tệp", "Hủy bỏ"), và TC tạm theo nhãn mockup.

---

## 6. Điểm chưa bản nào hỏi tới

Mình tìm trong bản Word, bản trong thư mục, `questions.md` và file case cha con; 6 điểm dưới đây chưa có. Mỗi điểm kèm đề xuất mặc định để Hanna chỉ cần đồng ý hoặc sửa.

| # | Câu hỏi | Vì sao cần | Đề xuất mặc định | Mức |
|---|---|---|---|---|
| N1 | Tên dài 255 ký tự mà bị trùng thì sao? Thêm " (1)" sẽ thành 259 ký tự, vượt giới hạn 255. Tương tự khi đường dẫn gần hết chỗ | Hai quy tắc đã chốt (tối đa 255; trùng thì tự thêm số) mâu thuẫn nhau ở ca biên này | Không tạo, báo lỗi và giữ hộp thoại để người dùng rút ngắn tên | QUAN TRỌNG |
| N2 | Chữ Nhật có dấu đục như "デ", "ガ" tính mấy ký tự? | Chốt 02/10 nói Full-width tính 1. Nhưng "Tại sảo" tính 9 cho thấy hệ thống đếm theo dạng tách dấu; đếm kiểu đó thì "デ" là 2, "データ" là 4, "ガイド" là 5. Hệ thống dùng tiếng Nhật nên tên kiểu này rất hay gặp | Tính theo dạng tách dấu, nhất quán với "Tại sảo" | QUAN TRỌNG |
| N3 | Nhấn Enter trong ô tên có lưu không? Đang gõ dở bằng bộ gõ tiếng Nhật hoặc tiếng Việt thì Enter chỉ chốt chữ hay lưu luôn? | Q11 mới hỏi Esc. Với bộ gõ tiếng Nhật, Enter dùng để chốt chữ; nếu lưu luôn thì tên bị tạo dở | Enter = «Lưu»; khi đang gõ dở thì Enter chỉ chốt chữ | QUAN TRỌNG |
| N4 | Đang lọc theo bước (bộ lọc «Tất cả các bước» chọn giá trị khác) hoặc đang có từ khoá tìm kiếm mà tạo thư mục: thư mục mới có hiện trong danh sách không? | Thư mục không có bước và có thể không khớp từ khoá, nên tạo xong có thể không thấy đâu. Mockup tr.10 đã bỏ cột bước nhưng vẫn giữ bộ lọc | Tạo xong thì xoá lọc và tìm kiếm, hiện thư mục mới | NHỎ |
| N5 | Dán tên có ký tự xuống dòng hoặc tab thì sao? | Q7 chỉ liệt kê 8 ký tự cấm nhìn thấy được | Đổi xuống dòng và tab thành dấu cách | NHỎ |
| N6 | Tạo thư mục con có đổi «Cập nhật lần cuối» và «Người cập nhật cuối» của thư mục cha không? | tr.1: thư mục gốc đang ghi «—» ở cột người cập nhật; cần biết để viết kết quả mong đợi cho dòng thư mục cha | Không đổi | NHỎ |

---

## 7. Đề nghị

1. Dùng bản trong thư mục `qa-pipeline` làm bản chuẩn; không dùng bản Word này để viết test. Nếu cần bản Word mới thì xuất lại từ nội dung trong thư mục.
2. Hanna trả lời N1, N2, N3 trước; N4 → N6 có thể theo mặc định.
3. Sửa câu trích tr.9 cho đủ ở FR-07 và AC-22 của bản trong thư mục.
4. Gửi D1 → D6 cho người vẽ mockup, hoặc xác nhận lấy ảnh hệ thống đang chạy làm hình tham chiếu cho các trạng thái đó.

Mình chưa sửa file nào đang có trong thư mục; mục 2 và 3 chờ Hanna đồng ý.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-10-02 | Khởi tạo | Yêu cầu "đọc và phân tích" ngày 02/10 |
