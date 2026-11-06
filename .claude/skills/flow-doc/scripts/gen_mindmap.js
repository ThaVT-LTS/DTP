// Build the interactive happy-path mind map (HTML) from flow specs: node gen_mindmap.js <config.json>
// config: { out, specDir (relative to the config), title, waves?: [{ title, note, active, flows: [keys], locked: [{ title, result }] }], flows: [{ key, spec, short, shape: { chains: [[0,1,..]], fork?: { step: [[..]] } },
//           planned: { stepIndex: [{ title, who, result, children: [...] }] }, next: [keys], needs: key|null }] }
const fs = require('fs'), path = require('path');
const CFG_PATH = path.resolve(process.argv[2] || path.join(__dirname, 'mindmap.sgs-dtp.json'));
const CFG = JSON.parse(fs.readFileSync(CFG_PATH, 'utf8'));
const DIR = path.dirname(CFG.out), SPEC_DIR = path.resolve(path.dirname(CFG_PATH), CFG.specDir || '.');
const keys = CFG.flows.map(f => f.key), byKey = Object.fromEntries(CFG.flows.map(f => [f.key, f]));
// Flow number: config 'num', else the spec's seq[0] (same number as the Word file), else the position.
const numOf = k => { const F = byKey[k]; if (F.num) return F.num; try { const S = JSON.parse(fs.readFileSync(path.join(SPEC_DIR, F.spec), 'utf8')); if (S.seq) return S.seq[0]; } catch {} return keys.indexOf(k) + 1; };
const label = k => `Flow ${numOf(k)} · ${byKey[k].short}`;

let uid = 0;
const nodes = {};
function add(n) { n.id = 'n' + (++uid); n.children = n.children || []; nodes[n.id] = n; return n; }
function planned(p, flowKey) { const n = add({ kind: 'planned', title: p.title, who: p.who, result: p.result, flow: flowKey }); n.children = (p.children || []).map(c => planned(c, flowKey).id); return n; }
const root = add({ kind: 'root', title: CFG.title || 'Happy path', who: '', result: CFG.rootResult || `${keys.length} flows` });
// Optional waves: root > wave > flow. Inactive waves list their flows as locked boxes (visible, not open yet).
const waveOf = {}, waveNodes = [];
(CFG.waves || []).forEach(Wv => {
  const w = add({ kind: 'wave', title: Wv.title, who: '', result: Wv.result || '', note: Wv.note || '', active: !!Wv.active, blocked: [] });
  root.children.push(w.id); waveNodes.push(w);
  (Wv.flows || []).forEach(k => { waveOf[k] = w; });
  (Wv.locked || []).forEach(l => w.children.push(add({ kind: 'flow', locked: true, title: l.title, result: l.result || '', badge: Wv.badge || '', note: Wv.note || '', wave: Wv.title, intro: [], blocked: [], next: [], needs: '' }).id));
});
CFG.flows.forEach((F, fi) => {
  const S = JSON.parse(fs.readFileSync(path.join(SPEC_DIR, F.spec), 'utf8'));
  const rel = d => path.relative(DIR, d).split(path.sep).join('/');
  const docx = path.basename(S.out);
  const flow = add({ kind: 'flow', flow: F.key, seq: numOf(F.key), total: keys.length, title: label(F.key), who: '', result: F.result || `${S.steps.length} steps`, docx, intro: S.intro || [], blocked: S.blocked || [],
    needs: F.needs ? label(F.needs) : '', next: (F.next || []).map(label) });
  const parent = waveOf[F.key] || root; parent.children.push(flow.id);
  if (waveOf[F.key]) for (const b of S.blocked || []) if (!parent.blocked.some(x => x[0] === b[0])) parent.blocked.push(b);
  const stepNode = {};
  S.steps.forEach((s, i) => {
    stepNode[i] = add({ kind: 'step', fid: flow.id, flow: F.key, seq: numOf(F.key), step: i + 1, title: s.what, who: s.who, where: s.where, result: s.result, body: s.body || [], docx,
      shots: (s.shots || []).map(([f, cap]) => ({ src: rel(path.join(S.imgDir, f)), cap })) });
    ((F.planned || {})[i] || []).forEach(p => stepNode[i].children.push(planned(p, F.key).id));
  });
  const shape = F.shape || { chains: [S.steps.map((_, i) => i)] };
  const link = chain => { chain.forEach((s, j) => { if (j) stepNode[chain[j - 1]].children.unshift(stepNode[s].id); }); return stepNode[chain[0]].id; };
  shape.chains.forEach(c => flow.children.push(link(c)));
  Object.entries(shape.fork || {}).forEach(([at, chains]) => chains.forEach(c => stepNode[at].children.push(link(c))));
  // happy children first, planned after
  Object.values(stepNode).forEach(n => n.children.sort((a, b) => (nodes[a].kind === 'planned') - (nodes[b].kind === 'planned')));
});
const data = { root: root.id, open: [root.id, ...waveNodes.filter(w => w.active).map(w => w.id)], nodes, total: keys.length, generated: new Date().toISOString().slice(0, 10) };
const tpl = fs.readFileSync(path.join(__dirname, 'mindmap.tpl.html'), 'utf8');
// Optional company logo (config.logo, relative to the config), embedded so the HTML stays one file.
const logo = [].concat(CFG.logo || []).length ? `<div class="lts">${[].concat(CFG.logo).map(x => { const f = x.file || x; return `<img alt="${path.basename(f, '.png')}" style="height:${Math.round(30 * (x.scale || 1))}px" src="data:image/png;base64,${fs.readFileSync(path.resolve(path.dirname(CFG_PATH), f)).toString('base64')}">`; }).join('')}</div>` : '';
fs.writeFileSync(CFG.out, tpl.replace('<!--LOGO-->', logo).replace('/*__DATA__*/null', JSON.stringify(data)));
console.log('wrote', CFG.out, Object.keys(nodes).length, 'nodes');
