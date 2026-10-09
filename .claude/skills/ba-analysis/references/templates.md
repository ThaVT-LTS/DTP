# Template đầu ra — BA

Mục lục: §1 analysis.md · §2 inventory (a) danh sách UC · §3 inventory (b) UC spec · §4 phát hiện · §5 câu hỏi · §6 read-back · §7 báo cáo chat · §8 báo cáo ảnh hưởng · §9 baseline và changelog

---

## §1 Khung `analysis.md`

```markdown
# Phân tích BA — <tên tài liệu> <version>

> Trạng thái: BẢN NHÁP / ĐÃ CHỐT v<x.y> — <đang dừng ở bước nào, chờ gì>

| | |
|---|---|
| Nguồn | <file, kích thước, số sheet/trang> |
| Quy trình | skill ba-analysis v<x.y> — chế độ A/B · rule common + ba v<x.y> |
| Ngày | YYYY-MM-DD |
| Đi kèm | uc-inventory.md · questions.md |

## 1. Kiểm kê nguồn        — đã đọc gì; phần không đọc được; độ phủ chiều ngược; loại tài liệu (a)/(b); tài liệu được dẫn chiếu nhưng vắng mặt [CHƯA KIỂM CHỨNG]
## 2. Đối soát số liệu     — bảng: hạng mục | tài liệu ghi | đếm lại | lệch
## 3. Phân loại phạm vi    — quy tắc phân nhóm + bảng nhóm | số UC | UC | xử lý test [GIẢ ĐỊNH – chờ Q-nn]
## 4. Read-back            — §6
## 5. Phát hiện            — bảng F-nn (§4)
## 6. Bước tiếp theo
## Phụ lục                 — ma trận vai trò × UC, bảng thuật ngữ...
```

## §2 Mục inventory — (a) danh sách UC

Do `scripts/extract_uc_list.py` sinh. Mỗi UC một khối; trường **đậm** là nguyên văn nguồn, trường *nghiêng* là do bước phân tích thêm qua `--annotations`:

```markdown
#### UC-EVD-014 · Update Evidence Workflow Status
`UC List!R103`

- **Actor:** Customer Admin, Customer User
- **Description:** Update evidence workflow status using the MVP status model ...
- **WBS Reference:** CP-20 Evidence workflow statuses (P1)
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Phát hiện:* F-20, F-29, F-36
```

File annotations là JSON `{ "<UC ID>": { "<tên trường>": "<giá trị>" } }`.

## §3 Mục inventory — (b) UC spec

```markdown
#### UC-XXX-nnn · <tên UC nguyên văn>
Nguồn: <file · mục/trang>

- Actor chính: ... · Actor phụ: ...
- Mục tiêu: ...
- Tiền điều kiện: PRE-01 ...; PRE-02 ...
- Trigger: ...

Luồng chính
- UC-XXX-nnn-MF-01: <bước, nguyên văn>
- UC-XXX-nnn-MF-02: ...

Luồng thay thế
- UC-XXX-nnn-AF-01 (rẽ từ MF-03): <điều kiện> → <các bước> → <quay lại MF-nn / kết thúc>

Luồng ngoại lệ
- UC-XXX-nnn-EF-01 (tại MF-04): <sự cố> → <hệ thống xử lý>

Hậu điều kiện / tác động phụ
- UC-XXX-nnn-SE-01: <dữ liệu nào đổi, thông báo gửi ai, audit, màn hình khác cập nhật>

Business rule
- UC-XXX-nnn-BR-01: <nguyên văn> — điều kiện: ... — kết quả: ...

Trường dữ liệu
| ID | Nhãn (nguyên văn) | Kiểu | Bắt buộc | Độ dài | Giá trị / khoảng | Định dạng, ký tự cho phép | Mặc định | Duy nhất | Phụ thuộc | Thông báo lỗi |
|---|---|---|---|---|---|---|---|---|---|---|

Text giao diện (nguyên văn)
| ID | Loại (tiêu đề / nút / thông báo / hộp thoại) | Khi nào xuất hiện | Text |
|---|---|---|---|

Phân quyền: vai trò → hành động → phạm vi dữ liệu (tham chiếu PM-...)
Phần không đọc được: <hình, mockup...>
```

