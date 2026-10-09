# Mẫu dữ liệu và mẫu câu hỏi

## 1. File dữ liệu đầu vào — TSV phẳng

Một dòng một TC. Cột cha **lặp lại ở mọi dòng**, script sẽ gộp lúc xuất.

```
I	II	III	IV	Pri	Name	Pre	Step	Expected	UC	Wait
Đăng nhập - Login	Email	Hiển thị	Mặc định	High	Kiểm tra hiển thị mặc định của trường Email	Chưa đăng nhập, mở {{url.customer}}	1. Kiểm tra trường Email	- Nhãn: Email kèm dấu * đỏ\n- Placeholder: name@company.com	AUTH-001	
Đăng nhập - Login	Email	Kiểm tra dữ liệu	Bỏ trống	High	Kiểm tra bỏ trống Email rồi đăng nhập	Chưa đăng nhập	1. Để trống Email\n2. Bấm Sign in	- Không gọi đăng nhập\n- Hiện lỗi dưới trường Email	AUTH-001	Text lỗi nguyên văn → Q-L-01
```

Quy ước: `\n` trong ô là xuống dòng. Cột `Wait` có giá trị thì dòng đó bị tô đỏ và cột `Expected` được phép để trống.

Lệnh dựng file:

```
python scripts/tc_build_xlsx.py --data tc_login.tsv --sheet Login \
  --function "AUTH-L0001_Đăng nhập" --screen "Login · Customer Portal" \
  --creator "<tên>" --source "<file thiết kế, trang, ngày>" --out TestCase.xlsx
```

## 2. Sheet `_Data`

| Khoá | Giá trị | Mô tả | Ghi chú |
|---|---|---|---|
| `{{user.cust_admin}}` | | Customer Admin của tenant A | Tạo được dữ liệu |
| `{{user.cust_viewer}}` | | Vai trò chỉ đọc | Dùng cho case phân quyền |
| `{{user.tenantB_admin}}` | | Admin của tenant B | Dùng cho case cách ly dữ liệu |
| `{{url.customer}}` | | Địa chỉ cổng khách hàng | |

## 3. Sheet `_Labels`

| Khoá | Nhãn nguyên văn | Màn hình | Nguồn |
|---|---|---|---|
| `{{btn.sign_in}}` | Sign in | Login | Thiết kế, trang 1 |
| `{{msg.required_email}}` | — chưa có — | Login | Chờ Q-L-01 |

Nhãn chưa có thì để `— chưa có —`, không tự đặt.

## 4. Mẫu câu hỏi

```
Q-L-04 · Khoá tài khoản · CHẶN
- Câu hỏi: sai mật khẩu bao nhiêu lần thì khoá? Khoá bao lâu? Mở khoá bằng cách nào?
- Vì sao cần: thiết kế có màn Locked nhưng không nói điều kiện vào trạng thái đó.
- Ảnh hưởng: 3 TC chưa viết được kết quả mong đợi.
- Đề xuất mặc định: khoá sau 5 lần sai trong 15 phút, tự mở sau 30 phút.
- Cần xác nhận: đồng ý hay đổi?
```

Mức: `CHẶN` khi không có câu trả lời thì không viết được TC · `QUAN TRỌNG` khi viết được nhưng có thể phải sửa · `NHỎ` khi chỉ ảnh hưởng chi tiết hiển thị.

## 5. Mẫu báo cáo cuối việc

```
Màn <tên>: <n> TC · phủ <m> UC · <k> dòng còn câu hỏi mở.
Chờ trả lời: Q-L-01 … Q-L-13, trong đó <j> câu mức CHẶN.
Chưa viết được: <danh sách khu vực>, vì <lý do>.
```
