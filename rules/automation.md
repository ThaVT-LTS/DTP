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

## Lượt chạy hằng ngày, trạng thái case, bug và báo cáo (27–30/10/2026)

33. **Lượt chạy hằng ngày tự quyết theo rule** (FB-103, 29/10, skill `run-cycle`). Hai lượt mỗi ngày làm việc, khoảng 11:30 và 16:30, mỗi lượt khoảng 1 giờ:
    1. Ghi build đang deploy và commit mới (rule 22).
    2. Đọc tài liệu đầu vào mới (`tests/input`: Plan, UC List, mail, tài liệu dev gửi).
    3. Đọc `bugs.md` và Azure.
    4. Chọn việc làm được:
       - bug Fixed có commit fix nằm trong build đang deploy;
       - case Pending / Blocked đã hết lý do: chạy `tests/tools/unblocked.py`, và tự đọc thêm remark vì công cụ có thể bỏ sót.
    5. Chạy trên web, ghi TC, ticket, Azure (kèm lý do) và register.
    6. Tự quyết theo rule. Chỉ hỏi người dùng tối đa **3 mục**, mỗi mục kèm gợi ý. Chỉ hỏi khi: huỷ bug, đảo ngược bug đã fix hoặc Figma, đổi cấu hình dùng chung, hoặc câu hỏi BA.
    7. **Không dời case chạy được sang lượt sau.** Case chạy được thì chạy ngay trong lượt.

    Kết thúc lượt bằng một tin tóm tắt:
    - build;
    - case Passed / Failed / Pending;
    - bug Verified / Reopened / mới (mã, dev);
    - bảng Chưa fix / Chưa resolve theo dev;
    - **QnA cần push hôm nay**: nhóm theo người cần trả lời (BA, SGS / Xavier, PO, NirmatAI, dev, SGS IT, Plan), câu chặn nhiều case lên trước, mỗi câu một dòng gửi được ngay. Đóng các QnA đã có trả lời từ nguồn mới (mail, UC, Plan, decision log, web hiện tại).

    Người dùng xin ảnh cho QnA thì chụp màn hình web hiện tại, có URL, lưu `tests/evidence/qna-<ngày>/`.
34. **Pending, On hold, Failed: chọn theo lý do** (FB-104, 29–30/10; bổ sung bảng ở rule 19):
    | Lý do | Kết quả |
    |---|---|
    | Chức năng Not started, chưa có trong Plan, hoặc Plan ghi Done mà chưa làm | **On hold**. Remark ghi lý do và UC nào chuyển In progress / Done thì đưa case về Pending |
    | Chức năng đang In progress (dev đang làm) | **Pending**, để công cụ dò còn thấy |
    | Case gắn với một bug đang Open (đã chốt quy tắc, đã giao dev) | **Failed** kèm mã bug, không bao giờ On hold. Fix lên build thì test lại |
    | Chờ câu hỏi đang mở | Pending, ghi mã QnA |

    Mỗi lượt kiểm lại Plan: UC chuyển trạng thái thì đổi kết quả case theo bảng trên. Hai sheet của Plan có thể mâu thuẫn (vd "Plan by UC" ghi Done, "SDLC Plan" ghi In progress). Khi đó không tự chọn: ghi vào remark và đưa vào QnA cho người giữ Plan.
