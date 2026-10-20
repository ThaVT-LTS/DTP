# Execute Customers test cases (Round 1) on localhost — record one result per case

T = <WORK> — thư mục làm việc của lượt này, vd `projects/<dự-án>/runs/<ngày>-<việc>/` (xem SKILL.md)
PW = <PW> — `.claude/skills/e2e-flow/scripts` (lib.js, rec2.js; chạy `npm install` ở đó một lần)
## Input
`T\run\<GROUP>.json` — your cases: `{ tc (NEW id, use this), old, c1..c4, priority, name, pre, steps, expected, oq, uc }`.
Execute each case exactly as written (steps + every expected line). The test case workbook is NOT touched by you.

## Environment (running — never restart servers, never reset the DB)
Code: CORP-BA-DTP main b5cb690 (19/10/2026). Web http://localhost:3000, Operations Console /ops/login, Customer Portal /login,
Mailpit http://localhost:8025 (all local mail), Postgres localhost:5432 (docker container corp-ba-dtp-postgres-1, user sgs_dtp /
sgs_dtp_local, db sgs_dtp). Every account uses password `password`. "SGS Admin (Minh Nguyen)" in the cases = lin.mei@example.com
(SGS Taiwan). Customer Admin kevin.lin@example.com, Customer User jason.chen@example.com, Customer Viewer peggy.lai@example.com.
Use Playwright through `PW\lib.js` (signInAs, newPage, settle, visible, text, waitMail, mails, db, suffix…); put your scripts in
`T\run\<GROUP>-*.js`, screenshots in `T\run\shots\<tc>.png` (one per case, showing what the expected checks).
Other agents run other groups at the same time: give every name/email you create a unique suffix (e.g. "Riyadh Imports LLC <S>",
"omar.haddad+<S>@riyadh-imports.sa"). Pre-conditions that need data (ABC Trading Co., Ltd. with Customer Admin Linh Tran active,
a revoked invitation, 26+ customers…) — create them through the UI when possible, else insert via DB; reuse your own data across
your cases. NEVER leave a seed account (lin.mei, kevin.lin, jason.chen, peggy.lai, chen.wei) broken: if a case makes a seed email a
member of another customer, delete exactly the invitation + customer_membership rows you created right after the case, and check
the seed account can still sign in where it could before.

## Result per case (Round 1 column "Result")
- `Passed` — every expected line is true.
- `Failed` — the screen/feature exists but at least one expected line is false (wrong/missing text, no error shown, wrong
  behaviour…). Always say which line and what the web did.
- `Blocked` — cannot be executed on this local environment and no local substitute exists (say why and what is needed).
- `Pending` — the UC is not done yet per Plan v3.0 (ACC-07 NirmatAI link = Not started; Certifications tab = CRT, Wave 2), or the
  case only waits on an open question (Cần xác nhận) and the web has no behaviour to compare. Say which.
- `NA` — not applicable (explain).
When the expected says "Chờ BA chốt Q-…" give Failed only if the web is clearly wrong anyway (e.g. no error at all, data corrupted),
else Pending.

## Output — `T\results\<GROUP>.json`
```json
[ { "tc": "TC_033", "result": "Failed", "remark": "Thực tế: … ≠ Mong đợi: … (bước N)", "bug": "<short bug title if Failed, else ''>", "shot": "run/shots/TC_033.png" } ]
```
- One entry for EVERY case of your group, in order. Remark in Vietnamese, ≤ 3 lines, concrete (quote UI texts in English).
- Look at the screenshot before accepting a Failed (make sure it is the app, not your script).
- Validate the JSON parses. Report back ≤ 12 lines: counts per result, every Failed with one line, every Blocked/Pending reason.
