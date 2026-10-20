// Review report of the Wave 1 test cases (read-only review; the test case workbook is NOT modified).
// usage: node build-report.js <out.xlsx>
const ExcelJS = require('exceljs');
const fs = require('fs');
const path = require('path');
const OUT = process.argv[2];
const R = __dirname;
const SHEETS = ['Login', 'Users', 'Customers', 'Frameworks', 'Scopes', 'Workspaces', 'Workspace detail', 'Documents', 'Profile', 'Notifications', 'Audit Logs'];
const VERDICTS = ['Xoá', 'Sửa', 'Lệch web', 'Wave sau', 'OK'];
const VC = { 'Xoá': ['FFFFC7CE', 'FF9C0006'], 'Sửa': ['FFFFEB9C', 'FF9C5700'], 'Lệch web': ['FFF4B183', 'FF833C0B'], 'Wave sau': ['FFD9E1F2', 'FF1F3864'], 'OK': ['FFC6EFCE', 'FF006100'],
  'Đóng': ['FFC6EFCE', 'FF006100'], 'Giữ': ['FFFFEB9C', 'FF9C5700'], 'Bỏ': ['FFEDEDED', 'FF595959'] };
const F = (o = {}) => ({ name: 'Arial', size: 10, ...o });
const fill = argb => ({ type: 'pattern', pattern: 'solid', fgColor: { argb }, bgColor: { argb } });
const thin = { style: 'thin', color: { argb: 'FFBFBFBF' } };
const BOX = { top: thin, left: thin, bottom: thin, right: thin };
const NAVY = 'FF1F3864';
const lines = (t, w) => String(t || '').split('\n').reduce((n, l) => n + Math.max(1, Math.ceil(l.length / w)), 0);
const head = (ws, r, cols) => { cols.forEach((h, i) => { const c = ws.getCell(r, i + 1); c.value = h; c.style = { font: F({ bold: true, color: { argb: 'FFFFFFFF' } }), fill: fill(NAVY), border: BOX, alignment: { horizontal: 'center', vertical: 'middle', wrapText: true } }; }); ws.getRow(r).height = 30; };
const chip = (c, v) => { const k = VC[v] || ['FFFFFFFF', 'FF000000']; c.style = { font: F({ bold: true, color: { argb: k[1] } }), fill: fill(k[0]), border: BOX, alignment: { horizontal: 'center', vertical: 'top', wrapText: true } }; };

