# Câu hỏi làm rõ — SGS DTP MVP Use Case List v2.1

Nguồn: `SGS_DTP_MVP_Use_Case_List_v2_1_final_confirmation.xlsx` · Phân tích: `analysis.md` · Ngày: 2026-09-28

Cách trả lời: ghi ngay vào dòng **Trả lời** của từng câu, hoặc trả lời trong chat theo số câu (vd "Q-01: đồng ý đề xuất"). Chỉ cần xác nhận hoặc sửa phần **Đề xuất mặc định**.

Câu CHẶN chưa được trả lời thì AI không chốt baseline và không bàn giao sang Tester. Câu QUAN TRỌNG và NHỎ chưa trả lời thì AI làm tiếp theo đề xuất mặc định, gắn nhãn [GIẢ ĐỊNH].

| Mức | Số câu | Câu |
|---|---|---|
| CHẶN | 6 | Q-01 → Q-06 |
| QUAN TRỌNG | 9 | Q-07 → Q-15 |
| NHỎ | 3 | Q-16 → Q-18 |

---

## CHẶN

### Q-01 · Phạm vi MVP thật để test
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-11, F-12, F-19
- **Vị trí:** UC List cột H (LTS suggestion), I (SGS Comments), J (ESt); Scope Summary!B2
- **Vấn đề:** Sheet UC List (Scope Summary gọi là MVP) có 159 UC, nhưng chỉ 87 UC có giờ mà không vướng đề xuất nào. Còn lại: 59 UC LTS đề xuất Phase 2 chưa có phản hồi SGS; 2 UC Phase 2 SGS đã đồng ý (AUTH-003/004); 5 UC SGS muốn giữ P1 — OPS-001, CMT-002, CMT-007 đã có giờ, CKP-001, CKP-002 chưa có; 2 UC "move back to P1" chưa có giờ (FWK-003, FWK-013); 3 UC không có đề xuất lẫn giờ (AUD-002, SOA-001, SOA-002). Nếu kéo CKP-001 về P1 thì phải kéo theo JRN-004 và RDN-001.
- **Ảnh hưởng:** chưa biết test UC nào → chưa lập được test plan, phạm vi regression, ước lượng test.
- **Đề xuất mặc định:** Trong phạm vi test = UC có giờ > 0 hoặc LTS ghi "move back to P1" → 93 UC (nhóm A, F, C, D ở `analysis.md` §3). Còn lại coi là Phase 2; riêng AUD-002 chờ Q-13, SOA chờ Q-15. Xác nhận quy tắc này, hoặc gửi danh sách phạm vi đã chốt với SGS.
- **Trả lời:**

### Q-02 · UC-RGF-001 Regulatory Feed: Future hay Phase 1?
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-03
- **Vị trí:** Future Release!R24
- **Vấn đề:** UC nằm trong sheet Future Release, nhưng cột lý do ghi "Q&A #58 confirms inclusion in Phase 1". Dòng này còn bị lệch cột: cột Description chứa "Customer Portal", cột WBS chứa mô tả, cột Portal trống.
- **Ảnh hưởng:** nếu thuộc Phase 1 thì MVP đang thiếu một chức năng, chưa có ước lượng và chưa có UC liên quan nào trong sheet MVP.
- **Đề xuất mặc định:** theo vị trí sheet — Future Release, ngoài phạm vi test — cho đến khi có xác nhận.
- **Trả lời:**

### Q-03 · Ma trận phân quyền và danh sách vai trò
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-32
- **Vị trí:** UC-ROL-001, UC-ROL-002 (UC List!R21–R22); ghi chú FRD 4.3 ở UC-ROL-003..005
- **Vấn đề:** ROL-001 (36 giờ, UC lớn nhất) thực thi "the predefined role and permission matrix" trên API và UI, nhưng ma trận không có trong tài liệu. Ghi chú FRD 4.3 nói mô hình 7 vai trò, trong khi danh sách UC có 8: Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant.
- **Ảnh hưởng:** không có ma trận thì không có kết quả mong đợi cho test phân quyền — loại test quan trọng nhất của hệ thống nhiều tenant — và không biết cần bao nhiêu tài khoản test.
- **Đề xuất mặc định:** gửi ma trận phân quyền (CP-03 / PRD). Trong lúc chờ, dùng ma trận sơ bộ suy từ cột Actor (`analysis.md` Phụ lục A), gắn nhãn [GIẢ ĐỊNH], và coi là 8 vai trò.
- **Trả lời:**

