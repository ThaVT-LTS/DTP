# Soát lỗi bản 1.11 sheet Workspaces (Sonnet dựng) — 09/10/2026 11:00

File: `exports/SGS-DTP_TestCase1_v1.11_Workspaces.xlsx` (35 case, 15 case có câu hỏi, 5 case trống Expected). Opus chỉ liệt kê. Hanna ra lệnh "làm lại" lúc 11:08 → Sonnet sửa ở bản 1.12 (FB-063).
Đã đạt: sheet đặt cạnh Frameworks, tên sheet đúng tên menu; TVP_ID Workspaces_001 → 035; Cover có dòng 1.11 đúng chỗ (trước Annotation), giữ đủ 1.0 → 1.10; Test_Report có 9 dòng cho Workspaces; tc_check 0 lỗi; số liệu báo trong chat (35 / 15 / 5, Q-W-02 → 11) khớp file; không có case tạo workspace, Change tier (đúng ý Hanna ở Q-W-01); chữ giao diện ở 001, 004, 007, 012, 015, 028–031 khớp prototype.

## 1. Chưa đọc Figma mà vẫn coi Expected như đã có căn cứ (rule 1, 2, 13; tiêu chí FB-060)
- Figma trang 05 Workspace & Evidence chưa mở. 20 case có Expected chỉ dựa trên prototype và không có câu hỏi: 001, 002, 004, 006, 007, 009, 013, 014, 015, 016 (Expected), 018, 021–024, 028–031, 034, 035. Rule 1: không lấy hành vi prototype làm Expected; rule 13: Expected chưa kiểm chứng phải kèm câu hỏi. Cần đọc Figma trước, hoặc hỏi Hanna có chấp nhận cách "Expected theo prototype" cho sheet này không.
- Reference ở đầu sheet ghi "UC v5.3 WSP-01…06" nhưng sheet chỉ phủ WSP-02 (danh sách), ROL-001; ghi thừa phạm vi.

## 2. Giá trị tính toán: Expected viết như đã biết logic trong khi 020 còn hỏi logic (rule 31)
- 020 hỏi "x, n nghĩa là gì?" (Q-W-07) nhưng 021–024 đã điền Expected theo đúng cách hiểu đó, không có câu hỏi → mâu thuẫn trong cùng nhóm.
- Cách làm tròn: 021 (63.79 → 64) và 022 (19.35 → 19) giả định làm tròn thường. Trên hệ thống chỉ thấy một số thật (ISO 42001: 8/76 = 10.53% → 11%), không phân biệt được làm tròn thường với làm tròn lên. 022 cần câu hỏi (ở Scopes Hanna gắn Q-S-11 cho cả nhóm Coverage).
- Pre-condition không dựng được: n = 31, 8, 250 không phải số requirement của framework/tier nào đang có (đã thấy 44, 61, 76, 116, 52, 70, 78). Tester không tạo được workspace có 31 hay 250 requirement. Nên chọn n theo tier có thật, hoặc hỏi cách dựng dữ liệu.
- Chưa ghi logic vào khung case cha trước khi viết (rule 31, gạch 1): khung chỉ có Q-W-07, không có mục "mỗi con số nghĩa là gì, cách tính, đã thử trên số thật".

## 3. Expected không quan sát được hoặc gộp nhiều loại (rule 9, 12)
- 003: "Chuyển sang màn chi tiết của [Workspace]" không nói thấy gì. Hệ thống có tiêu đề `<framework> · <version> · <tier>`, dòng phụ `<scope> · <loại> scope`, URL `/workspaces/ws-…`.
- 010: "Hệ thống hiển thị data đúng định dạng" là chữ bị cấm ở rule 12. Thêm nữa, trên hệ thống Sonnet thử **chữ thường** ("tisax"), không thử chữ hoa; case tên "Chữ hoa" chưa được kiểm.
- 016: gộp ba loại scope (Organization, System, Product) vào một Expected; rule 9 yêu cầu mỗi loại một case. `<framework>` không rõ: danh sách hiện tên ngắn (TISAX · ISA 6.0, Appendix 10 · 2022), không phải tên đầy đủ ở hộp thoại (Security Baselines for ICT Systems (Appendix 10)).
- 017: gộp hai cách hiển thị tier khác nhau (TISAX "Very high" không có chữ Hán; Appendix 10 "Basic · 普" có) vào một Expected "ví dụ …". "Tier đã chọn khi tạo" là suy ra: sau Change tier cột này hiện tier mới, không phải tier lúc tạo.
- 028: mẫu "Dòng 1–<n> of <n> items" sai khi n > 10 (ví dụ ngay sau đó là 1–10 of 15).
- 032: Expected "kể cả scope Customer Admin chưa được gán riêng" nhưng Pre không dựng điều kiện chưa gán → Pre và Expected không khớp.

