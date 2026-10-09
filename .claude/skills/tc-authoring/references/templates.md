# Mẫu dữ liệu và mẫu câu hỏi

## 1. File dữ liệu đầu vào — TSV phẳng

Một dòng một TC. Cột cha **lặp lại ở mọi dòng**, script sẽ gộp lúc xuất.

```
I	II	III	IV	Pri	Name	Pre	Step	Expected	UC	Wait
Login	Email	Display	Default	High	Verify the default display of the Email field	Not logged in, open the Customer Portal sign-in page	1. Observe the Email field	- Label: Email with a red *\n- Placeholder: name@company.com	AUTH-001	
Login	Email	Validation	Empty	High	Verify signing in with an empty Email	Not logged in, open the Customer Portal sign-in page	1. Leave Email empty\n2. Click Sign in	- The sign-in request is not sent\n- An error message shows under the Email field	AUTH-001	Text lỗi nguyên văn → Q-L-01
```

Quy ước: `\n` trong ô là xuống dòng. Cột `Wait` có giá trị thì dòng đó bị tô đỏ và cột `Expected` được phép để trống.

Lệnh dựng file:

```
python scripts/tc_build_xlsx.py --data tc_login.tsv --sheet Login \
  --function "AUTH-L0001_Login" --screen "Login · Customer Portal" \
  --creator "<tên>" --source "<file thiết kế, trang, ngày>" --out TestCase.xlsx
```

## 2. Mẫu câu hỏi

```
Q-L-04 · Khoá tài khoản · CHẶN
- Câu hỏi: sai mật khẩu bao nhiêu lần thì khoá? Khoá bao lâu? Mở khoá bằng cách nào?
- Vì sao cần: thiết kế có màn Locked nhưng không nói điều kiện vào trạng thái đó.
- Ảnh hưởng: 3 TC chưa viết được kết quả mong đợi.
- Đề xuất mặc định: khoá sau 5 lần sai trong 15 phút, tự mở sau 30 phút.
- Cần xác nhận: đồng ý hay đổi?
```

Mức: `CHẶN` khi không có câu trả lời thì không viết được TC · `QUAN TRỌNG` khi viết được nhưng có thể phải sửa · `NHỎ` khi chỉ ảnh hưởng chi tiết hiển thị.

## 3. Mẫu báo cáo cuối việc

```
Màn <tên>: <n> TC · phủ <m> UC · <k> dòng còn câu hỏi mở.
Chờ trả lời: Q-L-01 … Q-L-13, trong đó <j> câu mức CHẶN.
Chưa viết được: <danh sách khu vực>, vì <lý do>.
```

## 4. Bảng UC → sheet (ở Cover)

Mỗi UC của baseline đúng một dòng. Cột `Sheet` ghi một trong ba: tên sheet · `Chờ: <lý do>` · `Kiểm ở: <sheet>` (UC không có sheet riêng). Xem `rules/tc-authoring.md` mục G.

| UC | Tên UC | Sheet | Ghi chú |
|---|---|---|---|
| SCP-03 | Create scope | Scopes | |
| WSP-01 | Create workspace | Workspaces | Mở từ Scopes ("Link framework") chỉ kiểm mở đúng form, scope điền sẵn (rule 26) |
| AUD-01 | Record audit events | Kiểm ở: mọi sheet có hành động ghi vết | Nhóm Ghi vết |
| BLK-01 | Upload documents in bulk | Chờ: chưa có thiết kế Bulk | |
