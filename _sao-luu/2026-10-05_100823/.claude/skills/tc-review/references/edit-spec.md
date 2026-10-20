# Pass 2 — write the exact new cell contents (still do NOT touch the workbook; the main session applies them)

R = <WORK> — thư mục làm việc của lượt này, vd `projects/<dự-án>/runs/<ngày>-<việc>/` (xem SKILL.md)
The user approved applying your review to the test case workbook. For each sheet you reviewed, write
`R\edits\<Sheet>.json` (same file-name style as out/, e.g. `Workspace_detail.json`):
```json
{ "sheet": "Customers", "edits": [
  { "row": 27, "tc": "TC_015", "name": "<new value or omit>", "pre": "...", "steps": "...", "expected": "...", "uc": "...", "openQuestion": "" } ] }
```
Rules
- One entry for EVERY case whose verdict is `Sửa` (and for any other case whose text must change because of a closed question
  or the decision below). Give ONLY the fields that change, each as the FULL new cell text (not a diff, not a description).
- Keep the file's style exactly (look at the existing cells in `R\in\<Sheet>.json`): Vietnamese prose; steps as
  "1. Bấm …\n2. …"; expected as "- …" lines; pre-condition like "Login acc SGS Admin (…)"; UI texts in English exactly as the
  source of truth says. Remove "[Phase 2]" tags that were wrong, remove "Chưa viết Expected" by writing the expected.
- `openQuestion`: if the case's question was closed (decision `Đóng`), put the answer into steps/expected and set
  `"openQuestion": ""`. If it is still `Giữ`, leave it.
- Xoá / Lệch web / Wave sau / OK cases: no entry (Xoá rows are deleted by the main session; Lệch web stays as written — it is correct).
- DECISION (dev, 19/10/2026): the helper line "Your affiliate. New customers always belong to it." under SGS affiliate was removed
  on purpose (main commit 48e50cb). Test cases must follow the web here: remove that line from every expected result and add
  nothing in its place. (Only the Customers sheet should be affected; check Users too.)
- Validate the JSON parses. Report back: number of edits per sheet and anything you could not express as a cell value.
