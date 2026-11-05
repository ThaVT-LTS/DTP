---
name: figma-ui-update
description: So UC hiện hành với Figma và sửa màn trên Figma theo UC / ảnh màn mẫu, từng màn một, chờ QA lead duyệt. Dùng khi được yêu cầu "so UC với Figma", "sửa màn X trên Figma theo hình", "cập nhật Figma theo UC".
---
# So UC ↔ Figma và sửa màn trên Figma (v0.1 — [ĐỀ XUẤT], chờ duyệt · FB-128)
Tuân thủ `rules/common.md`, `rules/automation.md` (rule 53, 54, 57). Cần Figma MCP; trước mỗi `use_figma` đọc skill `figma-use` (sửa giao diện: thêm `figma-generate-design`).

## Tài khoản và quyền
- `whoami` trước: phải có ghế **Full / Dev trên plan của file**. Ghế View: không sửa được và chỉ ~6 lượt gọi / tháng → báo người dùng đổi tài khoản kết nối (claude.ai → Settings → Connectors → Figma → Disconnect / Connect, đăng nhập đúng tài khoản trên trình duyệt trước). Không nhập mật khẩu hộ.
- Đổi tài khoản → `sessionId` cũ hết hiệu lực, gọi `create_session` lại.

## So UC ↔ Figma (chỉ đọc)
1. Dump UC (`P1 Use Cases`, `Decision log`) ra text.
2. Mỗi trang Figma 1 lệnh `use_figma` chạy song song: tên frame + chữ mới của frame (bỏ chữ đã gặp ở frame trước). Frame đặt tên theo mã UC (vd "SCP-01 Scope list") → map trực tiếp.
3. Báo theo 3 nhóm: lệch quy tắc (nặng, kèm mã D / UC) · UC có mà Figma chưa có màn · lệch tên gọi. Ghi trang prototype dựa trên bản UC nào.

## Sửa màn
- **Không sửa trang của designer.** Vẽ trên trang riêng `◆ QA · UC v6.5 updates` (đổi số phiên bản UC); nhân bản frame gần nhất (ưu tiên prototype mới nhất) rồi sửa, giữ component / màu của bộ design.
- **Mỗi lần một màn**, xong báo link frame + danh sách đã sửa + đối chiếu UC (khớp / cần quyết / còn lệch), chờ QA lead "ok" mới sang màn sau. Điểm ảnh mẫu trái UC → hỏi, không tự sửa.
- Script lỗi thì Figma tự hoàn tác toàn bộ lệnh đó → kiểm canvas một lần rồi chạy lại.
- **QA lead thích giao diện có màu** ("màu mè hơn đi", 05/11): mỗi card / khối một màu nhấn — icon đặt trong ô bo góc 36px nền nhạt cùng tông, số lớn tô màu nhấn, viền trên card 4px màu nhấn. Màu dùng trên Home: Reviews cam #E8590C, Workspaces xanh dương #1C6ED8, Documents tím #7048E8, Service Requests xanh ngọc #0C8599, Bulk chàm #3B5BDB, Trust Centre xanh lá #2B8A3E. Màn sau dùng lại đúng màu của khối tương ứng.
- **Dựng lại theo web** (QA lead 05/11: "trên web đang có tốt hơn thì ít nhất nên giữ lại"): đọc web bằng Playwright (mọi vai trò, mở cả bộ lọc / modal / drawer) trước khi vẽ. Giữ **mọi điều khiển web đang có** — ô tìm kiếm, lọc theo cột (vẽ thêm 1 frame trạng thái đang mở bộ lọc), sắp xếp, phân trang — trừ khi UC cấm. Kết hợp UC + bug đã Verified (ghi mã bug vào note).
- **Hiện đủ nội dung**: frame không cắt nội dung (nới chiều cao frame theo nội dung, không để 900px cố định); bảng / danh sách có data mẫu đủ dày (≈ 8–9 dòng, đủ loại, có dòng dài để thấy "…"); xếp theo đúng quy tắc sort của web.
- **Bố cục trang**: mỗi module một khối có tiêu đề; trong khối chia hàng theo vai trò (Admin hàng trên, vai trò chỉ xem hàng dưới; SGS Portal xuống dưới Customer Portal); note vàng (tiếng Anh, vì SGS cũng xem file) đặt trên đầu khối / frame.
- **Tiêu chí "đẹp" của QA lead (05/11)**:
  - Menu trái mọi frame (cả SGS Portal) là **dải trắng kéo hết chiều cao frame**; chữ / icon menu màu tối, mục đang chọn giữ nền màu. Đổi nền thì kiểm lại màu chữ (05/11 lỡ để chữ trắng trên nền trắng ở menu SGS).
  - **Data dài, đủ trạng thái**: mỗi vai trò có danh sách dài (Admin ≈ 9–12 dòng; vai trò chỉ xem cũng ≥ 7 dòng, mỗi vai trò chỉ xem một frame riêng, vd Customer User và Customer Viewer tách 2 frame); bảng con (vd Workspaces trong chi tiết scope) đủ mọi trạng thái của UC (In progress, Not started, Archived, Deleted…), có dòng Bulk.
  - **Hai cột cân nhau**: trang chi tiết 2 cột — cột ngắn kéo dài (card cuối `layoutGrow = 1`) để thấy hết card cột kia, không bị cắt.
  - Tên đối tượng mở được (scope, workspace, số chứng chỉ) tô cam như link; tag trạng thái dùng đúng màu (Valid xanh, Expires vàng, Expired / Deleted đỏ, Not started viền đứt).
  - Data mẫu phải nhất quán giữa các khối (cùng tổ chức, cùng tên scope / số chứng chỉ; khách chỉ thấy dữ liệu của tổ chức mình).
  - Nền mờ sau modal / drawer dùng đúng màn mới (thay Body cũ của designer), quyền theo vai trò (khách: chỉ xem / tải file, không icon sửa / xoá).
  - Web có mà Figma chưa có / web chưa có mà nên có (vd bấm dòng chứng chỉ trong chi tiết scope mở panel) → vẽ và ghi "Design proposal (not on web yet)" trong note.
- **Phạm vi thread vẽ Figma**: chỉ dựng giao diện; không retest bug, không đổi ticket (bên khác làm). Lỗi web thấy khi đọc → ghi trong note / báo người dùng, không tự log.
- **Kiểm trước khi báo (bắt buộc)**:
  - Tag, nút, chip, badge: `layoutSizingHorizontal = 'HUG'`, chữ bên trong `textAutoResize = 'WIDTH_AND_HEIGHT'` → nền luôn bao hết chữ (05/11: tag "Expires in 47 days", "In progress", "Submitted" bị chữ tràn khỏi nền vì component gốc rộng cố định 80px).
  - Script đo: chữ tràn khỏi khung cha, phần tử con trong cùng một hàng đè nhau → phải ra 0.
  - Đổi bố cục (vd card thành 2 cột): tính bề rộng từ khung cha sau khi FILL, không dùng bề rộng cũ.
  - Chụp lại khu vực vừa sửa và tự xem trước khi gửi.
- Ghi tiến độ vào `tasks/handoff/` (rule 56).

## Changelog
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-11-05 | Khởi tạo từ lần so UC v6.5 ↔ DTP-P1 và sửa màn Home. **Chờ duyệt.** | FB-128 |
