# Rule — Vòng phản hồi và bộ nhớ (feedback loop)

Phiên bản: v0.2 · **Luôn nạp**, cùng `rules/common.md`. Quy trình chi tiết: skill `feedback-loop`. Sổ ghi nhớ: `feedback/log.md`.

Rule này biến mỗi nhận xét của người dùng thành một bản ghi có ID, có địa chỉ sửa, có cách kiểm và có version — để cùng một lỗi không bị nhắc lần thứ hai.

## A. Ghi nhận

1. **Mỗi nhận xét = một bản ghi `FB-nnn`** trong `feedback/log.md`, ghi **trước khi sửa** bất cứ thứ gì. Trích nguyên văn câu của người dùng vào trường `Nguồn`, không diễn giải lại. Nhận xét không được ghi thì coi như chưa nhận.
2. Một câu nói chứa nhiều ý → tách thành nhiều FB, mỗi FB một ý có thể kiểm riêng. Một ý nhắc lại ở nhiều thời điểm → cùng một FB, tăng trường `Tái phát`.
3. Nhận xét mơ hồ ("chưa ổn", "phần này viết lại") → hỏi lại **đúng một câu** để lấy tiêu chí kiểm được, rồi mới ghi FB. Không tự suy ra ý người dùng rồi ghi thành rule.
4. Không sửa, không xoá bản ghi cũ. Thay đổi nhận định thì thêm dòng `- Cập nhật: <ngày> · <nội dung>`.

## B. Xếp loại và định vị

5. Mỗi FB phải có `Loại` (L1–L7 theo `references/classification.md` của skill) và `Địa chỉ` — nơi sẽ sửa, ghi cụ thể:
   - rule: `rules/tester.md#7`
   - skill: `skills/test-design/SKILL.md#bước-3`
   - checklist / mẫu: `references/coverage-checklist.md#...`
   - script: `scripts/rtm_check.py`
   - sản phẩm: `PM-L0001!TC_012` hoặc `tests/cases/PM-L0001.md#TC_012`
   Chưa xác định được địa chỉ thì `Trạng thái: Chưa rõ phạm vi` kèm câu hỏi ngược, không đoán.
6. **Phân biệt sửa một lần và sửa nguyên tắc.** Lỗi chỉ đúng một chỗ (`L1-sản phẩm`) thì sửa tại chỗ, không sinh rule. Nhận xét về *cách làm* thì bắt buộc sinh thay đổi ở rule / checklist / mẫu / script — không được chỉ sửa sản phẩm rồi đóng FB.

## C. Tổng quát hoá

7. **Sửa một chỗ người dùng chỉ ra là chưa xong.** Mỗi FB loại L2–L5 phải quét toàn bộ sản phẩm hiện có tìm các chỗ cùng lỗi, ghi số lượng và danh sách vào `Phạm vi ảnh hưởng`, rồi sửa hoặc xếp hàng chờ sửa. Quét được bằng script thì chạy script, không tự khai.
8. Mỗi FB phải có `Cách kiểm`: cách chứng minh đã khắc phục — một mục checklist, một lệnh script, hoặc một câu tự soát trả lời được bằng có/không. FB không có cách kiểm thì chưa được chuyển khỏi trạng thái `Mới`.

## D. Vào rule và gắn gate

9. Thay đổi rule hoặc skill sinh từ FB phải: tăng version file đó, thêm một dòng changelog với cột `Nguồn` ghi `FB-nnn`. Không có `FB-nnn` hay bug lọt làm nguồn thì đó là đề xuất của AI → dán nhãn "chờ duyệt", không áp dụng như rule.
10. Vòng đời trạng thái, chỉ đi theo thứ tự này:
    `Mới` → `Đã sửa sản phẩm` → `Đã vào rule (chờ duyệt)` → `Đã duyệt` → `Đã có gate`.
    Chỉ **người dùng** chuyển sang `Đã duyệt`. AI không tự duyệt rule của chính mình. Người dùng bác thì `Bị bác` + lý do, và thay đổi rule sinh từ nó bị hoàn nguyên (ghi rõ trong changelog).
11. **Tái phát là lỗi của gate, không phải lỗi trí nhớ.** FB đã `Đã duyệt` mà AI vẫn lặp lại → `Tái phát` +1 và bắt buộc nâng cấp: rule dạng văn xuôi → mục bắt buộc trong checklist → điều kiện kiểm trong script. Một FB tái phát từ 2 lần trở lên mà vẫn chỉ nằm ở dạng văn xuôi thì coi là chưa xử lý.

## E. Dùng bộ nhớ

12. **Đầu mỗi task**: đọc `feedback/log.md`, nạp mọi FB chưa ở trạng thái `Đã có gate` hoặc `Bị bác`, và áp dụng chúng như rule. Chạy `python skills/feedback-loop/scripts/fb_report.py` khi sổ đã dài để lấy danh sách cần nạp.
13. **Cuối mỗi task**: báo trong 1–3 dòng: FB nào đã áp dụng, FB nào mới mở, FB nào đang chờ người dùng duyệt. Không kể lại toàn bộ sổ.
14. Sổ `feedback/log.md` là bộ nhớ chính thức và mang theo được giữa các phiên, các công cụ. Trí nhớ nội bộ của AI hay của một công cụ cụ thể chỉ là bản tiện dụng, khi lệch thì lấy sổ làm gốc.

## F. Làm theo lệnh, báo đúng

15. **Comment chờ lệnh.** Người dùng viết comment (trong file hay trong chat) thì ghi FB và nói lại ngắn gọn điều đã hiểu; **chưa sửa sản phẩm** cho tới khi người dùng bảo làm (vd "làm lại", "sửa đi", "update theo comment"). Yêu cầu "kiểm tra xem còn lỗi gì" là soát và liệt kê, không sửa file.
16. **Báo trong chat chỉ ghi điều đã kiểm.** Số lượng (số case, số ô, số câu hỏi) đếm bằng script trên file vừa giao. Không viết "giữ nguyên", "như bản gốc của bạn", "đã sửa hết" khi chưa so với file. Câu báo sai cũng là lỗi, ghi vào FB của vòng đó.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.2 | 2026-10-08 | Thêm mục F: rule 15 (comment của người dùng chờ lệnh mới sửa; "kiểm tra" chỉ là soát), rule 16 (báo trong chat chỉ ghi điều đã kiểm, số đếm bằng script). **Chờ duyệt.** | FB-058 · FB-056 |
| v0.1 | 2026-09-29 | Khởi tạo: ghi nhận FB có ID, xếp loại L1–L7, tổng quát hoá bắt buộc, vòng đời trạng thái, quy tắc tái phát → gate, cách nạp bộ nhớ đầu/cuối task. | FB-001. Rule 7 (tổng quát hoá) và 11 (tái phát → gate) là suy luận của AI từ `common.md` rule 8 — **chờ duyệt** |
