---
name: tc-authoring
description: Viết và cập nhật file test case Excel bàn giao được — một màn hình (tính theo mục menu) một sheet, vai trò nằm trong sheet, bốn cấp Classification I–IV có gộp ô, khu vực theo thứ tự mắt đọc, mỗi TC truy vết tới một UC, vai trò, dữ liệu và nhãn ghi bằng chữ ngay trong ô, dòng chưa có căn cứ thì để trống và tô đỏ. Gồm thư viện 12 pattern cho các thao tác cơ bản (tạo, sửa, xoá, di chuyển, upload, xem trước, tìm kiếm, lọc, phân trang, chọn hàng loạt, bảng, kiểm chéo vai trò), quy ước cột và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô), script dựng file xlsx và script kiểm tra. Dùng skill này khi người dùng muốn viết test case cho một màn hình hay một luồng, chuyển bộ TC sang ngôn ngữ khác, rà soát bộ TC cũ, hoặc hỏi "viết TC cho màn này".
---

# Viết test case (v0.8)

Tuân thủ `rules/common.md`, `rules/feedback.md`, `rules/tester.md` và `rules/tc-authoring.md` ở mọi bước.

| Cần gì | Đọc |
|---|---|
| Khu vực này thuộc loại nào, phải kiểm những gì | `references/patterns.md` |
| Cột nào, gộp ô ra sao, phông chữ, căn lề | `references/format.md` |
| Mẫu dữ liệu đầu vào cho script, mẫu câu hỏi | `references/templates.md` |

Vì sao cần skill riêng: viết TC thẳng từ màn hình thì chỉ ra được những gì nhìn thấy. Thư viện pattern biến mỗi khu vực thành một checklist đã kiểm chứng từ bộ TC thật, nên phần lặp lại không phải nghĩ nữa, chỉ còn phần đặc thù.

## Đầu ra

```
<tên bộ test>.xlsx
  Cover            thông tin bộ test, lịch sử thay đổi, bảng UC → sheet
  Hướng dẫn        quy ước, giải nghĩa bốn cấp, giá trị hợp lệ
  _Patterns        checklist của từng loại khu vực
  Phân quyền       tuỳ chọn: ma trận vai trò × UC, mỗi ô ghi TC ID đã phủ, không chứa TC
  <Màn hình>       mỗi màn một sheet, màn tính theo mục menu (rules/tc-authoring.md rule 3, mục G)
  API              tuỳ chọn: TC gọi thẳng API, chỉ khi profile.md ghi tester được gọi API (rule 29)
  FLOW-nn          mỗi luồng nghiệp vụ xuyên màn một sheet
  Test_Report      tổng hợp, sinh bằng công thức
```

---

## Bước 0 — Bảng độ phủ UC theo wave (rule 40)

Trước khi viết: lấy danh sách UC Phase 1 của UC List hiện hành và wave ghi ở `profile.md`; với mỗi UC đếm số case chạy được (có Expected, không mang `[Phase 2]`, `[OUT]`). UC nào chưa có case chạy được thì đưa vào danh sách việc của lượt này. Ghi bảng vào file thiết kế của lượt (vd khung case cha). `tc_check.py --uc <danh sách>` in bảng này theo wave.

## Bước 1 — Xác định nguồn và màn hình

1. Liệt kê các nguồn đang có theo thứ tự ưu tiên của rule 1: quyết định chốt (Final Confirmation, decision log), UC, tiêu chí chấp nhận của user story, Figma, web demo. Ghi rõ bản nào, ngày nào.
2. Đối chiếu danh sách màn hình giữa các nguồn. Lệch thì xử lý theo rule 1; không áp được mới ghi câu hỏi.
3. Chốt tên sheet theo tên mục menu của hệ thống.
4. Lập bảng UC → sheet theo `rules/tc-authoring.md` mục G: mỗi UC của baseline đúng một chỗ — tên sheet, `Chờ: <lý do>` hoặc `Kiểm ở: <sheet>`. Ghi vào Cover. Mẫu: `references/templates.md` §4.
5. Liệt kê vai trò và phạm vi dữ liệu của từng vai trò (thấy dữ liệu nào, làm được gì). Tên vai trò lấy đúng như tài liệu yêu cầu, vì Pre-condition ghi vai trò bằng tên này (`rules/tc-authoring.md` rule 14).
6. Đọc `profile.md` của dự án: ngôn ngữ viết file TC (rule 16), tester có được gọi API không (rule 29), file TC mẫu.

