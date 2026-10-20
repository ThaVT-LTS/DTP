---
name: test-design
description: Thiết kế bộ test case từ test basis do BA bàn giao — lập bản đồ kiểm thử, ma trận điều hướng, phân vùng tương đương, giá trị biên, bảng quyết định, chuyển trạng thái, ma trận phân quyền, CRUD, pairwise, đoán lỗi; viết test case theo khung Redirect / Validation / Function (Positive, Negative, Abnormal); đo độ phủ bằng ma trận truy vết (RTM) và bàn giao cho bước viết Playwright. Có chế độ cập nhật test case khi yêu cầu thay đổi. Dùng skill này bất cứ khi nào người dùng muốn viết test case, test scenario, checklist test, ma trận truy vết, rà độ phủ, review bộ test, hoặc sửa test case theo yêu cầu mới — kể cả khi họ chỉ nói "viết TC cho UC này" hay "xem còn thiếu case nào".
---

# Tester — Thiết kế test (v0.2)

Tuân thủ `rules/common.md` và `rules/tester.md` ở mọi bước.

| Cần gì | Đọc |
|---|---|
| Nhóm TC Redirect / Validation / Function, checklist từng nhóm | `references/tc-framework.md` |
| Cách làm từng kỹ thuật, ví dụ, tiêu chí phủ | `references/techniques.md` |
| Mẫu file thiết kế, mẫu TC, báo cáo bàn giao | `references/templates.md` |
| Tự review trước khi bàn giao, các kiểu bug hay lọt | `references/coverage-checklist.md` |
| Case ngoài nghiệp vụ: trên 100 mục, tên dài, điều hướng nhiều cấp, đồng thời, dữ liệu sau thao tác | `references/technical-risk-checklist.md` |
| Người dùng không cần TC mà cần file phân tích case cha con | `references/templates.md` §7 |
| Ví dụ hoàn chỉnh: test basis → thiết kế → TC → RTM | `examples/` |

Vì sao có bước thiết kế riêng: nếu viết TC thẳng từ UC, AI thường chỉ phủ luồng chính và vài case hiển nhiên. Kỹ thuật thiết kế biến mỗi trường, mỗi rule, mỗi trạng thái thành một tập giá trị cần thử có hệ thống, và script RTM cho biết chính xác còn thiếu gì — thay vì AI tự khai "đã phủ đủ".

## Chọn chế độ
- **Chế độ A — thiết kế mới:** test basis của module chưa có TC.
- **Chế độ B — cập nhật:** test basis lên version mới; changelog của BA liệt kê ID thay đổi.

## Đầu ra

```
tests/design/<UC-ID>.md      bản đồ kiểm thử + bảng kỹ thuật + loại trừ
tests/cases/<module>.md      test case theo khung R/V/F
tests/questions.md           câu hỏi Q-T-nn gửi BA
tests/rtm.md                 ma trận truy vết — do scripts/rtm_check.py sinh, không viết tay
tests/design-report.md       báo cáo bàn giao cho bước Code
```

---

## Chế độ A — thiết kế mới

### Bước 0 — Kiểm tra đầu vào
1. Xác nhận test basis có version và không còn câu CHẶN.
2. Với mỗi UC, soát theo checklist "Sẵn sàng bàn giao" của test basis: có NV, có FD + MS khi có nhập liệu, có MF, BR có kết quả khi vi phạm, có ST cho đối tượng có trạng thái, có dòng PM "Không".
3. Thiếu thì ghi `Q-T-nn` vào `tests/questions.md` (mức CHẶN / QUAN TRỌNG / NHỎ, vị trí, ảnh hưởng, đề xuất mặc định). Phần đủ thông tin vẫn thiết kế tiếp; phần thiếu đánh dấu `[CHỜ Q-T-nn]` trong file thiết kế.

### Bước 1 — Bản đồ kiểm thử
Trong `tests/design/<UC-ID>.md`, liệt kê mọi ID của UC trong test basis (NV, FD, MS, MF, AF, EF, BR, SE) và các dòng PM, ST liên quan, xếp vào nhóm R / V / F, gắn kỹ thuật dự định và ưu tiên. Đây là danh sách "phải phủ"; script sẽ kiểm tra lại.

### Bước 2 — Chọn kỹ thuật và lập bảng thiết kế
Tra bảng dưới, rồi làm theo `references/techniques.md`. Mỗi dòng trong bảng thiết kế có ID riêng để TC trỏ tới.

| Gặp trong test basis | Kỹ thuật | Sản phẩm (ID) | Nhóm TC |
|---|---|---|---|
| Đường vào / ra (NV) | Ma trận điều hướng × vai trò | dùng thẳng NV | Redirect |
| Trường nhập (FD) | Phân vùng tương đương + giá trị biên | `-EP-nn`, `-BV-nn` | Validation |
| Rule nhiều điều kiện (BR) | Bảng quyết định | `-DT-nn-Rk` | Function |
| Đối tượng có trạng thái | Chuyển trạng thái (hợp lệ + không hợp lệ) | dùng thẳng ST | Function |
| Phân quyền (PM) | Ma trận vai trò × hành động × phạm vi dữ liệu | dùng thẳng PM | Redirect (vào màn hình), Function (hành động) |
| Luồng (MF / AF / EF) | Use case / kịch bản | dùng thẳng MF, AF, EF | Function |
| Nhiều UC đụng cùng dữ liệu (SE) | Ma trận CRUD liên UC | dùng thẳng SE, thêm `-EG-nn` nếu cần | Function |
| Nhiều tham số độc lập kết hợp (bộ lọc, cấu hình, trình duyệt) | Pairwise | `-PW-nn` | Function / Validation |
| Chỗ hay lỗi theo kinh nghiệm | Đoán lỗi theo checklist | `-EG-nn` | cả ba nhóm |
| Mỗi màn hình / khu vực (bắt buộc, không phụ thuộc test basis) | Checklist rủi ro ngoài nghiệp vụ `technical-risk-checklist.md` A–G | `-EG-nn`, Nguồn ghi `CK-<mục>` | cả ba nhóm |

