# -*- coding: utf-8 -*-
import unicodedata
ADMIN="Đăng nhập account Customer Admin"
CU="Đăng nhập account Customer User"
CV="Đăng nhập account Customer Viewer"
OPEN="1. Mở chi tiết [Workspace] (màn Workspaces, bấm tên workspace)"
WS="[Workspace] Appendix 10 · 2022 · Medium của scope [System], chế độ Assisted"
EMPTY=WS+", chưa có evidence nào"
C=[]
def case(I,II,III,IV,pri,name,step,exp,uc="UC-EVA-01",q="",pre=ADMIN):
    C.append(dict(I=I,II=II,III=III,IV=IV,Pri=pri,Name=name,Pre=pre,Step=step,Expected=exp,UC=uc,Wait=q))

# ---------------- Câu hỏi (mỗi câu một mã, đúng một lần) ----------------
Q={}
Q[1]="Để có workspace 38 trên 61 requirement đủ evidence thì phải tạo 38 requirement có evidence: có dữ liệu dựng sẵn hoặc cách dựng nhanh không? (Figma Workspace / Requirement ghi 38 of 61 · 62%; hệ thống mới chỉ có 0 of 61 và 6 of 31)"
Q[2]="Nhãn vàng “No design yet” cạnh ô Owner là gì và khi nào hiện? (chỉ có ở hệ thống, requirement nào cũng có; UC và Figma không nêu)"
Q[3]="Requirement ở trạng thái Partial khi nào? (UC EVA-07 chỉ ghi Provided, Missing, Out of scope; Figma có chip Partial ở nhóm Access Control 58%)"
Q[4]="Requirement ngoài tier hoặc đã retired có hiện trong cây với trạng thái Out of scope không, hay bị ẩn? (UC WSP-06 ghi “not counted”, UC EVA-07 có trạng thái Out of scope; hệ thống ở workspace Medium chỉ hiện 61 requirement, không có chip Out of scope)"
Q[5]="“Clarification requested” hiện ở đâu (chip trạng thái, bộ lọc) và khi nào xuất hiện? (UC EVA-01, EVA-02 và D41: làm rõ qua Gap Analysis; Figma không có; bộ lọc hệ thống chỉ có All, Missing, Partial, Provided)"
Q[6]="Khi có cả bộ lọc trạng thái và từ khoá tìm kiếm thì hai điều kiện áp cùng lúc đúng không? (UC EVA-01 chỉ ghi “search and filter”)"
Q[7]="Khi bộ lọc trạng thái không có requirement nào khớp thì hiện thông báo gì? (hệ thống chỉ có thông báo cho trường hợp tìm kiếm: “No matching requirements” / “Try another search or filter”; Figma không có trạng thái này)"
Q[8]="Nhãn “from <tier>” hiện thế nào với requirement thêm ở Medium hoặc High? (Figma, hệ thống chỉ có “from Basic”)"
Q[9]="Requirement có nhiều expected evidence thì thẻ nào nhận file khi bấm Upload evidence hoặc Link existing evidence, dòng đếm ghi thế nào, và có expected evidence không bắt buộc (Optional) không? (Figma, hệ thống chỉ có requirement một expected evidence “Mandatory”; hộp thoại Upload ghi “For <requirement> · <EE>”)"
Q[10]="Câu “No evidence yet. Upload a file or link one that is already in this workspace.” có đúng văn bản chính thức không? (chỉ lấy từ hệ thống; Figma chưa có thẻ expected evidence trống)"
Q[11]="Dòng evidence ở màn requirement có hiện nhãn version (v1, v2, v3) như D21 không? (UC D21: “requirements show only the current version of each document with a version label”; Figma chỉ có tên file access-control-policy-v3.pdf, không có nhãn)"
Q[12]="Định dạng ngày ở dòng evidence là “Uploaded Sep 12, 2026” hay “12 Sep 2026”? (Figma dòng evidence ghi “Sep 12, 2026”, Figma chi tiết evidence và hộp thoại Upload ghi “12 Sep 2026”)"
Q[13]="Evidence không có ngày hết hạn thì dòng evidence hiện thế nào (bỏ “valid until” hay ghi “no expiry”)? (Figma chỉ có evidence có “valid until Sep 2027”; hộp thoại Upload ghi “Leave empty if it doesn't expire.”)"
Q[14]="Evidence quá ngày Valid until thì requirement còn Provided không, và dòng evidence có chip Expired không? (UC D7: hết hạn chỉ hiện dạng ngày, không phải trạng thái; Figma Documents lại có chip Expired và Expires soon)"
Q[15]="Requirement có yêu cầu làm rõ đang mở (Gap Analysis) thì hiện ở khu vực nào của chi tiết requirement? (UC EVA-02: “open clarifications (GAP-03)”; Figma, hệ thống không có)"
Q[16]="Valid from có điền sẵn ngày hôm nay không? (Figma hộp thoại Upload điền sẵn Valid from “20 Sep 2026”, hệ thống để trống; UC không nêu)"
Q[17]="Ô Name điền sẵn từ tên file thế nào (bỏ đuôi file, thay dấu gạch bằng khoảng trắng hay giữ nguyên)? (UC EVA-03: “titles from file names”; Figma ô Name ghi “AD inactive account policy – screenshot” cho file ad-inactive-accounts.png)"
Q[18]="Hộp thoại Upload chọn nhiều file thì hiện thế nào (mỗi file một dòng với ô Name riêng hay chung)? (UC EVA-03 và D21: nhiều file một lần, title từ tên file, metadata dùng chung; Figma chỉ có một dòng file và một ô Name)"
Q[19]="Câu báo lỗi khi bỏ trống File và Name có đúng văn bản chính thức không? (hệ thống: “Choose a file.” và “Enter a name.”; UC D8 chỉ ghi không lưu được khi thiếu; Figma không có trạng thái lỗi)"
Q[20]="Name có giới hạn độ dài không? (UC D8 chỉ ghi Name bắt buộc)"
Q[21]="File đúng 20 MB có được nhận không (1 MB là 1.048.576 hay 1.000.000 byte)? (Figma ghi “Any file type · up to 20 MB”; UC, hệ thống không nêu)"
Q[22]="File 0 KB và file thực thi (.exe) có được tải lên không? (Figma ghi “Any file type”; UC EVC-07: quét mã độc trước khi dùng)"
Q[23]="Valid until trước Valid from thì có báo lỗi không? (UC, Figma, hệ thống chưa nêu)"
Q[24]="Ô “Also use for” chọn được nhiều requirement không, và có liệt kê requirement ngoài tier không? (Figma ghi “Other requirements in this workspace”, một giá trị; UC không nêu)"
Q[25]="Trạng thái Scanning, Blocked, Scan failed hiện ở đâu trên dòng evidence? (UC EVA-07 và EVC-07: quét trước khi dùng; Figma chỉ có “Scanning for viruses…” trong hộp thoại và “scanned, clean” ở chi tiết)"
Q[26]="Upload lại đúng file đã có (cùng nội dung) cho requirement khác thì hệ thống xử lý thế nào? (UC EVC-04: file giống hệt bị từ chối khi thêm version; EVA-03 chưa nêu)"
Q[27]="Danh sách Link existing evidence chỉ gồm evidence của workspace này, hay của cả scope (gồm evidence Not mapped upload từ Evidence Library)? (Figma ghi “Evidence already in this workspace” và Documents ghi “Each file belongs to one workspace”; UC EVC-09 gắn evidence với scope, EVA-04 ghi “Library doc”)"
Q[28]="Ô “Search evidence” tìm theo tên evidence hay cả tên file? (Figma, hệ thống chỉ có ô tìm kiếm)"
Q[29]="Nút xác nhận hiện thế nào khi chọn nhiều evidence (“Link 2 items”?), và requirement một expected evidence có hai file thì dòng đếm “1 mandatory item · 1 provided” có đổi không? (Figma, hệ thống chỉ có “Link 1 item”)"
Q[30]="Khi không còn evidence nào để chọn thì hiện câu gì? (hệ thống hiện “Every file of this workspace is already linked here.” cả khi workspace chưa có evidence nào; Figma chưa có trạng thái này)"
Q[31]="Có hộp thoại xác nhận trước khi gỡ liên kết không? (hệ thống gỡ ngay; UC EVA-05 chỉ ghi “The document stays in the library”; Figma chưa có)"
Q[32]="Evidence không còn gắn requirement nào được gọi là “Not mapped” hay “Not linked”, ở Evidence Library (chip, tab) và ở dòng phụ trong danh sách Link? (UC EVA-07 và EVC-09: Not mapped; Figma Documents: chip và tab “Not linked”; hệ thống: “Not linked to any requirement” ở Library, “not linked yet” ở danh sách Link)"
Q[33]="Chi tiết requirement có ô Owner không và chưa gán thì hiện gì? (UC EVA-06 có gán owner, hệ thống có ô Owner ghi “Nobody yet”; Figma Workspace / Requirement không có ô Owner)"
Q[34]="Danh sách Owner có người Customer Viewer không? (UC EVA-06 ghi “The owner must have access to the scope”; hệ thống chỉ liệt kê người có quyền vào scope)"
Q[35]="Dữ liệu requirement retired tạo ở đâu và hiện thế nào trong workspace đã có từ trước? (UC WSP-06; Figma, hệ thống chưa có framework có requirement retired)"
Q[36]="Workspace đã Archive hiện thế nào khi mở: nút Upload, Link, Gỡ, ô Owner bị ẩn hay vô hiệu, có dòng thông báo chỉ đọc không? (UC WSP-04 “Make the workspace read-only”; Figma, hệ thống chưa có workspace Archived)"
Q[37]="Mở workspace của scope mà người dùng không được gán thì hiện trang gì? (hệ thống hiện “This workspace doesn't exist” / “It may have been removed, or it belongs to an organisation you can't see.” cho Customer User; Figma chưa có)"
Q[39]="Câu “No matching requirements” / “Try another search or filter.” có đúng văn bản chính thức không? (chỉ lấy từ hệ thống; Figma chưa có trạng thái không có kết quả)"
Q[38]="Ô tìm kiếm của cây requirement có phân biệt chữ hoa, chữ thường không? (hệ thống không phân biệt; UC, Figma không nêu)"
Q[40]="Evidence gắn từ ô “Also use for” vào expected evidence nào của requirement kia, khi requirement đó có nhiều expected evidence? (Figma ghi “Other requirements in this workspace”; UC không nêu)"
Q[41]="Kiểm tra Blocked và Scan failed bằng scanner thật hay bằng file mẫu nào (vd file thử EICAR)? (UC EVC-07: scanner adapter còn chờ CrowdStrike; hệ thống chưa có cách tạo file bị chặn)"
Q[42]="Bỏ chọn owner (về lại “Nobody yet”) được không? (UC EVA-06 chỉ ghi gán owner; Figma, hệ thống chưa nêu)"
Q[43]="Nút Link khi chưa chọn evidence nào là nút xám không bấm được hay bị ẩn? (hệ thống: xám; Figma chỉ có trạng thái “Link 1 item”)"
Q[44]="Dung lượng file ở dòng file hiển thị thế nào với file cỡ MB (19,99 MB, 19.99 MB hay 20.0 MB)? (Figma chỉ có “402 KB”)"
Q[45]="Nhóm 1 Access Control của Appendix 10 · 2022 · Medium có bao nhiêu requirement: 11 như hệ thống hay 6 dòng với 58% như Figma frame Workspace / Requirement? (hai nguồn lệch nhau)"
Q[46]="Workspace tier High của Appendix 10 · 2022 có 76 requirement không? (76 lấy từ sheet Frameworks; hệ thống chưa có workspace High, Figma không có)"
Q[47]="Requirement có tính Provided khi evidence còn Scanning, Blocked hoặc Scan failed không? (UC EVA-07, EVC-07: quét trước khi dùng; UC không nói rõ chip của requirement)"
Q[48]="Trường “source” trong UC EVA-02 (“Text, tier, source, owner, expected evidence and linked documents”) là trường nào và hiện ở đâu? (nhãn “from Basic” là tier; Figma, hệ thống không có trường khác)"
Q[49]="Name chỉ có khoảng trắng có bị coi là trống không? (UC D8 chỉ ghi Name bắt buộc)"
Q[50]="File lớn hơn 20 MB bị chặn lúc chọn file hay lúc bấm Upload, và báo lỗi gì? (Figma ghi “up to 20 MB”; UC, hệ thống không nêu thông báo)"
Q[51]="Thông báo sau khi gỡ liên kết ghi gì? (hệ thống báo “Mapping removed from 4.1. The file stays in your library.”; UC, Figma không nêu)"
Q[52]="Partial có được tính vào phần trăm của nhóm không, và tính bao nhiêu? (Figma: nhóm Access Control 58% khớp công thức Provided tính 1, Partial tính 0,5 chia 6 requirement của frame, số requirement này lệch hệ thống: xem Q-EA-45; phần trăm workspace 38/61 = 62% chỉ đếm Provided)"
Q[53]="Nhãn “from <tier>” hiện thế nào với requirement của framework không có tier (vd ISO/IEC 27001)? (Figma, hệ thống chỉ có “from Basic”)"
Q[54]="Tìm evidence trong hộp thoại Link mà không có kết quả thì hiện gì? (Figma, hệ thống chưa nêu)"
Q[55]="Ô tìm kiếm của cây requirement tìm theo những trường nào ngoài mã và tên requirement (mô tả, tên nhóm)? (UC EVA-01 chỉ ghi “search and filter”; hệ thống tìm được theo mã và tên)"
Q[56]="Customer User và Customer Viewer thấy ô Owner ở trạng thái nào (xám, ẩn, chỉ chữ)? (UC EVA-06 chỉ Customer Admin gán owner; hệ thống: ô xám, không mở được danh sách; Figma không có ô Owner)"
Q[57]="Người đang là owner của requirement bị gỡ quyền vào scope thì ô Owner hiện gì (giao lại cho ai hay bỏ trống)? (UC D43: giao lại hoặc bỏ trống, chưa nói giao cho ai; thao tác gỡ quyền thuộc sheet Users, Scopes)"
USED=set()
def q(n, ctx=None):
    USED.add(n)
    return "%s → Q-EA-%02d" % (Q[n], n)