35. **Quyết định trong decision log đè UC cũ** (FB-105, 30/10). Trước khi log một bug suy ra từ UC, đọc decision log của workspace (`knowledge/L1-domain/decision-log.md`, gồm các D mới thêm ngoài file UC) và commit `docs(...)` mới trên origin. File UC gửi khách có thể chưa cập nhật quyết định đã chốt với khách. Ví dụ DC-BUG-05: UC v6.3 ghi "xoá evidence 36 tháng sau archive", nhưng D84 (chốt với khách 28/10) ghi "36 tháng sau upload". Web làm theo D84 nên đó không phải bug. Trường hợp này: đề xuất huỷ bug (rule 37), sửa Expected theo quyết định mới, và nhắc BA sửa UC.
36. **Mã bug: chỉ cấp qua công cụ, kiểm trùng sau khi log** (FB-106, 29/10). Mã mới lấy bằng `python tests/tools/bug_codes.py next <TIỀN TỐ>`. Lệnh này đọc ticket, register, cột Bug của TC và Azure. Không đặt mã bằng tay, không dùng lại mã đã huỷ. Sau khi log, chạy `bug_codes.py check` phải ra 0 lỗi. Tiêu đề và nội dung bug viết tiếng Anh, tạo ticket workspace; Azure chỉ dùng cho bug cũ còn theo dõi.
37. **Huỷ bug: một lý do, ghi ở mọi nơi** (FB-107, 29/10). Chỉ người dùng quyết huỷ, AI chỉ đề xuất kèm căn cứ. Khi đã quyết:
    - ticket: Status Done, Progress "closed, won't fix (<ai>, <ngày>: <lý do>)", và một dòng Dev Notes;
    - Azure: Removed / Closed, comment ghi cùng lý do;
    - register: ghi status huỷ;
    - TC: các case gắn bug đó được sửa Expected và chạy lại.

    Bug đã giao dev thì không tự huỷ chỉ vì chưa có ai nhận.
38. **Báo cáo đếm bug từ `bugs.md`** (FB-107). Các trạng thái dùng: Open, Reopened, Chờ QA (Fixed — awaiting QA), Verified, Huỷ. Không đếm theo Azure.
    - Ticket chỉ được tính **Verified** khi có dòng "QA verified" hoặc "QA Round N: PASS". Ticket Done mà thiếu dòng đó là "Fixed — awaiting QA".
    - Đếm theo mã bug hay theo ticket thì ghi rõ (một bug có thể có ticket BE và FE).
39. **Kết quả chạy trên local và ảnh** (FB-108, 28–30/10):
    - Passed trên local **cùng commit** với web thì tính Passed, remark "Giả lập trên local".
    - **Khác commit** thì vẫn ghi Passed, remark "Passed trên local — cần xác nhận lại trên web", và đưa vào danh sách cùng tên trong báo cáo.
    - Chỉ kết luận bug sau khi chạy trên web. Phát hiện chỉ từ code hoặc chỉ từ local thì gọi là **nghi ngờ** (rule 31).
    - **Ảnh chỉ chụp cho bug**: 1–2 ảnh JPG có URL, để ở `tasks/tickets/evidence/<MÃ>/`. Case Passed không chụp.
40. **Git của workspace** (FB-109, 29–30/10). Trước khi push: `git fetch`, rồi ghép `origin/main` vào (merge, không rebase lịch sử đã có người dùng). Khi xung đột:
    - `bugs.md` và `kanban.md` là file sinh ra: lấy bản của mình rồi chạy lại `scripts/bug-sync.py` và `scripts/kanban-sync.py`.
    - Ticket: giữ trạng thái QA verified (mới hơn ghi chú G4 của dev), nhưng nhận tiêu đề mới và Dev Notes của dev.

    Chỉ push khi người dùng đồng ý. Đọc kỹ commit mới của origin: có thể có quyết định mới (rule 35).

42. **Đọc case / ticket trước khi nhắc tới** (FB-111, 02/11). Không mô tả một mã case, ticket hay bug theo trí nhớ. Trước khi nói case đó kiểm tra gì: mở dòng TC (mã, tên case, Expected, kết quả hiện tại) hoặc file ticket (tiêu đề, trạng thái, người làm) và trích đúng tên. Danh sách mã lấy từ nguồn khác (cột "Chặn" của QnA, báo cáo của agent con) phải kiểm từng mã có tồn tại và đúng nội dung trước khi báo; mã không khớp thì bỏ hoặc ghi rõ "không tìm thấy". Ví dụ minh hoạ phải ghi là giả định, không gắn vào mã thật. Chưa đọc thì nói "chưa đọc case".

