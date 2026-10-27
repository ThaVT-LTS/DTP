# Rule — Chạy manual và Automation (Playwright)

Phiên bản: v0.4 · **[ĐỀ XUẤT] — chờ duyệt.** Nạp cùng `rules/common.md`, `rules/feedback.md`, `rules/tester.md` khi chạy test hoặc viết spec. Skill: `manual-run`, `write-e2e-spec`. Ánh xạ TC → Playwright: `skills/test-design/references/templates.md` §6.

1. Chỉ chạy và chỉ tự động hoá TC thuộc bộ test đã qua cổng 3 (`rtm_check.py` sạch, đã review).
2. Title của `test()` là `<ID TC> · <tiêu đề>`; ID không đổi khi sửa nội dung. Tag đặt trong option `tag`, không nhét vào title: `@<UC-ID>`, `@<nhóm>`, `@<loại>`, `@P<n>`, và các ID trong trường `Nguồn` của TC.
3. Locator lấy từ nhãn nguyên văn trong test basis (FD, MS, NV); ưu tiên role, label, test-id. Phần tử không có tên ổn định thì liệt kê để nhờ dev bổ sung, không dùng selector theo vị trí.
4. Mỗi test tự chuẩn bị dữ liệu qua API hoặc fixture, không phụ thuộc test khác; tài khoản và URL lấy từ biến môi trường, không ghi trong code.
5. Mỗi ý trong `Mong đợi` của TC ứng với ít nhất một `expect`, comment ghi ID nguồn.
6. TC có nguồn đang `[CHỜ Q-nn]` thì `test.fixme('<Q-nn> chờ trả lời')`; không viết assertion đoán.
7. **Không sửa kết quả mong đợi cho test pass.** Khi chạy lệch: được sửa locator, thời gian chờ, bước thao tác. Giá trị mong đợi lệch thì dừng và báo người dùng quyết: bug, TC sai, hay yêu cầu đã đổi.
8. Kết quả chạy ghi vào `runs/`. Khi người dùng yêu cầu chạy một sheet TC, kết quả từng case ghi thêm vào cột **Round N** của file TC (Result, Test person, Test date, Bug_ID, Remark) để Test_Report tự đếm (19/10). Kết quả Fail phải được người dùng xác nhận trước khi thành bug thật (Jira, ticket).
9. Spec kiểm chứng một lần (cho một bug, một bản demo) để ở `automation/tests/verification/`; xong thì nâng thành spec hồi quy hoặc xoá. Bộ hồi quy không chứa spec loại này.
10. Phiên bản Playwright, Node và cấu hình chạy do `package.json` và `playwright.config.ts` quyết định; rule không ghi số phiên bản.

11. Mỗi dự án một thư mục tự đóng gói `automation/<dự-án>/` (có `package.json`, `playwright.config.js`, `.env`). Dự án mới sao từ `automation/_template/`. Test viết trước khi có TC chính thức mang ID tạm `LEARN-*` và tag `@legacy`; khi có TC chính thức thì đổi sang ID TC thật, test nào chưa đổi thì chưa tính vào bộ hồi quy.
12. Đăng nhập một lần: project `setup` lưu `storageState`, các project test dùng lại; test đăng nhập chạy ở project riêng không có `storageState`. Tất cả project dùng cùng một trình duyệt (`channel: 'chrome'`).
13. Cấu hình môi trường (`BASE_URL`, tài khoản) ở `.env`, không đưa lên git; có `.env.example` để người khác điền. Giá trị chứa `#` hoặc khoảng trắng phải đặt trong dấu nháy kép, nếu không bị cắt cụt (lỗi đã gặp: mật khẩu mất ký tự `#` cuối).
14. Mỗi màn hình một Page Object; chức năng dùng chung nhiều màn (tìm kiếm, bảng) tách thành class cha để kế thừa. Locator khai báo ở constructor, thao tác là phương thức.
15. Không dùng `waitForTimeout` và không chờ `networkidle` (ứng dụng có request nền thì không bao giờ idle). Chờ bằng web-first assertion. Bước dễ rớt (mở menu, dialog) bọc trong `expect(...).toPass()`.
16. Dữ liệu tạo trong test dùng tên duy nhất mỗi lần chạy (`uniqueName`). Không dựa vào tên dữ liệu có sẵn trên môi trường (lỗi đã gặp: file mẫu biến mất khi đổi môi trường): chọn theo vị trí hoặc tự tạo. Bắt buộc dùng dữ liệu có sẵn thì khai báo ở `fixtures/testdata.js` kèm chú thích. Test tạo dữ liệu mà chưa có bước dọn thì ghi rõ ở đầu spec.
17. Mỗi dự án ghi kết quả máy đọc được vào `automation/<dự-án>/runs/latest.json` (reporter `json`) và báo cáo HTML; AI đọc file này để biết test nào fail, người dùng không phải chụp màn hình. Kết quả tổng hợp theo TC vẫn ghi ở `projects/<dự-án>/runs/` (rule 8).
18. Test chưa có cơ sở để khẳng định (kết quả mong đợi chưa rõ, dữ liệu chưa tự tạo được) viết thành `test.fixme('<mã câu hỏi> …')` kèm lý do, không để comment hay đoán assertion cho pass.

