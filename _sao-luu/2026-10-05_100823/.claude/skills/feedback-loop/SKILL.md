---
name: feedback-loop
description: Biến mỗi nhận xét, góp ý, phê bình của người dùng thành một bản ghi nhớ FB-nnn có ID, địa chỉ sửa, cách kiểm và version — rồi sửa rule, checklist, mẫu hoặc script để lỗi đó không lặp lại. Gồm cách ghi sổ feedback/log.md, bảng xếp loại nhận xét L1–L7, cách quét toàn bộ sản phẩm tìm các chỗ cùng lỗi, cách nâng nhận xét thành gate tự động, và script fb_report.py kiểm tra tính toàn vẹn của sổ. Dùng skill này mỗi khi người dùng nhận xét về sản phẩm hoặc cách làm ("chỗ này sai", "TC thiếu pre-condition", "lần sau đừng...", "sao vẫn lặp lại lỗi này"), khi cần xem lại các góp ý đã ghi, khi bắt đầu một task để nạp bộ nhớ, hoặc sau khi có bug lọt.
---

# Vòng phản hồi và bộ nhớ (v0.1)

Tuân thủ `rules/common.md` và `rules/feedback.md` ở mọi bước.

| Cần gì | Đọc |
|---|---|
| Nhận xét này thuộc loại nào, sửa ở đâu, gắn gate kiểu gì | `references/classification.md` |
| Mẫu bản ghi FB, mẫu báo cáo áp dụng, mẫu dòng changelog | `references/templates.md` |

Vì sao cần skill riêng: một nhận xét được "ghi nhớ" trong đầu phiên chat sẽ mất khi mở phiên mới, và AI sẽ lặp lại đúng lỗi đó. Sổ FB làm nhận xét tồn tại độc lập với phiên; bước gắn gate làm nó tồn tại độc lập với việc AI có đọc sổ hay không.

## Đầu ra

```
feedback/log.md            sổ ghi nhớ — mỗi nhận xét một bản ghi FB-nnn
feedback/report.md          sinh bằng fb_report.py, không viết tay
rules/*.md, skills/**       bị sửa theo FB, kèm version + changelog trỏ FB-nnn
```

---

## 7 bước xử lý một nhận xét

### Bước 1 — Ghi trước, sửa sau
Mở `feedback/log.md`, cấp ID `FB-nnn` kế tiếp, dán **nguyên văn** câu của người dùng vào `Nguồn`. Nhiều ý trong một câu → tách nhiều FB. Chưa hiểu → hỏi đúng một câu lấy tiêu chí kiểm được (`rules/feedback.md` rule 3).

### Bước 2 — Xếp loại
Tra `references/classification.md`, chọn một loại L1–L7 và ghi `Địa chỉ` cụ thể. Quy ước địa chỉ:

| Đối tượng | Cách ghi |
|---|---|
| Rule | `rules/tester.md#7` |
| Skill | `skills/test-design/SKILL.md#bước-3` |
| Checklist, mẫu | `skills/test-design/references/coverage-checklist.md#luồng` |
| Script | `skills/test-design/scripts/rtm_check.py` |
| TC trong file Excel | `<sheet>!<TVP_ID>`, ví dụ `PM-L0001!TC_012` |
| TC trong repo | `tests/cases/PM-L0001.md#TC_012` |
| Tài liệu phân tích | `docs/test-basis/<tên>.v1.0.md#FD-03` |

### Bước 3 — Sửa chỗ được chỉ ra
Sửa đúng chỗ người dùng nói, ghi vào `Đã sửa`. Đây là phần nhỏ nhất của công việc — đừng dừng ở đây.

### Bước 4 — Quét tìm mọi chỗ cùng lỗi
Đây là bước làm nên chữ "cải thiện". Chuyển nhận xét thành một **tiêu chí tìm được**, rồi quét toàn bộ sản phẩm hiện có:

- quét được bằng script → chạy script, dán con số thật vào `Phạm vi ảnh hưởng`;
- chưa có script → viết một đoạn kiểm nhanh (grep, pandas/openpyxl với file Excel) và giữ lại đoạn đó;
- không quét được bằng máy → liệt kê tay từng chỗ, ghi rõ đã soát phạm vi nào.

