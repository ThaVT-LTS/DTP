# Quy ước cột và định dạng file test case

§1–§3 mô tả form mặc định. Dự án đã có file TC mẫu thì bố cục theo file mẫu (rule 24); chỗ nào file mẫu khác các mục này thì theo file mẫu và ghi thành câu hỏi. §4 (phông, bảng màu), §5–§7 áp cho mọi file.

## 1. Khối thông tin đầu sheet

| Ô | Nội dung |
|---|---|
| `C3` | Tên chức năng, ví dụ `AUTH-L0001_Đăng nhập` |
| `C4` | Tên màn hình |
| `C5` | Người viết |
| `C6` | Ngày tạo |
| `C7` | Nguồn tham chiếu — tên file thiết kế, trang, ngày |

Bên phải cùng khối là bảng tổng kết theo vòng test: `Round` · `Total` · `Passed` · `Failed` · `Pending` · `Blocked` · `NA` · `Not execute`, mỗi vòng một dòng, tính bằng công thức. Vùng đếm của công thức bắt đầu ở dòng dữ liệu đầu tiên và phủ tới dòng dữ liệu cuối — `tc_check.py` báo lỗi khi đếm thiếu.

## 2. Hàng tiêu đề hai tầng

- Hàng 11: nhóm cột — `Classification` gộp ngang bốn cột I–IV; `Test Round 1` gộp ngang năm cột; `Test Round 2` gộp ngang năm cột. Các cột còn lại gộp dọc hàng 11–12.
- Hàng 12: tên cột con `I` `II` `III` `IV`.
- Dữ liệu bắt đầu từ **hàng 13**.

## 3. Cột

| Cột | Tên | Nội dung |
|---|---|---|
| A | No. | Số thứ tự |
| B | I | Feature |
| C | II | Khu vực hoặc nhóm kiểm |
| D | III | Mục kiểm hoặc nhóm kết quả |
| E | IV | Case cụ thể |
| F | Priority | `High` · `Medium` · `Low` |
| G | TVP_ID | `TC_nnn`, duy nhất trong sheet |
| H | Test case name / Test view point | Kiểm cái gì, một câu |
| I | Pre-condition | Vai trò, dữ liệu, trạng thái cần có trước |
| J | Step | Đánh số từng bước, mỗi bước một hành động |
| K | Expected result | Quan sát được. Chưa có căn cứ thì **để trống** |
| L | Dev test | Dev tự kiểm trước khi bàn giao |
| M–Q | Round 1 | Result · Test person · Test date · Bug_ID · Remark |
| R–V | Round 2 | như trên |
| W | Open question | Chuỗi hoặc câu hỏi còn thiếu ở dòng này. Có giá trị thì tô đỏ |
| X | UC | Mã UC mà TC này phủ |

Thêm vòng test thì thêm một khối năm cột, không chèn vào giữa.

## 4. Phông chữ và căn lề

- **Times New Roman, cỡ 10** cho toàn bộ vùng dữ liệu.
- **Căn lề trái** cho mọi ô.
- Ô đã gộp: **căn giữa theo chiều dọc**.
- Ô dữ liệu: **căn trên theo chiều dọc**, bật xuống dòng tự động.
- Dòng còn câu hỏi mở: nền đỏ nhạt ở cột `Open question`, và ở cột `Expected result` khi ô đó còn trống.
- Dự án đã có file mẫu thì căn lề, đường kẻ, độ rộng cột theo sheet TC của file mẫu (rule 24); các gạch đầu dòng trên chỉ áp khi chưa có file mẫu.

### Bảng màu và phông — một bộ duy nhất cho mọi sheet, mọi file

Bảng màu lấy theo file mẫu của dự án và chỉ có **một** màu nền tiêu đề — người dùng chọn ngày 02/10/2026: "cho 1 trong 2 màu xanh này" của file mẫu (FB-019, FB-016). Màu cụ thể `00B0F0` (xanh dương, màu file mẫu dùng nhiều nhất) là [GIẢ ĐỊNH] của AI, chờ người dùng xác nhận; đổi sang màu kia thì sửa một dòng `HEAD_FILL` trong `scripts/tc_palette.py` rồi chạy `tc_restyle.py`. Script đọc bảng màu từ `scripts/tc_palette.py`; bảng dưới và file đó phải khớp nhau.

