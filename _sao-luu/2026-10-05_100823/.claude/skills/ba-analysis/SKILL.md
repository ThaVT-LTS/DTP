---
name: ba-analysis
description: Phân tích tài liệu yêu cầu (danh sách Use Case, UC spec, đặc tả màn hình) để chuẩn bị kiểm thử — kiểm kê nguồn, trích xuất nguyên văn, đối soát hai chiều, read-back, câu hỏi làm rõ, chốt baseline có version, rồi xuất test basis bàn giao cho Tester. Có chế độ phân tích ảnh hưởng khi yêu cầu thay đổi. Dùng skill này bất cứ khi nào người dùng gửi UC, yêu cầu, biên bản họp, câu trả lời Q&A hoặc bản cập nhật tài liệu và muốn phân tích, làm rõ, đối chiếu thay đổi hay chuẩn bị tài liệu cho Tester — kể cả khi họ chỉ nói "đọc giúp file này" hay "có gì mới trong bản này".
---

# BA — Phân tích yêu cầu (v0.2)

Tuân thủ `rules/common.md` và `rules/ba.md` ở mọi bước. Template: `references/templates.md`. Checklist soát lỗ hổng: `references/gap-checklist.md`. Mẫu bàn giao cho Tester: `references/test-basis-template.md`.

Mục tiêu của BA trong hệ sinh thái này là hiểu yêu cầu đủ chính xác để test. Vì vậy mọi đầu ra được thiết kế ngược từ nhu cầu của Tester: Tester cần biết người dùng vào màn hình bằng đường nào (Redirect), mỗi trường nhận giá trị gì (Validation), và luồng, rule, trạng thái chạy ra sao (Function).

## Chọn chế độ

- **Chế độ A — phân tích mới:** chưa có baseline cho tài liệu này.
- **Chế độ B — thay đổi:** đã có baseline, người dùng gửi bản mới, câu trả lời Q&A, biên bản họp, hoặc bug cho thấy hệ thống chạy khác yêu cầu.

## Đầu ra

```
docs/analysis/<tài-liệu>-<version>/   uc-inventory.md · analysis.md · questions.md
docs/baseline/<tên>.v<x.y>.md          baseline đã duyệt + docs/baseline/changelog.md
docs/test-basis/<tên>.v<x.y>.md        bàn giao cho Tester
docs/change/<tên>.v<x.y>-to-v<x.z>.md  báo cáo ảnh hưởng (chế độ B)
```

---

## Chế độ A — phân tích mới

### Bước 0 — Kiểm kê nguồn
1. Liệt kê file, sheet hoặc mục, kích thước.
2. Soát phần dễ bị bỏ sót: sheet/hàng/cột ẩn, comment, hình, sơ đồ, công thức, ô gộp, bộ lọc. Phần không đọc được thì ghi ra.
3. Xác định loại tài liệu: **(a)** danh sách UC — mỗi UC một dòng; **(b)** UC spec — có luồng, rule, trường dữ liệu. Loại (a) chỉ đủ để phân tích phạm vi, vai trò, phụ thuộc; ghi rõ điều này trong analysis.md.
4. Liệt kê tài liệu và mã được dẫn chiếu nhưng không có trong input (WBS, PRD, Q&A...), gắn [CHƯA KIỂM CHỨNG].

5. **Đánh giá mục đích sản phẩm** → mục đầu của `analysis.md`, 10–15 dòng, móc nối các dữ kiện để trả lời: ai dùng và họ đứng ở phía nào; sản phẩm giải quyết vấn đề nghiệp vụ gì; giá trị cốt lõi; ràng buộc nào định hình thiết kế; vì sao cấu trúc lại chia như vậy. Mỗi nhận định ghi vị trí nguồn, hoặc `[SUY LUẬN: dữ kiện A + dữ kiện B]` khi tự ghép lại. Rồi **soát ngược**: liệt kê chỗ đi ngược mục đích vừa nêu, mỗi chỗ thành một phát hiện F-nn và một câu hỏi; không tự kết luận đó là lỗi. Ở chế độ B, việc đầu tiên là đối chiếu tài liệu mới với đoạn mục đích hiện có: xác nhận, bổ sung hay mâu thuẫn — ghi rõ, không sửa âm thầm.
6. Tài liệu là **bản thiết kế / mockup**: trích từng màn, từng phần tử bấm được và trạng thái (disabled, rỗng, lỗi) kèm text nguyên văn; lập ma trận thao tác × lối vào (menu từng mục, thanh hàng loạt, màn chi tiết); có bản thiết kế mới thì so với bản cũ theo màn (mới / sửa / giữ nguyên). Thứ tự ưu tiên nguồn theo `rules/common.md` rule 9.

