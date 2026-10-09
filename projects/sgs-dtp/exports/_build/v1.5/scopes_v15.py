# -*- coding: utf-8 -*-
"""Bảng phẳng của sheet Scopes bản v1.5.

Phần A (dòng 13–69 của v1.4, No. 1–67 theo cách gọi của Hanna): giữ nội dung của Hanna,
chỉ sửa các chỗ ghi ở TOUCH (gõ nhầm, {{…}} còn sót, ô ID / UC trống) và thêm 4 case biên
cho cột Evidence coverage.
Phần B (dòng 70–148 của v1.4): viết lại theo cách của phần A.

Chạy:  python scopes_v15.py <v1.4.Scopes.json> <out.json>
"""
import json
import sys
import unicodedata

PRE = "Đăng nhập account Customer Admin"
OPEN = "1. Mở chi tiết scope (bấm tên scope ở màn Scopes)"

I_LIST = "Danh sách scope - Scope list"
I_DET = "Chi tiết scope - Scope detail"
I_PERM = "Phân quyền - Permission"
I_SEC = "Bảo mật - Security"


def clean(s):
    """Dạng dựng sẵn (NFC), bỏ khoảng trắng cuối từng dòng, bỏ dòng trống đầu và cuối ô."""
    if s is None:
        return ""
    s = unicodedata.normalize("NFC", str(s)).replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in s.split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


FIELDS = ("I", "II", "III", "IV", "Pri", "Name", "Pre", "Step", "Exp", "OQ", "UC")

Q28 = ("Danh sách scope có hiển thị What is in scope / What is out of scope không? Yêu cầu của Hanna: kiểm tra cả 4 thông tin "
       "trên Danh sách; Figma chỉ có các cột Scope, Belongs to, Frameworks, Users, Evidence coverage → Q-S-28")

# ----------------------------------------------------------------------------- Phần A: chỗ chạm vào
# dòng v1.4 -> (trường, giá trị mới hoặc hàm, lý do)
TOUCH = {
    18: [("Exp", lambda s: s.replace("a system.J18", "a system."),
          "bỏ chữ J18 dính ở cuối ô Expected")],
    28: [("Step", "1. Mở màn Scopes\n2. Mở hộp thoại\n3. Chọn Organization, nhập What is in scope, để trống Name\n4. Bấm Create scope",
          "bước 3 đang trùng case Bỏ trống What is in scope (nhập Name, để trống What is in scope); đặt lại như bản v1.3")],
    31: [("Name", "Kiểm tra tạo scope khi What is in scope chỉ có khoảng trắng",
          "tên case đang trùng case Name chỉ có khoảng trắng"),
         ("OQ", "Khoảng trắng có bị coi là rỗng → Q-S-05",
          "câu hỏi cũ (\"Trường này bắt buộc hay không → Q-S-04\") là của case System chưa chọn Belongs to organisation đã bỏ")],
    38: [("OQ", Q28,
          "câu hỏi cũ (\"Khối Frameworks khi chưa gắn framework hiển thị gì → Q-S-13\") là của case màn chi tiết đã bỏ; "
          "đặt câu Q-S-28 như hai case Organization, System; câu Q-S-13 chuyển xuống case trạng thái rỗng của khối Frameworks")],
    39: [("Step", lambda s: s.replace("[Organisation]", "[Organization]").replace("[Production]", "[Product]"),
          "tên trong ngoặc vuông theo tin nhắn 07/10: [Organization], [Product]"),
         ("Exp", lambda s: s.replace("+ Nhãn loại: Product", "+ Nhãn loại: System")
                           .replace("[Organisation]", "[Organization]").replace("[Production]", "[Product]"),
          "case System đang ghi Nhãn loại: Product; tên trong ngoặc vuông theo tin nhắn 07/10")],
    42: [("Step", "1. Mở màn Scopes\n2. Nhập [từ khóa] là một phần tên scope vào ô tìm kiếm", "thay {{text.partial}}"),
         ("Exp", lambda s: s.replace("{{text.partial}}", "[từ khóa]"), "thay {{text.partial}}")],
    43: [("Step", "1. Mở màn Scopes\n2. Nhập [từ khóa] viết hoa vào ô tìm kiếm", "thay {{text.partial_upper}}")],
    44: [("Step", "1. Mở màn Scopes\n2. Nhập [từ khóa] không khớp tên scope nào vào ô tìm kiếm", "thay {{text.nomatch}}"),
         ("Exp", lambda s: s.replace("{{text.nomatch}}", "[từ khóa]"), "thay {{text.nomatch}}")],
    45: [("Step", "1. Mở màn Scopes\n2. Nhập ' OR 1=1 -- vào ô tìm kiếm", "thay {{text.sql}} bằng chuỗi cụ thể")],
    59: [("Exp", lambda s: s.replace("0/101 × 100", "0/147 × 100"),
          "116 + 31 = 147; số 101 là của case phía trên")],
}

# UC cho các dòng Hanna thêm mà ô UC còn trống: lấy theo case cùng nhóm
UC_FILL = {50: "UC-SCP-001", 51: "UC-SCP-001", 52: "UC-SCP-001",
           56: "UC-RDN-004", 57: "UC-RDN-004", 58: "UC-RDN-004", 59: "UC-RDN-004", 60: "UC-RDN-004",
           66: "UC-SCP-001", 71: "UC-SCP-002", 72: "UC-SCP-002"}

