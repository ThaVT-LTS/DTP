---
name: flow-doc
description: Làm tài liệu luồng happy case bằng tiếng Anh (Word, mỗi luồng 1 file, ảnh web có URL, khung đỏ, bảng tổng quan bấm sang từng bước, mục "Not tested yet (blocked)") và mind map HTML tương tác nối các luồng. Dùng khi được yêu cầu "tạo luồng …", "kịch bản smoke test", "mind map luồng", "thêm nhánh cancel / discuss".
---
# Tài liệu luồng + mind map (v0.1 — [ĐỀ XUẤT], chờ duyệt · FB-124)
Tuân thủ `rules/common.md`, `rules/automation.md` (rule 22, 48, 52).

## Đầu ra (dự án SGS DTP)
- Thư mục: `dts-agent-workspace/tests/reports/Flow report/`.
- Word đánh số theo thứ tự đi luồng, tên **không** kèm "Review" / ngày: `01_Onboarding_Users_Flow.docx`, `02_Scope_Framework_Workspace_Flow.docx`, `03_Assisted_Workspace_Flow.docx`, `04_Change_and_Manage_Flow.docx` (các UC Wave 1 còn lại), `05_Bulk_NirmatAI_Flow.docx`, `06_Service_Requests_Flow.docx`, `07_Certifications_Marketplace_Flow.docx`. Số flow = `seq` trong spec = số trên mind map (06/11).
- Bộ theo wave (06/11, QA lead): Wave 1 = Flow 1–4 → `00_DTP_Wave1_Checklist.xlsx` (`scripts/build_checklist.py <checklist-map.json> <specs> <UC xlsx> <Plan xlsx> <bugs.md> <out>`; `only_round`; bước trùng ghi "Same as …") + `00_DTP_Wave1_MindMap.html` (`mindmap.sgs-dtp-w1.json`). Wave lấy từ Plan sheet "Plan by UC"; mỗi UC của wave phải có ≥ 1 bước.
- Mind map: `00_DTP_Happy_Path_MindMap.html` (mở offline; ảnh lấy từ `tests/evidence/…`, nút mở Word nằm cùng thư mục → gửi đi thì gửi cả cấu trúc thư mục).
- Ảnh: `dts-agent-workspace/tests/evidence/<luồng>-flow-<dd-mm>/`.
- Spec mỗi luồng + cấu hình mind map: `projects/sgs-dtp/tests/flows/` (`spec-*.json`, `mindmap.sgs-dtp.json`).

## Thứ tự luồng
Luồng nền trước, nhánh sau: Onboarding → Scope → Framework → Workspace (tách Assisted / Bulk) → chi tiết Assisted → chi tiết Bulk → Service requests (cần workspace) → Certifications / Marketplace. Mỗi file ghi "FLOW x OF n" và dòng "Before this … · Next …".

## Các bước
1. **Chụp trên web** (rule `web-first`), chỉ happy case, không chụp cancel / negative. Script chụp viết theo `references/example-capture.js`, dùng `scripts/mk.js`:
   - `mark(page, locator, 'label', 'top|bottom|left|right')` rồi `shot(page, 'tên.png')`: thanh URL + giờ ở trên, khung đỏ vẽ **sau** khi trang bị đẩy xuống nên không lệch. Đặt `QA_HELPER` trỏ tới helper Playwright của dự án (`H.page(browser, role)`, `L.launch`).
   - Nhãn tiếng Anh, ngắn, không đè chữ của màn: xem lại 3–4 ảnh bằng Read; đè thì đổi vị trí nhãn hoặc đánh dấu tiêu đề cột thay cho từng dòng.
   - Dữ liệu tạo mới có tiền tố `[QA] Dnn Smoke …`; không đụng cài đặt dùng chung, dữ liệu người khác, framework NirmatAI có sẵn; Approve and send / gửi NirmatAI chỉ khi người dùng đồng ý (rule 48). Không tạo file EICAR / malware.
   - Hộp thoại thuộc happy path (vd Approve and send) được mở rồi Cancel khi không được phép bấm thật; ghi rõ trong ghi chú.
