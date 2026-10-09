# Phân tích BA — SGS DTP MVP Use Case List v2.1

> **Trạng thái: BẢN NHÁP — chưa chốt baseline.** Đang dừng ở cổng duyệt cuối bước 3, chờ trả lời 6 câu CHẶN trong `questions.md`.

| | |
|---|---|
| Nguồn | `SGS_DTP_MVP_Use_Case_List_v2_1_final_confirmation.xlsx` (51 KB, 5 sheet) |
| Quy trình | skill `ba-analysis` v0.1 — chế độ A (phân tích mới) · rule `common` + `ba` v0.1 |
| Ngày | 2026-09-28 |
| Đi kèm | `uc-inventory.md` (lượt 1 — trích xuất nguyên văn 204 UC) · `questions.md` (18 câu hỏi) |

## 1. Kiểm kê nguồn (bước 0)

**Đã đọc:** 5 sheet — Scope Summary, UC List, Future Release, OOS - Not MVP, Pending Clarification — đều hiển thị. Không có sheet, hàng hay cột ẩn; không có comment, hình, biểu đồ, ô gộp hay data validation. Sheet UC List có 27 công thức ở cột J (giờ theo section và tổng chung). Sheet Pending Clarification không có UC.

**Độ phủ chiều ngược:** 1.767/1.767 ô có dữ liệu trong file gốc xuất hiện nguyên văn trong `uc-inventory.md` (script tự kiểm).

**Loại tài liệu:** danh sách UC — mỗi UC một dòng mô tả. Không có luồng chính/thay thế/ngoại lệ, business rule, trường dữ liệu hay text giao diện. Vì vậy lần phân tích này dừng ở mức phạm vi, vai trò, phụ thuộc và nhất quán. Muốn xuất test basis cho Tester (nhất là phần Validation) cần UC spec hoặc đặc tả màn hình của từng UC.

**Được dẫn chiếu nhưng không có trong input** [CHƯA KIỂM CHỨNG]:
- Presale WBS / estimation: mã CP-01 → CP-50 (không có CP-46), OPS-04 → OPS-23, A1–A5, A8, A9, B3
- PRD (RL-07, CC-16, RD-14, NFR-UX-02, NFR-PRV-03/04, NFR-MNT-03) và FRD (assumption 4.3)
- Q&A tracker: #7, #8, #10, #12–14, #16, #18–21, #23–26, #33, #34, #36, #38–41, #45, #47, #54, #56, #58, #59a, #59f, #59g
- Xác nhận của Xavier ngày 10-Sep-2026 về Marketplace

Mọi kết luận dựa vào các mã trên mới chỉ dựa trên dòng ghi chú trong file, chưa đối chiếu tài liệu gốc.

## 2. Đối soát số liệu

| Hạng mục | Scope Summary ghi | Đếm lại | Lệch |
|---|---|---|---|
| MVP UC List | 156 | 159 | +3 |
| Future Release | 39 | 40 | +1 |
| OOS / Not MVP | 5 | 5 | +0 |
| Pending Clarification | 0 | 0 | 0 |
| **Tổng** | **200** | **204** | **+4** |

Tổng giờ: 834 giờ trên 91 UC có giờ. Công thức J2 không cộng section 30 (F-02).

## 3. Phân loại phạm vi

Quy tắc phân nhóm suy ra từ ba cột LTS suggestion, SGS Comments và ESt (Hour) của sheet UC List:

| Nhóm | Số UC | UC | Xử lý test đề xuất [GIẢ ĐỊNH – chờ Q-01] |
|---|---|---|---|
| A — có giờ, LTS không đề xuất lùi | 87 | 87 UC — xem uc-inventory.md | Trong phạm vi |
| F — có giờ, SGS gợi ý có thể lùi P2 | 1 | FWK-008 | Trong phạm vi |
| C — LTS đề xuất P2, SGS muốn giữ P1, đã có giờ | 3 | CMT-002, CMT-007, OPS-001 | Trong phạm vi |
| D — LTS ghi 'move back to P1', chưa có giờ | 2 | FWK-003, FWK-013 | Trong phạm vi |
| B2 — LTS đề xuất P2, SGS muốn giữ P1, chưa có giờ | 2 | CKP-001, CKP-002 | Ngoài phạm vi đến khi chốt |
| B1 — LTS đề xuất P2, SGS đồng ý | 2 | AUTH-003, AUTH-004 | Ngoài phạm vi |
| B3 — LTS đề xuất P2, SGS chưa phản hồi | 59 | USR-004, USR-007, USR-008, USR-009, USR-010, ROL-003, ROL-004, ROL-005, NTF-003, FWK-006, FWK-014, SCH-001, SCH-002, SCH-003, SCH-004, SCH-005, SCH-006, SCH-007, SCH-008, CFG-001, CFG-002, ACC-008, ACC-009, ACC-010, ORG-001, ORG-002, SCP-005, SCP-008, CKP-003, JRN-001, JRN-002, JRN-003, JRN-004, ASM-001, ASM-002, ASM-003, RDN-001, RDN-002, RDN-003, RDN-004, RDN-005, TRN-004, TRN-005, TRN-006, TRN-008, CRT-002, CMT-001, CMT-003, CMT-004, CMT-005, CMT-006, PSP-001, PSP-002, PSP-003, PSP-004, PSP-005, PSP-007, OPS-002, OPS-003 | Ngoài phạm vi |
| E — không có đề xuất, không có giờ | 3 | AUD-002, SOA-001, SOA-002 | Chưa xác định (Q-13, Q-15) |
| **Tổng** | **159** | | **Trong phạm vi: 93** |

