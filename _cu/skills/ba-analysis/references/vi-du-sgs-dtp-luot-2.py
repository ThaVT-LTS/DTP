"""
VÍ DỤ THAM KHẢO — không chạy nguyên xi được cho dự án khác.

Đây là Lượt 2 (đối soát + nhóm phạm vi + tìm lỗi dữ liệu/phụ thuộc) đã chạy thật cho
SGS DTP MVP UC List v2.1: sinh dữ liệu cho analysis.md và annotations cho uc-inventory.md.

Giữ lại làm ví dụ về CẤU TRÚC của Lượt 2, không phải công cụ dùng chung:
- Tên cột ("LTS suggestion", "SGS Comments", "ESt (Hour)"), tên sheet, và tiền tố UC
  (UC-AUTH, UC-EVD, UC-REV...) là đặc thù của dự án này.
- Logic nhóm phạm vi (A/F/C/D/B1/B2/B3/E) phản ánh đúng quy ước phase của dự án này
  (LTS suggestion vs SGS Comments) — dự án khác cần định nghĩa lại nhóm phù hợp.
- Bảng phát hiện (F-01 .. F-40) là kết quả đọc thật bộ UC này, không tái dùng được.

Khi áp dụng cho dự án khác: giữ nguyên bộ khung (group() phân loại theo cột đặc thù,
roles() chuẩn hoá actor, F[] liệt kê phát hiện có ID + vị trí + câu hỏi, phần cuối sinh
snippets.json để lắp vào analysis.md) và viết lại phần nội dung theo tài liệu thật.
"""
import importlib.util, json, re, collections

spec = importlib.util.spec_from_file_location(
    "ex", "/home/claude/ai-ecosystem/skills/ba-analysis/scripts/extract_uc_list.py")
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)

SRC = "/mnt/user-data/uploads/SGS_DTP_MVP_Use_Case_List_v2_1_final_confirmation.xlsx"
wb, sheets = ex.extract(SRC)

def recs(title):
    sh = next(s for s in sheets if s["title"] == title)
    out = []
    for u in sh["ucs"]:
        d = dict(u["fields"]); d["_id"] = u["id"]; d["_row"] = u["row"]; d["_sec"] = u["section"]
        d["_sheet"] = title
        out.append(d)
    return out

MVP, FUT, OOS = recs("UC List"), recs("Future Release"), recs("OOS - Not MVP")
ALL = MVP + FUT + OOS

# ---------- Nhóm phạm vi ----------
GROUP_TXT = {
    "A": "A — có giờ, LTS không đề xuất lùi",
    "F": "F — có giờ, SGS gợi ý có thể lùi P2",
    "C": "C — LTS đề xuất P2, SGS muốn giữ P1, đã có giờ",
    "D": "D — LTS ghi 'move back to P1', chưa có giờ",
    "B2": "B2 — LTS đề xuất P2, SGS muốn giữ P1, chưa có giờ",
    "B1": "B1 — LTS đề xuất P2, SGS đồng ý",
    "B3": "B3 — LTS đề xuất P2, SGS chưa phản hồi",
    "E": "E — không có đề xuất, không có giờ",
    "FUT": "Future Release (theo sheet)",
    "OOS": "OOS / Not MVP (theo sheet)",
}
IN_SCOPE = {"A", "F", "C", "D"}

def group(d):
    if d["_sheet"] == "Future Release": return "FUT"
    if d["_sheet"] == "OOS - Not MVP": return "OOS"
    lts = (d.get("LTS suggestion") or "").lower(); sgs = (d.get("SGS Comments") or "").lower()
    est = d.get("ESt (Hour)"); has = bool(est) and est not in ("0",)
    try: has = float(est) > 0
    except (TypeError, ValueError): has = False
    if lts == "phase 2" and has: return "C"
    if lts == "phase 2":
        if "suggest to be included in p1" in sgs: return "B2"
        return "B1" if sgs else "B3"
    if "move back to p1" in lts: return "D"
    if not has: return "E"
    return "F" if sgs else "A"