### Q-04 · Mô hình trạng thái của Review
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-28
- **Vị trí:** UC-REV-001, 005, 008, 015, 016 (UC List!R138, R142, R145, R150, R151)
- **Vấn đề:** chưa có (a) danh sách trạng thái của từng requirement/control trong review (REV-005); (b) quy tắc suy ra trạng thái tổng từ trạng thái item (REV-016); (c) thế nào là "completed" để đủ điều kiện đóng (REV-015); (d) các giá trị phân loại finding (REV-008); (e) vai trò nào được tạo loại review nào, và "review-context separation" (A2 ở REV-001) nghĩa là ai không được thấy gì.
- **Ảnh hưởng:** module có 14 UC, 121 giờ; thiếu mô hình trạng thái thì không viết được kết quả mong đợi cho hầu hết test của module.
- **Đề xuất mặc định:** gửi biên bản Q&A #26 (khách đã xác nhận cơ chế này). Nếu chưa có văn bản, AI soạn một mô hình trạng thái mẫu để bạn và SGS sửa.
- **Trả lời:**

### Q-05 · Trạng thái bằng chứng và cách nộp bằng chứng cho review
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-20, F-29, F-36
- **Vị trí:** UC-EVD-014, 015, 019 (UC List!R103, R104, R106); Future Release: EVD-017/018, REV-009/010
- **Vấn đề:** EVD-014 cho Customer Admin/User cập nhật bằng chứng qua các trạng thái draft, submitted for review, reviewed, rejected, accepted, archived — trong đó reviewed/accepted/rejected nghe như việc của SGS; chưa có bảng chuyển trạng thái; ghi chú ở EVD-019 cho thấy việc archive thuộc CP-20 phần P2. Evidence Package (EVD-017/018) và Accept/Reject Package (REV-009/010) là Future, nên chưa rõ trạng thái bằng chứng liên hệ thế nào với trạng thái item trong review (REV-005). EVD-015 xóa "where retention policy permits" nhưng chưa có chính sách; chưa rõ có xóa được bằng chứng đang được map hoặc đang nằm trong review chưa đóng không.
- **Ảnh hưởng:** không test được EVD-014, EVD-015 và phần giao giữa Evidence và Review.
- **Đề xuất mặc định:** khách chỉ chuyển draft ↔ submitted for review; reviewed/accepted/rejected do SGS đặt thông qua review; archived thuộc Phase 2; không xóa được bằng chứng đang có mapping hoặc đang trong review chưa đóng.
- **Trả lời:**