## Chạy test và báo kết quả (19–20/10/2026, chờ duyệt)

19. **Kết quả của một case, một bước E2E** (FB-093):
    | Kết quả | Khi nào |
    |---|---|
    | Passed | mọi ý của Expected đúng |
    | Failed | màn, chức năng có nhưng ít nhất một ý sai so với Expected **hoặc Figma** (chữ, thiếu thành phần, link thay vì nút, số liệu, trạng thái). Ghi chú "khác Figma" không được để Passed |
    | Blocked | Plan ghi UC Done mà bản đang chạy chưa có màn, chức năng; hoặc môi trường không làm được và không có cách thay thế (ghi cần gì) |
    | Pending | UC chưa Done theo Plan (Not started, hoặc thuộc wave sau); hoặc case chỉ chờ câu hỏi đang mở mà web chưa có hành vi để so. Case vẫn giữ trong bộ, không bỏ |
    | NA | không áp dụng (ghi lý do) |
    Lỗi môi trường trong lúc chạy (backend sập, 502, hết phiên do người khác đăng xuất) không ghi Failed: dựng lại môi trường và chạy lại.
20. **Remark của case Failed** (FB-090): dòng `Thực tế:`, rồi mỗi dữ liệu hoặc tình huống đã thử một dòng có tên và số thật, rồi `Mong đợi (bước N): …`. Không dùng biến `[W]`, `[N]`, không dùng `≠`, chữ giao diện ghi nguyên văn tiếng Anh. Tối đa khoảng 8 dòng. Tiêu đề bug nói đúng nguyên nhân; chức năng đang đúng (vd chu kỳ 3 trạng thái của nút sắp xếp) không bị gán lỗi chỉ vì số liệu đầu vào sai.
    ```
    Thực tế: cột Workspaces luôn hiện "—" thay vì số workspace:
    - "ABC Trading Co., Ltd. a154930" có 0 workspace → hiện "—" (mong đợi: 0)
    - "E2E WS Tenant yaxgl37" có 1 workspace → hiện "—" (mong đợi: 1)
    Mong đợi (bước 2): cột Workspaces ghi đúng số workspace của khách hàng.
    ```