def test_treatment(d, g):
    if d["_id"] == "UC-RGF-001": return "Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-02]"
    if g in IN_SCOPE: return "Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]"
    if g in ("B1", "B2", "B3"): return "Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]"
    if g == "E": return "Chưa xác định – chờ " + ("Q-13" if d["_id"] == "UC-AUD-002" else "Q-15")
    return "Ngoài phạm vi test (theo sheet)"

for d in ALL:
    d["_g"] = group(d)

# ---------- Chuẩn hóa vai trò ----------
ROLES = [("CA", "Customer Admin", r"Customer Admin"), ("CU", "Customer User", r"Customer User"),
         ("CV", "Customer Viewer", r"Customer Viewer"), ("SA", "SGS Admin", r"SGS Admin"),
         ("SU", "SGS User", r"SGS User"), ("STA", "SGS Trainer/Assessor", r"SGS Trainer/Assessor"),
         ("SAC", "SGS Auditor/Certification", r"SGS Auditor(?:/Certification)?"),
         ("SC", "SGS Consultant", r"SGS Consultant")]

def roles(actor):
    a = actor or ""
    if "All authenticated roles" in a:
        return {k: "full" for k, _, _ in ROLES}, "tất cả 8 vai trò đăng nhập"
    res, note = {}, []
    groups = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"\([^)]*\)", a)]
    def ro_span(pos):
        for s, e, txt in groups:
            if s <= pos < e and re.search(r"read-only|view only", txt, re.I): return True
        return False
    for k, _, pat in ROLES:
        for m in re.finditer(pat, a):
            ro = ro_span(m.start())
            after = a[m.end():m.end() + 3]
            if not ro and after.lstrip().startswith("("):
                g = next((t for s, e, t in groups if s >= m.end() and s <= m.end() + 2), "")
                # "(+ ...)" là danh sách bổ sung, không phải bổ nghĩa cho vai trò đứng trước
                ro = (not g.startswith("(+")) and bool(re.search(r"read-only|view only", g, re.I))
            prev = res.get(k)
            res[k] = "full" if prev == "full" or not ro else "read"
    for s, e, txt in groups:
        if "assigned SGS roles" in txt:
            for k in ("SU", "STA", "SAC"):
                res.setdefault(k, "read")
            if "including SGS Consultant" in txt: res.setdefault("SC", "read")
            note.append("'assigned SGS roles' hiểu là SGS User, Trainer/Assessor, Auditor/Certification"
                        + (", Consultant" if "including SGS Consultant" in txt else "") + " [GIẢ ĐỊNH]")
    if re.search(r"\bSystem\b", a): note.append("System")
    if "External Stakeholder" in a: note.append("External Stakeholder")
    if "SGS Auditor" in a and "SGS Auditor/Certification" not in a: note.append("'SGS Auditor' hiểu là SGS Auditor/Certification [GIẢ ĐỊNH]")
    return res, "; ".join(note)

def roles_txt(d):
    r, note = roles(d.get("Actor"))
    parts = [f"{name}{' (xem)' if r[k] == 'read' else ''}" for k, name, _ in ROLES if k in r]
    if not parts:
        return note or "—"
    return ", ".join(parts) + (f" — {note}" if note else "")

