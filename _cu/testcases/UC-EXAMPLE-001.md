# Test case — UC-EXAMPLE-001

## EX-TC-001: Đăng nhập thành công với tài khoản hợp lệ
- UC: UC-EXAMPLE-001
- BR: BR-EXAMPLE-001-01
- Flow: main
- Type: Positive
- Technique: EP
- Priority: High
- Automation: Auto-UI
- Tags: smoke
- Status: draft
- Pre-condition: Bộ dữ liệu `seed-basic`; tài khoản {{user.admin}} đang hoạt động
- Test data: email = {{user.admin}}, password = {{pass.admin}}
### Steps
1. Mở trang đăng nhập
2. Nhập email và mật khẩu, bấm "Login"
### Expected
1. Hiển thị form đăng nhập
2. Chuyển tới trang Dashboard

## EX-TC-002: Thông báo khi sai mật khẩu
- UC: UC-EXAMPLE-001
- BR: BR-EXAMPLE-001-02
- Flow: E1
- Type: Negative
- Technique: EP
- Priority: High
- Automation: Auto-UI
- Tags: regression
- Status: blocked
- Blocked-by: Q-001
- Pre-condition: Bộ dữ liệu `seed-basic`
- Test data: email = {{user.admin}}, password = sai
### Steps
1. Mở trang đăng nhập
2. Nhập mật khẩu sai, bấm "Login"
### Expected
