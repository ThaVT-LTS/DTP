# Quy ước cột và định dạng file test case

## 1. Khối thông tin đầu sheet

| Ô | Nội dung |
|---|---|
| `C3` | Tên chức năng, ví dụ `AUTH-L0001_Đăng nhập` |
| `C4` | Tên màn hình |
| `C5` | Người viết |
| `C6` | Ngày tạo |
| `C7` | Nguồn tham chiếu — tên file thiết kế, trang, ngày |

Bên phải cùng khối là bảng tổng kết theo vòng test: `Round` · `Total` · `Passed` · `Failed` · `Pending` · `Blocked` · `NA` · `Not execute`, mỗi vòng một dòng, tính bằng công thức.

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
| W | Open question | Câu hỏi còn chưa có trả lời của dòng này, mẫu `<câu hỏi>? (<ghi chú nguồn>) → Q-<mã màn>-nn`. Có giá trị thì tô đỏ; đã có trả lời thì xoá và bỏ tô (rule 13, 23) |
| X | UC | Mã UC mà TC này phủ |

Thêm vòng test thì thêm một khối năm cột, không chèn vào giữa.

## 4. Phông chữ và căn lề

- **Times New Roman, cỡ 10** cho toàn bộ vùng dữ liệu.
- **Căn lề trái** cho mọi ô (cột No. theo file mẫu).
- Ô đã gộp (ô neo ở cột B–E): **căn giữa theo chiều dọc, xuống dòng**, để chữ dài không bị che.
- Ô dữ liệu: **căn giữa theo chiều dọc** như file TC mẫu, bật xuống dòng tự động. `tc_check.py` báo lỗi ô sai (rule 19).
- Dòng còn câu hỏi mở: nền đỏ nhạt ở cột `Expected result` và cột `Open question`.

### Bảng màu và phông — một bộ duy nhất cho mọi sheet, mọi file

| Dùng cho | Nền | Chữ |
|---|---|---|
| Hàng tiêu đề (nhóm cột và tên cột) | `00B0F0` | màu mặc định, đậm |
| Nhãn khối thông tin, tiêu đề bảng tổng kết | `00B0F0` | màu mặc định, đậm |
| Vùng dữ liệu, giá trị của khối thông tin | không nền | `363A45` |
| Dòng còn câu hỏi mở | `FBE9E7` ở cột `Expected result` và `Open question` | `363A45` ở `Expected result`, `B8362B` ở `Open question` |
| Đường kẻ ô | — | màu mặc định, nét mảnh |

Bảng màu lấy theo file TC mẫu (`profile.md`, dòng "File TC mẫu của dự án"); file mẫu SGS DTP và FEEC dùng cùng bảng này. File mẫu đổi màu thì sửa bảng này và `PALETTE` của hai script trước.

- Phông **Times New Roman cỡ 10** áp cho **mọi ô có nội dung ở mọi sheet**, kể cả `Cover`, `Hướng dẫn`, `_Patterns`, `FLOW-nn`, `Test_Report`. Nhấn mạnh chỉ bằng chữ đậm, không đổi phông, không đổi cỡ.
- Không dùng màu ngoài bảng trên. Cần thêm một màu (ví dụ cho trạng thái mới) thì thêm vào bảng này và vào `PALETTE` của hai script trước, rồi mới dùng.
- Định dạng do script đặt. Không tô màu, đổi phông bằng tay trên file đã xuất.
- `tc_check.py` kiểm phông, cỡ chữ, màu nền, màu chữ của mọi ô có nội dung và báo lỗi theo từng sheet.

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

Việc gộp ô do `scripts/tc_build_xlsx.py` làm lúc xuất file.

**Không sửa tay trên file đã gộp.** Ô gộp không lọc được, không sort được, kéo công thức xuống là vỡ, và script đọc ra ô rỗng. Cần sửa thì sửa bản phẳng rồi xuất lại.

## 7. Giá trị hợp lệ

| Cột | Giá trị |
|---|---|
| Priority | `High` · `Medium` · `Low` |
| Result | `Passed` · `Failed` · `Pending` · `Blocked` · `NA` · `Not execute` |

Mọi giá trị không thuộc danh sách trên đều bị `tc_check.py` báo lỗi.

**Tên nhóm kiểm** — bảng từ cố định, ghi theo ngôn ngữ của file TC (`rules/tc-authoring.md` rule 16). Mỗi ô một thứ tiếng: file tiếng Anh ghi `Login`, không ghi `Đăng nhập - Login`.

| Tiếng Việt | English |
|---|---|
| Hiển thị | Display |
| Nhập liệu | Input |
| Kiểm tra dữ liệu | Validation |
| Thành công | Success |
| Không thành công | Failure |
| Phân quyền | Permission |
| Bảo mật | Security |
| Điều hướng | Navigation |
| Trạng thái rỗng | Empty state |
| Ghi vết | Audit log |
| Tìm kiếm | Search |
| Lọc | Filter |
| Sắp xếp | Sort |
| Phân trang | Pagination |