def qq(*ns):
    return "\n".join(q(n) for n in ns)

# =============== Điều hướng ===============
NAV="Điều hướng - Redirect"
case(NAV,"Vào chi tiết - Workspace detail","Bằng URL","Đã đăng nhập","Medium","Kiểm tra mở chi tiết workspace bằng URL",
 "1. Mở thẳng url chi tiết của [Workspace]",
 "- Hiển thị màn chi tiết [Workspace]\n- Mục Workspaces ở menu trái được tô nền",
 pre=ADMIN+"; có "+WS)
case(NAV,"Sang Evidence library","Từ chi tiết workspace","Bấm Evidence library","High","Kiểm tra mở Evidence library từ chi tiết workspace",
 OPEN+"\n2. Bấm nút Evidence library ở góc phải phần đầu trang",
 "- Chuyển sang màn Documents\n- Ô Workspace của bộ lọc chọn sẵn [Workspace] (Appendix 10 · 2022 · [System])\n- Có liên kết Back to workspace",
 uc="UC-EVC-01",pre=ADMIN+"; có "+WS)
case(NAV,"","Quay lại chi tiết","Bấm Back to workspace","Medium","Kiểm tra quay lại chi tiết workspace từ Evidence library",
 OPEN+"\n2. Bấm nút Evidence library\n3. Bấm liên kết Back to workspace",
 "- Quay lại màn chi tiết [Workspace]",
 uc="UC-EVC-01",pre=ADMIN+"; có "+WS)

# =============== Phần đầu màn ===============
HD="Phần đầu màn - Header"
case(HD,"Tiêu đề","Hiển thị","Tên workspace và scope","High","Kiểm tra tiêu đề và dòng phụ của chi tiết workspace",
 OPEN+"\n2. Kiểm tra phần đầu trang",
 "- Có nút mũi tên quay lại ở bên trái tiêu đề\n- Tiêu đề: Appendix 10 · 2022 · Medium\n- Dòng phụ: [System] · System scope",
 pre=ADMIN+"; có "+WS)
case(HD,"","Chip trạng thái","Preparing và coverage","High","Kiểm tra chip trạng thái ở phần đầu trang",
 OPEN+"\n2. Kiểm tra chip bên phải tiêu đề",
 "- Chip ghi: Preparing · 62% coverage (cùng số với cột Evidence coverage ở màn Workspaces)",
 pre=ADMIN+"; có "+WS+", 38 trên 61 requirement đủ evidence bắt buộc",q=q(1))
case(HD,"Tóm tắt coverage","Hiển thị","Workspace có evidence","High","Kiểm tra khung tóm tắt coverage của cây requirement",
 OPEN+"\n2. Kiểm tra khung trên cùng của cột trái",
 "- Dòng đầu: Appendix 10 · 2022 · Medium và 62%\n- Thanh tiến độ tô 62%\n- Dòng chữ: 38 of 61 requirements have their mandatory evidence · not a compliance decision",
 pre=ADMIN+"; có "+WS+", 38 trên 61 requirement đủ evidence bắt buộc")