43. **QnA: đối chiếu với TC trước khi đưa ra** (FB-112, 02/11). Trước khi liệt kê một câu QnA là "còn mở" hay đưa vào danh sách push: xem từng case trong cột "Chặn" (kết quả hiện tại + Expected). Case đã Passed với Expected trả lời được câu hỏi → đóng QnA, ghi "đã có trả lời qua <case> Passed dd/mm", không đưa ra nữa. Lượt chạy hằng ngày làm bước này cho mọi câu còn mở, không chỉ đóng theo mail / UC / Plan. Câu đã được QA lead gửi mail cho khách → ghi "đã gửi, chờ trả lời", không nhắc lại trong danh sách push. Mỗi câu còn mở phải ghi rõ: hỏi gì, web đang thế nào, đề xuất (Chốt theo web / Hỏi / Đóng / Bug?).
44. **Khách quyết sau cùng** (FB-113, 02/11). Khi câu trả lời của khách (SGS / Xavier / Mao-Chi) khác quyết định của QA lead hoặc team (vd giữ Bulk luôn qua NirmatAI, chuyển nhiều account sang Phase 2): báo xung đột ngay, nêu nguồn và giờ, rồi làm theo khách khi QA lead xác nhận. Đổi lại toàn bộ: TC (kết quả + remark có nguồn), ticket (gỡ hoặc thêm dòng `- Blocked:`), QnA, memory. "agree" trích cả một tin nhiều điểm: ghi rõ điểm nào chắc chắn được xác nhận, điểm nào còn nghi.
45. **Chuyển phase / hoãn** (FB-114, 02/11). Hạng mục chuyển Phase 2: case → On hold, remark "Chuyển Phase 2 (<ai> dd/mm)"; ticket bug giữ nguyên, thêm dòng `- Blocked: … moved to Phase 2` (không huỷ bug). Quay lại Phase 1: đổi dòng đó thành ghi chú lịch sử (không bắt đầu bằng `- Blocked:`), case về Pending / Failed như trước.
46. **Ticket dev đánh Done khi chưa deploy** (FB-115, 02/11). Mỗi lượt: so commit fix với build đang chạy (Portainer). Fix chưa có trong build → báo "chờ deploy", không Verified, không mở lại. Code trên `main` chưa deploy mà lệch tài liệu khách (vd luồng Customer Consultant vào thẳng In Progress) → báo dev ngay kèm nguồn, không đợi deploy rồi mới log bug.
47. **Kiểm số liệu của agent con** (FB-116, 02/11). Báo cáo của agent con (mã ticket, số đếm theo dev, danh sách case) phải đối chiếu lại `bugs.md` / file TC trước khi gửi QA lead. Mã không tồn tại (vd "BE-71") → bỏ và nói rõ đã sửa.
48. **Thao tác trên môi trường dùng chung** (FB-117, 02/11):
    - Không đụng workspace / request QA lead đang test tay; hỏi tên và dặn agent con tránh.
    - "Approve and send" tự động bị chặn bởi bộ kiểm quyền dù QA lead đồng ý → không lách; chuẩn bị sẵn request, đưa QA lead bấm tay.
    - Link NirmatAI client: tìm client có sẵn trước; chỉ tạo client mới tên `[QA] …`, một client cho mỗi Customer Account; không chọn client của người khác (link khoá sau lần gửi đầu).
    - Lỗi NirmatAI (từ chối file, hết lần thử, 503…) test trên local cùng commit web bằng mock có sẵn; không sửa mock khi chưa hỏi.
49. **Trả lời QA lead: ngắn, một bảng** (FB-118, 02/11). Mặc định một bảng phẳng (Mã · Hỏi gì / Việc · Hiện trạng · Đề xuất), không chia nhiều nhóm, không giải thích dài; tiếng Việt trừ khi được yêu cầu câu tiếng Anh để gửi đi. Danh sách dài → đưa số tổng và mục chính trước.

