// E2E workbook v3 — Wave 1 only: sheet "Danh sách E2E" (+ UC coverage vs Plan v3.0) and one sheet per executed flow.
// Each step: Figma action screen (red ①②) · Figma expected screen (green ⒶⒷ) · actual screenshot, then a table
// expected ↔ actual per bullet with UC + Plan status. usage: node build-e2e-v3.js <out.xlsx> <flowId>...
const ExcelJS = require('exceljs');
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');
const OUT = process.argv[2];
const RUN_FLOWS = process.argv.slice(3);
const IMG = 'C:/Users/thavt/Documents/DTP/dts-agent-workspace/docs/prototypes/figma-p1/img/';
const PLAN = 'C:/Users/thavt/Documents/DTP/review-testcase-2026-10-15/SGS_DTP_Detailed_Plan_v3.0.xlsx';
const TMP = path.join(__dirname, 'e2e-img3'); fs.mkdirSync(TMP, { recursive: true });

const F = (o = {}) => ({ name: 'Arial', size: 10, ...o });
const fill = argb => ({ type: 'pattern', pattern: 'solid', fgColor: { argb }, bgColor: { argb } });
const thin = { style: 'thin', color: { argb: 'FFBFBFBF' } };
const BOX = { top: thin, left: thin, bottom: thin, right: thin };
const C = { navy: 'FF1F3864', lblue: 'FFDDEBF7', grey: 'FFF2F2F2', white: 'FFFFFFFF', note: 'FFFFF2CC', link: 'FF0563C1' };
const RES = {
  Passed: { fill: 'FFC6EFCE', font: 'FF006100' }, Failed: { fill: 'FFFFC7CE', font: 'FF9C0006' },
  Blocked: { fill: 'FFFFEB9C', font: 'FF9C5700' }, Pending: { fill: 'FFD9E1F2', font: 'FF1F3864' }, NA: { fill: 'FFEDEDED', font: 'FF595959' },
  'Not executed': { fill: 'FFEDEDED', font: 'FF595959' },
};
const ROLE = [['SGS Admin', 'FF1F4E79'], ['Customer Admin', 'FFC55A11'], ['Customer User', 'FFED7D31'], ['Customer Viewer', 'FFBF8F00'], ['Consultant', 'FF7030A0'], ['Người được mời', 'FF548235'], ['Hệ thống', 'FF7F7F7F']];
const roleColor = r => (ROLE.find(([k]) => r.startsWith(k)) || ['', 'FF7F7F7F'])[1];
const lines = (t, w) => String(t || '').split('\n').reduce((n, l) => n + Math.max(1, Math.ceil(l.length / w)), 0);
const ucs = s => [...String(s || '').matchAll(/[A-Z]{3,4}-\d\d/g)].map(m => m[0]);
const resultCell = (cell, value) => {
  cell.value = value; const s = RES[value] || RES.NA;
  cell.style = { font: F({ bold: true, color: { argb: s.font } }), fill: fill(s.fill), border: BOX, alignment: { horizontal: 'center', vertical: 'middle', wrapText: true } };
  cell.dataValidation = { type: 'list', allowBlank: true, formulae: ['"Passed,Failed,Blocked,Pending,NA"'] };
};
function colourResults(ws, ref) {
  ws.addConditionalFormatting({ ref, rules: Object.entries(RES).filter(([k]) => k !== 'Not executed').map(([k, s], i) => ({
    type: 'containsText', operator: 'containsText', text: k, priority: i + 1,
    style: { fill: { type: 'pattern', pattern: 'solid', bgColor: { argb: s.fill } }, font: { color: { argb: s.font }, bold: true } } })) });
}

// ------------------------------------------------------------------ Plan v3.0
async function loadPlan() {
  const wb = new ExcelJS.Workbook(); await wb.xlsx.readFile(PLAN);
  const ws = wb.getWorksheet('Plan by UC'); const plan = {};
  const t = v => (v == null ? '' : v.richText ? v.richText.map(x => x.text).join('') : v.result !== undefined ? String(v.result) : typeof v === 'object' ? '' : String(v));
  ws.eachRow((row, i) => { const id = t(row.getCell(1).value).trim(); if (/^[A-Z]{3,4}-\d\d$/.test(id)) plan[id] = { name: t(row.getCell(2).value), pic: t(row.getCell(3).value), wave: Number(t(row.getCell(4).value)), status: t(row.getCell(11).value) || 'Not started', note: t(row.getCell(17).value) }; });
  return plan;
}
const isDone = p => p && p.status === 'Done';
const isPending = p => !p || p.wave > 1 || p.status === 'Not started';
const planTag = (id, plan) => { const p = plan[id]; return p ? `${id} · ${p.wave > 1 ? 'W' + p.wave + ' ' : ''}${p.status}` : `${id} · không có trong Plan`; };

