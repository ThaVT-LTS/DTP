# Render each .docx in a folder to PDF with ONLYOFFICE x2t, then report page count and near-empty pages.
import sys, os, subprocess, pypdf
sys.stdout.reconfigure(encoding='utf-8')
X2T = r'C:\Program Files\ONLYOFFICE\DesktopEditors\converter\x2t.exe'
FD = r'C:\Users\thavt\AppData\Local\ONLYOFFICE\DesktopEditors\data\fonts'
d = os.path.abspath(sys.argv[1]); tmp = os.path.join(d, 'tmp'); os.makedirs(tmp, exist_ok=True)
for f in sorted(x for x in os.listdir(d) if x.endswith('.docx')):
    src = os.path.join(d, f); pdf = src[:-5] + '.pdf'; xml = os.path.join(d, 'p.xml')
    open(xml, 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="utf-8"?><TaskQueueDataConvert><m_sFileFrom>{src}</m_sFileFrom><m_sFileTo>{pdf}</m_sFileTo><m_nFormatTo>513</m_nFormatTo><m_sFontDir>{FD}</m_sFontDir><m_sAllFontsPath>{FD}\\AllFonts.js</m_sAllFontsPath><m_sTempDir>{tmp}</m_sTempDir><m_bIsNoBase64>true</m_bIsNoBase64></TaskQueueDataConvert>')
    rc = subprocess.run([X2T, xml], capture_output=True).returncode
    if not os.path.exists(pdf): print(f, 'render failed rc', rc); continue
    r = pypdf.PdfReader(pdf); blank = []
    for i, pg in enumerate(r.pages, 1):
        txt = (pg.extract_text() or '')
        body = ' '.join(l for l in txt.splitlines() if 'Page' not in l and 'Flow' not in l and '→' not in l).strip()
        imgs = len(pg.images) if hasattr(pg, 'images') else 0
        if len(body) < 40 and imgs == 0 and 'Figure' not in body: blank.append((i, body[:40]))  # x2t images are not seen by pypdf; a Figure caption means the page holds an image
    print(f, 'pages', len(r.pages), 'near-empty', blank)
