---
name: tc-authoring
description: Viết và cập nhật file test case Excel bàn giao được — một màn hình (tính theo mục menu) một sheet, vai trò nằm trong sheet, bốn cấp Classification I–IV có gộp ô, khu vực theo thứ tự mắt đọc, mỗi TC truy vết tới một UC, vai trò, dữ liệu và nhãn ghi bằng chữ ngay trong ô, dòng chưa có căn cứ thì để trống và tô đỏ. Gồm thư viện 12 pattern cho các thao tác cơ bản (tạo, sửa, xoá, di chuyển, upload, xem trước, tìm kiếm, lọc, phân trang, chọn hàng loạt, bảng, kiểm chéo vai trò), quy ước cột và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô), script dựng file xlsx và script kiểm tra. Dùng skill này khi người dùng muốn viết test case cho một màn hình hay một luồng, chuyển bộ TC sang ngôn ngữ khác, rà soát bộ TC cũ, hoặc hỏi "viết TC cho màn này".
---

# Viết test case (v0.3)

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

## Bước 1 — Xác định nguồn và màn hình

1. Liệt kê ba nguồn đang có: tài liệu yêu cầu, bản thiết kế, hệ thống đang chạy. Ghi rõ bản nào, ngày nào.
2. Đối chiếu danh sách màn hình giữa ba nguồn. Lệch chỗ nào thì ghi câu hỏi, không tự chọn.
3. Chốt tên sheet theo tên mục menu của hệ thống.
4. Lập bảng UC → sheet theo `rules/tc-authoring.md` mục G: mỗi UC của baseline đúng một chỗ — tên sheet, `Chờ: <lý do>` hoặc `Kiểm ở: <sheet>`. Ghi vào Cover. Mẫu: `references/templates.md` §4.
5. Liệt kê vai trò và phạm vi dữ liệu của từng vai trò (thấy dữ liệu nào, làm được gì). Tên vai trò lấy đúng như tài liệu yêu cầu, vì Pre-condition ghi vai trò bằng tên này (`rules/tc-authoring.md` rule 14).
6. Đọc `profile.md` của dự án: ngôn ngữ viết file TC (rule 16), tester có được gọi API không (rule 29), file TC mẫu.

Prototype chỉ cho biết *màn nào có, nút nào có*. Hành vi lấy từ tài liệu yêu cầu.

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

Theo pattern của từng khu vực, theo thứ tự: hiển thị → nhập liệu → kiểm tra dữ liệu → thành công → không thành công → phân quyền → bảo mật (file tiếng Anh: Display → Input → Validation → Success → Failure → Permission → Security; bảng từ ở `references/format.md` §7). Màn có danh sách thì trạng thái rỗng đứng trước tạo mới và các khu vực cần dữ liệu (`rules/tc-authoring.md` rule 4).

Trong mỗi nhóm, xếp case cùng kết quả liền nhau để gộp ô được.

Quy tắc không được phá:
- mỗi TC một `UC_ID`;
- kết quả mong đợi quan sát được;
- **chưa có căn cứ thì để trống kết quả, ghi câu hỏi vào cột `Open question`, tô đỏ**;
- Pre-condition mở đầu bằng dòng đăng nhập theo `rules/tc-authoring.md` rule 14 (`Logged in as <role>` / `Not logged in`); dữ liệu và nhãn ghi thẳng trong ô;
- Step là thao tác cụ thể; Expected mỗi mục một dòng, không trỏ sang TC khác (rule 12, 14);
- không viết TC gọi thẳng API khi `profile.md` ghi tester không được gọi API (rule 29).

## Bước 6 — Dựng file

Viết dữ liệu dạng **bảng phẳng** (giá trị cột cha lặp ở mọi dòng), rồi:

```
python scripts/tc_build_xlsx.py --data tc_login.tsv --sheet Login --out TestCase.xlsx
```

