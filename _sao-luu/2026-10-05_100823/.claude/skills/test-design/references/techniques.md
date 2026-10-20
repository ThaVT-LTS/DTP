# Kỹ thuật thiết kế test

Mục lục: §1 Phân vùng tương đương · §2 Giá trị biên · §3 Bảng quyết định · §4 Chuyển trạng thái · §5 Kịch bản use case · §6 Ma trận phân quyền · §7 Ma trận CRUD · §8 Pairwise · §9 Đoán lỗi · §10 Ma trận điều hướng · §11 Exploratory · §12 Tiêu chí phủ tối thiểu

Ví dụ dùng UC minh họa `UC-DEMO-001 · Tạo người dùng` trong `examples/`.

---

## §1 Phân vùng tương đương (Equivalence Partitioning — EP)

**Khi nào:** mọi trường nhập, mọi tham số đầu vào, cả đầu vào "ẩn" như vai trò người dùng hay trạng thái bản ghi.

**Cách làm:**
1. Chia miền giá trị thành các lớp mà hệ thống được kỳ vọng xử lý giống nhau trong cùng lớp.
2. Tách lớp hợp lệ và lớp không hợp lệ. Mỗi lý do bị từ chối là một lớp riêng (trống, quá ngắn, quá dài, sai ký tự, trùng...).
3. Chọn một giá trị đại diện cho mỗi lớp.
4. TC: gộp được nhiều lớp **hợp lệ** vào một TC; mỗi lớp **không hợp lệ** một TC riêng, các trường khác giữ giá trị hợp lệ.

**Ví dụ** — FD-01 "Họ và tên", 2–50 ký tự sau trim, chỉ chữ, khoảng trắng, `'`, `-`:

| ID | Lớp | Hợp lệ | Đại diện | Thông báo |
|---|---|---|---|---|
| UC-DEMO-001-EP-01 | 2–50 ký tự hợp lệ, có dấu | Có | "Nguyễn Thị Ánh" | — |
| UC-DEMO-001-EP-02 | Trống | Không | "" | MS-01 |
| UC-DEMO-001-EP-03 | Chỉ khoảng trắng | Không | "   " | MS-01 |
| UC-DEMO-001-EP-04 | Chứa số hoặc ký tự cấm | Không | "An3" | MS-03 |

**Tiêu chí phủ:** mỗi lớp có ít nhất một TC.

**Lỗi hay gặp:** gộp hai lớp không hợp lệ trong một TC (lỗi đầu che lỗi sau); quên các lớp "ẩn" như chỉ-khoảng-trắng, trùng sau trim, khác hoa thường.

## §2 Phân tích giá trị biên (Boundary Value Analysis — BVA)

**Khi nào:** mọi thứ có giới hạn — độ dài, khoảng số, ngày, dung lượng file, số lượng (tối đa 5 Admin, tối đa 1 Consultant active), phân trang.

**Cách làm:**
- Biên hai giá trị (mặc định): `min−1, min, max, max+1`.
- Biên ba giá trị (rule nhạy cảm, tiền, bảo mật): `min−1, min, min+1, max−1, max, max+1`.
- Biên của số lượng: 0, 1, giới hạn − 1, giới hạn, giới hạn + 1.
- Biên thời gian: hôm qua, hôm nay, ngày mai; 23:59:59 và 00:00:00; cuối tháng, năm nhuận; múi giờ.
- Xác định biên tính trước hay sau khi trim, theo ký tự hay theo byte.

**Ví dụ** — FD-01 độ dài 2–50:

| ID | Giá trị | Độ dài | Hợp lệ | Thông báo |
|---|---|---|---|---|
| UC-DEMO-001-BV-01 | "A" | 1 | Không | MS-02 |
| UC-DEMO-001-BV-02 | "An" | 2 | Có | — |
| UC-DEMO-001-BV-03 | 50 ký tự | 50 | Có | — |
| UC-DEMO-001-BV-04 | 51 ký tự | 51 | Không | MS-02 |

**Tiêu chí phủ:** mỗi giá trị biên một TC (giá trị biên hợp lệ có thể gộp khi cùng trường, cùng kết quả).

**Lỗi hay gặp:** chỉ thử max+1 mà quên min−1; thử biên trên UI nhưng quên API (khi tester được gọi API); quên biên của con số nằm trong business rule.

## §3 Bảng quyết định (Decision Table)

**Khi nào:** kết quả phụ thuộc vào tổ hợp nhiều điều kiện — rule nghiệp vụ, bắt buộc có điều kiện, quyền theo nhiều yếu tố.

**Cách làm:**
1. Liệt kê điều kiện (C1..Cn) và hành động (A1..Am).
2. Bảng đầy đủ có 2ⁿ cột với điều kiện đúng/sai. Gộp cột mà một điều kiện không ảnh hưởng kết quả bằng `–`.
3. Kiểm tra **đủ**: mọi tổ hợp đều rơi vào đúng một cột. Kiểm tra **nhất quán**: không có hai cột cùng điều kiện mà khác hành động. Tổ hợp nào test basis không nói kết quả → câu hỏi Q-T, không tự điền.
4. Mỗi cột một TC.