EC = dict(I=I_LIST, II="Bảng danh sách - Table", III="Hiển thị", IV="Cột Evidence coverage", UC="UC-RDN-004", Pre=PRE)
EC_NEW = [
    dict(EC, Pri="Medium", Name="Kiểm tra Evidence coverage khi scope chưa gắn framework nào",
         Step="1. Mở màn hình Scopes\n2. Kiểm tra cột Evidence coverage của scope chưa gắn framework",
         Exp="", OQ="Scope chưa gắn framework: cột Evidence coverage hiện —, 0% hay để trống → Q-S-13",
         note="case biên: không có framework nào để tính"),
    dict(EC, Pri="Medium", Name="Kiểm tra Evidence coverage khi phần thập phân đúng bằng .5",
         Step="1. Mở màn hình Scopes\n2. Tạo Frameworks với:\n- Framework A: 1/8",
         Exp="", OQ="1/8 × 100 = 12.5%: hiển thị 12% hay 13% (cách làm tròn khi phần thập phân đúng bằng .5) → Q-S-11",
         note="case biên: hai case làm tròn phía trên (35.56 → 36, 53.47 → 53) chưa cho biết .5 làm tròn về đâu"),
    dict(EC, Pri="Medium", Name="Kiểm tra Evidence coverage khi kết quả trên 0% và dưới 0.5%",
         Step="1. Mở màn hình Scopes\n2. Tạo Frameworks với:\n- Framework A: 1/250",
         Exp="", OQ="1/250 × 100 = 0.4%: làm tròn như các case trên thì ra 0% dù đã có 1 requirement đủ evidence; "
                    "hiển thị 0%, 1% hay <1% → Q-S-11",
         note="case biên: 0% trong khi đã có evidence"),
    dict(EC, Pri="Medium", Name="Kiểm tra Evidence coverage khi kết quả từ 99.5% đến dưới 100%",
         Step="1. Mở màn hình Scopes\n2. Tạo Frameworks với:\n- Framework A: 249/250",
         Exp="", OQ="249/250 × 100 = 99.6%: làm tròn như các case trên thì ra 100% dù còn 1 requirement chưa đủ evidence; "
                    "hiển thị 100% hay 99% → Q-S-11",
         note="case biên: 100% trong khi chưa đủ"),
]


# ----------------------------------------------------------------------------- Phần B
def R(src, II, III, IV, Pri, Name, Step, Exp, UC, OQ="", Pre=PRE, I=I_DET, note=""):
    return dict(src=src, I=I, II=II, III=III, IV=IV, Pri=Pri, Name=Name, Pre=Pre, Step=Step, Exp=Exp, OQ=OQ, UC=UC, note=note)