50. **Hỏi luồng hoạt động → bảng theo mẫu của QA lead** (FB-122, 03/11). Khi QA lead hỏi một luồng (ai làm gì ở đâu, trạng thái ra sao), trả lời bằng bảng Excel theo mẫu `docs/templates/flow-table-template.xlsx`, dựng bằng `scripts/flow_table.py`:
    - Cột: **Ở đâu** (Portal, gộp ô) · **Ai làm** (2 cột: Vai trò | Tên tài khoản, gộp ô theo vai trò) · **Làm gì** (đánh số bước theo thứ tự chạy, ghi menu › màn › nút) · **Kết quả** chia 2 cột **Trạng thái của <bên 1>** / **Trạng thái của <bên 2>** (trạng thái mỗi bên thấy sau bước đó, kèm nút chính hiện ra).
    - Nhóm dòng theo Portal rồi Vai trò; vai trò không tham gia ghi "—". Mỗi luồng (vd Marketplace / My consultants) một sheet; không gộp hai luồng vào một bảng có cột ✔/—.
    - Chỉ ghi trạng thái đã thấy trên web; bước chưa chạy ghi "(chưa chạy)", chỗ web lệch ghi "web: … ❌ (mã bug)". Dòng chú thích dưới bảng: request dùng, build, ngày.
    - Lưu file vào `tests/reports/SGS-DTP_<tên luồng>-flow_<dd-mm-yyyy>.xlsx`, trả lời trong chat 1–2 dòng + link file.

51. **Mỗi build mới: bảng độ phủ cho phần thay đổi, không báo "đã test" khi chưa có case** (FB-123, 04/11). Khi có build / commit mới:
    - Đọc diff code (`git diff <build cũ>..<build mới>`), liệt kê **mọi** nút, ô nhập, hộp thoại, upload, giới hạn (ký tự, dung lượng, loại file, quét mã độc), trạng thái mới — theo màn × vai trò × luồng.
    - Đối chiếu từng mục với file TC: đã chạy trên build này / chỉ chạy trên build cũ / có case chưa chạy / **chưa có case**. Mục chưa có case → viết case (rule 41, 50, 51 của tc-authoring) và chạy ngay trong lượt đó, trước các case cũ.
    - Khi QA lead hỏi "đã test chưa": trả lời theo bảng (case nào, build nào, ngày nào); không suy từ code, không trả lời "có" khi chỉ có case ở build cũ.
    - Rule "chỉ chạy lại case liên quan" không áp cho tính năng mới: tính năng mới luôn chạy đủ case.

52. **Tài liệu luồng happy case + mind map** (FB-124, 05/11). Khi được yêu cầu "tạo luồng", "kịch bản smoke test", "mind map": làm theo skill `flow-doc`:
    - Tiếng Anh, mỗi luồng 1 file Word, đánh số theo thứ tự đi luồng (luồng nền trước, nhánh sau), tên không kèm "Review" / ngày; lưu `tests/reports/Flow report/`.
    - Chỉ happy case, ảnh chụp trên web có URL và khung đỏ không đè chữ; luôn có mục "Not tested yet (blocked)" (Entra, SMTP, NirmatAI cert, malware, tính năng chưa có).
    - Không có trang trắng: kiểm bằng `pagecheck.py` trước khi giao.
    - Mind map HTML sinh từ cùng spec với Word; nhánh phụ để dạng planned cho tới khi chụp, khi chụp thì thêm "Alternative paths" vào file Word của luồng đó.