| Dùng cho | Nền | Chữ |
|---|---|---|
| Mọi ô có nền: hàng tiêu đề, nhãn khối thông tin, khối tổng kết vòng test (Round 1 và Round 2 cùng màu), dòng tổng của báo cáo | `00B0F0` | `FFFFFF` |
| Mọi ô không nền: vùng dữ liệu, giá trị khối thông tin, trang bìa | không nền | `363A45` |
| Dòng còn câu hỏi mở: ô `Open question`, và ô `Expected result` khi còn trống | `FBE9E7` | `B8362B` ở ô `Open question` |
| Đường kẻ ô | — | màu tự động |

- Phông **Times New Roman cỡ 10** áp cho **mọi ô ở mọi sheet**, kể cả `Cover`, `Hướng dẫn`, `_Data`, `_Labels`, `_Patterns`, `FLOW-nn`, `Test_Report`. Nhấn mạnh chỉ bằng chữ đậm, không đổi phông, không đổi cỡ, không dùng chữ nghiêng hay gạch chân.
- Không dùng màu ngoài bảng trên. Cần thêm một màu (ví dụ cho trạng thái mới) thì thêm vào bảng này và vào `scripts/tc_palette.py` trước, rồi mới dùng.
- Định dạng do script đặt. Không tô màu, đổi phông bằng tay trên file đã xuất. File có sẵn bị lệch (file mẫu mới nhận, file sửa tay) thì chạy `scripts/tc_restyle.py` để đưa cả file về đúng bảng này.
- `tc_check.py` kiểm phông, cỡ chữ, kiểu chữ, màu nền, màu chữ của **mọi kiểu ô đang dùng** — ô có nội dung, ô trống đã định dạng (người chạy test sẽ gõ kết quả vào đó), kiểu mặc định của cột và dòng, chữ định dạng riêng từng đoạn trong một ô; kể cả màu theme và màu indexed — và báo lỗi theo từng sheet.

## 5. Quy tắc gộp ô

Áp cho bốn cột Classification I–IV:

1. Gộp các dòng **liền nhau có cùng giá trị**. Ô trống nghĩa là "giống dòng trên".
2. Cụm con **không được vượt ranh giới cụm cha**: cột III đổi cụm thì cột IV phải cắt tại đó, dù giá trị ở IV vẫn giống nhau.
3. Cụm chỉ có một dòng thì **không gộp**.
4. Chỉ **ô neo** giữ giá trị; các ô còn lại trong cụm để trống.

Ví dụ đúng:

```
B13:B64   Đăng nhập - Login          ← cả feature
  C44:C53   Đăng nhập - Sign in      ← một khu vực
    D44:D47   Thành công             ← cắt đúng trong C44:C53
    D48:D53   Không thành công
```

Ví dụ sai: `D45:D90` vắt qua ranh giới của `C44:C53` sang khu vực kế tiếp.

## 6. Viết phẳng, gộp lúc xuất

Người viết và AI làm việc trên bảng **phẳng** — giá trị cột cha lặp lại ở mọi dòng. Như vậy lọc được, sort được, sửa hàng loạt được, và script đọc được.

Việc gộp ô do script làm lúc xuất file: `scripts/tc_add_sheet.py` khi dự án đã có file mẫu, `scripts/tc_build_xlsx.py` khi chưa có.

**Không sửa tay trên file đã gộp.** Ô gộp không lọc được, không sort được, kéo công thức xuống là vỡ, và script đọc ra ô rỗng. Cần sửa thì sửa bản phẳng rồi xuất lại.

## 7. Giá trị hợp lệ

| Cột | Giá trị |
|---|---|
| Priority | `High` · `Medium` · `Low` |
| Result | `Passed` · `Failed` · `Pending` · `Blocked` · `NA` · `Not execute` |

Mọi giá trị không thuộc danh sách trên đều bị `tc_check.py` báo lỗi.
