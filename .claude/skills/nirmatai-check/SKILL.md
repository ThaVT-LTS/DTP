---
name: nirmatai-check
description: Kiểm luồng Bulk → NirmatAI trên web test — chuẩn bị request, gửi (chỉ khi người dùng đồng ý), theo dõi trạng thái, ghi đủ mã để NirmatAI tra cứu, và các case biên từ Connection Guide. Dùng khi chạy case Bulk upload / Settings / Customers liên quan NirmatAI, khi NirmatAI (Usman) xin một lần chạy thật, hoặc khi người dùng hỏi một audit đã sang NirmatAI chưa.
---
# Kiểm tích hợp NirmatAI (v0.1)

Tuân thủ rule 32 của `rules/automation.md` (cùng rule 22, 23, 29, 31). Tài liệu: `DTP/dts-agent-workspace/docs/integrations/nirmatai/` (Connection Guide dev v4, OpenAPI).

## Thông số env dev (27/10/2026)

| Mục | Giá trị |
|---|---|
| NirmatAI org | 10 "Digital Trust Platform" |
| Standard | 107 `ISO27001-2022-DEMO-DTP`, 35 WP (DTP: framework NAI-107, nguồn NirmatAI, Activated) |
| Client của Development organisation | #63 "Development organisation" |
| Lần gửi mẫu | Bulk B → audit_id 486, `AUD-4391-00009`, 27/10 07:27Z, 4 file Ready sau khoảng 9 phút |

Dòng framework cùng tên nhưng nguồn **Imported** (Hanna_Framework_02) và NAI-108 đang Inactivated: không dùng.

## Các bước

1. **Ghi build** (Portainer, chỉ đọc). Giờ DTP hiển thị theo Đài Loan (UTC+8).
2. **Chuẩn bị (chỉ đọc + dữ liệu [QA])**: Bulk workspace có tài liệu đã map WP, request ở "Waiting for approval", framework Activated, client đã link. Chụp từng bước có URL.
3. **Dừng trước thao tác dùng chung**: link/đổi client, Approve and send, Sync, bật/tắt framework. Hỏi người dùng; chỉ làm khi có câu đồng ý rõ ràng. Hệ thống chặn thì nhờ người dùng tự bấm.
4. **Sau khi gửi (chỉ đọc)**: refresh tới khi các lượt gửi rời Queued/Sending; ghi trạng thái request, từng lượt gửi, từng file và "Processing in NirmatAI", màn khách hàng, audit log, chuông thông báo.
5. **Báo kết quả**: bảng ngắn + tin nhắn cho dev/Usman có `audit_code`, `audit_id`, client, org, standard, giờ tạo UTC, danh sách file + WP. Nhắc: `audit_code` là mã NirmatAI, mở ở `/prepare-audit?auditCode=…`.
6. **Điểm lạ chỉ thấy trên UI** ghi "cần xem", chưa log (rule 29: báo người dùng trước).

## Case biên nên có trong TC

Loại file không hỗ trợ · file > 100 MiB (upload session, ≤ 3 GiB) · trùng tên tài liệu trong audit · > 25 tài liệu một lần · đổi WP khi tài liệu đang xử lý · tài liệu xử lý lỗi (`failure`) · framework thuộc org khác · hiển thị giờ trả về từ NirmatAI (UTC không có múi giờ).