/** Result of one expectation from the run + Plan rule. */
function bulletResult(check, uc, plan) {
  const p = plan[uc];
  if (check.ok === true) return { res: 'Passed', why: '', early: p && !isDone(p) ? `${uc} (${p.wave > 1 ? 'Wave ' + p.wave + ' · ' : ''}${p.status})` : '' };
  if (check.ok === false) return isPending(p) ? { res: 'Pending', why: `${uc} chưa làm theo Plan (${p ? (p.wave > 1 ? 'Wave ' + p.wave + ', ' : '') + p.status : 'không có trong Plan'}) — chưa tính lỗi.` } : { res: 'Failed', why: '' };
  return isDone(p) ? { res: 'Blocked', why: `Plan ghi ${uc} Done nhưng bản chạy chưa có.` } : { res: 'Pending', why: `${uc} chưa xong theo Plan (${p ? (p.wave > 1 ? 'Wave ' + p.wave + ', ' : '') + p.status : '—'}).` };
}
/** Failed > Blocked > Pending > Passed as plain comparisons (no COUNTIF) so every spreadsheet app agrees. */
const anyOf = cells => { const has = v => `OR(${cells.map(c => `${c}="${v}"`).join(',')})`; return `IF(${has('Failed')},"Failed",IF(${has('Blocked')},"Blocked",IF(${has('Pending')},"Pending",IF(AND(${cells.map(c => `${c}="Passed"`).join(',')}),"Passed",""))))`; };
const worst = rs => ['Failed', 'Blocked', 'Pending', 'Passed'].find(r => rs.includes(r)) || '';

// ------------------------------------------------------------------ images
const SLOT_W = 500, SLOT_H = 312;
async function annotate(spec, name, colour, label) {
  const meta = await sharp(IMG + spec.img).metadata();
  const svg = [`<svg width="${meta.width}" height="${meta.height}" xmlns="http://www.w3.org/2000/svg">`];
  for (const { n, b: [x1, y1, x2, y2] } of spec.marks || []) {
    svg.push(`<rect x="${x1}" y="${y1}" width="${x2 - x1}" height="${y2 - y1}" rx="4" fill="none" stroke="${colour}" stroke-width="3"/>`);
    const cx = Math.max(13, x1 - 2), cy = Math.max(13, y1 - 2);
    svg.push(`<circle cx="${cx}" cy="${cy}" r="12" fill="${colour}"/><text x="${cx}" y="${cy + 5}" font-family="Arial" font-weight="bold" font-size="15" fill="#fff" text-anchor="middle">${label(n)}</text>`);
  }
  svg.push('</svg>');
  const out = path.join(TMP, name);
  await sharp(IMG + spec.img).composite([{ input: Buffer.from(svg.join('')) }]).extend({ top: 2, bottom: 2, left: 2, right: 2, background: '#9E9E9E' }).jpeg({ quality: 85 }).toFile(out);
  return { out, w: meta.width + 4, h: meta.height + 4 };
}
async function textCard(name, title, body, colour = '#7F7F7F') {
  const out = path.join(TMP, name);
  const wrap = (s, n) => { const w = []; let cur = ''; for (const word of String(s).split(' ')) { if ((cur + ' ' + word).trim().length > n) { w.push(cur.trim()); cur = word; } else cur += ' ' + word; } if (cur.trim()) w.push(cur.trim()); return w; };
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const bodyLines = wrap(body || '', 58).slice(0, 6).map((l, i) => `<text x="540" y="${370 + i * 40}" font-family="Arial" font-size="27" fill="#595959" text-anchor="middle">${esc(l)}</text>`).join('');
  const svg = `<svg width="1080" height="675" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="3" width="1074" height="669" fill="#F7F7F7" stroke="${colour}" stroke-width="4" stroke-dasharray="14 9"/><text x="540" y="290" font-family="Arial" font-weight="bold" font-size="36" fill="${colour}" text-anchor="middle">${esc(title)}</text>${bodyLines}</svg>`;
  await sharp(Buffer.from(svg)).jpeg({ quality: 85 }).toFile(out); return { out, w: 1080, h: 675 };
}
async function shot(file, name) {
  const out = path.join(TMP, name); const meta = await sharp(file).metadata();
  await sharp(file).extend({ top: 3, bottom: 3, left: 3, right: 3, background: '#2E7D32' }).jpeg({ quality: 85 }).toFile(out);
  return { out, w: meta.width + 6, h: meta.height + 6 };
}
const fit = (img, h = SLOT_H) => { const k = Math.min(SLOT_W / img.w, h / img.h); return { width: Math.round(img.w * k), height: Math.round(img.h * k) }; };
const circled = n => String.fromCharCode(0x2460 + n - 1);
const lettered = n => n;
const plain = t => String(t || '').replace(/[Ⓐ-Ⓩ]/g, c => '(' + String.fromCharCode(c.charCodeAt(0) - 0x24B6 + 65) + ')');

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

