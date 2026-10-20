// ------------------------------------------------------------------ guide
function addGuide(wb) {
  const g = wb.addWorksheet('Hướng dẫn', { views: [{ showGridLines: false }] });
  g.getColumn(1).width = 3; g.getColumn(2).width = 26; g.getColumn(3).width = 120;
  let r = 2;
  g.mergeCells(r, 2, r, 3); g.getCell(r, 2).value = 'SGS DTP — Test case E2E Phase 1 · Wave 1';
  g.getCell(r, 2).style = { font: F({ bold: true, size: 15, color: { argb: C.white } }), fill: fill(C.navy), alignment: { vertical: 'middle', indent: 1 } }; g.getRow(r).height = 30; r += 2;
  const section = t => { g.mergeCells(r, 2, r, 3); g.getCell(r, 2).value = t; g.getCell(r, 2).style = { font: F({ bold: true, color: { argb: C.white } }), fill: fill('FF2F5597'), alignment: { vertical: 'middle', indent: 1 } }; g.getRow(r).height = 20; r++; };
  const row = (k, v, style) => {
    const a = g.getCell(r, 2), b = g.getCell(r, 3); a.value = k; b.value = v;
    a.style = style || { font: F({ bold: true }), fill: fill(C.grey), border: BOX, alignment: { vertical: 'top', wrapText: true, indent: 1 } };
    b.style = { font: F(), border: BOX, alignment: { vertical: 'top', wrapText: true } }; g.getRow(r).height = Math.max(18, lines(v, 125) * 14 + 4); r++;
  };
  section('E2E là gì');
  row('Định nghĩa', 'Một case E2E chạy trọn MỘT luồng nghiệp vụ qua nhiều màn hình và nhiều vai trò; dữ liệu bước trước dùng cho bước sau.\nCase màn hình (file SGS-DTP_TestCase_Phase1) kiểm chi tiết từng màn; case E2E chỉ kiểm các màn NỐI VỚI NHAU đúng không: dữ liệu mang sang, quyền thay đổi, email / thông báo tới đúng người, trạng thái chuyển đúng, có ghi vết.');
  row('Mã case', 'E2E<wave>_<số thứ tự>. Ví dụ E2E1_012 = Wave 1, luồng thứ 12.');
  row('Phạm vi', 'Wave 1 theo SGS_DTP_Detailed_Plan_v3.0. Một luồng Wave 1 có thể đi qua UC mà Plan xếp ở wave sau (vd Home / CKP, Audit log / AUD, thông báo / NTF). Các bước đó vẫn giữ trong kịch bản và ghi Pending cho tới khi tới wave đó.');
  section('Cách đọc một sheet case');
  row('Đầu sheet', 'Thông tin case (mục tiêu, vai trò, pre-condition, dữ liệu test, UC kèm trạng thái Plan, môi trường chạy), Kết quả case và Sơ đồ luồng (mỗi bước một dòng; bấm tên bước để nhảy tới bước đó).');
  row('Mỗi bước — 3 ảnh', '① Figma · Màn thao tác: khung ĐỎ ①②③ là chỗ cần nhập / bấm.\n(A) Figma · Kết quả mong đợi: màn sau khi thao tác; khung XANH (A)(B)(C) là chỗ cần kiểm tra. Nếu Figma chưa có màn đó, ô ảnh ghi "Figma chưa có màn này".\nẢnh thực tế: chụp từ app khi chạy.');
  row('Mỗi bước — bảng đối chiếu', 'Mỗi dòng là MỘT kết quả mong đợi: Kết quả mong đợi · UC (kèm trạng thái Plan) · Thực tế · Kết quả · Ghi chú. Kết quả bước tự tính từ các dòng; Kết quả case tự tính từ các bước.');
  row('Ảnh Figma', 'Lấy từ Figma DTP P1 (bản 14/10/2026). Khi ảnh dùng dữ liệu mẫu khác, ô "Lưu ý" ghi rõ — so theo bố cục và câu chữ.');
  section('Kết quả');
  const RD = [
    ['Passed', 'Đúng như kết quả mong đợi.'],
    ['Failed', 'Chức năng có nhưng sai so với kết quả mong đợi / Figma (sai chữ, thiếu thành phần, link thay vì nút, sai số liệu, sai trạng thái…). Áp dụng khi UC đã Done / In progress / Blocked theo Plan.'],
    ['Blocked', 'Plan ghi UC Done nhưng bản chạy chưa có màn / chức năng để kiểm.'],
    ['Pending', 'UC chưa Done theo Plan (Not started, hoặc thuộc wave sau): chưa làm nên chưa kiểm, KHÔNG tính lỗi. Nếu chức năng đã có và chạy đúng thì vẫn ghi Passed.'],
    ['NA', 'Không áp dụng cho lần chạy này.'],
  ];
  for (const [k, v] of RD) row(k, v, { font: F({ bold: true, color: { argb: RES[k].font } }), fill: fill(RES[k].fill), border: BOX, alignment: { vertical: 'top', indent: 1 } });
  row('Thứ tự ưu tiên', 'Kết quả bước / case = mức nặng nhất trong các dòng: Failed > Blocked > Pending > Passed. Tester có thể sửa Result từng dòng (danh sách chọn); kết quả bước và case tự cập nhật.');
  section('Màu theo vai trò');
  const RT = { 'SGS Admin': 'Nhân viên SGS quản trị · Operations Console', 'Customer Admin': 'Quản trị phía khách hàng · Customer Portal', 'Customer User': 'Người dùng phía khách hàng · Customer Portal', 'Customer Viewer': 'Người chỉ xem phía khách hàng · Customer Portal', Consultant: 'Consultant · Consultant Portal / Customer Portal', 'Người được mời': 'Người nhận lời mời, chưa kích hoạt · Hộp thư, trang kích hoạt', 'Hệ thống': 'Việc hệ thống tự làm (job, quét malware, đồng bộ)' };
  for (const [k, c] of ROLE) row(k, RT[k], { font: F({ bold: true, color: { argb: C.white } }), fill: fill(c), border: BOX, alignment: { vertical: 'top', indent: 1 } });
  section('Môi trường & dữ liệu dùng chung');
  row('Lần chạy này', 'Local (máy QC): web + backend dev, Postgres / Mailpit trên Docker, đăng nhập dev (mật khẩu chung). DB seed lại 19/10/2026. Code: CORP-BA-DTP main (commit 4be5d13, 15/10/2026).');
  row('Hộp thư test', 'Mailpit của môi trường test (local: http://localhost:8025).');
  row('Dữ liệu dùng chung', 'SGS Admin Lin Mei (SGS Taiwan) · khách hàng Hsinchu AI Labs / 新竹人工智慧實驗室股份有限公司 · Customer Admin 張雅婷 · Customer User Kevin Wu · Customer Viewer Iris Huang · tenant khác Formosa Payments Ltd. (Kevin Lin). Khi chạy tự động, tên / email có thêm hậu tố để mỗi lần chạy là dữ liệu mới; dữ liệu tiền đề mà màn hình chưa hỗ trợ được tạo qua DB và ghi ở "Ghi chú khi chạy".');
  row('Thứ tự chạy', 'Theo sheet Danh sách E2E; luồng sau dùng dữ liệu luồng trước tạo (ghi ở Pre-condition).');
}