53. **Đọc UC trước khi log bug hay đổi Expected — kể cả khi QA lead đã quyết** (FB-125, 05/11). Trước mỗi bug / Expected / sửa case: tìm dòng UC hiện hành (P1 Use Cases, Decision log, Open Questions) cho đúng vai trò và màn, trích nguyên văn vào ticket. Ý của QA lead ngược UC → báo trước ("UC SRQ-03 ghi ngược lại: …"), chỉ log khi chị vẫn muốn, ghi rõ mâu thuẫn trong ticket. Bài học: IS-BUG-13 (SGS Admin xem clarification) log theo quyết định 04/11, trái UC SRQ-03 / D57 → dev từ chối, QA lead phải huỷ.
54. **Câu hỏi xác nhận của QA lead không phải lệnh làm** (FB-126, 05/11). "… phải không?", "là … à?", "đã log chưa?" → trả lời (có / không + lý do ngắn), đề xuất thay đổi cụ thể, chờ "ok / làm đi / log đi". Không tự sửa ticket, Expected, case, người nhận, hay gộp bug. Ngoại lệ: việc thường kỳ của lượt chạy (ghi kết quả, log bug mới theo rule 33–40). Khi sửa Expected chỉ sửa đúng ý được duyệt, không ghi đè các ý khác của case (05/11: ghi đè cả Expected AR_025 làm mất 3 ý).
55. **Hiện trạng dự án SGS DTP**: đọc `projects/sgs-dtp/current-baseline-2026-11-05.md` trước `profile.md` (UC v6.5 đã duyệt, quy tắc Q42/Q43/C-01–03, 3 nguồn consultant, môi trường, người nhận bug, việc đang dở). Cập nhật file đó (hoặc tạo bản ngày mới) khi có quyết định mới.
56. **Bàn giao giữa các thread (handoff)** (FB-127, 05/11). QA lead giao việc ở nhiều thread. Bắt đầu: đọc các file mới nhất trong `<workspace>/tasks/handoff/` (SGS DTP: `dts-agent-workspace/tasks/handoff/`, ≥ 3 ngày gần nhất hoặc theo chủ đề). Kết thúc / dừng giữa chừng / trước khi context bị tóm tắt: ghi hoặc cập nhật `<yyyy-mm-dd>-<chủ-đề>.md` theo `tasks/handoff/README.md` (Đã làm · Còn dở / chờ ai · Quyết định mới + nguồn · File liên quan). Handoff chỉ trỏ tới nguồn; trạng thái bug vẫn từ `bugs.md`, kết quả case vẫn từ file TC. Quy ước nạp sẵn qua `DTP/CLAUDE.md`.
57. **Sửa màn trên Figma: từng màn, chờ duyệt, nút / tag phải bao hết chữ** (FB-128, 05/11). Làm theo skill `figma-ui-update`: vẽ trên trang QA riêng, không sửa trang designer; xong một màn báo link + đối chiếu UC rồi chờ "ok". Trước khi báo: mọi tag / nút / chip / badge để Hug theo chữ (nền bao hết chữ), chạy kiểm chữ tràn và phần tử đè nhau = 0, chụp lại tự xem. Bài học 05/11: Home gửi đi còn tag "Expires in 47 days", "In progress" tràn chữ khỏi nền, QA lead phải chỉ ra.

## Changelog

