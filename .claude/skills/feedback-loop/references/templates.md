# Mẫu — bản ghi FB, báo cáo, changelog

## 1. Bản ghi FB trong `feedback/log.md`

Giữ đúng tên trường và thứ tự trường: `fb_report.py` đọc theo mẫu này.

```markdown
## FB-007 · Tiêu đề ngắn gọn lỗi hoặc yêu cầu
- Ngày: 2026-09-29
- Nguồn: chat 29/09 · "TC nào cũng phải ghi pre-condition, không thì người test sau không chạy lại được"
- Loại: L2-rule
- Địa chỉ: rules/tester.md#7 · skills/test-design/references/templates.md#mẫu-tc
- Tiêu chí kiểm: TC có bước phụ thuộc vai trò đăng nhập hoặc trạng thái dữ liệu mà cột Pre-condition rỗng
- Phạm vi ảnh hưởng: 422/429 TC rỗng cột Pre-condition (PM-L0001 247/254, PM-L0002 25/25, DM-L0001 150/150)
- Đã sửa: rules/tester.md v0.1→v0.2 rule 7; thêm mục kiểm vào coverage-checklist.md; sửa 12 TC mẫu trong tests/cases/
- Cách kiểm: python scripts/rtm_check.py --cases tests/cases/*.md → không còn cảnh báo PRECOND_EMPTY
- Gate: mức 3 · rtm_check.py điều kiện PRECOND_EMPTY
- Trạng thái: Đã vào rule (chờ duyệt)
- Tái phát: 0
```

Trường bắt buộc: `Ngày`, `Nguồn`, `Loại`, `Địa chỉ`, `Tiêu chí kiểm`, `Trạng thái`, `Tái phát`.
Trường thêm khi đã xử lý: `Phạm vi ảnh hưởng`, `Đã sửa`, `Cách kiểm`, `Gate`.
Trường tuỳ chọn: `Cập nhật:` (thêm dòng mới, không sửa dòng cũ), `Liên quan:` (`FB-003`, `UC-EVD-008`, `Bug 14`).

### Giá trị hợp lệ

`Loại`: `L1-sản phẩm` · `L2-rule` · `L3-checklist` · `L4-mẫu` · `L5-script` · `L6-tri thức` · `L7-trình bày`

`Trạng thái`: `Mới` · `Chưa rõ phạm vi` · `Đã sửa sản phẩm` · `Đã vào rule (chờ duyệt)` · `Đã duyệt` · `Đã có gate` · `Bị bác`

`Gate`: `chưa có` · `mức 1` · `mức 2 · <đường dẫn checklist>` · `mức 3 · <script + tên điều kiện>`

## 2. Bản ghi tái phát

Không tạo FB mới. Thêm vào FB cũ:

```markdown
- Cập nhật: 2026-10-05 · Tái phát lần 1 tại DM-L0002!TC_031. Nguyên nhân: rule đúng nhưng chỉ ở mức 1. Nâng lên mức 3 (rtm_check.py).
- Tái phát: 1
```

## 3. Dòng changelog khi sửa rule hoặc skill theo FB

Trong file bị sửa:

```markdown
| v0.2 | 2026-09-29 | Rule 7: mọi TC có bước phụ thuộc vai trò hoặc trạng thái dữ liệu phải ghi Pre-condition; kiểm bằng rtm_check.py. | FB-007 |
```

Bãi bỏ một rule vì FB:

```markdown
| v0.3 | 2026-10-02 | Bãi bỏ rule 4 cũ (bắt buộc đủ ba nhóm R/V/F cho mọi UC) — xung đột với format TC của khách hàng; thay bằng ánh xạ Classification I/II. | FB-011 |
```

## 4. Báo cáo cuối task (viết trong chat, không thành file)

```
FB: mở FB-012 (thiếu ca ký tự đặc biệt, L3) · áp dụng FB-007 và FB-009 · đã sửa 34 chỗ cùng lỗi với FB-007.
Chờ bạn duyệt: FB-007, FB-012.
```

## 5. Khung `feedback/log.md`

```markdown
# Sổ ghi nhớ góp ý

Quy tắc: `rules/feedback.md` · Quy trình: skill `feedback-loop` · Kiểm tra sổ: `fb_report.py`

| FB | Tiêu đề | Loại | Trạng thái | Tái phát |
|---|---|---|---|---|
| FB-001 | ... | L2-rule | Đã duyệt | 0 |

---

## FB-001 · ...
(các trường như mẫu ở mục 1)
```

Bảng đầu file là bảng tra nhanh; `fb_report.py --sync` kiểm bảng có khớp các bản ghi bên dưới không.