**Ví dụ** — DT-01 tạo người dùng:

| | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| C1 Email đã tồn tại trong tenant | N | N | N | Y | Y |
| C2 Người dùng trùng email đang Deactivated | – | – | – | N | Y |
| C3 Vai trò chọn là Admin | N | Y | Y | – | – |
| C4 Tenant đã có 5 Admin | – | N | Y | – | – |
| Tạo người dùng Invited, hiện MS-07 | X | X | | | |
| Từ chối, hiện MS-10 | | | X | | |
| Từ chối, hiện MS-06 | | | | X | |
| Không tạo, hiện MS-08 | | | | | X |

ID dòng: `UC-DEMO-001-DT-01-R1` … `-R5`.

**Tiêu chí phủ:** mỗi cột một TC.

**Lỗi hay gặp:** điều kiện không độc lập (C2 chỉ có nghĩa khi C1 = Y — phải gạch `–` đúng chỗ); bỏ sót tổ hợp mà tài liệu không nhắc tới.

## §4 Chuyển trạng thái (State Transition)

**Khi nào:** đối tượng có trạng thái — yêu cầu, review, bằng chứng, chứng nhận, tài khoản.

**Cách làm:**
1. Vẽ sơ đồ từ bảng ST trong test basis: trạng thái, sự kiện, ai được kích hoạt, điều kiện.
2. Lập bảng trạng thái × sự kiện; mỗi ô là "sang trạng thái X" hoặc "không hợp lệ".
3. TC:
   - mỗi chuyển hợp lệ một TC (phủ 0-switch);
   - mỗi ô không hợp lệ có rủi ro (hủy khi đã đóng, duyệt khi chưa gửi) một TC — kiểm nút không hiện; API bị từ chối thì kiểm ở sheet `API` khi tester được gọi API;
   - đúng chuyển nhưng sai vai trò một TC;
   - chuỗi hai bước quan trọng (1-switch) khi luồng quay vòng (trả về → gửi lại).

**Ví dụ** — tài khoản người dùng:

| Từ \ Sự kiện | Chấp nhận lời mời | Thu hồi lời mời | Vô hiệu hóa | Kích hoạt lại |
|---|---|---|---|---|
| Invited | Active (ST-USER-02) | Revoked (ST-USER-03) | không hợp lệ | không hợp lệ |
| Active | không hợp lệ | không hợp lệ | Deactivated (ST-USER-04) | không hợp lệ |
| Deactivated | không hợp lệ | không hợp lệ | không hợp lệ | Active (ST-USER-05) |
| Revoked | không hợp lệ (ST-USER-06) | không hợp lệ | không hợp lệ | không hợp lệ |

**Tiêu chí phủ:** 100% chuyển hợp lệ; mọi chuyển không hợp lệ mà test basis ghi phản ứng; mọi cặp (chuyển, vai trò không được phép) cho hành động ghi.

**Lỗi hay gặp:** chỉ test đường thẳng; quên trạng thái cuối (không còn đi đâu được); quên link cũ trong email khi trạng thái đã đổi.

## §5 Kịch bản use case (Use Case / Scenario Testing)

**Khi nào:** mọi UC có luồng.

**Cách làm:** luồng chính → một kịch bản Positive; mỗi AF → một kịch bản; mỗi EF → một kịch bản Abnormal. Kịch bản đi hết đến hậu điều kiện và kiểm tác động phụ (SE). Luồng nhiều bước thì thêm kịch bản dừng giữa chừng (back, refresh, hết phiên).

**Tiêu chí phủ:** 100% MF, AF, EF.

## §6 Ma trận phân quyền (Role / Permission Matrix)

**Khi nào:** mọi hệ thống có vai trò; đặc biệt hệ thống nhiều tenant, nhiều đơn vị, có phân công.

**Cách làm:**
1. Lấy bảng PM trong test basis: vai trò × hành động × phạm vi dữ liệu.
2. Thêm chiều ranh giới dữ liệu: của mình / cùng tenant khác scope / tenant khác / được phân công / không được phân công.
3. TC cho mỗi ô: "Có" → làm được; "Không" → UI ẩn hoặc tắt, mở thẳng URL bị chặn; khi tester được gọi API thì thêm TC API từ chối, không lộ dữ liệu trong response (sheet `API`).

**Tiêu chí phủ:** mọi dòng PM; dòng "Không" của hành động ghi dữ liệu kiểm giao diện và URL; kiểm API khi tester được gọi API.

**Lỗi hay gặp:** chỉ kiểm nút bị ẩn; quên đổi id trên URL (IDOR); khi tester được gọi API, quên response của API danh sách có lộ bản ghi ngoài quyền không.