(async () => {
  const wb = new ExcelJS.Workbook(); wb.creator = 'Claude';
  const data = SHEETS.map(s => {
    const f = path.join(R, 'out', s.replace(/ /g, '_') + '.json');
    const input = JSON.parse(fs.readFileSync(path.join(R, 'in', s.replace(/ /g, '_') + '.json'), 'utf8')).cases;
    const out = fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, 'utf8')) : { cases: [], questions: [] };
    return { sheet: s, input, out };
  });
  const allQ = JSON.parse(fs.readFileSync(path.join(R, 'in', 'Can_xac_nhan.json'), 'utf8'));

  // ------------------------------------------------ Tổng quan
  const S = wb.addWorksheet('Tổng quan', { views: [{ showGridLines: false }] });
  [22, 10, 10, 10, 10, 11, 10, 12, 60].forEach((w, i) => (S.getColumn(i + 1).width = w));
  S.mergeCells(1, 1, 1, 9); S.getCell(1, 1).value = 'Rà soát test case Wave 1 — SGS-DTP_TestCase_v0.2_Phase1.xlsx';
  S.getCell(1, 1).style = { font: F({ bold: true, size: 14, color: { argb: 'FFFFFFFF' } }), fill: fill(NAVY), alignment: { vertical: 'middle', indent: 1 } }; S.getRow(1).height = 28;
  S.mergeCells(2, 1, 2, 9); S.getCell(2, 1).value = 'Đối chiếu với: UC v5.4 · US (AC) · decision log · Figma DTP P1 (14/10/2026) · web local main b5cb690 (19/10/2026). Chỉ rà soát, CHƯA sửa file test case. Phạm vi Wave 1 theo SGS_DTP_Detailed_Plan_v3.0.';
  S.getCell(2, 1).style = { font: F({ italic: true, color: { argb: 'FF595959' } }), alignment: { wrapText: true, vertical: 'middle', indent: 1 } }; S.getRow(2).height = 30;
  let r = 4;
  head(S, r, ['Sheet', 'Tổng case', ...VERDICTS, 'Đã rà', 'Ghi chú']); r++;
  const tot = { n: 0, done: 0 }; VERDICTS.forEach(v => (tot[v] = 0));
  for (const d of data) {
    const cnt = v => d.out.cases.filter(c => c.verdict === v).length;
    const vals = [d.sheet, d.input.length, ...VERDICTS.map(cnt), d.out.cases.length, d.out.cases.length < d.input.length ? `Thiếu ${d.input.length - d.out.cases.length} case chưa rà` : ''];
    vals.forEach((v, i) => { const c = S.getCell(r, i + 1); c.value = v; c.style = { font: F({ bold: i === 0 }), border: BOX, alignment: { horizontal: i === 0 || i === 8 ? undefined : 'center', vertical: 'middle' } }; });
    S.getCell(r, 1).value = { text: d.sheet, hyperlink: `#'${d.sheet}'!A1` }; S.getCell(r, 1).font = F({ bold: true, color: { argb: 'FF0563C1' }, underline: true });
    VERDICTS.forEach((v, i) => { if (vals[i + 2]) { const k = VC[v]; S.getCell(r, i + 3).style = { ...S.getCell(r, i + 3).style, fill: fill(k[0]), font: F({ bold: true, color: { argb: k[1] } }) }; } });
    tot.n += d.input.length; tot.done += d.out.cases.length; VERDICTS.forEach(v => (tot[v] += cnt(v))); r++;
  }
  ['Tổng', tot.n, ...VERDICTS.map(v => tot[v]), tot.done, ''].forEach((v, i) => { const c = S.getCell(r, i + 1); c.value = v; c.style = { font: F({ bold: true }), fill: fill('FFF2F2F2'), border: BOX, alignment: { horizontal: i === 0 ? undefined : 'center' } }; });
  r += 2;
  const legend = [['Xoá', 'Case phải bỏ: đánh [OUT], tính năng không có trong UC v5.4 / Figma P1 (vd Country), Phase 2, hoặc trùng case khác.'],
    ['Sửa', 'Case đúng phạm vi nhưng viết sai so với Figma / UC / US: nhãn, nút, câu thông báo, bước, vai trò, Expected, mã UC, gắn nhầm [Phase 2]…'],
    ['Lệch web', 'Case đúng theo Figma / UC nhưng web (main b5cb690) làm khác hoặc chưa build → báo dev, không sửa case.'],
    ['Wave sau', 'UC thuộc Wave 2/3 theo Plan v3.0 — giữ case, chưa rà sâu.'], ['OK', 'Đúng và khớp web.']];
  for (const [k, v] of legend) { const a = S.getCell(r, 1); a.value = k; chip(a, k); S.mergeCells(r, 2, r, 9); const b = S.getCell(r, 2); b.value = v; b.style = { font: F(), border: BOX, alignment: { wrapText: true, vertical: 'middle' } }; S.getRow(r).height = 20; r++; }

  // ------------------------------------------------ one tab per sheet
  for (const d of data) {
    const ws = wb.addWorksheet(d.sheet, { views: [{ state: 'frozen', ySplit: 2, showGridLines: false }] });
    [7, 14, 11, 40, 9, 48, 48, 40, 30].forEach((w, i) => (ws.getColumn(i + 1).width = w));
    ws.mergeCells(1, 1, 1, 9); ws.getCell(1, 1).value = { text: `← Tổng quan   ·   ${d.sheet}: ${d.input.length} case`, hyperlink: "#'Tổng quan'!A1" };
    ws.getCell(1, 1).style = { font: F({ bold: true, color: { argb: 'FFFFFFFF' } }), fill: fill(NAVY), alignment: { vertical: 'middle', indent: 1 } }; ws.getRow(1).height = 22;
    head(ws, 2, ['Dòng', 'Mã TC', 'UC', 'Tên case (hiện tại)', 'Kết luận', 'Sai ở đâu', 'Đề xuất sửa', 'Web hiện tại (main b5cb690)', 'Nguồn']);
    let rr = 3;
    for (const c of d.input) {
      const o = d.out.cases.find(x => x.row === c.row) || d.out.cases.find(x => x.tc === c.tc) || { verdict: 'Chưa rà', issue: '', fix: '', web: '', source: '' };
      const vals = [c.row, c.tc, c.uc, c.name, o.verdict, o.issue, o.fix, o.web, o.source];
      vals.forEach((v, i) => { const cell = ws.getCell(rr, i + 1); cell.value = v; cell.style = { font: F({ size: 9.5 }), border: BOX, alignment: { vertical: 'top', wrapText: true, horizontal: i < 3 ? 'center' : undefined } }; });
      chip(ws.getCell(rr, 5), o.verdict);
      ws.getRow(rr).height = Math.max(18, Math.max(lines(c.name, 42), lines(o.issue, 50), lines(o.fix, 50), lines(o.web, 42), lines(o.source, 30)) * 12.5 + 6);
      rr++;
    }
    ws.autoFilter = { from: { row: 2, column: 1 }, to: { row: rr - 1, column: 9 } };
  }

  // ------------------------------------------------ Cần xác nhận
  const Q = wb.addWorksheet('Cần xác nhận', { views: [{ state: 'frozen', ySplit: 2, showGridLines: false }] });
  [7, 9, 14, 50, 16, 10, 60].forEach((w, i) => (Q.getColumn(i + 1).width = w));
  Q.mergeCells(1, 1, 1, 7); Q.getCell(1, 1).value = { text: '← Tổng quan   ·   Sheet "Cần xác nhận" — chỉ các câu của sheet Wave 1', hyperlink: "#'Tổng quan'!A1" };
  Q.getCell(1, 1).style = { font: F({ bold: true, color: { argb: 'FFFFFFFF' } }), fill: fill(NAVY), alignment: { vertical: 'middle', indent: 1 } }; Q.getRow(1).height = 22;
  head(Q, 2, ['Dòng', 'Mã', 'Sheet', 'Câu hỏi', 'TC liên quan', 'Đề xuất', 'Câu trả lời / lý do']);
  let qr = 3; const qcount = { 'Đóng': 0, 'Giữ': 0, 'Bỏ': 0 };
  for (const q of allQ.filter(x => SHEETS.includes(x.sheet))) {
    const d = data.find(x => x.sheet === q.sheet);
    const o = (d.out.questions || []).find(x => x.row === q.row || x.id === q.id) || { decision: 'Chưa rà', answer: '' };
    if (qcount[o.decision] !== undefined) qcount[o.decision]++;
    const vals = [q.row, q.id, q.sheet, q.question, q.tcs, o.decision, o.answer];
    vals.forEach((v, i) => { const cell = Q.getCell(qr, i + 1); cell.value = v; cell.style = { font: F({ size: 9.5 }), border: BOX, alignment: { vertical: 'top', wrapText: true } }; });
    chip(Q.getCell(qr, 6), o.decision);
    Q.getRow(qr).height = Math.max(18, Math.max(lines(q.question, 48), lines(o.answer, 58)) * 12.5 + 6); qr++;
  }
  Q.autoFilter = { from: { row: 2, column: 1 }, to: { row: qr - 1, column: 7 } };
  // summary line for questions
  r += 1; S.mergeCells(r, 1, r, 9);
  S.getCell(r, 1).value = { text: `Cần xác nhận (Wave 1): Đóng ${qcount['Đóng']} · Giữ ${qcount['Giữ']} · Bỏ ${qcount['Bỏ']}  →  xem tab Cần xác nhận`, hyperlink: "#'Cần xác nhận'!A1" };
  S.getCell(r, 1).style = { font: F({ bold: true, color: { argb: 'FF0563C1' }, underline: true }), alignment: { indent: 1 } };

  await wb.xlsx.writeFile(OUT);
  console.log('written', OUT, JSON.stringify(tot), JSON.stringify(qcount));
})().catch(e => { console.error(e); process.exit(1); });
