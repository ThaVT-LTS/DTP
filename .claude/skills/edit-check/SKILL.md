---
name: edit-check
description: Kiểm mọi form sửa (Edit drawer / dialog / trang) trên web test — mở lại sau Save không F5 có hiện giá trị cũ không, Save lần hai có ghi đè không, giới hạn ký tự web so với API, ô giá trị cố định gõ tay bị bỏ âm thầm, ô đã lưu có hiện ở màn người xem không, trạng thái bật theo điều kiện (Publish…). Dùng khi viết / chạy case cho một màn có Edit, khi có build mới đụng form, hoặc khi người dùng thấy "sửa rồi mà mở lại vẫn cũ".
---
# Kiểm form sửa (v0.1 — [ĐỀ XUẤT], chờ duyệt)

Tuân thủ rule 51 của `rules/tc-authoring.md`, mẫu lỗi 19–23 của `rules/bug-patterns.md`, rule 50 (nút khoá khi thiếu dữ liệu là đúng).

Nguồn gốc: 03/11 QA lead sửa profile Chen Wei (SGS Portal › Marketplace): Save xong mở lại hộp vẫn tên cũ, phải F5; Languages gõ "En" bị bỏ âm thầm; Publish phải Save + F5 + Save → MK-BUG-04. Giới hạn ký tự lệch → MK-BUG-05. QA đã kết luận "không cần F5" chỉ từ code — sai; **luôn chạy trên web trước khi kết luận** (rule bug verdict).

## 1. Lập danh sách form

- Đọc đúng commit đang deploy (`git show <commit>:<file>`, build từ `tests/tools/pw/portainer-ps.js`), không sửa repo app.
- Liệt kê mọi form sửa trong `apps/web/src/features/**`: tên, màn, URL, component. Với mỗi form ghi **cách lấy giá trị ban đầu** và **có reset khi bản ghi đổi không**:
  - mở mới mỗi lần (unmount khi đóng / `key` đổi theo `version`) → thường không lỗi;
  - dùng lại component, `key` chỉ theo `id`, form `reset()` không tham số khi đóng (SGS DTP: `components/templates/drawer-form.tsx:125-128`) → **nghi lỗi giá trị cũ**.
- Ghi giới hạn từng ô ở form web (zod `max`) và ở schema API (`packages/api-contracts`). Lệch là nghi lỗi.

## 2. Chạy trên web (dữ liệu [QA] của mình)

Không sửa dữ liệu seed / của người khác / workspace của QA lead; không publish, ẩn, gửi gì nếu case không cần. Mỗi form:

| # | Bước | Đạt khi |
|---|---|---|
| E1 | Sửa 1 ô chữ + 1 ô chọn, Save, **mở lại cùng dòng không F5** | Mọi ô = API (đọc API bằng `fetch` trong trang) |
| E2 | F5, mở lại | Mọi ô = API |
| E3 | Mở lại, Save không sửa gì | API không quay về giá trị trước lần Save ở E1 |
| E4 | Mỗi ô chữ: gõ đúng giới hạn, rồi +1 | Đúng giới hạn lưu được; +1 bị chặn trên form có câu báo; giới hạn web = API = mức chốt (SGS DTP 03/11: ô lý do, Public name, Based in, About 250; Headline 160) |
| E5 | Ô có tập giá trị cố định | Là dropdown. Nếu ô chữ: gõ sai hoa thường / tên đầy đủ, Save, đọc API — bỏ âm thầm là bug |
| E6 | Mỗi ô có giá trị: mở màn người kia xem (portal còn lại, danh sách, chi tiết) | Giá trị hiện, hoặc UC nói rõ không hiện |
| E7 | Trạng thái theo điều kiện (Publish, Active…): thiếu từng điều kiện một (đọc `publishChecklist` / `allowedActions`) | Câu báo nêu đúng mục thiếu; ô không bắt buộc vẫn Save được khi trống |
| E8 | Điền đủ điều kiện trong form, tick trạng thái, Save **một lần** | Trạng thái mới ngay trên danh sách, không F5 |

Chụp ảnh chỉ khi lỗi (1–2 ảnh, có URL), API trả gì ghi vào remark.

## 3. Ra kết quả

- Bảng: màn · URL · form · E1–E8 (Đạt / Lỗi / chỉ code) · bằng chứng.
- Lỗi cùng nguyên nhân (cùng component dùng chung) → **một bug**, liệt kê mọi form bị ảnh hưởng; hỏi QA lead trước khi gộp vào bug đã có.
- Thêm case vào TC theo rule 51 cho mỗi form; Expected viết theo quyết định QA lead, có ảnh mock-up khi Expected là giao diện mới.
- Kết luận "không lỗi" chỉ khi đã chạy E1–E3 trên web; chỉ đọc code thì ghi "nghi, chưa chạy".
