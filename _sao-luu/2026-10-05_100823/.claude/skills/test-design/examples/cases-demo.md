# Test case — DEMO · Quản lý người dùng

> **VÍ DỤ MINH HỌA** — sinh từ `test-basis-demo.md` và `design-UC-DEMO-001.md`. Mẫu TC: `references/templates.md` §2.

| | |
|---|---|
| Test basis | examples/test-basis-demo.md (v1.0) |
| Số TC | 46 |
| Trạng thái | Đã tự review, chờ review độc lập |

## UC-DEMO-001 · Tạo người dùng và gửi lời mời

### I. Redirect

#### UC-DEMO-001-TC-R01 · Admin mở form từ nút Tạo người dùng
- Nhóm: Redirect
- Loại: Positive
- Ưu tiên: P1
- Kỹ thuật: Điều hướng
- Nguồn: UC-DEMO-001-NV-01, PM-USER-01
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, T1); đang ở /users
- Bước: 1) Bấm nút "Tạo người dùng"
- Mong đợi: Mở màn hình có tiêu đề "Tạo người dùng"; URL là /users/new
- Tag: @UC-DEMO-001 @redirect @positive @P1 @smoke
- Tự động hóa: Có

#### UC-DEMO-001-TC-R02 · Admin mở form bằng URL trực tiếp
- Nhóm: Redirect
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: Điều hướng
- Nguồn: UC-DEMO-001-NV-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, T1)
- Bước: 1) Nhập /users/new vào thanh địa chỉ
- Mong đợi: Mở màn hình có tiêu đề "Tạo người dùng"; URL giữ nguyên /users/new
- Tag: @UC-DEMO-001 @redirect @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-R03 · Chưa đăng nhập mở URL tạo người dùng thì phải đăng nhập rồi quay lại
- Nhóm: Redirect
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: Điều hướng
- Nguồn: UC-DEMO-001-NV-03
- Tiền điều kiện: Chưa đăng nhập (không có cookie phiên)
- Bước: 1) Mở /users/new; 2) Đăng nhập admin1@t1.demo.test
- Mong đợi: Sau bước 1 URL là /login; sau bước 2 URL là /users/new và hiện tiêu đề "Tạo người dùng"
- Tag: @UC-DEMO-001 @redirect @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-R04 · Member mở URL tạo người dùng bị chặn
- Nhóm: Redirect
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: Phân quyền
- Nguồn: UC-DEMO-001-NV-04, PM-USER-02
- Tiền điều kiện: Đăng nhập member1@t1.demo.test (Member, T1)
- Bước: 1) Mở /users/new
- Mong đợi: Hiện trang 403 với text "Bạn không có quyền truy cập trang này."; không hiện form "Tạo người dùng"
- Tag: @UC-DEMO-001 @redirect @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-R05 · Member không thấy nút Tạo người dùng
- Nhóm: Redirect
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: Phân quyền
- Nguồn: PM-USER-02
- Tiền điều kiện: Đăng nhập member1@t1.demo.test (Member, T1); đang ở /users
- Bước: 1) Quan sát màn hình "Người dùng"
- Mong đợi: Không có nút "Tạo người dùng" trên màn hình
- Tag: @UC-DEMO-001 @redirect @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-R06 · Gửi lời mời thành công thì về danh sách kèm thông báo
- Nhóm: Redirect
- Loại: Positive
- Ưu tiên: P1
- Kỹ thuật: Điều hướng
- Nguồn: UC-DEMO-001-NV-05, UC-DEMO-001-MS-07
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = "r06@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: URL là /users; hiện toast "Đã gửi lời mời đến r06@demo.test."
- Tag: @UC-DEMO-001 @redirect @positive @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-R07 · Hủy khi đã nhập và chọn Bỏ thay đổi
- Nhóm: Redirect
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: Điều hướng
- Nguồn: UC-DEMO-001-NV-06, UC-DEMO-001-MS-12
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"
- Bước: 1) Nhập Họ và tên; 2) Bấm "Hủy"; 3) Chọn "Bỏ thay đổi"
- Mong đợi: Sau bước 2 hiện hộp thoại "Bỏ các thay đổi chưa lưu?" có nút "Bỏ thay đổi" và "Ở lại"; sau bước 3 URL là /users; danh sách không có người dùng "Trần Minh"
- Tag: @UC-DEMO-001 @redirect @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-R08 · Hủy khi đã nhập và chọn Ở lại
- Nhóm: Redirect
- Loại: Positive
- Ưu tiên: P3
- Kỹ thuật: Điều hướng
- Nguồn: UC-DEMO-001-NV-06, UC-DEMO-001-MS-12
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"
- Bước: 1) Nhập Họ và tên; 2) Bấm "Hủy"; 3) Chọn "Ở lại"
- Mong đợi: Hộp thoại đóng; vẫn ở /users/new; "Họ và tên" vẫn là "Trần Minh"
- Tag: @UC-DEMO-001 @redirect @positive @P3
- Tự động hóa: Có

