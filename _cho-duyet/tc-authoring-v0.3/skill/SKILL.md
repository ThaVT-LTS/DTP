---
name: tc-authoring
description: Viết và cập nhật file test case Excel bàn giao được — một màn hình một sheet, bốn cấp Classification I–IV có gộp ô, khu vực theo thứ tự mắt đọc, mỗi TC truy vết tới một UC, dữ liệu và nhãn giao diện tách ra khoá {{...}}, dòng chưa có căn cứ thì để trống và tô đỏ. Gồm thư viện 12 pattern cho các thao tác cơ bản (tạo, sửa, xoá, di chuyển, upload, xem trước, tìm kiếm, lọc, phân trang, chọn hàng loạt, bảng, kiểm chéo vai trò), quy ước cột và định dạng (Times New Roman 10, căn trái, quy tắc gộp ô, một bảng màu), script thêm sheet vào file TC mẫu của dự án, script dựng file xlsx và script kiểm tra. Dùng skill này khi người dùng muốn viết test case cho một màn hình hay một luồng, chuyển bộ TC sang ngôn ngữ khác, rà soát bộ TC cũ, hoặc hỏi "viết TC cho màn này".
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
  Cover            thông tin bộ test, lịch sử thay đổi
  Hướng dẫn        quy ước, giải nghĩa bốn cấp, giá trị hợp lệ
  _Data            dữ liệu test dùng chung, gọi bằng {{...}}
  _Labels          nhãn giao diện nguyên văn, gọi bằng {{...}}
  _Patterns        checklist của từng loại khu vực
  <Màn hình>       mỗi màn một sheet
  FLOW-nn          mỗi luồng nghiệp vụ xuyên màn một sheet
  Test_Report      tổng hợp, sinh bằng công thức
```

Dự án đã có file TC mẫu thì bộ sheet và form là của file mẫu (rule 24); danh sách trên là form mặc định, dùng khi chưa có file mẫu.

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

Viết dữ liệu dạng **bảng phẳng** (giá trị cột cha lặp ở mọi dòng), rồi chọn đường dựng theo rule 24.

**Dự án đã có file mẫu (mặc định).** File mẫu ghi ở `profile.md` của dự án. Thêm sheet vào chính file đó, nhân bản form của một sheet TC đã duyệt:

```
python scripts/tc_add_sheet.py --book <file mẫu>.xlsx --like Login --sheet Scopes --data scopes.tsv \
    --function "..." --screen "..." --creator "..." --created dd/mm/yyyy --source "..." \
    --report Test_Report --change "ngày|version|mục|A|mô tả|tham chiếu" --out <file>.xlsx
```

Script làm trên XML (cần `lxml`) nên giữ nguyên logo, dropdown và các sheet khác; mọi kiểu ô lấy từ sheet mẫu. Nó còn: gộp ô bốn cột Classification, tô dòng còn câu hỏi mở, sửa vùng công thức tổng kết, nới dropdown Priority/Result, dựng lại sheet báo cáo cho mọi sheet TC, thêm một dòng Record of change. Không mở rồi lưu file mẫu bằng openpyxl: openpyxl làm rơi logo và dropdown.

**File mẫu mới nhận, hoặc file bị sửa tay.** Đưa cả file về một phông, một bảng màu trước khi dùng làm mẫu:

```
python scripts/tc_restyle.py <file>.xlsx --out <file>.xlsx [--copy-style "*!F11>W11,X11"] \
    [--rename-header "Tên cũ=Tên mới"] [--fix-summary] [--change "ngày|version|mục|M|mô tả|tham chiếu"]
```

`--copy-style` chép kiểu của một ô sang ô lệch; `--fix-summary` kéo vùng đếm của khối tổng kết về đúng dòng dữ liệu đầu. Script không đổi bố cục: ô nào của file mẫu khác rule về căn lề, gộp ô, chiều cao dòng thì giữ nguyên và ghi thành câu hỏi (rule 24).

**Dự án chưa có file mẫu.** Dựng bản tạm, và hỏi người dùng file mẫu trước khi bàn giao:

```
python scripts/tc_build_xlsx.py --data tc_login.tsv --sheet Login --out TestCase.xlsx
```

Cả bốn script lấy phông và bảng màu từ `scripts/tc_palette.py` (khớp `references/format.md` §4).

## Bước 7 — Kiểm

```
python scripts/tc_check.py TestCase.xlsx --like <sheet TC mẫu>
```

Script báo: TC thiếu `UC_ID` · `TVP_ID` trùng · kết quả mong đợi mơ hồ · dòng còn chuỗi ngôn ngữ gốc mà không khai ở cột `Open question` · khoá `{{...}}` chưa có trong `_Data`/`_Labels` · khu vực thiếu nhóm bắt buộc · UC chưa có TC nào · kiểu ô sai phông, sai cỡ chữ, chữ nghiêng, gạch chân hoặc dùng màu ngoài bảng màu · dòng có `Open question` mà chưa tô · khối tổng kết đếm thiếu dòng dữ liệu. Có `--like`: sheet TC nào khác form sheet mẫu (khối tiêu đề, độ rộng cột, trang in, kiểu ô dữ liệu, dropdown) cũng báo lỗi.

Phần kiểm định dạng đọc thẳng XML và xét **mọi kiểu ô đang dùng ở mọi sheet**: ô có nội dung, ô trống đã định dạng (người chạy test sẽ gõ kết quả vào đó), kiểu mặc định của cột và dòng, chữ định dạng riêng từng đoạn trong một ô, kể cả màu theme và màu indexed.

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
| v0.3 | 2026-10-02 | Bước 6 có ba đường dựng; mặc định là `tc_add_sheet.py` (thêm sheet vào file mẫu của dự án, nhân bản form của sheet TC đã duyệt). Thêm `tc_restyle.py` (đưa cả file về một phông, một bảng màu; tuỳ chọn chép kiểu ô, đổi tên cột, sửa vùng đếm của khối tổng kết) và `tc_palette.py` (một nguồn bảng màu cho mọi script). Bảng màu đổi theo file mẫu, một màu nền tiêu đề `00B0F0`. `tc_check.py`: thêm `--like`; phần kiểm định dạng đọc thẳng XML nên xét cả ô trống đã định dạng, kiểu mặc định của cột và dòng, chữ định dạng từng đoạn, chữ nghiêng và gạch chân, màu theme và indexed; bắt dòng có `Open question` chưa tô; bắt khối tổng kết đếm thiếu dòng; hết cảnh báo nhầm dấu `·` `—`. `tc_build_xlsx.py`: sửa nhãn `UC-[NGOÀI UC]`, chiều cao dòng theo nội dung. **Chờ duyệt.** | FB-019 · FB-016 |
| v0.2 | 2026-10-02 | Cột `Chờ text` đổi tên thành `Open question`. `tc_check.py` kiểm thêm phông, cỡ chữ và màu của mọi ô ở mọi sheet theo bảng màu trong `references/format.md` §4. **Chờ duyệt.** | FB-015 · FB-016 |
| v0.1 | 2026-10-01 | Khởi tạo: 7 bước, hai chế độ phụ (chuyển ngôn ngữ, rút pattern từ bộ TC cũ), thư viện 12 pattern, quy ước định dạng, hai script. | FB-010 → FB-013 |