# ---------- Phát hiện ----------
# (Bảng F đầy đủ — 40 dòng — giữ nguyên như đã chạy thật, xem lịch sử phân tích SGS DTP.
#  Mỗi dòng: id, loại, vị trí nguồn, UC liên quan, nội dung phát hiện, câu hỏi liên quan.
#  Cấu trúc này — không phải nội dung — là phần nên copy sang dự án khác.)
F = [
 ("F-01","Số liệu","Scope Summary!B2:B3",[],"Scope Summary ghi 156 UC MVP và 39 UC Future Release; đếm thực tế là 159 (sheet UC List) và 40 (sheet Future Release). OOS khớp (5).","Q-16"),
 ("F-02","Số liệu","UC List!J2, R185",["UC-SOA-001","UC-SOA-002"],"Công thức tổng giờ J2 không cộng dòng section 30 (R185). Hiện section 30 bằng 0 nên tổng 834 giờ (91 UC có giờ) vẫn đúng, nhưng giờ của SOA sẽ bị bỏ sót khi được ước lượng.","Q-16"),
 ("F-03","Lỗi dữ liệu · Phạm vi","Future Release!R24",["UC-RGF-001"],"UC-RGF-001 bị lệch cột (Description chứa 'Customer Portal', cột WBS chứa mô tả, cột lý do chứa WBS, cột Portal trống) và mâu thuẫn phạm vi: nằm trong Future Release nhưng lý do ghi Q&A #58 xác nhận đưa vào Phase 1.","Q-02"),
 ("F-04","Lỗi dữ liệu","UC List!R158, R163",["UC-CMT-002","UC-CMT-007"],"CMT-002 và CMT-007 cùng tên 'Generate Certification Milestone Notification', mô tả gần giống, mỗi UC 5 giờ → nghi trùng chức năng và tính giờ hai lần.","Q-09"),
 ("F-05","Lỗi dữ liệu","UC List!R182–R183",["UC-MKT-004","UC-MKT-005"],"MKT-005 có tên UC là 'Customer Admin, Customer User' (chép nhầm actor). MKT-004 tên 'View Consultant Details' nhưng mô tả là xem danh sách Consultant → nhiều khả năng MKT-004 là danh sách, MKT-005 là chi tiết.","Q-16"),
 ("F-06","Lỗi dữ liệu","UC List!R123",["UC-TRN-006"],"TRN-006 có Actor là 'rket'.","Q-16"),
 ("F-07","Lỗi dữ liệu","UC List!R18",["UC-USR-009"],"USR-009 (Delete User Account) không có mô tả.","Q-16"),
 ("F-08","Lỗi dữ liệu","UC List!R125",["UC-TRN-009"],"TRN-009 có khoảng trắng cuối ID, không có WBS Reference, module ghi 'Training & SGS Academy' trong khi các UC cùng section ghi 'SGS Academy'.","Q-16"),
 ("F-09","Lỗi dữ liệu","Toàn file",[],"Không có UC-AUD-003 ở cả ba sheet; không có section 24 (đánh số nhảy từ 23 sang 25).","Q-16"),
 ("F-10","Lỗi dữ liệu","UC List!R187",["UC-SOA-002"],"SOA-002 ghi vai trò 'SGS Auditor' thay vì 'SGS Auditor/Certification'.","Q-15"),
 ("F-11","Phạm vi","UC List cột H–J",[],"__F11__","Q-01"),
 ("F-12","Phạm vi","UC List!R82–R83, R158, R163, R172",["UC-CKP-001","UC-CKP-002","UC-CMT-002","UC-CMT-007","UC-OPS-001"],"Các UC có ý kiến SGS 'Suggest to be included in P1' được xử lý không đồng nhất: OPS-001, CMT-002, CMT-007 đã có giờ; CKP-001, CKP-002 chưa có.","Q-01"),
 ("F-13","Phạm vi","UC List!R37, R44",["UC-FWK-003","UC-FWK-013"],"FWK-003 và FWK-013 được LTS ghi 'move back to P1' theo yêu cầu SGS nhưng chưa có giờ.","Q-07"),
 ("F-14","Phạm vi","UC List!R32, R186–R187",["UC-AUD-002","UC-SOA-001","UC-SOA-002"],"AUD-002 chỉ có ghi chú SGS 'Phase 2?'; SOA-001, SOA-002 không có WBS, đề xuất, ý kiến hay giờ → chưa xác định thuộc phạm vi nào.","Q-13, Q-15"),
 ("F-15","Phạm vi","UC List!R116",["UC-RDN-004"],"RDN-004 (readiness overview) được khách xác nhận qua Q&A #23, nhưng LTS đề xuất P2 và SGS chưa phản hồi.","Q-11"),
 ("F-16","Phụ thuộc","UC List!R50, R52, R153–R163",["UC-CRT-001","UC-CRT-002","UC-CRT-003","UC-CMT-001","UC-CMT-003","UC-CMT-004","UC-CMT-005","UC-CMT-006","UC-CMT-007","UC-SCH-004","UC-SCH-006"],"CRT-001 tạo bản ghi 'using the configured certification fields' nhưng cấu hình trường (SCH-004) là P2. Sửa bản ghi (CRT-002) và toàn bộ vòng đời (CMT-001, 003, 004, 005, 006) đều P2 → trạng thái chứng nhận đứng yên, không tự hết hạn, trong khi CRT-003 hiển thị status và expiry. CMT-007 dựa trên 'scheme's configured offsets' (SCH-006, P2).","Q-09"),
 ("F-17","Phụ thuộc","UC List!R94, R95, R97",["UC-EVD-004","UC-EVD-005","UC-EVD-007"],"EVD-004, EVD-005, EVD-007 hiển thị declaration state, maturity declaration, gap flags, freshness — dữ liệu do ASM-001/002, RDN-002/003, CFG-002 tạo ra, đều P2.","Q-11"),
 ("F-18","Phụ thuộc","UC List!R107, R176",["UC-EVD-020","UC-CNS-001"],"Consultant hỗ trợ 'Gap Analysis' (EVD-020) và bình luận trong 'gap context' (CNS-001), nhưng Gap List (RDN-005) và gap rules (RDN-002) là P2.","Q-11"),
 ("F-19","Phụ thuộc","UC List!R82, R89, R113",["UC-CKP-001"],"Nếu kéo CKP-001 về P1 như SGS đề nghị thì cần JRN-004 và RDN-001 (đều P2) để có 'Digital Trust status' và 'recommended next step'.","Q-01"),
 ("F-20","Phụ thuộc","UC List!R103; Future Release!R32–R33, R42–R43",["UC-EVD-014"],"Evidence Package (EVD-017/018) và Accept/Reject Package (REV-009/010) là Future → chưa rõ trong MVP khách nộp bằng chứng cho review thế nào và trạng thái bằng chứng (EVD-014) liên hệ gì với trạng thái item trong review (REV-005).","Q-05"),
 ("F-21","Phụ thuộc","UC List!R61, R65, R66",["UC-ACC-003","UC-ACC-007","UC-ACC-008"],"Tạo tài khoản khách (ACC-003) và mời Customer Admin (ACC-007) thuộc MVP, nhưng kích hoạt tài khoản (ACC-008) là P2 → chưa rõ trạng thái mặc định sau khi tạo.","Q-14"),
 ("F-22","Thiếu luồng","UC List!R6–R7, R13, R17–R19",["UC-USR-004","UC-USR-008","UC-USR-009","UC-USR-010","UC-AUTH-003","UC-AUTH-004"],"MVP không có sửa, vô hiệu hóa, xóa người dùng (USR-004/008/009) và không có đặt lại mật khẩu (AUTH-003/004, USR-010). SGS đã chấp nhận hỗ trợ thủ công cho mật khẩu, chưa có ý kiến về thu hồi quyền truy cập → người nghỉ việc vẫn đăng nhập được.","Q-14"),
 ("F-23","Thiếu luồng","UC List!R77, R79",["UC-SCP-005","UC-SCP-007"],"Không có UC xóa scope; Archive Scope (SCP-005) là P2 → scope tạo sai không gỡ được. SCP-007 gỡ framework khỏi scope nhưng không nói workspace tương ứng ra sao.","Q-08"),
 ("F-24","Thiếu luồng","UC List!R39–R41",["UC-FWK-005","UC-FWK-006","UC-FWK-007"],"Tạo requirement/control (FWK-005) và retire (FWK-007) thuộc MVP, nhưng sửa (FWK-006) là P2.","Q-07"),
 ("F-25","Thiếu luồng","UC List!R125",["UC-TRN-009"],"Không có UC quản trị catalogue đào tạo tại chỗ; 'tracks' chưa rõ theo dõi cái gì.","Q-17"),
 ("F-26","Thuật ngữ","UC List!R44, R78, R92; Future Release!R29",["UC-SCP-006","UC-EVD-002","UC-FWK-013","UC-DSC-005"],"Bốn cách gọi cho việc gắn framework: 'Link Framework to Scope' (SCP-006), 'framework is activated on a scope' (EVD-002), 'Activate Framework' ở cấp nền tảng (FWK-013), 'Activate Recommended Frameworks' / CP-12 (DSC-005, Future).","Q-08"),
 ("F-27","Thuật ngữ","UC List!R91–R92",["UC-EVD-001","UC-EVD-002"],"'Certification cycle' dùng để chặn tạo trùng workspace nhưng không được định nghĩa; không UC nào trong MVP bắt đầu một chu kỳ mới.","Q-08"),
 ("F-28","Mơ hồ","UC List!R138, R142, R145, R150, R151",["UC-REV-001","UC-REV-005","UC-REV-008","UC-REV-015","UC-REV-016"],"Review Workflow thiếu: danh sách trạng thái item (REV-005), quy tắc suy ra trạng thái tổng (REV-016), định nghĩa 'completed' để đóng (REV-015), phân loại finding (REV-008), vai trò nào tạo loại review nào và 'review-context separation' (A2) ẩn gì với ai (REV-001).","Q-04"),
 ("F-29","Mơ hồ","UC List!R103–R104, R106",["UC-EVD-014","UC-EVD-015","UC-EVD-019"],"EVD-014 cho khách hàng đặt cả 'reviewed', 'rejected', 'accepted'; không có bảng chuyển trạng thái; ghi chú ở EVD-019 cho thấy việc archive thuộc CP-20 phần P2 trong khi EVD-014 có trạng thái 'archived'. EVD-015 xóa 'where retention policy permits' nhưng chưa có chính sách.","Q-05"),
 ("F-30","Mơ hồ","UC List!R127–R135",["UC-SRQ-001","UC-SRQ-004","UC-SRQ-006","UC-SRQ-007","UC-SRQ-008","UC-SRQ-009"],"Service Request chưa có trạng thái khởi tạo và bảng chuyển; 'before SGS delivery begins' (SRQ-004) chưa gắn với trạng thái cụ thể; danh mục loại yêu cầu còn mở (Q&A #33); SGS Consultant được giao yêu cầu tư vấn (SRQ-006) nhưng không có trong actor của SRQ-007/008/009; SRQ-009 thiếu SGS Auditor/Certification so với SRQ-007/008.","Q-06"),
 ("F-31","Mơ hồ","UC List!R15, R96, R146",["UC-USR-006","UC-EVD-006","UC-REV-011"],"EVD-006 cho Customer User xem 'all evidence held by the organization', trong khi USR-006 giới hạn Customer User theo scope và REV-011 ghi 'assigned scope'.","Q-10"),
 ("F-32","Mơ hồ · Khó test","UC List!R21–R25",["UC-ROL-001","UC-ROL-002"],"ROL-001 (36 giờ, UC lớn nhất) thực thi 'predefined role and permission matrix' nhưng ma trận không có trong tài liệu → không có oracle cho test phân quyền. Ghi chú FRD 4.3 (ở ROL-003..005) nói mô hình 7 vai trò, danh sách UC có 8 vai trò.","Q-03"),
 ("F-33","Mơ hồ","UC List!R8",["UC-AUTH-005"],"AUTH-005 chỉ liệt kê 4 vai trò kích hoạt qua lời mời (Customer Admin, Customer User, SGS User, SGS Consultant); thiếu Customer Viewer, SGS Admin, SGS Trainer/Assessor, SGS Auditor/Certification.","Q-14"),
 ("F-34","Mơ hồ","UC List!R64, R127, R132, R182–R184",["UC-ACC-006","UC-SRQ-001","UC-SRQ-006","UC-MKT-004","UC-MKT-005","UC-MKT-006"],"Chưa rõ hồ sơ Consultant trên Marketplace (nội dung do SGS Admin quản lý, MKT-006) có gắn với tài khoản vai trò SGS Consultant không; ACC-006 cho tối đa 1 Consultant active mỗi khách hàng, chưa rõ xử lý khi khách chọn Consultant khác qua Marketplace (MKT-005 → SRQ-001).","Q-12"),
 ("F-35","Mơ hồ","UC List!R37, R42",["UC-FWK-003","UC-FWK-008"],"SGS yêu cầu hỗ trợ ban đầu 'ISO27001, ISO42001 and CMS' — chưa rõ 'CMS' là framework nào. FWK-008: SGS hỏi 'What are the types of evidences? Files?' và gợi ý lùi P2, chưa có trả lời.","Q-07"),
 ("F-36","Mơ hồ","12 UC trong phạm vi đề xuất",["UC-NTF-001","UC-AUD-001","UC-FWK-004","UC-EVD-008","UC-EVD-011","UC-EVD-014","UC-EVD-015","UC-SRQ-001","UC-SRQ-006","UC-REV-001","UC-REV-004","UC-MKT-003"],"Cụm từ cần được liệt kê cụ thể trong UC spec: 'such as' (NTF-001, EVD-008, MKT-003), 'relevant' (NTF-001, SRQ-001, REV-001, REV-004), 'sensitive' (AUD-001), 'supported' (FWK-004, EVD-008, SRQ-001), 'where permitted' (EVD-011), 'permitted transitions' (EVD-014), 'retention policy' (EVD-015), 'where applicable' / 'appropriate' (SRQ-006).","Q-05, Q-06, Q-13"),
 ("F-37","Khó test","UC List!R31–R33",["UC-AUD-001","UC-AUD-002","UC-AUD-004"],"Nếu AUD-002 là P2 thì MVP không có màn hình để SGS xem audit do AUD-001 ghi; AUD-004 chỉ hiển thị hoạt động của tổ chức khách → cần API hoặc DB để kiểm chứng AUD-001.","Q-13"),
 ("F-38","Khó test","UC List!R158, R163",["UC-CMT-002","UC-CMT-007"],"CMT-002/007 là job chạy theo thời gian → môi trường test cần cách kích hoạt job hoặc chỉnh thời gian.","Q-18"),
 ("F-39","Khó test","UC List!R119–R120",["UC-TRN-001","UC-TRN-002"],"TRN-001/002 phụ thuộc Academy API bên ngoài; cần sandbox hoặc mock để test cả trường hợp API lỗi. 'Graceful message' chưa có nội dung cụ thể.","Q-18"),
 ("F-40","Khó test","UC List!R63, R180, R182",["UC-ACC-005","UC-MKT-002","UC-MKT-004"],"Dữ liệu Pentesting và Consultant do SGS Taiwan cung cấp (MKT-002/004); test ranh giới affiliate (ACC-005) cần ít nhất hai affiliate.","Q-18"),
]

