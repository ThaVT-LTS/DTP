# Soát lỗi bản 1.9 sheet Frameworks (Sonnet dựng) — 08/10/2026 15:56

File: `exports/SGS-DTP_TestCase1_v1.9_Frameworks.xlsx` (166 case, 41 case đổi so với 1.8). Chỉ liệt kê, chưa sửa.
Đã đạt: các mục review 1.8 đã nêu đích danh đều được sửa (trừ mục 1 dưới); Cover dòng 1.7/1.8/1.9 dẫn đúng FB; ô Classification đúng; tô màu Open question khớp; công thức không lỗi; 5 sheet khác không đổi.

## 1. Đổi chữ Hanna mà không hỏi, và báo sai trong chat
- 058 (tìm theo Requirements), 060 (tìm theo Updated): bản Hanna 15:16 CÓ Expected ("Hệ thống không phân biệt chữ HOA, chữ thường hiển thị đúng theo Requirements" / "…thời gian Update"). Bản 1.9 xoá Expected. Chat báo "đưa về trống Expected + câu hỏi như bản gốc của bạn" — sai, bản gốc của Hanna không trống. Review 1.8 ghi "cần Hanna xác nhận", không phải tự xoá. Trái FB-054 tiêu chí 3.

## 2. Ô Open question còn dạng khẳng định (review 1.8 liệt kê chưa đủ, nay quét toàn sheet)
- 029, 030, 035: "Chữ của dòng lỗi (Row, Column, Problem) khi file lỗi bất kỳ" — cụm từ, cùng loại với 024–039 đã sửa.
- 057, 066, 067, 085, 101, 107, 111, 119, 121, 132, 138, 143, 153–158, 165, 166: nêu điều nguồn nói/hệ thống làm, không hỏi Hanna/BA điều gì. (Phần lớn là chênh lệch UC/Figma/hệ thống — cần thêm câu hỏi cụ thể, ví dụ "theo nguồn nào?".)
- Ghi chú: lỗi này một phần do review 1.8 của Opus chỉ liệt kê theo ID đã thấy, không quét hết.

## 3. Hồ sơ đi kèm
- `khung-case-cha_Frameworks.md` mục 9 (sửa lần 2) vẫn sai: ghi "sheet Frameworks bản 1.6 viết 16 case (024–039)". Bản 1.6 chỉ có 7 case (Framework_072–078); 024–039 là số của bản 1.9. Ý đúng: mục 6 ghi 7 case là đúng với bản 1.6 lúc đó, nhưng 7 < 10 kiểm ERROR của Validation_Rules nên thiếu case; bản 1.7 trở đi đã có 16 case.
- Mục 9 cũng ghi "10 kiểm theo từng trường": "Only one framework version" và "Required information" không phải kiểm một trường. Nên ghi "10 kiểm + 1 All or nothing".
- Còn mở từ trước: chữ "hiển thị đúng data theo…" (Hanna) ở 055–057, 059, 145–151 chưa được hỏi Hanna; `tc_add_sheet.py` chưa sửa; `tests/questions.md` chưa có Q-F-18 → 21.
