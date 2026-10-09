# Bản đồ skill cho vai trò Tester — [ĐỀ XUẤT], chờ duyệt

Ngày: 2026-09-29 · Nguồn suy luận: bộ rule/skill hiện có + rà file `FEEC_PM_IT_Test_Case.xlsx` (429 TC, 3 sheet, 2 vòng test).

Hiện bộ skill chỉ phủ **một** trong mười việc của tester: thiết kế. Bảy việc còn lại đang làm bằng tay và không có gate nào — đó là lý do các lỗi ở `feedback/log.md` (FB-002 → FB-009) lặp đều trên cả ba sheet.

## Mười việc của một tester và skill tương ứng

| # | Việc | Skill | Trạng thái | Ưu tiên |
|---|---|---|---|---|
| 1 | Đọc spec, biết mình **thiếu thông tin gì** để test | `test-basis-review` | Một phần trong `ba-analysis` | 2 |
| 2 | Biến yêu cầu thành **tập giá trị phải thử** | `test-design` | Có, v0.1 | — |
| 3 | Viết TC **đúng định dạng** khách hàng dùng | `tc-authoring` | Chưa có | **1** |
| 4 | Chuẩn bị **dữ liệu và môi trường** | `test-data` | Chưa có | 3 |
| 5 | **Chạy** một vòng test và ghi kết quả | `test-execution` | Chưa có | **1** |
| 6 | **Báo lỗi** để dev sửa được ngay lần đầu | `bug-reporting` | Chưa có | **1** |
| 7 | **Báo cáo** vòng test, quyết định dừng hay chạy tiếp | `test-report` | Chưa có | 2 |
| 8 | Chọn **bộ chạy lại** sau khi fix | `regression-selection` | Chưa có | 2 |
| 9 | Test vùng **spec mỏng** một cách có kỷ luật | `exploratory-charter` | Chưa có | 3 |
| 10 | Bàn giao cho **Playwright** | `automation-handoff` | Chưa có | 2 |
| — | Học từ nhận xét và bug lọt | `feedback-loop` | Có, v0.1 | — |

## Nhóm 1 — làm trước

### `tc-authoring` — viết TC đúng định dạng đang dùng
Vì sao trước tiên: skill `test-design` hiện xuất TC dạng Markdown theo khung Redirect/Validation/Function, còn file thật là Excel với `Classification I–IV`, `TVP_ID`, `Priority`, `Pre-condition`, `Step`, `Expected result`, `Dev test`, và một khối cột cho mỗi vòng test. Hai định dạng không nối được với nhau, nên mọi gate của `test-design` không chạm được tới file thật.

Nội dung: ánh xạ R/V/F ↔ Classification I/II; quy ước `TVP_ID` duy nhất toàn dự án (FB-003); cột `Nguồn` trỏ ID spec để đo được độ phủ (FB-004); khi nào bắt buộc `Pre-condition` (FB-002); định nghĩa ba mức `Priority` (FB-006); một `Step` một hành động.

Script: `tc_check_xlsx.py` — đọc thẳng `.xlsx`, bắt trường rỗng, ID trùng, TC không trỏ spec, kết quả mong đợi mơ hồ, nhóm khai báo mà 0 TC (FB-007). Đây là cái nâng FB-002…FB-007 lên **gate mức 3**.

### `test-execution` — chạy một vòng test
Định nghĩa dứt khoát `Passed / Failed / Pending / Blocked / NA / Not execute`, mỗi trạng thái không-Passed phải có lý do; điều kiện mở và đóng một vòng; evidence lưu ở đâu và tồn tại bao lâu (file thật đang dùng link `prnt.sc` — ảnh ngoài, sẽ mất); không sửa TC khi đang chạy vòng; cách ghi khối cột của Round 2.
Bằng chứng cần skill này: Round 1 còn 41 Pending + 22 NA ở PM-L0001 và 73 Pending + 32 Failed ở DM-L0001; Round 2 đánh 191/254 TC là NA mà không nêu lý do (FB-008).

### `bug-reporting` — báo lỗi
Tiêu đề một dòng nói được triệu chứng; bước tái hiện tối thiểu; kết quả mong đợi trích nguyên văn spec; phân biệt Severity và Priority; evidence; chống trùng; vòng retest → Closed/Reopen; `Bug_ID` có định dạng cố định và nối được với nơi quản lý bug (FB-005: hiện lưu `6.0`, `14.0`, `11, 34 `).

## Nhóm 2 — làm sau khi nhóm 1 chạy ổn

- **`test-report`**: tự tính lại mọi con số từ dữ liệu TC rồi sinh sheet báo cáo, thay cho công thức Excel (sheet `Test_Report` đang hiện `#DIV/0!` ở nhóm có 0 TC); kèm tiêu chí kết thúc và rủi ro còn lại.
- **`regression-selection`**: chọn bộ chạy lại = TC của bug đã fix + TC cùng chức năng mức P1 + bộ smoke + TC quanh vùng code thay đổi. Hiện Round 2 chạy lại toàn bộ 254 TC rồi bỏ NA 191 — tốn công mà không nói được đã phủ lại cái gì.
- **`automation-handoff`**: đánh dấu TC nào tự động hoá được, lấy locator từ nhãn giao diện nguyên văn, đặt tag `@UC-ID @nhóm @Pn` cho Playwright. Đây là chỗ nối sang vai trò Code.
- **`test-basis-review`**: checklist tester dùng để soát spec trước khi nhận việc, và mẫu câu hỏi `Q-T-nn` có ID, mức độ, người nhận, trạng thái (FB-009: 9 câu hỏi về giới hạn ký tự đang nằm rời ở sheet `Tổng hợp`).

## Nhóm 3 — khi dự án cần

- **`test-data`**: bộ dữ liệu master, tài khoản theo vai trò, dữ liệu biên dựng sẵn, dọn dữ liệu sau khi chạy, không dùng dữ liệu thật.
- **`exploratory-charter`**: phiên có mục tiêu, thời hạn, ghi chú — dùng đúng cho những chỗ spec không nói (giới hạn ký tự, số dòng tối đa).
- Kiểm thử phi chức năng (hiệu năng, bảo mật, khả năng truy cập): chỉ dựng khi dự án đưa vào phạm vi, vì mỗi loại là một bộ kỹ thuật riêng.

## Thứ tự đề nghị

1. `tc-authoring` + script kiểm file Excel → có gate cho FB-002…FB-007.
2. `test-execution` và `bug-reporting` → hai việc tester làm hằng ngày, hiện không có quy tắc nào.
3. `test-report` + `regression-selection` → đóng vòng một đợt test.
4. `automation-handoff` → mở đường sang Playwright.
