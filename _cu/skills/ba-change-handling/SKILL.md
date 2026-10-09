---
name: ba-change-handling
description: Xử lý khi có thông tin mới trên một UC đã có baseline — UC version mới, câu trả lời cho câu hỏi cũ, biên bản họp, hoặc bug cho thấy hệ thống chạy khác UC. Dùng khi người dùng nói "UC này vừa đổi", "SGS/khách vừa trả lời câu hỏi", "cập nhật lại UC theo bản mới". Chỉ dùng sau khi skill ba-analysis đã chốt baseline v1.0 cho UC đó — không dùng cho UC chưa từng phân tích.
license: Proprietary — nội bộ dự án
---

# Xử lý thay đổi (BA)

**Điều kiện tiên quyết:** UC đã có baseline có version, lưu file trong repo (sản phẩm của skill `ba-analysis`). Nếu chỉ có cách hiểu ban đầu nằm trong lịch sử chat, không có gì để so sánh — phải có bản gốc đã lưu file thì mới đối chiếu trước/sau được đúng.

## Quy trình

1. **Phân loại thay đổi** — thêm / sửa / xóa, ở ID nào.
2. **So sánh trước/sau** ở mức từng bước, đối chiếu với baseline đã lưu (không dựa vào trí nhớ của cuộc hội thoại).
3. **Truy vết ảnh hưởng**: bước UC → business rule liên quan → UC khác có phụ thuộc → test case → file spec.
4. **Đề xuất phạm vi regression** — những gì cần chạy lại test, không chỉ những gì vừa đổi.
5. **Liệt kê câu hỏi mới phát sinh**, dùng cùng thang mức CHẶN / QUAN TRỌNG / NHỎ như skill `ba-analysis`.
6. **[DỪNG] chờ duyệt** — câu CHẶN chưa trả lời thì chưa lên version mới.
7. **Lên baseline v1.1 kèm changelog** — ghi rõ thay đổi gì, do ai xác nhận, ngày nào.

## Gắn tag để truy vết tới code

Gắn ID vào test Playwright bằng tag, để khi UC đổi có thể tìm đúng test bị ảnh hưởng thay vì đoán:

```ts
test('Đăng nhập sai mật khẩu', { tag: ['@UC03', '@BR-12'] }, async ({ page }) => {
  // ...
});
```

Chạy đúng phần bị ảnh hưởng: `npx playwright test --grep @UC03`.

## Liên quan

Rule chung (`.claude/rules/ba.md`) và checklist làm rõ (`../ba-analysis/references/checklist-lam-ro.md`) vẫn áp dụng nguyên vẹn ở đây — skill này chỉ thêm bước so sánh/truy vết, không thay thế các quy tắc đó.
