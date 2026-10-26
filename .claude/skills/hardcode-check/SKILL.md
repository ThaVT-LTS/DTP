---
name: hardcode-check
description: Quét code đang deploy tìm giá trị gán cứng (dropdown chỉ tải N mục, hằng số nghiệp vụ lệch UC, ID / tên tổ chức / URL viết thẳng, text không qua i18n, bộ lọc mặc định ẩn dữ liệu) rồi biến thành case TC và bug. Dùng trước mỗi lượt chạy TC, khi có build mới, hoặc khi người dùng thấy dữ liệu "bị thiếu" trên một màn.
---
# Quét giá trị gán cứng (v0.1 — [ĐỀ XUẤT], chờ duyệt)

Tuân thủ rule 30 của `rules/automation.md`, mẫu lỗi 12–13 của `rules/bug-patterns.md`, rule 28 (đối chiếu quyết định mới nhất trước khi ghi bug).

Nguồn gốc: 26/10 dropdown Scope của "Create Bulk workspace" chỉ lấy 100 scope đầu (`limit: 100`, không tìm kiếm, không phân trang) → BU-BUG-20.

## 1. Chọn đúng code

- Repo app (SGS DTP): `C:\Users\thavt\Documents\DTP\CORP-BA-DTP`. **Không sửa, không checkout / pull** working tree (có thể đang chạy local). Chỉ `git fetch` rồi đọc `origin/main`:
  `git -C <repo> fetch -q origin` · `git -C <repo> grep -n <mẫu> origin/main -- <thư mục>` · `git -C <repo> show origin/main:<file>`.
- **Quét đúng commit đang deploy**, không mặc định `origin/main`. Repo có 2 remote: `origin` (Azure) và `gitlab` (nguồn deploy). Lấy commit build trên web (tag image Portainer, hoặc build ghi trong ticket QA gần nhất, vd `72246de8`) rồi đọc thẳng `git show <commit>:<file>`. 26/10: quét nhầm `origin/main` Azure (cũ hơn ở phần Bulk) nên báo sai 25 MB / 500 file, trong khi build deploy đúng 20 file / 100 MB.
- Trước khi đề xuất bug: tìm trong `DTP/dts-agent-workspace/tasks/tickets` (mã QA, tiêu đề) và Azure DevOps (WIQL theo từ khoá tiêu đề; PAT ở `C:/Users/thavt/.azdo-pat`, không in ra). Đã có thì chỉ đề xuất bổ sung màn vào bug cũ.
- Ghi vào báo cáo: commit đã quét (`git log -1 --format='%h %ad' origin/main`) và commit đang deploy trên web (tag image Portainer). Khác nhau thì nói rõ.

## 2. Mẫu cần quét

| Nhóm | Mẫu grep (gợi ý) | Hỏi gì |
|---|---|---|
| A. Danh sách / dropdown cắt cứng | `limit: ?[0-9]{2,}`, `pageSize`, `slice\(0,`, `take:` trong `apps/web/src` | Màn nào dùng? Có ô tìm kiếm (`q:`) hoặc phân trang không? Backend cho tối đa bao nhiêu (`max(` trong schema list)? |
| B. Hằng số nghiệp vụ | `MB`, `1024 \* 1024`, `maxFiles`, `days`, `months`, `hours`, `cron`, `setInterval`, `refetchInterval`, `expires`, `ttl`, `retry` trong web + `apps/backend/src` + `packages` | So với bảng giá trị UC ở mục 3; lệch là lỗi |
| C. Dữ liệu viết thẳng | `SGS Taiwan`, `@sgs`, `https?://`, uuid cố định, `tenantId =`, `affiliateId =`, tên chuẩn / tier / role viết tay | Có cần lấy từ API / cấu hình không? Khách khác hay affiliate khác có bị sai không? |
| D. Text không qua i18n | chuỗi tiếng Anh trong JSX ngoài `t(…)`, email template viết thẳng | Đổi sang 繁體中文 có còn tiếng Anh không? |
| E. Bộ lọc mặc định ẩn dữ liệu | `status: "ACTIVE"`, `mode: "ASSISTED"`, `sort:` cố định | Người dùng có cách nào thấy phần bị lọc không? Có đúng UC không? |
| F. Múi giờ / định dạng | `UTC`, `toISOString`, `Asia/Taipei`, `en-US` | "Ngày làm việc", hạn, giờ hiển thị có theo giờ Đài Loan (UTC+8) không? (mẫu lỗi 8) |

