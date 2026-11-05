// Build a flow document (.docx) from a JSON spec: node buildflow.js spec.json
// spec: { title, out, imgDir, env, intro: [], steps: [{ who, where, what, result, body: [], shots: [[file, caption]] }],
//         tables?: [{ heading, cols: [], widths: [], rows: [[]] }], blocked?: [[area, what, why, check]], limitations?: [] }
const fs = require('fs'), path = require('path');
const { Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType, HeadingLevel,
  AlignmentType, BorderStyle, InternalHyperlink, Bookmark, LevelFormat, Footer, Header, PageNumber, VerticalAlign, TableLayoutType } = require('docx');
const S = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const FONT = 'Calibri', HFONT = 'Calibri Light';
const C = { orange: 'D2551E', dark: '263746', slate: '3E5566', soft: 'FCEBE1', zebra: 'F5F7F9', line: 'D5DCE2', grey: '6B7680', red: 'B4232A', redSoft: 'FCE8E8', blue: '1F5FA8', green: '2E7D4F', greenSoft: 'E6F3EC' };
const TW = 9360;
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: none, bottom: none, left: none, right: none };
const thin = c => ({ style: BorderStyle.SINGLE, size: 4, color: c });
const lineBorders = { top: thin(C.line), bottom: thin(C.line), left: thin(C.line), right: thin(C.line) };
const t = (text, o = {}) => new TextRun({ text, font: FONT, size: 21, color: '262626', ...o });
const p = (runs, o = {}) => new Paragraph({ children: Array.isArray(runs) ? runs : [t(runs)], spacing: { after: 100, line: 276 }, ...o });
const cell = (children, w, o = {}) => new TableCell({ borders: lineBorders, width: { size: w, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, verticalAlign: VerticalAlign.CENTER, children, ...o });
const fill = c => ({ fill: c, type: ShadingType.CLEAR, color: 'auto' });
const hcell = (h, w, bg = C.dark) => cell([p([t(h, { bold: true, color: 'FFFFFF', size: 20 })], { spacing: { after: 0 } })], w, { shading: fill(bg) });
const section = (text, o = {}) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text, font: HFONT })], ...o });
const tbl = (widths, rows) => new Table({ width: { size: TW, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows });

// Cover band + meta card
const band = tbl([TW], [new TableRow({ children: [new TableCell({ borders: noBorders, width: { size: TW, type: WidthType.DXA }, shading: fill(C.dark), margins: { top: 360, bottom: 360, left: 360, right: 360 }, children: [
  new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: 'SGS DIGITAL TRUST PLATFORM  ·  ' + (S.seq ? `FLOW ${S.seq[0]} OF ${S.seq[1]}` : 'FLOW REVIEW'), font: FONT, size: 18, bold: true, color: 'F4A57A', characterSpacing: 40 })] }),
  new Paragraph({ spacing: { after: 120 }, children: [new Bookmark({ id: 'top', children: [new TextRun({ text: S.title, font: HFONT, size: 48, color: 'FFFFFF' })] })] }),
  new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: 'Happy path · English · screenshots with page URL', font: FONT, size: 20, color: 'C9D3DB' })] }),
] })] })]);
const envParts = S.env.replace(/^Environment:\s*/, '').split('·').map(x => x.trim()).filter(Boolean);
const metaRows = [['Environment', envParts[0] || ''], ['Captured', (envParts.find(x => /Screenshots/.test(x)) || '').replace(/^Screenshots taken\s*/, '')], ['Steps', `${S.steps.length} steps · ${S.steps.reduce((a, s) => a + (s.shots || []).length, 0)} screenshots`], ['Prepared by', 'QA team']];
const meta = tbl([2200, TW - 2200], metaRows.map(([k, v]) => new TableRow({ children: [
  cell([p([t(k, { bold: true, color: C.orange, size: 20 })], { spacing: { after: 0 } })], 2200, { shading: fill(C.soft) }),
  cell([p([t(v, { size: 20 })], { spacing: { after: 0 } })], TW - 2200)] })));
const callout = (runs, bar = C.orange, bg = C.zebra) => tbl([TW], [new TableRow({ children: [new TableCell({ width: { size: TW, type: WidthType.DXA }, shading: fill(bg), margins: { top: 100, bottom: 100, left: 200, right: 160 },
  borders: { top: none, bottom: none, right: none, left: { style: BorderStyle.SINGLE, size: 24, color: bar } }, children: runs.map(r => p(Array.isArray(r) ? r : [t(r)], { spacing: { after: 40, line: 276 } })) })] })]);

const W = [800, 1500, 2300, 2600, 2160];
const overview = tbl(W, [new TableRow({ tableHeader: true, children: ['Step', 'Who', 'Where', 'What', 'Result'].map((h, i) => hcell(h, W[i])) }),
  ...S.steps.map((s, n) => { const bg = n % 2 ? fill(C.zebra) : undefined; return new TableRow({ cantSplit: true, children: [
    cell([p([t(String(n + 1), { bold: true, color: 'FFFFFF', size: 20 })], { spacing: { after: 0 }, alignment: AlignmentType.CENTER })], W[0], { shading: fill(C.orange) }),
    cell([p([t(s.who, { bold: true, color: C.slate, size: 20 })], { spacing: { after: 0 } })], W[1], { shading: bg }),
    cell([new Paragraph({ spacing: { after: 0 }, children: [new InternalHyperlink({ anchor: 's' + (n + 1), children: [t(s.where, { color: C.blue, underline: {}, size: 20 })] })] })], W[2], { shading: bg }),
    cell([p([t(s.what, { size: 20 })], { spacing: { after: 0 } })], W[3], { shading: bg }),
    cell([p([t(s.result, { size: 20, color: C.green })], { spacing: { after: 0 } })], W[4], { shading: bg }),
  ] }); })]);