#### UC-DEMO-001-TC-R09 · Trạng thái form khi vừa mở
- Nhóm: Redirect
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: Điều hướng
- Nguồn: UC-DEMO-001-NV-07, UC-DEMO-001-FD-03
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, T1)
- Bước: 1) Mở /users/new
- Mong đợi: Tiêu đề "Tạo người dùng"; "Họ và tên" và "Email" trống; "Vai trò" = "Member"; con trỏ ở "Họ và tên"; nút "Gửi lời mời" bật
- Tag: @UC-DEMO-001 @redirect @positive @P2
- Tự động hóa: Có

### II. Validation

#### UC-DEMO-001-TC-V01 · Họ và tên có dấu tiếng Việt được chấp nhận và lưu đúng
- Nhóm: Validation
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-EP-01
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Nguyễn Thị Ánh"; Email = "v01@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến v01@demo.test."; dòng v01@demo.test trong danh sách có Họ và tên "Nguyễn Thị Ánh"
- Tag: @UC-DEMO-001 @validation @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V02 · Họ và tên có dấu ' và - được chấp nhận
- Nhóm: Validation
- Loại: Positive
- Ưu tiên: P3
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-EP-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Anne-Marie O'Neil"; Email = "v02@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến v02@demo.test."; dòng v02@demo.test có Họ và tên "Anne-Marie O'Neil"
- Tag: @UC-DEMO-001 @validation @positive @P3
- Tự động hóa: Có

#### UC-DEMO-001-TC-V03 · Họ và tên để trống bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-EP-03, UC-DEMO-001-MS-01
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = ""; Email = "v03@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Họ và tên" hiện "Vui lòng nhập họ và tên."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V04 · Họ và tên chỉ có khoảng trắng bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-EP-04, UC-DEMO-001-MS-01
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "   "; Email = "v04@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Họ và tên" hiện "Vui lòng nhập họ và tên."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V05 · Họ và tên 1 ký tự bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-BV-01, UC-DEMO-001-MS-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "A"; Email = "v05@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Họ và tên" hiện "Họ và tên từ 2 đến 50 ký tự."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V06 · Họ và tên 2 ký tự được chấp nhận
- Nhóm: Validation
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-BV-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "An"; Email = "v06@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến v06@demo.test."; dòng v06@demo.test có Họ và tên "An"
- Tag: @UC-DEMO-001 @validation @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V07 · Họ và tên 50 ký tự được chấp nhận và không bị cắt
- Nhóm: Validation
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-BV-03
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Nguyen " + 43 chữ "a" (50 ký tự); Email = "v07@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến v07@demo.test."; dòng v07@demo.test hiển thị đủ 50 ký tự của Họ và tên
- Tag: @UC-DEMO-001 @validation @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V08 · Họ và tên 51 ký tự bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-BV-04, UC-DEMO-001-MS-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Nguyen " + 44 chữ "a" (51 ký tự); Email = "v08@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Họ và tên" hiện "Họ và tên từ 2 đến 50 ký tự."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V09 · Họ và tên còn 1 ký tự sau khi trim bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P3
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-BV-05, UC-DEMO-001-MS-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = " A "; Email = "v09@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Họ và tên" hiện "Họ và tên từ 2 đến 50 ký tự."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P3
- Tự động hóa: Có

