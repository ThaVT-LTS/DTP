---
name: coverage-review
description: Soát độc lập xem bộ test case có lọt case không. Dùng sau khi viết xong TC, trước khi con người duyệt.
---
# Soát độ phủ
Giao cho agent `coverage-reviewer` (không dùng chính phiên vừa viết TC). Chỉ đưa cho agent: `docs/ba/`, `docs/design-review/`, `docs/questions.md`, `testcases/`. Không đưa lời giải thích của người viết.
Kết quả ghi `coverage/review-<ngày>.md`:
- Chỗ hổng theo từng UC (luồng, BR, biên, quyền, abnormal, API).
- TC có vấn đề (nhiều mục tiêu, Expected mơ hồ, phụ thuộc TC khác).
- TC đề xuất thêm, viết sẵn đúng định dạng, `Status: draft`.
Không tự thêm TC đề xuất vào bộ chính. Con người duyệt rồi mới thêm.