## §4 Dòng phát hiện

```markdown
| ID | Loại | Vị trí | Phát hiện | Câu hỏi |
|---|---|---|---|---|
| F-17 | Phụ thuộc | UC List!R94, R95, R97 | EVD-004/005/007 hiển thị ... do ASM-001/002 tạo ra, đều P2. | Q-11 |
```

Loại: Số liệu · Lỗi dữ liệu · Phạm vi · Phụ thuộc · Thiếu luồng · Thuật ngữ · Mơ hồ · Mâu thuẫn · Khó test. Phát hiện nào không gắn được vào vị trí cụ thể thì bỏ.

## §5 Khối câu hỏi

```markdown
### Q-05 · <tiêu đề ngắn>
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-20, F-29
- **Vị trí:** <sheet!hàng / mục, ID>
- **Vấn đề:** <mô tả, trích nguyên văn chỗ mơ hồ>
- **Ảnh hưởng:** <không làm rõ thì test/kết quả mong đợi bị ảnh hưởng thế nào>
- **Đề xuất mặc định:** <phương án cụ thể để người dùng chỉ cần xác nhận hoặc sửa>
- **Trả lời:**
```

Sau khi có trả lời: `**Trạng thái:** Đã trả lời · <người trả lời> · <ngày>` và ghi câu trả lời nguyên văn.

## §6 Read-back

- (a) Danh sách UC: "Luồng nghiệp vụ chính" tối đa 15 ý, mỗi ý có ID UC trong ngoặc; một đoạn "Vai trò làm được gì"; một dòng "Ngoài phạm vi".
- (b) UC spec, mỗi UC 5–7 dòng:

```markdown
**UC-XXX-nnn** — <Actor> <làm gì> để <mục tiêu>. Luồng chính: <3–4 bước chính>.
Rule quan trọng: <BR-..>. Kết thúc khi <hậu điều kiện>. Chỗ AI chưa chắc: <nếu có>.
```

## §7 Báo cáo chat cuối bước 3 (tối đa 15 dòng)

1. Đã làm bước nào, đang dừng ở cổng nào.
2. Con số chính (số UC, phạm vi đề xuất, số phát hiện, số câu hỏi theo mức).
3. Danh sách câu CHẶN, mỗi câu một dòng.
4. Rule/skill AI tự rút ra trong lần chạy (chờ duyệt).
5. Tên các file đầu ra.

## §8 Báo cáo ảnh hưởng (chế độ B) — `docs/change/<tên>.v1.0-to-v1.1.md`

```markdown
# Ảnh hưởng thay đổi — <tên> v1.0 → v1.1
Nguồn thay đổi: <file mới / Q&A #.. / biên bản ngày .. / bug ..>

| # | Loại | ID | Trước | Sau | Nguồn |
|---|---|---|---|---|---|
| 1 | Sửa | UC-SRQ-004-BR-01 | Hủy khi Submitted | Hủy khi Submitted hoặc Accepted | Q&A #61 |

## Truy vết
| ID đổi | Rule / UC liên quan | ID test basis bị ảnh hưởng | TC bị ảnh hưởng (theo Nguồn/tag) |
|---|---|---|---|

## Regression đề xuất
npx playwright test --grep "@UC-SRQ-004|@UC-SRQ-007"

## Câu hỏi mới
## Chờ duyệt → baseline v1.1, test basis v1.1, changelog
```

## §9 Baseline và changelog

Đầu file baseline:

```markdown
# Baseline — <tên> v1.0
Duyệt bởi: <người> · Ngày: <..> · Từ phân tích: docs/analysis/<..>/
Giả định còn hiệu lực: Q-07 (đề xuất mặc định), Q-11 ...
```

`docs/baseline/changelog.md`:

```markdown
| Version | Ngày | ID thay đổi | Mô tả | Nguồn | Người duyệt |
|---|---|---|---|---|---|
```