// ------------------------------------------------------------------ Wave 1 list
const NEW_FLOWS = [
  { id: 'E2E1_012', name: 'Cập nhật khách hàng & liên kết NirmatAI: SGS Admin sửa thông tin khách hàng → Customer Admin thấy tên mới → liên kết khách hàng với NirmatAI client → tab NirmatAI hiển thị đã liên kết', uc: 'ACC-04, ACC-02, ACC-07, AUD-01' },
  { id: 'E2E1_013', name: 'Sửa metadata framework: SGS Admin sửa tên / mô tả framework đang dùng → danh sách & chi tiết framework cập nhật → workspace của khách hàng hiển thị tên mới', uc: 'FWK-05, FWK-01, FWK-02, WSP-03, AUD-01' },
  { id: 'E2E1_014', name: 'Sửa scope: Customer Admin sửa thông tin scope → Customer User được cấp quyền thấy thay đổi → workspace thuộc scope vẫn hoạt động', uc: 'SCP-04, SCP-02, USR-05, WSP-03, AUD-03' },
  { id: 'E2E1_015', name: 'Ma trận quyền khớp thực tế: Customer Admin xem Roles & permissions → Customer User / Customer Viewer làm được và bị chặn đúng như ma trận', uc: 'ROL-02, ROL-01, USR-01' },
];
const EXTRA_UC = { E2E1_011: ['AUTH-02'] }; // UC added to existing flows to cover the Plan

