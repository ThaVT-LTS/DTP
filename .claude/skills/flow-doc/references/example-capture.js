// WEB: same scope gets a Bulk workspace next to its Assisted one (for the Scope > Framework > Workspace doc).
const OUT = 'C:/Users/thavt/Documents/DTP/dts-agent-workspace/tests/evidence/scope-framework-workspace-05-11';
const M = require('./mk.js')(OUT); const { mark, shot, dlg, L, H } = M; const one = s => (s || '').replace(/\s+/g, ' ').trim();
const SCOPE = '[QA] D05 Smoke Assisted Org 0851', BULK_NAME = '[QA] D05 Smoke Bulk WS 0851';
(async () => {
  if (!L.BASE.includes('dtp.ltsgroup.tech')) throw new Error('not web');
  const b = await L.launch();
  const p = await H.page(b, 'admin', { viewport: { width: 1440, height: 960 } });
  const scopes = await H.api(p, 'GET', '/scopes?q=' + encodeURIComponent('D05 Smoke Assisted Org'));
  const sc = (scopes.body.data || []).find(x => x.name === SCOPE); if (!sc) throw new Error('scope not found ' + JSON.stringify(scopes.body).slice(0, 300));
  await p.goto(L.BASE + '/scopes/' + sc.id); await L.settle(p, 2500);
  console.log('scope', one(await p.locator('main').innerText()).slice(0, 500));
  const cw = p.getByRole('button', { name: /Create workspace/ }).first();
  await cw.click(); await p.waitForTimeout(700);
  await mark(p, p.getByRole('menuitem', { name: /Assisted/i }), 'Assisted: requirements + evidence, tier', 'left');
  await mark(p, p.getByRole('menuitem', { name: /Bulk/i }), 'Bulk: upload documents, sent to NirmatAI', 'left');
  await shot(p, '10a-scope-create-menu.png');
  await p.getByRole('menuitem', { name: /Bulk/i }).click();
  const d = dlg(p); await d.waitFor(); await p.waitForTimeout(1200);
  console.log('bulk dlg', one(await d.innerText()).slice(0, 400));
  // Opened from the scope page, the scope may already be chosen; pick it if step 1 is shown.
  const r = d.getByRole('radio', { name: new RegExp(SCOPE.replace(/[[\]]/g, '\\$&')) });
  if (await r.count()) { await r.first().check().catch(() => r.first().click({ force: true })); await d.getByRole('button', { name: /^Next$/ }).click(); await L.settle(p, 1800); }
  const std = d.getByRole('radio', { name: /27001/ }); await std.first().check().catch(() => std.first().click({ force: true }));
  await mark(p, d.locator('label').filter({ hasText: /27001/ }).first(), 'Only NirmatAI frameworks activated by SGS', 'top');
  await shot(p, '10b-bulk-standard.png');
  await d.getByRole('button', { name: /^Next$/ }).click(); await L.settle(p, 1500);
  const nm = d.getByLabel(/Workspace name/); if (await nm.count()) await nm.fill(BULK_NAME);
  await mark(p, d.getByText(new RegExp('Scope: ' + SCOPE.replace(/[[\]]/g, '\\$&'))).first(), 'Same scope as the Assisted workspace', 'top');
  await mark(p, d.getByRole('button', { name: /^Create workspace$/ }), 'No tier for Bulk', 'left');
  await shot(p, '10c-bulk-details.png');
  await d.getByRole('button', { name: /^Create workspace$/ }).click(); await L.settle(p, 3000);
  console.log('after create', p.url(), one(await p.locator('main').innerText()).slice(0, 300));
  await mark(p, p.locator('main h1').first(), 'Bulk workspace created', 'top');
  await mark(p, p.getByRole('button', { name: /Open documents/ }).or(p.getByRole('link', { name: /Open documents/ })), 'Next: upload documents (see the NirmatAI flow)', 'left');
  await shot(p, '10d-bulk-created.png');
  await p.goto(L.BASE + '/scopes/' + sc.id); await L.settle(p, 2500);
  const wsCard = p.getByRole('heading', { name: /^Workspaces/ }).first();
  if (await wsCard.count()) { await wsCard.scrollIntoViewIfNeeded(); await p.waitForTimeout(500); }
  await mark(p, p.locator('main').getByText('[QA] D05 Smoke Assisted WS 0851').first(), 'Assisted workspace', 'right');
  await mark(p, p.locator('main').getByText(BULK_NAME).first(), 'Bulk workspace', 'right');
  await shot(p, '10e-scope-both-workspaces.png');
  await p.goto(L.BASE + '/workspaces'); await L.settle(p, 2000);
  const s = p.getByPlaceholder(/Search/).first(); if (await s.count()) { await s.fill('D05 Smoke'); await p.waitForTimeout(1500); await L.settle(p, 800); }
  console.log('ws list', one(await p.locator('main').innerText()).slice(0, 500));
  await mark(p, p.getByRole('row').filter({ hasText: '[QA] D05 Smoke Assisted WS 0851' }), 'Assisted', 'bottom');
  await mark(p, p.getByRole('row').filter({ hasText: BULK_NAME }), 'Bulk', 'bottom');
  await shot(p, '10f-workspaces-list.png');
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