Ví dụ: nhận xét "TC này thiếu pre-condition" → tiêu chí "TC có bước phụ thuộc vai trò/trạng thái dữ liệu mà cột Pre-condition rỗng" → đếm trên cả 3 sheet, không chỉ sheet đang mở.

Số chỗ tìm được quyết định việc tiếp theo: 1 chỗ → `L1-sản phẩm`, đóng FB; nhiều chỗ → lên `L2`–`L5` và đi tiếp bước 5.

### Bước 5 — Đưa vào rule / checklist / mẫu / script
Sửa đúng file ở `Địa chỉ`, tăng version file đó, thêm dòng changelog có `Nguồn = FB-nnn` (mẫu trong `references/templates.md`). Nếu nhận xét đi ngược một rule đang có → không sửa lặng lẽ: nêu xung đột, hỏi người dùng chọn, rồi mới sửa.

Chuyển `Trạng thái: Đã vào rule (chờ duyệt)`. **Không tự chuyển sang `Đã duyệt`.**

### Bước 6 — Gắn gate
Rule dạng văn xuôi là mức yếu nhất. Nâng dần:

```
văn xuôi trong rule  →  mục bắt buộc trong checklist  →  điều kiện trong script (mã thoát ≠ 0)
```

Chọn mức theo `references/classification.md`. Việc nào script kiểm được (trường rỗng, sai định dạng ID, thiếu nhóm TC, kết quả mong đợi mơ hồ, TC không truy vết) thì phải lên script — theo `common.md` rule 5. Ghi lệnh kiểm vào `Cách kiểm` và `Gate`.

### Bước 7 — Báo cáo ngắn
Cuối task, 1–3 dòng: FB nào vừa mở, đã sửa gì, đã sửa bao nhiêu chỗ cùng loại, đang chờ duyệt gì. Mẫu trong `references/templates.md`.

---

## Nạp bộ nhớ đầu task

1. Đọc `feedback/log.md`.
2. Chạy kiểm tra sổ và lấy danh sách phải nạp:
   ```
   python skills/feedback-loop/scripts/fb_report.py --log feedback/log.md --repo . --out feedback/report.md
   ```
   Script báo: FB thiếu trường bắt buộc, trạng thái sai vòng đời, FB `Đã vào rule` mà không changelog nào trỏ `FB-nnn`, FB tái phát ≥ 2 chưa có gate script, FB đứng ở `Mới` quá lâu.
3. Nạp mọi FB chưa `Đã có gate` / `Bị bác` như rule bổ sung cho task này.
4. Sổ dài thì đọc `feedback/report.md` mục "Cần nạp" thay vì đọc cả sổ.

## Khi AI lặp lại lỗi đã có FB

Không xin lỗi rồi sửa tại chỗ. Làm đúng thứ tự:
1. Tìm FB cũ, `Tái phát` +1, ghi ngày và chỗ lặp lại.
2. Hỏi: gate hiện tại là mức nào? Nếu mới ở văn xuôi hoặc checklist → nâng một mức (bước 6). Nếu đã có script mà vẫn lọt → script kiểm sai, sửa script và thêm ca kiểm cho chính nó.
3. Ghi nguyên nhân vào FB: chưa đọc sổ / rule viết mơ hồ / rule đúng nhưng không có gate / gate có mà sai.

## Nối với các vòng học khác

| Nguồn học | Vào đâu |
|---|---|
| Nhận xét của người dùng | FB — skill này |
| Bug lọt sau khi test | `test-design` mục "Vòng học từ bug lọt" → mở FB loại `L3-checklist` để phần sửa checklist đi cùng một sổ |
| Câu hỏi CHẶN bị trả lời muộn | `ba-analysis` — không mở FB, trừ khi người dùng nhận xét về *cách đặt câu hỏi* |

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-09-29 | Khởi tạo: 7 bước xử lý nhận xét, quy ước địa chỉ, cách nạp bộ nhớ đầu task, xử lý tái phát, script `fb_report.py`. | Yêu cầu trong chat: mỗi nhận xét thành một bản ghi nhớ và cải thiện dần |
