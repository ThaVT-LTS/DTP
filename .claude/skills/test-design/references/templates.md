# Template — Tester

Mục lục: §1 file thiết kế · §2 test case · §3 câu hỏi Q-T · §4 RTM · §5 báo cáo bàn giao · §6 ánh xạ sang Playwright

---

## §1 File thiết kế — `tests/design/<UC-ID>.md`

```markdown
# Thiết kế test — UC-XXX-nnn · <tên>

| | |
|---|---|
| Test basis | docs/test-basis/<tên>.v<x.y>.md |
| Ngày | YYYY-MM-DD |
| Trạng thái | Nháp / Đã tự review / Đã review độc lập |

## 1. Bản đồ kiểm thử
| ID nguồn | Nội dung tóm tắt | Nhóm | Kỹ thuật | Ưu tiên |
|---|---|---|---|---|

## 2. Redirect — ma trận điều hướng
| NV | <vai trò 1> | <vai trò 2> | Chưa đăng nhập |
|---|---|---|---|

## 3. Validation — phân vùng và biên theo trường
### UC-XXX-nnn-FD-01 · <nhãn>
| ID | Lớp / giá trị | Hợp lệ | Giá trị test | Kết quả (MS) |
|---|---|---|---|---|

## 4. Function
### 4.1 Kịch bản (MF / AF / EF)
### 4.2 Bảng quyết định UC-XXX-nnn-DT-01 · <rule>
### 4.3 Chuyển trạng thái (ST liên quan)
### 4.4 Phân quyền (PM liên quan) — thêm chiều ranh giới dữ liệu
### 4.5 Tác động phụ và CRUD liên UC
### 4.6 Đoán lỗi
| ID | Tình huống | Kết quả mong đợi | Nguồn của kết quả |
|---|---|---|---|

## 5. Loại trừ và câu hỏi
- ST-XXX-nn [THUỘC UC-XXX-nnn] — phủ ở UC đó
- UC-XXX-nnn-FD-04 [CHỜ Q-T-03] — chưa có độ dài tối đa
```

Không ghi cột "TC" trong bảng thiết kế — mối liên kết nằm ở trường `Nguồn` của TC, và `tests/rtm.md` do script sinh. Một nguồn sự thật, không lệch.

Dấu loại trừ script hiểu được (đặt trên cùng dòng, sau ID): `[NGOÀI PHẠM VI]`, `[CHỜ Q-nn]`, `[CHỜ Q-T-nn]`, `[THUỘC UC-...]`, `[KHÔNG ÁP DỤNG]`. Nhóm không áp dụng cho cả UC: một dòng có ID UC và dấu, vd `- UC-XXX-nnn [KHÔNG ÁP DỤNG: Validation — màn hình chỉ xem]`.

## §2 Test case — `tests/cases/<module>.md`

Cấu trúc: `##` UC → `###` nhóm (I. Redirect, II. Validation, III. Function) → `####` TC. Mỗi TC một khối, mỗi trường một dòng, đúng tên trường — script đọc theo mẫu này.

```markdown
## UC-XXX-nnn · <tên UC>

### I. Redirect
#### UC-XXX-nnn-TC-R01 · ...

### II. Validation
#### UC-XXX-nnn-TC-V03 · Họ và tên 1 ký tự bị từ chối
- Nhóm: Validation
- Loại: Negative
- Ưu tiên: P2
- Kỹ thuật: BVA
- Nguồn: UC-XXX-nnn-FD-01, UC-XXX-nnn-BV-01, UC-XXX-nnn-MS-02
- Tiền điều kiện: Đăng nhập Admin của tenant T1; đang ở màn hình "Tạo người dùng"
- Dữ liệu: Họ và tên = "A"; Email = v03@demo.test; Vai trò = Member
- Bước: 1) Nhập dữ liệu; 2) Bấm "Gửi lời mời"
- Mong đợi: Dưới trường "Họ và tên" hiện "Họ và tên từ 2 đến 50 ký tự."; không tạo người dùng; vẫn ở màn hình "Tạo người dùng"
- Tag: @UC-XXX-nnn @validation @negative @P2
- Tự động hóa: Có
```

| Trường | Bắt buộc | Giá trị |
|---|---|---|
| Nhóm | Có | Redirect / Validation / Function — khớp chữ R/V/F trong ID |
| Loại | Có | Positive / Negative / Abnormal |
| Ưu tiên | Có | P1 / P2 / P3 |
| Kỹ thuật | Có | EP, BVA, Bảng quyết định, Chuyển trạng thái, Kịch bản, Phân quyền, CRUD, Pairwise, Đoán lỗi, Điều hướng |
| Nguồn | Có | Các ID được phủ, cách nhau bởi dấu phẩy |
| Tiền điều kiện | Có | Vai trò, tenant, dữ liệu, trạng thái, màn hình đang đứng |
| Dữ liệu | Khi có nhập | Giá trị cụ thể, không ghi "dữ liệu hợp lệ" |
| Bước | Có | `1) ...; 2) ...` trên một dòng |
| Mong đợi | Có | Text nguyên văn, URL/màn hình, trạng thái, dữ liệu thay đổi — ngăn cách bằng `;` |
| Tag | Có | `@<UC-ID> @<nhóm> @<loại> @P<n>` (+ `@smoke`, `@bug-<mã>`) |
| Tự động hóa | Có | Có / Không — <lý do> |
| Trạng thái | Khi đổi | `Sửa ở v<x.y>` / `Deprecated ở v<x.y>` |

