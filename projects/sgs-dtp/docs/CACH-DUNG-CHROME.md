# Cách để Sonnet vào Figma, SharePoint, prototype mà không phải đăng nhập lại

Ngày: 2026-10-09 · Viết bởi Opus theo yêu cầu của Hanna (09:00)

## Vì sao đang bị hỏi đăng nhập
Claude có hai trình duyệt, **sign-in của hai bên tách riêng**:
- **Trình duyệt trong app** (khung bên phải, tên công cụ `Claude_Browser`): hồ sơ riêng, ban đầu chưa đăng nhập gì. Dự án đang đặt đây là "Preferred browser" nên Sonnet mặc định mở trình duyệt này, và gặp màn đăng nhập Figma, SharePoint (login.microsoftonline.com), prototype.
- **Chrome thật của Hanna** (extension Claude in Chrome): dùng chính các sign-in của Hanna (Figma, SharePoint Microsoft 365, prototype nếu đã đăng nhập). Kiểm ngày 09/10 09:00: extension đang kết nối, "Browser 1", Windows, cùng máy.

Claude không nhập mật khẩu hộ Hanna, nên cách đúng là dùng Chrome đã đăng nhập sẵn.

## Việc của Hanna (làm một lần)
1. Mở **Chrome** trên máy này, mở extension Claude in Chrome, thấy trạng thái đã kết nối (đừng đóng Chrome khi Sonnet đang làm).
2. Trong Chrome, tự đăng nhập và mở được trang cần đọc, vd:
   - Figma: `figma.com/design/KM5Oc1DaB78FXOMimDyB0U/SGS-DTP-DS`
   - UC v4 trên SharePoint: link `lotuslts-my.sharepoint.com/:x:/g/personal/duyp_ltsgroup_tech/…`
   - Prototype: `sgs-dtp-ds-demo-prototype.vercel.app` (đăng nhập bằng tài khoản demo của Hanna, ở tab Chrome)
3. Trong extension, cho phép các site trên (site permissions) nếu extension hỏi.
4. Mở khung chat với Sonnet và **nhắn rõ**: "dùng Chrome" hoặc "dùng Chrome của tôi (extension), không dùng trình duyệt trong app". Đây là yêu cầu đích danh nên Claude dùng Chrome dù Preferred browser đang là trình duyệt trong app.
   - Muốn khỏi nhắc mỗi lần: đổi **Preferred browser** sang Chrome trong Settings của app Claude.
5. Không gửi mật khẩu vào chat. Nếu Chrome hỏi đăng nhập lại, Hanna tự đăng nhập trong Chrome rồi báo Sonnet làm tiếp.

## Các bước Sonnet làm
1. Đọc skill `chrome-browser` (nếu có trong danh sách skill) trước bước đầu tiên.
2. Tải công cụ Chrome **một lần**: ToolSearch `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp`.
3. Gọi `tabs_context_mcp` trước mọi thao tác. Nếu báo có nhiều Chrome mà chưa chọn: gọi `list_connected_browsers`, hỏi Hanna chọn (AskUserQuestion), rồi `select_browser`. Không tự chọn.
4. Mở **tab mới** (`tabs_create_mcp`), không dùng lại tab cũ trừ khi Hanna bảo. Vào từng nguồn bằng `navigate`.
5. Đọc bằng `get_page_text` hoặc `read_page`; dùng ảnh chụp khi cần xem bố cục (Figma). Figma: chọn frame rồi zoom (Shift+2), ẩn bảng bằng Ctrl+\ nếu cần; cửa sổ Chrome rộng hơn khung trong app nên đọc được cả frame 1440 px.
6. SharePoint Excel Online: đọc sheet `P1 Use Cases` hoặc sheet nói tới; chỉ tải file về khi Hanna đồng ý (nêu tên file, nguồn, dung lượng). Không sửa file trên SharePoint.
7. Nếu gặp màn đăng nhập hoặc xác minh: **dừng, báo Hanna tự đăng nhập trong Chrome**, rồi tiếp tục. Không nhập tài khoản, mật khẩu, mã OTP.
8. Không bấm nút xác nhận trên prototype (Check file với file hợp lệ, Activate, Discard, Import new version, Create workspace nếu có) và không đổi vai trò ở thanh Demo trừ khi Hanna yêu cầu (FB-018).
9. Tránh hộp thoại alert/confirm của trình duyệt (chặn extension). Gặp lỗi công cụ 2–3 lần thì dừng và hỏi Hanna, không thử lại mãi.
10. Cuối việc: ghi điều đã đọc vào `tests/design/`, nêu nguồn từng điều (dòng UC, frame Figma, màn prototype).

## Nếu vẫn bị hỏi đăng nhập
| Dấu hiệu | Nguyên nhân | Cách xử lý |
|---|---|---|
| Công cụ tên `Claude_Browser__…` | Sonnet vẫn đang dùng trình duyệt trong app | Nhắn "dùng Chrome", hoặc đổi Preferred browser |
| `list_connected_browsers` trả danh sách rỗng | Chrome chưa mở hoặc extension chưa đăng nhập tài khoản Claude | Mở Chrome, bật extension, đăng nhập đúng tài khoản Claude |
| Chrome hỏi đăng nhập Figma, Microsoft | Chrome của Hanna chưa đăng nhập site đó | Hanna đăng nhập một lần trong Chrome |
| "site isn't allowed" | Extension chặn site | Hanna cho phép site trong extension |
| Cùng một nội dung đòi đăng nhập ở tab mới | Đăng nhập ở cửa sổ ẩn danh hoặc hồ sơ Chrome khác | Đăng nhập trong cùng hồ sơ Chrome mà extension đang gắn |
