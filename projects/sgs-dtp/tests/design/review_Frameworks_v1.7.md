# Soát lỗi bản 1.7 sheet Frameworks (do Sonnet dựng) — 08/10/2026 15:34

File soát: `SGS-DTP_TestCase1_v1.7_Frameworks.xlsx` Hanna gửi 15:34. Nội dung 167 case trùng hoàn toàn bản Sonnet xuất 15:2x (so từng ô).
Chỉ liệt kê lỗi, chưa sửa file (chờ lệnh Hanna).

## 1. Định dạng
- Ô Classification đã gộp ở cột B, C, D: 61 ô không có xuống dòng, không căn giữa dọc, không căn trái (chữ bị che, vd "Nhập framework - Import framework", "Trùng mã và phiên bản"). Sheet Scopes các ô này đều có. Lỗi do script dựng sheet. (Comment Hanna 15:29)
- Framework_095 và Framework_123 trùng tên "Kiểm tra bấm mục trong cột điều hướng".

## 2. Cột Open question ghi ghi chú, không phải câu hỏi
Comment Hanna: đã có câu trả lời thì xoá câu hỏi. Nhiều ô chỉ ghi nguồn hoặc kết quả đã thấy, Expected đã viết theo đó:
- "Chưa bấm thử / chưa bấm Check file…": 045, 046, 050, 094, 107, 114, 115, 165.
- "Text lấy từ hệ thống…": 006, 021, 022, 023, 063, 148, 160, 164.
- Ghi kết quả hệ thống, không hỏi gì: 019, 020, 057, 059, 061, 062, 065, 080, 081, 149, 153.
- "Figma không có icon sắp xếp → Q-F-13": 078, 079, 082, 083.
- "Hanna thêm case." ở 057–060: ghi chú cho Hanna, không phải câu hỏi.

## 3. Báo cáo sai trong chat 15:2x
- Đã báo "giữ các case bạn thêm/sửa" nhưng Sonnet thay chữ ở các case Hanna đã sửa: tìm kiếm (Hanna 011, 012), không có kết quả (Hanna 013: bỏ dòng "Dòng đếm không đổi"), xoá chữ tìm (Hanna 014: thay Expected), tìm và lọc requirement (Hanna 044–050), Import new version (Hanna 054), Download template (Hanna 007: bỏ "(không nền)"). Không báo Hanna.
- Cover dòng 1.7 ghi tham chiếu FB-054 nhưng log không có FB-054 (chỉ cập nhật FB-053).
- Q-F-18, Q-F-19, Q-F-20, Q-F-21 được dùng ở nhiều case nhưng chưa có trong `tests/questions.md` hay khung.

## 4. Khẳng định chưa kiểm chứng (FB-042)
- 029, 030, 035: Problem lấy theo dạng câu của prototype nhưng đổi mã (R.9.4.2, R.9.9, R.4; prototype là R.8.4.2, 8.9, 8.4), căn cứ ghi TP FG. Câu 030 "does not exist in this sheet." chưa đối chiếu đủ câu trên hệ thống.
- 040, 044, 050: dùng file bcm-2019.xlsx — prototype chỉ báo lỗi vì tên file có "bcm", không đọc nội dung; Step ghi 3 lỗi với mã khác prototype.
- 019 (chọn file thứ hai thì thay file cũ), 020 (hiện "20.0 MB"), 016 ("180 KB", dấu tích xanh), 063 ("Bảng và dòng phân trang ẩn"), 146 ("Nhóm không có requirement khớp bị ẩn"), 136 (bấm ô Requirements mở phần Requirements): không có ghi nhận đã thấy trên hệ thống.

## 5. Mâu thuẫn trong case
- 131, 133, 098: Expected khẳng định "Total to meet tier cao nhất bằng số Requirements" trong khi Q-F-10 ở chính case đó nghi ngờ điều này (Figma 79 so với 76).
- 134 khẳng định số requirement khi lọc tier bằng New at this tier (lọc theo nhãn riêng), nhưng 150, 151 để trống Expected chờ đúng câu hỏi đó (Q-F-12).
- 129–131: Pre là framework có 3 tier tổng quát nhưng Step ghi cố định tên Basic/Medium/High (TISAX dùng Normal/High/Very high). Nên ghi theo Rank.
- 061 "Chữ hoa" trùng ý dòng "Không phân biệt chữ hoa, chữ thường" đã thêm vào 055, 056, 057, 059.

## 6. Việc chưa làm như đã nêu
- `khung-case-cha_Frameworks.md` chưa sửa (Q-F-06, 08, 11, 13).
