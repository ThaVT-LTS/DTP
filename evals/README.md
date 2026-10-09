# Bộ bài kiểm cho rule/skill
Mục đích: biết rule và skill còn chạy đúng không mỗi khi **đổi model** hoặc **sửa rule/skill**.

## Cách dựng
Mỗi bài một thư mục `evals/<NN-tên>/`:
- `input/` — tài liệu UC đầu vào (lấy từ UC thật đã làm xong, đã ẩn thông tin nhạy cảm).
- `expected.md` — đáp án do con người chốt: danh sách BR, danh sách mục tiêu TC bắt buộc phải có, các câu hỏi phải được nêu.
- `prompt.md` — câu lệnh cố định giao cho Claude.

Nên có 10–20 bài, gồm cả UC đơn giản, UC nhiều BR, UC thiếu thông tin (đáp án đúng là "hỏi lại"), UC có mâu thuẫn giữa các nguồn.

## Cách chấm
Chạy từng bài trong phiên mới. So với `expected.md`: BR lọt, TC bắt buộc lọt, câu hỏi không được nêu, chỗ tự đoán. Ghi kết quả vào `evals/results.md`:

| Ngày | Model | Phiên bản rule (git commit) | Đạt/Tổng | Bài trượt và lý do |
|---|---|---|---|---|

Điểm giảm so với lần trước thì không dùng rule/model mới cho dự án thật cho tới khi tìm ra nguyên nhân.