Web đã hiện hành vi hợp lý, không trái nguồn trên nó thì theo web (rule 1).

## Bước 1b — Đọc đủ nguồn và rà màn đã làm (rule 36, 37)

1. Mở **cả ba nguồn** của màn: UC bản hiện hành (đọc trực tiếp ở nơi lưu, ghi số bản), Figma (trang, khung), hệ thống (vai trò, ngày). Với Figma: mở từng khung của màn, phóng to đọc chữ thật, ghi số liệu thấy trên khung. Thiếu nguồn nào thì dừng, ghi "chưa đọc" ở đầu khung và hỏi người dùng link hoặc quyền; không viết Expected thay.
2. Ghi vào khung case cha bảng "ba nguồn nói gì" theo từng UC, mỗi điểm lệch một câu hỏi.
3. **Rà màn đã làm**: với mọi sheet đã có, tìm case chịu ảnh hưởng của điều vừa đọc (luồng đổi, nhãn đổi, trạng thái mới, số liệu mới). Lập bảng "màn đã làm bị ảnh hưởng" (rule 37): sheet · case · điều lệch · xử lý. Case của AI thì sửa; case có chữ của người dùng thì nêu câu hỏi. Báo người dùng đã rà sheet nào.

## Bước 2 — Cắt khu vực

Chia màn hình thành khu vực theo thứ tự mắt đọc: **trên → dưới trong một cột, hết cột trái sang cột phải**.

Với mỗi khu vực, khai **pattern** của nó (xem `references/patterns.md`). Pattern quyết định checklist bắt buộc.

## Bước 3 — Liệt kê phần tử bấm được

Mọi nút, liên kết, tab, icon, dòng bảng — mỗi cái một dòng trong `_Nav`: mục đích · kiểu đích (Trang · Popup · Panel · Inline · Tải file · Không làm gì) · màn đích · nguồn xác minh · trạng thái.

Chưa biết đích thì `CHƯA RÕ`, tô đỏ, sinh câu hỏi. **Không viết TC điều hướng cho phần tử chưa xác minh.**

## Bước 4 — Khai điểm hiển thị hệ quả

Mỗi hành động ghi dữ liệu phải trả lời: dữ liệu vừa tạo **xuất hiện ở những đâu**, ai nhìn thấy, sau bao lâu, có điều kiện gì không.

Mỗi điểm hiển thị là một TC riêng. Điểm nào chỉ xuất hiện sau một hành động khác thì ghi rõ — đây là chỗ sai nhiều nhất.

TC điểm hiển thị viết ở sheet của hành động, kể cả khi điểm đó nằm ở màn khác hay vai trò khác (rule 27). Chỉ chuỗi nhiều hành động qua nhiều chức năng mới tách ra `FLOW-nn`.

## Bước 5 — Viết TC

Theo pattern của từng khu vực, theo thứ tự: hiển thị → nhập liệu → không thành công → thành công → phân quyền → bảo mật (rule 8; file tiếng Anh: Display → Input → Failure → Success → Permission → Security; bảng từ ở `references/format.md` §7). Màn có danh sách thì trạng thái rỗng đứng trước tạo mới và các khu vực cần dữ liệu (`rules/tc-authoring.md` rule 4).

Trong mỗi nhóm, xếp case cùng kết quả liền nhau để gộp ô được.

