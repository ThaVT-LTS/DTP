// Shared helpers for the Wave 1 E2E flow runs (local app). One script per flow: run-<id>.js.
// Output: ../xl/runs/<ID>.json + ../xl/runs/<ID>/*.png, read by ../xl/build-e2e-v2.js.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { Pool } = require('pg');

const BASE = process.env.BASE_URL || 'http://localhost:3000';
const MAILPIT = process.env.MAILPIT_URL || 'http://localhost:8025';
const DEV_PASSWORD = 'password'; // local dev sign-in: one shared password for every account
const EXE = path.join(process.env.LOCALAPPDATA, 'ms-playwright', 'chromium-1228', 'chrome-win64', 'chrome.exe');
const ENV = 'Local (máy QC) · web + backend dev, Postgres/Mailpit trên Docker · đăng nhập dev · DB seed lại 19/10/2026';
const LOGIN = { customer: '/login', ops: '/ops/login', consultant: '/consultant/login' };
/** Dev-seed accounts (password "password"). */
const SEED = {
  sgsAdmin: { email: 'lin.mei@example.com', portal: 'ops' },
  customerAdmin: { email: 'kevin.lin@example.com', portal: 'customer' },
  customerUser: { email: 'jason.chen@example.com', portal: 'customer' },
  customerViewer: { email: 'peggy.lai@example.com', portal: 'customer' },
  consultant: { email: 'chen.wei@example.com', portal: 'consultant' },
};

/** Short unique suffix (HHMM + 2 random digits) so every run creates its own data. */
const suffix = () => new Date().toTimeString().slice(0, 5).replace(':', '') + String(Math.floor(Math.random() * 90 + 10));
const sleep = ms => new Promise(r => setTimeout(r, ms));
const visible = async (loc, t = 5000) => { try { await loc.first().waitFor({ state: 'visible', timeout: t }); return true; } catch { return false; } };
const text = async loc => ((await loc.first().innerText().catch(() => '')) || '').replace(/\s+/g, ' ').trim();

async function launch() {
  return chromium.launch({ executablePath: EXE });
}
async function newPage(browser, opts = {}) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: opts.locale || 'en-US' });
  return ctx.newPage();
}
async function settle(page, ms = 800) {
  await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(ms);
}
async function signIn(page, email, portal = 'customer', password = DEV_PASSWORD) {
  await page.goto(BASE + LOGIN[portal], { timeout: 120000 });
  await page.getByLabel(/^Email/).fill(email);
  await page.getByLabel(/^Password/).fill(password);
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.waitForURL(u => !/\/login$/.test(u.pathname), { timeout: 30000 });
  await settle(page);
}
async function signInAs(browser, role) {
  const page = await newPage(browser);
  await signIn(page, SEED[role].email, SEED[role].portal);
  return page;
}

/** Recorder for one flow. step() never throws; a thrown error marks the step Failed with the message. */
function run(id) {
  const dir = path.join(__dirname, '..', 'xl', 'runs', id);
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
  const steps = [];
  const api = {
    dir,
    /** fn(r) records checks on r; return value ignored. Screenshot of `page` saved as the step's actual image. */
    async step(n, title, page, fn) {
      const r = { n, title, result: 'Passed', notes: [] };
      try { await fn(r); } catch (e) { r.result = 'Failed'; r.notes.push('✘ Lỗi khi chạy: ' + String(e.message).split('\n')[0].slice(0, 220)); }
      if (page && !r.shot) { try { await page.screenshot({ path: path.join(dir, `step${n}.png`) }); r.shot = `step${n}.png`; } catch {} }
      steps.push(r);
      console.log(`Bước ${n} [${r.result}] ${title}\n   ${r.notes.join('\n   ')}`);
      return r;
    },
    /** Save a named screenshot and use it as the step's actual image. */
    async shot(r, page, name) { const f = `step${r.n}-${name}.png`; await page.screenshot({ path: path.join(dir, f) }); r.shot = f; },
    check(r, ok, msg) { if (ok) r.notes.push('✔ ' + msg); else { if (r.result !== 'Blocked') r.result = 'Failed'; r.notes.push('✘ ' + msg); } return ok; },
    /** Observation that does not change the result (e.g. differs from Figma, needs dev check). */
    warn(r, msg) { r.notes.push('⚠ ' + msg); },
    info(r, msg) { r.notes.push(msg); },
    block(r, why) { r.result = 'Blocked'; r.notes.push('⛔ ' + why); },
    /** Record a step that cannot run at all. */
    blocked(n, title, why) { const r = { n, title, result: 'Blocked', notes: ['⛔ ' + why] }; steps.push(r); console.log(`Bước ${n} [Blocked] ${title}\n   ⛔ ${why}`); return r; },
    failedBefore() { return steps.some(s => s.result === 'Failed'); },
    finish() {
      steps.sort((a, b) => a.n - b.n);
      fs.writeFileSync(path.join(dir, '..', id + '.json'), JSON.stringify({ id, env: ENV, steps }, null, 1));
      const c = s => steps.filter(x => x.result === s).length;
      console.log(`== ${id}: Passed ${c('Passed')} · Failed ${c('Failed')} · Blocked ${c('Blocked')} / ${steps.length}`);
    },
  };
  return api;
}

