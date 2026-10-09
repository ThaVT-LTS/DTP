# Soát lỗi bản 1.8 sheet Frameworks (Sonnet dựng) — 08/10/2026 15:41

File: `exports/SGS-DTP_TestCase1_v1.8_Frameworks.xlsx` (166 case). Chỉ liệt kê, chưa sửa (chờ lệnh Hanna).
Đã đạt: ô Classification B, C, D căn đúng; 5 sheet khác không đổi; công thức không lỗi; hai case trùng tên đã đổi.

## 1. Câu hỏi đã có trả lời / chỉ là ghi chú — còn sót (báo "đã xoá" nhưng mới xoá một phần)
- "Chưa bấm thử / chưa bấm Check file…": 045, 046, 050, 093, 106, 113, 114, 164 — giữ nguyên như bản 1.7 dù review 1.7 đã liệt kê.
- Câu khẳng định, không hỏi: 013, 014 (Hệ thống ghi tên file…), 043, 105, 112 (Thiết kế không ghi; hệ thống đóng hộp thoại ngay), 077, 083, 086, 088, 089, 099, 125, 142.
- 024–028, 031–034, 036–039: "Chữ ở cột Row, Column, Problem → Q-F-14" là cụm từ, không thành câu hỏi.
- 150 (Chọn High) chép nguyên câu của 149: "(Medium chỉ hiện requirement From Medium)".

## 2. Khôi phục chữ Hanna nhưng làm mất câu hỏi / sinh khẳng định chưa kiểm
- 058 (tìm theo Requirements), 060 (tìm theo Updated): Expected "hiển thị đúng theo …", câu hỏi bị xoá; hệ thống chưa kiểm được (FB-042). Cần Hanna xác nhận đã kiểm hay để câu hỏi.
- 055–060: dòng "không phân biệt chữ HOA, chữ thường" ở case tìm theo số Requirements và hh:mm không có nghĩa.
- 055–060, 145–151: Expected "hiển thị đúng data theo …" không nói thấy gì để Pass/Fail. Là chữ của Hanna — hỏi Hanna có muốn viết cụ thể không, không tự đổi.

## 3. Mâu thuẫn
- 055 hỏi "Dòng đếm có đổi theo kết quả không" (Q-F-12), còn 062 (không có kết quả) khẳng định "Dòng đếm không đổi", không có câu hỏi.
- 130: Step 4 "So với số Requirements ở khối Content" còn, nhưng Expected đã bỏ dòng so sánh → bước không có kết quả.
- 129: Step đổi sang Rank nhưng Expected còn "(Total to meet của Basic + New at this tier của Medium)".
- 128–130: Pre ghi "From tier Rank 2" — nhãn thật trên màn là "From <tên tier>", câu khó đọc.

## 4. Hồ sơ đi kèm
- Cover dòng 1.7 ghi tham chiếu FB-054, nhưng FB-054 mới lập ở bản 1.8 cho lỗi của 1.7.
- `khung-case-cha_Frameworks.md` mục 9 (Sonnet thêm) ghi sai: mục 6 của khung không nói "không có WARNING" (đã ghi Validation_Rules có ERROR, WARNING, INFO); lỗi thật ở mục 6 là "7 case lấy từ Validation_Rules" trong khi sheet có 11 dòng ERROR (10 kiểm + All or nothing). Mục 9 ghi "chỉ có 10 kiểm ERROR" cũng chưa khớp.
- Chưa làm (Sonnet đã báo): sửa `tc_add_sheet.py` cho ô Classification; thêm Q-F-18 → Q-F-21 vào `tests/questions.md`.