def part_b(old):
    """old: {dòng v1.4: bản ghi}. Trả về danh sách dòng của phần B."""
    def keep(src, **over):
        """Giữ nguyên dòng của v1.4 (dòng Hanna đã sửa), chỉ đổi các trường nêu trong over."""
        o = old[src]
        rec = dict(src=src, I=o["I"], II=o["II"], III=o["III"], IV=o["IV"], Pri=o["Pri"], Name=o["Name"], Pre=o["Pre"],
                   Step=o["Step"], Exp=o["Exp"], OQ=o["OQ"], UC=o["UC"], note="")
        rec.update(over)
        return rec

    out = []
    # ---------------------------------------------------------------- Phần đầu - Header
    H = "Phần đầu - Header"
    out += [
        R(70, H, "Hiển thị", "Các thành phần", "High", "Kiểm tra phần đầu màn chi tiết",
          "1. Mở chi tiết scope Organization (bấm tên scope ở màn Scopes)\n2. Kiểm tra phần đầu trang, từ trái sang phải",
          "- Nút quay lại ←\n- Tiêu đề: tên scope\n- Dòng phụ: Organization scope · [Tên Organization]\n- Nhãn Active\n- Nút ⋮ ở góc phải",
          "UC-SCP-002", OQ="Ngoài Active còn trạng thái nào → Q-S-14"),
        keep(71, UC="UC-SCP-002"),
        keep(72, UC="UC-SCP-002"),
        keep(73),
        R(74, H, "Nút quay lại", "Bấm ←", "Medium", "Kiểm tra nút quay lại",
          OPEN + "\n2. Bấm nút ←", "- Quay về màn Scopes", "UC-SCP-002"),
        R(75, H, "Menu ⋮", "Các mục", "Medium", "Kiểm tra menu ⋮ của scope",
          OPEN + "\n2. Bấm nút ⋮", "- Menu chỉ có một mục: Edit scope", "UC-SCP-004",
          OQ="Không có Archive, Delete: SCP-005 lùi Phase 2, nhưng WBS CP-06 ghi CRUD → Q-S-14"),
        R(76, H, "Menu ⋮", "Bấm Edit scope", "Medium", "Kiểm tra mục Edit scope trong menu ⋮",
          OPEN + "\n2. Bấm nút ⋮\n3. Bấm Edit scope", "- Mở hộp thoại Edit scope", "UC-SCP-004",
          OQ="Figma không có frame sửa scope → Q-S-15",
          note="Expected bỏ câu trỏ sang chỗ khác (\"giống khi bấm nút Edit ở khối Overview\")"),
    ]
    # ---------------------------------------------------------------- Điều hướng trong màn
    N = "Điều hướng trong màn - Section nav"
    out += [
        R(77, N, "Hiển thị", "Ba mục", "Low", "Kiểm tra cột điều hướng bên trái",
          OPEN + "\n2. Kiểm tra cột bên trái",
          "- Ba mục theo thứ tự:\n+ Overview\n+ Frameworks\n+ Users\n- Mục Overview được tô nền khi mới mở", "UC-SCP-002"),
        R(78, N, "Bấm mục", "Frameworks, Users", "Low", "Kiểm tra bấm mục trong cột điều hướng",
          OPEN + "\n2. Bấm Frameworks\n3. Bấm Users",
          "- Sau bước 2: trang cuộn tới khối Frameworks\n- Sau bước 3: trang cuộn tới khối Users", "UC-SCP-002",
          note="Expected đang ghi Bước 1, Bước 2 trong khi thao tác ở bước 2, bước 3"),
    ]
    # ---------------------------------------------------------------- Tổng quan - Overview
    O = "Tổng quan - Overview"
    IO = "\n- In scope: [What is in scope]\n- Out of scope: [What is out of scope]"
    out += [
        R(79, O, "Hiển thị", "Scope Organization", "High", "Kiểm tra khối Overview của scope Organization",
          "1. Mở chi tiết scope Organization\n2. Kiểm tra khối số 1 Overview",
          "- Tiêu đề khối: Overview, có nút Edit\n- Type: Organization\n- Contains: [System] (system)" + IO, "UC-SCP-002",
          Pre=PRE + "; scope Organization đã có scope System thuộc về",
          note="ô tô vàng ở v1.4; thông tin của scope ghi từng dòng, dữ liệu trong ngoặc vuông"),
        R(80, O, "Hiển thị", "Scope Product", "Medium", "Kiểm tra khối Overview của scope Product",
          "1. Mở chi tiết scope Product\n2. Kiểm tra khối số 1 Overview",
          "- Type: Product\n- Contains: [System] (system)" + IO, "UC-SCP-002",
          Pre=PRE + "; scope Product đã có scope System thuộc về",
          note="ô tô vàng ở v1.4"),
        R(81, O, "Hiển thị", "Scope System", "High", "Kiểm tra khối Overview của scope System",
          "1. Mở chi tiết scope System\n2. Kiểm tra khối số 1 Overview",
          "- Type: System\n- Không có trường Contains\n- Belongs to: [Organization], [Product]" + IO, "UC-SCP-002",
          Pre=PRE + "; scope System đã chọn Belongs to organisation: [Organization], Belongs to product (optional): [Product]"),
        R(82, O, "Hiển thị", "Trường không có dữ liệu", "Low", "Kiểm tra trường không có dữ liệu",
          "1. Mở chi tiết scope Product\n2. Kiểm tra khối số 1 Overview",
          "- Contains: —\n- Out of scope: —", "UC-SCP-002",
          Pre=PRE + "; scope Product chưa có scope System thuộc về, What is out of scope (optional) để trống"),
    ]
    # ---------------------------------------------------------------- Sửa scope - Edit scope
    E = "Sửa scope - Edit scope"
    ED = OPEN + "\n2. Mở Edit scope"
    out += [
        R(83, E, "Mở hộp thoại", "Bấm Edit", "High", "Kiểm tra mở hộp thoại Edit scope",
          OPEN + "\n2. Bấm nút Edit ở khối Overview",
          "- Mở hộp thoại Edit scope, có nút đóng ×\n- Các trường điền sẵn giá trị hiện tại:\n+ Name *\n+ What is in scope *\n"
          "+ What is out of scope (optional)\n- Không có trường Type, Belongs to\n- Có nút Cancel và nút Save", "UC-SCP-004",
          OQ="Figma không có frame sửa scope; không cho đổi Type, Belongs to có đúng chủ ý → Q-S-15"),
        R(84, E, "Không thành công", "Xoá trống Name", "High", "Kiểm tra lưu khi xoá trống Name",
          ED + "\n3. Xoá hết Name\n4. Bấm Save",
          "- Không lưu, hộp thoại vẫn mở\n- Hiện lỗi tại Name:\n\"Enter a name.\"", "UC-SCP-004",
          OQ="Text lỗi nguyên văn → Q-S-05", note="từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công"),
        R(85, E, "Không thành công", "Xoá trống What is in scope", "High", "Kiểm tra lưu khi xoá trống What is in scope",
          ED + "\n3. Xoá hết What is in scope\n4. Bấm Save",
          "- Không lưu, hộp thoại vẫn mở\n- Hiện lỗi tại What is in scope:\n\"Describe what is in scope.\"", "UC-SCP-004",
          OQ="Text lỗi nguyên văn → Q-S-05", note="từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công"),
        R(86, E, "Không thành công", "Trùng tên scope khác", "Medium", "Kiểm tra đổi Name trùng tên scope khác",
          ED + "\n3. Đổi Name thành tên của một scope khác đang có\n4. Bấm Save",
          "- Không lưu, hộp thoại vẫn mở\n- Hiện lỗi tại Name:\n\"A scope with this name already exists.\"", "UC-SCP-004",
          OQ="Chặn hay cho phép trùng tên → Q-S-05", note="từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công; ô Step tô vàng ở v1.4"),
        R(92, E, "Không thành công", "Bấm Cancel", "Medium", "Kiểm tra huỷ sửa scope",
          ED + ", đổi Name\n3. Bấm Cancel",
          "- Hộp thoại đóng\n- Tiêu đề và khối Overview giữ giá trị cũ", "UC-SCP-004"),
        R(93, E, "Không thành công", "Scope đang có audit", "High", "Kiểm tra sửa scope khi đang có audit",
          "1. Mở chi tiết scope đang có audit\n2. Bấm nút Edit ở khối Overview",
          "- Không mở hộp thoại Edit scope\n- Hiện thông báo:\n\"The scope can't be edited while an audit is running.\"", "UC-SCP-004",
          OQ="Quy tắc và text lấy từ prototype, UC không ghi → Q-S-16",
          Pre=PRE + "; scope đang có audit chạy trên một framework"),
        R(87, E, "Thành công", "Đổi Name — tiêu đề chi tiết", "High", "Kiểm tra tên mới ở màn chi tiết sau khi sửa",
          ED + "\n3. Đổi Name thành: abc1\n4. Bấm Save",
          "- Hộp thoại đóng\n- Tiêu đề trang đổi thành abc1", "UC-SCP-004", note="ô Step tô vàng ở v1.4"),
        R(88, E, "Thành công", "Đổi Name — danh sách", "High", "Kiểm tra tên mới ở màn danh sách",
          ED + "\n3. Đổi Name thành: abc1\n4. Bấm Save\n5. Bấm nút ← để về màn Scopes\n6. Kiểm tra dòng của scope vừa sửa",
          "- Cột Scope hiển thị tên mới: abc1", "UC-SCP-004",
          note="ô Step tô vàng ở v1.4; thao tác đổi tên đưa từ Pre-condition vào Step để case tự chạy được"),
        R(91, E, "Thành công", "Sửa In scope, Out of scope", "Medium", "Kiểm tra sửa In scope và Out of scope",
          ED + "\n3. Sửa\n- What is in scope: abc1\n- What is out of scope (optional): xoá trống\n4. Bấm Save",
          "- Hộp thoại đóng\n- Khối Overview:\n+ In scope: abc1\n+ Out of scope: —", "UC-SCP-004"),
    ]
    # ---------------------------------------------------------------- Khối Frameworks
    F = "Khối Frameworks - Frameworks"
    FW = "1. Mở chi tiết scope đã gắn framework"
    Q11 = ("[ĐỀ XUẤT LÙI] RDN-004. Cách tính và làm tròn lấy theo cột Evidence coverage ở danh sách; "
           "prototype hiện <%> + thanh tiến trình + <đã có>/<tổng> → Q-S-11")

    def cov(name, frac, exp, pri, src=None, note=""):
        return R(src, F, "Hiển thị", "Cột Coverage", pri, name,
                 "1. Mở chi tiết scope\n2. Tạo Frameworks với:\n- Framework A: %s\n3. Kiểm tra cột Coverage của Framework A" % frac,
                 "- Hiển thị Coverage = " + exp, "UC-RDN-004", OQ=Q11, note=note)

    out += [
        R(None, F, "Trạng thái rỗng", "Chưa gắn framework", "Medium", "Kiểm tra khối Frameworks khi scope chưa gắn framework",
          "1. Mở chi tiết scope chưa gắn framework\n2. Kiểm tra khối số 2 Frameworks", "", "UC-SCP-002",
          OQ="Khối Frameworks khi chưa gắn framework hiển thị gì → Q-S-13",
          note="câu Q-S-13 trước nằm nhờ ở case tạo scope (dòng 38 của v1.4); đưa về đúng khối"),
        R(94, F, "Hiển thị", "Tiêu đề khối và cột", "High", "Kiểm tra khối Frameworks",
          FW + "\n2. Kiểm tra khối số 2 Frameworks",
          "- Tiêu đề: Frameworks\n- Mô tả: Each framework gets its own workspace\n- Có nút gắn framework\n"
          "- Bảng 4 cột theo thứ tự:\n+ Framework · version\n+ Tier\n+ Coverage\n+ Status", "UC-SCP-002",
          OQ="Nhãn nút: Figma 'Link framework', prototype '+ Link framework' → Q-S-03"),
        R(95, F, "Hiển thị", "Cột Framework · version", "Medium", "Kiểm tra cột Framework · version",
          FW + "\n2. Kiểm tra cột đầu của bảng ở khối Frameworks",
          "- Mỗi dòng dạng <tên framework> · <phiên bản>, ví dụ ISO/IEC 27001 · 2022\n- Tên framework dạng liên kết", "UC-SCP-002"),
        R(96, F, "Hiển thị", "Cột Tier", "High", "Kiểm tra cột Tier của framework có tier",
          "1. Mở chi tiết scope đã gắn framework có tier\n2. Kiểm tra cột Tier của framework đó",
          "- Hiển thị tier hiện tại của framework", "UC-SCP-002",
          OQ="Prototype ghi 'Medium · 中' ở đây nhưng 'Medium' ở danh sách và Summary; tier có phải 'obligation level' của SCP-002 → Q-S-17",
          note="tách từ case Cột Tier của v1.4: mỗi loại framework một case"),
        R(None, F, "Hiển thị", "Cột Tier", "Medium", "Kiểm tra cột Tier của framework không phân tier",
          "1. Mở chi tiết scope đã gắn framework không phân tier\n2. Kiểm tra cột Tier của framework đó",
          "- Hiển thị: No tiers", "UC-SCP-002",
          note="tách từ case Cột Tier của v1.4 (dòng 96): mỗi loại framework một case"),
        cov("Kiểm tra cột Coverage khi kết quả phải làm tròn lên", "74/116", "74/116 × 100 = 63.79% → 64%", "High", src=97,
            note="thay case Cột Coverage để trống Expected của v1.4 bằng các case có số cụ thể"),
        cov("Kiểm tra cột Coverage khi kết quả phải làm tròn xuống", "6/31", "6/31 × 100 = 19.35% → 19%", "Medium",
            note="thêm theo góp ý 07/10: giá trị tính toán cần nhiều case"),
        cov("Kiểm tra cột Coverage khi chưa requirement nào đủ evidence", "0/78", "0/78 × 100 = 0%", "Medium",
            note="thêm theo góp ý 07/10: giá trị tính toán cần nhiều case"),
        cov("Kiểm tra cột Coverage khi mọi requirement đều đủ evidence", "61/61", "61/61 × 100 = 100%", "Medium",
            note="thêm theo góp ý 07/10: giá trị tính toán cần nhiều case"),
        R(98, F, "Hiển thị", "Cột Status", "Medium", "Kiểm tra cột Status",
          FW + "\n2. Kiểm tra cột Status",
          "- Mỗi framework có nhãn trạng thái của workspace, ví dụ Preparing, Audit in progress", "UC-SCP-002",
          OQ="Danh sách trạng thái đầy đủ → Q-S-20"),
        R(99, F, "Hiển thị", "Nút Change tier", "Medium", "Kiểm tra nút Change tier trên từng dòng",
          "1. Mở chi tiết scope đã gắn framework có tier và framework không phân tier\n2. Kiểm tra cuối mỗi dòng của bảng ở khối Frameworks",
          "- Dòng framework có tier có nút Change tier\n- Dòng framework không phân tier không có nút này", "UC-SCP-002"),
        R(100, F, "Liên kết", "Bấm tên framework", "High", "Kiểm tra mở workspace từ tên framework",
          FW + "\n2. Bấm tên một framework trong bảng ở khối Frameworks",
          "- Chuyển sang màn workspace của framework đó trong scope đang xem", "UC-SCP-002"),
    ]
    # ---------------------------------------------------------------- Gắn framework
    L = "Gắn framework - Link framework"
    LD = OPEN + "\n2. Mở hộp thoại Link a framework"
    out += [
        R(101, L, "Mở hộp thoại", "Bấm nút gắn framework", "High", "Kiểm tra mở hộp thoại gắn framework",
          OPEN + "\n2. Bấm nút gắn framework ở khối Frameworks",
          "- Mở hộp thoại Link a framework, có nút đóng ×\n- Trường Framework *, placeholder: Choose a framework\n- Ghi chú:\n"
          "\"A workspace is created for this scope with the requirements of the chosen tier. You can change the tier later; "
          "uploaded evidence stays.\"\n- Có nút Cancel và nút Link and create workspace", "UC-SCP-006"),
        R(102, L, "Danh sách framework", "Các lựa chọn", "High", "Kiểm tra danh sách framework",
          LD + "\n3. Mở danh sách Framework",
          "- Mỗi lựa chọn có tên framework và dòng phụ ghi tổ chức ban hành, kèm các tier nếu có, ví dụ MODA · tiers Basic / Medium / High",
          "UC-SCP-006"),
        R(103, L, "Danh sách framework", "Framework đã gắn", "High", "Kiểm tra framework đã gắn vào scope có trong danh sách không",
          "1. Mở chi tiết scope đã gắn [Framework]\n2. Mở hộp thoại Link a framework\n3. Mở danh sách Framework\n4. Tìm [Framework]",
          "", "UC-SCP-006", OQ="Prototype vẫn liệt kê và cho chọn → ẩn, khoá hay cho gắn lần hai → Q-S-19"),
        R(104, L, "Chọn framework", "Framework có tier", "High", "Kiểm tra chọn framework có phân tier",
          LD + "\n3. Chọn một framework có tier",
          "- Hiện trường Version * đã có sẵn giá trị, ghi chú: Only active versions are listed.\n"
          "- Hiện mục Protection tier of this organization * gồm 3 lựa chọn, mỗi lựa chọn có tên tier, mô tả, số requirement\n"
          "- Chưa chọn sẵn tier nào", "UC-SCP-006", OQ="Số requirement tier High: Figma 79, prototype 76 → Q-S-18"),
        R(105, L, "Chọn framework", "Framework không tier", "Medium", "Kiểm tra chọn framework không phân tier",
          LD + "\n3. Chọn một framework không phân tier", "", "UC-SCP-006",
          OQ="Phần chọn tier ẩn đi hay hiện No tiers → Q-S-17"),
        R(106, L, "Không thành công", "Chưa chọn framework", "High", "Kiểm tra bấm gắn khi chưa chọn framework",
          LD + "\n3. Bấm Link and create workspace", "- Không gắn, hộp thoại vẫn mở", "UC-SCP-006",
          OQ="Hiện lỗi hay khoá nút khi chưa chọn; text lỗi → Q-S-05", note="từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công"),
        R(107, L, "Không thành công", "Chưa chọn tier", "High", "Kiểm tra bấm gắn khi chưa chọn tier",
          LD + ", chọn một framework có tier\n3. Không chọn tier\n4. Bấm Link and create workspace",
          "- Không gắn, hộp thoại vẫn mở", "UC-SCP-006",
          OQ="Hiện lỗi hay khoá nút; text lỗi → Q-S-05", note="từ nhóm Kiểm tra dữ liệu chuyển sang Không thành công"),
        R(112, L, "Không thành công", "Bấm Cancel", "Medium", "Kiểm tra huỷ gắn framework",
          LD + ", chọn một framework\n3. Bấm Cancel",
          "- Hộp thoại đóng\n- Bảng Frameworks không có dòng mới", "UC-SCP-006"),
        R(113, L, "Không thành công", "Scope đang có audit", "Medium", "Kiểm tra gắn thêm framework khi scope đang có audit",
          "1. Mở chi tiết scope đang có audit\n2. Bấm nút gắn framework", "", "UC-SCP-006",
          OQ="Text khoá chỉ nói sửa scope và gỡ framework bị chặn; gắn thêm có bị chặn → Q-S-16",
          Pre=PRE + "; scope đang có audit chạy trên một framework", note="ô Step tô vàng ở v1.4"),
        R(108, L, "Thành công", "Framework có tier", "High", "Kiểm tra gắn framework có tier",
          LD + "\n3. Chọn\n- Framework: [Framework] có tier\n- Protection tier of this organization: Medium\n4. Bấm Link and create workspace",
          "- Hộp thoại đóng\n- Bảng Frameworks có thêm dòng [Framework] · <phiên bản>\n- Cột Tier của dòng đó là tier đã chọn",
          "UC-SCP-006", OQ="Trạng thái ban đầu của workspace → Q-S-20",
          note="tên case cũ: Hiện ở khối Frameworks; nhóm Thành công đặt theo loại framework"),
        R(None, L, "Thành công", "Framework không phân tier", "Medium", "Kiểm tra gắn framework không phân tier",
          LD + "\n3. Chọn Framework: [Framework] không phân tier\n4. Bấm Link and create workspace",
          "- Hộp thoại đóng\n- Bảng Frameworks có thêm dòng [Framework] · <phiên bản>\n- Cột Tier của dòng đó: No tiers",
          "UC-SCP-006", OQ="Phần chọn tier ẩn đi hay hiện No tiers → Q-S-17; trạng thái ban đầu của workspace → Q-S-20",
          note="thêm: mỗi loại framework một case Thành công, như 3 case theo Type ở Tạo scope"),
        R(110, L, "Thành công", "Hiện ở màn Workspaces", "High", "Kiểm tra workspace mới hiện ở màn Workspaces",
          "1. Mở màn Workspaces\n2. Tìm workspace của [Organization]",
          "- Có workspace của [Organization] với [Framework] vừa gắn", "UC-EVD-003",
          OQ="Workspace tạo ngay hay sau một khoảng → Q-S-20",
          Pre=PRE + "; trên Scopes đã gắn [Framework] vào scope [Organization]",
          note="hệ quả ở màn khác, giữ ở sheet của hành động theo rule 27"),
    ]
    # ---------------------------------------------------------------- Gỡ framework
    out += [
        R(114, "Gỡ framework - Unlink framework", "Lối vào", "Tìm chức năng gỡ", "High", "Kiểm tra lối vào gỡ framework khỏi scope",
          FW + "\n2. Tìm chức năng gỡ framework ở khối Frameworks và menu ⋮", "", "UC-SCP-007",
          OQ="Không có lối vào ở Figma lẫn prototype dù SCP-007 có 8 giờ → Q-S-21"),
    ]
    # ---------------------------------------------------------------- Đổi tier
    C = "Đổi tier - Change tier"
    NU = "[NGOÀI UC]"
    T_OPEN = "1. Mở chi tiết scope đã gắn framework có tier, không có audit"
    T_LOCK = "1. Mở chi tiết scope đang có audit"
    P_LOCK = PRE + "; audit [Mã audit] đang chạy trên framework có tier của scope"
    out += [
        R(115, C, "Mở hộp thoại", "Không có audit", "High", "Kiểm tra hộp thoại đổi tier",
          T_OPEN + "\n2. Bấm Change tier ở dòng framework đó",
          "- Mở hộp thoại Change tier\n- Dòng mô tả ghi framework, phiên bản và tier hiện tại\n"
          "- 3 lựa chọn tier kèm số requirement, tier hiện tại được đánh dấu\n- Có nút Cancel và nút xác nhận", NU,
          OQ="Theo Figma, prototype chưa có dữ liệu để mở; đổi tier thuộc UC nào → Q-S-17", note="ô Step tô vàng ở v1.4"),
        R(116, C, "Mở hộp thoại", "Đang có audit", "High", "Kiểm tra hộp thoại đổi tier khi đang có audit",
          T_LOCK + "\n2. Bấm Change tier ở dòng framework đang có audit",
          "- Dòng mô tả: [Tên scope] · [Framework] · <phiên bản> · <tier>\n- Khung cảnh báo: Tier can't be changed during an audit\n"
          "- Nội dung:\n\"Audit [Mã audit] is reviewing this workspace against tier <tier> (<n> requirements). You can change the tier "
          "after the review closes. Unlinking the framework and editing the scope are blocked for the same reason.\"\n"
          "- Có nút Close\n- Nút Change tier bị khoá", NU,
          OQ="Text lấy từ prototype, chưa đối chiếu frame Change tier locked → Q-S-16", Pre=P_LOCK, note="ô Step tô vàng ở v1.4"),
        R(119, C, "Không thành công", "Bấm Cancel", "Medium", "Kiểm tra huỷ đổi tier",
          T_OPEN + "\n2. Mở Change tier\n3. Chọn tier khác\n4. Bấm Cancel",
          "- Hộp thoại đóng, cột Tier giữ nguyên", NU, OQ="Đổi tier thuộc UC nào → Q-S-17", note="ô Step tô vàng ở v1.4"),
        R(120, C, "Không thành công", "Đóng hộp thoại khoá", "Low", "Kiểm tra đóng hộp thoại khoá bằng Close",
          T_LOCK + "\n2. Mở Change tier của framework đang có audit\n3. Bấm Close",
          "- Hộp thoại đóng, cột Tier giữ nguyên", NU, OQ="Đổi tier thuộc UC nào → Q-S-17", Pre=P_LOCK, note="ô Step tô vàng ở v1.4"),
        R(117, C, "Thành công", "Nâng tier", "High", "Kiểm tra nâng tier",
          T_OPEN + "\n2. Mở Change tier của framework đang ở Medium\n3. Chọn High\n4. Kiểm tra khung cảnh báo\n5. Bấm Change to High",
          "- Sau bước 3: có cảnh báo số requirement tăng và độ phủ sẽ giảm\n- Sau bước 5: hộp thoại đóng, cột Tier đổi thành High", NU,
          OQ="Bằng chứng đã tải có giữ nguyên → Q-S-22",
          note="ô Step tô vàng ở v1.4; Expected đang ghi Sau bước 2, Sau bước 4 trong khi thao tác ở bước 3, bước 5"),
        R(118, C, "Thành công", "Hạ tier", "Medium", "Kiểm tra hạ tier",
          T_OPEN + "\n2. Mở Change tier của framework đang ở High\n3. Chọn Medium\n4. Bấm nút xác nhận", "", NU,
          OQ="Hạ tier có cảnh báo gì; bằng chứng của requirement bị bỏ ra sao → Q-S-22", note="ô Step tô vàng ở v1.4"),
    ]
    # ---------------------------------------------------------------- Khối Users
    U = "Khối Users - Users"
    out += [
        R(121, U, "Hiển thị", "Tiêu đề khối và cột", "High", "Kiểm tra khối Users",
          OPEN + "\n2. Kiểm tra khối số 3 Users",
          "- Tiêu đề: Users\n- Mô tả: Can work in every workspace of this scope\n- Có nút Assign users\n"
          "- Bảng 3 cột theo thứ tự:\n+ User\n+ Role\n+ Given", "UC-USR-006",
          note="dòng cuối của Expected đang là \"- F106\" (hỏng từ bản v1.3); đặt lại 3 cột User, Role, Given"),
        R(122, U, "Hiển thị", "Dòng Customer Admin", "Medium", "Kiểm tra dòng của Customer Admin",
          OPEN + "\n2. Kiểm tra dòng của Customer Admin ở khối Users",
          "- Role: Customer Admin · sees every scope\n- Given: —", "UC-USR-006"),
        R(123, U, "Hiển thị", "Dòng người được gán", "Medium", "Kiểm tra dòng của người được gán",
          "1. Mở chi tiết scope đã gán [Customer User]\n2. Kiểm tra dòng của [Customer User] ở khối Users",
          "- Role: Customer User\n- Given: ngày được gán, dạng DD Mon YYYY, ví dụ 21 Sep 2026", "UC-USR-006"),
    ]
    # ---------------------------------------------------------------- Gán người dùng
    A = "Gán người dùng - Assign users"
    AD = OPEN + "\n2. Mở Assign users"
    out += [
        R(124, A, "Mở hộp thoại", "Bấm Assign users", "High", "Kiểm tra mở hộp thoại Assign users",
          OPEN + "\n2. Bấm nút Assign users",
          "- Mở hộp thoại Assign users, có nút đóng ×\n- Mô tả:\n\"Users you tick can work in every workspace of [Tên scope]. "
          "Customer Admins always have access.\"\n- Mỗi người một dòng gồm:\n+ Ô tick\n+ Tên\n+ Email\n"
          "- Người chưa kích hoạt có thêm: · invitation pending\n- Người đang được gán đã tick sẵn\n"
          "- Không có Customer Admin trong danh sách\n- Có nút Cancel và nút Save", "UC-USR-006"),
        R(125, A, "Mở hộp thoại", "Vai trò trong danh sách", "High", "Kiểm tra những vai trò có trong danh sách gán",
          AD + "\n3. Đối chiếu vai trò của từng người trong danh sách", "", "UC-USR-006",
          OQ="USR-006 chỉ nói Customer User; prototype có cả Customer Viewer và người chưa kích hoạt → Q-S-23"),
        R(132, A, "Không thành công", "Bấm Cancel", "Medium", "Kiểm tra huỷ gán người dùng",
          AD + ", tick thêm một người\n3. Bấm Cancel", "- Hộp thoại đóng, khối Users không đổi", "UC-USR-006"),
        R(126, A, "Thành công", "Tick thêm — khối Users", "High", "Kiểm tra người vừa gán hiện ở khối Users",
          AD + "\n3. Tick [Customer User] chưa được gán\n4. Bấm Save",
          "- Hộp thoại đóng\n- Khối Users có thêm dòng:\n+ User: [Customer User]\n+ Role: Customer User\n+ Given: ngày hôm nay",
          "UC-USR-006", note="ô tô vàng ở v1.4"),
        R(128, A, "Thành công", "Tick thêm — người được gán thấy scope", "High", "Kiểm tra người vừa được gán thấy scope",
          "1. Mở chi tiết scope [Organization], gán [Customer User] (Assign users, tick, Save)\n"
          "2. Đăng xuất, đăng nhập account [Customer User]\n3. Mở màn Scopes",
          "- Danh sách có [Organization]", "UC-USR-006", note="ô tô vàng ở v1.4; Expected đang cụt (\"- Danh sách có\")"),
        R(129, A, "Thành công", "Tick thêm — chi tiết người dùng", "Medium", "Kiểm tra scope hiện ở chi tiết người dùng",
          "1. Mở chi tiết scope [Organization], gán [Customer User] (Assign users, tick, Save)\n"
          "2. Mở Users ở mục Administration\n3. Mở chi tiết [Customer User]",
          "- Phần scope được gán có [Organization]", "UC-USR-002",
          note="ô tô vàng ở v1.4; Expected đang cụt; hệ quả ở màn khác, giữ ở sheet của hành động theo rule 27"),
        R(130, A, "Thành công", "Bỏ tick — khối Users", "High", "Kiểm tra bỏ gán người dùng",
          "1. Mở chi tiết scope đã gán [Customer User]\n2. Mở Assign users\n3. Bỏ tick [Customer User]\n4. Bấm Save",
          "- Hộp thoại đóng\n- Khối Users không còn dòng [Customer User]", "UC-USR-006",
          OQ="Thu hồi có thuộc USR-006, có hỏi xác nhận → Q-S-23", note="ô Step tô vàng ở v1.4"),
        R(131, A, "Thành công", "Bỏ tick — người bị bỏ gán", "High", "Kiểm tra người bị bỏ gán không còn thấy scope",
          "1. Mở chi tiết scope [Organization], bỏ gán [Customer User] (Assign users, bỏ tick, Save)\n"
          "2. Đăng xuất, đăng nhập account [Customer User]\n3. Mở màn Scopes\n4. Mở url chi tiết của [Organization]",
          "- Sau bước 3: danh sách không có [Organization]\n- Sau bước 4: không hiển thị nội dung của [Organization]", "UC-USR-006",
          OQ="Thu hồi có thuộc USR-006 → Q-S-23", note="ô tô vàng ở v1.4; Expected đang cụt"),
    ]
    # ---------------------------------------------------------------- Tổng hợp
    out += [
        R(133, "Tổng hợp - Summary", "Hiển thị", "Evidence coverage", "Medium", "Kiểm tra khối Summary",
          FW + "\n2. Kiểm tra khối Summary bên phải", "", "UC-RDN-004",
          OQ="[ĐỀ XUẤT LÙI] RDN-004. Prototype: mỗi framework một dòng %, thanh tiến trình, '<n> of <m> requirements have their "
             "mandatory evidence'; ghi chú 'Preparation progress only — not a compliance decision.' → Q-S-11"),
    ]
    # ---------------------------------------------------------------- Phân quyền
    CU = "Đăng nhập account Customer User; được gán scope [System], không được gán scope [Organization]"
    SG = "Vai trò SGS - SGS roles"
    out += [
        R(134, "Customer User", "Danh sách", "Chỉ scope được gán", "High", "Kiểm tra màn Scopes với Customer User",
          "1. Mở màn Scopes", "- Danh sách có [System]\n- Danh sách không có [Organization]\n- Không có nút tạo scope",
          "UC-SCP-001", Pre=CU, I=I_PERM, note="ô Pre-condition tô vàng ở v1.4"),
        R(135, "Customer User", "Danh sách", "Mô tả trang", "Low", "Kiểm tra mô tả trang với Customer User",
          "1. Mở màn Scopes\n2. Kiểm tra dòng mô tả dưới tiêu đề",
          "- Mô tả:\n\"Scopes assigned to you. Only scopes assigned to you are listed.\"", "UC-SCP-001",
          OQ="Text lấy từ prototype, Figma chỉ có bản Customer Admin → Q-S-01", Pre=CU, I=I_PERM, note="ô Pre-condition tô vàng ở v1.4"),
        R(136, "Customer User", "Chi tiết", "Không có thao tác ghi", "High", "Kiểm tra màn chi tiết với Customer User",
          "1. Mở màn Scopes\n2. Bấm tên [System] để mở chi tiết",
          "- Không có:\n+ Nút Edit ở khối Overview\n+ Mục Edit scope\n+ Nút gắn framework\n+ Nút Change tier\n+ Nút Assign users",
          "UC-SCP-002", Pre=CU, I=I_PERM, note="ô tô vàng ở v1.4"),
        R(137, "Customer User", "Chi tiết", "Scope không được gán, mở bằng URL", "High",
          "Kiểm tra Customer User mở scope không được gán bằng URL",
          "1. Mở url chi tiết của [Organization]", "- Không hiển thị nội dung của [Organization]", "UC-ROL-001",
          OQ="Hiện trang gì → Q-S-26", Pre=CU, I=I_PERM, note="ô tô vàng ở v1.4; Expected đang cụt"),
        R(140, "Customer Viewer", "Danh sách và chi tiết", "Quyền xem", "High", "Kiểm tra màn Scopes với Customer Viewer",
          "1. Mở màn Scopes\n2. Mở chi tiết một scope", "", "UC-ROL-001",
          OQ="SCP-001/002 không có Customer Viewer trong actor, nhưng prototype gán được Viewer vào scope → Q-S-24",
          Pre="Đăng nhập account Customer Viewer", I=I_PERM, note="ô Pre-condition tô vàng ở v1.4"),
        R(141, SG, "Được phân công", "Chỉ đọc", "High", "Kiểm tra SGS Consultant xem scope của khách được phân công",
          "1. Mở danh sách scope của [Tên Organization]\n2. Mở chi tiết một scope",
          "- Xem được danh sách và chi tiết scope\n- Không có:\n+ Nút tạo scope\n+ Nút Edit\n+ Nút gắn framework\n"
          "+ Nút Change tier\n+ Nút Assign users", "UC-SCP-002",
          OQ="Lối vào từ SGS Portal ở đâu → Q-S-25",
          Pre="Đăng nhập account SGS Consultant ở SGS Portal; đã được phân công khách hàng [Tên Organization]", I=I_PERM,
          note="ô Pre-condition tô vàng ở v1.4"),
        R(142, SG, "Không được phân công", "Không thấy scope", "High",
          "Kiểm tra người dùng SGS không được phân công không thấy scope của khách hàng",
          "1. Tìm scope của [Tên Organization] trên SGS Portal", "- Không thấy scope của [Tên Organization]", "UC-ROL-001",
          OQ="Lối vào từ SGS Portal ở đâu → Q-S-25",
          Pre="Đăng nhập account SGS ở SGS Portal; không được phân công khách hàng [Tên Organization]", I=I_PERM,
          note="ô Pre-condition tô vàng ở v1.4; bỏ bước gọi API (Tester không được gọi API)"),
    ]
    # ---------------------------------------------------------------- Bảo mật
    TB = "Đăng nhập account Customer Admin của tenant B; tenant A là tenant khác, đã có scope"
    TI = "Cách ly tenant - Tenant isolation"
    out += [
        R(143, TI, "Danh sách", "Scope của tenant khác", "High", "Kiểm tra cách ly danh sách scope giữa hai tenant",
          "1. Mở màn Scopes", "- Chỉ thấy scope của tenant B\n- Không có scope nào của tenant A", "UC-ROL-001",
          Pre=TB, I=I_SEC, note="ô Pre-condition tô vàng ở v1.4"),
        R(144, TI, "URL", "Chi tiết scope tenant khác", "High", "Kiểm tra mở chi tiết scope của tenant khác bằng URL",
          "1. Mở url chi tiết của một scope thuộc tenant A", "- Không hiển thị dữ liệu của tenant A", "UC-ROL-001",
          OQ="Hiện trang gì → Q-S-26", Pre=TB, I=I_SEC, note="ô tô vàng ở v1.4"),
        R(147, "Dữ liệu nhập - Input", "Mã độc", "Name chứa thẻ script", "High", "Kiểm tra tạo scope có Name chứa mã độc",
          "1. Mở màn Scopes\n2. Bấm nút tạo scope để mở hộp thoại Create scope\n3. Chọn Type: Organization\n4. Nhập\n"
          "- Name: <script>alert(1)</script>\n- What is in scope: abc\n5. Bấm Create scope\n6. Xem scope đó ở danh sách và màn chi tiết",
          "- Name hiển thị nguyên chuỗi <script>alert(1)</script> dưới dạng chữ\n- Không có hộp thoại hay đoạn mã nào được chạy",
          "UC-SCP-003", I=I_SEC),
        R(148, "Ghi vết - Audit log", "Thao tác ghi", "Tạo, sửa, gắn, gán", "Medium", "Kiểm tra ghi audit cho các thao tác trên scope",
          "1. Mở màn Scopes\n2. Tạo scope, sửa scope, gắn framework, gán người dùng\n3. Mở Audit Logs", "", "UC-AUD-001",
          OQ="Thao tác trên scope có thuộc diện phải ghi audit → Q-S-27", I=I_SEC),
    ]
    return out