### Bước 1 — Trích xuất (lượt 1) → `uc-inventory.md`
- Input dạng bảng Excel (.xlsx; CSV thì lưu thành .xlsx trước): chạy `scripts/extract_uc_list.py <file.xlsx> <out.md> --summary summary.json`. Script nhận UC theo ID dạng `UC-<MODULE>-<số>`; tài liệu dùng dạng ID khác thì sửa `ID_RE` ở đầu script. Script chép nguyên văn mọi cột, ghi vị trí nguồn, bắt lỗi dữ liệu (ID trùng, ID có khoảng trắng, ID nhảy số, ô chính trống, tên trùng actor, lệch cột, actor hiếm gặp) và tự kiểm độ phủ chiều ngược. Không chép tay, vì chép tay là nơi AI tóm tắt và bỏ sót.
- Input dạng văn bản (docx, pdf): trích từng UC theo template (b) trong `references/templates.md`, gán ID cho từng phần tử theo quy ước bên dưới.
- Trường do AI suy ra (nhóm phạm vi, vai trò chuẩn hóa) để ở dạng in nghiêng, tách khỏi trường nguyên văn, và ghi quy tắc suy ra trong analysis.md.

### Bước 2 — Đối soát (lượt 2) → `analysis.md`
1. Chiều xuôi: mỗi mục inventory có vị trí nguồn.
2. Chiều ngược: mọi ô hoặc đoạn trong nguồn có mặt trong inventory (script báo `coverage`).
3. Đếm lại mọi số liệu tổng hợp của tài liệu (số UC, tổng giờ, công thức) và so với con số tài liệu tự ghi.
4. Soát từng UC và cả bộ theo `references/gap-checklist.md`.
5. Soát liên UC: UC trong phạm vi phụ thuộc UC ngoài phạm vi; một khái niệm nhiều tên gọi; trạng thái của cùng đối tượng qua nhiều UC; phân quyền và tên vai trò nhất quán; quy tắc giới hạn (vd "tối đa 1") mâu thuẫn với luồng khác; UC trùng chức năng.
6. Ghi mỗi phát hiện thành một dòng F-nn (template trong references), gắn loại và câu hỏi xử lý nó.

### Bước 3 — Read-back và câu hỏi → `analysis.md`, `questions.md`
1. Read-back — cách AI đang hiểu, để người dùng bắt chỗ hiểu lệch mà checklist không bắt được:
   - (a) danh sách UC: luồng nghiệp vụ xuyên suốt của phạm vi (tối đa 15 ý) + mỗi vai trò làm được gì;
   - (b) UC spec: 5–7 dòng mỗi UC (ai, để đạt gì, luồng chính, rule quan trọng).
2. Câu hỏi: gom một lượt, gộp các phát hiện cùng gốc vào một câu, sắp CHẶN → QUAN TRỌNG → NHỎ. Mỗi câu có vị trí, vấn đề, ảnh hưởng, đề xuất mặc định, ô trả lời.
   - CHẶN: không có câu trả lời thì không xác định được phạm vi test hoặc kết quả mong đợi.
   - QUAN TRỌNG: ảnh hưởng thiết kế test, làm tiếp được với [GIẢ ĐỊNH].
   - NHỎ: lỗi dữ liệu, chuẩn bị môi trường.
3. **DỪNG.** Báo cáo ngắn trong chat theo template: con số chính, các câu CHẶN, file đầu ra. Không sang bước 4 khi còn câu CHẶN mở.

### Bước 4 — Chốt baseline (sau khi có trả lời)
1. Ghi từng câu trả lời vào `questions.md` (ai trả lời, ngày), chuyển trạng thái câu hỏi.
2. Cập nhật inventory theo câu trả lời; mỗi thay đổi ghi nguồn `Q-nn`.
3. Tạo `docs/baseline/<tên>.v1.0.md` và dòng đầu tiên trong changelog. Giả định còn dùng phải được liệt kê ở đầu baseline.

