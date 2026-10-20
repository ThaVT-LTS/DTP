# Wave 1 E2E — format v2: write the flow, run it, record one result per expected bullet

SP = <WORK> — thư mục làm việc của lượt này, vd `projects/<dự-án>/runs/<ngày>-<việc>/` (xem SKILL.md)
## The finished example — read these three files first and copy their style exactly
- `SP\xl\flows2\E2E1_001.json` — flow definition v2
- `SP\pw\run2-E2E1_001.js` — run script v2 (uses `SP\pw\lib.js` + `SP\pw\rec2.js`)
- `SP\xl\runs2\E2E1_001.json` — what a run produces

## Environment (already running — never start/stop servers, never reset the DB)
Web http://localhost:3000 · backend :3001 (+ worker) · Mailpit http://localhost:8025 · Postgres localhost:5432
(superuser sgs_dtp / sgs_dtp_local, db sgs_dtp) · Azurite :10000. Dev sign-in password for every account: `password`.
Seed accounts: SGS Admin lin.mei@example.com (/ops/login, affiliate SGS Taiwan), Customer Admin kevin.lin@example.com,
Customer User jason.chen@example.com, Customer Viewer peggy.lai@example.com (/login), Consultant chen.wei@example.com.
Source (READ ONLY): C:\Users\thavt\Documents\DTP\CORP-BA-DTP. Placeholder pages (page.tsx renders only `<PortalPage/>`):
customer /home /admin/users /admin/roles /workspaces(list) /activity-log /service-requests /marketplace; ops /ops/home
/ops/admin/users /ops/admin/roles /ops/audit-logs /ops/requests /ops/bulk-workspaces. Customer /workspaces/[id] runs on
fake in-browser data (apps/web/src/features/workspaces/shared/fake-data.ts, one workspace `csma-card-data`, dev tenant only).
Other agents run other flows at the same time on the same app — use `L.suffix()` in every name/email you create.

## 1 · Flow definition `SP\xl\flows2\<ID>.json`
Start from the old definition `SP\xl\flows\<ID>.json` (keep id, name, goal, roles, pre, data, step titles/roles/order,
act texts, inputs, notes, rel) and convert each step to v2:
- `act`: the Figma screen where the tester ACTS, with RED numbered marks ①②… `{img, frame, marks:[{n:1,b:[x1,y1,x2,y2]}]}`
  (pixels of the original image). `null` when the step only looks at a screen (observation step).
- `expImg`: the Figma screen of the EXPECTED RESULT after the action, with GREEN lettered marks A, B, C…
  `{img, frame, portrait?, marks:[{n:"A",b:[…]}]}`. Pick the frame that shows the result (e.g. the dialog that opens,
  the next wizard step, the list with the new row, the status after the change). If Figma has no such screen →
  `expImg: null` + `expNote: "Figma chưa có màn … (<UC> · …)"`. Never pretend.
- `do`: action lines (use ①② for marks on `act`). `input`: data lines.
- `exp`: array of `{ "t": "<one checkable expectation>", "uc": "<ONE UC id it belongs to>" }`. Prefix with `Ⓐ Ⓑ …`
  when it points at a green mark, `①②` when it points at a red mark on `act`. Split compound bullets so each is one
  check. Include visible design facts that matter (button vs link, missing block, wording), not pixel details.
- `uc` per step = the UCs of its bullets.
Figma mirror: `C:\Users\thavt\Documents\DTP\dts-agent-workspace\docs\prototypes\figma-p1\*.md` (one `## <frame>` + image
per frame, `_index.md` lists UC → frame and "no screen"), images in `...\figma-p1\img\`. Look at the image (Read) to place
boxes; then run `cd SP/xl && node preview2.js flows2/<ID>.json` and LOOK at every `preview2/<ID>-s*-*.png` until every box
sits on the thing it names. Expectations must come from Figma, UC v5.4 (`dts-agent-workspace/docs/user-stories/uc-list-v5.4.md`),
US acceptance criteria (`docs/user-stories/US-NNN.md`) or the decision log — never invent UI text; if unsure, write the
behaviour and add a step `note`.

## 2 · Run script `SP\pw\run2-<ID>.js`
Port the old script `SP\pw\run-<ID>.js` (it already knows the DOM, data seeding and helpers `h-*.js` — reuse them) to the
v2 recorder: `const R = run2('<ID>')`, `await R.step(n, page, async r => { … })`, and for every bullet i of that step
`R.exp(r, i, ok, actual)`:
- `ok === true`  → matches the expectation.
- `ok === false` → the screen/feature EXISTS but differs from the expectation or the Figma expected image
  (wrong text, link instead of button, missing element on an existing screen, wrong number, wrong status…).
- `ok = 'absent'` (or `R.absent(r, reason)` for all remaining bullets) → the screen/feature is NOT BUILT / not reachable,
  so it cannot be checked (placeholder page, no button, no API, fake data that never reaches the backend…). Say what is
  missing and the evidence (route, file) in `actual`.
- `actual` = what you really saw, short and concrete (quote texts, give values). Vietnamese prose, UI texts in English.
Do NOT decide Passed/Failed/Pending yourself — the builder does that from `ok` + the Plan status of the bullet's UC.
Screenshots: the step screenshot (`R.shot(r, page, 'name')`) must show the state the bullets check. For emails, screenshot
`L.MAILPIT + '/view/' + mail.id + '.html'` (body only) at viewport 900×620.
Preconditions from earlier flows: create them inside your script (UI when possible, else `L.db()` inserts following the
Drizzle schema — never alter schema, never delete rows you didn't create) and say so with `R.note(r, …)` once.
Before accepting `false`, look at the screenshot (Read the png) to be sure it is the app, not your locator.
Iterate until the run has no "Lỗi khi chạy" notes caused by your script. Final: one clean full run per flow.

## 3 · Report (≤ 12 lines per flow)
Per flow: steps · bullets total · ok true / false / absent; every `false` bullet as "thực tế ≠ mong đợi" one line; steps
with `expImg: null`; data seeded via DB.
