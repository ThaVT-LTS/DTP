# -*- coding: utf-8 -*-
import re, unicodedata, sys
from fwk_tree import P
from fwk_cases import C
N=lambda s: unicodedata.normalize("NFC", s)
rows=[]; k=0
for p in P:
    if p["st"]=="C": continue
    for it in p["items"]:
        pri,name,step,exp,wait,uc,pre=C[k]; k+=1
        if uc is None:
            m=re.search(r"FWK-\d\d",p["uc"]); uc=m.group(0) if m else p["uc"]
        login="Đăng nhập account SGS Admin"; extra=[]
        for ln in pre.split("\n"):
            if ln.startswith("Đăng nhập account"): login=re.sub(r" \(thay cho SGS Admin\)","",ln)
            elif ln: extra.append(ln)
        rows.append(dict(I=p["I"],II=p["II"],III=p["III"],IV=it,Pri=pri,Name=name,Pre="\n".join([login]+extra),Step=step,Expected=exp,UC=uc,Wait=wait))
assert k==len(C), (k,len(C))
print("rows",len(rows),file=sys.stderr)
cols=["I","II","III","IV","Pri","Name","Pre","Step","Expected","UC","Wait"]
with open("frameworks.tsv","w",encoding="utf-8",newline="") as f:
    f.write("\t".join(cols)+"\n")
    for r in rows:
        f.write("\t".join(N(r[c]).replace("\t"," ").replace("\n","\\n") for c in cols)+"\n")
blank=sum(1 for r in rows if not r["Expected"]); print("blank expected",blank,"with Q",sum(1 for r in rows if r["Wait"]),file=sys.stderr)