#### UC-DEMO-001-TC-V10 · Họ và tên có chữ số bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-EP-05, UC-DEMO-001-MS-03
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "An3"; Email = "v10@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Họ và tên" hiện "Họ và tên chỉ gồm chữ, khoảng trắng, dấu ' và -."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V11 · Họ và tên chứa script bị từ chối và không thực thi
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-EP-06, UC-DEMO-001-MS-03
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "<script>alert(1)</script>"; Email = "v11@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Họ và tên" hiện "Họ và tên chỉ gồm chữ, khoảng trắng, dấu ' và -."; không có hộp thoại alert nào xuất hiện; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-V12 · Họ và tên có khoảng trắng đầu cuối được trim khi lưu
- Nhóm: Validation
- Loại: Positive
- Ưu tiên: P3
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-EP-07
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "  Lan  "; Email = "v12@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến v12@demo.test."; dòng v12@demo.test có Họ và tên "Lan", không có khoảng trắng đầu/cuối
- Tag: @UC-DEMO-001 @validation @positive @P3
- Tự động hóa: Có

#### UC-DEMO-001-TC-V13 · Email để trống bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-02, UC-DEMO-001-EP-09, UC-DEMO-001-MS-04
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = ""; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Email" hiện "Vui lòng nhập email."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V14 · Email thiếu @ bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-02, UC-DEMO-001-EP-10, UC-DEMO-001-MS-05
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = "lan.demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Email" hiện "Email không đúng định dạng."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V15 · Email thiếu tên miền bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-02, UC-DEMO-001-EP-11, UC-DEMO-001-MS-05
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = "lan@"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Email" hiện "Email không đúng định dạng."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V16 · Email có khoảng trắng ở giữa bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-02, UC-DEMO-001-EP-12, UC-DEMO-001-MS-05
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = "lan nguyen@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Email" hiện "Email không đúng định dạng."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V17 · Email có khoảng trắng đầu cuối và chữ hoa được chuẩn hóa khi lưu
- Nhóm: Validation
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-02, UC-DEMO-001-EP-13, UC-DEMO-001-EP-14
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = "  V17@DEMO.TEST  "; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến v17@demo.test."; danh sách có dòng email "v17@demo.test" (chữ thường, không khoảng trắng)
- Tag: @UC-DEMO-001 @validation @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V18 · Email 254 ký tự được chấp nhận
- Nhóm: Validation
- Loại: Positive
- Ưu tiên: P3
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-02, UC-DEMO-001-BV-06
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = 64 ký tự + "@" + tên miền 189 ký tự, mỗi nhãn ≤ 63 (tổng 254); Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến <email>." với đủ 254 ký tự; danh sách hiển thị đủ email
- Tag: @UC-DEMO-001 @validation @positive @P3
- Tự động hóa: Có

#### UC-DEMO-001-TC-V19 · Email 255 ký tự bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P3
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-02, UC-DEMO-001-BV-07, UC-DEMO-001-MS-05
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Trần Minh"; Email = 64 ký tự + "@" + tên miền 190 ký tự, mỗi nhãn ≤ 63 (tổng 255); Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Email" hiện "Email không đúng định dạng."; không tạo người dùng; vẫn ở /users/new
- Tag: @UC-DEMO-001 @validation @negative @P3
- Tự động hóa: Có

#### UC-DEMO-001-TC-V20 · API từ chối vai trò ngoài danh sách
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: EP
- Nguồn: UC-DEMO-001-FD-03, UC-DEMO-001-EP-17, UC-DEMO-001-MS-13
- Tiền điều kiện: Có token của admin1@t1.demo.test (Admin, T1)
- Dữ liệu: body {"name": "Trần Minh", "email": "v20@demo.test", "role": "Owner"}
- Bước: 1) Gửi POST /api/users với body ở cột Dữ liệu; 2) Gửi GET /api/users?email=v20@demo.test
- Mong đợi: Bước 1 trả HTTP 400, body {"error": "INVALID_ROLE"}; bước 2 trả danh sách rỗng
- Tag: @UC-DEMO-001 @validation @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-V21 · API từ chối Họ và tên 51 ký tự khi bỏ qua kiểm tra trên UI
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: BVA
- Nguồn: UC-DEMO-001-FD-01, UC-DEMO-001-BV-04, UC-DEMO-001-MS-14
- Tiền điều kiện: Có token của admin1@t1.demo.test (Admin, T1)
- Dữ liệu: body {"name": "Nguyen " + 44 chữ "a", "email": "v21@demo.test", "role": "Member"}
- Bước: 1) Gửi POST /api/users với body ở cột Dữ liệu; 2) Gửi GET /api/users?email=v21@demo.test
- Mong đợi: Bước 1 trả HTTP 400, body có "error": "VALIDATION" và "fields" chứa "name"; bước 2 trả danh sách rỗng
- Tag: @UC-DEMO-001 @validation @negative @P1
- Tự động hóa: Có

