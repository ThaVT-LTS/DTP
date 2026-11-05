# SGS DTP — hiện trạng 05/11/2026 (đọc file này TRƯỚC `profile.md`)

Viết 05/11/2026 cuối ngày để một phiên / thread khác tiếp tục được. Khi khác với `profile.md` hoặc memory cũ, **file này thắng** (trừ khi có quyết định mới hơn ghi trong ticket / Decision log).

## 1. Nguồn chuẩn

| Nguồn | Vị trí | Trạng thái |
|---|---|---|
| **UC List v6.5** | `DTP/dts-agent-workspace/tests/input/SGS_DTP_Use_Case_List_v6.5.xlsx` (bản **05/11 11:31**, có trả lời Q42/Q43) | **SGS duyệt 05/11 13:13** (Mao-Chi: "UC List v6.5 can be considered approved"). Baseline Phase 1 đã khoá. Figma sửa song song |
| Plan | `tests/input/SGS_DTP_Detailed_Plan_v3.0.xlsx` | dùng để ghi Pending / Blocked |
| Workflow Rules (consultant) | `tests/input/SGS_DTP_Pending_Confirmations_XV_TW.xlsx` › Consultant Workflow Rules WF-01–16 | vẫn dùng; khi lệch UC v6.5 → UC thắng |
| Trả lời SGS ngoài UC | Teams 05/11 Mao-Chi 11:51 (3 nguồn consultant, Reassign C-01–C-03) | QA lead cho cập nhật TC / log bug ngay, không chờ UC v6.6 |
| Figma | DTP-P1 `jluZdAkgifmZndi5hD12tt` (cockpit V4 page `785:490`, Customer Admin Home `785:531`) | một số màn còn luồng cũ (vd Reviews "Access requested → Review access") |

## 2. Quy tắc nghiệp vụ đã chốt (dùng cho Expected)

| Chủ đề | Quy tắc | Nguồn |
|---|---|---|
| Multi-account Customer Portal | **Phase 2** (chọn / chuyển account, account dùng lần trước). P1: một account active cho mỗi người | UC v6.5 D103, D105 |
| Mời email đã active ở tenant khác | UC v6.5 **D104 / AUTH-03 col F–G**: P1 **không** cho kích hoạt membership thứ 2 (cách chặn chờ **Q44**). **Quy tắc tạm của QA lead 04/11** (đang áp cho CU_103, US_103, CU-BUG-27): vẫn mời + kích hoạt như thường, đăng nhập mở 1 account. **05/11 QA lead chốt: theo UC v6.5 D104** — không kích hoạt membership thứ 2 (CU-BUG-29, CU_103 / US_103 Failed); quy tắc tạm 04/11 bỏ | D104, Q44 |
| Ai quyết termination / completion | **Chỉ Customer Admin** (Approve/Reject termination, Confirm/Decline completion). Grant Workspace Access & Start cũng chỉ Customer Admin | UC v6.5 Q43 (SGS 05/11) — bug IS-BUG-16 |
| Thay consultant của khách | Customer Admin thay consultant khách chỉ định (My consultants); cũ mất quyền; mới xin quyền; bị từ chối → chọn người khác hoặc để chờ | Q42 (SGS 05/11) |
| Reassign (mọi nguồn) | **Customer Admin và SGS Admin đều bắt đầu được, bên kia xác nhận**; chọn theo đúng nguồn ban đầu; request **giữ In progress + trạng thái phụ "Reassignment"**; giữ dữ liệu cũ; consultant cũ mất quyền, mới phải được Grant; từ chối → chọn khác | SGS C-01–C-03 (05/11) — bug IS-BUG-17 (+ IS-BUG-07 gộp) |
| Nguồn consultant | **3 lựa chọn**: Your organisation · Consultants from SGS network (consultant ngoài qua Marketplace) · **Services provided by SGS** (khách yêu cầu SGS, SGS Admin giao nhân viên SGS) — cả Gap Analysis và Implementation Support | SGS 05/11 11:51 — bug IS-BUG-18 |
| Consultant cũ sau Reassign | chỉ cần câu "This request was reassigned to another consultant on <date>." thay "Page not found" | QA lead 05/11 — IS-BUG-08 |
| SGS Admin xem request | **Chỉ thông tin vận hành** (khách, consultant, dịch vụ, workspace, trạng thái, ngày, lý do). **Không** clarification / finding / deliverable / notes | UC SRQ-03 (từ v6.3), D57 — vì vậy IS-BUG-13 bị huỷ |
| SGS Admin Decline request Submitted | **Không** (chỉ SGS Consultant) | UC SRQ-05 |
| Giới hạn chữ | mọi ô chữ của service request **250** (lý do, câu hỏi, trả lời, finding, message, comment); Headline profile 160; Notes 10.000 | QA lead 04/11 |
| Cockpit = Home | CKP-01 Customer Admin (khối **Reviews** theo luồng mới: "Ready to start → Grant access & start"), CKP-03 SGS Admin (khối **Audit Requests**: Bulk chờ duyệt / gửi lỗi / chưa link) | HM-BUG-07, HM-BUG-08 |
| Certifications → **Trust Centre** | đã đổi trên web, Verified | D101, CT-BUG-11 |
| Login | bỏ dòng hỗ trợ (Need help / Trouble signing in) | QA lead + Việt 04/11, LG-BUG-07 Verified |
| On-site training TRN-03–06 | **Phase 1** (QA lead 05/11: theo UC v6.5). TR_031–039 Failed, thêm TR_040–042 (phía SGS), TR-BUG-02 mở lại (Việt) | UC v6.5 TRN-03–06 |
| Q44, Q45, Q40 | Q44 (cách chặn tenant thứ 2) và Q40 (Bulk không qua NirmatAI kết thúc thế nào) còn mở; Q45 coi như đóng vì v6.5 đã duyệt | UC v6.5 Open Questions |

