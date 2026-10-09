---
name: impact
description: Xử lý thay đổi sau khi đã có baseline — tài liệu mới, UC/BR bị sửa, câu hỏi vừa được trả lời — và tìm test case, spec bị ảnh hưởng. Dùng khi docs/ba hoặc docs/source đổi, hoặc khi được hỏi "cái này đổi thì ảnh hưởng gì".
---
# Xử lý thay đổi và phân tích ảnh hưởng
Phần cập nhật baseline BA làm theo skill `ba-change-handling`; skill này lo phần ảnh hưởng tới test case và spec.
1. **Đối chiếu với đoạn mục đích sản phẩm hiện có:** tài liệu mới xác nhận, bổ sung hay mâu thuẫn. Ghi rõ, không sửa âm thầm.
2. **Phân loại** thay đổi: câu hỏi cũ đã có lời giải / vẫn mở / thông tin hoàn toàn mới / phát hiện cũ đang được xử lý hay bị chặn.
3. **So trước/sau:** `git diff` trên `docs/ba/` và `docs/questions.md` để biết chính xác ID nào đổi. Không viết lại từ đầu.
4. **Truy vết ảnh hưởng:** tìm theo mã UC, bước (MF/AF/EF), BR, `Blocked-by` trong `testcases/`; tag `@UC03`, `@BR-12` và comment BR trong `automation/tests/`. Đọc lại từng kết quả rồi phân loại:
   - **Đã cũ** — TC/spec assert theo nội dung cũ → sửa.
   - **Chưa có** — BR/luồng mới → viết mới.
   - **Hết bị chặn** — câu hỏi đã có trả lời → bỏ blocked/fixme, điền Expected.
   - **Không ảnh hưởng** — ghi lại để biết đã kiểm.
5. **Phạm vi regression** và **câu hỏi mới** phát sinh.
6. **[DỪNG]** trình danh sách cho con người duyệt.
7. **Baseline v1.x + changelog.** TC bị sửa quay về `draft`.
