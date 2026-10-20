// Bug evidence workbook for the Customers Round 1 run: summary sheet + one sheet per bug (Figma expected + actual screenshots).
// usage: node build-bug-report.js <out.xlsx>
const ExcelJS = require('exceljs');
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');
const T = __dirname;
const OUT = process.argv[2];
const FIG = 'C:/Users/thavt/Documents/DTP/dts-agent-workspace/docs/prototypes/figma-p1/img/';
const TMP = path.join(T, 'bug-img'); fs.mkdirSync(TMP, { recursive: true });
const w = JSON.parse(fs.readFileSync(path.join(T, 'writeback.json'), 'utf8'));
const cases = JSON.parse(fs.readFileSync(path.join(T, 'customers-cases.json'), 'utf8'));
const res = {}; for (const g of ['A', 'B', 'C', 'D']) JSON.parse(fs.readFileSync(path.join(T, 'results', g + '.json'), 'utf8')).forEach(r => (res[r.tc] = r));

// severity + Figma frame of the expected screen (null = no Figma screen for this behaviour)
const META = {
  'CU-BUG-01': ['Trung bình', '191-29625.jpg', 'ACC-01 Customer accounts'],
  'CU-BUG-02': ['Trung bình', '191-29625.jpg', 'ACC-01 Customer accounts (Scopes 0, Workspaces 0)'],
  'CU-BUG-03': ['Thấp', '191-30058.jpg', 'ACC-03 ACC-05 Invite initial Customer Admin'],
  'CU-BUG-04': ['Trung bình', '191-29808.jpg', 'ACC-03 Create customer account'],
  'CU-BUG-05': ['Cao', '191-29808.jpg', 'ACC-03 Create customer account'],
  'CU-BUG-06': ['Trung bình', '191-29808.jpg', 'ACC-03 Create customer account'],
  'CU-BUG-07': ['Trung bình', '191-30058.jpg', 'ACC-03 ACC-05 Invite initial Customer Admin'],
  'CU-BUG-08': ['Cao', null, 'Figma không có màn cho tình huống này (hành vi theo US-008, Q-U-17)'],
  'CU-BUG-09': ['Cao', null, 'Figma không có màn cho tình huống này (Q-CU-15)'],
  'CU-BUG-10': ['Trung bình', null, 'Figma không có màn lỗi mạng'],
  'CU-BUG-11': ['Trung bình', null, 'Figma không có màn lỗi gửi email'],
  'CU-BUG-12': ['Thấp', '9-26710.jpg', 'NTF-03 Invitation email'],
  'CU-BUG-13': ['Thấp', '191-30282.jpg', 'ACC-02 Customer account details'],
  'CU-BUG-14': ['Thấp', '191-29625.jpg', 'ACC-01 Customer accounts'],
  'CU-BUG-15': ['Trung bình', '191-29625.jpg', 'ACC-01 Customer accounts (hàng tiêu đề cột của bảng)'],
};
const SEV = { 'Cao': ['FFFFC7CE', 'FF9C0006'], 'Trung bình': ['FFFFEB9C', 'FF9C5700'], 'Thấp': ['FFDDEBF7', 'FF1F3864'] };
const F = (o = {}) => ({ name: 'Arial', size: 10, ...o });
const fill = argb => ({ type: 'pattern', pattern: 'solid', fgColor: { argb }, bgColor: { argb } });
const thin = { style: 'thin', color: { argb: 'FFBFBFBF' } };
const BOX = { top: thin, left: thin, bottom: thin, right: thin };
const NAVY = 'FF1F3864', LBLUE = 'FFDDEBF7', LINK = 'FF0563C1';
const lines = (t, wd) => String(t || '').split('\n').reduce((n, l) => n + Math.max(1, Math.ceil(l.length / wd)), 0);
const IMG_W = 620;

async function prep(file, name, colour) {
  const meta = await sharp(file).metadata();
  const out = path.join(TMP, name);
  await sharp(file).extend({ top: 3, bottom: 3, left: 3, right: 3, background: colour }).jpeg({ quality: 85 }).toFile(out);
  return { out, w: meta.width + 6, h: meta.height + 6 };
}
const fit = (img, maxW = IMG_W, maxH = 420) => { const k = Math.min(maxW / img.w, maxH / img.h); return { width: Math.round(img.w * k), height: Math.round(img.h * k) }; };