Quy tắc không được phá:
- mỗi TC một `UC_ID`;
- kết quả mong đợi quan sát được;
- câu hỏi chỉ khi nguồn lệch mà không áp được rule 1, hoặc chưa có căn cứ: để trống Expected, ghi `Open question`, tô màu; Expected đề xuất thì tô vàng ô UC (rule 13);
- chữ báo lỗi chưa thấy trên web ghi theo mẫu của app, không hỏi (rule 13);
- Pre-condition mở đầu bằng `Login acc <vai trò> (<tên>) …` hoặc `Chưa đăng nhập`, không dấu `;` sau vai trò; không còn `{{…}}` (rule 14);
- Step: bước 1 nhập URL hoặc bấm menu trái; `button [Tên]`; case xem hiển thị ghi `Nhìn <vùng>`; không ghi "Kiểm tra…", "Mở màn…"; Expected mỗi mục một dòng, nhiều bước thì `Sau bước n: …` (rule 12, 14);
- chức năng chưa có thiết kế hoặc chưa làm Phase 1 thì `[Phase 2]` / `[Ngoài Phase 1]`; case lỗi thời `[OUT]`, không xoá, không đánh lại mã (rule 11, 40);
- không viết TC gọi thẳng API khi `profile.md` ghi tester không được gọi API (rule 29).

## Bước 6 — Dựng file

Viết dữ liệu dạng **bảng phẳng** (giá trị cột cha lặp ở mọi dòng), rồi:

```
python scripts/tc_build_xlsx.py --data tc_login.tsv --sheet Login --out TestCase.xlsx
```

Script tự: gộp ô bốn cột Classification theo quy tắc, đặt phông Times New Roman 10, căn trái, tô đỏ dòng còn câu hỏi mở, dựng khối thông tin đầu sheet và hàng tiêu đề hai tầng.

Case mới chèn vào **đúng nhóm Classification** của nó bằng `tc_rows.py` (giữ cụm gộp, mã TC, chiều cao dòng; dựng lại Test_Report theo nhóm), không thêm ở cuối sheet (rule 8). Thêm sheet vào file mẫu bằng `tc_add_sheet.py --creator <người viết>` (bắt buộc, rule 6) (ở `scripts/` của skill này, cùng `tc_palette.py`, `tc_restyle.py`): script này **chưa đặt căn lề** cho ô Classification của sheet mới. Sau khi dựng phải đặt xuống dòng, căn giữa dọc, căn trái cho ô neo ở cột B–E (`rules/tc-authoring.md` rule 19), rồi chạy Bước 7. Người dùng đã gửi lại file tự sửa thì dựng từ file đó (rule 34).

Rule viết TC còn đang bàn với người dùng thì chưa gửi file TC; chốt xong mới gửi một lần. Bản xem trước (chức năng → nhóm kiểm → tên case, đánh dấu Mới / Sửa / Bỏ) là tuỳ chọn. Thấy vấn đề cần người dùng xem ngay thì gửi sớm.

## Bước 6b — Tự soát nội dung trước khi giao (rule 38)

Sau khi dựng file, trước khi chạy Bước 7: quét sheet bằng script và đối chiếu `references/tu-soat.md` và danh sách ở `rules/tc-authoring.md` rule 38 — nguồn của Expected, Pre-condition dựng được trên dữ liệu thật, số tính toán thử lại trên số thật, câu hỏi đặt đúng case và có `?`, mỗi loại một case, case của sheet cũ đã xử lý, số báo trong chat lấy từ script, Cover và khung khớp file. Sửa hết rồi mới chạy `tc_check.py` và báo xong. Soát chéo của model khác (chế độ phụ bên dưới) bổ sung cho bước này, không thay thế.

## Bước 7 — Kiểm

Cổng trước khi giao (rule 38), cả hai **0 lỗi**:

```
python scripts/tc_fix_xlsx.py TestCase.xlsx --fix --creator Hanna
python scripts/tc_check.py TestCase.xlsx --creator Hanna [--uc uc_p1.txt]
```

Rồi mở file bằng Excel hoặc OnlyOffice, xem qua một sheet mới và một sheet cũ.

Script báo: TC thiếu `UC_ID` · `TVP_ID` trùng · kết quả mong đợi mơ hồ · dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khu vực thiếu nhóm bắt buộc · UC chưa có TC nào · ô sai phông, sai cỡ chữ hoặc dùng màu ngoài bảng màu (mọi sheet) · ô chữ của bảng TC chưa xuống dòng, chưa căn giữa dọc hoặc chưa căn trái (rule 19) · ô `Open question` có chữ mà không tô màu, hoặc tô màu mà đã hết câu hỏi (rule 13). Cảnh báo: ô `Open question` có phần không phải câu hỏi, thiếu dấu `?` (rule 23) — đọc từng cảnh báo, sửa thành câu hỏi thật.

Chạy thêm `--lang en` khi `profile.md` ghi file TC viết tiếng Anh: script cảnh báo ô còn chữ tiếng Việt, trừ cột `Open question` và sheet `Cần xác nhận`.

Sửa đến khi script sạch, hoặc ghi lý do loại trừ từng dòng. Không bỏ qua cả một loại lỗi: lỗi giả thì sửa bảng màu hoặc script trước, vì lỗi thật có thể nằm lẫn trong đó.

---

## Chế độ phụ — soát chéo giữa hai model (một bên soát, một bên sửa)

Dùng khi người dùng cho một model soát bản do model khác viết (vd Opus soát, Sonnet sửa), lặp tới khi hết lỗi.

1. **Bên soát chỉ liệt kê, không sửa file.** Ghi `tests/design/review_<sheet>_v<bản>.md`: tên file, số case; mục "Đã đạt"; lỗi theo nhóm, mỗi lỗi ghi số dòng (No.) cụ thể và vì sao sai; mục "Còn mở từ trước". Trong chat chỉ tóm tắt.
2. **Mỗi loại lỗi quét toàn sheet bằng script**, không chỉ các dòng đã thấy ở vòng trước (vd quét hết cột `Open question` tìm ô không phải câu hỏi). Soát cả: chữ người dùng đã sửa còn nguyên không (so với file của họ, rule 34); các câu bên sửa đã báo trong chat có đúng với file không (`rules/feedback.md` rule 16); Cover; hồ sơ đi kèm (khung case cha, `questions.md`). Kiểm thêm nguồn ghi trong câu hỏi có đúng không (rule 23).
2b. **Gửi đủ lỗi trong một lần** (rule 39). Vòng đầu, trước khi ghi file review, bên soát chạy hết danh sách rule 38 và mọi loại lỗi đã gặp ở các sheet trước trên toàn bộ case; mỗi lỗi thấy được thì quét tiếp mọi case cùng kiểu (cùng câu hỏi, cùng dữ liệu, cùng cách viết) và ghi tất cả vào cùng một mục. Không gửi review rồi mới tìm tiếp. Vòng sau chỉ còn hai loại: mục của vòng trước chưa sửa hết, và lỗi do bản sửa sinh ra. Lỗi đã có từ bản trước mà vòng trước bỏ sót vẫn phải báo, nhưng đánh dấu `sót từ vòng trước`, và đầu file review ghi số mục mỗi loại (chưa sửa hết · phát sinh do bản sửa · sót từ vòng trước).
3. **Bên sửa chỉ bắt đầu khi người dùng bảo** (`rules/feedback.md` rule 15). Sửa hết các mục của file review; mục cần người dùng quyết thì hỏi, không tự chọn. Dựng từ bản mới nhất (rule 34, 35), tăng số bản, thêm dòng Cover, ghi một FB loại L1 trỏ tới file review, chạy `tc_check.py` và `fb_report.py`, báo số liệu đếm bằng script.
4. Lặp bước 1–3 tới khi file review không còn lỗi. Lỗi lặp lại qua hai vòng thì đưa vào rule hoặc script (`rules/feedback.md` rule 11).