21. **Bug** (FB-091, FB-092): một mã bug = một nguyên nhân; nhiều case cùng nguyên nhân dùng chung mã. Mã tạm `<MÀN>-BUG-nn` đánh theo case Failed đầu tiên trong sheet, thay bằng mã Jira khi tạo bug. Mỗi lượt có Fail thì có file bằng chứng kèm ảnh (skill `bug-evidence`): Figma mong đợi, từng case (Pre, bước, mong đợi, thực tế, ảnh), ảnh gốc chép vào `evidence/`. Lỗi thấy khi test tự do mà chưa có case thì thêm case vào đúng nhóm và gắn mã bug.
22. **Môi trường và phiên bản code** (FB-096): SGS DTP chỉ chạy trên localhost (quyết định 19/10). Trước khi chạy: `git fetch` (kiểm thành công), báo `<nhánh> <commit> (<ngày>)` và chậm bao nhiêu commit so với `origin/main`; ghi dòng này vào mọi file kết quả. Kết quả chạy trên bản cũ phải ghi rõ là bản cũ.
23. **Dữ liệu test** : mọi tên, email tạo ra có hậu tố duy nhất của lượt chạy. Dữ liệu tiền đề mà màn hình chưa hỗ trợ (vd mời user khi màn Users chưa có) được tạo qua DB và ghi rõ ở ghi chú bước. **Không để hỏng tài khoản có sẵn**: case mời email của tài khoản seed (đã là user khách hàng khác, là tài khoản SGS) phải xoá đúng bản ghi mình tạo (invitation, membership) ngay sau case và kiểm tài khoản đó đăng nhập lại được.
24. **Xác nhận Failed bằng ảnh** trước khi ghi: mở ảnh chụp của bước, chắc chắn lỗi là của ứng dụng chứ không phải của locator hay dữ liệu.
25. **Ghi vào file Excel có công thức, ô gộp** (Test_Report đếm bằng COUNTIF theo vùng dòng, cột Classification gộp ô): xoá, chèn dòng và ghi ô bằng chính Excel (COM) để công thức và ô gộp tự chỉnh; sao lưu trước khi ghi; chạy thử trên bản sao rồi mới ghi file thật. Công thức mới viết bằng so sánh trực tiếp (`OR(F17="Failed",…)`), không dùng COUNTIF (ONLYOFFICE của người dùng tính sai). File đang mở trong ONLYOFFICE (có `.~lock.<tên>#`) thì không ghi: nhờ người dùng đóng file, không lưu.
26. **Môi trường local SGS DTP — điều đã gặp** (để không mất thời gian lần sau): Mailpit không lưu email khi khởi động lại, dừng Mailpit làm mất email của mọi luồng khác; `nest start --watch` có thể tự sập trên Windows khi khởi động lại, chạy dài thì chạy backend bằng `node --enable-source-maps dist/main.js`; sau `git pull` build lại `packages/api-contracts` trước `db:reset`; `db:reset` xoá toàn bộ dữ liệu; Next.js có phần tử `role="alert"` ẩn (route announcer), không dùng nó để dò thông báo lỗi.

27. **Case cần email thật: gửi mời và lấy link TRƯỚC, rồi mới chạy** (FB-100). Trên môi trường không có Mailpit / DB (vd web test dùng Gmail thật), AI không đọc được hộp thư và token kích hoạt chỉ nằm trong email. Vì vậy, trước khi chạy một lượt có case cần email thật (mời, kích hoạt, nội dung email, link cũ / đã thu hồi):
    - Liệt kê case nào cần email, mỗi case dùng hộp thư nào (`<mail người dùng>+qaNN@…`), gom case để ít hộp thư nhất.
    - Gửi các lời mời đó trước, **dừng lại hỏi người dùng** dán link kích hoạt (và ảnh chụp email nếu kiểm nội dung). Chờ có link.
    - Chỉ sau đó mới chạy, kể cả các case email, để kết quả là Passed / Failed thật. Không chạy hàng loạt rồi để case ở "Chờ email" / "Not execute".
    - Việc nào phụ thuộc người dùng (link, ảnh, quyết định, dữ liệu) thì hỏi và xác nhận trước khi dùng nhiều agent chạy song song.
28. **Trước khi ghi một bug, đối chiếu quyết định mới nhất** (FB-101): user story đã sửa, decision log, contract API, commit có chủ đích của dev (ghi rõ ngày). Web làm đúng theo quyết định mới hơn Figma / TC thì không phải bug: case Passed, Remark nêu căn cứ, sửa Expected (rule 1 của `tc-authoring.md`, FB-095, FB-099). Bug đã ghi mà sau đó thấy đúng quyết định thì đánh **Rút** trong register, không xoá mã.

29. **Bug người dùng báo khi test tay → bug + case + mẫu lỗi** (23/10): ngoài việc log như mọi bug (tiếng Anh, ticket rồi Azure, gán theo PIC trong Plan), làm luôn hai việc: (a) thêm hoặc sửa case trong đúng nhóm của sheet TC, gắn mã bug, Expected theo đúng quy tắc người dùng đã làm rõ; (b) thêm mẫu lỗi tổng quát vào `rules/bug-patterns.md` (mẫu · cách kiểm · mã ví dụ). Khi thiết kế TC cho màn mới hoặc chạy lượt mới, đối chiếu `bug-patterns.md` và thêm case cho mẫu áp dụng được.

