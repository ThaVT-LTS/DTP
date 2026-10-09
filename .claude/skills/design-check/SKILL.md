---
name: design-check
description: Đối chiếu bản thiết kế (Figma, mockup, ảnh màn hình) với baseline yêu cầu. Dùng sau bước phân tích BA và trước khi xuất test basis, hoặc khi có bản thiết kế mới.
---
# Check design (v0.1 — [ĐỀ XUẤT], chờ duyệt)
Tuân thủ `rules/common.md` (rule 9: tài liệu yêu cầu > bản thiết kế đã duyệt > hệ thống đang chạy) và `rules/ba.md`.

1. Trích bản thiết kế theo `ba-analysis` bước 0 mục 6: từng màn, phần tử bấm được, trạng thái, text nguyên văn.
2. Đối chiếu hai chiều với inventory/baseline: phần tử yêu cầu chưa thấy trên thiết kế; phần tử trên thiết kế không có yêu cầu nào.
3. Ghi `docs/design-review/<màn hoặc UC>.md`: bảng khớp / lệch kèm nguồn (tên frame, ảnh).
4. Mỗi điểm lệch thành câu hỏi trong `questions.md`, đúng mức CHẶN / QUAN TRỌNG / NHỎ. Không tự chọn bên nào đúng.