## §7 Ma trận CRUD liên UC

**Khi nào:** nhiều UC cùng tạo/đọc/sửa/xóa một đối tượng.

**Cách làm:** bảng đối tượng × UC với C/R/U/D. Dùng để:
- tìm thao tác thiếu (đối tượng tạo được nhưng không sửa, không xóa được) → câu hỏi cho BA;
- sinh TC liên UC: sửa hoặc xóa ở UC này thì UC kia (danh sách, chi tiết, báo cáo) hiển thị đúng.

| Đối tượng | UC-DEMO-001 Tạo | UC-DEMO-002 Danh sách | UC-DEMO-003 Sửa | UC-DEMO-004 Vô hiệu hóa |
|---|---|---|---|---|
| Người dùng | C | R | U | U (trạng thái) |

**Tiêu chí phủ:** mỗi SE có TC; mỗi cặp (U hoặc D ở UC A, R ở UC B) có rủi ro có TC.

## §8 Pairwise (kết hợp từng cặp)

**Khi nào:** nhiều tham số **độc lập**, mỗi tham số nhiều giá trị, không thể thử hết tổ hợp — bộ lọc danh sách, cấu hình, trình duyệt × thiết bị × ngôn ngữ.

**Cách làm:** liệt kê tham số và giá trị; sinh bộ tổ hợp sao cho mọi cặp giá trị của hai tham số bất kỳ xuất hiện ít nhất một lần. Công cụ: PICT (Microsoft) hoặc `allpairspy` (Python). Vd 4 bộ lọc × 3 giá trị: 81 tổ hợp đầy đủ → khoảng 9–10 tổ hợp pairwise.

**Không dùng khi:** tham số phụ thuộc nhau — khi đó dùng bảng quyết định.

**ID:** `<UC>-PW-nn` cho mỗi tổ hợp.

## §9 Đoán lỗi (Error Guessing, checklist-based)

**Khi nào:** luôn luôn, sau các kỹ thuật trên, để bắt những thứ tài liệu không viết.

**Cách làm:** đi qua checklist Abnormal, các mục "hay lọt" trong `coverage-checklist.md` và checklist rủi ro ngoài nghiệp vụ `technical-risk-checklist.md` (khối lượng dữ liệu, chuỗi dài, điều hướng nhiều cấp, đồng thời, dữ liệu sau thao tác); mục nào áp dụng thì ghi `<UC>-EG-nn` trong file thiết kế và viết TC. Kết quả mong đợi của EG phải có nguồn (rule chung, quy ước chung trong test basis §1.5). Không có nguồn → câu hỏi Q-T.

**Ví dụ:** EG-01 bấm "Gửi lời mời" hai lần → chỉ một người dùng được tạo.

## §10 Ma trận điều hướng (cho Redirect)

**Cách làm:** bảng đường vào/ra (NV) × vai trò × trạng thái dữ liệu. Mỗi ô có kết quả khác nhau là một TC. Điền cả vai trò bị chặn.

| NV | Admin | Member | Chưa đăng nhập |
|---|---|---|---|
| NV-01 menu | vào form | không thấy menu | — |
| NV-02 URL /users/new | vào form | 403 | → đăng nhập → quay lại |

## §11 Exploratory — khi tài liệu chưa đủ

Kịch bản viết sẵn không bắt được mọi thứ. Với vùng rủi ro cao hoặc tài liệu mỏng, viết charter khám phá có thời hạn thay vì bịa TC:

```
Charter: Khám phá <vùng> với <dữ liệu / công cụ> để tìm <loại rủi ro>. Thời lượng: 60 phút.
```

Phát hiện từ exploratory → bug, hoặc câu hỏi cho BA, hoặc TC mới khi đã có nguồn.

## §12 Tiêu chí phủ tối thiểu (script `rtm_check.py` kiểm phần có ID)

| Đối tượng | Tối thiểu |
|---|---|
| Đường vào/ra NV | mỗi NV ≥ 1 TC; mỗi vai trò bị chặn ≥ 1 TC |
| Trường FD | mỗi lớp EP và mỗi giá trị BV ≥ 1 TC |
| Thông báo MS | mỗi MS xuất hiện trong ≥ 1 TC |
| Luồng MF / AF / EF | mỗi luồng ≥ 1 TC |
| Business rule BR | ≥ 1 TC Positive và ≥ 1 TC Negative |
| Bảng quyết định | mỗi cột ≥ 1 TC |
| Trạng thái ST | mỗi chuyển hợp lệ ≥ 1 TC; mỗi chuyển không hợp lệ được liệt kê ≥ 1 TC |
| Phân quyền PM | mỗi dòng ≥ 1 TC; dòng "Không" của hành động ghi: UI + URL, thêm API khi tester được gọi API |
| Tác động phụ SE | mỗi SE ≥ 1 TC |