| Version | Ngày | Thay đổi | Nguồn |
|---|---|---|---|
| v1.4 | 2026-11-05 | Thêm rule 57: sửa màn Figma từng màn, tag / nút Hug theo chữ, kiểm tràn / đè; skill `figma-ui-update`. **Chờ duyệt.** | FB-128 |
| v1.3 | 2026-11-05 | Thêm rule 56: handoff giữa các thread (`tasks/handoff/`, nạp qua `DTP/CLAUDE.md`). **Chờ duyệt.** | FB-127 |
| v1.2 | 2026-11-05 | Thêm rule 52: tài liệu luồng happy case (Word tiếng Anh, đánh số) + mind map HTML; skill `flow-doc`. **Chờ duyệt.** | FB-124 |
| v1.1 | 2026-11-02 | Thêm rule 42–49: đọc case trước khi nhắc, QnA đối chiếu TC, khách quyết sau cùng, chuyển phase, ticket Done chưa deploy, kiểm số liệu agent con, môi trường dùng chung, trả lời ngắn. **Chờ duyệt.** | Chat QA lead 02/11 |
| v0.9 | 2026-10-30 | Thêm rule 33–40: lượt chạy hằng ngày tự quyết (≤ 3 câu hỏi, QnA cần push); Pending / On hold / Failed theo lý do; decision log đè UC; cấp mã bug bằng `bug_codes.py`; huỷ bug đồng nhất; báo cáo đếm từ `bugs.md`; kết quả local và ảnh chỉ cho bug; git merge origin trước khi push. **Chờ duyệt.** | FB-103 … FB-109 · lượt chạy 27–30/10 |
| v0.8 | 2026-10-27 | Thêm rule 32: test tích hợp NirmatAI (luồng, cấu hình dùng chung, thông tin phải báo, case biên từ Connection Guide dev v4); skill `nirmatai-check` | Người dùng 27/10; NirmatAI Connection Guide v4 |
| v0.7 | 2026-10-26 | Thêm rule 31: mỗi lượt chạy tìm lỗi chủ động theo 4 hướng (quét code, tạo dữ liệu, biên và thời gian, gọi thẳng API); nghi ngờ → case kích hoạt → lỗi / tiềm ẩn; quy trình 5 bước (skill `run-cycle`). **Chờ duyệt.** | Yêu cầu người dùng 26/10 |
| v0.6 | 2026-10-26 | Thêm rule 30: quét giá trị gán cứng trong code (skill `hardcode-check`) trước mỗi lượt chạy. **Chờ duyệt.** | Yêu cầu người dùng 26/10 (dropdown Scope chỉ tải 100 mục) |
| v0.x | 2026-11-05 | Thêm rule 53 (đọc UC trước khi log / đổi Expected), 54 (câu hỏi xác nhận ≠ lệnh làm), 55 (file hiện trạng SGS DTP). | QA lead 05/11 (IS-BUG-13 huỷ, AR_025 ghi đè) |
| v0.5 | 2026-10-23 | Thêm rule 29: bug người dùng báo khi test tay → log, thêm case vào TC, thêm mẫu vào `rules/bug-patterns.md`. **Chờ duyệt.** | Yêu cầu người dùng 23/10 |
| v0.4 | 2026-10-21 | Thêm rule 27 (case cần email thật: gửi mời, lấy link trước rồi mới chạy) và rule 28 (đối chiếu quyết định mới nhất trước khi ghi bug). **Chờ duyệt.** | FB-100 · FB-101 · lượt chạy web 21/10 |
| v0.1 | 2026-10-02 | Khởi tạo. Rule 2, 5, 6, 7, 9 lấy theo cách làm của đề xuất FEEC Local E2E (v13, 30/09/2026); rule 8 theo yêu cầu "một số yêu cầu cần confirm vẫn cần con người vào". Đề xuất của AI — **chờ duyệt** | Thiết kế trong chat Building 02/10 |
| v0.3 | 2026-10-20 | Rule 8: kết quả ghi thêm vào cột Round N của file TC khi người dùng yêu cầu. Thêm rule 19–26: bảng kết quả Passed/Failed/Blocked/Pending/NA theo Plan; mẫu Remark Failed; bug một nguyên nhân một mã, file bằng chứng kèm ảnh; môi trường và commit; dữ liệu test và tài khoản seed; xác nhận Failed bằng ảnh; ghi Excel bằng COM, không COUNTIF, file đang mở; điều đã gặp ở môi trường local. **Chờ duyệt.** | FB-090 · FB-091 · FB-092 · FB-093 · FB-096 · chạy Customers Round 1 và E2E Wave 1 ngày 19–20/10 |
| v0.2 | 2026-10-02 | Thêm rule 11–18 rút từ dự án thử nghiệm `automation/feec-learning` (chạy thật lần đầu: lỗi `#` trong `.env`, `networkidle`, dữ liệu phụ thuộc môi trường, menu rớt). Đề xuất của AI — **chờ duyệt** | FB-020 |
