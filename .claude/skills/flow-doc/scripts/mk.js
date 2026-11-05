// Annotated screenshots for flow documents: red box + red label, URL bar on top.
// const M = require('./mk.js')(OUT); await M.mark(p, locator, 'label', 'top|bottom|left|right'); await M.shot(p, 'name.png');
// Needs the project's Playwright helper (H.page(browser, role), L.launch/settle/BASE); path via QA_HELPER.
const H = require(process.env.QA_HELPER || './h.js'); const { L, path } = H;
module.exports = OUT => {
  require('fs').mkdirSync(OUT, { recursive: true });
  const clear = p => p.evaluate(() => document.querySelectorAll('.__qa_mark').forEach(e => e.remove())).catch(() => {});
  // Marks are drawn after the URL bar is added, so boxes line up with the shifted page.
  const pending = new WeakMap();
  async function mark(p, loc, label, pos = 'top') {
    const l = loc.first(); if (!(await l.count())) { console.log('  no mark:', label); return false; }
    if (!(await l.boundingBox().catch(() => null))) { console.log('  no box:', label); return false; }
    const list = pending.get(p) || []; list.push([l, label, pos]); pending.set(p, list); return true;
  }
  async function draw(p) {
    for (const [l, label, pos] of pending.get(p) || []) {
      const bb = await l.boundingBox().catch(() => null); if (!bb) continue;
      await p.evaluate(([bb, label, pos]) => {
        const d = document.createElement('div'); d.className = '__qa_mark';
        Object.assign(d.style, { position: 'fixed', left: bb.x - 4 + 'px', top: bb.y - 4 + 'px', width: bb.width + 8 + 'px', height: bb.height + 8 + 'px', border: '3px solid #e00000', zIndex: 2147483646, pointerEvents: 'none', boxSizing: 'border-box' });
        document.body.appendChild(d);
        if (!label) return;
        const t = document.createElement('div'); t.className = '__qa_mark'; t.textContent = label;
        const s = { position: 'fixed', color: '#e00000', font: 'bold 14px Arial, sans-serif', background: 'rgba(255,255,255,.92)', padding: '1px 5px', zIndex: 2147483646, pointerEvents: 'none', whiteSpace: 'nowrap' };
        if (pos === 'top') Object.assign(s, { left: bb.x - 4 + 'px', top: Math.max(34, bb.y - 26) + 'px' });
        if (pos === 'bottom') Object.assign(s, { left: bb.x - 4 + 'px', top: bb.y + bb.height + 6 + 'px' });
        if (pos === 'left') Object.assign(s, { right: (window.innerWidth - bb.x + 10) + 'px', top: bb.y + bb.height / 2 - 10 + 'px' });
        if (pos === 'right') Object.assign(s, { left: bb.x + bb.width + 10 + 'px', top: bb.y + bb.height / 2 - 10 + 'px' });
        Object.assign(t.style, s); document.body.appendChild(t);
      }, [bb, label, pos]);
    }
    pending.set(p, []);
  }
  async function shot(p, name) {
    await p.waitForTimeout(400);
    // Same URL bar as L.shotWithUrl, but marks are drawn after the page shifts.
    const url = p.url();
    await p.evaluate(u => {
      const d = document.createElement('div'); d.id = '__qa_urlbar'; d.textContent = '🔒 ' + u + '    ·    ' + new Date().toLocaleString('en-GB', { timeZone: 'Asia/Ho_Chi_Minh' }) + ' (GMT+7)';
      Object.assign(d.style, { position: 'fixed', top: '0', left: '0', right: '0', zIndex: '2147483647', background: '#f1f3f4', color: '#202124', font: '13px Arial, sans-serif', padding: '7px 12px', borderBottom: '1px solid #c4c7c5', pointerEvents: 'none' });
      document.body.appendChild(d); document.body.style.paddingTop = (parseInt(getComputedStyle(document.body).paddingTop) || 0) + 32 + 'px';
    }, url).catch(() => {});
    await p.waitForTimeout(200); await draw(p);
    await p.screenshot({ path: path.join(OUT, name) });
    await p.evaluate(() => { const d = document.getElementById('__qa_urlbar'); if (d) { d.remove(); document.body.style.paddingTop = (parseInt(getComputedStyle(document.body).paddingTop) || 32) - 32 + 'px'; } }).catch(() => {});
    await clear(p); console.log('shot', name);
  }
  const dlg = p => p.locator('[role=dialog],[role=alertdialog]').last();
  return { mark, shot, dlg, L, H };
};