**Đề xuất phạm vi test = A + F + C + D = 93 UC** (92 chức năng nếu CMT-002 và CMT-007 là một). Đây là [GIẢ ĐỊNH] chờ Q-01.

Theo section:

| Section | Tổng UC | Trong phạm vi đề xuất | Ngoài / chưa xác định |
|---|---|---|---|
| 1. Authentication | 5 | 3 | 2 |
| 2. User & Profile Management | 10 | 5 | 5 |
| 3. Role & Permission Administration | 5 | 2 | 3 |
| 5. Notification | 3 | 2 | 1 |
| 6. Audit Trail | 3 | 2 | 1 |
| 7. Framework Content Management | 11 | 9 | 2 |
| 8. Certification Configuration | 8 | 0 | 8 |
| 10. Platform & Tenant Configuration | 2 | 0 | 2 |
| 11. Customer Account Administration | 10 | 7 | 3 |
| 12. Organization Profile Management | 2 | 0 | 2 |
| 13. Scope Management | 8 | 6 | 2 |
| 14. Customer Cockpit | 3 | 0 | 3 |
| 15. Customer Journey | 4 | 0 | 4 |
| 17. Evidence Management | 17 | 17 | 0 |
| 18. Self-Assessment & Maturity Declaration | 3 | 0 | 3 |
| 19. Readiness Indicators | 5 | 0 | 5 |
| 20. Training & SGS Academy | 7 | 3 | 4 |
| 21. Service Request | 10 | 10 | 0 |
| 22. Review Workflow | 14 | 14 | 0 |
| 23. Certification Record Management | 3 | 2 | 1 |
| 25. Certification Maintenance | 7 | 2 | 5 |
| 26. Digital Trust Passport & External Sharing | 6 | 0 | 6 |
| 27. Operations Monitoring & Reporting | 3 | 1 | 2 |
| 28. Consulting Services | 2 | 2 | 0 |
| 29. DT Marketplace | 6 | 6 | 0 |
| 30. Statement of Applicability | 2 | 0 | 2 |

Chín section hoàn toàn nằm ngoài phạm vi đề xuất: 8, 10, 12, 14, 15, 18, 19, 26, 30. Ba module Evidence Management, Service Request và Review Workflow chiếm 41 UC và 337/834 giờ — đây là trọng tâm test của MVP.

## 4. Read-back — cách AI đang hiểu MVP

Bạn đọc phần này trước. Checklist chỉ bắt được chỗ AI biết là mình chưa rõ; chỗ AI hiểu lệch chỉ lộ ra khi bạn đọc lại cách nó hiểu. Phần dưới chỉ tính 93 UC trong phạm vi đề xuất.

DTP có hai cổng: Customer Portal cho khách hàng và SGS Portal cho nhân sự SGS; MVP dành cho Đài Loan. Luồng nghiệp vụ chính:

1. **Khởi tạo khách hàng (SGS Admin).** Tạo tài khoản khách và tenant (ACC-003), gắn với một affiliate SGS — affiliate giới hạn toàn bộ quyền nhìn thấy phía SGS (ACC-005). Phân công nhân sự SGS, mỗi khách tối đa một Consultant active (ACC-006). Mời Customer Admin đầu tiên (ACC-007).
2. **Chuẩn bị framework (SGS Admin).** Đưa nội dung ISO 27001/42001 vào bằng import XLSX (FWK-009) hoặc tạo tay (FWK-003, FWK-005), khai báo loại bằng chứng mong đợi cho từng control (FWK-008), rồi kích hoạt framework (FWK-013). Mỗi framework độc lập, không có ánh xạ chéo.
3. **Khách hàng tự thiết lập (Customer Admin).** Kích hoạt tài khoản từ lời mời (AUTH-005); tạo người dùng, gán vai trò, gán scope cho Customer User (USR-003/005/006); tạo scope tổ chức, sản phẩm hoặc hệ thống (SCP-003); gắn framework vào scope (SCP-006) → hệ thống tự tạo Evidence Workspace, mỗi scope + framework chỉ một workspace trong một chu kỳ chứng nhận (EVD-002).
4. **Chuẩn bị bằng chứng (Customer Admin, Customer User).** Duyệt control (EVD-004/005), upload và map bằng chứng vào control (EVD-008/011), thay phiên bản (EVD-013), cập nhật trạng thái (EVD-014). Chỉ Customer Admin được xóa bằng chứng, gán owner, lưu trữ workspace (EVD-015/016/019). SGS Trainer/Assessor, Auditor/Certification và Consultant xem bằng chứng của khách được giao (EVD-020). Consultant để lại bình luận mà khách thấy được nhưng không trả lời được (CNS-001/002).
5. **Yêu cầu dịch vụ.** Khách gửi yêu cầu (SRQ-001) từ Evidence Management (tự điền scope/framework) hoặc từ hồ sơ Consultant trên Marketplace (MKT-005). SGS User tiếp nhận hoặc từ chối (SRQ-005); SGS Admin/User phân công (SRQ-006); hai bên trao đổi thông tin (SRQ-009/010); SGS chuyển sang in progress rồi closed (SRQ-007). Khách hủy được trước khi SGS bắt đầu (SRQ-004).
6. **Review.** Chỉ SGS tạo review, gồm hai loại: Readiness Assessment Review và Audit Review (REV-001). Phân công reviewer (REV-002) → reviewer (Trainer/Assessor hoặc Auditor/Certification) cập nhật trạng thái từng requirement/control, bình luận, yêu cầu bổ sung, ghi finding (REV-005..008) → khách xem, phản hồi, nộp hành động khắc phục (REV-011..013) → reviewer đánh giá (REV-014) → hệ thống suy ra trạng thái tổng (REV-016) → reviewer đóng review thủ công (REV-015).
7. **Chứng nhận.** SGS User tạo bản ghi chứng nhận thủ công (CRT-001); khách và SGS xem danh sách (CRT-003). Trong MVP không sửa bản ghi và không đổi trạng thái vòng đời. Thông báo mốc gia hạn/giám sát (CMT-002/007) và dashboard vận hành SGS (OPS-001) chỉ có nếu nhóm C được chốt.
8. **Xuyên suốt.** Phân quyền theo vai trò + tenant + affiliate + phân công (ROL-001); thông báo trong ứng dụng (NTF-001/002), không có email; audit log (AUD-001); Customer Admin xem nhật ký hoạt động của tổ chức (AUD-004).
9. **Phụ.** Xem catalogue SGS Academy (TRN-001/002) — đăng ký khóa học và badge đều ngoài MVP; catalogue đào tạo tại chỗ (TRN-009); Marketplace gồm dịch vụ pentest (chỉ hiển thị thông tin nhà cung cấp) và hồ sơ Consultant, nội dung do SGS Admin quản lý (MKT-001..006).

**Vai trò (tóm tắt Phụ lục A).** Customer Admin làm hầu hết việc phía khách. Customer User làm việc với bằng chứng, yêu cầu dịch vụ và review, nhưng không quản trị người dùng, scope hay xóa bằng chứng. **Customer Viewer chỉ đăng nhập, xem thông báo và danh sách chứng nhận.** SGS Admin quản trị khách hàng, framework và Marketplace. SGS User tiếp nhận yêu cầu, tạo review và bản ghi chứng nhận. SGS Trainer/Assessor và Auditor/Certification thực hiện review. SGS Consultant chỉ xem khách được giao và bình luận.

**Ngoài MVP theo đề xuất:** Regulatory Discovery, Customer Journey, Customer Cockpit, Readiness Indicators, Self-Assessment, Digital Trust Passport và chia sẻ ra ngoài, cấu hình scheme chứng nhận, cấu hình nền tảng, hồ sơ tổ chức, kiểm soát xung đột lợi ích (COI), Evidence Package, bulk upload, ánh xạ chéo framework, SSO.

## 5. Phát hiện đối soát (lượt 2)

40 phát hiện, gom thành 18 câu hỏi trong `questions.md`. Cột Câu hỏi cho biết phát hiện được xử lý ở câu nào. Sáu lỗi dữ liệu (F-03, F-05 → F-08, F-10) được script trích xuất tự bắt; phần còn lại từ đối soát liên UC.