# dòng của v1.4 không còn ở v1.5: (dòng, lý do)
REMOVED = [
    (89, "Hệ quả suy ra (tên mới ở Overview của scope con), không có căn cứ trực tiếp ở UC hay Figma; nơi hiển thị này đã có khu vực "
         "Tổng quan ▸ Scope System (FB-042, FB-044)"),
    (90, "Hệ quả suy ra (tên mới ở cột Belongs to của danh sách); nơi hiển thị này đã có khu vực Bảng danh sách ▸ Cột Belongs to "
         "(FB-042, FB-044)"),
    (109, "Nơi hiển thị đã có case riêng: Bảng danh sách ▸ Cột Frameworks — đã gắn (FB-044)"),
    (111, "Nơi hiển thị đã có case riêng: Tổng hợp ▸ Evidence coverage; case này để trống Expected (FB-044)"),
    (127, "Nơi hiển thị đã có case riêng: Bảng danh sách ▸ Cột Users, so số ở cột với số dòng ở khối Users (FB-044)"),
    (138, "Case gọi API: profile.md ghi Tester không được gọi API, không viết ở sheet màn hình (FB-039, rule 29)"),
    (139, "Case gọi API (FB-039, rule 29)"),
    (145, "Case gọi API (FB-039, rule 29)"),
    (146, "Case gọi API; trên giao diện không có thao tác gán người của tenant khác (FB-039, rule 29)"),
]


