---
name: ba-analysis
description: Phân tích Use Case (UC) mới cho vai trò BA — trích xuất có ID, đối soát hai chiều với tài liệu gốc, gom câu hỏi làm rõ theo mức độ, và chốt baseline có version trước khi bàn giao sang Code/Test. Dùng khi có UC List (Excel/Word/PDF) hoặc tài liệu yêu cầu cần phân tích, khi người dùng nói "đọc UC", "phân tích use case", "trích xuất UC", hoặc khi chuẩn bị bàn giao đặc tả cho viết test Playwright. Không dùng cho việc xử lý thay đổi trên UC đã có baseline — xem skill ba-change-handling.
license: Proprietary — nội bộ dự án
---

# Phân tích UC mới (BA)

## Vì sao quy trình này tồn tại

"Đọc UC 2 lượt" không kiểm chứng được và không có tác dụng thật với AI — dù có đọc lại hay không, AI vẫn luôn báo "đã đọc kỹ". AI thường bỏ sót vì ba lý do: tài liệu dài nên chi tiết bị lướt qua, thông tin nằm trong bảng/hình/mockup, và AI có xu hướng tóm tắt thay vì trích xuất nguyên văn. Quy trình dưới đây thay "đọc lại" bằng các sản phẩm bắt buộc phải ra sau mỗi bước, để việc kiểm tra không phụ thuộc vào lời tự báo cáo của AI.

## Quy trình

### 1. Trích xuất

Nếu nguồn là Excel (UC List dạng bảng): chạy

```bash
python scripts/extract_uc_list.py <file.xlsx> <out.md> --summary summary.json
```

Script trích nguyên văn mọi cột (không tóm tắt, không dịch), ghi vị trí nguồn (`Sheet!R<dòng>`) cho từng UC, và tự phát hiện các lỗi vệ sinh dữ liệu phổ biến: ID trùng, ID có khoảng trắng thừa, ID nhảy số, ô trống ở cột chính (name/actor/description), tên UC bị chép nhầm trùng nội dung cột Actor. Đọc phần in ở cuối (JSON summary) trước — nó chỉ ra ngay những dòng cần chú ý mà không phải dò cả file.

Nếu nguồn là Word/PDF/tài liệu văn xuôi (không có cấu trúc bảng UC-ID sẵn): phân rã thủ công theo cùng một template cho mỗi UC, mỗi phần tử có ID:

- actor, tiền điều kiện, hậu điều kiện
- từng bước luồng chính (`UC03-MF-04`), luồng thay thế (`UC03-AF-4a`), luồng ngoại lệ (`UC03-EF-01`)
- business rule (`BR-12`)
- trường dữ liệu (bắt buộc, định dạng, độ dài)
- text trên màn hình, phân quyền

Tài liệu dài → xử lý theo từng đoạn có phạm vi dòng/mục rõ ràng (ví dụ "UC03, dòng 40–85"), đừng đọc hết cả file rồi mới tóm tắt — đó chính là chỗ AI hay lướt qua chi tiết.

### 2. Đối soát hai chiều

Mỗi dòng trong bảng trích xuất phải chỉ ra được vị trí trong tài liệu gốc, và mỗi đoạn tài liệu gốc phải có mặt trong bảng. Ở lượt này, đánh dấu thêm:

- mâu thuẫn và chỗ thiếu
- từ mơ hồ ("nhanh", "hợp lệ", "phù hợp", "v.v.", "the necessary information"…)
- yêu cầu không test được
- text hiển thị / thông báo lỗi không có nguyên văn trong nguồn → chuyển thành câu hỏi CHẶN ở bước 4, không tự diễn giải hay bịa ra

Nếu phân tích cả một bộ nhiều UC (không phải một UC lẻ), làm thêm một lượt liên UC:

- quan hệ include/extend
- trạng thái của cùng một đối tượng qua nhiều UC (ví dụ: đơn hàng Nháp → Đã gửi → Đã duyệt)
- phân quyền có nhất quán giữa các UC không
- rule giữa các UC có xung đột không