const children = [band, new Paragraph({ spacing: { after: 160 } }), meta, new Paragraph({ spacing: { after: 160 } })];
if ((S.intro || []).length) children.push(callout(S.intro));
if (S.related) children.push(new Paragraph({ spacing: { before: 120, after: 60 }, children: [t(S.related, { color: C.slate, size: 19, bold: true })] }));
children.push(section('Flow overview'), p([t('Click a cell in the Where column to jump to the screenshots of that step.', { color: C.grey, italics: true, size: 19 })]), overview);
for (const tb of S.tables || []) {
  children.push(section(tb.heading));
  children.push(tbl(tb.widths, [new TableRow({ tableHeader: true, children: tb.cols.map((h, i) => hcell(h, tb.widths[i])) }),
    ...tb.rows.map((r, n) => new TableRow({ cantSplit: true, children: r.map((v, i) => cell([p([t(String(v), { size: 20, bold: i === 0 })], { spacing: { after: 0 } })], tb.widths[i], { shading: n % 2 ? fill(C.zebra) : undefined })) }))]));
}
if ((S.blocked || []).length) {
  const BW = [1900, 2300, 2760, 2400];
  children.push(section('Not tested yet (blocked)'));
  children.push(p([t('These parts of the flow could not be tested on the LTS test environment. Check them on the SGS environment once the blocker is cleared.', { color: C.grey, size: 19, italics: true })]));
  children.push(tbl(BW, [new TableRow({ tableHeader: true, children: ['Area', 'Not tested', 'Why it is blocked', 'Check on the SGS environment'].map((h, i) => hcell(h, BW[i], C.red)) }),
    ...S.blocked.map(r => new TableRow({ cantSplit: true, children: r.map((v, i) => cell([p([t(v, { size: 20, bold: i === 0, color: i === 0 ? C.red : '262626' })], { spacing: { after: 0 } })], BW[i], { shading: fill(i === 0 ? C.redSoft : 'FFFFFF') })) }))]));
}
if ((S.limitations || []).length) {
  children.push(section('Notes on the test environment'));
  S.limitations.forEach(x => children.push(new Paragraph({ numbering: { reference: 'b', level: 0 }, children: [t(x, { size: 20 })], spacing: { after: 60 } })));
}
const kvRow = (k, v, color) => new TableRow({ children: [
  cell([p([t(k, { bold: true, color: C.orange, size: 20 })], { spacing: { after: 0 } })], 1500, { shading: fill(C.soft) }),
  cell([p([t(v, { size: 20, color: color || '262626', bold: !!color })], { spacing: { after: 0 } })], TW - 1500)] });
S.steps.forEach((s, n) => {
  // pageBreakBefore on the heading (not a separate PageBreak paragraph) avoids blank pages after a full page.
  children.push(new Paragraph({ pageBreakBefore: true, spacing: { after: 0 }, children: [new TextRun({ text: `STEP ${n + 1} OF ${S.steps.length}`, font: FONT, size: 18, bold: true, color: C.orange, characterSpacing: 30 })] }));
  children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 40, after: 140 }, children: [new Bookmark({ id: 's' + (n + 1), children: [new TextRun({ text: s.what, font: HFONT })] })] }));
  children.push(new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 60 }, children: [new InternalHyperlink({ anchor: 'top', children: [t('↑ Back to the flow overview', { color: C.blue, underline: {}, size: 18 })] })] }));
  children.push(tbl([1500, TW - 1500], [kvRow('Who', s.who), kvRow('Where', s.where), kvRow('Result', s.result, C.green)]));
  if ((s.body || []).length) { children.push(new Paragraph({ spacing: { after: 100 } }), callout(s.body, C.slate)); }
  (s.shots || []).forEach(([f, cap], i) => {
    const data = fs.readFileSync(path.join(S.imgDir, f));
    const w = data.readUInt32BE(16), h = data.readUInt32BE(20);
    // Keep heading + card + image + caption on one page: cap the height.
    let dw = 620, dh = Math.round(h * dw / w); const max = i === 0 ? ((s.body || []).length ? 450 : 500) : 630; if (dh > max) { dh = max; dw = Math.round(w * dh / h); }
    children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 60 }, keepNext: true, children: [new ImageRun({ type: 'png', data, transformation: { width: dw, height: dh }, altText: { title: cap, description: cap, name: f } })] }));
    children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [t(`Figure ${n + 1}.${i + 1}  `, { bold: true, color: C.orange, size: 18 }), t(cap, { color: C.grey, size: 18, italics: true })] }));
  });
});
const doc = new Document({
  creator: 'QA', title: S.title,
  numbering: { config: [{ reference: 'b', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } }, run: { color: C.orange } } }] }] },
  styles: { default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [{ id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HFONT, size: 32, color: C.dark },
      paragraph: { spacing: { before: 320, after: 140 }, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.orange, space: 4 } } } }] },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1440, right: 1440 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [t((S.seq ? `Flow ${S.seq[0]} · ` : '') + S.title, { size: 16, color: C.grey })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, border: { top: { style: BorderStyle.SINGLE, size: 4, color: C.line, space: 4 } }, children: [t('SGS DTP · QA  ·  Page ', { size: 16, color: C.grey }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: C.grey })] })] }) },
    children }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(S.out, b); console.log('wrote', S.out, b.length); });