30. **Quét giá trị gán cứng trong code trước mỗi lượt chạy** (26/10): khi có build mới hoặc trước lượt chạy, chạy skill `hardcode-check` trên code đang deploy (ghi rõ commit). Tìm: (a) danh sách / dropdown lấy cố định N mục mà không có tìm kiếm hay phân trang; (b) hằng số nghiệp vụ (số file, MB, ngày, tháng, giờ poll, hạn link) so với bảng giá trị của UC; (c) ID, tên tổ chức, email, URL viết thẳng; (d) text hiển thị không qua i18n EN/ZH; (e) bộ lọc mặc định làm ẩn dữ liệu. Mỗi chỗ lệch UC hoặc làm người dùng không tới được dữ liệu: thêm case vào đúng sheet TC (không đánh dấu "chờ dữ liệu", tạo dữ liệu cần thiết hoặc hỏi người dùng), kiểm trên web, có bug thì báo người dùng trước rồi mới log (tiếng Anh).

31. **Mỗi lượt chạy: tìm lỗi chủ động, phân loại nghi ngờ / lỗi / tiềm ẩn** (26/10, skill `run-cycle`). TC chỉ theo UC sẽ bỏ sót lỗi chỉ lộ ra khi có dữ liệu, giờ hoặc cách gọi đặc biệt. Ngoài TC thường, tìm theo 4 hướng:
    - **Quét code**: giới hạn, hằng số, text viết cứng, so với UC (skill `hardcode-check`, rule 30). Ví dụ: `limit 100`, 25 MB, 500 file, "SGS Taiwan".
    - **Tạo đúng dữ liệu để lỗi lộ ra trên web**: hơn 100 scope, file 30 MB, hơn 50 evidence.
    - **Test biên và thời gian**: số lượng lớn, file lớn, khung 00:00–08:00 giờ Đài Loan (lỗi ngày tính theo UTC).
    - **Gọi thẳng API** những gì giao diện đang chặn (vd UI chặn 21 file nhưng API nhận 500). Đây vẫn là lỗi thật vì người khác có thể gọi API trực tiếp. Chỉ gọi trên môi trường test, bằng tài khoản test.

    Lỗi tìm theo 4 hướng này ghi là **nghi ngờ**, rồi **viết case TC kèm dữ liệu để kích hoạt**. Chạy trên web thấy lỗi thì log (báo người dùng trước, rule 29). Không tái hiện được thì ghi **tiềm ẩn**, báo dev xem, không tính là bug.

    Quy trình mỗi lượt:
    1. Ghi lại build và commit đang deploy (rule 22). Quét đúng commit đó, không mặc định `origin/main`.
    2. Kiểm môi trường: biến cấu hình, migration đã chạy, dịch vụ ngoài (mail, scanner, NirmatAI) đang dùng thật hay giả.
    3. Quét code để có danh sách nghi ngờ (skill `hardcode-check`). Đối chiếu ticket và Azure để không trùng bug đã có.
    4. Chạy TC trên web, kèm các case kích hoạt nghi ngờ (skill `manual-run`).
    5. Phân loại kết quả: **lỗi code** (gán dev theo PIC trong Plan), **lỗi môi trường hoặc deploy** (gán devops, không ghi Failed cho case), **tiềm ẩn** (chưa log, ghi vào báo cáo cho dev).

