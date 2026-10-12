# -*- coding: utf-8 -*-
"""Quét nội dung sheet Assisted workspace theo rule 38 (không thay tc_check). Dùng: python3 quet-noi-dung_Assisted-workspace.py ea_flat.tsv cases_ea.py"""
import csv,re,sys,importlib.util,io,contextlib
rows=list(csv.DictReader(open(sys.argv[1],encoding='utf-8'),delimiter='\t'))
with contextlib.redirect_stdout(io.StringIO()):
    sp=importlib.util.spec_from_file_location('ce',sys.argv[2]); ce=importlib.util.module_from_spec(sp); sp.loader.exec_module(ce)
Q=ce.Q; bad=[]
def n(i): return "%03d"%i
def add(k,i,t=''): bad.append((k,n(i),t))
use={}
for r in rows:
    for c in re.findall(r'Q-EA-(\d+)',r['Wait']): use[int(c)]=use.get(int(c),0)+1
for k,v in Q.items():
    head=v.split('(')[0]
    if (head.count('?')>=2 or ', và ' in head) and use.get(k,0)>=2: bad.append(('Q nhiều vế','Q-EA-%02d'%k,head[:80]))
for i,r in enumerate(rows,1):
    E,P,S,W,U=r['Expected'],r['Pre'],r['Step'],r['Wait'],r['UC']
    if re.search(r'from Medium|from High',E): add('Expected from Medium/High',i)
    if re.search(r'như Customer|đúng định dạng|như bình thường',E): add('Expected mơ hồ',i,E[:50])
    if (re.fullmatch(r'- Hiển thị [^\n]*',E) and '\\n' not in E): add('Expected quá chung',i,E[:50])
    if not E and not W: add('Expected trống không câu hỏi',i)
    if '11 requirement' in P+E and 'Q-EA-45' not in W: add('nhóm 11 req không Q-EA-45',i)
    if re.search(r'Owner',S+r['Name']) and not re.search(r'Q-EA-(33|56)',W): add('Owner không Q-EA-33/56',i)
    if re.search(r'Unlink from',S) and r['I'].startswith('Gỡ') and 'Q-EA-31' not in W and 'thông báo' not in r['Name']: add('gỡ không Q-EA-31',i)
    if re.match(r'Đăng nhập account Customer (User|Viewer)',P) and not re.search(r'\((Wei Chen|Iris Huang)\)',P) and re.match(r'Đăng nhập account Customer (User|Viewer)',P): add('tên tài khoản',i)
    if re.search(r'Upload evidence|Link 1 item|Unlink from',S) and U in ('UC-WSP-02','UC-EVC-01'): add('UC theo thao tác',i,U)
    m=re.search(r'Mở chi tiết \[([^\]]+)\]',S); m2=re.search(r'\[Workspace[^\]]*\]',P)
    if m and m2 and m.group(0)!='Mở chi tiết '+m2.group(0) and m.group(1)!='Workspace' : add('Pre/Step khác workspace',i,m.group(1)+' vs '+m2.group(0))
    if 'R.1.1.4' in P and 'Partial' in P: add('R.1.1.4 Partial tự đặt',i)
for b in bad: print(*b,sep=' | ')
print('TỔNG',len(bad),'phát hiện trên',len(rows),'case')
