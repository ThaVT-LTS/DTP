// Builds apply-plan.json for apply-tc.ps1 from out/*.json (verdict Xoá → delete row; questions Đóng → delete row)
// and edits/*.json (new cell values). Columns: name H(8) pre I(9) steps J(10) expected K(11) openQuestion W(23) uc X(24).
const fs = require('fs');
const path = require('path');
const R = __dirname;
const COL = { c1: 2, c2: 3, c3: 4, c4: 5, name: 8, pre: 9, steps: 10, expected: 11, openQuestion: 23, uc: 24 };
const SHEETS = ['Login', 'Users', 'Customers', 'Frameworks', 'Scopes', 'Workspaces', 'Workspace detail', 'Documents', 'Profile', 'Notifications', 'Audit Logs'];
const plan = { sheets: [], questionDeletes: [], warnings: [] };
const closedQ = [];
for (const s of SHEETS) {
  const f = s.replace(/ /g, '_') + '.json';
  const out = JSON.parse(fs.readFileSync(path.join(R, 'out', f), 'utf8'));
  const input = JSON.parse(fs.readFileSync(path.join(R, 'in', f), 'utf8')).cases;
  const ed = fs.existsSync(path.join(R, 'edits', f)) ? JSON.parse(fs.readFileSync(path.join(R, 'edits', f), 'utf8')).edits : null;
  if (!ed) plan.warnings.push(`${s}: chưa có edits`);
  const deletes = out.cases.filter(c => c.verdict === 'Xoá').map(c => c.row);
  const cells = [];
  for (const e of ed || []) {
    const inp = input.find(c => c.row === e.row);
    if (!inp || inp.tc !== e.tc) { plan.warnings.push(`${s}: edit row ${e.row} ${e.tc} không khớp input (${inp && inp.tc})`); continue; }
    if (deletes.includes(e.row)) { plan.warnings.push(`${s}: ${e.tc} vừa Xoá vừa có edit — bỏ edit`); continue; }
    for (const [k, col] of Object.entries(COL)) if (e[k] !== undefined && e[k] !== inp[k]) cells.push({ row: e.row, col, value: String(e[k]) });
  }
  plan.sheets.push({ name: s, deletes: deletes.sort((a, b) => b - a), cells, nEdits: (ed || []).length });
  for (const q of out.questions || []) if (q.decision === 'Đóng') closedQ.push(q);
}
const allQ = JSON.parse(fs.readFileSync(path.join(R, 'in', 'Can_xac_nhan.json'), 'utf8'));
for (const q of closedQ) { const m = allQ.find(x => x.row === q.row && x.id === q.id) || allQ.find(x => x.id === q.id); if (m) plan.questionDeletes.push(m.row); else plan.warnings.push(`Câu hỏi ${q.id} không tìm thấy`); }
plan.questionDeletes = [...new Set(plan.questionDeletes)].sort((a, b) => b - a);
fs.writeFileSync(path.join(R, 'apply-plan.json'), JSON.stringify(plan, null, 1));
for (const s of plan.sheets) console.log(s.name.padEnd(18), 'delete', String(s.deletes.length).padStart(3), '· edits', String(s.nEdits).padStart(3), '· cells', s.cells.length);
console.log('Cần xác nhận delete', plan.questionDeletes.length);
plan.warnings.forEach(w => console.log('WARN', w));
