---
name: tc-authoring
description: Viết và cập nhật file test case Excel bàn giao được — một màn hình một sheet, bốn cấp Classification I–IV có gộp ô, khu vực theo thứ tự mắt đọc, mỗi TC truy vết tới một UC, dữ liệu và nhãn giao diện tách ra khoá {{...}}, dòng chưa có căn cứ thì để trống và tô đỏ. Gồm thư viện 12 pattern cho các thao tác cơ bản (tạo, sửa, xoá, di chuyển, upload, xem trước, tìm kiếm, lọc, phân trang, chọn hàng loạt, bảng, kiểm chéo vai trò), quy ước cột và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô), script dựng file xlsx và script kiểm tra. Dùng skill này khi người dùng muốn viết test case cho một màn hình hay một luồng, chuyển bộ TC sang ngôn ngữ khác, rà soát bộ TC cũ, hoặc hỏi "viết TC cho màn này".
---

# Viết test case (v0.2)

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
  Cover            thông tin bộ test, lịch sử thay đổi
  Hướng dẫn        quy ước, giải nghĩa bốn cấp, giá trị hợp lệ
  _Data            dữ liệu test dùng chung, gọi bằng {{...}}
  _Labels          nhãn giao diện nguyên văn, gọi bằng {{...}}
  _Patterns        checklist của từng loại khu vực
  <Màn hình>       mỗi màn một sheet
  FLOW-nn          mỗi luồng nghiệp vụ xuyên màn một sheet
  Test_Report      tổng hợp, sinh bằng công thức
```

---

## Bước 1 — Xác định nguồn và màn hình

1. Liệt kê ba nguồn đang có: tài liệu yêu cầu, bản thiết kế, hệ thống đang chạy. Ghi rõ bản nào, ngày nào.
2. Đối chiếu danh sách màn hình giữa ba nguồn. Lệch chỗ nào thì ghi câu hỏi, không tự chọn.
3. Chốt tên sheet theo tên mục menu của hệ thống.

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

## Bước 5 — Viết TC

Theo pattern của từng khu vực, theo thứ tự: hiển thị → nhập liệu → kiểm tra dữ liệu → thành công → không thành công → phân quyền → bảo mật.

Trong mỗi nhóm, xếp case cùng kết quả liền nhau để gộp ô được.

Quy tắc không được phá:
- mỗi TC một `UC_ID`;
- kết quả mong đợi quan sát được;
- **chưa có căn cứ thì để trống kết quả, ghi câu hỏi vào cột `Open question`, tô đỏ**;
- giá trị và nhãn dùng khoá `{{...}}`.

## Bước 6 — Dựng file

Viết dữ liệu dạng **bảng phẳng** (giá trị cột cha lặp ở mọi dòng), rồi:

```
python scripts/tc_build_xlsx.py --data tc_login.tsv --sheet Login --out TestCase.xlsx
```

Script tự: gộp ô bốn cột Classification theo quy tắc, đặt phông Times New Roman 10, căn trái, tô đỏ dòng còn câu hỏi mở, dựng khối thông tin đầu sheet và hàng tiêu đề hai tầng.

## Bước 7 — Kiểm

```
python scripts/tc_check.py TestCase.xlsx
```

Script báo: TC thiếu `UC_ID` · `TVP_ID` trùng · kết quả mong đợi mơ hồ · dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khoá `{{...}}` chưa có trong `_Data`/`_Labels` · khu vực thiếu nhóm bắt buộc · UC chưa có TC nào · ô sai phông, sai cỡ chữ hoặc dùng màu ngoài bảng màu (mọi sheet).

Sửa đến khi script sạch, hoặc ghi lý do loại trừ.

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
| v0.2 | 2026-10-02 | Cột `Chờ text` đổi tên thành `Open question`. `tc_check.py` kiểm thêm phông, cỡ chữ và màu của mọi ô ở mọi sheet theo bảng màu trong `references/format.md` §4. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: 7 bước, hai chế độ phụ (chuyển ngôn ngữ, rút pattern từ bộ TC cũ), thư viện 12 pattern, quy ước định dạng, hai script. | FB-010 → FB-013 |