Xem `references/vi-du-sgs-dtp-luot-2.py` — ví dụ thật đã chạy cho một bộ 159 UC thật (nhóm UC theo mức xác nhận phạm vi MVP/Phase 2, dò lỗi dữ liệu, phụ thuộc chưa xử lý, thuật ngữ không nhất quán, sinh bảng phát hiện có ID và câu hỏi kèm theo). Đây là ví dụ để phỏng theo **cấu trúc và cách tư duy**, không phải script chạy nguyên xi được cho dự án khác — tên cột, tiền tố UC, và logic nhóm phạm vi luôn khác nhau giữa các dự án, cần viết lại phần này cho từng bộ UC.

Hình, sơ đồ, bảng nào không đọc được → liệt kê ra trong một mục riêng, không im lặng bỏ qua.

### 3. Read-back

Tóm tắt cách hiểu của bạn cho mỗi UC trong 5–7 dòng: ai làm, để đạt gì, luồng chính ra sao, rule nào quan trọng. Checklist (bước 4) chỉ bắt được chỗ bạn *biết* mình chưa rõ; read-back bắt chỗ bạn hiểu sai mà không biết là sai — người đọc chỉ mất nửa phút để thấy chỗ lệch.

### 4. Gom câu hỏi

Một lượt duy nhất, sắp theo mức: **CHẶN**, **QUAN TRỌNG**, **NHỎ**. Mỗi câu ghi rõ: vị trí trong UC, ảnh hưởng nếu không làm rõ, và một đề xuất mặc định để người dùng chỉ cần xác nhận hoặc sửa. Ví dụ:

```
Q-07 · UC03-MF-05 · CHẶN
Vấn đề: UC ghi "hiển thị thông báo lỗi" khi sai mật khẩu nhưng không nêu nội dung.
Ảnh hưởng: không có text chính xác thì Playwright không assert được.
Đề xuất: "Tên đăng nhập hoặc mật khẩu không đúng" → xác nhận hay sửa?
```

Dùng `references/checklist-lam-ro.md` để không bỏ sót nhóm câu hỏi thường gặp.

### 5. [DỪNG] chờ duyệt

Câu hỏi mức CHẶN chưa được trả lời → **không đi tiếp**, không bàn giao sang Code/Test. Câu mức thấp hơn được làm tiếp nhưng gắn nhãn `[GIẢ ĐỊNH]`.

### 6. Chốt baseline v1.0

Lưu kết quả (bảng trích xuất + đối soát + câu trả lời đã duyệt) thành file có version trong repo, cạnh code test. Mỗi câu trả lời ghi kèm nguồn: ai xác nhận, ngày nào — không chỉ nằm trong lịch sử chat.

### 7. Rủi ro & phạm vi test

Ba mục cụ thể, không suggest chung chung kiểu "nên validate input":

- **Rủi ro / điểm dễ sai** của UC, để ưu tiên test.
- **Phạm vi test**: trong phạm vi / ngoài phạm vi / chưa đủ thông tin để test.
- **Đề xuất bổ sung yêu cầu** — mỗi đề xuất gắn với một ID cụ thể và có lý do; đề xuất không gắn được vào đâu thì bỏ. Đề xuất nào làm thay đổi yêu cầu thì quay lại bước 4 xin duyệt, **không được tự đưa vào baseline hay test**.

### 8. Bàn giao

Kiểm tra theo `references/definition-of-done.md` trước khi coi là xong: mọi bước UC có ID · không còn câu CHẶN mở · mọi kết quả mong đợi đều quan sát được · baseline đã có version.

## Review độc lập

Đưa kết quả phân tích sang một phiên/agent mới để review, kèm UC gốc và tiêu chí hoàn thành (`references/definition-of-done.md`), với nhiệm vụ duy nhất là tìm lỗi. Không dùng cùng một phiên vừa phân tích vừa tự review — dễ tự xác nhận lại chính mình.

## Tệp tham khảo

- `scripts/extract_uc_list.py` — script Lượt 1, đọc trực tiếp một UC List dạng Excel.
- `references/checklist-lam-ro.md` — checklist câu hỏi làm rõ dùng lại cho mọi UC.
- `references/definition-of-done.md` — tiêu chí hoàn thành trước khi bàn giao.
- `references/vi-du-sgs-dtp-luot-2.py` — ví dụ Lượt 2 thật đã chạy trên một dự án cụ thể.
