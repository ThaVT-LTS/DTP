// Builds writeback.json: new TC ids (by row order), Round 1 results, and the question-sheet references.
const fs = require('fs');
const path = require('path');
const T = __dirname;
const cases = JSON.parse(fs.readFileSync(path.join(T, 'customers-cases.json'), 'utf8'));
const results = [];
for (const g of ['A', 'B', 'C', 'D']) {
  const f = path.join(T, 'results', g + '.json');
  if (fs.existsSync(f)) results.push(...JSON.parse(fs.readFileSync(f, 'utf8')));
}
const ALLOWED = ['Passed', 'Failed', 'Pending', 'Blocked', 'NA'];
const warn = [];
// one local bug code per distinct bug title (to be replaced by tracker ids)
const bugCodes = new Map();
const rows = cases.map(c => {
  const r = results.find(x => x.tc === c.tc);
  if (!r) warn.push(`no result for ${c.tc} (${c.old})`);
  else if (!ALLOWED.includes(r.result)) warn.push(`bad result ${r.result} for ${c.tc}`);
  let bug = '';
  if (r && r.result === 'Failed' && r.bug) {
    const key = r.bug.trim().toLowerCase();
    if (!bugCodes.has(key)) bugCodes.set(key, { code: 'CU-BUG-' + String(bugCodes.size + 1).padStart(2, '0'), title: r.bug.trim(), tcs: [] });
    bugCodes.get(key).tcs.push(c.tc); bug = bugCodes.get(key).code;
  }
  return { row: c.row, old: c.old, tc: c.tc, result: r ? r.result : '', remark: r ? (bug ? `[${bug}] ${r.bug}\n` : '') + r.remark : '', bug };
});
const byOld = Object.fromEntries(cases.map(c => [c.old, c.tc]));
const byName = re => cases.filter(c => re.test(c.c4) || re.test(c.name)).map(c => c.tc).join(', ');
const q = {
  'Q-CU-07': 'Customers ' + byOld['TC_010'],
  'Q-CU-08': 'Customers ' + byOld['TC_031'],
  'Q-CU-09': 'Customers ' + byOld['TC_035'],
  'Q-CU-12': 'Customers ' + cases.filter(c => c.c3 === 'Quá độ dài').map(c => c.tc).join(', '),
  'Q-CU-13': 'Customers ' + byName(/Contact phone có chữ/),
  'Q-CU-14': 'Customers ' + byName(/Customer Admin của khách hàng khác|Khác chữ hoa/),
  'Q-CU-15': 'Customers ' + byName(/Email của tài khoản SGS/),
  'Q-CU-16': 'Customers ' + byName(/Back, đổi Contact/),
};
const out = { sheet: 'Customers', questionSheet: 'Cần xác nhận', tester: 'Auto (Claude) · localhost main b5cb690', date: '19/10/2026', rows, questionRefs: q, bugs: [...bugCodes.values()] };
fs.writeFileSync(path.join(T, 'writeback.json'), JSON.stringify(out, null, 1));
const cnt = {}; rows.forEach(r => (cnt[r.result || '(none)'] = (cnt[r.result || '(none)'] || 0) + 1));
console.log('results', JSON.stringify(cnt), '| bugs', bugCodes.size);
console.log(JSON.stringify(q, null, 1));
warn.forEach(w => console.log('WARN', w));