Viết `Mong đợi` sao cho người khác chạy tay và AI viết Playwright đều ra cùng một assertion. Tránh: "hiển thị đúng", "hoạt động bình thường", "thành công", "như mong đợi".

## §3 Câu hỏi gửi BA — `tests/questions.md`

```markdown
### Q-T-03 · <tiêu đề>
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở
- **Vị trí:** docs/test-basis/<tên>.v1.0.md · UC-XXX-nnn-FD-04
- **Vấn đề:** chưa có độ dài tối đa của trường "Mô tả".
- **Ảnh hưởng:** không lập được giá trị biên, thiếu 2 TC.
- **Đề xuất mặc định:** 500 ký tự.
- **Trả lời:**
```

## §4 RTM — `tests/rtm.md`

Do `scripts/rtm_check.py` sinh; không sửa tay. Gồm: tóm tắt độ phủ, lỗ hổng, rule thiếu TC Positive/Negative, UC thiếu nhóm, vấn đề định dạng TC, bảng ID → TC theo UC, danh sách loại trừ. Script trả mã lỗi khác 0 khi còn lỗ hổng — dùng được trong CI.

## §5 Báo cáo bàn giao — `tests/design-report.md`

```markdown
# Báo cáo thiết kế test — <module> v<x.y>

| | |
|---|---|
| Test basis | docs/test-basis/<tên>.v<x.y>.md |
| Bộ test | tests/cases/<module>.md — <n> TC |
| RTM | tests/rtm.md — <n> ID, 0 lỗ hổng, <n> loại trừ |

## Số lượng
| UC | Redirect | Validation | Function | Positive | Negative | Abnormal | P1 | P2 | P3 |
|---|---|---|---|---|---|---|---|---|---|

## Bộ smoke (@smoke)
## Không tự động hóa được — lý do
## Dữ liệu và môi trường cần chuẩn bị
## Câu hỏi Q-T còn mở và giả định đang dùng
## Rủi ro còn lại (chưa có TC, cần exploratory)
```

## §6 Ánh xạ sang Playwright (cho bước Code)

| Từ TC | Sang Playwright |
|---|---|
| ID + tiêu đề | `test('UC-XXX-nnn-TC-V03 · Họ và tên 1 ký tự bị từ chối', ...)` |
| Tag + ID trong Nguồn | `{ tag: ['@UC-XXX-nnn', '@validation', '@negative', '@P2', '@UC-XXX-nnn-FD-01'] }` |
| Nhãn trường trong FD | `page.getByLabel('Họ và tên')` |
| Tên nút trong Bước | `page.getByRole('button', { name: 'Gửi lời mời' })` |
| Text trong Mong đợi | `await expect(page.getByText('Họ và tên từ 2 đến 50 ký tự.')).toBeVisible()` |
| URL trong NV | `await expect(page).toHaveURL(/\/users\/new$/)` |
| "gọi API thẳng bị từ chối" | `const res = await request.post('/api/users', { data }); expect(res.status()).toBe(403)` |
| Tiền điều kiện | fixture đăng nhập theo vai trò + dữ liệu tạo qua API trong `beforeEach` |

Chạy theo phạm vi: `npx playwright test --grep @UC-XXX-nnn`, `--grep @smoke`; kết hợp hai tag (VÀ) bằng lookahead: `--grep "(?=.*@P1)(?=.*@negative)"`.

## §7 File phân tích case cha con (khi người dùng không cần TC)

Dùng khi người dùng yêu cầu "phân tích chi tiết theo kiểu case cha con, dễ nhìn, dễ hiểu" thay cho viết TC (FB-026). Ví dụ đã làm: `projects/quan-ly-tai-lieu/tests/design/Tao_thu_muc_phan_tich_case_cha_con.xlsx`.

**File Excel, các sheet:** `Case cha con` · `Thông báo` (text nguyên văn) · `Quy tắc` · `Còn mở`.

**Sheet `Case cha con`:** khối đầu ghi tên chức năng, nguồn (trả lời nào, ngày nào) và dòng đếm theo trạng thái bằng công thức. Cột:

| Cột | Nội dung |
|---|---|
| ID | `<số cha>.<số con>`, vd `2.4` |
| Case cha | Gộp ô theo nhóm; dòng đầu ghi tên nhóm và một dòng mô tả ngắn |
| Case con | Tên ngắn nói đúng cái đang kiểm |
| Điều kiện / Dữ liệu | Trạng thái và **giá trị cụ thể** để nhập |
| Thao tác | Một thao tác |
| Kết quả mong đợi | Quan sát được, text nguyên văn; chưa có căn cứ thì ghi "Ghi lại hệ thống làm gì" |
| Căn cứ | ID yêu cầu (AC, BR, MSG), câu hỏi và trả lời, ảnh |
| Trạng thái | `Đã chốt` (người dùng đã xác nhận) · `Theo mặc định` (đề xuất của AI, người dùng chưa trả lời) · `Suy ra` (AI suy ra từ quy tắc đã chốt) · `Còn mở` (chưa có căn cứ) |

**Cách chia nhóm cha** (theo thứ tự người đọc hiểu): mở hộp thoại → nhập và đếm → kiểm khi bấm Lưu → thành công → trùng → giới hạn → đóng → sau khi tạo → lỗi → ngoài phạm vi (ghi để biết). Mỗi nhóm cha phải đi qua `technical-risk-checklist.md` (đặc biệt biên của con số, dán chuỗi dài, tên dài, nhiều cấp).

Case con `Còn mở` không được tự đặt kết quả; ghi vào sheet `Còn mở` kèm câu hỏi.
