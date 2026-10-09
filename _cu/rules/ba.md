---
paths:
  - "projects/*/docs/**"
---
# Rule BA
(Gộp từ rule BA đã chốt trong chat Business Analysis, 28/09–01/10/2026.)

1. **Nhãn nguồn.** Mọi thông tin gắn `[UC: vị trí]`, `[SUY LUẬN: dữ kiện A + dữ kiện B]`, `[GIẢ ĐỊNH]` hoặc `[ĐỀ XUẤT]`. Không có nguồn thì không viết như sự thật.
2. **Không tự trả lời câu hỏi làm rõ.** Câu mức CHẶN chưa trả lời → dừng, không bàn giao sang Test/Auto. Câu mức QUAN TRỌNG/NHỎ → làm tiếp, gắn `[GIẢ ĐỊNH]`.
3. **ID cho mọi phần tử:** `UC03-MF-10` (luồng chính), `UC03-AF-4a` (nhánh rẽ), `UC03-EF-01` (ngoại lệ), `BR-12` (quy tắc), `M03-…` (màn hình/phần tử giao diện). Đánh số bước cách quãng (10, 20, 30…) để chèn bước mới mà không vỡ ID và tag.
4. **Text hiển thị và thông báo lỗi trích nguyên văn**, không diễn giải. Không có text chính xác → câu hỏi CHẶN, không tự bịa.
5. **Đề xuất** không được đưa vào baseline hay test khi chưa được duyệt.
6. **Baseline chỉ đổi khi con người duyệt.** Mỗi lần đổi tăng version (v1.0 → v1.1) và ghi changelog. Bản chưa duyệt là v0.x, `status: draft`.
7. **Hình, sơ đồ, bảng không đọc được** → liệt kê ra, không im lặng bỏ qua.
8. **Ghi ra file ngay khi xong mỗi UC**, không để trôi trong chat.
9. **Mỗi khi nhận tài liệu**, móc nối các dữ kiện để nêu đánh giá mục đích của sản phẩm (bước 0 của skill `ba-analysis`).
10. **Đính chính công khai** khi phát hiện kết luận trước đó sai; không sửa âm thầm.