Script tự: gộp ô bốn cột Classification theo quy tắc, đặt phông Times New Roman 10, căn trái, tô đỏ dòng còn câu hỏi mở, dựng khối thông tin đầu sheet và hàng tiêu đề hai tầng.

Rule viết TC còn đang bàn với người dùng thì chưa gửi file TC; chốt xong mới gửi một lần. Bản xem trước (chức năng → nhóm kiểm → tên case, đánh dấu Mới / Sửa / Bỏ) là tuỳ chọn. Thấy vấn đề cần người dùng xem ngay thì gửi sớm.

## Bước 7 — Kiểm

```
python scripts/tc_check.py TestCase.xlsx
```

Script báo: TC thiếu `UC_ID` · `TVP_ID` trùng · kết quả mong đợi mơ hồ · dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khu vực thiếu nhóm bắt buộc · UC chưa có TC nào · ô sai phông, sai cỡ chữ hoặc dùng màu ngoài bảng màu (mọi sheet).

Chạy thêm `--lang en` khi `profile.md` ghi file TC viết tiếng Anh: script cảnh báo ô còn chữ tiếng Việt, trừ cột `Open question` và sheet `Cần xác nhận`.

Sửa đến khi script sạch, hoặc ghi lý do loại trừ từng dòng. Không bỏ qua cả một loại lỗi: lỗi giả thì sửa bảng màu hoặc script trước, vì lỗi thật có thể nằm lẫn trong đó.

---

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
| v0.3 | 2026-10-05 | Vai trò, dữ liệu, nhãn ghi bằng chữ ngay trong ô (`rules/tc-authoring.md` rule 14); bỏ sheet `_Data`, `_Labels` khỏi Đầu ra, Bước 7, `tc_check.py`, `references/templates.md`, `references/format.md`. Đầu ra: Cover thêm bảng UC → sheet; thêm sheet `Phân quyền` và `API` tuỳ chọn. Bước 1 thêm bước 4–6: bảng UC → sheet, vai trò, đọc `profile.md`. Bước 4: TC điểm hiển thị ở sheet của hành động. Bước 5: thứ tự nhóm bằng tiếng Anh, trạng thái rỗng trước, quy tắc Pre-condition, Step, Expected, API. Bước 6: chưa gửi file TC khi rule còn đang bàn. Bước 7: `--lang en`, không bỏ qua cả một loại lỗi. `references/format.md`: bảng màu theo file TC mẫu, bảng từ tên nhóm kiểm (§7). `references/patterns.md`: P5, P12, mục hay thiếu #3. `tc_check.py`: bảng màu mới, câu mơ hồ tiếng Anh, nhóm Success/Failure, `--lang en`, cảnh báo ký tự bỏ qua dấu câu, bỏ qua sheet `Phân quyền`. `tc_build_xlsx.py`: bảng màu mới. Hanna duyệt 05/10, trừ phần **chờ duyệt**: chia sheet (Đầu ra, Bước 1 bước 4, Bước 4, sheet `Phân quyền`), câu "không bỏ qua cả một loại lỗi" ở Bước 7, bảng màu và căn giữa theo chiều dọc (đề xuất của AI theo file mẫu). | FB-???[chia-sheet] · FB-???[gop-tach-sheet] · FB-???[pre-condition] · FB-???[tieng-anh] · FB-???[rong-truoc] · FB-???[rong-du] · FB-???[khong-lung-lo] · FB-???[moi-dong] · FB-???[xem-truoc] · FB-???[api] · FB-016 · FB-013 |
| v0.2 | 2026-10-02 | Cột `Chờ text` đổi tên thành `Open question`. `tc_check.py` kiểm thêm phông, cỡ chữ và màu của mọi ô ở mọi sheet theo bảng màu trong `references/format.md` §4. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: 7 bước, hai chế độ phụ (chuyển ngôn ngữ, rút pattern từ bộ TC cũ), thư viện 12 pattern, quy ước định dạng, hai script. | FB-010 → FB-013 |