### III. Function

#### UC-DEMO-001-TC-F01 · Admin tạo Member mới thành công
- Nhóm: Function
- Loại: Positive
- Ưu tiên: P1
- Kỹ thuật: Kịch bản
- Nguồn: UC-DEMO-001-MF-01, UC-DEMO-001-MF-02, UC-DEMO-001-MF-03, UC-DEMO-001-MF-04, UC-DEMO-001-DT-01-R1, UC-DEMO-001-BR-01, ST-USER-01, UC-DEMO-001-SE-01, PM-USER-01, UC-DEMO-001-EP-08, UC-DEMO-001-EP-16
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Phạm Hoa"; Email = "f01@demo.test"; Vai trò = Member
- Bước: 1) Nhập Họ và tên và Email, giữ Vai trò mặc định; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến f01@demo.test."; URL là /users; dòng đầu danh sách là f01@demo.test, Vai trò "Member", Trạng thái "Đã mời"
- Tag: @UC-DEMO-001 @function @positive @P1 @smoke
- Tự động hóa: Có

#### UC-DEMO-001-TC-F02 · Admin tạo Admin khi tenant đang có 4 Admin
- Nhóm: Function
- Loại: Positive
- Ưu tiên: P1
- Kỹ thuật: Bảng quyết định
- Nguồn: UC-DEMO-001-DT-01-R2, UC-DEMO-001-BR-02, UC-DEMO-001-EP-15
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"; T1 có đúng 4 Admin
- Dữ liệu: Họ và tên = "Lê Quang"; Email = "f02@demo.test"; Vai trò = Admin
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến f02@demo.test."; dòng f02@demo.test có Vai trò "Admin", Trạng thái "Đã mời"
- Tag: @UC-DEMO-001 @function @positive @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-F03 · Tạo Admin thứ 6 bị từ chối, Admin đang Invited vẫn được tính
- Nhóm: Function
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: Bảng quyết định
- Nguồn: UC-DEMO-001-DT-01-R3, UC-DEMO-001-BR-02, UC-DEMO-001-MS-10
- Tiền điều kiện: Đăng nhập admin1@t3.demo.test (Admin, T3); T3 có đúng 5 Admin, trong đó 1 người Invited; đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Lê Quang"; Email = "f03@demo.test"; Vai trò = Admin
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Vai trò" hiện "Tổ chức đã có tối đa 5 Admin."; không tạo người dùng; vẫn ở /users/new; T3 vẫn có 5 Admin
- Tag: @UC-DEMO-001 @function @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-F04 · Email trùng khác hoa thường trong tenant bị từ chối
- Nhóm: Function
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: Bảng quyết định
- Nguồn: UC-DEMO-001-DT-01-R4, UC-DEMO-001-BR-01, UC-DEMO-001-MS-06
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"; T1 có lan@demo.test (Active)
- Dữ liệu: Họ và tên = "Nguyễn Lan"; Email = "LAN@DEMO.TEST"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới "Email" hiện "Email đã tồn tại trong tổ chức."; không tạo người dùng; vẫn ở /users/new; T1 vẫn chỉ có một lan@demo.test
- Tag: @UC-DEMO-001 @function @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-F05 · Email đã có ở tenant khác vẫn tạo được
- Nhóm: Function
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: Bảng quyết định
- Nguồn: UC-DEMO-001-DT-01-R1, UC-DEMO-001-BR-01
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"; minh@demo.test chỉ tồn tại ở T2
- Dữ liệu: Họ và tên = "Hoàng Minh"; Email = "minh@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã gửi lời mời đến minh@demo.test."; T1 có dòng minh@demo.test Trạng thái "Đã mời"; người dùng minh@demo.test ở T2 không đổi
- Tag: @UC-DEMO-001 @function @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-F06 · Email của người dùng đã vô hiệu hóa không tạo mới
- Nhóm: Function
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: Bảng quyết định
- Nguồn: UC-DEMO-001-AF-01, UC-DEMO-001-DT-01-R5, UC-DEMO-001-BR-01, UC-DEMO-001-MS-08
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"; T1 có old.user@demo.test (Deactivated)
- Dữ liệu: Họ và tên = "Người Cũ"; Email = "old.user@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện hộp thông báo "Người dùng này đã bị vô hiệu hóa. Hãy kích hoạt lại thay vì tạo mới."; không tạo người dùng mới; old.user@demo.test vẫn ở trạng thái Deactivated
- Tag: @UC-DEMO-001 @function @negative @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-F07 · Dịch vụ email lỗi vẫn tạo người dùng và cảnh báo
- Nhóm: Function
- Loại: Abnormal
- Ưu tiên: P2
- Kỹ thuật: Kịch bản
- Nguồn: UC-DEMO-001-EF-01, UC-DEMO-001-MS-09
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"; mock email bật chế độ lỗi
- Dữ liệu: Họ và tên = "Đỗ Hà"; Email = "f07@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Đã tạo người dùng nhưng chưa gửi được email. Bạn có thể gửi lại lời mời sau."; danh sách có f07@demo.test Trạng thái "Đã mời"; hộp thư test không có email tới f07@demo.test
- Tag: @UC-DEMO-001 @function @abnormal @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-F08 · Mất kết nối khi gửi thì giữ dữ liệu và không tạo
- Nhóm: Function
- Loại: Abnormal
- Ưu tiên: P2
- Kỹ thuật: Kịch bản
- Nguồn: UC-DEMO-001-EF-02, UC-DEMO-001-MS-11
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Đỗ Hà"; Email = "f08@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Chặn request POST /api/users (mô phỏng mất mạng); 3) Bấm "Gửi lời mời"
- Mong đợi: Hiện toast "Không kết nối được máy chủ. Vui lòng thử lại."; "Họ và tên" và "Email" giữ nguyên giá trị đã nhập; GET /api/users?email=f08@demo.test (sau khi có mạng lại) trả danh sách rỗng
- Tag: @UC-DEMO-001 @function @abnormal @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-F09 · Member gọi API tạo người dùng bị từ chối
- Nhóm: Function
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: Phân quyền
- Nguồn: PM-USER-02
- Tiền điều kiện: Có token của member1@t1.demo.test (Member, T1) và của admin1@t1.demo.test
- Dữ liệu: body {"name": "Trần Minh", "email": "f09@demo.test", "role": "Member"}
- Bước: 1) Dùng token Member gửi POST /api/users với body ở cột Dữ liệu; 2) Dùng token Admin gửi GET /api/users?email=f09@demo.test
- Mong đợi: Bước 1 trả HTTP 403; bước 2 trả danh sách rỗng
- Tag: @UC-DEMO-001 @function @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-F10 · Admin tạo người dùng sang tenant khác qua API bị từ chối
- Nhóm: Function
- Loại: Negative
- Ưu tiên: P1
- Kỹ thuật: Phân quyền
- Nguồn: PM-USER-03
- Tiền điều kiện: Có token của admin1@t1.demo.test (T1) và admin1@t2.demo.test (T2)
- Dữ liệu: body {"name": "Trần Minh", "email": "f10@demo.test", "role": "Member", "tenantId": "T2"}
- Bước: 1) Dùng token Admin T1 gửi POST /api/users với body ở cột Dữ liệu; 2) Dùng token Admin T2 gửi GET /api/users?email=f10@demo.test
- Mong đợi: Bước 1 trả HTTP 403; bước 2 trả danh sách rỗng
- Tag: @UC-DEMO-001 @function @negative @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-F11 · Email mời được gửi tới đúng địa chỉ
- Nhóm: Function
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: Kịch bản
- Nguồn: UC-DEMO-001-SE-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"; hộp thư test trống
- Dữ liệu: Họ và tên = "Phạm Hoa"; Email = "f11@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"; 3) Đọc hộp thư test của f11@demo.test
- Mong đợi: Hộp thư f11@demo.test có đúng 1 email tiêu đề "Lời mời tham gia Demo"; nội dung có link kích hoạt
- Tag: @UC-DEMO-001 @function @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-F12 · Audit ghi sự kiện mời người dùng
- Nhóm: Function
- Loại: Positive
- Ưu tiên: P2
- Kỹ thuật: Kịch bản
- Nguồn: UC-DEMO-001-SE-03
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Phạm Hoa"; Email = "f12@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"; 3) Gửi GET /api/audit?target=f12@demo.test
- Mong đợi: Có đúng 1 bản ghi: action "user.invited", actor "admin1@t1.demo.test", target "f12@demo.test"
- Tag: @UC-DEMO-001 @function @positive @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-F13 · Bấm Gửi lời mời hai lần liên tiếp chỉ tạo một người dùng
- Nhóm: Function
- Loại: Abnormal
- Ưu tiên: P1
- Kỹ thuật: Đoán lỗi
- Nguồn: UC-DEMO-001-EG-01
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Phạm Hoa"; Email = "f13@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời" hai lần liên tiếp (double click)
- Mong đợi: Danh sách chỉ có 1 dòng f13@demo.test; hộp thư test chỉ có 1 email mời tới f13@demo.test
- Tag: @UC-DEMO-001 @function @abnormal @P1
- Tự động hóa: Có