## 3. Môi trường và dữ liệu

- Web test `https://dtp.ltsgroup.tech`, build lấy bằng `tests/tools/pw/portainer-ps.js`. **05/11 cuối ngày: web / backend `6ba165c4`.** Web và backend có thể lệch phiên bản khi deploy riêng → lỗi kiểu "The documents couldn't be loaded" là **lỗi môi trường**, không log.
- **SGS bắt đầu smoke test Wave 1 trên chính web này** (Xavier đồng ý 05/11 12:53). Người test UAT phía SGS: Mao-Chi Chen, Webber Huang, Sam Lin, Geoffrey Wang (@sgs.com). Mail của web test chỉ vào Mailpit.
- Local `CORP-BA-DTP` chạy cùng commit với web khi cần giả lập ngày / job (retention, nhắc). Dựng lại DB local thì **bảng `non_working_day` trống** (migration 0088 chỉ nạp ngày lễ cho affiliate có sẵn) → phải chèn lại 32 ngày lễ SGS Taiwan trước khi chạy IS_155. Trên web cần kiểm bảng này.
- Tài khoản (mật khẩu dev chung, lấy từ RUN-SPEC qua env, không in ra):
  - SGS Portal `/ops/login`: Lin Mei (SGS Admin), **Chen Wei** (từ 05/11 hiển thị **SGS employee**), [QA] PM2 Ken Lin (Freelancer — dùng khi cần luồng Freelancer), [QA] D02 SGS Consultant.
  - Customer Portal `/login`: Kevin Lin (Customer Admin, Development organisation), Leo Wu ([QA] W9 R2, Customer User), Peggy Lai (Viewer), [QA] M22 M2 Ian Chang (Customer Consultant), [QA] Mia Tran (Admin của 2 tenant [QA] D04 MT A / B).
  - Không đụng: Jason Chen, dữ liệu QA lead (HANNA*, ggg, dfdf, Hanna scope, SR-2026-063/068/071/105/108/118/121), profile Chen Wei.
