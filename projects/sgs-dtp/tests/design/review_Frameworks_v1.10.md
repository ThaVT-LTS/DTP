# Soát lỗi bản 1.10 sheet Frameworks (Sonnet dựng) — 08/10/2026 16:04

File: `exports/SGS-DTP_TestCase1_v1.10_Frameworks.xlsx` (166 case, 92 case có câu hỏi, 10 case trống Expected). Chỉ liệt kê, chưa sửa.
Đã đạt: 058/060 đã trả đúng chữ Hanna (khớp file 15:16); 23 ô review 1.9 nêu đã thành câu hỏi; Cover có đủ dòng 1.6 → 1.10, cột G đúng FB; ô Classification căn đúng (498 ô); công thức không lỗi; 5 sheet khác không đổi; khung case cha mục 9 đã sửa số case; fb_report 0 lỗi.

## 1. Câu hỏi mới viết sai nguồn (FB-042)
- 057: "…hay chỉ tìm theo mã và tên như UC?" — UC v4 FWK-01 không nói gì về ô tìm kiếm. "Search code or name" là chữ placeholder của Figma/hệ thống, không phải UC.

## 2. Ô Open question vẫn còn dạng khẳng định (review 1.9 chỉ quét các ô đã nêu, chưa quét hết sheet)
Chỉ nêu điều nguồn ghi hoặc hệ thống làm, không hỏi gì:
- 011, 015: UC ghi EN/ZH, file mẫu ver 1 không có Tiers → chưa hỏi "dùng file mẫu nào?"
- 040, 044 (vế đầu): "Prototype chỉ báo 3 lỗi này khi tên file có chữ bcm…"
- 047, 051: liệt kê UC và Figma khác nhau, chưa hỏi theo bên nào
- 064: "Hệ thống không bỏ khoảng trắng…"
- 076: liệt kê Hanna / hệ thống / Figma, chưa hỏi thứ tự đúng là gì
- 102, 120, 123: "UC không nêu…", "UC FWK-03 cho cập nhật…", "UC FWK-02 có applicability settings…"
- 108: "Chưa có bản nháp không tier để xem; mã nguồn prototype: bỏ dòng về tier"
- 128, 129: "Công thức suy ra từ…"
- 134: "Nhóm gọi là Dimensions, Clauses hay Chapters tuỳ framework"
- 149: khẳng định, trong khi 150 cùng nội dung đã là câu hỏi → hai case lệch nhau
Câu hỏi có nhưng khó hiểu:
- 109: "Màn báo gì chưa có" (thiếu chủ ngữ, không rõ hỏi gì)
- 020, 041, 052, 087: là câu hỏi nhưng không có dấu "?" (không thống nhất với các ô khác)
Lệch chữ nhỏ: 029, 030, 035 ghi "các cột Row, Column, Problem", 13 case cùng cụm 024–039 ghi "cột Row, Column, Problem".

## 3. 058, 060: Expected của Hanna khác cách hệ thống đang tìm
- Prototype đã kiểm: ô tìm khớp mã, tên, version, issuer, status; không khớp số Requirements, thời gian Updated. Expected "hiển thị đúng theo Requirements / thời gian Update" sẽ Fail trên prototype. Ô Open question trống nên case đọc như đã kiểm xong.
- Sonnet đã hỏi Hanna trong chat (đúng như review 1.9) nhưng không nói cho Hanna biết điểm lệch này. Trong bảng phẳng, cột căn cứ ghi "HT Hanna-15:16" — đây là chữ Hanna, không phải bằng chứng hệ thống (HT).

## 4. Báo sai trong chat và trong FB-056
- Chat và FB-056 ghi "viết lại 26 ô Open question". Thực tế 23 ô (029, 030, 035, 057, 066, 067, 085, 101, 107, 111, 119, 121, 132, 138, 143, 153–158, 165, 166); 058/060 là xoá câu hỏi, không phải viết lại.
- Câu trong chat "bản 1.6 chỉ có 7 case lỗi file (72–78), nhiều hơn một chút trong bản 1.7 trở đi là 16 case" sai ngữ pháp, đọc ra nghĩa ngược. Mục 9 trong file thì đúng.

## 5. Còn mở từ trước (không phải lỗi mới)
- Chữ "hiển thị đúng data theo…" của Hanna ở 055–057, 059, 145–151: đã hỏi trong chat, chờ Hanna.
- `tc_add_sheet.py` trong thư mục dự án chưa sửa (căn lề Classification, `--change` một dòng). Bản sửa chỉ có ở scratchpad.
- FB-048/051 (A/B), Q-F-10.


## 6. Bổ sung sau khi có `tc_check.py` mới (08/10 16:2x)
Quét bằng script (cảnh báo "Open question có phần không phải câu hỏi"): 36 ô, nhiều hơn danh sách ở mục 2 (mục 2 đọc bằng mắt nên sót các ô có một phần là câu hỏi, phần còn lại không). Danh sách đầy đủ theo No.: 011 015 020 040 041 044 045 047 048 051 052 064 074 076 084 087 097 102 103 104 106 108 109 113 116 120 123 127 128 129 130 131 133 134 135 149 
Vòng sửa kế tiếp lấy danh sách này làm chuẩn; xong khi lệnh `tc_check.py ... --sheets Frameworks` không còn cảnh báo loại này.
