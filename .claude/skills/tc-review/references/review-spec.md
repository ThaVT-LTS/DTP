# Rà soát test case Wave 1 — READ ONLY (không sửa file test case, không sửa repo)

R = <WORK> — thư mục làm việc của lượt này, vd `projects/<dự-án>/runs/<ngày>-<việc>/` (xem SKILL.md)
## Input
- `R\in\<Sheet>.json` — every case of the sheet: `{row, tc, c1..c4 (classification), priority, name, pre, steps, expected, openQuestion, uc}`
  (row = Excel row in `SGS-DTP_TestCase_v0.2_Phase1.xlsx`, sheet = same name).
- `R\in\Can_xac_nhan.json` — sheet "Cần xác nhận": `{row, id, sheet, question, basis, tcs, proposal, level, status}`. Review only the items whose `sheet` is one of yours.
- `R\plan-by-uc.txt` — Plan v3.0: `UC | name | PIC | wave | confirmed | start | end | status | note`. Wave 1 = wave 1.

## Sources of truth (in this order)
1. UC v5.4: `C:\Users\thavt\Documents\DTP\dts-agent-workspace\docs\user-stories\uc-list-v5.4.md`, `changes-vs-source-v5.4.md`, `p2-deferred-v5.4.md`
2. US acceptance criteria: `...\docs\user-stories\US-NNN.md`; decisions: `...\knowledge\L1-domain\decision-log.md`
3. Figma P1 mirror: `...\docs\prototypes\figma-p1\*.md` (+ `_index.md`; images in `img\` — Read an image when the text is not enough)
4. Prototype review decisions: `...\docs\user-stories\prototype-review\*.md`, `...\docs\prototypes\self-designed.md`
5. Web as built — latest code `C:\Users\thavt\Documents\DTP\CORP-BA-DTP` (branch main, commit b5cb690, 19/10/2026): UI texts in
   `apps/web/src/messages/en/*.json` (+ zh-TW), screens in `apps/web/src/app` and `apps/web/src/features`, API in
   `packages/api-contracts`, backend `apps/backend/src`. Placeholder pages (only `<PortalPage/>`) = not built. The app also runs at
   http://localhost:3000 (password `password`; SGS Admin lin.mei@example.com /ops/login, Customer Admin kevin.lin@example.com,
   Customer User jason.chen@example.com, Customer Viewer peggy.lai@example.com /login) — you may look at it with Playwright
   (`<PW>/lib.js` has signInAs/newPage),
   but do NOT create lots of data and never reset the DB. Reading the code is usually enough.
Never edit any repo or the test case workbook.

## For EVERY case decide one verdict
- `Xoá` — must be removed: marked [OUT]; feature not in UC v5.4 / Figma P1 (e.g. Country, Internal note, old web-demo-only things);
  Phase 2 per p2-deferred; exact duplicate of another case (name the other TC).
- `Sửa` — case is in scope but wrong vs Figma / UC / US: wrong labels, button names, messages, steps, roles, pre-condition, expected,
  wrong UC code, wrong "[Phase 2]" tag on a P1 UC, unanswered "Chưa viết Expected", vague expected. Give the exact correction.
- `Lệch web` — case is correct per Figma/UC but the web (main b5cb690) differs (different text/behaviour, or screen/feature not built).
  This is a bug/report for dev, not a test case fix. Say what the web does, with file path.
- `Wave sau` — the case's UC is Wave 2/3 in Plan v3.0 (keep, just mark; no deep review).
- `OK` — correct and matches the web.
A case can need both a fix and a web note: use `Sửa` and also fill `web`.

## Output — write `R\out\<Sheet>.json` (one per sheet you own)
```json
{ "sheet": "Customers", "cases": [
  { "row": 29, "tc": "TC_017", "verdict": "Xoá", "issue": "<ngắn gọn, tiếng Việt: sai gì>",
    "fix": "<nội dung sửa cụ thể: tên/bước/expected mới; hoặc 'Xoá case'>",
    "web": "<hành vi web thực tế nếu khác, kèm file; '' nếu không>", "source": "<Figma file:dòng / uc-list:dòng / US-0xx ACn / Dxx / file web>" } ],
  "questions": [ { "row": 7, "id": "Q-U-04", "decision": "Đóng" | "Giữ" | "Bỏ", "answer": "<câu trả lời + nguồn, hoặc vì sao vẫn cần hỏi>" } ] }
```
- Include EVERY case of the sheet (also `OK` ones; for OK leave issue/fix ''). Vietnamese prose; UI texts in English exactly.
- `questions`: for each "Cần xác nhận" item of your sheets: `Đóng` = already answered by UC/US/Figma/decision/web (give the answer),
  `Bỏ` = only concerns cases that are Xoá / out of Wave 1, `Giữ` = still needs BA/SGS (say why).
- Validate the JSON parses. Be concrete; no invented UI text — if a text is not in any source, say so.

## Report back (≤ 12 lines per sheet)
Counts per verdict; the 5 most serious problems; questions Đóng/Giữ/Bỏ counts.