case(HD,"","Workspace mới","Chưa có evidence","High","Kiểm tra workspace mới chưa có evidence",
 OPEN,
 "- Khung tóm tắt: 0% và dòng 0 of 61 requirements have their mandatory evidence · not a compliance decision\n- Mọi requirement trong cây có chip Missing\n- Mọi nhóm có 0%",
 uc="UC-EVA-07",pre=ADMIN+"; có "+EMPTY)

# =============== Cây requirement ===============
TR="Cây requirement - Requirement tree"
case(TR,"Nhóm requirement","Hiển thị","Dòng nhóm","Medium","Kiểm tra dòng nhóm của cây requirement",
 OPEN+"\n2. Kiểm tra dòng nhóm 1 Access Control",
 "- Dòng nhóm có: mũi tên, số thứ tự trong ô vuông, tên nhóm, phần trăm ở bên phải\n- Thanh tiến độ ở dưới dòng nhóm",
 pre=ADMIN+"; có "+WS)
case(TR,"","Mặc định","Khi mở màn","High","Kiểm tra nhóm và requirement mặc định khi mở màn",
 OPEN,
 "- Nhóm 1 được mở sẵn, các nhóm còn lại thu gọn\n- Requirement đầu tiên của nhóm 1 (R.1.1.1) được chọn, dòng tô nền cam nhạt, viền cam\n- Cột phải hiển thị chi tiết R.1.1.1",
 pre=ADMIN+"; có "+WS)
case(TR,"","Chọn requirement","Bấm một requirement","High","Kiểm tra chọn requirement khác trong cây",
 OPEN+"\n2. Bấm requirement R.1.1.2 trong nhóm 1",
 "- Dòng R.1.1.2 được tô nền cam nhạt, viền cam; dòng R.1.1.1 trở lại nền thường\n- Cột phải đổi sang chi tiết R.1.1.2: breadcrumb, tiêu đề, chip trạng thái",
 pre=ADMIN+"; có "+WS)
case(TR,"","Phần trăm nhóm","Nhóm có evidence","High","Kiểm tra phần trăm của nhóm có 3 trên 11 requirement Provided",
 OPEN+"\n2. Kiểm tra dòng nhóm 1 Access Control",
 "- Dòng nhóm ghi 27%\n- Thanh tiến độ tô 27%",
 uc="UC-EVA-07",pre=ADMIN+"; có "+WS+", nhóm 1 Access Control (11 requirement): 3 Provided, 8 Missing",q=q(45))
case(TR,"","","Nhóm đủ evidence","Medium","Kiểm tra phần trăm của nhóm có mọi requirement Provided",
 OPEN+"\n2. Kiểm tra dòng nhóm 1 Access Control",
 "- Dòng nhóm ghi 100%\n- Thanh tiến độ tô đầy",
 uc="UC-EVA-07",pre=ADMIN+"; có "+WS+", nhóm 1 Access Control (11 requirement) đều Provided",q=q(45))
case(TR,"","","Nhóm có Partial","Medium","Kiểm tra phần trăm của nhóm có requirement Partial",
 OPEN+"\n2. Kiểm tra dòng nhóm 1 Access Control","",
 uc="UC-EVA-07",pre=ADMIN+"; có "+WS+", nhóm 1 Access Control (11 requirement): 1 Provided, 1 Partial, 9 Missing",q=qq(52,45))
case(TR,"Trạng thái requirement","Missing","Chưa có evidence","High","Kiểm tra chip Missing",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Kiểm tra chip của R.1.1.2 ở cây và ở chi tiết",
 "- Cả hai nơi có chip Missing, nền hồng, icon tròn đỏ dấu !",
 uc="UC-EVA-07",pre=ADMIN+"; có "+WS+"; R.1.1.2 chưa có evidence")
case(TR,"","Provided","Đủ evidence bắt buộc","High","Kiểm tra chip Provided",
 OPEN+"\n2. Kiểm tra chip của requirement R.1.1.1 ở cây và ở chi tiết",
 "- Cả hai nơi có chip Provided, nền xanh nhạt, dấu tích xanh",
 uc="UC-EVA-07",pre=ADMIN+"; có "+WS+"; R.1.1.1 đã có evidence sạch ở EE-001")
case(TR,"","Partial","Thiếu một phần evidence","Medium","Kiểm tra chip Partial",
 OPEN+"\n2. Kiểm tra chip của requirement [Requirement Partial] ở cây",
 "",uc="UC-EVA-07",pre=ADMIN+"; có "+WS+"; có requirement [Requirement Partial] ở trạng thái Partial",q=q(3))
case(TR,"","Out of scope","Ngoài tier hoặc retired","Medium","Kiểm tra hiển thị requirement ngoài tier",
 OPEN+"\n2. Tìm trong cây xem có requirement chỉ thuộc tier High không","",
 uc="UC-WSP-06",pre=ADMIN+"; có "+WS,q=q(4))
case(TR,"","Clarification requested","Có yêu cầu làm rõ","Medium","Kiểm tra trạng thái Clarification requested",
 OPEN+"\n2. Kiểm tra requirement R.1.1.2 ở cây","",
 uc="UC-EVA-01",pre=ADMIN+"; có "+WS+"; R.1.1.2 có yêu cầu làm rõ đang mở",q=q(5))
SR="Tìm kiếm - Search"
case(TR,SR,"Hiển thị","Ô tìm kiếm","Low","Kiểm tra ô tìm kiếm của cây requirement",
 OPEN+"\n2. Kiểm tra ô tìm kiếm ở đầu cột trái",
 "- Ô tìm kiếm có icon kính lúp, placeholder: Search\n- Bên cạnh có ô lọc trạng thái, mặc định All",
 pre=ADMIN+"; có "+WS)
case(TR,"","Theo mã","Mã requirement","High","Kiểm tra tìm theo mã requirement",
 OPEN+"\n2. Nhập R.1.1.2 vào ô tìm kiếm",
 "- Cây chỉ còn nhóm 1 với requirement R.1.1.2\n- Cột phải vẫn hiển thị requirement đang chọn trước đó",
 pre=ADMIN+"; có "+WS)
case(TR,"","Theo tên","Một phần tên requirement","High","Kiểm tra tìm theo một phần tên requirement",
 OPEN+"\n2. Nhập inactive vào ô tìm kiếm",
 "- Cây chỉ còn nhóm 1 với requirement R.1.1.3 Disable inactive accounts automatically",
 pre=ADMIN+"; có "+WS)
case(TR,"","Theo nhóm","Tên nhóm","Medium","Kiểm tra tìm theo tên nhóm requirement",
 OPEN+"\n2. Nhập Access Control vào ô tìm kiếm","",
 uc="UC-EVA-01",pre=ADMIN+"; có "+WS,q=q(55))
case(TR,"","Chữ hoa","Từ khoá viết hoa","Medium","Kiểm tra tìm kiếm khi nhập chữ hoa",
 OPEN+"\n2. Nhập ACCESS vào ô tìm kiếm",
 "- Kết quả giống khi nhập access: các requirement có chữ access trong tên (R.1.3.1, R.1.3.3, R.2.6.1) cùng nhóm của chúng",
 pre=ADMIN+"; có "+WS,q=q(38))
case(TR,"","Không có kết quả","Từ khoá không khớp","High","Kiểm tra tìm kiếm không ra kết quả",
 OPEN+"\n2. Nhập zzzxx vào ô tìm kiếm",
 "- Cây ẩn mọi nhóm\n- Thông báo: No matching requirements\n- Dòng phụ: Try another search or filter.",
 pre=ADMIN+"; có "+WS,q=q(39))
case(TR,"","Ký tự đặc biệt","Chuỗi đặc biệt","Medium","Kiểm tra nhập ký tự đặc biệt vào ô tìm kiếm",
 OPEN+"\n2. Nhập ' OR 1=1 -- vào ô tìm kiếm",
 "- Không có lỗi hệ thống, không lộ thông tin kỹ thuật\n- Chuỗi được tìm như văn bản thường",
 pre=ADMIN+"; có "+WS)
case(TR,"","Xoá từ khoá","Xoá hết","Medium","Kiểm tra xoá từ khoá tìm kiếm",
 OPEN+"\n2. Nhập inactive vào ô tìm kiếm\n3. Xoá hết nội dung ô tìm kiếm",
 "- Cây hiển thị lại đủ nhóm như lúc mở màn",
 pre=ADMIN+"; có "+WS)
FL="Bộ lọc - Filter"
case(TR,FL,"Hiển thị","Các lựa chọn","Medium","Kiểm tra các lựa chọn của ô lọc trạng thái",
 OPEN+"\n2. Bấm ô lọc trạng thái cạnh ô tìm kiếm",
 "- Mặc định: All\n- Các lựa chọn: All, Missing, Partial, Provided; mục đang chọn có dấu tích",
 pre=ADMIN+"; có "+WS,q=q(5))