32. **Test tích hợp NirmatAI (Bulk → NirmatAI)** (27/10, skill `nirmatai-check`). Tài liệu gốc: `DTP/dts-agent-workspace/docs/integrations/nirmatai/` (Connection Guide dev v4 của Usman và file OpenAPI, 20 endpoint DTP được gọi).
    - **Luồng**: khách tạo Bulk workspace, upload, map Work Product (WP) → Request audit → SGS Admin link client NirmatAI (trên trang chi tiết request) → **Approve and send** → DTP tạo audit (`POST /audits`), upload, `trigger-ingestion` → chờ từng tài liệu `success` / `failure` (khoảng 2 phút mỗi file) → gán WP.
    - **Approve and send, link/đổi client, Sync, bật/tắt framework là cấu hình NirmatAI dùng chung và không quay lại được**: chỉ làm khi người dùng đồng ý rõ ràng trong tin nhắn; nếu hệ thống chặn, nhờ người dùng tự bấm rồi QA kiểm phần còn lại ở chế độ chỉ đọc.
    - **Khi báo kết quả cho dev / NirmatAI** luôn ghi: `audit_code` (dạng `AUD-4391-000NN`, là mã của NirmatAI, mở tại `/prepare-audit?auditCode=<audit_code>`), `audit_id`, client ID và tên, org ID (dev: 10 "Digital Trust Platform"), standard (dev: 107 `ISO27001-2022-DEMO-DTP`, 35 WP), giờ tạo (UTC), danh sách file và WP.
    - **Phía DTP kiểm**: trạng thái request (Waiting for approval → Sending → Under review), từng lượt gửi (Initial / Additional: Queued → Sent), cột "Processing in NirmatAI" (Ready / lỗi), màn khách hàng, audit log, thông báo. **Phía NirmatAI** QA không có quyền: nhờ Usman kiểm.
    - **Case biên lấy từ tài liệu** (thêm vào TC Bulk upload / Settings): file loại không hỗ trợ (`400 E_INVALID_TYPE`), file trên 100 MiB (phải đi upload session, tối đa 3 GiB), trùng tên trong cùng audit (`409 E_DUPLICATE_DOCUMENTS`), hơn 25 tài liệu (một lần xử lý tối đa 25), đổi WP khi tài liệu đang `running` (bị từ chối), tài liệu `failure` thì DTP phải hiện lỗi, framework của org khác (`400 E_ORG_MISMATCH`), giờ NirmatAI trả dạng `YYYY-MM-DD HH:MM:SS` UTC phải hiện đúng giờ Đài Loan.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v0.8 | 2026-10-27 | Thêm rule 32: test tích hợp NirmatAI (luồng, cấu hình dùng chung, thông tin phải báo, case biên từ Connection Guide dev v4); skill `nirmatai-check` | Người dùng 27/10; NirmatAI Connection Guide v4 |
| v0.7 | 2026-10-26 | Thêm rule 31: mỗi lượt chạy tìm lỗi chủ động theo 4 hướng (quét code, tạo dữ liệu, biên và thời gian, gọi thẳng API); nghi ngờ → case kích hoạt → lỗi / tiềm ẩn; quy trình 5 bước (skill `run-cycle`). **Chờ duyệt.** | Yêu cầu người dùng 26/10 |
| v0.6 | 2026-10-26 | Thêm rule 30: quét giá trị gán cứng trong code (skill `hardcode-check`) trước mỗi lượt chạy. **Chờ duyệt.** | Yêu cầu người dùng 26/10 (dropdown Scope chỉ tải 100 mục) |
| v0.5 | 2026-10-23 | Thêm rule 29: bug người dùng báo khi test tay → log, thêm case vào TC, thêm mẫu vào `rules/bug-patterns.md`. **Chờ duyệt.** | Yêu cầu người dùng 23/10 |
| v0.4 | 2026-10-21 | Thêm rule 27 (case cần email thật: gửi mời, lấy link trước rồi mới chạy) và rule 28 (đối chiếu quyết định mới nhất trước khi ghi bug). **Chờ duyệt.** | FB-100 · FB-101 · lượt chạy web 21/10 |
| v0.1 | 2026-10-02 | Khởi tạo. Rule 2, 5, 6, 7, 9 lấy theo cách làm của đề xuất FEEC Local E2E (v13, 30/09/2026); rule 8 theo yêu cầu "một số yêu cầu cần confirm vẫn cần con người vào". Đề xuất của AI — **chờ duyệt** | Thiết kế trong chat Building 02/10 |
| v0.3 | 2026-10-20 | Rule 8: kết quả ghi thêm vào cột Round N của file TC khi người dùng yêu cầu. Thêm rule 19–26: bảng kết quả Passed/Failed/Blocked/Pending/NA theo Plan; mẫu Remark Failed; bug một nguyên nhân một mã, file bằng chứng kèm ảnh; môi trường và commit; dữ liệu test và tài khoản seed; xác nhận Failed bằng ảnh; ghi Excel bằng COM, không COUNTIF, file đang mở; điều đã gặp ở môi trường local. **Chờ duyệt.** | FB-090 · FB-091 · FB-092 · FB-093 · FB-096 · chạy Customers Round 1 và E2E Wave 1 ngày 19–20/10 |
| v0.2 | 2026-10-02 | Thêm rule 11–18 rút từ dự án thử nghiệm `automation/feec-learning` (chạy thật lần đầu: lỗi `#` trong `.env`, `networkidle`, dữ liệu phụ thuộc môi trường, menu rớt). Đề xuất của AI — **chờ duyệt** | FB-020 |
