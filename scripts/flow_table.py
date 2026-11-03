"""Bảng luồng hoạt động theo mẫu QA lead 03/11: Ở đâu (Portal) · Ai làm (Vai trò | Tên) · Làm gì · Kết quả (Trạng thái của 2 bên)."""
import sys
import openpyxl
from openpyxl.styles import Alignment, Font, Border, Side, PatternFill

thin = Side(style='thin', color='000000')
BD = Border(left=thin, right=thin, top=thin, bottom=thin)
CENTER = Alignment(horizontal='center', vertical='center', wrap_text=True)
LEFT = Alignment(horizontal='left', vertical='center', wrap_text=True)


def sheet(wb, title, caption, side_x, side_y, groups):
    """groups: [(portal, [(role, name, [(làm gì, trạng thái x, trạng thái y), ...]), ...]), ...]"""
    ws = wb.create_sheet(title)
    ws['A1'] = 'Ở đâu'; ws.merge_cells('A1:A2')
    ws['B1'] = 'Ai làm'; ws.merge_cells('B1:C2')
    ws['D1'] = 'Làm gì'; ws.merge_cells('D1:D2')
    ws['E1'] = 'Kết quả'; ws.merge_cells('E1:F1')
    ws['E2'] = 'Trạng thái của ' + side_x
    ws['F2'] = 'Trạng thái của ' + side_y
    for r in (1, 2):
        for c in range(1, 7):
            cell = ws.cell(r, c); cell.font = Font(bold=True); cell.alignment = CENTER; cell.border = BD
    r = 3
    for portal, roles in groups:
        p0 = r
        for role, name, acts in roles:
            acts = acts or [('—', '', '')]
            r0 = r
            for act, sx, sy in acts:
                ws.cell(r, 4, act); ws.cell(r, 5, sx); ws.cell(r, 6, sy)
                r += 1
            ws.cell(r0, 2, role); ws.cell(r0, 3, name)
            if r - 1 > r0:
                ws.merge_cells(start_row=r0, start_column=2, end_row=r - 1, end_column=2)
                ws.merge_cells(start_row=r0, start_column=3, end_row=r - 1, end_column=3)
        ws.cell(p0, 1, portal)
        if r - 1 > p0:
            ws.merge_cells(start_row=p0, start_column=1, end_row=r - 1, end_column=1)
    for row in ws.iter_rows(min_row=3, max_row=r - 1, max_col=6):
        for c in row:
            c.border = BD
            c.alignment = LEFT if c.column in (2, 3, 4, 5, 6) else CENTER
    ws.cell(r + 1, 1, caption).font = Font(italic=True, color='555555')
    for col, w in zip('ABCDEF', (18, 22, 24, 62, 30, 30)):
        ws.column_dimensions[col].width = w
    return ws


def template(path):
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    sheet(wb, 'Mẫu', 'Mẫu bảng luồng hoạt động (QA lead 03/11). Mỗi dòng Làm gì đánh số bước theo thứ tự chạy; bên không tham gia ghi —.', 'xx', 'yy',
          [('Customer Portal', [('Customer Admin', 'Kevin Lin', [('1. Tạo Service Request', '', ''), ('', '', '')]),
                                ('Customer Consultant', '[QA] M22 M2 Ian Chang', [('', '', ''), ('', '', '')])]),
           ('SGS Portal', [('SGS Admin', 'Lin Mei', [('', '', ''), ('', '', '')]),
                           ('SGS Consultant', 'Chen Wei', [('', '', ''), ('', '', '')])])])
    wb.save(path)