2. **Viết spec** (`references/example-spec.json`): `title, out, imgDir, env, intro[], steps[{who, where, what, result, body[], shots[[file, caption]]}], tables[], blocked[[area, not tested, why, check on SGS env]], limitations[], seq, related`. Ảnh dùng lại từ luồng khác thì chép sang thư mục ảnh của luồng này (tiền tố `A-`, `N-` …).
3. **Build Word**: `node scripts/buildflow.js <spec.json>` (cần `npm install` trong `scripts/`). Giao diện: Calibri, dải tiêu đề, thẻ thông tin, bảng tổng quan (ô Where bấm sang bước), bảng đỏ "Not tested yet (blocked)", mỗi bước một trang (`pageBreakBefore` trên tiêu đề, không dùng đoạn PageBreak riêng), link quay lại tổng quan đặt **dưới tiêu đề bước**, ảnh giới hạn chiều cao.
4. **Kiểm trang trắng** trước khi giao: `python -I scripts/pagecheck.py <thư mục chứa bản sao docx>` (ONLYOFFICE x2t → PDF → pypdf). Word COM trên máy QA bị treo (`RPC_E_CALL_REJECTED`), không dùng. File đang mở trong ONLYOFFICE → build ra bản tạm, chép đè sau.
5. **Mind map**: `node scripts/gen_mindmap.js projects/sgs-dtp/tests/flows/mindmap.sgs-dtp.json`. Cấu hình mỗi luồng: `shape.chains` (chuỗi bước), `shape.fork` (bước tách nhánh, vd Assisted / Bulk), `planned` (nhánh chưa chụp), `next`, `needs`. Kiểm: mở bằng Playwright, bấm qua các nút, mọi ảnh tải được, không lỗi console.
6. **Báo người dùng**: bảng file + số bước + số ảnh, dữ liệu đã tạo, điểm lạ (đã tra `bugs.md`: có mã thì ghi mã; chưa có mới ghi "suspected", không tự log), mục chưa test được.

## Mục "Not tested yet (blocked)" — luôn có
Đăng nhập Microsoft Entra (kích hoạt, đặt / quên mật khẩu do trang Entra lo) · gửi mail thật qua SMTP SGS (web test dùng Mailpit) · kết nối NirmatAI trên môi trường SGS (thiếu cert) · quét malware (Symantec xoá file test) · tính năng chưa có trên web (vd yêu cầu đào tạo on-site). Mỗi dòng: Area · Not tested · Why · Check on the SGS environment.

## Nhánh phụ (cancel, discuss, terminate …)
- Mind map giữ sẵn nhánh phụ dạng **planned** (xám, nét đứt, ẩn mặc định, bật bằng "Show planned branches"), lấy theo Workflow Rules đã chốt.
- Khi chụp: thêm phần **"Alternative paths"** vào cuối file Word của luồng đó (mỗi nhánh: ai làm, lý do, trạng thái sau, 1–2 ảnh); trên mind map nhánh đã chụp chuyển thành ô màu, đường cam nét đứt, có ảnh.
- **Đọc kết quả có sẵn trước khi chạy**: nhánh phụ phần lớn đã có case TC và bug (vd IS-BUG-08/09/13/14, ST-BUG-21, AL-BUG-01/02 ngày 05/11). Tra `tasks/bugs.md` + cột kết quả file TC; nhánh đã Passed thì chỉ chụp lại ảnh, nhánh có bug thì ghi **mã bug + trạng thái** vào tài liệu, không ghi "suspected".
- Điểm lạ mới thấy khi chụp: tra `bugs.md` (theo từ khoá) trước; đã có mã → ghi mã; quyết định đã chốt khác (vd CU-BUG-24 chỉ cho số và + - ( ), TR-BUG-02 on-site không thuộc Phase 1) → không phải lỗi, sửa lời trong tài liệu; chưa có → mới ghi "suspected" và báo người dùng.
- Dữ liệu: mỗi nhánh một request / workspace riêng `[QA] Dnn Alt …`, script đưa tới đúng trạng thái rồi mới bấm nhánh phụ.
- Thứ tự đề xuất: (1) Service request: Decline, Cancel (3 chỗ), Close negotiation, Return to discussion, Decline completion · (2) Terminate, Request termination duyệt / từ chối, Reassign consultant → Request access duyệt / từ chối (cần consultant thứ 2) · (3) Bulk Send additional documents (gửi NirmatAI → cần đồng ý), Change client, Assisted Archive / New cycle, Resend invitation, Delete certification.

## Changelog
| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.1 | 2026-11-05 | Khởi tạo từ bộ 6 luồng smoke test cho Xavier (02–05/11) và mind map happy path; cách làm nhánh phụ. **Chờ duyệt.** | FB-124 · chat QA lead 02–05/11 |
