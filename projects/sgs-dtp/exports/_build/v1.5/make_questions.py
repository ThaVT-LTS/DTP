#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh danh sách câu hỏi mở của sheet Scopes từ file TC.

    python make_questions.py <file TC.xlsx> <cau-hoi_Scopes.md> [ghi chú về file, vd "bản Hanna sửa, gửi 13:28 ngày 07/10"]

Đọc từ file TC: cột Open question của sheet Scopes (TC nào đang chờ mã nào, ô Expected đang trống hay đã ghi)
và sheet Cần xác nhận (mã nào đã có trong sheet). Phần câu hỏi đầy đủ, căn cứ và ghi nhận nằm ở QUESTIONS dưới đây:
khi có trả lời hoặc file TC đổi thì sửa cột ghi nhận ở đó rồi chạy lại.
"""
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flat import flat  # noqa: E402
from xl import Book  # noqa: E402

SHEET, ASK_SHEET = "Scopes", "Cần xác nhận"
LEVELS = ["CHẶN", "QUAN TRỌNG", "NHỎ"]

# (mã, mức, chủ đề, câu hỏi, căn cứ ghi ngày 01/10 — Q-S-28: 06/10, ghi nhận 07/10)
QUESTIONS = [
("Q-S-01", "NHỎ", "Mô tả trang của Customer User",
 "Customer User thấy mô tả \"Scopes assigned to you. Only scopes assigned to you are listed.\" — đây có phải text chính thức?",
 "Figma Scopes / List chỉ có bản Customer Admin. Prototype đổi mô tả theo vai trò.",
 ""),
("Q-S-02", "NHỎ", "Tên khách hàng ngắn hay đầy đủ",
 "Mô tả trang danh sách dùng tên ngắn, dòng phụ màn chi tiết dùng tên pháp lý. Lấy từ hai trường khác nhau có đúng chủ ý?",
 "Danh sách: \"The parts of ABC Trading you prepare…\". Chi tiết: \"Organization scope · ABC Trading Co., Ltd.\"",
 ""),
("Q-S-03", "NHỎ", "Nhãn nút có dấu +",
 "Nhãn chính thức là \"Create scope\" / \"Link framework\" hay \"+ Create scope\" / \"+ Link framework\"?",
 "Figma không có dấu +. Prototype có dấu +.",
 ""),
("Q-S-04", "QUAN TRỌNG", "Trường Belongs to khi tạo scope System",
 "1) Belongs to organisation bắt buộc hay không? 2) Mỗi trường chọn được một hay nhiều scope? 3) Đổi từ System sang loại khác thì giá trị đã chọn bị bỏ? 4) Figma frame Create scope có hai trường này không?",
 "Prototype: chọn System hiện \"Belongs to organisation\" (không * , không \"(optional)\") và \"Belongs to product (optional)\" mặc định None. UC-SCP-003: \"a system may belong to both an organization and a product\".",
 "Bản v1.4: Hanna thêm case tạo scope System bỏ trống cả hai trường Belongs to, cột Belongs to hiện \"—\" (Scope_040). Phần 1 có câu trả lời theo hệ thống đang chạy (không bắt buộc), chờ SGS xác nhận. Case \"System chưa chọn Belongs to organisation\" của v1.3 đã được Hanna thay bằng case khác (Scope_019)."),
("Q-S-05", "CHẶN", "Kiểm tra dữ liệu khi tạo, sửa, gắn",
 "Cần text lỗi nguyên văn cho: không chọn Type; bỏ trống Name; bỏ trống What is in scope; chưa chọn Framework; chưa chọn tier. Giới hạn ký tự của Name, What is in scope, What is out of scope. Trùng tên trong tenant: chặn hay cho phép, có phân biệt hoa thường? Name chỉ có khoảng trắng coi là rỗng? Nút gắn bị khoá khi chưa chọn hay bấm được rồi báo lỗi?",
 "UC, Figma và prototype đều không có text lỗi hay giới hạn.",
 "Bản v1.4: Hanna điền text lỗi theo hệ thống đang chạy và vẫn giữ câu hỏi: \"Choose the type of scope.\" (Scope_015) · \"Enter a name.\" (Scope_016, 017, 076) · \"Describe what is in scope.\" (Scope_018, 019, 077) · \"A scope with this name already exists.\" (Scope_020, 078). Chưa có: giới hạn ký tự (Scope_021), chưa chọn framework, chưa chọn tier (Scope_101, 102). Câu \"UC, Figma và prototype đều không có text lỗi\" ở cột căn cứ vì vậy không còn đúng với hệ thống đang chạy."),
("Q-S-06", "NHỎ", "Huỷ khi đang nhập dở",
 "Đang nhập dở mà bấm Cancel, × hoặc nhấn Esc: đóng ngay hay hỏi xác nhận?",
 "Prototype đóng ngay, kể cả khi nhấn Esc. Thiết kế không ghi.",
 "Bản v1.4: Hanna điền Expected cho case nhấn Esc (hộp thoại đóng, không tạo scope — Scope_024), vẫn giữ câu hỏi."),
("Q-S-07", "QUAN TRỌNG", "Tìm kiếm",
 "1) Tìm theo trường nào (tên, mô tả)? 2) Có phân biệt hoa thường, có dấu? 3) Dòng đếm \"<n> scopes\" giữ tổng hay đổi theo kết quả? 4) Text khi không có kết quả?",
 "Prototype: không phân biệt hoa thường, tìm chuỗi con trong tên; dòng đếm giữ \"4 scopes\" trong khi phân trang đổi thành \"1–2 of 2 items\"; không có kết quả thì hiện \"No results for “zzqq”\" và \"Try a different search term.\" Figma chưa có trạng thái này.",
 "Chiều 07/10: Hanna điền Expected cho case nhập chữ hoa — không phân biệt chữ hoa, chữ thường (Scope_031), vẫn giữ câu hỏi."),
("Q-S-08", "NHỎ", "Sắp xếp",
 "Thứ tự mặc định khi mở màn là gì? Cột nào sắp xếp được?",
 "Figma không có icon sắp xếp. Prototype chỉ cột Scope sắp được (A→Z, Z→A); mặc định không theo tên.",
 "Bản v1.4: Hanna điền thứ tự mặc định là thời gian cũ nhất xuống mới nhất (Scope_054), vẫn giữ câu hỏi."),
("Q-S-09", "QUAN TRỌNG", "Phân trang",
 "Dùng bản Figma hay bản prototype? Số dòng mỗi trang mặc định là bao nhiêu?",
 "Figma: \"1–4 of 4 items · Page 1 of 1\", không chọn số dòng. Prototype: \"Items per page 10\" (10/25/50/100) · \"1–4 of 4 items\" · \"[1] of 1 page\" · nút ‹ ›.",
 "Bản v1.4: Hanna điền theo hệ thống đang chạy và vẫn giữ câu hỏi: mặc định 10 items (Scope_057), chọn giá trị khác thì bảng hiển thị đủ số dòng (Scope_059); thêm case các giá trị 10, 25, 50, 100 items (Scope_058, không kèm câu hỏi)."),
("Q-S-10", "CHẶN", "Trạng thái rỗng",
 "Text tiêu đề, mô tả và nút (nếu có) của màn Scopes khi tenant chưa có scope nào.",
 "Figma có frame Scopes / Empty, AI chưa đối chiếu được text.",
 "Bản v1.4: Hanna điền text theo hệ thống đang chạy (\"Create your first scope\" và đoạn mô tả — Scope_007), vẫn giữ câu hỏi."),
("Q-S-11", "CHẶN", "Evidence coverage trong MVP",
 "1) MVP có hiển thị độ phủ bằng chứng trên màn Scopes không? 2) Nếu có thì thuộc UC nào, bao nhiêu giờ? 3) Công thức: tổng requirement đã có bằng chứng / tổng requirement của mọi framework, như prototype? Làm tròn thế nào?",
 "Hiện ở 3 chỗ: cột Evidence coverage (danh sách), cột Coverage (khối Frameworks), khối Summary. UC tính và xem chỉ số là RDN-001, RDN-004: 0 giờ, LTS đề xuất Phase 2, SGS chưa ý kiến → [ĐỀ XUẤT LÙI]. SCP-001/002 không nhắc độ phủ. Prototype: Head office 54% = (74+6)/(116+31), không phải trung bình 41,5%.",
 "Bản v1.4: Hanna thêm 6 case có bộ số cụ thể và phép tính cho cột Evidence coverage (Scope_044 → 049); 5 case đầu không kèm câu hỏi. Bản v1.5: AI thêm 3 case biên về làm tròn (Scope_051 → 053) và viết 4 case cột Coverage cùng kiểu (Scope_089 → 092). Chiều 07/10: Hanna điền kết quả cho 3 case biên (12.5% → 13%, 0.4% → 0%, 99.6% → 100%) và cho khối Summary (\"Hiển thị thông tin giống khung Frameworks\" — Scope_126), vẫn giữ câu hỏi. Cách ghi Expected cho giá trị tính toán chờ Hanna xác nhận (FB-048). `tests/design/bo-cuc-sheet_uc-v4.md` (05/10) ghi UC-RDN-004 đã sang P2 ở UC List v4; sheet Scopes đang có 15 TC trỏ UC-RDN-004."),
("Q-S-12", "NHỎ", "Cột Users đếm những ai",
 "Số ở cột Users có tính Customer Admin không? Tenant có 3 admin thì scope mới tạo hiện 3?",
 "Prototype: cột Users bằng số dòng ở khối Users, gồm cả dòng \"Customer Admin · sees every scope\" (Retail loyalty app = 1, chỉ có admin).",
 ""),
("Q-S-13", "NHỎ", "Scope chưa gắn framework",
 "Xác nhận text \"None linked yet\" ở cột Frameworks; cột Evidence coverage hiện \"—\"; khối Frameworks ở màn chi tiết khi chưa có framework hiển thị gì?",
 "Figma có \"None linked yet\" cho AI platform. Prototype không có scope nào chưa gắn framework.",
 "Bản v1.5: AI thêm 2 case — cột Evidence coverage khi scope chưa gắn framework (Scope_050), khối Frameworks khi chưa gắn framework (Scope_084). Chiều 07/10: Hanna điền theo hệ thống đang chạy và vẫn giữ câu hỏi: cột Evidence coverage hiện \"—\" (Scope_050); khối Frameworks hiện \"No framework linked yet. Link one to create a workspace and start collecting evidence.\" (Scope_084)."),
("Q-S-14", "QUAN TRỌNG", "Xoá và lưu trữ scope",
 "MVP có xoá scope không? Ngoài \"Active\" scope còn trạng thái nào?",
 "Menu ⋮ chỉ có \"Edit scope\". SCP-005 Archive: 0 giờ, LTS đề xuất Phase 2. Nhưng WBS ghi \"CP-06 CRUD (P1) implies hard delete only\" — WBS có tính xoá, không có UC xoá, không có nút xoá.",
 ""),
("Q-S-15", "QUAN TRỌNG", "Hộp thoại sửa scope",
 "Hộp thoại Edit scope của prototype có phải thiết kế chính thức? Không cho đổi Type và Belongs to — đúng chủ ý?",
 "SCP-004 có 5 giờ, Figma không có frame sửa. Prototype: Name *, What is in scope *, What is out of scope (optional), Cancel / Save.",
 ""),
("Q-S-16", "QUAN TRỌNG", "Khoá khi đang có audit",
 "1) Quy tắc khoá có đúng không? 2) Một framework đang audit thì sửa scope bị khoá toàn bộ? 3) Gắn thêm framework, gán người dùng có bị khoá? 4) Text chính thức?",
 "Prototype, scope Customer data platform: bấm Edit → \"The scope can't be edited while an audit is running.\"; Change tier → \"Tier can't be changed during an audit … Unlinking the framework and editing the scope are blocked for the same reason.\" Không UC nào ghi quy tắc này. Figma có frame Change tier locked, AI chưa đối chiếu text.",
 "Chiều 07/10: Hanna chuyển case gắn thêm framework khi scope đang có audit sang nhóm Thành công và bỏ câu hỏi ở TC đó (Scope_104). Phần 3 có câu trả lời theo hệ thống đang chạy (vẫn gắn được), chờ SGS xác nhận."),
("Q-S-17", "CHẶN", "Tier thuộc UC nào",
 "1) \"obligation level\" trong SCP-002 có phải là tier? 2) Đổi tier sau khi gắn thuộc UC nào (SCP-004, SCP-006 hay chưa có)? 3) Framework không phân tier: hộp thoại gắn ẩn phần tier? 4) Hiển thị tier thống nhất thế nào?",
 "Tier có ở cột Tier, hộp thoại Link, hộp thoại Change tier, cột Frameworks của danh sách. Không UC nào nhắc tier. Prototype ghi \"Medium · 中\" ở bảng Frameworks nhưng \"Medium\" ở danh sách và Summary.",
 "`tests/design/bo-cuc-sheet_uc-v4.md` (05/10) ghi: UC List v4 không có UC đổi tier, tier chỉ chọn lúc tạo workspace; 6 TC Đổi tier (Scope_109 → 114) đang ghi [NGOÀI UC]. Chiều 07/10: Hanna điền Expected cho case chọn framework không phân tier — 'Không hiển thị button \"Change tier\"' (Scope_100), vẫn giữ câu hỏi."),
("Q-S-18", "QUAN TRỌNG", "Số requirement của tier High",
 "Tier High của Appendix 10 có 79 hay 76 requirement?",
 "Figma (Link framework): Basic 44 · Medium 61 · High 79. Prototype: 44 · 61 · 76, mô tả \"Medium + 15 more controls\" (61 + 15 = 76).",
 ""),
("Q-S-19", "QUAN TRỌNG", "Framework đã gắn trong danh sách chọn",
 "Framework đã gắn vào scope phải ẩn, hiện nhưng khoá, hay cho gắn lần hai (ví dụ khác phiên bản)?",
 "Prototype: Head office đã có ISO/IEC 27001 và ISO 22301, danh sách vẫn liệt kê và chọn được cả hai.",
 "Chiều 07/10: Hanna điền theo hệ thống đang chạy và vẫn giữ câu hỏi: framework đã gắn vẫn hiện trong danh sách chọn, có thông báo đỏ \"… is already linked to this scope.\" (Scope_098)."),
("Q-S-20", "QUAN TRỌNG", "Workspace sau khi gắn framework",
 "Workspace được tạo ngay hay sau một khoảng? Trạng thái ban đầu là gì? Danh sách đầy đủ các trạng thái?",
 "SCP-006: \"triggering workspace creation\". Prototype có \"Preparing\" và \"Audit in progress\".",
 "`tests/design/bo-cuc-sheet_uc-v4.md` (05/10) đề xuất chuyển các TC Gắn framework, Gỡ framework sang sheet Workspaces (nay là Scope_096 → 107); file TC vẫn để ở sheet Scopes."),
("Q-S-21", "CHẶN", "Gỡ framework (SCP-007)",
 "MVP có gỡ framework không? Lối vào ở đâu? Bằng chứng và lịch sử review giữ lại hiển thị ở đâu?",
 "SCP-007 có 8 giờ, WBS: \"PRESALE WBS GAP — Unlinking a framework from a scope is not priced\". Figma và prototype không có lối vào. Nhưng text khoá audit có nhắc \"Unlinking the framework … blocked\".",
 "Chiều 07/10: Hanna bỏ TC duy nhất của câu này (Scope_108 ở bản v1.5). Câu hỏi vẫn mở."),
("Q-S-22", "QUAN TRỌNG", "Đổi tier và bằng chứng",
 "Nâng tier: bằng chứng đã tải giữ nguyên? Hạ tier: bằng chứng của requirement bị bỏ ra sao, có cảnh báo?",
 "Figma Change tier: cảnh báo độ phủ giảm khi nâng tier. Hộp thoại Link ghi \"You can change the tier later; uploaded evidence stays.\" Prototype không có dữ liệu để mở hộp thoại đổi tier không khoá.",
 "Chiều 07/10: Hanna điền Expected cho case hạ tier (Scope_114); nội dung đang giống case nâng tier, cần Hanna xem lại (`so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 3)."),
("Q-S-23", "QUAN TRỌNG", "Ai được gán vào scope, thu hồi",
 "Customer Viewer có được gán? Người đang chờ kích hoạt có được gán? Bỏ tick (thu hồi) có thuộc USR-006, có cần xác nhận?",
 "USR-006: \"Grant a Customer User access…\". Prototype: danh sách có cả Customer Viewer (Iris Huang) và người \"invitation pending\"; bỏ tick là thu hồi.",
 "Sheet Cần xác nhận (viết 05/10) ghi: phần \"thu hồi có thuộc USR-006 không\" đã được UC List v4 trả lời — USR-05 có \"Grant or remove\". Ô Open question của Scope_124, Scope_125 vẫn còn hỏi phần này."),
("Q-S-24", "CHẶN", "Customer Viewer có vào màn Scopes",
 "Customer Viewer có vào được màn Scopes không? Thấy những gì?",
 "Actor của SCP-001/002 không có Customer Viewer. RDN-004 có Customer Viewer. Prototype gán được Viewer vào scope.",
 "`tests/design/bo-cuc-sheet_uc-v4.md` (05/10) có cùng câu hỏi theo UC List v4, mặc định ghi ở đó: theo cột Actor(s), Customer Viewer không mở được."),
("Q-S-25", "QUAN TRỌNG", "SGS xem scope của khách",
 "Lối vào danh sách và chi tiết scope của khách từ SGS Portal nằm ở đâu?",
 "SCP-001/002: SGS roles được phân công xem chỉ đọc, portal \"Customer Portal & SGS Portal\". Chưa thấy màn tương ứng.",
 ""),
("Q-S-26", "NHỎ", "Mở scope không tồn tại hoặc không có quyền",
 "Mở URL chi tiết scope không tồn tại, không được gán, hoặc của tenant khác thì hiển thị gì?",
 "Thiết kế không có màn lỗi cho trường hợp này.",
 "Bản v1.4: Hanna điền text theo hệ thống đang chạy cho mã scope không tồn tại (\"This scope doesn’t exist\" và dòng mô tả — Scope_005), vẫn giữ câu hỏi."),
("Q-S-27", "NHỎ", "Ghi audit cho thao tác trên scope",
 "Tạo, sửa scope, gắn framework, đổi tier, gán người dùng có thuộc diện phải ghi audit?",
 "AUD-001: \"sensitive platform, review and service-request actions\" — không liệt kê thao tác cụ thể.",
 ""),
("Q-S-28", "QUAN TRỌNG", "In scope / Out of scope ở danh sách",
 "Danh sách scope có hiển thị What is in scope và What is out of scope của từng scope không?",
 "Hanna yêu cầu kiểm tra cả 4 thông tin (Type, Name, In scope, Out of scope) trên Danh sách sau khi tạo; Figma Screens 05 chỉ có cột Scope (kèm nhãn loại), Belongs to, Frameworks, Users, Evidence coverage.",
 ""),
]


def nfc(s):
    return unicodedata.normalize("NFC", str(s or ""))


def md(s):
    """Chữ đặt trong ô bảng markdown."""
    s = nfc(s).strip().replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
    return s if s else "—"


def ids(lst):
    """Scope_044, Scope_045, Scope_046 → Scope_044 → 046 (gom dải liền nhau)."""
    nums = sorted({int(x.split("_")[1]) for x in lst})
    prefix = lst[0].split("_")[0] if lst else ""
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j - i >= 2:
            out.append("%s_%03d → %03d" % (prefix, nums[i], nums[j]))
        else:
            out.extend("%s_%03d" % (prefix, n) for n in nums[i:j + 1])
        i = j + 1
    return ", ".join(out)


def main():
    book_p, out_p = sys.argv[1], sys.argv[2]
    file_note = sys.argv[3] if len(sys.argv) > 3 else ""
    book = Book(book_p)
    rows = flat(book, SHEET)

    waiting = OrderedDict()                     # mã → [(TVP_ID, ô Open question, Expected có chữ?)]
    no_code = []
    for r in rows:
        oq = nfc(r["OQ"]).strip()
        if not oq:
            continue
        codes = list(dict.fromkeys(re.findall(r"Q-[A-Z]+-\d+", oq)))
        if not codes:
            no_code.append(r["ID"])
        for c in codes:
            waiting.setdefault(c, []).append((r["ID"], oq, bool(nfc(r["Exp"]).strip())))
    n_oq = sum(1 for r in rows if nfc(r["OQ"]).strip())
    n_empty = sum(1 for r in rows if nfc(r["OQ"]).strip() and not nfc(r["Exp"]).strip())

    in_sheet = {}
    if any(n == ASK_SHEET for n, _, _ in book.sheets):
        for (c, r), v in book.cells(ASK_SHEET).items():
            if c == 1 and r > 1 and v[0]:
                in_sheet[nfc(v[0]).strip()] = r

    known = [q[0] for q in QUESTIONS]
    qmap = {q[0]: q for q in QUESTIONS}
    used = sorted(waiting, key=lambda x: int(x.split("-")[2]))
    missing_def = [c for c in used if c not in known]
    if missing_def:
        raise SystemExit("Mã có trong file TC mà chưa có trong QUESTIONS: %s" % ", ".join(missing_def))
    unused = [c for c in known if c not in waiting]
    absent = [c for c in known if c not in in_sheet]

    L = []
    w = L.append
    w("# Câu hỏi mở của sheet Scopes")
    w("")
    w("- Sinh bằng `exports/_build/v1.5/make_questions.py` từ `exports/%s`%s. Số TC và số đếm do script đọc từ file." % (
        Path(book_p).name, (" (%s)" % file_note) if file_note else ""))
    w("- Sheet %s: %d TC, trong đó **%d TC còn câu hỏi mở**, dùng **%d mã** `Q-S`; **%d TC để trống Expected**, số còn lại đã ghi Expected kèm câu hỏi." % (
        SHEET, len(rows), n_oq, len(used), n_empty))
    w("- Danh sách có %d câu. Sheet `%s` của file TC mới có **%d câu** (%s); %d câu còn lại chỉ được nhắc ở cột Open question của từng TC, chưa có chỗ nào trong thư mục ghi câu hỏi đầy đủ — file này bù chỗ đó." % (
        len(known), ASK_SHEET, len(known) - len(absent), ", ".join(c for c in known if c in in_sheet), len(absent)))
    w("- Cột \"Câu hỏi\" và \"Căn cứ\" ở mục 2 là bản AI viết ngày 01/10 (Q-S-28: ngày 06/10), dựa trên UC List v2.1, Figma và prototype; mã UC trong đó là mã của v2.1 (vd `SCP-001`). **Chưa soát lại theo UC List v4.** Cột \"Ghi nhận\" là điều thấy trong các bản file TC ngày 07/10 và trong `tests/design/bo-cuc-sheet_uc-v4.md`.")
    w("- Mức do AI xếp, chờ Hanna duyệt: CHẶN là chưa trả lời thì không viết được Expected cho cả một nhóm TC.")
    if no_code:
        w("- TC có chữ ở cột Open question mà không ghi mã: %s." % ids(no_code))
    if unused:
        w("- Câu không còn TC nào chờ: %s." % ", ".join(unused))
    w("")

    w("## 1. Tổng hợp")
    w("")
    w("| Mức | Số câu | Mã | Số TC đang chờ |")
    w("|---|---|---|---|")
    for lv in LEVELS:
        cs = [c for c in known if qmap[c][1] == lv]
        tcs = sorted({t for c in cs for t, _, _ in waiting.get(c, [])})
        w("| %s | %d | %s | %d |" % (lv, len(cs), ", ".join(c.replace("Q-S-", "") for c in cs), len(tcs)))
    w("")
    multi = Counter(t for c in used for t in {x for x, _, _ in waiting[c]})
    twice = sorted(t for t, n in multi.items() if n > 1)
    if twice:
        w("TC chờ hai mã cùng lúc: %s; vì vậy tổng cột cuối lớn hơn %d." % (ids(twice), n_oq))
        w("")

    w("## 2. Từng câu hỏi")
    w("")
    w("| Mã · mức | Câu hỏi | Căn cứ ghi ngày 01/10 | TC đang chờ | Ghi nhận |")
    w("|---|---|---|---|---|")
    for c in known:
        _, lv, topic, ask, why, note = qmap[c]
        items = waiting.get(c, [])
        tcs = [t for t, _, _ in items]
        empty = [t for t, _, has in items if not has]
        cell = ids(tcs) if tcs else "không còn TC nào"
        if empty:
            cell += "<br>Expected trống: " + ids(empty)
        mark = "" if c in in_sheet else "<br>chưa có trong sheet"
        w("| **%s**<br>%s%s | **%s.** %s | %s | %s | %s |" % (c, lv, mark, md(topic), md(ask), md(why), cell, md(note)))
    w("")

    w("## 3. Nguyên văn ô Open question của từng TC")
    w("")
    w("| Mã | TC | Expected | Ô Open question |")
    w("|---|---|---|---|")
    for c in used:
        groups = OrderedDict()
        for t, oq, has in waiting[c]:
            groups.setdefault((oq, has), []).append(t)
        for (oq, has), ts in groups.items():
            w("| %s | %s | %s | %s |" % (c, ids(ts), "đã ghi" if has else "trống", md(oq)))
    w("")

    w("## 4. Cần Hanna chọn")
    w("")
    w("1. Có đưa %d câu còn thiếu vào sheet `%s` của file TC không? AI chưa đưa, vì căn cứ đang viết theo UC List v2.1 và prototype; nên soát theo UC List v4 trước (file UC List v4 chưa có trong `docs/source`)." % (len(absent), ASK_SHEET))
    w("2. Các TC Hanna đã điền Expected theo hệ thống đang chạy mà vẫn giữ câu hỏi (xem cột \"Ghi nhận\"): coi là Expected tạm chờ SGS xác nhận, hay coi là đã có căn cứ và đóng câu hỏi? Liên quan dòng 1 ở `so-sanh_v1.5-ban-Hanna-sua-0710.md` mục 2.")
    w("3. Q-S-23: phần \"thu hồi có thuộc USR-006 không\" được sheet `%s` ghi là đã có trả lời ở UC List v4. Nếu đúng thì sửa ô Open question của Scope_124, Scope_125 (Scope_125 chỉ còn hỏi phần này)." % ASK_SHEET)
    w("4. Q-S-11: Evidence coverage có kiểm ở giai đoạn này không, khi `bo-cuc-sheet_uc-v4.md` ghi UC-RDN-004 đã sang P2? Góp ý ngày 07/10 yêu cầu thêm TC cho cột này nên file TC đã thêm; cần Hanna xác nhận để biết các TC đó chạy ở giai đoạn nào.")
    w("")

    Path(out_p).parent.mkdir(parents=True, exist_ok=True)
    Path(out_p).write_text("\n".join(L), encoding="utf-8", newline="\n")
    print("câu hỏi: %s · %d câu, %d câu còn TC chờ · %d TC chờ · %d TC trống Expected · %d câu chưa có trong sheet" % (
        out_p, len(known), len(used), n_oq, n_empty, len(absent)))


if __name__ == "__main__":
    sys.exit(main())