// ------------------------------------------------------------------ Mailpit
async function mails(to) {
  const res = await fetch(`${MAILPIT}/api/v1/search?query=${encodeURIComponent('to:' + to)}`).then(r => r.json()).catch(() => ({}));
  return res.messages || [];
}
/** Waits for the newest mail to `to` (optionally whose subject matches `re`, received after `since` ms). */
async function waitMail(to, { re, since = 0, timeout = 30000 } = {}) {
  const end = Date.now() + timeout;
  while (Date.now() < end) {
    const m = (await mails(to)).find(x => (!re || re.test(x.Subject)) && new Date(x.Created).getTime() >= since - 2000);
    if (m) {
      const full = await fetch(`${MAILPIT}/api/v1/message/${m.ID}`).then(r => r.json());
      const html = String(full.HTML || ''), body = String(full.Text || '');
      const links = (html + ' ' + body).match(/https?:\/\/[^"'\s<>]+/g) || [];
      return { id: m.ID, subject: full.Subject, text: body, html, links: links.map(u => u.replace(/&amp;/g, '&')), viewUrl: `${MAILPIT}/view/${m.ID}` };
    }
    await sleep(1500);
  }
  return null;
}
const localLink = u => u.replace(/^https?:\/\/[^/]+/, BASE);

// ------------------------------------------------------------------ database (local docker postgres, superuser)
let pool;
function db() { pool ??= new Pool({ connectionString: process.env.DB_URL || 'postgresql://sgs_dtp:sgs_dtp_local@localhost:5432/sgs_dtp', max: 2 }); return pool; }
async function closeDb() { if (pool) await pool.end(); pool = undefined; }

// ------------------------------------------------------------------ activation of an invited user (from an invitation mail)
async function activateFromMail(browser, email, name, { since = 0 } = {}) {
  const mail = await waitMail(email, { re: /invited/i, since });
  if (!mail) throw new Error(`Không thấy email mời gửi tới ${email}`);
  const link = mail.links.find(u => /activate/i.test(u));
  if (!link) throw new Error('Email mời không có link kích hoạt');
  const page = await newPage(browser);
  await page.goto(localLink(link), { timeout: 60000 });
  await settle(page);
  const full = page.getByLabel(/^Full name/);
  if (await visible(full, 3000) && !(await full.inputValue())) await full.fill(name);
  await page.getByLabel(/^Create password/).fill('Hsinchu#2026Secure');
  await page.getByLabel(/^Confirm password/).fill('Hsinchu#2026Secure');
  await page.getByRole('checkbox').first().check();
  await page.getByRole('button', { name: /Activate account/ }).click();
  await settle(page, 1500);
  return { page, mail };
}

/**
 * Precondition helper: SGS Admin (Lin Mei) creates customer `company` and invites its first Customer Admin,
 * who activates and signs in. Returns { ops, admin, company, adminEmail, customerHref }.
 * Pages: ops = signed-in SGS Admin, admin = signed-in Customer Admin of the new customer.
 */
async function onboardCustomer(browser, { company, companyZh = '新竹人工智慧實驗室股份有限公司', contact = '張雅婷', adminEmail, phone = '+886 3 578 1234' }) {
  const ops = await signInAs(browser, 'sgsAdmin');
  await ops.goto(BASE + '/ops/customers'); await settle(ops);
  await ops.getByRole('button', { name: /Create customer account/ }).click();
  const dlg = ops.getByRole('dialog');
  await dlg.locator('input[name=name]').fill(company);
  await dlg.locator('input[name=nameZh]').fill(companyZh);
  await dlg.locator('input[name=contactName]').fill(contact);
  await dlg.locator('input[name=contactEmail]').fill(adminEmail);
  await dlg.locator('input[name=contactPhone]').fill(phone);
  await dlg.getByRole('button', { name: 'Next' }).click();
  await dlg.getByLabel(/^Name/).fill(contact);
  await dlg.getByLabel(/^Email/).fill(adminEmail);
  const since = Date.now();
  await dlg.getByRole('button', { name: /Create and send invitation/ }).click();
  await dlg.waitFor({ state: 'hidden', timeout: 15000 });
  await settle(ops);
  // After creating, the app opens the new customer's detail page.
  let customerHref = new URL(ops.url()).pathname;
  if (!/^\/ops\/customers\/[^/]+$/.test(customerHref)) {
    await ops.goto(BASE + '/ops/customers'); await settle(ops);
    customerHref = await ops.locator('a[href*="/ops/customers/"]').filter({ hasText: company }).first().getAttribute('href');
  }
  const { page } = await activateFromMail(browser, adminEmail, contact, { since });
  await page.close();
  const admin = await newPage(browser);
  await signIn(admin, adminEmail, 'customer');
  return { ops, admin, company, adminEmail, customerHref };
}

module.exports = {
  BASE, MAILPIT, DEV_PASSWORD, SEED, ENV, path, fs,
  suffix, sleep, visible, text, launch, newPage, settle, signIn, signInAs, run,
  mails, waitMail, localLink, db, closeDb, activateFromMail, onboardCustomer,
};