### Q-06 · Mô hình trạng thái của Service Request
- **Mức:** CHẶN · **Trạng thái:** Mở · **Phát hiện:** F-30, F-36
- **Vị trí:** UC-SRQ-001, 004, 005, 006, 007, 008, 009 (UC List!R127–R135)
- **Vấn đề:** các UC nhắc tới accept/reject (SRQ-005), information requested (SRQ-009), in progress và closed (SRQ-007), hủy (SRQ-004 — WBS ghi hủy không có trong tập trạng thái CP-35), nhưng chưa có trạng thái khởi tạo, bảng chuyển, và "before SGS delivery begins" ứng với trạng thái nào. Danh mục loại yêu cầu còn mở (Q&A #33). SGS Consultant được giao yêu cầu tư vấn (SRQ-006) nhưng không có trong actor của SRQ-007/008/009; SRQ-009 cũng thiếu SGS Auditor/Certification so với SRQ-007/008.
- **Ảnh hưởng:** không test được luồng Service Request (10 UC, 81 giờ), phân quyền theo loại yêu cầu và thông báo đổi trạng thái.
- **Đề xuất mặc định:** Submitted → Accepted hoặc Rejected → In Progress (có thể qua Information Requested rồi quay lại) → Closed; khách hủy được khi Submitted hoặc Accepted; Consultant chỉ xem. Kèm danh sách category khi Q&A #33 chốt.
- **Trả lời:**

---

## QUAN TRỌNG

### Q-07 · Đưa framework vào hệ thống
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-13, F-24, F-35
- **Vị trí:** UC-FWK-003, 005, 006, 007, 008, 009, 013 (UC List!R37–R44)
- **Vấn đề:** FWK-003 (tạo) và FWK-013 (kích hoạt) đã "move back to P1" nhưng chưa có giờ. SGS yêu cầu hỗ trợ ban đầu "ISO27001, ISO42001 and CMS" — chưa rõ "CMS" là framework nào. Sửa requirement/control (FWK-006) là P2 trong khi tạo (FWK-005) và retire (FWK-007) thuộc MVP. FWK-008: SGS hỏi "What are the types of evidences? Files?" và gợi ý lùi P2, chưa có trả lời.
- **Ảnh hưởng:** framework là dữ liệu tiền đề của toàn bộ Evidence và Review → quyết định cách chuẩn bị dữ liệu test.
- **Đề xuất mặc định:** MVP có 3 framework (ISO 27001, ISO 42001 và "CMS" — chờ tên đầy đủ); cách chính là import XLSX (FWK-009); sửa nội dung bằng cách import lại; loại bằng chứng mong đợi là mô tả dạng văn bản, không ràng buộc định dạng file.
- **Trả lời:**

### Q-08 · Thuật ngữ gắn framework, chu kỳ chứng nhận, gỡ và xóa scope
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-23, F-26, F-27
- **Vị trí:** UC-SCP-005, 006, 007 (R77–R79), EVD-001, 002 (R91–R92), FWK-013 (R44); Future Release!R29 (DSC-005)
- **Vấn đề:** có bốn cách gọi: "Link Framework to Scope" (SCP-006, kích hoạt tạo workspace), "framework is activated on a scope" (EVD-002), "Activate Framework" ở cấp nền tảng (FWK-013), "Activate Recommended Frameworks" / CP-12 (DSC-005, Future). "Certification cycle" dùng để chặn trùng workspace nhưng không được định nghĩa, và không UC nào trong MVP bắt đầu chu kỳ mới. SCP-007 gỡ framework khỏi scope nhưng không nói workspace ra sao. Không có UC xóa scope; Archive Scope (SCP-005) là P2.
- **Ảnh hưởng:** không viết được test chống tạo trùng workspace, test gỡ framework, và không có cách dọn dữ liệu test scope.
- **Đề xuất mặc định:** "link" ở SCP-006 chính là "activated on a scope" ở EVD-002; FWK-013 là điều kiện để framework xuất hiện trong danh sách chọn ở SCP-006; MVP chỉ có một chu kỳ cho mỗi scope + framework; gỡ framework thì workspace chuyển sang archived như EVD-019; không xóa được scope trong MVP.
- **Trả lời:**

### Q-09 · Bản ghi chứng nhận trong MVP
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-04, F-16
- **Vị trí:** UC-CRT-001..003 (R153–R155), CMT-001..007 (R157–R163), SCH-004, SCH-006 (R50, R52)
- **Vấn đề:** CRT-001 tạo bản ghi "using the configured certification fields" nhưng cấu hình trường (SCH-004) là P2. Sửa bản ghi (CRT-002) và mọi chuyển trạng thái vòng đời (CMT-001, 003, 004, 005, 006) đều P2, nên trạng thái đứng yên và không tự hết hạn, trong khi CRT-003 hiển thị status và expiry. CMT-002 và CMT-007 cùng tên, mô tả gần giống, mỗi UC 5 giờ; CMT-007 dựa trên "scheme's configured offsets" (SCH-006, P2).
- **Ảnh hưởng:** xác định test gì cho chứng nhận và thông báo mốc; nghi tính giờ hai lần.
- **Đề xuất mặc định:** bộ trường cố định trong code (cần danh sách trường); nhập sai thì xử lý ngoài hệ thống; CMT-002 và CMT-007 là một chức năng; các mốc thông báo là giá trị cố định (cần số ngày cụ thể).
- **Trả lời:**

### Q-10 · Customer User và Customer Viewer thấy những gì
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-31
- **Vị trí:** UC-USR-006 (R15), EVD-006 (R96), REV-011 (R146), CRT-003 (R155)
- **Vấn đề:** EVD-006 cho xem "all evidence held by the organization", trong khi USR-006 giới hạn Customer User theo scope được gán và REV-011 ghi "assigned scope". Trong phạm vi đề xuất, Customer Viewer chỉ có ở CRT-003 và các UC dành cho mọi vai trò (đăng nhập, thông báo).
- **Ảnh hưởng:** kết quả mong đợi của mọi màn hình danh sách phía khách hàng.
- **Đề xuất mặc định:** Customer User chỉ thấy dữ liệu thuộc scope được gán ở mọi màn hình, kể cả Evidence Library; Customer Viewer trong MVP chỉ đăng nhập, xem thông báo và danh sách chứng nhận.
- **Trả lời:**

### Q-11 · Màn hình MVP hiển thị dữ liệu của tính năng Phase 2
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-15, F-17, F-18
- **Vị trí:** UC-EVD-004, 005, 007 (R94, R95, R97), EVD-020 (R107), CNS-001 (R176), RDN-004, RDN-005 (R116–R117)
- **Vấn đề:** EVD-004, EVD-005, EVD-007 hiển thị declaration state, maturity declaration, gap flags, freshness — do ASM-001/002, RDN-002/003, CFG-002 tạo ra, đều P2. Consultant làm "Gap Analysis" (EVD-020, CNS-001) nhưng Gap List (RDN-005) là P2. RDN-004 (readiness overview) được khách xác nhận qua Q&A #23 nhưng LTS đề xuất P2 và SGS chưa phản hồi.
- **Ảnh hưởng:** không biết các trường này bị ẩn, để trống hay tính theo quy tắc đơn giản; ảnh hưởng mọi test của Evidence Management.
- **Đề xuất mặc định:** ẩn các trường này trong MVP; Gap Analysis của Consultant chỉ bằng bình luận (CNS-001); RDN-004 theo quyết định ở Q-01.
- **Trả lời:**

### Q-12 · Consultant trên Marketplace và Consultant được giao
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-34
- **Vị trí:** UC-ACC-006 (R64), SRQ-001 (R127), SRQ-006 (R132), MKT-004..006 (R182–R184)
- **Vấn đề:** hồ sơ Consultant trên Marketplace là nội dung do SGS Admin quản lý (MKT-006); chưa rõ mỗi hồ sơ có gắn với một tài khoản vai trò SGS Consultant không. ACC-006 cho tối đa một Consultant active mỗi khách hàng; chưa rõ xử lý khi khách chọn Consultant B qua Marketplace (MKT-005 → SRQ-001) trong lúc Consultant A đang active.
- **Ảnh hưởng:** test luồng Marketplace → Service Request → phân công, và quyền nhìn dữ liệu của Consultant.
- **Đề xuất mặc định:** mỗi hồ sơ Marketplace gắn một tài khoản SGS Consultant; lựa chọn của khách chỉ là gợi ý, SGS quyết định ở SRQ-006; khi SGS giao B thì A hết active.
- **Trả lời:**

### Q-13 · Sự kiện thông báo, sự kiện audit và cách kiểm chứng audit
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-14, F-36, F-37
- **Vị trí:** UC-NTF-001 (R27), AUD-001, 002, 004 (R31–R33)
- **Vấn đề:** NTF-001 liệt kê sự kiện bằng "such as"; người nhận từng loại chưa rõ. AUD-001 ghi "sensitive … actions" mà không liệt kê. AUD-002 (SGS Admin tra cứu audit) chỉ có ghi chú SGS "Phase 2?", không có giờ — nếu là P2 thì MVP không có màn hình để SGS xem audit.
- **Ảnh hưởng:** không có danh sách thì không xác định được đủ test; không có màn hình thì Playwright không kiểm chứng được AUD-001 qua UI.
- **Đề xuất mặc định:** AUD-002 thuộc Phase 2; AUD-001 được kiểm chứng qua API hoặc DB (cần quyền truy cập môi trường test) và phần hiển thị trong AUD-004. Xin bảng: sự kiện → người nhận → nội dung thông báo, và danh sách hành động được audit.
- **Trả lời:**

### Q-14 · Trạng thái mặc định của tài khoản và vòng đời người dùng
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-21, F-22, F-33
- **Vị trí:** UC-AUTH-003..005 (R6–R8), USR-004, 008, 009, 010 (R13, R17–R19), ACC-003, 007, 008 (R61, R65, R66)
- **Vấn đề:** tạo tài khoản khách (ACC-003) thuộc MVP nhưng kích hoạt (ACC-008) là P2 → tài khoản mới tạo có active ngay không? AUTH-005 chỉ liệt kê 4 vai trò kích hoạt qua lời mời (thiếu Customer Viewer, SGS Admin, SGS Trainer/Assessor, SGS Auditor/Certification). MVP không có sửa, vô hiệu hóa, xóa người dùng (USR-004/008/009; USR-009 còn trống mô tả). SGS đã chấp nhận hỗ trợ thủ công cho mật khẩu nhưng chưa có ý kiến về thu hồi quyền truy cập.
- **Ảnh hưởng:** tiền điều kiện của mọi test đăng nhập và phân quyền; rủi ro bảo mật (người nghỉ việc vẫn đăng nhập được) cần được chấp nhận rõ.
- **Đề xuất mặc định:** tài khoản active ngay khi tạo; mọi vai trò kích hoạt qua lời mời; thu hồi quyền truy cập do đội vận hành xử lý thủ công, cần SGS xác nhận bằng văn bản.
- **Trả lời:**

### Q-15 · Statement of Applicability có thuộc MVP không
- **Mức:** QUAN TRỌNG · **Trạng thái:** Mở · **Phát hiện:** F-10, F-14
- **Vị trí:** UC-SOA-001, SOA-002 (UC List!R186–R187)
- **Vấn đề:** SOA nằm trong sheet MVP nhưng không có WBS, ước lượng, đề xuất hay ý kiến; section 30 không được cộng vào tổng giờ (J2). Nếu có, SOA quyết định "applicable" trong REV-005 và REV-015, và trùng khái niệm "N/A" với khai báo maturity (ASM-001, P2). SOA-002 ghi "SGS Auditor" thay vì "SGS Auditor/Certification" và không có SGS User, SGS Trainer/Assessor.
- **Ảnh hưởng:** định nghĩa "applicable" trong review; phạm vi test.
- **Đề xuất mặc định:** SOA thuộc MVP (UC mới được thêm vào sheet MVP) và là nguồn duy nhất xác định applicability; chờ ước lượng; "SGS Auditor" hiểu là SGS Auditor/Certification.
- **Trả lời:**

---

## NHỎ

### Q-16 · Sửa lỗi dữ liệu trong file nguồn
- **Mức:** NHỎ · **Trạng thái:** Mở · **Phát hiện:** F-01, F-02, F-05, F-06, F-07, F-08, F-09
- **Vị trí:** Scope Summary!B2:B3; UC List!J2, R18, R123, R125, R182–R183
- **Vấn đề:** Scope Summary lệch số (156/39 so với thực tế 159/40); J2 không cộng section 30; tên MKT-005 là actor và tên MKT-004 không khớp mô tả; actor của TRN-006 là "rket"; USR-009 trống mô tả; TRN-009 có khoảng trắng trong ID, thiếu WBS, tên module khác nhóm; không có UC-AUD-003 và section 24.
- **Ảnh hưởng:** ID và tên sai sẽ đi vào test case và tag Playwright; số liệu sai làm lệch báo cáo phạm vi.
- **Đề xuất mặc định:** trong baseline AI dùng giá trị đã sửa: MKT-004 = "View Consultant List", MKT-005 = "View Consultant Details"; actor TRN-006 = "Customer Admin, Customer User" (giống TRN-001/002); ID TRN-009 bỏ khoảng trắng; AUD-003 và section 24 coi là đã bỏ. Nhờ bạn báo người giữ file sửa bản gốc.
- **Trả lời:**

### Q-17 · Luồng quản trị còn thiếu
- **Mức:** NHỎ · **Trạng thái:** Mở · **Phát hiện:** F-25
- **Vị trí:** UC-TRN-009 (R125), MKT-006 (R184)
- **Vấn đề:** không có UC quản trị catalogue đào tạo tại chỗ (TRN-009) và chưa rõ "tracks" theo dõi gì. MKT-006 gộp năm thao tác (tạo, sửa, kích hoạt, vô hiệu hóa, xóa) trong một UC; chưa rõ xóa hồ sơ Consultant đang được Service Request tham chiếu thì sao.
- **Ảnh hưởng:** không biết dữ liệu test cho TRN-009 đến từ đâu; một UC gộp nhiều thao tác khó truy vết test.
- **Đề xuất mặc định:** catalogue đào tạo tại chỗ do đội triển khai nạp sẵn, "tracks" chỉ là hiển thị; xóa hồ sơ đã được tham chiếu là ẩn mềm. [ĐỀ XUẤT] tách MKT-006 thành các UC con khi viết UC spec.
- **Trả lời:**

### Q-18 · Môi trường và dữ liệu test
- **Mức:** NHỎ · **Trạng thái:** Mở · **Phát hiện:** F-38, F-39, F-40
- **Vị trí:** UC-TRN-001/002 (R119–R120), CMT-002/007 (R158, R163), MKT-002/004 (R180, R182), ACC-005 (R63)
- **Vấn đề:** TRN-001/002 gọi Academy API bên ngoài; CMT-002/007 là job chạy theo thời gian; dữ liệu Pentesting và Consultant do SGS Taiwan cung cấp; test ranh giới affiliate cần ít nhất hai affiliate.
- **Ảnh hưởng:** thiếu các điều kiện này thì một phần test không chạy tự động được.
- **Đề xuất mặc định:** có sandbox hoặc mock Academy API ở phía backend (API gọi từ server thì Playwright không chặn được bằng `page.route`); có endpoint hoặc lệnh kích hoạt job trong môi trường test; môi trường test có ít nhất hai affiliate; cần nội dung chính xác của thông báo khi catalogue không khả dụng (TRN-001).
- **Trả lời:**