## Chế độ phụ — chuyển bộ TC sang ngôn ngữ khác

1. Trích mọi chuỗi ngôn ngữ gốc trong bộ TC, đếm tần suất.
2. Lập bảng đối chiếu, mỗi chuỗi ghi rõ **căn cứ**: bảng đối chiếu thật · danh sách phần tử đã duyệt · chưa có.
3. Dịch **chuỗi dài trước, chuỗi ngắn sau**. Chuỗi ngắn là con của chuỗi dài sẽ cắt nát chuỗi dài nếu làm ngược.
4. Chuỗi chưa có bản dịch chính thức: giữ nguyên, tô đỏ, ghi vào `Open question`. Không tự đặt.
5. Lập riêng danh sách **TC sai hành vi** — dịch xong vẫn sai, phải viết lại.

## Chế độ phụ — rà soát bộ TC cũ để rút pattern

Dùng khi có một hệ thống cũ đã có bộ TC chạy thật. Bộ TC đó là tài liệu đặc tả ngược: nó ghi lại các quy tắc nghiệp vụ mà tài liệu yêu cầu không có.

1. Đếm TC theo từng cấp Classification để biết chỗ nào dày, chỗ nào mỏng.
2. Đọc kết quả mong đợi của các case biên — chúng chứa giới hạn thật (dung lượng, số cấp, số ký tự) và text lỗi nguyên văn.
3. Đối chiếu với tài liệu yêu cầu: chỗ nào bộ TC trả lời được câu hỏi đang để mở thì đóng câu hỏi đó.
4. Chỗ nào mỏng bất thường so với các nhóm khác là lỗ hổng — ghi lại.
5. Gom thành pattern, bổ sung vào `references/patterns.md`.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.8 | 2026-10-15 | Theo bản tổng hợp 15/10 (`rules/tc-authoring.md` v0.10): thêm Bước 0 (bảng độ phủ UC theo wave); Bước 1 thứ tự 5 nguồn; Bước 5 thứ tự nhóm mới, dòng `Login acc`, Step, `[Phase 2]`/`[OUT]`, mẫu chữ báo lỗi; Bước 6 chèn case bằng `tc_rows.py`, `--creator` bắt buộc; Bước 6b đọc `references/tu-soat.md`; Bước 7 cổng `tc_fix_xlsx.py` + `tc_check.py --creator`. `tc_fix_xlsx.py`, `tc_rows.py`, phép kiểm mới của `tc_check.py`: **chờ file kèm theo**. | FB-074 · FB-075 · FB-076 · FB-077 · FB-078 · FB-079 · FB-080 · FB-081 · FB-082 |
| v0.7 | 2026-10-14 | `tc_add_sheet.py`, `tc_palette.py`, `tc_restyle.py` chép từ `_cho-duyet/tc-authoring-v0.3/` vào `scripts/` của skill; Bước 6 trỏ chỗ mới. `tc_check.py`, `tc_build_xlsx.py` giữ bản của skill (bản `_cho-duyet` là nhánh khác: `--like`, kiểm kiểu ô, kiểm Test_Report — chưa ghép). | FB-072 |
| v0.6 | 2026-10-09 | Chế độ soát chéo: thêm bước 2b — bên soát gửi đủ lỗi trong một lần; vòng sau chỉ báo mục chưa sửa hết và lỗi do bản sửa sinh ra, lỗi sót từ vòng trước phải đánh dấu và đếm (rule 39). **Chờ duyệt.** | FB-067 |
| v0.5 | 2026-10-09 | Thêm Bước 1b (đọc đủ ba nguồn, bảng màn đã làm bị ảnh hưởng) và Bước 6b (tự soát nội dung trước khi giao) theo `rules/tc-authoring.md` v0.7 rule 36–38. **Chờ duyệt.** | FB-064 |
| v0.4 | 2026-10-08 | Bước 6: `tc_add_sheet.py` chưa đặt căn lề ô Classification, phải đặt sau khi dựng; dựng từ file người dùng đã sửa. Bước 7: `tc_check.py` kiểm thêm căn lề và xuống dòng của ô chữ trong bảng TC (bỏ qua ô trong cụm gộp không phải ô neo), ô `Open question` có chữ mà không tô hoặc tô mà hết câu hỏi (lỗi), phần không phải câu hỏi (cảnh báo). Thêm chế độ phụ "soát chéo giữa hai model". `references/format.md` §3 cột W, §4: căn lề và mẫu câu hỏi theo rule 19, 23. **Chờ duyệt.** | FB-054 · FB-055 · FB-056 · FB-059 |
| v0.3 | 2026-10-05 | Vai trò, dữ liệu, nhãn ghi bằng chữ ngay trong ô (`rules/tc-authoring.md` rule 14); bỏ sheet `_Data`, `_Labels` khỏi Đầu ra, Bước 7, `tc_check.py`, `references/templates.md`, `references/format.md`. Đầu ra: Cover thêm bảng UC → sheet; thêm sheet `Phân quyền` và `API` tuỳ chọn. Bước 1 thêm bước 4–6: bảng UC → sheet, vai trò, đọc `profile.md`. Bước 4: TC điểm hiển thị ở sheet của hành động. Bước 5: thứ tự nhóm bằng tiếng Anh, trạng thái rỗng trước, quy tắc Pre-condition, Step, Expected, API. Bước 6: chưa gửi file TC khi rule còn đang bàn. Bước 7: `--lang en`, không bỏ qua cả một loại lỗi. `references/format.md`: bảng màu theo file TC mẫu, bảng từ tên nhóm kiểm (§7). `references/patterns.md`: P5, P12, mục hay thiếu #3. `tc_check.py`: bảng màu mới, câu mơ hồ tiếng Anh, nhóm Success/Failure, `--lang en`, cảnh báo ký tự bỏ qua dấu câu, bỏ qua sheet `Phân quyền`. `tc_build_xlsx.py`: bảng màu mới. Hanna duyệt 05/10, trừ phần **chờ duyệt**: chia sheet (Đầu ra, Bước 1 bước 4, Bước 4, sheet `Phân quyền`), câu "không bỏ qua cả một loại lỗi" ở Bước 7, bảng màu và căn giữa theo chiều dọc (đề xuất của AI theo file mẫu). | FB-029 · FB-030 · FB-035 · FB-031 · FB-032 · FB-033 · FB-034 · FB-036 · FB-038 · FB-039 · FB-016 · FB-013 |
| v0.2 | 2026-10-02 | Cột `Chờ text` đổi tên thành `Open question`. `tc_check.py` kiểm thêm phông, cỡ chữ và màu của mọi ô ở mọi sheet theo bảng màu trong `references/format.md` §4. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: 7 bước, hai chế độ phụ (chuyển ngôn ngữ, rút pattern từ bộ TC cũ), thư viện 12 pattern, quy ước định dạng, hai script. | FB-010 → FB-013 |

## Mẫu lỗi người dùng đã báo

Trước khi viết hoặc review case cho một màn, đọc `rules/bug-patterns.md` (rule 29 của `rules/automation.md`) và thêm case cho mọi mẫu áp dụng được với màn đó (dropdown cuộn, divider gây hiểu lầm, thứ tự dòng chính/phụ của thẻ, menu ⋮ theo trạng thái, nhãn bộ lọc, chọn một/nhiều đồng nhất, mục chọn được lên trên, múi giờ, Back trong wizard, giá trị gán cứng / chỉ tải 100 mục — quét bằng skill `hardcode-check`…).
