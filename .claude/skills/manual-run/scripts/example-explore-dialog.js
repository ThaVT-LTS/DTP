// Exploratory checks of the 2-step "Create customer account" dialog (Operations Console), local main b5cb690.
const L = require('./lib');
const path = require('path');
const fs = require('fs');
const { BASE, visible, text, settle } = L;
const OUT = path.join(__dirname, 'explore-cc'); fs.mkdirSync(OUT, { recursive: true });
const S = L.suffix();
const log = (id, ok, msg) => console.log(`${ok === true ? 'OK ' : ok === false ? 'BUG' : 'NOTE'} [${id}] ${msg}`);

(async () => {
  const browser = await L.launch();
  const ops = await L.signInAs(browser, 'sgsAdmin');
  const shot = n => ops.screenshot({ path: path.join(OUT, n + '.png') });
  const open = async () => { await ops.goto(BASE + '/ops/customers'); await settle(ops); await ops.getByRole('button', { name: /Create customer account/ }).click(); await visible(ops.getByRole('dialog')); return ops.getByRole('dialog'); };
  const stepState = async dlg => dlg.locator('ol li').evaluateAll(lis => lis.map(li => {
    const dot = li.querySelector('span'); const cs = getComputedStyle(dot);
    return { label: li.innerText.replace(/\s+/g, ' ').trim(), current: li.getAttribute('aria-current') === 'step', bg: cs.backgroundColor, tag: li.querySelector('button,a') ? 'clickable' : 'static' };
  }));
  const err = async (dlg, label) => text(dlg.locator(`xpath=.//label[contains(.,"${label}")]/ancestor::*[contains(@class,"flex")][1]`)).catch(() => '');

  // A. step indicator on step 1
  let dlg = await open();
  let st = await stepState(dlg); log('A1', null, 'Bước 1 indicator: ' + JSON.stringify(st));
  await dlg.getByText('Invite initial Customer Admin').click().catch(() => {});
  log('A2', !(await visible(dlg.getByLabel(/^Name/), 800)), 'Bấm chữ bước 2 không chuyển bước');
  await shot('A-step1');

  // B. Next with nothing / whitespace-only company name
  await dlg.locator('input[name=name]').fill('   ');
  await dlg.getByRole('button', { name: 'Next' }).click(); await ops.waitForTimeout(400);
  log('B1', !(await visible(dlg.getByLabel(/^Name/), 800)), 'Company name chỉ có dấu cách → không qua bước 2. Body: ' + (await text(dlg)).slice(0, 220));
  await shot('B-whitespace');

  // C. contact phone garbage, contact email invalid variants
  await dlg.locator('input[name=name]').fill(`QA Explore ${S}`);
  await dlg.locator('input[name=contactPhone]').fill('abc!!!');
  await dlg.locator('input[name=contactEmail]').fill('a@b');
  await dlg.getByRole('button', { name: 'Next' }).click(); await ops.waitForTimeout(400);
  const toStep2 = await visible(dlg.getByLabel(/^Name/), 800);
  log('C1', null, `Contact email "a@b" + phone "abc!!!" → ${toStep2 ? 'QUA bước 2' : 'chặn'}; ${(await text(dlg)).match(/Enter[^.]*\.|Use[^.]*\./g) || 'không có lỗi hiển thị'}`);
  await shot('C-invalid-contact');
  if (toStep2) { await dlg.getByRole('button', { name: 'Back' }).click(); await ops.waitForTimeout(300); }
  await dlg.locator('input[name=contactPhone]').fill('+886 3 578 1234');
  await dlg.locator('input[name=contactEmail]').fill(`yt.chang+${S}@hsinchu-ai.com`);
  await dlg.locator('input[name=contactName]').fill('張雅婷');

  // D. long company name (300 chars)
  const long = 'L'.repeat(300);
  await dlg.locator('input[name=name]').fill(long);
  await dlg.getByRole('button', { name: 'Next' }).click(); await ops.waitForTimeout(400);
  log('D1', null, `Company name 300 ký tự → ${(await visible(dlg.getByLabel(/^Name/), 800)) ? 'QUA bước 2' : 'chặn: ' + ((await text(dlg)).match(/Use at most[^.]*\.?/) || '')}`);
  if (await visible(dlg.getByLabel(/^Name/), 300)) { await dlg.getByRole('button', { name: 'Back' }).click(); await ops.waitForTimeout(300); }
  await dlg.locator('input[name=name]').fill(`QA Explore ${S}`);

  // E. step 2 state, prefill, intro line
  await dlg.getByRole('button', { name: 'Next' }).click(); await visible(dlg.getByLabel(/^Name/));
  st = await stepState(dlg); log('E1', null, 'Bước 2 indicator: ' + JSON.stringify(st));
  log('E2', (await dlg.getByLabel(/^Name/).inputValue()) === '張雅婷' && (await dlg.getByLabel(/^Email/).inputValue()) === `yt.chang+${S}@hsinchu-ai.com`, 'Name/Email tự điền từ Contact');
  log('E3', null, 'Dòng đầu bước 2: ' + (await text(dlg.getByText(/The Customer Admin invites/))));
  await shot('E-step2');

  // F. back keeps data; change contact; prefill not refreshed
  await dlg.getByRole('button', { name: 'Back' }).click(); await ops.waitForTimeout(300);
  log('F1', (await dlg.locator('input[name=name]').inputValue()) === `QA Explore ${S}`, 'Back giữ Company name');
  await dlg.locator('input[name=contactName]').fill('Kevin Wu');
  await dlg.locator('input[name=name]').fill(`QA Explore ${S} B`);
  await dlg.getByRole('button', { name: 'Next' }).click(); await visible(dlg.getByLabel(/^Name/));
  const nm = await dlg.getByLabel(/^Name/).inputValue();
  log('F2', nm === 'Kevin Wu', `Đổi Contact name thành Kevin Wu rồi Next → ô Name = "${nm}"`);
  log('F3', /QA Explore .* B ·/.test(await text(dlg.getByText(/The Customer Admin invites/))), 'Dòng đầu cập nhật tên công ty mới: ' + (await text(dlg.getByText(/The Customer Admin invites/))));
  await shot('F-after-back');

  // G. step 2 validation
  await dlg.getByLabel(/^Name/).fill('');
  await dlg.getByLabel(/^Email/).fill('abc@');
  await dlg.getByRole('button', { name: /Create and send invitation/ }).click(); await ops.waitForTimeout(500);
  log('G1', null, 'Bước 2 Name trống + Email "abc@": ' + ((await text(dlg)).match(/Enter[^.]*\./g) || 'không có lỗi'));
  await shot('G-step2-errors');
  await dlg.getByLabel(/^Name/).fill('   ');
  await dlg.getByLabel(/^Email/).fill(`yt.chang+${S}@hsinchu-ai.com`);
  await dlg.getByRole('button', { name: /Create and send invitation/ }).click(); await ops.waitForTimeout(500);
  log('G2', await visible(dlg.getByText('Enter the name.'), 800), 'Name chỉ dấu cách bị chặn');

  // H. close on step 2 → discard; reopen at step 1 empty
  await ops.keyboard.press('Escape'); await ops.waitForTimeout(400);
  const discard = await visible(ops.getByText('Discard unsaved changes?'), 1500);
  log('H1', discard, 'Esc ở bước 2 → hỏi Discard unsaved changes?');
  await shot('H-discard');
  if (discard) { await ops.getByRole('button', { name: 'Discard changes' }).click(); await ops.waitForTimeout(800); }
  dlg = await open();
  st = await stepState(dlg);
  log('H2', st[0] && st[0].current && !(await dlg.locator('input[name=name]').inputValue()), 'Mở lại: về bước 1, form trống');

  // I. Enter key on step 1 / double submit
  await dlg.locator('input[name=name]').fill(`QA Explore ${S} C`);
  await dlg.locator('input[name=name]').press('Enter'); await ops.waitForTimeout(500);
  log('I1', null, `Enter ở bước 1 → ${(await visible(dlg.getByLabel(/^Name/), 600)) ? 'sang bước 2' : 'không làm gì'}`);
  if (!(await visible(dlg.getByLabel(/^Name/), 300))) { await dlg.getByRole('button', { name: 'Next' }).click(); }
  await dlg.getByLabel(/^Name/).fill('QA Admin C');
  await dlg.getByLabel(/^Email/).fill(`qa.c+${S}@example.com`);
  const btn = dlg.getByRole('button', { name: /Create and send invitation/ });
  await btn.click(); const disabledAfter = await btn.isDisabled().catch(() => 'detached'); await btn.click({ timeout: 800 }).catch(() => {}); await btn.click({ timeout: 800 }).catch(() => {});
  log('I3', disabledAfter === true || disabledAfter === 'detached', 'Nút Create khoá ngay sau lần bấm đầu: ' + disabledAfter);
  await settle(ops, 1500);
  const rows = await L.db().query(`select count(*)::int n from tenant where name = $1`, [`QA Explore ${S} C`]).catch(e => ({ rows: [{ n: 'n/a ' + e.message }] }));
  log('I2', rows.rows[0].n === 1, `Bấm nhanh 3 lần Create → số khách hàng tạo ra: ${rows.rows[0].n}`);

  // J. invite an email that already belongs to another customer / same email again
  dlg = await open();
  await dlg.locator('input[name=name]').fill(`QA Explore ${S} D`);
  await dlg.getByRole('button', { name: 'Next' }).click(); await visible(dlg.getByLabel(/^Name/));
  await dlg.getByLabel(/^Name/).fill('Kevin Lin'); await dlg.getByLabel(/^Email/).fill('kevin.lin@example.com');
  await dlg.getByRole('button', { name: /Create and send invitation/ }).click(); await settle(ops, 1500);
  log('J1', null, `Mời email đã là Customer Admin của khách hàng khác (kevin.lin) → ${(await visible(ops.getByRole('dialog'), 500)) ? 'hộp thoại còn mở: ' + ((await text(ops.getByRole('dialog'))).match(/This email[^.]*\.|Something[^.]*\.|could not[^.]*\./) || '') : 'tạo xong, url ' + new URL(ops.url()).pathname}`);
  await shot('J-existing-email');
  if (await visible(ops.getByRole('dialog'), 300)) { await ops.keyboard.press('Escape'); await ops.getByRole('button', { name: 'Discard changes' }).click().catch(() => {}); }
  dlg = await open();
  await dlg.locator('input[name=name]').fill(`QA Explore ${S} E`);
  await dlg.getByRole('button', { name: 'Next' }).click(); await visible(dlg.getByLabel(/^Name/));
  await dlg.getByLabel(/^Name/).fill('Lin Mei'); await dlg.getByLabel(/^Email/).fill('lin.mei@example.com');
  await dlg.getByRole('button', { name: /Create and send invitation/ }).click(); await settle(ops, 1500);
  log('J2', null, `Mời email của SGS Admin (lin.mei) làm Customer Admin → ${(await visible(ops.getByRole('dialog'), 500)) ? 'hộp thoại còn mở: ' + ((await text(ops.getByRole('dialog'))).match(/This email[^.]*\.|Something[^.]*\.|[^.]*refused[^.]*\./i) || (await text(ops.getByRole('dialog'))).slice(-160)) : 'tạo xong, url ' + new URL(ops.url()).pathname}`);
  await shot('J-sgs-email');

  // K. zh-TW: step labels
  await ops.goto(BASE + '/ops/customers'); await settle(ops);
  await browser.close(); await L.closeDb();
  console.log('screenshots:', OUT);
})().catch(e => { console.error('FATAL', e); process.exit(1); });