- File TC: `tests/cases/SGS-DTP_TestCase_v0.4_Phase1.xlsx`. Mã case theo màn: AR_ (All requests), GA_, RT_, ST_, TR_, CS_, RV_ (đổi từ TC_ ngày 04/11). Ghi file **bằng Excel COM** (giữ ảnh Cover, công thức Test_Report); khi thêm dòng phải mở rộng công thức L4:Q6 và Test_Report. Script mẫu: `scratchpad/uc65.ps1` của phiên 05/11 (ops set/prefix/prepend/date + new rows).
- Bug = ticket `dts-agent-workspace/tasks/tickets/TICKET-FIX-*.md`; mã qua `tests/tools/bug_codes.py next <PREFIX>` + `check`; sau đó `scripts/bug-sync.py` và `scripts/kanban-sync.py`. Xung đột rebase ở `bugs.md` / `kanban.md` → lấy bản upstream rồi chạy lại 2 script.
- Báo cáo ngày: `tests/tools/report/daily.py --no-post` rồi `report_extra.py`; từ 05/11 ô bug tách **Chờ merge** (fix chưa lên web) và **Chờ QA** (fix đã lên web). Dòng "Mới log" / "Verified" của sheet Hôm nay vẫn điền tay.

## 4. Ai nhận bug

| Loại | Người |
|---|---|
| Mặc định | **Huy** |
| Home / cockpit | **duongnhd** (Dương) |
| Responsive (IS-BUG-15, LG-BUG-08) | **Đại** — chỉ vì QA lead chỉ định 05/11; không tự giao Đại |
| Việt | khi QA lead chỉ định (Marketplace MK-BUG-04–07, US-BUG-23, LG-BUG-07, CU-BUG-27…) |
| DuyP | chỉ ticket cũ của DuyP |

## 5. Bug mở đáng chú ý (05/11 cuối ngày)

- **GA-BUG-06 (High, Huy)** — deliverable > 10 MB bị proxy web cắt (`apps/web/src/proxy.ts` thiếu 2 route deliverable). Cần sửa trước smoke test.
- IS-BUG-16 (Q43), IS-BUG-17 (Reassign C-01–C-03, gộp IS-BUG-07), IS-BUG-18 (3 nguồn consultant), HM-BUG-07 (Reviews), HM-BUG-08 (Audit Requests), US-BUG-25 (Last sign-in lộ tenant khác), IS-BUG-15 / LG-BUG-08 (responsive), IS-BUG-04 (My consultants vào thẳng In progress), US-BUG-23 (chữ "Customer" trong tên role).
- MK-BUG-07: Việt nói đã có "Create Marketplace profile" ở SGS Users › Consultant detail — QA đã thấy nút trên web; **chờ QA lead OK** để kiểm hết luồng rồi Verified và sửa MK_064–067.

## 6. Việc đang dở cuối 05/11

1. Kết quả 2 luồng chạy chiều 05/11: (a) retest BU-BUG-08/10/25, FW-BUG-18, HM-BUG-03 + BU_138, US_103 + 32 case Marketplace/Home/Audit; (b) rà 96 case Pending/Blocked/On hold/NA với UC v6.5 (file `scratchpad/regress-05-11/R.json`, `W.json`). Ghi kết quả vào TC, báo QA lead các đề xuất UC_CHANGE (không tự áp).
2. Chờ QA lead: D104 vs quy tắc tạm (mục 2); On-site training P1/P2; 8 Expected cũ (WD_050, WD_147, DC_014, CE_044, BU_042, BU_097, BU_018, BU_099) + LG_037/057/050, US_021/022/094, US_017, US_002/069 (3 tab SGS Users); xoá file `tests/data/scan-infected.pdf`; MK-BUG-07.
3. Nghi ngờ chưa kết luận: trang kích hoạt lời mời tenant thứ 2 vẫn hỏi "Create password" (có tạo identity thứ 2 không?); số điện thoại có dấu cách bị từ chối sau CU-BUG-24; US_078 (Invite Freelancer không bắt buộc consulting firm); ST_044; bảng ngày lễ trên DB web.
4. Báo cáo ngày 05/11 trước 17:00.

## 7. Quyết định cuối ngày 05/11
- QA lead: **"chấp nhận theo UC 6.5" cho mọi chỗ lệch** (D104, on-site training, AUD-04, INT-01, INT-02, SRQ-10…). Khi UC v6.5 và quyết định cũ của QA lead khác nhau → **theo UC v6.5**.