case(TR,"","Lọc theo trạng thái","Missing","High","Kiểm tra lọc requirement Missing",
 OPEN+"\n2. Chọn Missing ở ô lọc trạng thái",
 "- Cây chỉ còn các requirement có chip Missing\n- Không còn requirement Provided",
 pre=ADMIN+"; có "+WS+"; R.1.1.1 Provided, các requirement còn lại Missing")
case(TR,"","","Provided","High","Kiểm tra lọc requirement Provided",
 OPEN+"\n2. Chọn Provided ở ô lọc trạng thái",
 "- Cây chỉ còn requirement R.1.1.1 (chip Provided)",
 pre=ADMIN+"; có "+WS+"; R.1.1.1 Provided, các requirement còn lại Missing")
case(TR,"","","Partial","Medium","Kiểm tra lọc requirement Partial",
 OPEN+"\n2. Chọn Partial ở ô lọc trạng thái",
 "",
 pre=ADMIN+"; có "+WS+"; có requirement [Requirement Partial] ở trạng thái Partial, các requirement còn lại Missing hoặc Provided",q=q(3))
case(TR,"","Kết hợp","Lọc và tìm cùng lúc","Medium","Kiểm tra dùng bộ lọc cùng từ khoá tìm kiếm",
 OPEN+"\n2. Chọn Missing ở ô lọc trạng thái\n3. Nhập inactive vào ô tìm kiếm",
 "- Cây chỉ còn requirement R.1.1.3 (Missing, tên có inactive)",
 pre=ADMIN+"; có "+WS+"; R.1.1.1 Provided, các requirement còn lại Missing",q=q(6))
case(TR,"","Không có kết quả","Không requirement khớp","Medium","Kiểm tra lọc khi không có requirement khớp",
 OPEN+"\n2. Chọn Provided ở ô lọc trạng thái","",
 pre=ADMIN+"; có "+EMPTY,q=q(7))

# =============== Chi tiết requirement ===============
DT="Chi tiết requirement - Requirement detail"
case(DT,"Phần đầu requirement","Breadcrumb","Nhóm / nhóm con / mã","Medium","Kiểm tra breadcrumb của requirement",
 OPEN+"\n2. Kiểm tra dòng đầu của cột phải",
 "- Breadcrumb: 1 Access Control / 1.1 Account management / R.1.1.1\n- Hai mục đầu màu cam, mục cuối màu đen",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS)
case(DT,"","Mã và tier","Requirement thuộc Basic","Medium","Kiểm tra dòng mã và tier của requirement thuộc Basic",
 OPEN+"\n2. Kiểm tra dòng nhỏ phía trên tiêu đề của R.1.1.1",
 "- Dòng ghi: R.1.1.1 · from Basic",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS)
case(DT,"","","Requirement thêm ở Medium","Medium","Kiểm tra dòng mã và tier của requirement thêm ở Medium",
 OPEN+"\n2. Chọn một requirement thêm ở tier Medium\n3. Kiểm tra dòng nhỏ phía trên tiêu đề",
 "",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS,q=q(8))
case(DT,"","","Framework không có tier","Medium","Kiểm tra dòng mã của requirement thuộc framework không có tier",
 "1. Mở chi tiết [Workspace ISO] (màn Workspaces, bấm tên workspace)\n2. Kiểm tra dòng nhỏ phía trên tiêu đề của requirement đầu tiên","",
 uc="UC-EVA-02",pre=ADMIN+"; có [Workspace ISO] ISO/IEC 27001 · 2022 của scope [Organization], chế độ Assisted",q=q(53))
case(DT,"","Nội dung","Tiêu đề, mô tả, chip","High","Kiểm tra tiêu đề, mô tả và chip trạng thái của requirement",
 OPEN+"\n2. Kiểm tra khối trên của cột phải",
 "- Tiêu đề: Establish an account management mechanism\n- Chip trạng thái ở góc phải khối\n- Mô tả: Establish an account management mechanism, including procedures for account application, creation, modification, activation, deactivation, and deletion.",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS)
case(DT,"","Nhãn lạ","No design yet","Low","Kiểm tra nhãn No design yet",
 OPEN+"\n2. Kiểm tra bên phải ô Owner","",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS,q=qq(2,33))
case(DT,"","Yêu cầu làm rõ","Đang mở","Medium","Kiểm tra hiển thị yêu cầu làm rõ đang mở",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Kiểm tra chi tiết requirement","",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; R.1.1.2 có yêu cầu làm rõ đang mở",q=q(15))
case(DT,"","Trường source","Source của requirement","Low","Kiểm tra trường source của requirement",
 OPEN+"\n2. Kiểm tra chi tiết requirement R.1.1.1","",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS,q=q(48))
EX="Expected evidence"
case(DT,EX,"Tiêu đề","Dòng đếm chưa có evidence","High","Kiểm tra dòng đếm expected evidence khi chưa có evidence",
 OPEN+"\n2. Kiểm tra khối Expected evidence",
 "- Tiêu đề: Expected evidence\n- Dòng đếm: 1 mandatory item · 0 provided\n- Có hai nút: Link existing evidence, Upload evidence",
 uc="UC-EVA-02",pre=ADMIN+"; có "+EMPTY)