## 4. Câu hỏi đặt sai chỗ, sai nguồn, sai cách nối (rule 23)
- Q-W-06 (Archive/Delete ở đâu) gắn vào 005 "Không có nút tạo"; Q-W-05 (gắn lại version đã link) gắn vào 016 "Cột Workspace"; Q-W-02 (bộ lọc) gắn vào 019 "Cột Status"; Q-W-04 (đổi tier ở đâu) gắn vào 017. Câu trả lời không làm đổi Expected của case đang mang câu hỏi → ô Open question không còn là "điều cần quyết cho dòng này".
- 012 dùng lại Q-S-07 cho "Figma có trạng thái không có kết quả không?" — Q-S-07 hỏi về Figma trang Scopes; trang Workspaces là màn khác, Hanna trả lời Q-S-07 không tự trả lời cho Workspaces. Tương tự 008, 010 (hành vi dòng đếm, hoa thường của ô tìm Workspaces). Nên là câu Q-W riêng, hoặc ghi rõ "áp chung câu trả lời Q-S-07?".
- 016, 019: hai câu hỏi trong một ô nối bằng xuống dòng; rule 23 nối bằng `;`.

## 5. Thiếu case
- Trạng thái rỗng (tổ chức chưa có workspace nào) — rule 4 đặt ngay sau mở màn.
- Sắp xếp cột: chưa kiểm cột có sắp xếp được không (sheet Frameworks có mũi tên sắp xếp ở 4 cột); không có case cũng không có câu hỏi.
- Phân quyền: chỉ có Customer Admin và Customer User; sheet Scopes có thêm Customer Viewer, vai trò SGS (được phân công / không được phân công). Customer Viewer chỉ có trong câu hỏi của 033.
- Bảo mật 035: Scopes cùng loại case có câu hỏi "Hiện trang gì? → Q-S-26"; ở đây Expected chỉ ghi "Không hiển thị dữ liệu", chưa hỏi trang hiện ra là gì.
- Quay lại từ chi tiết workspace về danh sách (nút mũi tên đã thấy trên màn chi tiết).

## 6. Hồ sơ đi kèm lệch với file (rule 35)
- `khung-case-cha_Workspaces.md`: dòng đầu ghi "Đã dựng: 35 case" nhưng mục 4 vẫn liệt kê khối "Tạo workspace từ Scope", "Đổi tier", "Archive và Delete" như thuộc sheet; không có khối Phân trang, Bảo mật, nhóm số coverage mà sheet đã có. Mục 5 vẫn ghi WSP-01, WSP-03 ở sheet này.
- Cover dòng 1.11 ghi "case còn câu hỏi Q-W để trống Expected": thực tế 10 case có câu hỏi vẫn có Expected, và 3 trong 5 case trống mang Q-S-11 chứ không phải Q-W.
- FB-062 ghi trạng thái "Đã vào rule (chờ duyệt)" nhưng không có rule, skill nào được sửa; đúng phải là "Đã sửa sản phẩm".
- Cột UC: cả 33 case danh sách ghi `UC-WSP-002`, kể cả 003 (mở chi tiết); mã này chưa đối chiếu với UC v5.3 (Sonnet đã tự nêu trong chat).

## 7. Q-W-12 → Q-W-15 chưa có chỗ
Bốn câu về hộp thoại Link a framework không nằm ở ô nào, chỉ nằm trong chat và khung. Cần Hanna quyết: thêm vào Open question của các case Gắn framework ở sheet Scopes (chạm chữ của Hanna, rule 34) hay ghi vào sheet `Cần xác nhận`.
