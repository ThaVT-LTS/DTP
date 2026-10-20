// E2E1_001 (format v2) · Onboard khách hàng mới → mời Customer Admin → email → kích hoạt → Customer Portal
const L = require('./lib');
const { run2 } = require('./rec2');
const { BASE, visible, text, settle } = L;

(async () => {
  const R = run2('E2E1_001');
  const S = L.suffix();
  const D = { company: `Hsinchu AI Labs ${S}`, companyZh: '新竹人工智慧實驗室股份有限公司', contact: '張雅婷', email: `yt.chang+${S}@hsinchu-ai.com`, phone: '+886 3 578 1234' };
  const browser = await L.launch();
  const ops = await L.signInAs(browser, 'sgsAdmin');
  let detailHref = null, mail = null, invitedAt = 0, portal = null;

  await R.step(1, ops, async r => {
    await ops.getByRole('link', { name: 'Customers' }).first().click(); await settle(ops);
    await ops.getByRole('button', { name: /Create customer account/ }).click();
    const dlg = ops.getByRole('dialog');
    const open = await visible(dlg.getByText('Create customer account'));
    const step1 = await visible(dlg.getByText('Account', { exact: true }));
    R.exp(r, 1, open && step1, open ? (step1 ? 'Hộp thoại Create customer account mở, bước 1 Account đang chọn' : 'Hộp thoại mở nhưng không thấy bước 1 Account') : 'Không mở hộp thoại');
  });

  await R.step(2, ops, async r => {
    const dlg = ops.getByRole('dialog');
    await dlg.locator('input[name=name]').fill(D.company);
    await dlg.locator('input[name=nameZh]').fill(D.companyZh);
    await dlg.locator('input[name=contactName]').fill(D.contact);
    await dlg.locator('input[name=contactEmail]').fill(D.email);
    await dlg.locator('input[name=contactPhone]').fill(D.phone);
    const aff = dlg.getByLabel(/SGS affiliate/);
    const val = await aff.inputValue().catch(() => '');
    const editable = await aff.isEditable().catch(() => false);
    R.exp(r, 1, val === 'SGS Taiwan' && !editable, `Ô SGS affiliate = "${val}", ${editable ? 'sửa được' : 'không sửa được'}`);
    const helper = await visible(dlg.getByText(/Your affiliate\. New customers always belong to it\./), 1500);
    R.exp(r, 2, helper, helper ? 'Có dòng "Your affiliate. New customers always belong to it."' : 'Không có dòng chữ nào dưới ô SGS affiliate');
    await R.shot(r, ops, 'filled');
    await dlg.getByRole('button', { name: 'Next' }).click();
    const s2 = await visible(dlg.getByLabel(/^Name/));
    R.exp(r, 3, s2, s2 ? 'Chuyển sang bước 2 Invite initial Customer Admin' : 'Không chuyển sang bước 2');
  });

  await R.step(3, ops, async r => {
    const dlg = ops.getByRole('dialog');
    const head = await text(dlg.getByText(/The Customer Admin invites the rest of their team/));
    R.exp(r, 1, head.startsWith(`${D.company} · SGS Taiwan.`), head ? `"${head}"` : 'Không có dòng đầu hộp thoại');
    const note = await text(dlg.getByText(/works once and expires after 7 days/));
    R.exp(r, 2, note === 'The invitation email works once and expires after 7 days. You can resend or revoke it on the account.', note ? `"${note}"` : 'Không có dòng ghi chú lời mời');
    await dlg.getByLabel(/^Name/).fill(D.contact);
    await dlg.getByLabel(/^Email/).fill(D.email);
    await R.shot(r, ops, 'filled');
    invitedAt = Date.now();
    await dlg.getByRole('button', { name: /Create and send invitation/ }).click();
    const closed = await dlg.waitFor({ state: 'hidden', timeout: 15000 }).then(() => true).catch(() => false);
    await settle(ops);
    const err = await visible(ops.getByText(/error|failed|could not|something went wrong/i), 1000);
    R.exp(r, 3, closed && !err, closed ? `Hộp thoại đóng, không có thông báo lỗi; app mở trang chi tiết khách hàng (${new URL(ops.url()).pathname})` : 'Hộp thoại không đóng');
    if (closed) R.note(r, 'Sau khi tạo, app chuyển sang trang chi tiết khách hàng mới (Figma không quy định màn tiếp theo).');
    if (/\/ops\/customers\/[^/]+$/.test(new URL(ops.url()).pathname)) detailHref = new URL(ops.url()).pathname;
  });

  const findCustomer = async () => { await ops.getByRole('searchbox').or(ops.getByPlaceholder(/Search customers/)).first().fill(D.company); await settle(ops, 800); };
  await R.step(4, ops, async r => {
    await ops.getByRole('link', { name: 'Customers' }).first().click(); await settle(ops);
    await findCustomer();
    const row = ops.getByRole('row').filter({ hasText: D.company });
    if (!(await visible(row))) { R.absent(r, 'Không thấy dòng khách hàng trong danh sách'); return; }
    const cells = (await row.first().locator('td').allInnerTexts()).map(x => x.replace(/\s+/g, ' ').trim());
    R.note(r, 'Dòng thực tế: ' + cells.join(' | '));
    R.exp(r, 1, cells[0].includes(D.company) && cells[0].includes(D.companyZh) && cells[1] === 'SGS Taiwan', `Customer "${cells[0]}", SGS affiliate "${cells[1]}"`);
    R.exp(r, 2, cells[2] === '1' && cells[3] === '0' && cells[4] === '0', `Users ${cells[2]}, Scopes ${cells[3]}, Workspaces ${cells[4]}`);
    R.exp(r, 3, /Customer Admin invited/.test(cells[5]), `Status "${cells[5]}"`);
    detailHref ??= await ops.locator('a[href*="/ops/customers/"]').filter({ hasText: D.company }).first().getAttribute('href');
  });

  await R.step(5, ops, async r => {
    if (!detailHref) { R.absent(r, 'Không mở được chi tiết khách hàng'); return; }
    await ops.goto(BASE + detailHref); await settle(ops);
    await ops.getByRole('tab', { name: /^Users/ }).click(); await settle(ops, 400);
    const row = ops.getByRole('row').filter({ hasText: D.email });
    const t = await text(row);
    R.exp(r, 1, /張雅婷/.test(t) && /Customer Admin/.test(t) && /Invited/.test(t), t ? `"${t}"` : 'Không có dòng người được mời');
    R.exp(r, 2, /Resend invitation/.test(t) && /Revoke/.test(t), /Resend invitation/.test(t) ? 'Có Resend invitation và Revoke' : 'Không có Resend invitation / Revoke');
    await R.shot(r, ops, 'users');
    await ops.getByRole('tab', { name: /^NirmatAI/ }).click(); await settle(ops, 400);
    const nl = await visible(ops.getByText(/Not linked to NirmatAI yet/));
    R.exp(r, 3, nl, nl ? 'Tab NirmatAI: Not linked to NirmatAI yet' : 'Không thấy "Not linked to NirmatAI yet"');
  });

  const inbox = await L.newPage(browser);
  await R.step(6, inbox, async r => {
    mail = await L.waitMail(D.email, { re: /invited/i, since: invitedAt });
    if (!mail) { R.absent(r, `Không có email nào gửi tới ${D.email}`); return; }
    const count = (await L.mails(D.email)).length;
    R.exp(r, 1, count === 1, `${count} email mời`);
    const h = mail.html;
    const logo = /<img/i.test(h), card = /style=|<table/i.test(h);
    R.exp(r, 2, logo && card, `${logo ? 'Có' : 'Không có'} logo SGS; ${card ? 'có' : 'không có'} khung/định dạng — email là văn bản thô (chỉ có chữ "Digital Trust Platform" in đậm)`);
    const h1 = (h.match(/<h1>(.*?)<\/h1>/) || [])[1] || '';
    R.exp(r, 3, h1 === 'You’re invited to the Digital Trust Platform', `Tiêu đề "${h1}"; Subject "${mail.subject}"`);
    const sentence = `Lin Mei invited you to join ${D.company} as a Customer Admin.`;
    R.exp(r, 4, h.includes(sentence), h.includes(sentence) ? `"${sentence}"` : 'Không có câu mời đúng');
    const a = (h.match(/<a [^>]*>Activate your account<\/a>/) || [''])[0];
    const isButton = /style=[^>]*background/i.test(a);
    R.exp(r, 5, !!a && isButton, a ? (isButton ? 'Nút Activate your account' : '"Activate your account" là link chữ thường (gạch chân, màu xanh), không phải nút cam') : 'Không có link Activate your account');
    const exp = (h.match(/This link works once and expires on ([^.]+)\. If it has expired, ask ([^ ]+ [^ ]+) to send a new invitation\./) || []);
    const want = new Date(invitedAt + 7 * 864e5).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
    R.exp(r, 6, exp[1] === want && exp[2] === 'Lin Mei', exp[0] ? `"${exp[0]}" (mong đợi ngày ${want})` : 'Không có dòng hạn dùng');
    const zh = /您受邀加入 Digital Trust Platform/.test(h) && /邀請您以 Customer Admin 身分加入/.test(h);
    R.exp(r, 7, zh, zh ? 'Có tiêu đề và đoạn mời tiếng Trung phồn thể' : 'Thiếu phần tiếng Trung');
    if (zh && !isButton) R.note(r, 'Đoạn tiếng Trung ghi "請點選上方按鈕" (bấm nút phía trên) nhưng email không có nút.');
    const foot = /SGS Taiwan · You received this email because an administrator invited you\./.test(h);
    R.exp(r, 8, foot, foot ? 'Có chân email SGS Taiwan · You received this email…' : 'Không có chân email');
    await inbox.setViewportSize({ width: 900, height: 620 });
    await inbox.goto(L.MAILPIT + '/view/' + mail.id + '.html'); await settle(inbox);
  });

  await R.step(7, null, async r => {
    const link = mail && mail.links.find(u => /activate/i.test(u));
    if (!link) { R.absent(r, 'Không có link kích hoạt (phụ thuộc bước 6)'); return; }
    portal = await L.newPage(browser);
    await portal.goto(L.localLink(link), { timeout: 60000 });
    await visible(portal.getByText(/You were invited as/), 10000);
    const body = await text(portal.locator('body'));
    const emailVal = await portal.getByLabel(/^Email/).inputValue().catch(() => '');
    const ok1 = body.includes(D.company) && /Customer Portal/.test(body) && /Customer Admin/.test(body) && emailVal === D.email;
    R.exp(r, 1, ok1, `Tổ chức ${body.includes(D.company) ? '✓' : '✗'}, Customer Portal ${/Customer Portal/.test(body) ? '✓' : '✗'}, Customer Admin ${/Customer Admin/.test(body) ? '✓' : '✗'}, email "${emailVal}"`);
    await R.shot(r, portal, 'activate');
    const name = portal.getByLabel(/^Full name/); if (!(await name.inputValue())) await name.fill(D.contact);
    await portal.getByLabel(/^Create password/).fill('Hsinchu#2026Secure');
    await portal.getByLabel(/^Confirm password/).fill('Hsinchu#2026Secure');
    await portal.getByRole('checkbox').first().check();
    await portal.getByRole('button', { name: /Activate account/ }).click(); await settle(portal, 1500);
    const ready = await visible(portal.getByText('Your account is ready'), 10000);
    R.exp(r, 2, ready, ready ? 'Màn "Your account is ready"' : 'Không thấy màn "Your account is ready"');
    if (ready) { await portal.getByRole('button', { name: /Continue to the portal/ }).or(portal.getByRole('link', { name: /Continue to the portal/ })).first().click(); await settle(portal, 1500); }
    if (/login/.test(portal.url())) {
      await portal.getByLabel(/^Email/).fill(D.email);
      await portal.getByLabel(/^Password/).fill(L.DEV_PASSWORD);
      await portal.getByRole('button', { name: 'Sign in' }).click(); await settle(portal, 2000);
      R.note(r, 'Môi trường local: đăng nhập dev dùng mật khẩu chung; mật khẩu đặt khi kích hoạt chỉ dùng với Microsoft Entra thật.');
    }
    const inPortal = !/login|activate/.test(portal.url());
    R.exp(r, 3, inPortal, inPortal ? `Vào Customer Portal (${new URL(portal.url()).pathname})` : 'Không đăng nhập được');
  });

  await R.step(8, portal, async r => {
    if (!portal || /login|activate/.test(portal.url())) { R.absent(r, 'Chưa đăng nhập được (phụ thuộc bước 7)'); return; }
    await portal.goto(BASE + '/home'); await settle(portal);
    const users = await visible(portal.getByRole('link', { name: 'Users' })), roles = await visible(portal.getByRole('link', { name: /Roles & permissions/ }), 1500);
    R.exp(r, 3, users && roles, `Menu: Users ${users ? 'có' : 'không có'}, Roles & permissions ${roles ? 'có' : 'không có'}`);
    if (!(await visible(portal.getByText(/Good (morning|afternoon|evening)/), 3000))) {
      R.absent(r, 'Màn Home chưa build — /home chỉ là trang giữ chỗ (tiêu đề "Home", không có lời chào, khối số liệu)');
      return;
    }
    R.exp(r, 1, true, 'Có lời chào');
    R.exp(r, 2, await visible(portal.getByText(D.company), 2000), 'Dòng phụ tên khách hàng');
  });

  await R.step(9, ops, async r => {
    await ops.goto(BASE + '/ops/customers'); await settle(ops);
    await findCustomer();
    const row = ops.getByRole('row').filter({ hasText: D.company });
    const cells = (await row.first().locator('td').allInnerTexts().catch(() => [])).map(x => x.replace(/\s+/g, ' ').trim());
    R.exp(r, 1, cells[5] === 'Active', cells.length ? `Status "${cells[5]}"` : 'Không thấy dòng khách hàng');
    await R.shot(r, ops, 'list');
    if (!detailHref) return;
    await ops.goto(BASE + detailHref); await settle(ops);
    await ops.getByRole('tab', { name: /^Users/ }).click(); await settle(ops, 400);
    const t = await text(ops.getByRole('row').filter({ hasText: D.email }));
    R.exp(r, 2, /Active/.test(t), `"${t}"`);
    R.exp(r, 3, !/Resend invitation|Revoke/.test(t), /Resend invitation|Revoke/.test(t) ? 'Vẫn còn Resend invitation / Revoke' : 'Không còn Resend invitation, Revoke');
  });

  await R.step(10, ops, async r => {
    await ops.goto(BASE + '/ops/audit-logs'); await settle(ops);
    if (!(await visible(ops.getByRole('row').nth(1), 3000))) { R.absent(r, 'Màn Audit logs chưa build — /ops/audit-logs chỉ là trang giữ chỗ'); return; }
    R.exp(r, 1, await visible(ops.getByText(D.company), 3000), 'Dòng Customer account created');
  });

  await browser.close();
  R.finish();
  await L.closeDb();
})().catch(e => { console.error('FATAL', e); process.exit(1); });