#### UC-DEMO-001-TC-F14 · Bấm Back sau khi tạo không tạo thêm người dùng
- Nhóm: Function
- Loại: Abnormal
- Ưu tiên: P2
- Kỹ thuật: Đoán lỗi
- Nguồn: UC-DEMO-001-EG-02
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Phạm Hoa"; Email = "f14@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"; 3) Bấm Back của trình duyệt; 4) Mở /users
- Mong đợi: Không có request POST /api/users nào sau bước 3; danh sách chỉ có 1 dòng f14@demo.test
- Tag: @UC-DEMO-001 @function @abnormal @P2
- Tự động hóa: Có

#### UC-DEMO-001-TC-F15 · Hai Admin gửi cùng một email đồng thời thì chỉ một thành công
- Nhóm: Function
- Loại: Abnormal
- Ưu tiên: P2
- Kỹ thuật: Đoán lỗi
- Nguồn: UC-DEMO-001-EG-03, UC-DEMO-001-BR-01, UC-DEMO-001-MS-06
- Tiền điều kiện: Hai phiên: admin1@t1.demo.test và admin2@t1.demo.test, cả hai đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Phạm Hoa"; Email = "f15@demo.test"; Vai trò = Member
- Bước: 1) Cả hai nhập cùng dữ liệu; 2) Cả hai bấm "Gửi lời mời" cùng lúc
- Mong đợi: Đúng một phiên hiện toast "Đã gửi lời mời đến f15@demo.test."; phiên còn lại hiện "Email đã tồn tại trong tổ chức."; danh sách chỉ có 1 dòng f15@demo.test
- Tag: @UC-DEMO-001 @function @abnormal @P2
- Tự động hóa: Có — hai browser context chạy song song

#### UC-DEMO-001-TC-F16 · Hết phiên khi đang nhập thì không tạo và chuyển tới đăng nhập
- Nhóm: Function
- Loại: Abnormal
- Ưu tiên: P3
- Kỹ thuật: Đoán lỗi
- Nguồn: UC-DEMO-001-EG-04
- Tiền điều kiện: Đăng nhập admin1@t1.demo.test (Admin, tenant T1); đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "Phạm Hoa"; Email = "f16@demo.test"; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Làm hết phiên (xóa cookie phiên); 3) Bấm "Gửi lời mời"; 4) Đăng nhập lại và mở /users
- Mong đợi: Sau bước 3 URL là /login; sau bước 4 danh sách không có f16@demo.test
- Tag: @UC-DEMO-001 @function @abnormal @P3
- Tự động hóa: Có — mô phỏng bằng xóa cookie; trường hợp chờ đủ 30 phút chạy tay