def build(v14_rows):
    old = {r["row"]: r for r in v14_rows}
    rows, touched = [], []
    for rn in range(13, 70):
        o = old[rn]
        rec = {k: o[k] for k in FIELDS}
        rec.update(src=rn, note="")
        notes = []
        for field, val, why in TOUCH.get(rn, []):
            new = val(rec[field]) if callable(val) else val
            if clean(new) == clean(rec[field]):
                raise SystemExit("TOUCH dòng %d trường %s không đổi gì — kiểm lại chuỗi tìm" % (rn, field))
            rec[field] = new
            notes.append("%s: %s" % (field, why))
        if rn in UC_FILL:
            if clean(o["UC"]):
                raise SystemExit("UC_FILL dòng %d: ô UC đã có giá trị %r" % (rn, o["UC"]))
            rec["UC"] = UC_FILL[rn]
            notes.append("UC: ô trống, điền theo case cùng nhóm")
        rec["note"] = "; ".join(notes)
        rows.append(rec)
        if rn == 61:
            for e in EC_NEW:
                rows.append(dict(e, src=None))
    b = part_b(old)
    rows += b
    out = []
    for i, r in enumerate(rows, 1):
        rec = {k: clean(r[k]) for k in FIELDS}
        o = old.get(r["src"]) if r["src"] else None
        rec.update(no=i, id="Scope_%03d" % i, src=r["src"], old_id=(o["ID"] if o else ""), old_no=(o["No"] if o else ""),
                   note=r.get("note", ""))
        if o is None:
            rec["chg"], rec["diff"] = "thêm", []
        else:
            diff = [k for k in FIELDS if clean(o[k]) != rec[k]]
            rec["chg"], rec["diff"] = ("giữ" if not diff else "sửa"), diff
        out.append(rec)
    used = {r["src"] for r in out if r["src"]}
    gone = [rn for rn in sorted(old) if rn not in used]
    listed = [rn for rn, _ in REMOVED]
    if gone != sorted(listed):
        raise SystemExit("Dòng v1.4 không còn ở v1.5 %s khác danh sách REMOVED %s" % (gone, sorted(listed)))
    dup = [s for s in used if sum(1 for r in out if r["src"] == s) > 1]
    if dup:
        raise SystemExit("Dòng v1.4 dùng hai lần: %s" % dup)
    removed = [dict(row=rn, id=old[rn]["ID"], no=old[rn]["No"], name=clean(old[rn]["Name"]), II=old[rn]["II"], III=old[rn]["III"],
                    IV=old[rn]["IV"], why=why) for rn, why in REMOVED]
    return out, removed


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    rows, removed = build(json.load(open(src, encoding="utf-8")))
    json.dump({"rows": rows, "removed": removed}, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(rows), "dòng ·", dict(Counter(r["chg"] for r in rows)), "· bỏ", len(removed))