(async () => {
  const plan = await loadPlan();
  const flows = [];
  for (let i = 1; i <= 15; i++) {
    const id = 'E2E1_' + String(i).padStart(3, '0');
    const v2 = path.join(__dirname, 'flows2', id + '.json');
    const v1 = path.join(__dirname, 'flows', id + '.json');
    if (!fs.existsSync(v2) && !fs.existsSync(v1)) { const n = NEW_FLOWS.find(x => x.id === id); flows.push({ id, name: n.name, uc: ucs(n.uc), steps: null, written: false }); continue; }
    const f = JSON.parse(fs.readFileSync(fs.existsSync(v2) ? v2 : v1, 'utf8'));
    const old = fs.existsSync(path.join(__dirname, 'runs', id + '.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, 'runs', id + '.json'), 'utf8')) : null;
    flows.push({ id, name: f.name, uc: [...new Set([...ucs(f.uc), ...(EXTRA_UC[id] || [])])], steps: f.steps.length, written: true, old, file: f });
  }

  const wb = new ExcelJS.Workbook(); wb.creator = 'Claude'; wb.calcProperties = { fullCalcOnLoad: true };
  addGuide(wb);
  const L = wb.addWorksheet('Danh sách E2E', { views: [{ showGridLines: false }] });
  [2, 11, 60, 30, 34, 8, 11, 12, 44].forEach((w, i) => (L.getColumn(i + 1).width = w));
  let r = 1;
  L.mergeCells(r, 2, r, 9); Object.assign(L.getCell(r, 2), { value: 'SGS DTP — E2E Phase 1 · Wave 1 (đối chiếu SGS_DTP_Detailed_Plan_v3.0)' });
  L.getCell(r, 2).style = { font: F({ bold: true, size: 14, color: { argb: C.white } }), fill: fill(C.navy), alignment: { vertical: 'middle', indent: 1 } }; L.getRow(r).height = 28; r++;
  L.mergeCells(r, 2, r, 9); L.getCell(r, 2).value = 'Pending = UC chưa Done theo Plan (Not started / In progress / Blocked / thuộc wave sau). Case vẫn giữ trong danh sách; khi chạy, bước dính UC chưa làm được ghi Pending, không tính lỗi.';
  L.getCell(r, 2).style = { font: F({ italic: true, color: { argb: 'FF595959' } }), alignment: { wrapText: true, vertical: 'middle', indent: 1 } }; L.getRow(r).height = 30; r += 2;
  const head = ['Mã case', 'Luồng', 'UC', 'UC Pending (chưa Done theo Plan)', 'Số bước', 'Kịch bản', 'Kết quả', 'Ghi chú'];
  head.forEach((h, i) => { const c = L.getCell(r, i + 2); c.value = h; c.style = { font: F({ bold: true, color: { argb: C.white } }), fill: fill(C.navy), border: BOX, alignment: { horizontal: 'center', vertical: 'middle', wrapText: true } }; });
  L.getRow(r).height = 30; const listTop = r + 1; r++;
  for (const f of flows) {
    const pend = f.uc.filter(u => !isDone(plan[u]));
    const groups = {}; pend.forEach(u => { const p = plan[u]; const k = p ? (p.wave > 1 ? `Wave ${p.wave} · ${p.status}` : p.status) : 'không có trong Plan'; (groups[k] ??= []).push(u); });
    const pendTxt = Object.entries(groups).map(([k, v]) => `${k}: ${v.join(', ')}`).join('\n') || '—';
    const executed = RUN_FLOWS.includes(f.id);
    const isNew = NEW_FLOWS.some(x => x.id === f.id);
    const note = !f.written ? 'Bổ sung theo Plan v3.0 — phủ UC Wave 1 chưa có E2E. Chưa viết kịch bản.'
      : executed ? (isNew ? 'Luồng mới, bổ sung theo Plan v3.0. ' : '') + 'Đã chạy theo format mới (19/10) — xem sheet.'
      : f.old ? `Lần chạy 19/10 (format cũ): ${['Passed', 'Failed', 'Blocked'].map(k => `${k} ${f.old.steps.filter(s => s.result === k).length}`).join(' · ')}. Sẽ chạy lại theo format mới.` : '';
    const extra = EXTRA_UC[f.id] ? `\nThêm ${EXTRA_UC[f.id].join(', ')} để phủ Plan.` : '';
    const vals = [f.id, f.name, f.uc.join(', '), pendTxt, f.steps ?? '—', f.written ? 'Đã viết' : 'Chưa viết', null, note + extra];
    vals.forEach((v, i) => { const c = L.getCell(r, i + 2); c.value = v; c.style = { font: F(), border: BOX, alignment: { vertical: 'top', wrapText: true, horizontal: [4, 5, 6].includes(i) ? 'center' : undefined } }; });
    if (pend.length) L.getCell(r, 5).style = { ...L.getCell(r, 5).style, fill: fill('FFD9E1F2') };
    if (!f.written) L.getCell(r, 7).style = { ...L.getCell(r, 7).style, font: F({ bold: true, color: { argb: 'FF9C5700' } }), fill: fill('FFFFEB9C') };
    if (executed) {
      L.getCell(r, 2).value = { text: f.id, hyperlink: `#'${f.id}'!A1` }; L.getCell(r, 2).font = F({ bold: true, color: { argb: C.link }, underline: true });
      resultCell(L.getCell(r, 8), f.result || '');
    } else resultCell(L.getCell(r, 8), 'Not executed');
    L.getCell(r, 2).alignment = { vertical: 'top', horizontal: 'center' };
    L.getRow(r).height = Math.max(32, Math.max(lines(f.name, 62), lines(vals[2], 30), lines(pendTxt, 34), lines(vals[7], 46)) * 13 + 6);
    r++;
  }
  colourResults(L, `H${listTop}:H${r - 1}`);

  // coverage of Plan Wave 1
  r += 1;
  L.mergeCells(r, 2, r, 9); L.getCell(r, 2).value = 'Đối chiếu UC Wave 1 của Plan v3.0 với E2E';
  L.getCell(r, 2).style = { font: F({ bold: true, color: { argb: C.white } }), fill: fill(C.navy), alignment: { vertical: 'middle', indent: 1 } }; L.getRow(r).height = 22; r++;
  ['UC', 'Use case (Plan)', 'PIC · Trạng thái Plan', 'Luồng E2E phủ UC', 'Phủ?', '', '', 'Ghi chú Plan'].forEach((h, i) => { if (!h) return; const c = L.getCell(r, i + 2); c.value = h; c.style = { font: F({ bold: true }), fill: fill(C.lblue), border: BOX, alignment: { horizontal: 'center', vertical: 'middle' } }; });
  L.mergeCells(r, 6, r, 8); r++;
  const w1 = Object.entries(plan).filter(([, p]) => p.wave === 1);
  let covered = 0;
  for (const [id, p] of w1) {
    const by = flows.filter(f => f.uc.includes(id)).map(f => f.id + (f.written ? '' : ' (chưa viết)'));
    if (by.length) covered++;
    const vals = [id, p.name, `${p.pic} · ${p.status}`, by.join(', ') || '—', by.length ? '✔' : '✘', null, null, p.note || ''];
    vals.forEach((v, i) => { if (i === 5 || i === 6) return; const c = L.getCell(r, i + 2); c.value = v; c.style = { font: F({ color: i === 4 ? { argb: by.length ? 'FF006100' : 'FF9C0006' } : undefined, bold: i === 4 }), border: BOX, alignment: { vertical: 'top', wrapText: true, horizontal: i === 4 ? 'center' : undefined } }; });
    L.mergeCells(r, 6, r, 8);
    const st = L.getCell(r, 4); st.style = { ...st.style, fill: fill(isDone(p) ? 'FFC6EFCE' : 'FFD9E1F2') };
    L.getRow(r).height = Math.max(16, lines(vals[3], 33) * 13 + 4); r++;
  }
  L.mergeCells(r, 2, r, 9); L.getCell(r, 2).value = `Wave 1 theo Plan: ${w1.length} UC · có luồng E2E phủ: ${covered}/${w1.length} (${w1.filter(([, p]) => isDone(p)).length} UC Done, ${w1.filter(([, p]) => !isDone(p)).length} UC chưa Done → Pending khi chạy).`;
  L.getCell(r, 2).style = { font: F({ bold: true }), fill: fill(C.grey), border: BOX, alignment: { vertical: 'middle', indent: 1, wrapText: true } }; L.getRow(r).height = 20;
  L.views = [{ state: 'frozen', ySplit: listTop - 1, showGridLines: false }];

  // ------------------------------------------------------------------ flow sheets
  for (const id of RUN_FLOWS) {
    const flow = JSON.parse(fs.readFileSync(path.join(__dirname, 'flows2', id + '.json'), 'utf8'));
    const run = JSON.parse(fs.readFileSync(path.join(__dirname, 'runs2', id + '.json'), 'utf8'));
    const ws = wb.addWorksheet(id, { views: [{ showGridLines: false }] });
    [2, 16, 56, 16, 56, 16, 56].forEach((w, i) => (ws.getColumn(i + 1).width = w));
    let r = 1;
    const back = ws.getCell(r, 2); back.value = { text: '← Danh sách E2E', hyperlink: "#'Danh sách E2E'!A1" }; back.font = F({ color: { argb: C.link }, underline: true }); r++;
    ws.mergeCells(r, 2, r, 7); const t = ws.getCell(r, 2); t.value = `${flow.id} · ${flow.name}`;
    t.style = { font: F({ bold: true, size: 14, color: { argb: C.white } }), fill: fill(C.navy), alignment: { vertical: 'middle', wrapText: true, indent: 1 } }; ws.getRow(r).height = 36; r += 2;
    const ucTxt = ucs(flow.uc).map(u => planTag(u, plan)).join('  ·  ');
    // suffix the run used for the data it created (e.g. yt.chang+114793@…)
    const runNo = (JSON.stringify(run).match(/\+(\d{4,})@/) || [])[1] || '';
    const fillRun = v => String(v).replace(/\{run\}/g, runNo || '<số>');
    const LOGIN = { ops: '/ops/login', customer: '/login', consultant: '/consultant/login' };
    // environment + accounts for every flow (001 carries its own, the rest come from accounts.json)
    if (!flow.accounts) {
      const all = JSON.parse(fs.readFileSync(path.join(__dirname, 'accounts.json'), 'utf8'));
      flow.env = { web: 'http://localhost:3000', mail: 'http://localhost:8025', password: 'password', code: 'CORP-BA-DTP main · commit 4be5d13 (15/10/2026)' };
      flow.accounts = (all[id] || []).map(a => ({ ...a, source: all._sources[a.source] || a.source }));
      const login = flow.accounts.map(a => `Đăng nhập ${a.role} · ${a.persona} tại ${flow.env.web}${LOGIN[a.portal]} — Email: ${a.email} — Password: ${flow.env.password}`);
      flow.pre = [...login, ...flow.pre.filter(p => !/^(Login acc|Acc )/i.test(p)), `Hộp thư test: ${flow.env.mail} — mọi email gửi từ môi trường local đều về đây, không gửi ra ngoài.`];
      const rd = {}; const company = (JSON.stringify(run).match(/Hsinchu AI Labs (\d{4,})/) || [])[0];
      if (company) rd['Khách hàng'] = company;
      flow.accounts.filter(a => a.email.includes('{run}')).forEach(a => { rd[`Email ${a.role} · ${a.persona}`] = a.email; });
      if (Object.keys(rd).length) flow.runData = rd;
    }
    const info = [['Mục tiêu', flow.goal], ['Priority', flow.priority], ['Vai trò tham gia', flow.roles.join('\n')]];
    if (flow.env) info.push(['Môi trường test', `Web: ${flow.env.web}  ·  Hộp thư test (Mailpit): ${flow.env.mail}\nMật khẩu chung cho mọi tài khoản: ${flow.env.password}\nCode: ${flow.env.code}`], ['Tài khoản test', 'ACCOUNTS']);
    // short numbered pre-condition: environment, one login line per account, then the business conditions
    const host = u => u.replace(/^https?:\/\//, '');
    const portals = [...new Set(flow.accounts.map(x => host(flow.env.web) + LOGIN[x.portal]))];
    const created = x => /Tạo trong luồng/.test(x.source);
    const biz = flow.pre.filter(p => !/^(Login acc|Acc |Đăng nhập |Hộp thư test|Mở được hộp thư test)/i.test(p));
    const preLines = [`Vào môi trường: ${portals.join(' · ')}`,
      ...flow.accounts.map(x => created(x)
        ? `${x.role} (${x.persona.replace(/ \(.*\)$/, '')}): ${x.email} / ${flow.env.password} — tạo trong luồng, đăng nhập sau khi kích hoạt`
        : `Login acc ${x.role} (${x.persona.replace(/ \(SGS Taiwan\)$/, '')}): ${x.email} / ${flow.env.password}`),
      ...biz, `Hộp thư test: ${host(flow.env.mail)}`];
    info.push(['Pre-condition', preLines.map((x, i) => `${i + 1}. ${fillRun(x)}`).join('\n')], ['Dữ liệu test', Object.entries(flow.data).map(([k, v]) => `${k}: ${v}`).join('\n') + (flow.dataNote ? '\n(' + flow.dataNote + ')' : '')]);
    if (flow.runData) info.push(['Dữ liệu lần chạy này', Object.entries(flow.runData).map(([k, v]) => `${k}: ${fillRun(v)}`).join('\n')]);
    info.push(['UC · trạng thái Plan', ucTxt], ['Lần chạy', `${run.env} · ${new Date(run.runAt).toLocaleString('vi-VN')}`], ['Kết quả case', null]);
    for (const [k, v] of info) {
      const a = ws.getCell(r, 2); a.value = k; a.style = { font: F({ bold: true }), fill: fill(C.lblue), border: BOX, alignment: { vertical: 'top', indent: 1, wrapText: true } };
      if (v === 'ACCOUNTS') {
        // header + one row per account: Vai trò · Nhân vật | Mật khẩu | Link đăng nhập | Email · Nguồn
        const top = r;
        ['Vai trò · Nhân vật', 'Mật khẩu', 'Link đăng nhập', 'Email  ·  Nguồn'].forEach((h, i) => { const c = ws.getCell(r, 3 + i); c.value = h; c.style = { font: F({ bold: true, size: 9 }), fill: fill(C.grey), border: BOX, alignment: { horizontal: 'center', vertical: 'middle' } }; });
        ws.mergeCells(r, 6, r, 7); ws.getRow(r).height = 17; r++;
        for (const acc of flow.accounts) {
          const url = flow.env.web + LOGIN[acc.portal];
          const cells = [`${acc.role} · ${acc.persona}`, flow.env.password, { text: url, hyperlink: url }, { richText: [{ text: fillRun(acc.email), font: F({ bold: true }) }, { text: '\n' + acc.source, font: F({ italic: true, size: 9, color: { argb: 'FF595959' } }) }] }];
          cells.forEach((v2, i) => { const c = ws.getCell(r, 3 + i); c.value = v2; c.style = { font: i === 2 ? F({ color: { argb: C.link }, underline: true }) : F({ bold: i === 1 }), border: BOX, alignment: { vertical: 'top', wrapText: true, horizontal: i === 1 ? 'center' : undefined } }; });
          const rc = ws.getCell(r, 3); rc.style = { ...rc.style, font: F({ bold: true, color: { argb: roleColor(acc.role) } }) };
          ws.mergeCells(r, 6, r, 7); ws.getRow(r).height = Math.max(30, lines(acc.source, 80) * 12 + 20); r++;
        }
        ws.mergeCells(top, 2, r - 1, 2);
        continue;
      }
      ws.mergeCells(r, 3, r, 7); const b = ws.getCell(r, 3); b.value = v; b.style = { font: F(), border: BOX, alignment: { vertical: 'top', wrapText: true } };
      ws.getRow(r).height = Math.max(18, lines(v, 190) * 13 + 5); r++;
    }
    const caseRow = r - 1;
    r++;
    // legend
    ws.mergeCells(r, 2, r, 7); ws.getCell(r, 2).value = 'Cách đọc kết quả:  Passed = đúng như mong đợi  ·  Failed = chức năng có nhưng sai so với mong đợi / Figma  ·  Blocked = Plan ghi Done nhưng bản chạy chưa có  ·  Pending = UC chưa Done theo Plan (chưa làm / wave sau), chưa tính lỗi.';
    ws.getCell(r, 2).style = { font: F({ italic: true, size: 9, color: { argb: 'FF595959' } }), alignment: { wrapText: true, vertical: 'middle', indent: 1 } }; ws.getRow(r).height = 26; r += 2;

    // compute results
    const stepRes = flow.steps.map((s, k) => {
      const rs = run.steps.find(x => x.n === k + 1) || { checks: [], notes: [] };
      const bullets = s.exp.map((e, i) => { const c = rs.checks.find(x => x.e === i + 1) || { ok: 'absent', actual: 'Chưa chạy' }; return { e, c, ...bulletResult(c, e.uc, plan) }; });
      return { rs, bullets, res: worst(bullets.map(b => b.res)) };
    });
    const caseRes = worst(stepRes.map(x => x.res));
    flows.find(f => f.id === id).result = caseRes;

    // flow summary
    ws.mergeCells(r, 2, r, 7); ws.getCell(r, 2).value = 'Sơ đồ luồng'; ws.getCell(r, 2).style = { font: F({ bold: true, color: { argb: C.white } }), fill: fill(C.navy), alignment: { vertical: 'middle', indent: 1 } }; ws.getRow(r).height = 20; r++;
    ['#', 'Bước', 'Vai trò', 'UC · Plan', 'Kết quả', 'Tóm tắt'].forEach((h, i) => { const c = ws.getCell(r, i + 2); c.value = h; c.style = { font: F({ bold: true }), fill: fill(C.lblue), border: BOX, alignment: { horizontal: 'center', vertical: 'middle' } }; }); r++;
    const sumRows = []; const sumTop = r;
    flow.steps.forEach((s, k) => {
      const x = stepRes[k]; const bad = x.bullets.filter(b => b.res !== 'Passed');
      const summary = bad.length ? bad.map(b => `${b.res}: ${plain(b.e.t).replace(/^(\([A-Z]\)|[①-⑳])\s*/, '')}`).join('\n') : `${x.bullets.length}/${x.bullets.length} kết quả đạt`;
      const vals = [k + 1, s.title, s.role.split(' · ')[0], ucs(s.uc).map(u => planTag(u, plan)).join('\n'), null, summary];
      vals.forEach((v, i) => { const c = ws.getCell(r, i + 2); c.value = v; c.style = { font: F(), border: BOX, alignment: { vertical: 'middle', wrapText: true, horizontal: i === 0 ? 'center' : undefined } }; });
      const rc = ws.getCell(r, 4); rc.style = { font: F({ bold: true, color: { argb: C.white } }), fill: fill(roleColor(s.role)), border: BOX, alignment: { horizontal: 'center', vertical: 'middle', wrapText: true } };
      ws.getRow(r).height = Math.max(20, Math.max(lines(summary, 60), ucs(s.uc).length, lines(s.title, 15)) * 13 + 6);
      sumRows.push(r); r++;
    });
    r++;

    // steps
    for (let k = 0; k < flow.steps.length; k++) {
      const s = flow.steps[k]; const x = stepRes[k]; const col = roleColor(s.role);
      for (const f of ['do', 'input']) s[f] = (s[f] || []).map(plain); if (s.note) s.note = plain(s.note);
      const bandRow = r;
      ws.mergeCells(r, 2, r, 5); const band = ws.getCell(r, 2); band.value = `BƯỚC ${k + 1}   ${s.title}`;
      band.style = { font: F({ bold: true, size: 12, color: { argb: C.white } }), fill: fill(col), alignment: { vertical: 'middle', indent: 1 } };
      ws.mergeCells(r, 6, r, 7); const rh = ws.getCell(r, 6); rh.value = s.role; rh.style = { font: F({ bold: true, color: { argb: C.white } }), fill: fill(col), alignment: { vertical: 'middle', horizontal: 'right', indent: 1 } };
      ws.getRow(r).height = 24; r++;
      // link from summary
      const sc = ws.getCell(sumRows[k], 3); sc.value = { text: s.title, hyperlink: `#'${id}'!B${bandRow}` }; sc.font = F({ color: { argb: C.link }, underline: true });
      // captions + images
      const caps = [`① Figma · Màn thao tác${s.act ? ' — ' + s.act.frame : ''}`, `(A) Figma · Kết quả mong đợi${s.expImg ? ' — ' + s.expImg.frame : ''}`, 'Ảnh thực tế · app chạy local'];
      caps.forEach((cv, i) => { ws.mergeCells(r, 2 + i * 2, r, 3 + i * 2); const c = ws.getCell(r, 2 + i * 2); c.value = cv; c.style = { font: F({ bold: true, size: 9, color: { argb: i === 0 ? 'FFC00000' : i === 1 ? 'FF2E7D32' : 'FF1F4E79' } }), fill: fill(C.grey), alignment: { vertical: 'middle', indent: 1 } }; });
      ws.getRow(r).height = 18; r++;
      const imgs = [
        s.act ? await annotate(s.act, `${id}-${k + 1}-act.jpg`, '#E00000', circled) : await textCard(`${id}-${k + 1}-act.jpg`, 'Bước quan sát', 'Không có thao tác trên màn riêng — xem các mục ở ảnh Kết quả mong đợi.'),
        s.expImg ? await annotate(s.expImg, `${id}-${k + 1}-exp.jpg`, '#2E7D32', lettered) : await textCard(`${id}-${k + 1}-exp.jpg`, 'Figma chưa có màn này', s.expNote || '', '#C00000'),
        x.rs.shot ? await shot(path.join(__dirname, 'runs2', id, x.rs.shot), `${id}-${k + 1}-actual.jpg`) : await textCard(`${id}-${k + 1}-actual.jpg`, 'Không có ảnh thực tế', ''),
      ];
      const slotH = (s.act && s.act.portrait) || (s.expImg && s.expImg.portrait) ? 560 : SLOT_H;
      const top = r; const rowsForImg = Math.ceil((slotH + 8) / 20);
      for (let i = 0; i < rowsForImg; i++) ws.getRow(r + i).height = 15;
      imgs.forEach((img, i) => ws.addImage(wb.addImage({ filename: img.out, extension: 'jpeg' }), { tl: { col: 1 + i * 2 + 0.05, row: top + 0.1 }, ext: fit(img, slotH) }));
      r += rowsForImg + 1;
      // action / input / note
      const rowsTxt = [['Thao tác', s.do.join('\n')], ['Dữ liệu nhập', s.input && s.input.length ? s.input.join('\n') : '—']];
      if (s.note) rowsTxt.push(['Lưu ý', s.note]);
      rowsTxt.push(['Case màn hình', s.rel || '—']);
      for (const [kk, v] of rowsTxt) {
        const a = ws.getCell(r, 2); a.value = kk; a.style = { font: F({ bold: true }), fill: fill(kk === 'Lưu ý' ? C.note : C.lblue), border: BOX, alignment: { vertical: 'top', indent: 1 } };
        ws.mergeCells(r, 3, r, 7); const b = ws.getCell(r, 3); b.value = v; b.style = { font: F({ italic: kk === 'Lưu ý', color: kk === 'Lưu ý' ? { argb: 'FFC00000' } : undefined }), fill: kk === 'Lưu ý' ? fill(C.note) : undefined, border: BOX, alignment: { vertical: 'top', wrapText: true } };
        ws.getRow(r).height = Math.max(17, lines(v, 190) * 13 + 4); r++;
      }
      // expected vs actual
      ['#', 'Kết quả mong đợi', 'UC · Plan', 'Thực tế', 'Kết quả', 'Ghi chú'].forEach((h, i) => { const c = ws.getCell(r, i + 2); c.value = h; c.style = { font: F({ bold: true, color: { argb: C.white } }), fill: fill('FF44546A'), border: BOX, alignment: { horizontal: 'center', vertical: 'middle' } }; });
      ws.getRow(r).height = 18; r++;
      const bTop = r;
      x.bullets.forEach((b, i) => {
        const vals = [i + 1, plain(b.e.t), planTag(b.e.uc, plan), b.c.actual, null, b.why];
        vals.forEach((v, j) => { const c = ws.getCell(r, j + 2); c.value = v; c.style = { font: F({ size: 9.5 }), border: BOX, alignment: { vertical: 'top', wrapText: true, horizontal: j === 0 ? 'center' : undefined } }; });
        resultCell(ws.getCell(r, 6), b.res);
        ws.getRow(r).height = Math.max(18, Math.max(lines(b.e.t, 58), lines(b.c.actual, 58), lines(b.why, 58), lines(vals[2], 16)) * 12.5 + 6); r++;
      });
      const bEnd = r - 1;
      colourResults(ws, `F${bTop}:F${bEnd}`);
      const early = [...new Set(x.bullets.map(b => b.early).filter(Boolean))];
      x.rs.notes = [...(x.rs.notes || [])]; if (early.length) x.rs.notes.push(`Plan ghi ${early.join(', ')} chưa Done nhưng phần liên quan đã chạy đúng.`);
      if (x.rs.notes && x.rs.notes.length) {
        const a = ws.getCell(r, 2); a.value = 'Ghi chú khi chạy'; a.style = { font: F({ bold: true }), fill: fill(C.grey), border: BOX, alignment: { vertical: 'top', indent: 1, wrapText: true } };
        ws.mergeCells(r, 3, r, 7); const b = ws.getCell(r, 3); b.value = x.rs.notes.map(n => '• ' + n).join('\n'); b.style = { font: F({ size: 9.5 }), border: BOX, alignment: { vertical: 'top', wrapText: true } };
        ws.getRow(r).height = Math.max(17, lines(b.value, 190) * 13 + 4); r++;
      }
      // step result (formula over the bullets, so manual edits flow up)
      const a = ws.getCell(r, 2); a.value = 'Kết quả bước'; a.style = { font: F({ bold: true }), fill: fill(C.lblue), border: BOX, alignment: { vertical: 'middle', indent: 1 } };
      const rng = `F${bTop}:F${bEnd}`;
      const cells = []; for (let q = bTop; q <= bEnd; q++) cells.push(`F${q}`);
      const fml = anyOf(cells);
      ws.mergeCells(r, 3, r, 3); resultCell(ws.getCell(r, 3), x.res); ws.getCell(r, 3).value = { formula: fml, result: x.res }; ws.getCell(r, 3).dataValidation = undefined;
      const bl = ws.getCell(r, 4); bl.value = 'Bug_ID'; bl.style = { font: F({ bold: true }), fill: fill(C.lblue), border: BOX, alignment: { vertical: 'middle', horizontal: 'center' } };
      ws.mergeCells(r, 5, r, 7); ws.getCell(r, 5).style = { border: BOX };
      colourResults(ws, `C${r}`);
      ws.getRow(r).height = 20;
      // summary result cell points at this one
      const sr = ws.getCell(sumRows[k], 6); resultCell(sr, x.res); sr.value = { formula: `C${r}`, result: x.res }; sr.dataValidation = undefined;
      r += 3;
    }
    colourResults(ws, `F${sumTop}:F${sumTop + flow.steps.length - 1}`);
    const cr = ws.getCell(caseRow, 3);
    const refs = sumRows.map(x => `F${x}`);
    cr.value = { formula: anyOf(sumRows.map(x => `F${x}`)), result: caseRes };
    cr.style = { font: F({ bold: true, size: 12 }), border: BOX, alignment: { vertical: 'middle' } };
    colourResults(ws, `C${caseRow}`);
    const counts = ['Passed', 'Failed', 'Blocked', 'Pending'].map(k2 => `${k2} ${stepRes.filter(s => s.res === k2).length}`).join(' · ');
    ws.getCell(caseRow - 1, 3).value = `${ws.getCell(caseRow - 1, 3).value}\nKết quả theo bước: ${counts} / ${flow.steps.length}`;
    ws.getRow(caseRow - 1).height = 32;
    // list link result
    for (let rr = listTop; rr < listTop + flows.length; rr++) if (String(L.getCell(rr, 2).value?.text || L.getCell(rr, 2).value) === id) { const c = L.getCell(rr, 8); resultCell(c, caseRes); c.value = { formula: `'${id}'!$C${caseRow}`, result: caseRes }; c.dataValidation = undefined; }
    console.log(`${id}: ${caseRes} · ${counts}`);
  }
  await wb.xlsx.writeFile(OUT);
  console.log('written', OUT);
})().catch(e => { console.error(e); process.exit(1); });
