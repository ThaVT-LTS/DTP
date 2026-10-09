---
name: manual-run
description: Chạy test case manual trên trình duyệt thật và ghi log vòng chạy. Dùng khi được yêu cầu chạy TC manual cho một UC, một tag hoặc một vòng test (Round N).
---
# Chạy manual (v0.1 — [ĐỀ XUẤT], chờ duyệt)
Tuân thủ `rules/common.md`, `rules/feedback.md`, `rules/automation.md`. Ứng với việc số 5 `test-execution` trong `docs/tester-skill-map.md`; định nghĩa trạng thái Pending / Blocked / NA còn chờ chốt (FB-008).

1. Xác nhận với người dùng: môi trường, URL, tài khoản theo vai trò, vòng chạy, phạm vi (tag hoặc danh sách TC).
2. Chỉ chạy TC của bộ test đã qua cổng 3. Đọc TC từ `tests/cases/*.md`.
3. Với mỗi TC: chuẩn bị theo `Tiền điều kiện`, thao tác từng bước trên trình duyệt, chụp màn hình ở mỗi ý của `Mong đợi`.
4. Ghi `runs/<ngày>-round<N>.md`: ID TC, kết quả, thực tế quan sát được, đường dẫn ảnh. Trạng thái không phải Passed phải có lý do.
5. Fail → **không tự ghi bug.** Trình người dùng: bước, mong đợi, thực tế, ảnh. Người dùng quyết: bug, TC sai, hay yêu cầu đổi.
6. TC `Tự động hóa: Không` vì chỉ kiểm được bằng mắt → chụp ảnh, để người dùng kết luận.
7. Không sửa TC trong lúc chạy vòng; đề xuất sửa ghi ở cuối log và thành FB nếu là vấn đề cách làm.