def consultant(path):
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    A = 'Customer Portal'; S = 'SGS Portal'
    sheet(wb, '1. Marketplace (Chen Wei)',
          'Request SR-2026-069 (Gap Analysis, [QA] W9 R4 ISO 22301:2012). Bước 1–4 đã chạy trên web 03/11 (build 6de6673f/ce2ea1d2); bước 5–7 chưa chạy. Lý do (Decline, Close negotiation, Terminate…) tối đa 250 ký tự — web còn 1.000 (IS-BUG-06).',
          'Kevin Lin (Customer Portal)', 'Chen Wei (SGS Portal)',
          [(A, [('Customer Admin', 'Kevin Lin', [
              ('1. Marketplace › View consultants › Chen Wei › View profile › Start a request → chọn Gap Analysis, workspace [QA] W9 R4 ISO 22301:2012, nhập mô tả → Send', 'Submitted', 'Submitted (có Accept / Decline)'),
              ('4. Service Requests › SR-2026-069 › Grant Workspace Access & Start', 'In progress', 'In progress (có Review workspace)'),
              ('7. Service Requests › SR-2026-069 › Confirm completion (hoặc Decline completion + lý do → vẫn In progress)', 'Completed', 'Completed (hết quyền xem workspace)')]),
                ('Customer Consultant', '[QA] M22 M2 Ian Chang', [('— (không tham gia luồng này)', '', '')])]),
           (S, [('SGS Admin', 'Lin Mei', [
               ('Requests › Service Requests › SR-2026-069: chỉ xem; Reassign consultant + lý do (khi cần đổi consultant)', 'không đổi', 'không đổi; consultant mới xin quyền lại')]),
                ('SGS Consultant', 'Chen Wei', [
                    ('2. Assigned to me › SR-2026-069 › Accept (hoặc Decline + lý do → Closed)', 'In discussion', 'In discussion'),
                    ('3. Assigned to me › SR-2026-069 › Ready to start (hoặc Close negotiation + lý do → Closed)', 'Ready to start (có Grant)', 'Ready to start'),
                    ('5. Assigned to me › SR-2026-069 › khối Deliverable › Upload deliverable', 'In progress (thấy deliverable)', 'In progress'),
                    ('6. Assigned to me › SR-2026-069 › Request completion (chưa có deliverable thì bị chặn: "Upload the deliverable first")', 'In progress (có Confirm / Decline completion)', 'In progress (chờ khách)')])])])
    sheet(wb, '2. My consultants (Ian Chang)',
          'Request SR-2026-063 (Gap Analysis, Hanna workspace 002). Theo UC v6.4 D98: gửi xong là Ready to start, không có Accept. Web hiện vào thẳng In progress (IS-BUG-04) nên bước 2 bị bỏ qua. Bước 3–5 chưa chạy.',
          'Kevin Lin (Customer Admin)', 'Ian Chang (Customer Consultant)',
          [(A, [('Customer Admin', 'Kevin Lin', [
              ('1. Service Requests › New request → Gap Analysis, workspace → Consultant: My consultants › [QA] M22 M2 Ian Chang, tick xác nhận hợp đồng → Send', 'Ready to start — web: In progress ❌ (IS-BUG-04)', 'Ready to start — web: In progress ❌'),
              ('2. Service Requests › request › Grant Workspace Access & Start', 'In progress — web: bỏ qua bước này ❌', 'In progress (có Review workspace)'),
              ('5. Service Requests › request › Confirm completion (hoặc Decline completion + lý do)', 'Completed', 'Completed')]),
                ('Customer Consultant', '[QA] M22 M2 Ian Chang', [
                    ('3. Assigned to me › SR-2026-063 › khối Deliverable › Upload deliverable', 'In progress', 'In progress'),
                    ('4. Assigned to me › SR-2026-063 › Request completion', 'In progress (có Confirm / Decline completion)', 'In progress (chờ khách)')])]),
           (S, [('SGS Admin', 'Lin Mei', [('Requests › Service Requests › SR-2026-063: chỉ xem (web còn nút Reassign — IS-BUG-07, câu hỏi BA)', 'không đổi', 'không đổi')]),
                ('SGS Consultant', 'Chen Wei', [('— (không tham gia luồng này)', '', '')])])])
    wb.save(path)


if __name__ == '__main__':
    template(sys.argv[1]); consultant(sys.argv[2]); print('ok')
