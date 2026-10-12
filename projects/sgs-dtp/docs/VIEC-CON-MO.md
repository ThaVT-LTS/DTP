
## 2026-10-08 15:16 · Sheet Frameworks bản 1.7
- Đã dựng bản 1.7 (167 case) trên file Hanna sửa; chờ Hanna duyệt công thức Total to meet (Q-F-10) và chốt A/B của FB-048.
- Chưa làm: sửa `khung-case-cha_Frameworks.md` (Q-F-06, 08, 11, 13); thêm Q-F-18 → Q-F-21 vào `tests/questions.md`.
- Case tìm theo Requirements / Updated để trống Expected: chưa kiểm được trên prototype (phải đăng nhập lại).

## 2026-10-08 · Frameworks bản 1.10
- Hỏi Hanna: Expected ở Framework_058 (tìm theo Requirements) và 060 (tìm theo Updated) là chữ của Hanna, đã giữ; Hanna đã kiểm trên hệ thống chưa (prototype chỉ tìm theo mã, tên, version, issuer, status)?
- Hỏi Hanna: chữ "hiển thị đúng data theo…" ở 055–057, 059, 145–151 có muốn viết cụ thể hơn không (giữ nguyên chữ Hanna).
- Còn mở: `tc_add_sheet.py` trong thư mục dự án chưa đặt căn lề ô Classification; chọn A/B của FB-048/FB-051; Q-F-10 (Total to meet).



## Module 07 Evidence – Assisted mode (09/10, FB-066)
- Chưa đọc sheet **Changes vs Source** của UC v5.3 (rule 36): đọc trước lần viết sheet kế tiếp của module 07.
- Chưa có case cho UC D43 (người mất quyền vào scope thì requirement, evidence họ sở hữu được giao lại hoặc bỏ trống): cần case ở sheet Users hoặc Scopes; chờ Hanna chọn sheet.
- Chưa có case cho nút Request certification ở chi tiết workspace và UC WSP-03 “Request support”: chờ Hanna chọn sheet.
- Q-EA-01 → 48 (`tests/design/cau-hoi_Assisted-workspace.md`): chờ Hanna chọn câu nào lên sheet Cần xác nhận.
- Mã UC: sheet Assisted workspace dùng 2 chữ số (UC-EVA-01), sheet cũ 3 chữ số (UC-WSP-002): chờ Hanna chọn một kiểu.
- `tests/design/bo-cuc-sheet_uc-v4.md` vẫn là bố cục UC v4; cần viết lại theo UC v5.3 (module 06, 07 đã tách sheet Workspaces, Assisted workspace).
