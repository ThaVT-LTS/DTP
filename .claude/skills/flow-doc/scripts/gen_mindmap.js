// Build the interactive happy-path mind map (HTML) from flow specs: node gen_mindmap.js <config.json>
// config: { out, specDir (relative to the config), title, flows: [{ key, spec, short, shape: { chains: [[0,1,..]], fork?: { step: [[..]] } },
//           planned: { stepIndex: [{ title, who, result, children: [...] }] }, next: [keys], needs: key|null }] }
const fs = require('fs'), path = require('path');
const CFG_PATH = path.resolve(process.argv[2] || path.join(__dirname, 'mindmap.sgs-dtp.json'));
const CFG = JSON.parse(fs.readFileSync(CFG_PATH, 'utf8'));
const DIR = path.dirname(CFG.out), SPEC_DIR = path.resolve(path.dirname(CFG_PATH), CFG.specDir || '.');
const keys = CFG.flows.map(f => f.key), byKey = Object.fromEntries(CFG.flows.map(f => [f.key, f]));
const label = k => `Flow ${keys.indexOf(k) + 1} · ${byKey[k].short}`;

let uid = 0;
const nodes = {};
function add(n) { n.id = 'n' + (++uid); n.children = n.children || []; nodes[n.id] = n; return n; }
function planned(p, flowKey) { const n = add({ kind: 'planned', title: p.title, who: p.who, result: p.result, flow: flowKey }); n.children = (p.children || []).map(c => planned(c, flowKey).id); return n; }
const root = add({ kind: 'root', title: CFG.title || 'Happy path', who: '', result: `${keys.length} flows` });
CFG.flows.forEach((F, fi) => {
  const S = JSON.parse(fs.readFileSync(path.join(SPEC_DIR, F.spec), 'utf8'));
  const rel = d => path.relative(DIR, d).split(path.sep).join('/');
  const docx = path.basename(S.out);
  const flow = add({ kind: 'flow', flow: F.key, seq: fi + 1, total: keys.length, title: label(F.key), who: '', result: `${S.steps.length} steps`, docx, intro: S.intro || [], blocked: S.blocked || [],
    needs: F.needs ? label(F.needs) : '', next: (F.next || []).map(label) });
  root.children.push(flow.id);
  const stepNode = {};
  S.steps.forEach((s, i) => {
    stepNode[i] = add({ kind: 'step', flow: F.key, seq: fi + 1, step: i + 1, title: s.what, who: s.who, where: s.where, result: s.result, body: s.body || [], docx,
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
const data = { root: root.id, nodes, total: keys.length, generated: new Date().toISOString().slice(0, 10) };
const tpl = fs.readFileSync(path.join(__dirname, 'mindmap.tpl.html'), 'utf8');
fs.writeFileSync(CFG.out, tpl.replace('/*__DATA__*/null', JSON.stringify(data)));
console.log('wrote', CFG.out, Object.keys(nodes).length, 'nodes');