# F-11 text with computed numbers
p2 = [d for d in MVP if d["_g"] in ("B1", "B2", "B3", "C")]
p2_wbs_p1 = [d for d in p2 if "(P1)" in (d.get("WBS Reference") or "")]
cnt = collections.Counter(d["_g"] for d in MVP)
F = [(a, b, c, u, (f"{len(p2)}/{len(MVP)} UC trong sheet MVP được LTS đề xuất Phase 2: {cnt['B3']} chưa có phản hồi SGS (B3), "
                   f"{cnt['B1']} SGS đồng ý (B1), {cnt['B2'] + cnt['C']} SGS muốn giữ P1 (B2, C). {len(p2_wbs_p1)} UC trong số đó có WBS ghi P1. "
                   "Tên file là 'final confirmation' nhưng phạm vi chưa chốt.") if t == "__F11__" else t, q)
     for a, b, c, u, t, q in F]

uc_f = collections.defaultdict(list)
for fid, _, _, ucs, _, _ in F:
    for u in ucs: uc_f[u].append(fid)

# ---------- Annotations cho inventory ----------
ann = {}
for d in ALL:
    g = d["_g"]
    ann[d["_id"]] = {
        "Nhóm phạm vi": GROUP_TXT[g],
        "Xử lý test": test_treatment(d, g),
        "Vai trò (chuẩn hóa)": roles_txt(d),
        "Phát hiện": ", ".join(uc_f.get(d["_id"], [])) or "—",
    }