### Bước 5 — Rủi ro, phạm vi test và bàn giao → `docs/test-basis/<tên>.v1.0.md`
1. Rủi ro và điểm dễ sai của từng UC, gắn ID, để Tester ưu tiên.
2. Phạm vi test: trong / ngoài / chưa đủ thông tin.
3. Đề xuất bổ sung yêu cầu → thành câu hỏi, không tự đưa vào baseline.
4. Điền test basis theo `references/test-basis-template.md`. Mỗi UC trong phạm vi phải có đủ các bảng: đường vào/ra (NV), trường dữ liệu (FD), thông báo (MS), luồng (MF/AF/EF), business rule (BR), tác động phụ (SE); phần dùng chung có ma trận phân quyền (PM) và mô hình trạng thái (ST). Phần nào thiếu thông tin thì ghi `[CHỜ Q-nn]`, không để trống và không tự điền.
5. Chạy checklist "Sẵn sàng bàn giao" cuối template. Đề nghị người dùng review test basis trong một phiên mới (chỉ đưa tài liệu gốc + test basis + checklist, nhiệm vụ duy nhất là tìm lỗi) trước khi Tester nhận.

---

## Chế độ B — thông tin thay đổi

1. **Phân loại** từng thay đổi: thêm / sửa / xóa, ở ID nào; nguồn thay đổi (bản UC mới, Q&A, biên bản, bug).
2. **So trước/sau** ở mức phần tử: chạy lại bước 1 trên bản mới, so inventory hai bản theo ID (không so theo vị trí dòng, vì dòng có thể dịch chuyển).
3. **Truy vết ảnh hưởng:** phần tử đổi → business rule → UC liên quan (phụ thuộc, cùng đối tượng, cùng trạng thái) → ID trong test basis → TC có `Nguồn` hoặc tag chứa các ID đó.
4. **Đề xuất phạm vi regression:** danh sách tag để chạy lại (vd `--grep "@UC-EVD-014|@UC-REV-005"`).
5. **Câu hỏi mới** phát sinh từ thay đổi, theo đúng format câu hỏi.
6. **DỪNG** chờ duyệt. Sau khi duyệt: baseline v1.1, test basis v1.1, changelog ghi rõ ID đổi — Tester dùng changelog này để cập nhật TC (skill `test-design`, chế độ B).

Template báo cáo ảnh hưởng: `references/templates.md` §8.

---

## Quy ước ID

| Phần tử | ID | Ví dụ |
|---|---|---|
| UC | giữ nguyên ID gốc | `UC-EVD-008` |
| Đường vào / ra | `<UC>-NV-nn` | `UC-EVD-008-NV-02` |
| Trường dữ liệu | `<UC>-FD-nn` | `UC-EVD-008-FD-03` |
| Thông báo, text UI | `<UC>-MS-nn` | `UC-EVD-008-MS-05` |
| Luồng chính / thay thế / ngoại lệ | `<UC>-MF-nn` / `-AF-nn` / `-EF-nn` | `UC-EVD-008-AF-01` |
| Business rule | `<UC>-BR-nn` | `UC-EVD-008-BR-02` |
| Tác động phụ, hậu điều kiện | `<UC>-SE-nn` | `UC-EVD-008-SE-01` |
| Dòng ma trận phân quyền (dùng chung) | `PM-<ĐỐI TƯỢNG>-nn` | `PM-EVD-04` |
| Chuyển trạng thái (dùng chung) | `ST-<ĐỐI TƯỢNG>-nn` | `ST-SRQ-03` |
| Phát hiện / câu hỏi | `F-nn` / `Q-nn` | `F-17`, `Q-05` |

Tài liệu gốc không có ID UC thì tự đặt theo dạng `UC-<MODULE>-nnn` và ghi bảng đối chiếu tên gốc ↔ ID. Luồng thay thế đánh số liên tục (`AF-01`, `AF-02`) và ghi bước rẽ nhánh trong nội dung, để script của Tester đọc được.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.2 | 2026-10-02 | Bước 0 thêm mục 5 (đánh giá mục đích sản phẩm + soát ngược) và mục 6 (tài liệu thiết kế / mockup). Gộp từ bản skill ở chat Analysis. **Chờ duyệt.** | FB-014 |
| v0.1 | 2026-09-28 | Khởi tạo: chế độ A (bước 0–5) và chế độ B gộp vào một skill; nhánh (a) danh sách UC và bước 0 thêm sau lần chạy đầu với SGS DTP UC List v2.1; bước 5 xuất test basis theo khung Redirect / Validation / Function của Tester. | Thiết kế trong chat lượt 1; lần chạy SGS (chờ duyệt); yêu cầu bàn giao cho Tester |