Quét rộng nên dùng 2 agent Explore song song (web / backend), mỗi agent báo `file:dòng · đoạn code · màn bị ảnh hưởng · giá trị · khớp / lệch UC · mức độ`.

## 3. Bảng giá trị UC để so (UC v6.0, cập nhật khi UC đổi)

| Quy tắc | Giá trị | Nguồn |
|---|---|---|
| Upload một lần (Assisted, Bulk) | ≤ 20 file, mỗi file ≤ 100 MB | D63, EVA-03, BLK-01 |
| Trùng tên file Bulk | bản mới → `_v2`, tài liệu khác → `(2)` | D38, BLK-01 |
| File certificate | 1 PDF, ≤ 10 MB, quét malware | D49, CRT-05 |
| Sửa / xoá certificate | trong 7 ngày kể từ khi tạo | D62, CRT-04/07 |
| Tag "Expires in X days" | trong 90 ngày trước ngày hết hạn, cấu hình được | D48, CRT-06 |
| Certification cycle mặc định | 3 năm | D11, WSP-01 |
| Link mời | dùng 1 lần, hết hạn sau 7 ngày | USR-03 (Figma 9:11509) |
| Retention | xoá 36 tháng sau archive; evidence chưa map xoá 36 tháng sau upload; báo Customer Admin trước 30 ngày | D60, RET-01..04 |
| Consulting request nguồn SGS | nhắc sau 3 ngày làm việc; khách được huỷ sau 5 ngày làm việc | D57, SRQ-06 |
| Audit log | tìm được trong 2 năm; không export CSV ở P1 | D64 |
| Bulk audit request | poll NirmatAI mỗi 6 giờ + nút Check now; gửi lỗi có retry | BAR-05, BAR-06 |
| Import framework | trả tối đa 200 issue; content_version phải cao hơn | US-017 |

## 4. Biến kết quả thành việc

1. Lập bảng: `chỗ (file:dòng) → màn / route → giá trị → khớp hay lệch UC → người dùng bị ảnh hưởng thế nào → mức độ`. Cao = người dùng không tới được dữ liệu hoặc quy tắc sai.
2. Đối chiếu rule 28: user story đã sửa, decision log, ticket có chủ đích của dev. Đúng quyết định mới hơn thì không phải bug.
3. Mỗi chỗ còn lệch → thêm case vào đúng sheet của file TC (`DTP\dts-agent-workspace\tests\cases\SGS-DTP_TestCase_v0.4_Phase1.xlsx`), Expected theo UC. **Không đánh dấu "chờ dữ liệu"**: tạo đủ dữ liệu để kiểm (vd > 100 scope) hoặc hỏi người dùng trước nếu phải tạo nhiều dữ liệu trên môi trường dùng chung `dtp.ltsgroup.tech`.
   Mỗi dòng lúc này là **nghi ngờ** (rule 31). Case kích hoạt ghi rõ cách lộ lỗi: tạo đúng dữ liệu (> 100 scope, file 30 MB, > 50 evidence), test biên / thời gian (00:00–08:00 giờ Đài Loan), hoặc **gọi thẳng API** khi UI đang chặn (UI chặn mà API nhận vẫn là lỗi thật).
4. Kiểm trên web, chụp ảnh có URL (Failed thì ảnh bắt buộc). Không tái hiện được → ghi **tiềm ẩn** trong báo cáo cho dev, không tính là bug, không log.
5. Có bug: **báo người dùng trước**, rồi log tiếng Anh (ticket ở dts-agent-workspace → Azure, gán theo PIC trong Plan), thêm dòng vào `rules/bug-patterns.md` nếu là mẫu mới.
6. Câu trả lời cho người dùng: ngắn, nêu commit đã quét, chỗ nào Cao trước.
