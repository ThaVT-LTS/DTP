// Recorder v2: one result per expected bullet (flows2/<ID>.json → steps[].exp[i]).
// Output ../xl/runs2/<ID>.json: { id, env, runAt, steps: [{ n, checks: [{ e, ok, actual }], notes, shot }] }
// ok: true = đạt · false = không đạt · 'absent' = màn/chức năng chưa có, không kiểm được.
const path = require('path');
const fs = require('fs');
const { ENV } = require('./lib');

function run2(id) {
  const flow = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'xl', 'flows2', id + '.json'), 'utf8'));
  const dir = path.join(__dirname, '..', 'xl', 'runs2', id);
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
  const steps = [];
  const sym = ok => (ok === true ? '✔' : ok === false ? '✘' : '⛔');
  return {
    flow, dir,
    async step(n, page, fn) {
      const r = { n, checks: [], notes: [] };
      const exp = flow.steps[n - 1].exp;
      try { await fn(r); } catch (e) { r.notes.push('Lỗi khi chạy: ' + String(e.message).split('\n')[0].slice(0, 220)); }
      // expectations the script never reached are "not checked"
      exp.forEach((_, i) => { if (!r.checks.some(c => c.e === i + 1)) r.checks.push({ e: i + 1, ok: 'absent', actual: r.stopReason || 'Không kiểm được (bước dừng trước khi tới)' }); });
      r.checks.sort((a, b) => a.e - b.e);
      if (page && !r.shot) { try { await page.screenshot({ path: path.join(dir, `step${n}.png`) }); r.shot = `step${n}.png`; } catch {} }
      steps.push(r);
      console.log(`Bước ${n} · ${flow.steps[n - 1].title}`);
      r.checks.forEach(c => console.log(`   ${sym(c.ok)} [${c.e}] ${exp[c.e - 1].t}\n        → ${c.actual}`));
      r.notes.forEach(x => console.log('   • ' + x));
      return r;
    },
    /** Record expectation #e (1-based) of the current step. */
    exp(r, e, ok, actual) { r.checks = r.checks.filter(c => c.e !== e); r.checks.push({ e, ok, actual }); return ok === true; },
    /** Mark every remaining expectation of the step as not checkable, with the reason. */
    absent(r, reason) { r.stopReason = reason; },
    note(r, msg) { r.notes.push(msg); },
    async shot(r, page, name) { const f = `step${r.n}-${name}.png`; await page.screenshot({ path: path.join(dir, f) }); r.shot = f; },
    finish() {
      steps.sort((a, b) => a.n - b.n);
      fs.writeFileSync(path.join(dir, '..', id + '.json'), JSON.stringify({ id, env: ENV, runAt: new Date().toISOString(), steps }, null, 1));
    },
  };
}
module.exports = { run2 };
