// Preview the Figma annotations of a v2 flow: node preview2.js flows2/<ID>.json [step]
// → preview2/<ID>-s<N>-act.png (red ①②) and preview2/<ID>-s<N>-exp.png (green A B). Look at every file.
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');
const IMG = 'C:/Users/thavt/Documents/DTP/dts-agent-workspace/docs/prototypes/figma-p1/img/';
const flow = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const only = process.argv[3] ? Number(process.argv[3]) : null;
const OUT = path.join(__dirname, 'preview2'); fs.mkdirSync(OUT, { recursive: true });
async function draw(spec, file, colour) {
  const meta = await sharp(IMG + spec.img).metadata();
  const svg = [`<svg width="${meta.width}" height="${meta.height}" xmlns="http://www.w3.org/2000/svg">`];
  for (const { n, b: [x1, y1, x2, y2] } of spec.marks || []) {
    svg.push(`<rect x="${x1}" y="${y1}" width="${x2 - x1}" height="${y2 - y1}" rx="4" fill="none" stroke="${colour}" stroke-width="3"/>`);
    const cx = Math.max(13, x1 - 2), cy = Math.max(13, y1 - 2);
    svg.push(`<circle cx="${cx}" cy="${cy}" r="12" fill="${colour}"/><text x="${cx}" y="${cy + 5}" font-family="Arial" font-weight="bold" font-size="15" fill="#fff" text-anchor="middle">${n}</text>`);
  }
  svg.push('</svg>');
  await sharp(IMG + spec.img).composite([{ input: Buffer.from(svg.join('')) }]).png().toFile(file);
  console.log(file);
}
(async () => {
  for (let k = 0; k < flow.steps.length; k++) {
    if (only && only !== k + 1) continue;
    const s = flow.steps[k];
    for (const [key, colour] of [['act', '#E00000'], ['expImg', '#2E7D32']]) {
      if (!s[key]) continue;
      if (!fs.existsSync(IMG + s[key].img)) { console.log(`MISSING image step ${k + 1} ${key}: ${s[key].img}`); continue; }
      await draw(s[key], path.join(OUT, `${flow.id}-s${k + 1}-${key === 'act' ? 'act' : 'exp'}.png`), colour);
    }
  }
})();