(async () => {
  const wb = new ExcelJS.Workbook(); wb.creator = 'Claude';
  // ---------------------------------------------------------- summary
  const S = wb.addWorksheet('Danh sách bug', { views: [{ showGridLines: false }] });
  [2, 12, 12, 70, 34, 8].forEach((x, i) => (S.getColumn(i + 1).width = x));
  S.mergeCells(1, 2, 1, 6); S.getCell(1, 2).value = 'Customers · Operations Console — Bug Round 1 (kèm ảnh)';
  S.getCell(1, 2).style = { font: F({ bold: true, size: 14, color: { argb: 'FFFFFFFF' } }), fill: fill(NAVY), alignment: { vertical: 'middle', indent: 1 } }; S.getRow(1).height = 28;
  S.mergeCells(2, 2, 2, 6);
  S.getCell(2, 2).value = 'Môi trường: localhost — web http://localhost:3000/ops/login, hộp thư http://localhost:8025 · Code CORP-BA-DTP main b5cb690 (19/10/2026) · Tài khoản SGS Admin lin.mei@example.com / password · Ngày chạy 19/10/2026 · Nguồn: SGS-DTP_TestCase_v0.3_Phase1.xlsx, sheet Customers (100 case: 65 Passed · 24 Failed · 11 Pending). Mã CU-BUG-xx là mã tạm, thay bằng mã Jira khi tạo bug.';
  S.getCell(2, 2).style = { font: F({ italic: true, color: { argb: 'FF595959' } }), alignment: { wrapText: true, vertical: 'middle', indent: 1 } }; S.getRow(2).height = 44;
  let r = 4;
  ['Mã bug', 'Mức độ', 'Tiêu đề', 'Case liên quan', 'Số case'].forEach((h, i) => { const c = S.getCell(r, i + 2); c.value = h; c.style = { font: F({ bold: true, color: { argb: 'FFFFFFFF' } }), fill: fill(NAVY), border: BOX, alignment: { horizontal: 'center', vertical: 'middle' } }; });
  S.getRow(r).height = 22; r++;
  for (const b of w.bugs) {
    const [sev] = META[b.code];
    const vals = [{ text: b.code, hyperlink: `#'${b.code}'!A1` }, sev, b.title, b.tcs.length ? b.tcs.join(', ') : 'Chưa có case (test tự do)', b.tcs.length];
    vals.forEach((v, i) => { const c = S.getCell(r, i + 2); c.value = v; c.style = { font: F(), border: BOX, alignment: { vertical: 'top', wrapText: true, horizontal: [0, 1, 4].includes(i) ? 'center' : undefined } }; });
    S.getCell(r, 2).font = F({ bold: true, color: { argb: LINK }, underline: true });
    S.getCell(r, 3).style = { ...S.getCell(r, 3).style, fill: fill(SEV[sev][0]), font: F({ bold: true, color: { argb: SEV[sev][1] } }) };
    S.getRow(r).height = Math.max(20, lines(b.title, 68) * 13 + 6); r++;
  }

  // ---------------------------------------------------------- one sheet per bug
  for (const b of w.bugs) {
    const [sev, fig, figName] = META[b.code];
    const ws = wb.addWorksheet(b.code, { views: [{ showGridLines: false }] });
    [2, 20, 70, 2, 90].forEach((x, i) => (ws.getColumn(i + 1).width = x));
    let r = 1;
    const back = ws.getCell(r, 2); back.value = { text: '← Danh sách bug', hyperlink: "#'Danh sách bug'!A1" }; back.font = F({ color: { argb: LINK }, underline: true }); r++;
    ws.mergeCells(r, 2, r, 5); const t = ws.getCell(r, 2); t.value = `${b.code} · ${b.title}`;
    t.style = { font: F({ bold: true, size: 13, color: { argb: 'FFFFFFFF' } }), fill: fill(NAVY), alignment: { vertical: 'middle', wrapText: true, indent: 1 } }; ws.getRow(r).height = Math.max(30, lines(t.value, 160) * 18 + 8); r += 2;
    const info = [['Mức độ', sev], ['Màn hình', 'Customers · Operations Console'], ['Môi trường', 'localhost · http://localhost:3000/ops/login · code main b5cb690 (19/10/2026)'],
      ['Tài khoản', 'SGS Admin lin.mei@example.com / password'], ['Case liên quan', b.tcs.length ? b.tcs.join(', ') + ' (sheet Customers, SGS-DTP_TestCase_v0.3_Phase1.xlsx)' : (b.repro && b.repro.note) || ''],
      ['UC', b.tcs.length ? [...new Set(b.tcs.map(tc => (cases.find(c => c.tc === tc) || {}).uc))].join(', ') : 'ACC-01']];
    for (const [k, v] of info) {
      const a = ws.getCell(r, 2); a.value = k; a.style = { font: F({ bold: true }), fill: fill(LBLUE), border: BOX, alignment: { vertical: 'top', indent: 1 } };
      ws.mergeCells(r, 3, r, 5); const c = ws.getCell(r, 3); c.value = v; c.style = { font: F({ bold: k === 'Mức độ', color: k === 'Mức độ' ? { argb: SEV[sev][1] } : undefined }), fill: k === 'Mức độ' ? fill(SEV[sev][0]) : undefined, border: BOX, alignment: { vertical: 'top', wrapText: true } };
      ws.getRow(r).height = 18; r++;
    }
    r++;
    // Figma expected
    ws.mergeCells(r, 2, r, 5); ws.getCell(r, 2).value = `Figma · Kết quả mong đợi — ${figName}`;
    ws.getCell(r, 2).style = { font: F({ bold: true, color: { argb: 'FF2E7D32' } }), fill: fill('FFF2F2F2'), alignment: { vertical: 'middle', indent: 1 } }; ws.getRow(r).height = 20; r++;
    if (fig) {
      const img = await prep(FIG + fig, `${b.code}-figma.jpg`, '#2E7D32'); const e = fit(img, 760, 470);
      for (let i = 0; i < Math.ceil((e.height + 10) / 20); i++) ws.getRow(r + i).height = 15;
      ws.addImage(wb.addImage({ filename: img.out, extension: 'jpeg' }), { tl: { col: 1.05, row: r - 1 + 0.2 }, ext: e });
      r += Math.ceil((e.height + 10) / 20) + 1;
    } else { ws.mergeCells(r, 2, r, 5); ws.getCell(r, 2).value = 'Không có ảnh Figma — so theo Kết quả mong đợi của từng case bên dưới.'; ws.getCell(r, 2).font = F({ italic: true, color: { argb: 'FF7F7F7F' } }); r += 2; }

    const items = b.tcs.length ? b.tcs.map(tc => ({ tc })) : [{ repro: b.repro }];
    for (const it of items) {
      const tc = it.tc;
      const c = tc ? cases.find(x => x.tc === tc) : { name: 'Tái hiện (test tự do)', pre: it.repro.pre, steps: it.repro.steps, expected: it.repro.expected }; const rs = tc ? res[tc] : { remark: it.repro.actual, shot: it.repro.shots[0] };
      ws.mergeCells(r, 2, r, 5); const h = ws.getCell(r, 2); h.value = tc ? `${tc} · ${c.name}` : c.name;
      h.style = { font: F({ bold: true, size: 11, color: { argb: 'FFFFFFFF' } }), fill: fill('FFC00000'), alignment: { vertical: 'middle', wrapText: true, indent: 1 } }; ws.getRow(r).height = 22; r++;
      const rowsTxt = [['Pre-condition', c.pre], ['Bước tái hiện', tc === 'TC_028' ? (w.stepEdits[0].steps) : c.steps], ['Kết quả mong đợi', c.expected], ['Thực tế', rs.remark]];
      for (const [k, v] of rowsTxt) {
        const a = ws.getCell(r, 2); a.value = k; a.style = { font: F({ bold: true, color: k === 'Thực tế' ? { argb: 'FFC00000' } : undefined }), fill: fill(k === 'Thực tế' ? 'FFFFC7CE' : LBLUE), border: BOX, alignment: { vertical: 'top', indent: 1 } };
        ws.mergeCells(r, 3, r, 5); const cc = ws.getCell(r, 3); cc.value = v; cc.style = { font: F(), border: BOX, alignment: { vertical: 'top', wrapText: true } };
        ws.getRow(r).height = Math.max(18, lines(v, 175) * 13 + 5); r++;
      }
      // actual screenshots: main + extra (TC_xxx-*.png), two per row
      const dir = path.join(T, 'run', 'shots');
      const files = (tc ? [path.join(T, rs.shot)].concat(fs.readdirSync(dir).filter(f => f.startsWith(tc + '-')).map(f => path.join(dir, f))) : it.repro.shots.map(f => path.join(T, f))).filter(f => fs.existsSync(f));
      ws.mergeCells(r, 2, r, 5); ws.getCell(r, 2).value = `Ảnh thực tế (${files.length}) · localhost main b5cb690`; ws.getCell(r, 2).style = { font: F({ bold: true, color: { argb: 'FF1F4E79' } }), fill: fill('FFF2F2F2'), alignment: { indent: 1 } }; ws.getRow(r).height = 18; r++;
      for (let i = 0; i < files.length; i += 2) {
        const pair = []; for (const f of files.slice(i, i + 2)) pair.push(await prep(f, `${tc || b.code}-${path.basename(f, '.png')}.jpg`, '#C00000'));
        const exts = pair.map(p => fit(p, 640, 400)); const hh = Math.max(...exts.map(e => e.height));
        const nRows = Math.ceil((hh + 10) / 20); for (let j = 0; j < nRows; j++) ws.getRow(r + j).height = 15;
        pair.forEach((p, j) => ws.addImage(wb.addImage({ filename: p.out, extension: 'jpeg' }), { tl: { col: j === 0 ? 1.05 : 4.02, row: r - 1 + 0.2 }, ext: exts[j] }));
        const caps = files.slice(i, i + 2).map(f => path.basename(f));
        r += nRows; ws.getCell(r, 2).value = caps[0]; if (caps[1]) ws.getCell(r, 5).value = caps[1];
        ws.getRow(r).font = F({ italic: true, size: 8, color: { argb: 'FF7F7F7F' } }); r += 1;
      }
      r += 1;
    }
  }
  await wb.xlsx.writeFile(OUT);
  console.log('written', OUT, 'bugs', w.bugs.length);
})().catch(e => { console.error(e); process.exit(1); });
