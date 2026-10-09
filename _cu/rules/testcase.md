---
paths:
  - "projects/*/testcases/**"
  - "projects/*/coverage/**"
---
# Rule test case
## Định dạng (bắt buộc, script kiểm)
Mỗi UC một file `testcases/<UC-ID>.md`. Mỗi TC:

    ## <MÃ-TC>: <tên TC — một mục tiêu>
    - UC: <UC-ID>
    - BR: <BR-…>[, <BR-…>]      (ghi `-` nếu TC không gắn BR nào, ví dụ kiểm giao diện)
    - Flow: main | A1 | E1 …
    - Type: Positive | Negative | Abnormal
    - Technique: EP | BVA | DecisionTable | StateTransition | Permission | ErrorGuessing | UI
    - Priority: High | Medium | Low
    - Automation: Auto-UI | Auto-API | Manual
    - Tags: smoke, regression …
    - Status: draft | reviewed | approved | blocked
    - Blocked-by: Q-…            (bắt buộc khi Status = blocked)
    - Pre-condition: …           (trỏ tới bộ dữ liệu có tên, không trỏ tới TC khác)
    - Test data: …               (dùng placeholder `{{…}}` trong profile.md)
    ### Steps
    1. …
    ### Expected
    1. …                          (đánh số khớp với bước; text UI ghi nguyên văn)

## Thiết kế để không lọt case
Với mỗi UC, đi lần lượt và ghi vào `coverage/matrix.md`:
1. Luồng chính → ít nhất 1 TC Positive.
2. Mỗi nhánh rẽ/ngoại lệ → ít nhất 1 TC.
3. Mỗi BR → ít nhất 1 TC; BR có điều kiện → cả nhánh đúng và sai.
4. Mỗi trường nhập → phân vùng tương đương + giá trị biên (độ dài, định dạng, bắt buộc, ký tự đặc biệt, ngôn ngữ của thị trường).
5. Nhiều điều kiện kết hợp → bảng quyết định.
6. Đối tượng có trạng thái → chuyển trạng thái hợp lệ và không hợp lệ.
7. Phân quyền → mỗi vai trò × mỗi hành động, kể cả gọi thẳng API bỏ qua UI.
8. Abnormal → bấm hai lần, mất mạng, hết phiên, back/refresh, mở hai tab.
9. Điều hướng (redirect) và hiển thị theo design.
Mục nào không áp dụng thì ghi "N/A — lý do" trong matrix, không bỏ trống.

## Khác
- Kết quả chạy không ghi vào file TC; ghi vào `runs/`.
- Mã TC ổn định, không đổi khi sửa nội dung; không tái dùng mã đã xoá.