| ID | Loại | Vị trí | Phát hiện | Câu hỏi |
|---|---|---|---|---|
| F-01 | Số liệu | Scope Summary!B2:B3 | Scope Summary ghi 156 UC MVP và 39 UC Future Release; đếm thực tế là 159 (sheet UC List) và 40 (sheet Future Release). OOS khớp (5). | Q-16 |
| F-02 | Số liệu | UC List!J2, R185 | Công thức tổng giờ J2 không cộng dòng section 30 (R185). Hiện section 30 bằng 0 nên tổng 834 giờ (91 UC có giờ) vẫn đúng, nhưng giờ của SOA sẽ bị bỏ sót khi được ước lượng. | Q-16 |
| F-03 | Lỗi dữ liệu · Phạm vi | Future Release!R24 | UC-RGF-001 bị lệch cột (Description chứa 'Customer Portal', cột WBS chứa mô tả, cột lý do chứa WBS, cột Portal trống) và mâu thuẫn phạm vi: nằm trong Future Release nhưng lý do ghi Q&A #58 xác nhận đưa vào Phase 1. | Q-02 |
| F-04 | Lỗi dữ liệu | UC List!R158, R163 | CMT-002 và CMT-007 cùng tên 'Generate Certification Milestone Notification', mô tả gần giống, mỗi UC 5 giờ → nghi trùng chức năng và tính giờ hai lần. | Q-09 |
| F-05 | Lỗi dữ liệu | UC List!R182–R183 | MKT-005 có tên UC là 'Customer Admin, Customer User' (chép nhầm actor). MKT-004 tên 'View Consultant Details' nhưng mô tả là xem danh sách Consultant → nhiều khả năng MKT-004 là danh sách, MKT-005 là chi tiết. | Q-16 |
| F-06 | Lỗi dữ liệu | UC List!R123 | TRN-006 có Actor là 'rket'. | Q-16 |
| F-07 | Lỗi dữ liệu | UC List!R18 | USR-009 (Delete User Account) không có mô tả. | Q-16 |
| F-08 | Lỗi dữ liệu | UC List!R125 | TRN-009 có khoảng trắng cuối ID, không có WBS Reference, module ghi 'Training & SGS Academy' trong khi các UC cùng section ghi 'SGS Academy'. | Q-16 |
| F-09 | Lỗi dữ liệu | Toàn file | Không có UC-AUD-003 ở cả ba sheet; không có section 24 (đánh số nhảy từ 23 sang 25). | Q-16 |
| F-10 | Lỗi dữ liệu | UC List!R187 | SOA-002 ghi vai trò 'SGS Auditor' thay vì 'SGS Auditor/Certification'. | Q-15 |
| F-11 | Phạm vi | UC List cột H–J | 66/159 UC trong sheet MVP được LTS đề xuất Phase 2: 59 chưa có phản hồi SGS (B3), 2 SGS đồng ý (B1), 5 SGS muốn giữ P1 (B2, C). 55 UC trong số đó có WBS ghi P1. Tên file là 'final confirmation' nhưng phạm vi chưa chốt. | Q-01 |
| F-12 | Phạm vi | UC List!R82–R83, R158, R163, R172 | Các UC có ý kiến SGS 'Suggest to be included in P1' được xử lý không đồng nhất: OPS-001, CMT-002, CMT-007 đã có giờ; CKP-001, CKP-002 chưa có. | Q-01 |
| F-13 | Phạm vi | UC List!R37, R44 | FWK-003 và FWK-013 được LTS ghi 'move back to P1' theo yêu cầu SGS nhưng chưa có giờ. | Q-07 |
| F-14 | Phạm vi | UC List!R32, R186–R187 | AUD-002 chỉ có ghi chú SGS 'Phase 2?'; SOA-001, SOA-002 không có WBS, đề xuất, ý kiến hay giờ → chưa xác định thuộc phạm vi nào. | Q-13, Q-15 |
| F-15 | Phạm vi | UC List!R116 | RDN-004 (readiness overview) được khách xác nhận qua Q&A #23, nhưng LTS đề xuất P2 và SGS chưa phản hồi. | Q-11 |
| F-16 | Phụ thuộc | UC List!R50, R52, R153–R163 | CRT-001 tạo bản ghi 'using the configured certification fields' nhưng cấu hình trường (SCH-004) là P2. Sửa bản ghi (CRT-002) và toàn bộ vòng đời (CMT-001, 003, 004, 005, 006) đều P2 → trạng thái chứng nhận đứng yên, không tự hết hạn, trong khi CRT-003 hiển thị status và expiry. CMT-007 dựa trên 'scheme's configured offsets' (SCH-006, P2). | Q-09 |
| F-17 | Phụ thuộc | UC List!R94, R95, R97 | EVD-004, EVD-005, EVD-007 hiển thị declaration state, maturity declaration, gap flags, freshness — dữ liệu do ASM-001/002, RDN-002/003, CFG-002 tạo ra, đều P2. | Q-11 |
| F-18 | Phụ thuộc | UC List!R107, R176 | Consultant hỗ trợ 'Gap Analysis' (EVD-020) và bình luận trong 'gap context' (CNS-001), nhưng Gap List (RDN-005) và gap rules (RDN-002) là P2. | Q-11 |
| F-19 | Phụ thuộc | UC List!R82, R89, R113 | Nếu kéo CKP-001 về P1 như SGS đề nghị thì cần JRN-004 và RDN-001 (đều P2) để có 'Digital Trust status' và 'recommended next step'. | Q-01 |
| F-20 | Phụ thuộc | UC List!R103; Future Release!R32–R33, R42–R43 | Evidence Package (EVD-017/018) và Accept/Reject Package (REV-009/010) là Future → chưa rõ trong MVP khách nộp bằng chứng cho review thế nào và trạng thái bằng chứng (EVD-014) liên hệ gì với trạng thái item trong review (REV-005). | Q-05 |
| F-21 | Phụ thuộc | UC List!R61, R65, R66 | Tạo tài khoản khách (ACC-003) và mời Customer Admin (ACC-007) thuộc MVP, nhưng kích hoạt tài khoản (ACC-008) là P2 → chưa rõ trạng thái mặc định sau khi tạo. | Q-14 |
| F-22 | Thiếu luồng | UC List!R6–R7, R13, R17–R19 | MVP không có sửa, vô hiệu hóa, xóa người dùng (USR-004/008/009) và không có đặt lại mật khẩu (AUTH-003/004, USR-010). SGS đã chấp nhận hỗ trợ thủ công cho mật khẩu, chưa có ý kiến về thu hồi quyền truy cập → người nghỉ việc vẫn đăng nhập được. | Q-14 |
| F-23 | Thiếu luồng | UC List!R77, R79 | Không có UC xóa scope; Archive Scope (SCP-005) là P2 → scope tạo sai không gỡ được. SCP-007 gỡ framework khỏi scope nhưng không nói workspace tương ứng ra sao. | Q-08 |
| F-24 | Thiếu luồng | UC List!R39–R41 | Tạo requirement/control (FWK-005) và retire (FWK-007) thuộc MVP, nhưng sửa (FWK-006) là P2. | Q-07 |
| F-25 | Thiếu luồng | UC List!R125 | Không có UC quản trị catalogue đào tạo tại chỗ; 'tracks' chưa rõ theo dõi cái gì. | Q-17 |
| F-26 | Thuật ngữ | UC List!R44, R78, R92; Future Release!R29 | Bốn cách gọi cho việc gắn framework: 'Link Framework to Scope' (SCP-006), 'framework is activated on a scope' (EVD-002), 'Activate Framework' ở cấp nền tảng (FWK-013), 'Activate Recommended Frameworks' / CP-12 (DSC-005, Future). | Q-08 |
| F-27 | Thuật ngữ | UC List!R91–R92 | 'Certification cycle' dùng để chặn tạo trùng workspace nhưng không được định nghĩa; không UC nào trong MVP bắt đầu một chu kỳ mới. | Q-08 |
| F-28 | Mơ hồ | UC List!R138, R142, R145, R150, R151 | Review Workflow thiếu: danh sách trạng thái item (REV-005), quy tắc suy ra trạng thái tổng (REV-016), định nghĩa 'completed' để đóng (REV-015), phân loại finding (REV-008), vai trò nào tạo loại review nào và 'review-context separation' (A2) ẩn gì với ai (REV-001). | Q-04 |
| F-29 | Mơ hồ | UC List!R103–R104, R106 | EVD-014 cho khách hàng đặt cả 'reviewed', 'rejected', 'accepted'; không có bảng chuyển trạng thái; ghi chú ở EVD-019 cho thấy việc archive thuộc CP-20 phần P2 trong khi EVD-014 có trạng thái 'archived'. EVD-015 xóa 'where retention policy permits' nhưng chưa có chính sách. | Q-05 |
| F-30 | Mơ hồ | UC List!R127–R135 | Service Request chưa có trạng thái khởi tạo và bảng chuyển; 'before SGS delivery begins' (SRQ-004) chưa gắn với trạng thái cụ thể; danh mục loại yêu cầu còn mở (Q&A #33); SGS Consultant được giao yêu cầu tư vấn (SRQ-006) nhưng không có trong actor của SRQ-007/008/009; SRQ-009 thiếu SGS Auditor/Certification so với SRQ-007/008. | Q-06 |
| F-31 | Mơ hồ | UC List!R15, R96, R146 | EVD-006 cho Customer User xem 'all evidence held by the organization', trong khi USR-006 giới hạn Customer User theo scope và REV-011 ghi 'assigned scope'. | Q-10 |
| F-32 | Mơ hồ · Khó test | UC List!R21–R25 | ROL-001 (36 giờ, UC lớn nhất) thực thi 'predefined role and permission matrix' nhưng ma trận không có trong tài liệu → không có oracle cho test phân quyền. Ghi chú FRD 4.3 (ở ROL-003..005) nói mô hình 7 vai trò, danh sách UC có 8 vai trò. | Q-03 |
| F-33 | Mơ hồ | UC List!R8 | AUTH-005 chỉ liệt kê 4 vai trò kích hoạt qua lời mời (Customer Admin, Customer User, SGS User, SGS Consultant); thiếu Customer Viewer, SGS Admin, SGS Trainer/Assessor, SGS Auditor/Certification. | Q-14 |
| F-34 | Mơ hồ | UC List!R64, R127, R132, R182–R184 | Chưa rõ hồ sơ Consultant trên Marketplace (nội dung do SGS Admin quản lý, MKT-006) có gắn với tài khoản vai trò SGS Consultant không; ACC-006 cho tối đa 1 Consultant active mỗi khách hàng, chưa rõ xử lý khi khách chọn Consultant khác qua Marketplace (MKT-005 → SRQ-001). | Q-12 |
| F-35 | Mơ hồ | UC List!R37, R42 | SGS yêu cầu hỗ trợ ban đầu 'ISO27001, ISO42001 and CMS' — chưa rõ 'CMS' là framework nào. FWK-008: SGS hỏi 'What are the types of evidences? Files?' và gợi ý lùi P2, chưa có trả lời. | Q-07 |
| F-36 | Mơ hồ | 12 UC trong phạm vi đề xuất | Cụm từ cần được liệt kê cụ thể trong UC spec: 'such as' (NTF-001, EVD-008, MKT-003), 'relevant' (NTF-001, SRQ-001, REV-001, REV-004), 'sensitive' (AUD-001), 'supported' (FWK-004, EVD-008, SRQ-001), 'where permitted' (EVD-011), 'permitted transitions' (EVD-014), 'retention policy' (EVD-015), 'where applicable' / 'appropriate' (SRQ-006). | Q-05, Q-06, Q-13 |
| F-37 | Khó test | UC List!R31–R33 | Nếu AUD-002 là P2 thì MVP không có màn hình để SGS xem audit do AUD-001 ghi; AUD-004 chỉ hiển thị hoạt động của tổ chức khách → cần API hoặc DB để kiểm chứng AUD-001. | Q-13 |
| F-38 | Khó test | UC List!R158, R163 | CMT-002/007 là job chạy theo thời gian → môi trường test cần cách kích hoạt job hoặc chỉnh thời gian. | Q-18 |
| F-39 | Khó test | UC List!R119–R120 | TRN-001/002 phụ thuộc Academy API bên ngoài; cần sandbox hoặc mock để test cả trường hợp API lỗi. 'Graceful message' chưa có nội dung cụ thể. | Q-18 |
| F-40 | Khó test | UC List!R63, R180, R182 | Dữ liệu Pentesting và Consultant do SGS Taiwan cung cấp (MKT-002/004); test ranh giới affiliate (ACC-005) cần ít nhất hai affiliate. | Q-18 |

## 6. Bước tiếp theo

1. Bạn trả lời 6 câu CHẶN (Q-01 → Q-06). Các câu còn lại AI làm tiếp theo đề xuất mặc định, gắn nhãn [GIẢ ĐỊNH].
2. AI ghi câu trả lời vào `questions.md`, cập nhật inventory, chốt baseline `docs/baseline/SGS-DTP-MVP.v1.0.md` kèm changelog.
3. Bước 5: rủi ro, phạm vi test, xuất test basis cho Tester. Với tài liệu hiện tại (chỉ là danh sách UC), test basis mới đủ cho phần Redirect và phân quyền. Phần Validation và Function chi tiết cần UC spec — nên ưu tiên Review Workflow, Evidence Management, Service Request.

## Phụ lục A — Vai trò × UC trong phạm vi đề xuất

[GIẢ ĐỊNH] Suy ra từ cột Actor, chờ ma trận phân quyền chính thức (Q-03). ✓ = thực hiện; xem = chỉ xem trong phạm vi được giao; ⚠ = UC có lỗi dữ liệu (xem mục 5).

CA Customer Admin · CU Customer User · CV Customer Viewer · SA SGS Admin · SU SGS User · STA SGS Trainer/Assessor · SAC SGS Auditor/Certification · SC SGS Consultant

| UC | Tên UC | CA | CU | CV | SA | SU | STA | SAC | SC | Khác |
|---|---|---|---|---|---|---|---|---|---|---|
| AUTH-001 | Log In to Platform | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| AUTH-002 | Log Out of Platform | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| AUTH-005 | Activate Account from Invitation | ✓ | ✓ |  |  | ✓ |  |  | ✓ |  |
| USR-001 | View User List | ✓ |  |  | ✓ |  |  |  |  |  |
| USR-002 | View User Details | ✓ |  |  | ✓ |  |  |  |  |  |
| USR-003 | Create User and Send Invitation | ✓ |  |  | ✓ |  |  |  |  |  |
| USR-005 | Assign Role to User | ✓ |  |  | ✓ |  |  |  |  |  |
| USR-006 | Assign Scope Access to Customer User | ✓ |  |  |  |  |  |  |  |  |
| ROL-001 | Enforce Role, Tenant and Affiliate Permissions |  |  |  |  |  |  |  |  | System |
| ROL-002 | View Role Permission Matrix | ✓ |  |  | ✓ |  |  |  |  |  |
| NTF-001 | Generate In-App Notification |  |  |  |  |  |  |  |  | System |
| NTF-002 | View Notification Inbox and History | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| AUD-001 | Record Audit Trail Entry |  |  |  |  |  |  |  |  | System |
| AUD-004 | View Own Organization Activity Log | ✓ |  |  |  |  |  |  |  |  |
| FWK-001 | View Framework List |  |  |  | ✓ |  |  |  |  |  |
| FWK-002 | View Framework Details |  |  |  | ✓ |  |  |  |  |  |
| FWK-003 | Create Framework |  |  |  | ✓ |  |  |  |  |  |
| FWK-004 | Edit Framework Metadata |  |  |  | ✓ |  |  |  |  |  |
| FWK-005 | Create Requirement or Control |  |  |  | ✓ |  |  |  |  |  |
| FWK-007 | Retire Requirement or Control |  |  |  | ✓ |  |  |  |  |  |
| FWK-008 | Define Expected Evidence Types for a Control |  |  |  | ✓ |  |  |  |  |  |
| FWK-009 | Import Framework Content |  |  |  | ✓ |  |  |  |  |  |
| FWK-013 | Activate Framework |  |  |  | ✓ |  |  |  |  |  |
| ACC-001 | View Customer Account List |  |  |  | ✓ | ✓ |  |  | ✓ |  |
| ACC-002 | View Customer Account Details |  |  |  | ✓ | ✓ |  |  | ✓ |  |
| ACC-003 | Create Customer Account and Tenant |  |  |  | ✓ |  |  |  |  |  |
| ACC-004 | Edit Customer Account |  |  |  | ✓ |  |  |  |  |  |
| ACC-005 | Link Customer Account to SGS Affiliate |  |  |  | ✓ |  |  |  |  |  |
| ACC-006 | Assign SGS Personnel to Customer Account |  |  |  | ✓ |  |  |  |  |  |
| ACC-007 | Invite Initial Customer Admin |  |  |  | ✓ |  |  |  |  |  |
| SCP-001 | View Scope List | ✓ | ✓ |  |  | xem | xem | xem | xem |  |
| SCP-002 | View Scope Details | ✓ | ✓ |  |  | xem | xem | xem | xem |  |
| SCP-003 | Create Scope | ✓ |  |  |  |  |  |  |  |  |
| SCP-004 | Edit Scope | ✓ |  |  |  |  |  |  |  |  |
| SCP-006 | Link Framework to Scope | ✓ |  |  |  |  |  |  |  |  |
| SCP-007 | Unlink Framework from Scope | ✓ |  |  |  |  |  |  |  |  |
| EVD-001 | Create Evidence Workspace | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-002 | Create Evidence Workspace on Framework Activation |  |  |  |  |  |  |  |  | System |
| EVD-003 | View Evidence Workspace List | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-004 | Browse Controls Catalogue | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-005 | View Control Details | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-006 | View Evidence Library | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-007 | View Evidence Details | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-008 | Upload Evidence | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-010 | Edit Evidence Metadata | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-011 | Map Evidence to Requirements or Controls | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-012 | Remove Evidence Mapping | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-013 | Replace Evidence with New Version | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-014 | Update Evidence Workflow Status | ✓ | ✓ |  |  |  |  |  |  |  |
| EVD-015 | Delete Evidence | ✓ |  |  |  |  |  |  |  |  |
| EVD-016 | Assign Requirement Owner | ✓ |  |  |  |  |  |  |  |  |
| EVD-019 | Archive Evidence Workspace | ✓ |  |  |  |  |  |  |  |  |
| EVD-020 | Access Assigned Customer Evidence |  |  |  |  |  | ✓ | ✓ | ✓ |  |
| TRN-001 | Browse SGS Academy Course Catalogue | ✓ | ✓ |  |  |  |  |  |  |  |
| TRN-002 | View Course Details | ✓ | ✓ |  |  |  |  |  |  |  |
| TRN-009 | Browse On-site Training Catalogue ⚠ | ✓ | ✓ |  |  |  |  |  |  |  |
| SRQ-001 | Submit Service Request | ✓ | ✓ |  |  |  |  |  |  |  |
| SRQ-002 | View Service Request List | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |
| SRQ-003 | View Service Request Details | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |
| SRQ-004 | Cancel Service Request | ✓ | ✓ |  |  |  |  |  |  |  |
| SRQ-005 | Triage Service Request |  |  |  |  | ✓ |  |  |  |  |
| SRQ-006 | Assign Service Request |  |  |  | ✓ | ✓ |  |  |  |  |
| SRQ-007 | Update Service Request Status |  |  |  |  | ✓ | ✓ | ✓ |  |  |
| SRQ-008 | Add Internal Comment to Service Request |  |  |  |  | ✓ | ✓ | ✓ |  |  |
| SRQ-009 | Request Information from Customer |  |  |  |  | ✓ | ✓ |  |  |  |
| SRQ-010 | Respond to Information Request | ✓ | ✓ |  |  |  |  |  |  |  |
| REV-001 | Create Review |  |  |  |  | ✓ | ✓ | ✓ |  |  |
| REV-002 | Assign Reviewer to Review |  |  |  | ✓ | ✓ |  |  |  |  |
| REV-003 | View Review Queue |  |  |  |  | ✓ | ✓ | ✓ |  |  |
| REV-004 | View Review Details | ✓ | ✓ |  |  | ✓ | ✓ | ✓ |  |  |
| REV-005 | Update Requirement / Control Review Status |  |  |  |  |  | ✓ | ✓ |  |  |
| REV-006 | Add Review Comment |  |  |  |  |  | ✓ | ✓ |  |  |
| REV-007 | Request Clarification or Additional Evidence |  |  |  |  |  | ✓ | ✓ |  |  |
| REV-008 | Raise Finding |  |  |  |  |  | ✓ | ✓ |  |  |
| REV-011 | View Review Feedback | ✓ | ✓ |  |  |  |  |  |  |  |
| REV-012 | Respond to Review Request | ✓ | ✓ |  |  |  |  |  |  |  |
| REV-013 | Submit Corrective Action | ✓ | ✓ |  |  |  |  |  |  |  |
| REV-014 | Evaluate Customer Response |  |  |  |  |  | ✓ | ✓ |  |  |
| REV-015 | Close Review |  |  |  |  |  | ✓ | ✓ |  |  |
| REV-016 | Derive Overall Review Status |  |  |  |  |  |  |  |  | System |
| CRT-001 | Create Certification Record |  |  |  |  | ✓ |  |  |  |  |
| CRT-003 | View Certification Record List | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |
| CMT-002 | Generate Certification Milestone Notification ⚠ |  |  |  |  |  |  |  |  | System |
| CMT-007 | Generate Certification Milestone Notification ⚠ |  |  |  |  |  |  |  |  | System |
| OPS-001 | View SGS Operations Dashboard |  |  |  | ✓ | ✓ |  |  |  |  |
| CNS-001 | Add Consulting Comment |  |  |  |  |  |  |  | ✓ |  |
| CNS-002 | View Consulting Comments | ✓ | ✓ |  |  |  |  |  | ✓ |  |
| MKT-001 | View DT Marketplace | ✓ | ✓ |  |  |  |  |  |  |  |
| MKT-002 | View Pentesting Service List | ✓ | ✓ |  |  |  |  |  |  |  |
| MKT-003 | View Pentesting Service Details | ✓ | ✓ |  |  |  |  |  |  |  |
| MKT-004 | View Consultant Details ⚠ | ✓ | ✓ |  |  |  |  |  |  |  |
| MKT-005 | Customer Admin, Customer User ⚠ | ✓ | ✓ |  |  |  |  |  |  |  |
| MKT-006 | Manage Marketplace Content |  |  |  | ✓ |  |  |  |  |  |
