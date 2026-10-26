---
name: run-cycle
description: Quy trình một lượt chạy test trên web có tìm lỗi chủ động — ghi build, kiểm môi trường, quét code lấy danh sách nghi ngờ, chạy TC kèm case kích hoạt, phân loại lỗi code / lỗi môi trường / tiềm ẩn. Dùng khi bắt đầu một lượt chạy (Round N), khi có build mới, hoặc khi người dùng yêu cầu "tìm thêm lỗi ngoài TC".
---
# Lượt chạy có tìm lỗi chủ động (v0.1 — [ĐỀ XUẤT], chờ duyệt)

Tuân thủ rule 31 của `rules/automation.md` (cùng rule 22, 28, 29, 30). Skill con: `hardcode-check` (quét code), `manual-run` (chạy TC, ghi kết quả), `bug-evidence` (file bằng chứng).

## Vì sao

TC chỉ viết theo UC sẽ bỏ sót lỗi chỉ lộ ra khi có dữ liệu, thời điểm hoặc cách gọi đặc biệt. Ví dụ 26/10: dropdown Scope chỉ lấy 100 mục (BU-BUG-20 / SC-BUG-07). Lỗi này chỉ thấy khi tổ chức có hơn 100 scope.

## Bốn hướng tìm lỗi

| Cách tìm | Ví dụ |
|---|---|
| **Quét code** tìm giới hạn, hằng số, text viết cứng, rồi so với UC (skill `hardcode-check`) | `limit 100`, 25 MB, 500 file, "SGS Taiwan" |
| **Tạo đúng dữ liệu** để lỗi lộ ra trên web | hơn 100 scope, file 30 MB, hơn 50 evidence |
| **Test biên và thời gian**: số lượng lớn, file lớn, khung 00:00–08:00 giờ Đài Loan | lỗi ngày tính theo UTC |
| **Gọi thẳng API** những gì giao diện đang chặn | UI chặn 21 file nhưng API nhận 500. Vẫn là lỗi thật vì người khác có thể gọi API trực tiếp |

Gọi API chỉ trên môi trường test, bằng tài khoản test, không dùng tài khoản thật của khách. Tạo nhiều dữ liệu trên môi trường dùng chung (`dtp.ltsgroup.tech`) thì hỏi người dùng trước; dữ liệu có tiền tố `[QA]` và hậu tố riêng (rule 23).

## Ba trạng thái của một phát hiện

1. **Nghi ngờ**: tìm được bằng 4 hướng trên, chưa thấy trên web. Viết ngay **case TC kèm dữ liệu để kích hoạt** (Pre-condition ghi rõ cách tạo dữ liệu, giờ chạy, lệnh gọi API). Không đánh dấu "chờ dữ liệu".
2. **Lỗi**: chạy case trên web thấy lỗi → báo người dùng trước, rồi log (tiếng Anh, rule 29).
3. **Tiềm ẩn**: không tái hiện được trên web (vd build deploy đã khác code, cần điều kiện không tạo được). Ghi vào báo cáo cho dev xem, **không tính là bug**, không log Azure.

## Quy trình mỗi lượt

1. **Ghi build và commit đang deploy** (tag image Portainer, hoặc build ghi trong ticket QA gần nhất). Quét đúng commit đó, không mặc định `origin/main` (repo có remote `origin` Azure và `gitlab`).
2. **Kiểm môi trường**: biến cấu hình (vd `NAI_ENABLED`, `SCANNER_DRIVER`, `EMAIL_DRIVER`, `CERTIFICATE_TIME_ZONE`), migration đã chạy, dịch vụ ngoài (mail, scanner, NirmatAI) là thật hay giả. Không đọc được thì hỏi dev / devops.
3. **Quét code** lấy danh sách nghi ngờ (skill `hardcode-check`). Đối chiếu `DTP/dts-agent-workspace/tasks/tickets` và Azure để không trùng bug đã có; đã có thì chỉ đề xuất bổ sung màn vào bug cũ.
4. **Chạy TC trên web**, kèm các case kích hoạt nghi ngờ (skill `manual-run`). Ảnh có URL; Failed bắt buộc có ảnh.
5. **Phân loại kết quả**:
   - **Lỗi code** → gán dev theo PIC trong Plan.
   - **Lỗi môi trường hoặc deploy** (cấu hình sai, migration thiếu, dịch vụ ngoài hỏng) → gán devops; case không ghi Failed, chạy lại khi môi trường đã sửa.
   - **Tiềm ẩn** → chưa log, ghi vào báo cáo.

## Báo cáo cuối lượt

Ngắn, theo thứ tự: build / commit đã chạy · số case Passed / Failed / Blocked / Pending · lỗi code (mã bug, mức) · lỗi môi trường · danh sách tiềm ẩn cho dev. Không nêu bug khi người dùng chưa duyệt.
