# Xếp loại nhận xét — L1 đến L7

Mỗi FB đúng **một** loại: loại quyết định sửa ở đâu và gate mức nào. Nhận xét có vẻ thuộc hai loại thì tách thành hai FB.

| Loại | Nhận xét kiểu gì | Sửa ở đâu | Gate tối thiểu | Có sinh rule? |
|---|---|---|---|---|
| `L1-sản phẩm` | Sai ở đúng một chỗ, không phải vấn đề cách làm: một TC ghi sai màn hình, một ID gõ sai, một con số lệch | Chính sản phẩm đó | Không | Không |
| `L2-rule` | Nguyên tắc làm việc: "TC nào cũng phải có pre-condition", "đừng tự đặt kết quả mong đợi khi spec không nói" | `rules/*.md` | Checklist hoặc script | Có |
| `L3-checklist` | Thiếu một điểm cần soát: "còn thiếu case nhập ký tự đặc biệt", "chưa thử quay lại bằng nút Back" | `references/*checklist*.md` | Mục bắt buộc trong checklist | Không (bổ sung mục) |
| `L4-mẫu` | Định dạng, bố cục, cột, cách đặt ID, thứ tự trường của đầu ra | `references/templates.md`, `tc-framework.md` | Script kiểm định dạng | Không (sửa mẫu) |
| `L5-script` | Việc kiểm thủ công nên để máy làm; hoặc script kiểm sai, bỏ sót | `scripts/*.py` | Chính script + ca kiểm cho script | Không |
| `L6-tri thức` | Sự thật về dự án: nghiệp vụ, thuật ngữ, vai trò, quyết định đã chốt, môi trường, dữ liệu master | `docs/` (glossary, baseline, test basis) | Trích dẫn nguồn khi dùng | Không |
| `L7-trình bày` | Cách AI giao tiếp: ngôn ngữ, độ dài, mức chi tiết, thứ tự trình bày, không hỏi lại quá nhiều | `rules/common.md` mục trình bày | Văn xuôi (chấp nhận được) | Có |

## Cách nhận biết nhanh

Đặt ba câu hỏi theo thứ tự:

1. **Lỗi này còn ở chỗ nào khác không?** Không → `L1`. Có → đi tiếp.
2. **Máy kiểm được không?** Được → `L4` nếu là định dạng, `L5` nếu cần viết/sửa script, còn lại `L2` với gate script.
3. **Đây là "phải làm gì" hay "đừng quên gì"?** Phải làm → `L2`. Đừng quên → `L3`.

Nhận xét là một **sự thật về dự án** chứ không phải cách làm → `L6`. Nhận xét về **cách nói chuyện của AI** → `L7`.

## Mức gate và khi nào phải nâng

| Mức | Hình thức | Điểm yếu |
|---|---|---|
| 1 | Câu văn trong rule | Phụ thuộc AI có đọc và có hiểu đúng |
| 2 | Mục bắt buộc trong checklist, có ô đánh dấu | Phụ thuộc AI có chạy checklist trung thực |
| 3 | Điều kiện trong script, mã thoát ≠ 0 khi vi phạm | Chỉ kiểm được cái đo được |

Quy tắc nâng mức (`rules/feedback.md` rule 11): tái phát 1 lần → nâng một mức. Việc đo được bằng máy thì không được dừng ở mức 1.

Ví dụ những việc **phải** ở mức 3: trường bắt buộc rỗng; ID sai định dạng hoặc trùng; TC không trỏ tới ID nào trong test basis; UC thiếu một trong ba nhóm R/V/F; kết quả mong đợi chứa từ mơ hồ ("bình thường", "đúng", "thành công") mà không nói thấy gì; tổng số liệu trong báo cáo lệch với dữ liệu nguồn.

## Nhận xét xung đột với rule đang có

Không sửa lặng lẽ và không bỏ qua. Ghi vào FB: rule nào, mâu thuẫn ở đâu, hai lựa chọn và hệ quả từng lựa chọn; hỏi người dùng chọn; `Trạng thái: Chưa rõ phạm vi` cho tới khi có trả lời. Sau khi chọn: rule bị bỏ được đánh dấu bãi bỏ trong changelog kèm `FB-nnn`, không xoá dòng cũ.