case(DT,"","","Dòng đếm đã có evidence","High","Kiểm tra dòng đếm expected evidence khi đã có evidence",
 OPEN+"\n2. Kiểm tra khối Expected evidence",
 "- Dòng đếm: 1 mandatory item · 1 provided",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; R.1.1.1 đã có evidence sạch ở EE-001")
case(DT,"","Thẻ expected evidence","Thông tin EE","High","Kiểm tra thẻ expected evidence",
 OPEN+"\n2. Kiểm tra thẻ trong khối Expected evidence",
 "- Dòng đầu: EE-001 · Account Management Procedure\n- Mô tả: Documented procedure covering account request, creation, modification, activation, deactivation, and deletion.\n- Tag Mandatory ở góc phải thẻ",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS)
case(DT,"","","Chưa có evidence","Medium","Kiểm tra thẻ expected evidence chưa có evidence",
 OPEN+"\n2. Kiểm tra thẻ EE-001",
 "- Thẻ không có dòng evidence nào\n- Dòng chữ: No evidence yet. Upload a file or link one that is already in this workspace.",
 uc="UC-EVA-02",pre=ADMIN+"; có "+EMPTY,q=q(10))
case(DT,"","","Nhiều expected evidence","Medium","Kiểm tra requirement có nhiều expected evidence",
 OPEN+"\n2. Chọn requirement [Requirement nhiều EE]\n3. Kiểm tra khối Expected evidence","",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; có requirement [Requirement nhiều EE] có từ hai expected evidence trở lên",q=q(9))
EV="Dòng evidence - Evidence row"
case(DT,EV,"Hiển thị","Thông tin evidence","High","Kiểm tra dòng evidence trong thẻ expected evidence",
 OPEN+"\n2. Kiểm tra dòng evidence dưới EE-001",
 "- Icon file, tên evidence (Access control policy)\n- Dòng phụ: access-control-policy-v3.pdf • Uploaded Sep 12, 2026 by Wei Chen • valid until Sep 2027 • also used in R.1.2.1\n- Chip Provided, icon mắt ở bên phải",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; evidence Access control policy (version 3, access-control-policy-v3.pdf, Wei Chen upload 12/09/2026, hết hạn 12/09/2027) gắn R.1.1.1 và R.1.2.1",q=q(12))
case(DT,"","","Evidence chỉ dùng cho một requirement","Medium","Kiểm tra dòng evidence chỉ gắn một requirement",
 OPEN+"\n2. Kiểm tra dòng evidence dưới EE-001",
 "- Dòng phụ không có đoạn also used in",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; evidence Access control policy chỉ gắn R.1.1.1")
case(DT,"","","Evidence dùng cho hai requirement","Medium","Kiểm tra dòng evidence gắn hai requirement ở requirement còn lại",
 OPEN+"\n2. Chọn requirement R.1.2.1\n3. Kiểm tra dòng evidence",
 "- Dòng phụ ghi: also used in R.1.1.1",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1 và R.1.2.1")
case(DT,"","","Không có ngày hết hạn","Medium","Kiểm tra dòng evidence không có Valid until",
 OPEN+"\n2. Kiểm tra dòng evidence dưới EE-001","",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; evidence của R.1.1.1 không điền Valid until",q=q(13))
case(DT,"","","Nhiều version","Medium","Kiểm tra requirement chỉ hiện version hiện hành của evidence",
 OPEN+"\n2. Kiểm tra dòng evidence dưới EE-001",
 "- Chỉ có một dòng evidence, file là access-control-policy-v3.pdf (version 3 hiện hành)\n- Không có dòng riêng cho version 1, version 2",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; evidence Access control policy có 3 version, gắn R.1.1.1",q=q(11))
case(DT,"","","Evidence quá hạn","Medium","Kiểm tra dòng evidence quá ngày Valid until",
 OPEN+"\n2. Kiểm tra dòng evidence dưới EE-001 và chip của requirement","",
 uc="UC-EVA-02",pre=ADMIN+"; có "+WS+"; evidence của R.1.1.1 có Valid until là ngày đã qua",q=q(14))
case(DT,"Chi tiết evidence","Mở","Bấm icon mắt","High","Kiểm tra mở chi tiết evidence từ dòng evidence",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001",
 "- Khung chi tiết trượt ra bên phải, tiêu đề Access control policy, dòng phụ: access-control-policy-v3.pdf · 1.2 MB · scanned, clean\n- Workspace: Appendix 10 · 2022 · [System]; Valid: 12 Sep 2026 – 12 Sep 2027; Review: Not reviewed by SGS yet\n- Bảng Used for: R.1.1.1 với EE-001, R.1.2.1 với EE-009\n- Bảng Versions: version 3, 2, 1 với tên file, ngày, người upload\n- Ba nút ở chân khung: Unlink from R.1.1.1, Download, Upload new version\n- Dấu × ở góc phải đóng khung",
 uc="UC-EVC-02",pre=ADMIN+"; có "+WS+"; evidence Access control policy (3 version) gắn R.1.1.1 (EE-001) và R.1.2.1 (EE-009)")

# =============== Upload evidence ===============
UP="Upload evidence"
case(UP,"Hộp thoại","Mở","Bấm Upload evidence","High","Kiểm tra mở hộp thoại Upload evidence",
 OPEN+"\n2. Bấm nút Upload evidence ở khối Expected evidence",
 "- Hiện hộp thoại Upload evidence, dấu × ở góc phải\n- Dòng ngữ cảnh: For R.1.1.1 Establish an account management mechanism · EE-001 Account Management Procedure",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","Các ô","Ô và nút","High","Kiểm tra các ô và nút của hộp thoại Upload evidence",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Kiểm tra các ô trong hộp thoại",
 "- Ô File * là vùng kéo thả: icon tải lên, Drag files here or browse., dòng nhỏ Any file type · up to 20 MB · scanned for viruses\n- Ô Name * trống\n- Ô Valid from (optional) và Valid until (optional), placeholder DD MMM YYYY, icon lịch; dưới Valid until có dòng Leave empty if it doesn't expire.\n- Ô Also use for (optional), placeholder Other requirements in this workspace\n- Nút Cancel và Upload",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(16))
case(UP,"Chọn file","Một file","Bằng nút browse","High","Kiểm tra chọn một file bằng browse",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Bấm browse, chọn file ad-inactive-accounts.png (402 KB)",
 "- Dưới vùng kéo thả có dòng file: ad-inactive-accounts.png, Scanning for viruses… · 402 KB\n- Ô Name được điền sẵn từ tên file",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(17))
case(UP,"","Nhiều file","Chọn ba file","Medium","Kiểm tra chọn ba file cùng lúc",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Bấm browse, chọn ba file a.pdf, b.pdf, c.pdf",
 "- Ba file được nhận một lần, mỗi file thành một evidence có title lấy từ tên file\n- Valid from, Valid until, Also use for áp chung cho cả ba file",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(18))
case(UP,"Kiểm tra bắt buộc","Bỏ trống","File và Name","High","Kiểm tra bấm Upload khi chưa chọn file và chưa nhập Name",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Bấm nút Upload",
 "- Hộp thoại vẫn mở, không tạo evidence\n- Dưới ô File: Choose a file.\n- Dưới ô Name: Enter a name.",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(19))
case(UP,"","Thiếu một ô","Có file, bỏ trống Name","High","Kiểm tra bấm Upload khi đã chọn file nhưng xoá Name",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Xoá hết nội dung ô Name\n5. Bấm nút Upload",
 "- Hộp thoại vẫn mở, không tạo evidence\n- Dưới ô Name: Enter a name.\n- Không có lỗi ở ô File",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","","Có Name, chưa chọn file","High","Kiểm tra bấm Upload khi đã nhập Name nhưng chưa chọn file",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Nhập Name: Inactive account policy\n4. Bấm nút Upload",
 "- Hộp thoại vẫn mở, không tạo evidence\n- Dưới ô File: Choose a file.\n- Không có lỗi ở ô Name",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","Name","Chỉ khoảng trắng","Medium","Kiểm tra Name chỉ có khoảng trắng",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Xoá nội dung ô Name, nhập ba dấu cách\n5. Bấm nút Upload",
 "- Hộp thoại vẫn mở, không tạo evidence\n- Dưới ô Name: Enter a name.",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(49))
case(UP,"","","Name rất dài","Low","Kiểm tra Name rất dài",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Nhập vào ô Name chuỗi 1000 ký tự\n5. Bấm nút Upload","",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(20))
case(UP,"Kích thước file","Dưới giới hạn","19,99 MB","High","Kiểm tra chọn file dưới 20 MB",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file big-ok.pdf (19,99 MB)",
 "- File được nhận, dưới vùng kéo thả có dòng file big-ok.pdf, Scanning for viruses… và dung lượng của file",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(44))
case(UP,"","Đúng giới hạn","20 MB","Medium","Kiểm tra chọn file đúng 20 MB",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file big-20.pdf (đúng 20 MB)","",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(21))
case(UP,"","Quá giới hạn","Lớn hơn 20 MB","High","Kiểm tra chọn file lớn hơn 20 MB",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file big-over.pdf (21 MB)",
 "",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(50))
case(UP,"","File đặc biệt","0 KB, .exe","Low","Kiểm tra chọn file 0 KB và file .exe",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file empty.txt (0 KB)\n4. Chọn file tool.exe","",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(22))
case(UP,"Ngày hiệu lực","Chọn ngày","Valid from và Valid until","Medium","Kiểm tra chọn ngày hiệu lực",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Bấm icon lịch ở Valid from, chọn 20/09/2026\n4. Bấm icon lịch ở Valid until, chọn 20/09/2027",
 "- Valid from hiển thị 20 Sep 2026, Valid until hiển thị 20 Sep 2027 (định dạng DD MMM YYYY)",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","Ngày sai","Valid until trước Valid from","Medium","Kiểm tra Valid until trước Valid from",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Chọn Valid from 20/09/2026, Valid until 19/09/2026\n5. Bấm nút Upload","",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(23))
case(UP,"Also use for","Danh sách","Requirement khác","Medium","Kiểm tra danh sách ô Also use for",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Bấm ô Also use for",
 "- Danh sách liệt kê các requirement khác trong workspace\n- Không có R.1.1.1 (requirement đang upload)",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(24))
case(UP,"Hủy","Cancel","Bấm Cancel","Medium","Kiểm tra bấm Cancel trong hộp thoại Upload",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Bấm nút Cancel",
 "- Hộp thoại đóng\n- R.1.1.1 vẫn Missing, không có evidence mới",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","Đóng","Bấm dấu ×","Low","Kiểm tra bấm dấu × trong hộp thoại Upload",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Bấm dấu × ở góc phải hộp thoại",
 "- Hộp thoại đóng\n- R.1.1.1 vẫn Missing, không có evidence mới",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"Upload thành công","Một file","Hiện dưới expected evidence","High","Kiểm tra evidence hiện dưới expected evidence sau khi upload",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png, giữ Name điền sẵn\n4. Bấm nút Upload",
 "- Hộp thoại đóng\n- Dưới EE-001 có dòng evidence mới: tên theo Name, tên file ad-inactive-accounts.png, Uploaded <ngày hôm nay> by <tên người đăng nhập>",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","Số liệu","Coverage tăng","High","Kiểm tra số liệu coverage sau khi upload evidence cho R.1.1.1",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Bấm nút Upload\n5. Chờ file quét xong, kiểm tra cây và khung tóm tắt",
 "- R.1.1.1 có chip Provided; dòng đếm: 1 mandatory item · 1 provided\n- Khung tóm tắt: 2% và dòng 1 of 61 requirements have their mandatory evidence · not a compliance decision\n- Nhóm 1 Access Control (11 requirement): 9%\n- Chip phần đầu trang: Preparing · 2% coverage",
 uc="UC-EVA-07",pre=ADMIN+"; có "+EMPTY,q=q(45))
case(UP,"","Màn Workspaces","Coverage ở danh sách","High","Kiểm tra coverage ở màn Workspaces sau khi upload",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png, bấm Upload, chờ quét xong\n4. Bấm menu Workspaces ở menu trái",
 "- Dòng [Workspace]: cột Evidence coverage ghi 1 of 61 requirements và 2%",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","Evidence Library","Hiện trong thư viện","High","Kiểm tra evidence vừa upload hiện trong Evidence Library",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png, bấm Upload\n4. Bấm nút Evidence library",
 "- Bảng Documents có dòng evidence mới: tên theo Name, tên file ad-inactive-accounts.png, Workspace Appendix 10 · 2022 · [System], Used for R.1.1.1, Uploaded <tên người đăng nhập> · <ngày hôm nay>\n- Số trên tab All tăng 1",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(UP,"","Also use for","Dùng cho requirement khác","High","Kiểm tra upload có chọn Also use for",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Chọn R.1.1.4 ở ô Also use for\n5. Bấm nút Upload",
 "- Dòng evidence mới hiện ở R.1.1.1 với also used in R.1.1.4\n- Chọn R.1.1.4: dòng evidence mới cũng hiện ở R.1.1.4 với also used in R.1.1.1",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY,q=q(40))
case(UP,"Trạng thái quét","Scanning","Vừa upload xong","High","Kiểm tra trạng thái ngay sau khi upload",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png, bấm Upload\n4. Kiểm tra dòng evidence ngay sau khi upload",
 "- Dòng evidence có trạng thái Scanning",
 uc="UC-EVA-07",pre=ADMIN+"; có "+EMPTY,q=q(25))
case(UP,"","Blocked","File bị chặn","High","Kiểm tra evidence khi file bị chặn",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file bị scanner chặn, bấm Upload\n4. Chờ quét xong, kiểm tra dòng evidence",
 "- Dòng evidence có trạng thái Blocked",
 uc="UC-EVA-07",pre=ADMIN+"; có "+EMPTY,q=qq(25,41))
case(UP,"","Scan failed","Quét lỗi","Medium","Kiểm tra evidence khi quét lỗi",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file, bấm Upload, để scanner trả lỗi\n4. Kiểm tra dòng evidence",
 "- Dòng evidence có trạng thái Scan failed",
 uc="UC-EVA-07",pre=ADMIN+"; có "+EMPTY,q=qq(25,41))
case(UP,"","Chip requirement","Evidence Blocked","High","Kiểm tra chip requirement khi evidence bị chặn",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file bị scanner chặn, bấm Upload\n4. Chờ quét xong, kiểm tra chip của R.1.1.1 ở cây và ở chi tiết","",
 uc="UC-EVA-07",pre=ADMIN+"; có "+EMPTY,q=qq(47,41))
case(UP,"Trùng file","Upload lại","Cùng nội dung","Medium","Kiểm tra upload lại đúng file đã có",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Upload evidence\n4. Chọn file ad-inactive-accounts.png (cùng nội dung), bấm Upload","",
 uc="UC-EVA-03",pre=ADMIN+"; có "+WS+"; file ad-inactive-accounts.png đã upload cho R.1.1.1",q=q(26))

# =============== Link existing evidence ===============
LK="Link existing evidence"
case(LK,"Hộp thoại","Mở","Bấm Link existing evidence","High","Kiểm tra mở hộp thoại Link existing evidence",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence",
 "- Hiện hộp thoại Link existing evidence, dấu × ở góc phải\n- Dòng giải thích: Evidence already in this workspace. Linking doesn't copy the file; a new version updates every requirement that uses it.\n- Ô Search evidence có icon kính lúp\n- Danh sách evidence, mỗi dòng có ô tick, tên evidence, dòng phụ <tên file> · used in <requirement>\n- Nút Cancel và nút Link",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; evidence Access control policy (access-control-policy-v3.pdf) gắn R.1.1.1 và R.1.2.1")
case(LK,"","Nút Link","Chưa chọn","Medium","Kiểm tra nút Link khi chưa chọn evidence",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence",
 "- Nút Link màu xám, không bấm được",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1",q=q(43))
case(LK,"","","Chọn một evidence","High","Kiểm tra nút Link khi chọn một evidence",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Tick evidence Access control policy",
 "- Ô tick của evidence được chọn có dấu tích\n- Nút đổi thành Link 1 item, màu cam, bấm được",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1")
case(LK,"","","Chọn hai evidence","Medium","Kiểm tra nút Link khi chọn hai evidence",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Tick hai evidence","",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; có hai evidence gắn R.1.1.1",q=q(29))
case(LK,"Tìm trong hộp thoại","Theo tên","Một phần tên evidence","Medium","Kiểm tra tìm evidence trong hộp thoại Link",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Nhập Access vào ô Search evidence",
 "- Danh sách chỉ còn evidence có tên chứa Access",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; có evidence Access control policy và evidence Account review minutes Q2 gắn R.1.1.4",q=q(28))
case(LK,"","Không có kết quả","Từ khoá không khớp","Low","Kiểm tra tìm evidence không ra kết quả trong hộp thoại Link",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Nhập zzzxx vào ô Search evidence","",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1",q=q(54))
case(LK,"Danh sách evidence","Evidence chưa gắn","Chưa dùng cho requirement nào","Medium","Kiểm tra evidence chưa gắn requirement nào trong danh sách",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence",
 "- Danh sách có dòng evidence Access control policy, có ô tick",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; evidence Access control policy đã gỡ khỏi mọi requirement",q=q(32))
case(LK,"","Điều kiện","Evidence chưa quét xong hoặc bị chặn","High","Kiểm tra danh sách không cho chọn evidence chưa sạch",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence",
 "- Danh sách không có evidence Blocked và evidence đang Scanning (UC EVA-04: chỉ file sạch)",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; có evidence Blocked và evidence đang Scanning",q=q(41))
case(LK,"","Phạm vi","Evidence của workspace khác","High","Kiểm tra danh sách không có evidence của workspace khác",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence",
 "",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; scope [System] có thêm workspace [Workspace khác] khác framework, đã có evidence",q=q(27))
case(LK,"","Trạng thái rỗng","Workspace chưa có evidence","Medium","Kiểm tra hộp thoại Link khi workspace chưa có evidence",
 OPEN+"\n2. Bấm nút Link existing evidence",
 "- Không có dòng evidence nào để chọn\n- Hiển thị câu: Every file of this workspace is already linked here.\n- Nút Link màu xám",
 uc="UC-EVA-04",pre=ADMIN+"; có "+EMPTY,q=q(30))
case(LK,"Hủy","Cancel","Bấm Cancel","Low","Kiểm tra bấm Cancel trong hộp thoại Link",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Tick evidence Access control policy\n5. Bấm nút Cancel",
 "- Hộp thoại đóng\n- R.1.1.2 không có evidence mới",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1")
case(LK,"Liên kết thành công","Một evidence","Hiện dưới expected evidence","High","Kiểm tra evidence hiện dưới expected evidence sau khi link",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Tick evidence Access control policy\n5. Bấm nút Link 1 item",
 "- Hộp thoại đóng\n- Dưới thẻ expected evidence của R.1.1.2 có dòng evidence Access control policy với also used in R.1.1.1\n- R.1.1.2 có chip Provided",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; R.1.1.2 chưa có evidence; evidence Access control policy sạch, gắn R.1.1.1")
case(LK,"","Số liệu","Coverage tăng","High","Kiểm tra số liệu coverage sau khi link evidence cho R.1.1.2",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Tick evidence Access control policy\n5. Bấm nút Link 1 item",
 "- Khung tóm tắt: 3% và dòng 2 of 61 requirements have their mandatory evidence · not a compliance decision\n- Nhóm 1 Access Control (11 requirement): 18%\n- Dòng evidence ở R.1.1.1 đổi thành also used in R.1.1.2",
 uc="UC-EVA-07",pre=ADMIN+"; có "+WS+"; 1 of 61 requirement Provided (R.1.1.1 có evidence Access control policy sạch); R.1.1.2 chưa có evidence",q=q(45))
case(LK,"","Không sao chép","Một file duy nhất","Medium","Kiểm tra link không tạo thêm file trong Evidence Library",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence\n4. Tick evidence Access control policy, bấm Link 1 item\n5. Bấm nút Evidence library",
 "- Documents chỉ có một dòng Access control policy\n- Cột Used for của dòng đó ghi R.1.1.1, R.1.1.2",
 uc="UC-EVA-04",pre=ADMIN+"; có "+WS+"; R.1.1.2 chưa có evidence; evidence Access control policy sạch, gắn R.1.1.1")

# =============== Gỡ liên kết ===============
UL="Gỡ liên kết - Unlink"
case(UL,"Gỡ evidence","Evidence duy nhất","Requirement về Missing","High","Kiểm tra gỡ evidence duy nhất khỏi requirement",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001\n3. Bấm Unlink from R.1.1.1",
 "- Dòng evidence biến mất khỏi EE-001, thẻ không còn dòng evidence nào\n- R.1.1.1 đổi chip Provided thành Missing; dòng đếm: 1 mandatory item · 0 provided\n- Khung tóm tắt: 0% và dòng 0 of 61 requirements…; nhóm 1: 0%",
 uc="UC-EVA-05",pre=ADMIN+"; có "+WS+"; 1 of 61 requirement Provided (R.1.1.1 có evidence Access control policy chỉ gắn R.1.1.1)",q=q(31))
case(UL,"","Evidence dùng hai nơi","Requirement kia giữ nguyên","High","Kiểm tra gỡ evidence dùng cho hai requirement",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001\n3. Bấm Unlink from R.1.1.1\n4. Chọn requirement R.1.2.1",
 "- R.1.1.1 không còn dòng evidence\n- R.1.2.1 vẫn có dòng evidence Access control policy và chip Provided",
 uc="UC-EVA-05",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1 và R.1.2.1",q=q(31))
case(UL,"","Chi tiết evidence","Used for sau khi gỡ","Medium","Kiểm tra bảng Used for sau khi gỡ khỏi một requirement",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001\n3. Bấm Unlink from R.1.1.1\n4. Chọn R.1.2.1, bấm icon mắt ở dòng evidence",
 "- Bảng Used for chỉ còn R.1.2.1 với EE-009",
 uc="UC-EVA-05",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1 (EE-001) và R.1.2.1 (EE-009)",q=q(31))
case(UL,"Evidence còn trong thư viện","Gỡ khỏi mọi requirement","Evidence không bị xoá","High","Kiểm tra evidence còn trong Evidence Library sau khi gỡ",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001\n3. Bấm Unlink from R.1.1.1\n4. Bấm nút Evidence library",
 "- Documents vẫn có dòng Access control policy (file access-control-policy-v3.pdf)\n- Cột Used for không còn R.1.1.1",
 uc="UC-EVA-05",pre=ADMIN+"; có "+WS+"; evidence Access control policy chỉ gắn R.1.1.1",q=qq(32,31))
case(UL,"Thông báo","Sau khi gỡ","Nội dung thông báo","Low","Kiểm tra thông báo sau khi gỡ evidence",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001\n3. Bấm Unlink from R.1.1.1","",
 uc="UC-EVA-05",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1",q=q(51))
case(UL,"Xác nhận","Hộp thoại","Trước khi gỡ","Medium","Kiểm tra hộp thoại xác nhận khi gỡ evidence",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001\n3. Bấm Unlink from R.1.1.1","",
 uc="UC-EVA-05",pre=ADMIN+"; có "+WS+"; evidence Access control policy gắn R.1.1.1",q=q(31))

# =============== Owner ===============
OW="Chủ sở hữu requirement - Owner"
case(OW,"Ô Owner","Mặc định","Chưa gán owner","Medium","Kiểm tra ô Owner khi requirement chưa có owner",
 OPEN+"\n2. Kiểm tra ô Owner ở chi tiết R.1.1.1",
 "- Chi tiết requirement có ô Owner dạng danh sách chọn, hiển thị Nobody yet",
 uc="UC-EVA-06",pre=ADMIN+"; có "+EMPTY,q=q(33))
case(OW,"","Danh sách","Người có quyền vào scope","High","Kiểm tra danh sách chọn owner",
 OPEN+"\n2. Bấm ô Owner ở chi tiết R.1.1.1",
 "- Danh sách có Linh Tran và Wei Chen (được gán scope [System])\n- Không có Mei Lin (không được gán scope [System])",
 uc="UC-EVA-06",pre=ADMIN+"; có "+EMPTY+"; Linh Tran và Wei Chen được gán scope [System], Mei Lin không được gán",q=q(33))
case(OW,"","","Customer Viewer trong danh sách","Medium","Kiểm tra danh sách chọn owner có người Customer Viewer",
 OPEN+"\n2. Bấm ô Owner ở chi tiết R.1.1.1","",
 uc="UC-EVA-06",pre=ADMIN+"; có "+EMPTY+"; Iris Huang (Customer Viewer) được gán scope [System]",q=qq(34,33))
case(OW,"Gán owner","Gán lần đầu","Chọn một người","High","Kiểm tra gán owner cho requirement",
 OPEN+"\n2. Bấm ô Owner ở chi tiết R.1.1.1\n3. Chọn Linh Tran\n4. Tải lại trang, chọn requirement R.1.1.1 và R.1.1.2",
 "- Ô Owner của R.1.1.1 hiển thị Linh Tran, vẫn hiển thị sau khi tải lại trang\n- Ô Owner của R.1.1.2 vẫn hiển thị Nobody yet",
 uc="UC-EVA-06",pre=ADMIN+"; có "+EMPTY,q=q(33))
case(OW,"","Đổi owner","Chọn người khác","Medium","Kiểm tra đổi owner của requirement",
 OPEN+"\n2. Bấm ô Owner ở chi tiết R.1.1.1\n3. Chọn Wei Chen",
 "- Ô Owner của R.1.1.1 hiển thị Wei Chen thay cho Linh Tran",
 uc="UC-EVA-06",pre=ADMIN+"; có "+EMPTY+"; Linh Tran và Wei Chen đều được gán scope [System]; R.1.1.1 có owner Linh Tran",q=q(33))

case(OW,"","Bỏ owner","Chọn lại Nobody yet","Medium","Kiểm tra bỏ owner của requirement",
 OPEN+"\n2. Bấm ô Owner ở chi tiết R.1.1.1\n3. Chọn bỏ owner","",
 uc="UC-EVA-06",pre=ADMIN+"; có "+EMPTY+"; R.1.1.1 có owner Linh Tran",q=qq(42,33))

case(OW,"","Mất quyền vào scope","Owner bị gỡ khỏi scope","Medium","Kiểm tra ô Owner khi owner bị gỡ quyền vào scope",
 OPEN+"\n2. Kiểm tra ô Owner ở chi tiết R.1.1.1","",
 uc="UC-EVA-06",pre=ADMIN+"; có "+EMPTY+"; R.1.1.1 có owner Linh Tran; Linh Tran đã bị gỡ khỏi scope [System]",q=qq(57,33))

# =============== Requirement theo tier ===============
TI="Requirement theo tier - Effective scope"
case(TI,"Số requirement","Tier Basic","44 requirement","High","Kiểm tra số requirement của workspace Basic",
 "1. Mở chi tiết [Workspace Basic] (màn Workspaces, bấm tên workspace)\n2. Kiểm tra khung tóm tắt và dòng mã của các requirement",
 "- Khung tóm tắt ghi 0 of 44 requirements have their mandatory evidence · not a compliance decision\n- Mọi requirement trong cây có nhãn from Basic",
 uc="UC-WSP-06",pre=ADMIN+"; có [Workspace Basic] Appendix 10 · 2022 · Basic của scope [System], chế độ Assisted, chưa có evidence")
case(TI,"","Tier Medium","61 requirement","High","Kiểm tra số requirement của workspace Medium",
 OPEN+"\n2. Kiểm tra khung tóm tắt",
 "- Khung tóm tắt ghi 0 of 61 requirements have their mandatory evidence · not a compliance decision",
 uc="UC-WSP-06",pre=ADMIN+"; có "+EMPTY)
case(TI,"","Tier High","76 requirement","Medium","Kiểm tra số requirement của workspace High",
 "1. Mở chi tiết [Workspace High] (màn Workspaces, bấm tên workspace)\n2. Kiểm tra khung tóm tắt",
 "- Khung tóm tắt ghi 0 of 76 requirements have their mandatory evidence · not a compliance decision",
 uc="UC-WSP-06",pre=ADMIN+"; có [Workspace High] Appendix 10 · 2022 · High của scope [System], chế độ Assisted, chưa có evidence",q=q(46))
case(TI,"","Requirement retired","Không tính","Medium","Kiểm tra requirement retired không được tính",
 "1. Mở chi tiết [Workspace Retired] (màn Workspaces, bấm tên workspace)\n2. Kiểm tra khung tóm tắt và cây","",
 uc="UC-WSP-06",pre=ADMIN+"; có [Workspace Retired] của framework có một requirement đã retired, chế độ Assisted",q=q(35))

# =============== Workspace Archived ===============
AR="Workspace đã Archive"
ARP="; có [Workspace Archived] đã Archive, R.1.1.1 đã có evidence Access control policy"
ARS="1. Mở chi tiết [Workspace Archived] (màn Workspaces, bấm tên workspace)"
case(AR,"Chỉ đọc","Upload","Nút Upload evidence","High","Kiểm tra workspace Archived có nút Upload evidence",
 ARS+"\n2. Kiểm tra khối Expected evidence","",uc="UC-WSP-04",pre=ADMIN+ARP,q=q(36))
case(AR,"","Link","Nút Link existing evidence","High","Kiểm tra workspace Archived có nút Link existing evidence",
 ARS+"\n2. Kiểm tra khối Expected evidence","",uc="UC-WSP-04",pre=ADMIN+ARP,q=q(36))
case(AR,"","Gỡ liên kết","Unlink from <requirement>","High","Kiểm tra workspace Archived có nút Unlink from <requirement>",
 ARS+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001","",uc="UC-WSP-04",pre=ADMIN+ARP,q=q(36))
case(AR,"","Owner","Ô Owner","High","Kiểm tra workspace Archived có đổi được Owner",
 ARS+"\n2. Bấm ô Owner ở chi tiết R.1.1.1","",uc="UC-WSP-04",pre=ADMIN+ARP,q=qq(36,33))

# =============== Phân quyền ===============
PM="Phân quyền - Permission"
case(PM,"Customer User","Xem","Mở cây và chi tiết","High","Kiểm tra Customer User xem cây requirement và chi tiết",
 OPEN,
 "- Cột trái: khung tóm tắt coverage, ô tìm kiếm, ô lọc trạng thái, các nhóm requirement\n- Cột phải: breadcrumb, tiêu đề, chip trạng thái, mô tả và khối Expected evidence của R.1.1.1",
 uc="UC-EVA-01",pre=CU+" (Wei Chen); được gán scope [System]; có "+WS)
case(PM,"","Upload","Có quyền","High","Kiểm tra Customer User mở được hộp thoại Upload evidence",
 OPEN+"\n2. Bấm nút Upload evidence ở khối Expected evidence",
 "- Hiện hộp thoại Upload evidence",
 uc="UC-EVA-03",pre=CU+" (Wei Chen); được gán scope [System]; có "+WS+"; R.1.1.1 đã có evidence Access control policy")
case(PM,"","Link","Có quyền","High","Kiểm tra Customer User mở được hộp thoại Link existing evidence",
 OPEN+"\n2. Chọn requirement R.1.1.2\n3. Bấm nút Link existing evidence",
 "- Hiện hộp thoại Link existing evidence",
 uc="UC-EVA-04",pre=CU+" (Wei Chen); được gán scope [System]; có "+WS+"; R.1.1.1 đã có evidence Access control policy")
case(PM,"","Gỡ liên kết","Có quyền","High","Kiểm tra Customer User có nút Unlink from <requirement>",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001",
 "- Chân khung chi tiết evidence có nút Unlink from R.1.1.1",
 uc="UC-EVA-05",pre=CU+" (Wei Chen); được gán scope [System]; có "+WS+"; R.1.1.1 đã có evidence Access control policy")
case(PM,"","Owner","Không được gán owner","High","Kiểm tra Customer User không đổi được Owner",
 OPEN+"\n2. Bấm ô Owner ở chi tiết R.1.1.1",
 "- Ô Owner màu xám, không mở được danh sách chọn",
 uc="UC-EVA-06",q=q(56),pre=CU+" (Wei Chen); được gán scope [System]; có "+WS)
case(PM,"","Owner","Thấy owner đã gán","Medium","Kiểm tra Customer User thấy owner đã gán",
 OPEN+"\n2. Kiểm tra ô Owner ở chi tiết R.1.1.1",
 "- Ô Owner hiển thị Linh Tran",
 uc="UC-EVA-02",pre=CU+" (Wei Chen); được gán scope [System]; có "+WS+"; R.1.1.1 có owner Linh Tran",q=q(33))
case(PM,"Customer Viewer","Xem","Mở cây và chi tiết","High","Kiểm tra Customer Viewer xem cây requirement và chi tiết",
 OPEN,
 "- Cột trái: khung tóm tắt coverage, ô tìm kiếm, ô lọc trạng thái, các nhóm requirement\n- Cột phải: breadcrumb, tiêu đề, chip trạng thái, mô tả và khối Expected evidence của R.1.1.1",
 uc="UC-EVA-01",pre=CV+" (Iris Huang); được gán scope [System]; có "+WS)
case(PM,"","Upload, Link","Không có quyền","High","Kiểm tra Customer Viewer không có nút Upload và Link",
 OPEN+"\n2. Kiểm tra khối Expected evidence",
 "- Không có nút Link existing evidence và Upload evidence",
 uc="UC-EVA-03",pre=CV+" (Iris Huang); được gán scope [System]; có "+WS+"; R.1.1.1 đã có evidence")
case(PM,"","Chi tiết evidence","Chỉ tải về","Medium","Kiểm tra Customer Viewer mở chi tiết evidence",
 OPEN+"\n2. Bấm icon mắt ở dòng evidence dưới EE-001",
 "- Khung chi tiết hiển thị đủ thông tin\n- Chân khung chỉ có nút Download, không có Unlink from R.1.1.1 và Upload new version",
 uc="UC-EVC-02",pre=CV+" (Iris Huang); được gán scope [System]; có "+WS+"; R.1.1.1 đã có evidence")
case(PM,"","Owner","Không được gán owner","Medium","Kiểm tra Customer Viewer không đổi được Owner",
 OPEN+"\n2. Bấm ô Owner ở chi tiết R.1.1.1",
 "- Ô Owner màu xám, không mở được danh sách chọn",
 uc="UC-EVA-06",q=q(56),pre=CV+" (Iris Huang); được gán scope [System]; có "+WS)

case(PM,"","Owner","Thấy owner đã gán","Medium","Kiểm tra Customer Viewer thấy owner đã gán",
 OPEN+"\n2. Kiểm tra ô Owner ở chi tiết R.1.1.1",
 "- Ô Owner hiển thị Linh Tran",
 uc="UC-EVA-02",q=q(33),pre=CV+" (Iris Huang); được gán scope [System]; có "+WS+"; R.1.1.1 có owner Linh Tran")

# =============== Bảo mật ===============
SC="Bảo mật - Security"
case(SC,"Phạm vi scope","URL","Workspace của scope không được gán","High","Kiểm tra mở workspace của scope không được gán bằng URL",
 "1. Mở url chi tiết của [Workspace Organization]","- Không hiển thị cây requirement và evidence của [Workspace Organization]",
 uc="UC-EVA-01",pre=CU+" (Wei Chen); được gán scope [System], không được gán scope [Organization]; scope [Organization] đã có workspace [Workspace Organization]",q=q(37))
case(SC,"Dữ liệu nhập","Tên evidence","Chứa mã HTML","Medium","Kiểm tra Name chứa mã HTML",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file ad-inactive-accounts.png\n4. Nhập Name: <img src=x onerror=alert(1)>\n5. Bấm Upload, chờ quét xong",
 "- Dòng evidence hiển thị đúng chuỗi <img src=x onerror=alert(1)> như văn bản\n- Không chạy script, không hiện hộp thoại alert",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)
case(SC,"","Tên file","Chứa mã HTML","Medium","Kiểm tra tên file chứa mã HTML",
 OPEN+"\n2. Bấm nút Upload evidence\n3. Chọn file có tên <b>x</b>.txt\n4. Bấm Upload, chờ quét xong",
 "- Tên file ở dòng evidence và ở khung chi tiết hiển thị đúng chuỗi <b>x</b>.txt như văn bản, không in đậm",
 uc="UC-EVA-03",pre=ADMIN+"; có "+EMPTY)

# =============== xuất ===============
N=lambda s: unicodedata.normalize("NFC",s)
cols=["I","II","III","IV","Pri","Name","Pre","Step","Expected","UC","Wait"]
cur=['']*4
with open('ea_flat.tsv','w',encoding='utf-8',newline='') as f:
    f.write("\t".join(cols)+"\n")
    for c in C:
        for i,k in enumerate(["I","II","III","IV"]):
            if c[k]: cur[i]=c[k]
            c[k]=cur[i]
        f.write("\t".join(N(c[k]).replace("\t"," ").replace("\n","\\n") for k in cols)+"\n")
print(len(C),'blank exp',sum(1 for c in C if not c['Expected']),'with q',sum(1 for c in C if c['Wait']))
unused=[n for n in Q if n not in USED]; print('unused Q',unused)
bad=[c['Name'] for c in C if c['Wait'] and not all(p.strip().count('?')>=1 for p in c['Wait'].split('\n'))]
print('no ?',bad)