### Bước 3 — Viết TC theo khung R / V / F
- Theo `references/tc-framework.md`: mỗi UC có ba nhóm; mỗi TC thuộc một loại Positive (happy case), Negative (cố tình sai) hoặc Abnormal (sự cố bất thường).
- Theo mẫu TC trong `references/templates.md` — đúng tên trường, một trường một dòng, vì script đọc theo mẫu này.
- `Nguồn` liệt kê mọi ID mà TC phủ (ID test basis + ID bảng thiết kế).
- `Mong đợi` dùng text nguyên văn từ MS và tiêu đề/URL từ NV.
- Ưu tiên: P1 = luồng chính, phân quyền, dữ liệu và bảo mật; P2 = luồng thay thế, rule, validation chính; P3 = hiển thị và trường hợp hiếm. P1 Positive của luồng chính gắn thêm `@smoke`.

### Bước 4 — Đo độ phủ
```
python scripts/rtm_check.py --basis docs/test-basis/<tên>.md tests/design/*.md --cases tests/cases/*.md --out tests/rtm.md
```
Script báo: ID chưa có TC, rule thiếu TC vi phạm hoặc thiếu TC thỏa, UC thiếu nhóm R/V/F, TC trỏ tới ID không tồn tại, TC thiếu trường, TC trùng ID, kết quả mong đợi mơ hồ. Sửa đến khi script không còn lỗi, hoặc ghi lý do loại trừ vào file thiết kế. Không sửa `tests/rtm.md` bằng tay.

### Bước 5 — Review
1. Tự review theo `references/coverage-checklist.md`.
2. Đề nghị người dùng review trong một phiên mới: chỉ đưa test basis + file thiết kế + TC + checklist, nhiệm vụ duy nhất là tìm case còn thiếu hoặc kết quả mong đợi sai.

### Bước 6 — Bàn giao cho Code
Viết `tests/design-report.md` theo mẫu: version bộ test, số TC theo nhóm/loại/ưu tiên, bộ smoke, TC không tự động hóa được và lý do, dữ liệu và môi trường cần chuẩn bị, Q-T còn mở, rủi ro còn lại. Khi cần file Excel để chạy tay hoặc nhập công cụ quản lý test:
```
python scripts/tc_export_xlsx.py tests/cases/*.md --out tests/test-cases.xlsx
```

---

## Chế độ B — cập nhật khi test basis đổi

1. Đọc changelog test basis: danh sách ID thêm / sửa / xóa.
2. Tìm TC bị ảnh hưởng: TC có `Nguồn` chứa ID đổi (tìm chuỗi ID trong `tests/cases/`), và TC của UC liên quan mà báo cáo ảnh hưởng của BA nêu.
3. Cập nhật bảng thiết kế trước (lớp tương đương, biên, rule bảng quyết định, trạng thái), rồi mới sửa TC.
4. TC không còn đúng: sửa nội dung và ghi `- Trạng thái: Sửa ở v<x.y>`; TC không còn áp dụng: `- Trạng thái: Deprecated ở v<x.y>` — không xóa, không tái sử dụng ID. ID mới được thêm thì viết TC mới.
5. Chạy lại `rtm_check.py`. Đề xuất bộ regression: TC bị sửa + TC cùng UC mức P1 + bộ smoke, dạng lệnh `npx playwright test --grep "..."`.

## Vòng học từ bug lọt

Mỗi bug lọt ra sau khi test là dữ liệu để cải thiện bộ quy tắc:
1. Tìm TC lẽ ra phải bắt bug. Không có TC nào → vì sao: test basis thiếu (báo BA), thiếu kỹ thuật, thiếu mục trong checklist, hay kết quả mong đợi sai.
2. Viết TC bắt được bug, gắn tag `@bug-<mã>`.
3. Đề xuất sửa rule, skill hoặc checklist tương ứng; chờ người dùng duyệt rồi tăng version.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.2 | 2026-10-05 | `references/coverage-checklist.md`, `techniques.md`, `tc-framework.md`: phân quyền âm kiểm trên giao diện và URL; kiểm API chỉ khi `profile.md` ghi tester được gọi API, viết ở sheet `API` riêng (14 chỗ). Hanna duyệt 05/10. | FB-039 |
| v0.2 | 2026-10-02 | Thêm checklist rủi ro ngoài nghiệp vụ (`technical-risk-checklist.md`), bước bắt buộc cho mỗi màn hình; mẫu phân tích case cha con (templates §7); coverage-checklist thêm các kiểu bug 16–20 và mục E. | FB-028 |
| v0.1 | 2026-09-28 | Khởi tạo: chế độ A (bước 0–6), chế độ B, vòng học từ bug lọt; khung Redirect / Validation / Function; script RTM và xuất Excel. | Yêu cầu trong chat: ma trận, bảng quyết định, phân vùng biên, khung TC Redirect / Validation / Function |