json.dump(ann, open("/home/claude/work/annotations.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- Snippets ----------
def short(u): return u.replace("UC-", "")
snip = {}
snip["counts"] = "\n".join([
    "| Hạng mục | Scope Summary ghi | Đếm lại | Lệch |", "|---|---|---|---|",
    f"| MVP UC List | 156 | {len(MVP)} | {len(MVP) - 156:+d} |",
    f"| Future Release | 39 | {len(FUT)} | {len(FUT) - 39:+d} |",
    f"| OOS / Not MVP | 5 | {len(OOS)} | {len(OOS) - 5:+d} |",
    "| Pending Clarification | 0 | 0 | 0 |",
    f"| **Tổng** | **200** | **{len(ALL)}** | **{len(ALL) - 200:+d}** |",
])
est_rows = [d for d in MVP if d["_g"] in ("A", "F", "C")]
tot = sum(float(d["ESt (Hour)"]) for d in est_rows)
snip["hours"] = f"{int(tot)} giờ trên {len(est_rows)} UC có giờ"

order = ["A", "F", "C", "D", "B2", "B1", "B3", "E"]
rows = ["| Nhóm | Số UC | UC | Xử lý test đề xuất [GIẢ ĐỊNH – chờ Q-01] |", "|---|---|---|---|"]
for g in order:
    ids = [short(d["_id"]) for d in MVP if d["_g"] == g]
    treat = {"A": "Trong phạm vi", "F": "Trong phạm vi", "C": "Trong phạm vi", "D": "Trong phạm vi",
             "B2": "Ngoài phạm vi đến khi chốt", "B1": "Ngoài phạm vi", "B3": "Ngoài phạm vi",
             "E": "Chưa xác định (Q-13, Q-15)"}[g]
    idtxt = ", ".join(ids) if g != "A" else f"{len(ids)} UC — xem uc-inventory.md"
    rows.append(f"| {GROUP_TXT[g]} | {len(ids)} | {idtxt} | {treat} |")
rows.append(f"| **Tổng** | **{len(MVP)}** | | **Trong phạm vi: {sum(1 for d in MVP if d['_g'] in IN_SCOPE)}** |")
snip["scope"] = "\n".join(rows)

# section-level summary
sec = collections.OrderedDict()
for d in MVP:
    s = sec.setdefault(d["_sec"], collections.Counter()); s[d["_g"] in IN_SCOPE] += 1
srows = ["| Section | Tổng UC | Trong phạm vi đề xuất | Ngoài / chưa xác định |", "|---|---|---|---|"]
for s, c in sec.items():
    srows.append(f"| {s} | {c[True] + c[False]} | {c[True]} | {c[False]} |")
snip["sections"] = "\n".join(srows)

# role matrix (in scope)
hdr = "| UC | Tên UC | " + " | ".join(k for k, _, _ in ROLES) + " | Khác |"
mrows = [hdr, "|" + "---|" * (len(ROLES) + 3)]
for d in MVP:
    if d["_g"] not in IN_SCOPE: continue
    r, note = roles(d.get("Actor"))
    other = []
    if re.search(r"\bSystem\b", d.get("Actor") or ""): other.append("System")
    cells = ["✓" if r.get(k) == "full" else ("xem" if r.get(k) == "read" else "") for k, _, _ in ROLES]
    bad = any(t.startswith("Lỗi dữ liệu") for fid, t, _, us, _, _ in F if d["_id"] in us)
    name = (d.get('Use Case Name') or '') + (" ⚠" if bad else "")
    mrows.append(f"| {short(d['_id'])} | {name} | " + " | ".join(cells) + f" | {', '.join(other)} |")
snip["matrix"] = "\n".join(mrows)

# findings table
frows = ["| ID | Loại | Vị trí | Phát hiện | Câu hỏi |", "|---|---|---|---|---|"]
for fid, typ, where, _, txt, q in F:
    frows.append(f"| {fid} | {typ} | {where} | {txt} | {q} |")
snip["findings"] = "\n".join(frows)
snip["n_findings"] = str(len(F))
snip["n_in"] = str(sum(1 for d in MVP if d["_g"] in IN_SCOPE))
json.dump(snip, open("/home/claude/work/snippets.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("groups:", dict(cnt)); print("in scope:", snip["n_in"]); print("hours:", snip["hours"])
print("p2 with WBS P1:", len(p2_wbs_p1), "of", len(p2))
print(snip["counts"]); print(snip["scope"]); print(snip["sections"])
