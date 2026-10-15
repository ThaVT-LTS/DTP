# Cập nhật Rule và Skill viết TC – bản tổng hợp 15/10/2026

Gửi: phiên Claude Code làm việc trên repo `ThaVT-LTS/DTP` (thư mục local `qa-pipeline`).
Từ: phiên chat của Hanna (project Hanna Test).
Thay thế: gói `rule-update_2026-10-13.zip` (toàn bộ nội dung gói đó đã gộp vào file này).

**Việc cần làm:** cập nhật `rules/tc-authoring.md`, `CLAUDE.md`, skill `.claude/skills/tc-authoring/` theo file này. Ghi FB, chạy thử, cho Hanna xem diff, rồi commit và push lên GitHub.
**Không** sửa file TC trong lượt này.

---

## 0. Bối cảnh

- Hai phiên Claude đang viết TC theo hai bộ rule khác nhau:
  - phiên chat: rule 1–47;
  - Claude Code: bộ rule trên máy, chưa có rule 36–47.
- So sánh hai bộ TC:
  - bản chat v0.22: 1.226 case, phủ 78/119 UC;
  - bản Claude Code `v0.2_Phase1`: 1.845 case, phủ 119/119 UC.
- Mỗi bên có điểm mạnh riêng. File này gộp điểm mạnh của cả hai thành **một bộ rule duy nhất trên GitHub**, để hai phiên dùng chung.
- Nguồn hiện hành:
  - UC List v5.4 (13/10);
  - Open Questions Final Confirmation (13/10);
  - Change Management (13/10);
  - Figma DTP-P1 (file key `jluZdAkgifmZndi5hD12tt`);
  - web demo `sgs-dtp-ds-demo-prototype.vercel.app`.
- **GitHub đang ở commit `80e9168`, `rules/tc-authoring.md` bản v0.6.** Bản trên máy mới hơn (v0.8 trở lên). Áp lên bản trên máy, **không** lấy bản GitHub làm nền.

---

## 1. Rule mới (thêm vào mục F của `rules/tc-authoring.md`, sau rule 35)

### Nhóm A – Định dạng và cổng kiểm (36–39)

36. **Người viết.** Ô `Creator` ở mọi sheet và trên Cover ghi tên người chịu trách nhiệm (Hanna), không ghi tên AI hay công cụ. Thuộc tính tác giả của file (`docProps/core.xml`) cũng ghi Hanna. Tên lấy từ `profile.md`; script dựng sheet nhận `--creator`, không có giá trị mặc định.

37. **Không còn `{{…}}`** ở bất kỳ ô nào của file giao.
    - Người dùng → dòng đăng nhập (rule 40).
    - Dữ liệu có sẵn chưa xác định → `[tên]`.
    - Dữ liệu tester nhập → giá trị cụ thể.
    - Địa chỉ → `[URL …]`, định nghĩa ở ô Reference.

38. **Phông Times New Roman 10 ở mức XML**: phông mặc định (font 0), mọi phông trong `styles.xml`, phông theme major và minor, không còn thẻ `scheme`, cỡ ghi `10` (không ghi `10.000000`). Dòng Function Name, Screen Name, Reference của khối thông tin đủ cao để không cắt chữ.

39. **Cổng trước khi giao:** chạy `tc_fix_xlsx.py --fix --creator Hanna`, rồi `tc_check.py --creator Hanna`; cả hai **0 lỗi** mới giao. Sau đó mở file bằng Excel hoặc OnlyOffice, xem qua một sheet mới và một sheet cũ.

### Nhóm B – Cách viết case (40–47)

40. **Dòng đăng nhập ở Pre-condition:** `Login acc <vai trò> <điều kiện>`, **không dùng dấu `;` sau vai trò**.
    - Điều kiện bắt đầu bằng có, chưa có, được, đã… thì viết liền sau vai trò:
      - `Login acc Customer Admin (Linh Tran) chưa có sự kiện nào`
      - `Login acc Customer Viewer (Iris Huang) được gán scope [System], không được gán scope [Organization]`
    - Điều kiện khác nối bằng dấu phẩy:
      - `Login acc Customer Admin của Formosa Chips Inc. (Chen Wei-Ting), ABC Trading Co., Ltd. có evidence …`
    - Màn không cần đăng nhập ghi `Chưa đăng nhập`.

41. **Khi các nguồn lệch nhau** (bổ sung rule 1). Thứ tự ưu tiên:
    1. quyết định chốt của khách hàng (Final Confirmation, decision log);
    2. UC;
    3. tiêu chí chấp nhận của user story;
    4. Figma bản mới nhất;
    5. web demo.

    Cách xử lý:
    - Web đã hiện và hợp lý mà không trái các nguồn trên → ghi theo web.
    - Web có nhiều chức năng hơn UC → vẫn viết theo web. Nếu UC xếp chức năng đó vào Phase 2 thì cột UC ghi mã `P2-…`.
    - UC có mà web và Figma chưa có → vẫn viết case, theo rule 46.
    - Web sai rõ ràng (lỗi chính tả, dữ liệu hai chỗ lệch nhau, phi logic) → Expected ghi điều đúng; case sẽ fail và thành bug.

42. **Open question tinh gọn** (bổ sung rule 13, 23).
    - Chỉ giữ câu hỏi khi các nguồn mâu thuẫn mà không áp được rule 41, hoặc khi chưa có căn cứ nào để viết Expected.
    - Câu đã có câu trả lời thì **ghi câu trả lời vào Expected**, xoá câu hỏi ở case và ở sheet Cần xác nhận.
    - Câu người dùng đã xoá là đã xử lý: không thêm lại, không tô đỏ lại.
    - Mẫu câu hỏi: ngắn, có dấu `?`, nguồn trong ngoặc, một mã Q, vd `… ? (nguồn) → Q-XX-nn`. Ô có câu hỏi **phải tô màu** (rule 13).

43. **Chữ báo lỗi chưa thấy trên web** ghi theo mẫu của ứng dụng, không đặt câu hỏi. Đoán không chắc thì chỉ ghi hành vi (không lưu, ô viền đỏ, có lỗi dưới ô). Ô Reference ghi "chạy thấy khác thì sửa theo web".

    | Tình huống | Mẫu |
    |---|---|
    | Bỏ trống ô nhập chữ | `Enter a/the <trường>.` |
    | Bỏ trống ô chọn, ngày, file | `Choose a <thứ cần chọn>.` |
    | Sai định dạng | `Enter a valid <…>, e.g. <ví dụ>.` |
    | Trùng | `A <đối tượng> with this name already exists.` |

44. **Step ghi rõ thao tác** (bổ sung rule 14):
    - Bước 1 là nhập URL vào thanh địa chỉ hoặc bấm mục ở menu trái.
    - Mỗi bước một thao tác cụ thể: bấm vào đâu, nhập giá trị gì.
    - Tên nút ghi `button [Tên]`.
    - Case chỉ kiểm hiển thị ghi `Nhìn <vùng>`. **Không** ghi "Kiểm tra …" hay "Mở màn …" trong Step.
    - Một case có nhiều kết quả theo bước thì Expected ghi `Sau bước n: …`.

45. **Nhiều vai trò, nhiều portal trong một sheet** (bổ sung rule 24):
    - phía SGS ghi tiền tố `[SGS]` ở Classification I;
    - phía consultant ghi `[Consultant] …`.

    Kết quả hiện ở portal kia (vd khách hàng thấy yêu cầu đã được nhận) kiểm trong cùng case với hành động (rule 27).

46. **Chức năng chưa có thiết kế, hoặc chưa làm ở Phase 1:**
    - tên case bắt đầu `[Phase 2]`, cột UC ghi mã UC gốc;
    - Expected ghi `- Chưa viết Expected: thuộc Phase 2 (<lý do>)`;
    - quyết định ghi rõ "không thuộc Phase 1" thì dùng `[Ngoài Phase 1]`.

47. **Mã TC không bao giờ đánh lại** sau khi file đã giao cho Hanna hoặc đã đưa lên Azure (bổ sung rule 11).
    - Case mới lấy mã tiếp theo.
    - Case bỏ đi không dùng lại mã (dùng rule 50).

### Nhóm C – Rút ra từ bản `v0.2_Phase1` (48–56)

48. **Nguồn để viết Expected** gồm cả **tiêu chí chấp nhận của user story** và **decision log**. Phải đọc hết các nguồn đang có rồi mới coi một chỗ là "chưa có căn cứ" và đặt câu hỏi. Ô Reference của sheet ghi rõ đã dùng nguồn nào.

49. **Viết theo danh sách UC, theo wave.**
    - Trước khi viết, lập bảng độ phủ: mỗi UC Phase 1 của UC List hiện hành có bao nhiêu case chạy được.
    - Mỗi UC phải có **ít nhất một case chạy được**, tức có Expected và không mang tiền tố `[Phase 2]`, `[OUT]`.
    - Wave (theo phân chia ngày 14/10):
      - **Wave 1** (onboarding, setup, evidence): AUTH, ACC, USR, ROL, FWK, SCP, WSP, EVA, EVC, PRF-01, NTF-02, NTF-03.
      - **Wave 2** (Bulk, NirmatAI, Certification, Training): BLK, INT, CFG, CRT, TRN, NTF-04.
      - **Wave 3** (Consulting, Gap Analysis, Cockpit, Audit, Retention): SRQ, GAP, CKP, AUD, RET, MKT, NTF-01.

50. **Case lỗi thời giữ lại với tiền tố `[OUT]`**, không xoá, không đánh lại mã.
    - Vẫn giữ mã UC gốc.
    - Ô Remark (hoặc Expected) ghi lý do và căn cứ, vd `OUT: D57, SGS Admin không còn duyệt yêu cầu`.
    - Case `[OUT]` **không tính** vào Test_Report và bị `tc_check` bỏ qua phần kiểm Expected và câu hỏi.

51. **Expected tự đề xuất** (không có trong nguồn nào, viết theo suy luận hợp lý):
    - tô **màu vàng `FFF2CC`** ở ô UC;
    - giữ câu hỏi ở Open question;
    - đưa vào sheet Cần xác nhận, kèm cột **"Đề xuất mặc định"**.

    Tester vẫn chạy được theo đề xuất; BA chỉ cần xác nhận hoặc sửa.

52. **Mọi câu hỏi ở sheet Cần xác nhận phải có "Đề xuất mặc định"**: phương án nên chọn, kèm lý do ngắn. Vd Q-L-24: "Bỏ checkbox Keep me signed in ở Phase 1, phiên do Microsoft Entra quản lý".

53. **Mức ưu tiên Critical, CHỜ HANNA CHỐT.** Đề xuất: Critical dành cho case bảo mật và phân quyền, phải qua trước khi UAT (vd consultant chưa được duyệt mở workspace bằng URL, dữ liệu nháp lộ sang khách hàng).
    - Nếu Hanna đồng ý: thêm Critical vào dropdown Priority và danh sách hợp lệ của `tc_check.py`.
    - Nếu không: đổi các case Critical về High.

    **Hỏi Hanna trước khi áp rule này.**

54. **Case mới chèn vào đúng nhóm Classification**, không thêm ở cuối sheet.
    - Không để một khu vực bị tách làm hai nơi.
    - Thứ tự trong khu vực: Hiển thị → Nhập liệu → Không thành công → Thành công (rule 4).
    - Test_Report dựng lại theo nhóm (I, II), mỗi khối sheet có dòng Total, và **tổng cuối bảng gồm mọi khối**. Không dùng dòng "Case bổ sung" nằm ngoài tổng.

55. **Một số phiên bản duy nhất:** tên file, ô Version trên Cover và dòng cuối nhật ký Record of change ghi **cùng một số**. Mỗi lần giao thêm một dòng nhật ký, không nhảy số. Đánh số lại thì ghi một dòng nhật ký giải thích.

56. **Một bộ rule duy nhất:** rule, skill, script chỉ sửa trên repo và đẩy lên GitHub. Phiên chat và Claude Code đều đọc từ GitHub; không giữ bản rule riêng ở từng nơi.

---

## 2. Sửa rule đang có

| Rule | Sửa |
|---|---|
| 1 | Thêm thứ tự nguồn của rule 41 và nguồn ở rule 48 |
| 4 | Thêm: case mới chèn đúng nhóm (rule 54) |
| 10 | Case `[OUT]` vẫn giữ mã UC (rule 50) |
| 11 | Dẫn chiếu tới rule 47, 50 |
| 13, 23 | Dẫn chiếu tới rule 42, 43, 51, 52 |
| 14 | Dòng đăng nhập theo rule 40; Step theo rule 44 |
| 18 | Kiểm cả phông ở mức XML (rule 38) |
| 24 | Ví dụ đổi theo rule 40; thêm tiền tố `[Consultant]` (rule 45) |
| Priority | Chờ rule 53 |

---

## 3. Sửa skill `.claude/skills/tc-authoring/`

| File | Sửa |
|---|---|
| `SKILL.md` | Thêm **Bước 0**: lập bảng độ phủ UC theo wave (rule 49) trước khi viết. Bước cuối: chạy cổng kiểm rule 39. Ghi rõ case mới phải chèn đúng nhóm (rule 54) |
| `scripts/tc_fix_xlsx.py` | **Mới** (file kèm theo): kiểm và sửa phông mức XML, Creator, thuộc tính tác giả, chiều cao khối thông tin; báo `{{…}}` |
| `scripts/tc_check.py` | Áp `tc_check_dinh-dang.patch` (thêm `--creator`, gọi `tc_fix_xlsx`). Thêm các phép kiểm ở mục 4 |
| `scripts/tc_add_sheet.py` | Bỏ giá trị mặc định của `--creator` |
| Công cụ chèn case | Dùng `tc_edit_helpers_reference.py` (file kèm theo) làm mẫu: chèn và xoá case mà giữ cụm gộp, mã TC, row height và dựng lại Test_Report theo nhóm; thêm sheet mới kèm khối Test_Report. Chuẩn hoá thành script `tc_rows.py` có tham số dòng lệnh |
| `references/tu-soat.md` | Thêm dòng tự soát cho rule 37–55 |

## 4. Phép kiểm cần thêm vào `tc_check.py`

| Phép kiểm | Rule | Lỗi hay cảnh báo |
|---|---|---|
| Pre-condition có `Login acc <vai trò>;` | 40 | Lỗi |
| Step có dòng bắt đầu bằng "Kiểm tra" hoặc "Mở màn/chi tiết/trang" | 44 | Cảnh báo |
| Case `[OUT]` thiếu mã UC hoặc thiếu lý do | 50 | Lỗi |
| Bỏ qua case `[OUT]` khi kiểm Expected, câu hỏi, Test_Report | 50 | — |
| Ô UC tô vàng mà không có câu hỏi, hoặc có câu hỏi "đề xuất" mà ô UC chưa tô | 51 | Lỗi |
| Câu hỏi trong sheet Cần xác nhận thiếu "Đề xuất mặc định" | 52 | Cảnh báo |
| Cùng một nhóm Classification I xuất hiện ở hai nơi trong sheet | 54 | Lỗi |
| Dòng Test_Report nằm ngoài khối của sheet, hoặc khối không nằm trong tổng cuối bảng | 54 | Lỗi |
| Tên file, ô Version trên Cover, dòng cuối nhật ký khác số nhau | 55 | Lỗi |
| UC Phase 1 không có case chạy được (khi truyền `--uc`) | 49 | Cảnh báo, kèm danh sách theo wave |

## 5. Ghi vào `profile.md` của sgs-dtp (quy ước dự án, không phải rule chung)

- Tên tier hiện kèm tiếng Trung: `Medium · 中`.
- Mở bằng URL scope hoặc workspace không có quyền hay không tồn tại: hiện `This scope doesn’t exist` / `This workspace doesn’t exist`, dòng dưới `It may have been removed, or it belongs to an organisation you can’t see.`
- Mô hình consultant (v5.4, D56): đồng nghiệp cùng công ty là Customer User; consultant do khách hàng thuê là guest trong Customer Portal; consultant do SGS giới thiệu dùng Consultant Portal. Giao diện chỉ ghi "Consultant".
- SGS Admin chỉ xem thông tin cơ bản của yêu cầu tư vấn, không duyệt hay từ chối (D57).
- "Documents" đổi thành "Evidence Library" (D70).
- Giới hạn upload: 20 file mỗi lần, mỗi file 100 MB (D63).
- Tài khoản demo đổi bằng menu Demo, mật khẩu `Demo-Password-01`. Reset dữ liệu trước khi chạy test.
- Wave của Phase 1: như rule 49.

## 6. FB cần ghi khi áp (cấp số thật theo `CLAUDE.md`)

| FB | Nội dung | Rule |
|---|---|---|
| a | Creator ghi Claude | 36 |
| b | Còn `{{…}}` | 37 |
| c | Ô trống, ô gộp hiện Arial | 38 |
| d | Dòng đăng nhập Login acc … | 40 |
| e | Quá nhiều câu hỏi; câu đã xoá bị tô lại | 41, 42 |
| f | Chữ báo lỗi chưa thấy: ghi theo mẫu | 43 |
| g | Step chưa rõ bấm vào đâu | 44 |
| h | UC có mà web chưa có: ghi Phase 2 | 46 |
| i | So sánh v0.22 và v0.2_Phase1: nguồn, độ phủ UC, `[OUT]`, đề xuất mặc định, chèn đúng nhóm, số phiên bản | 48–56 |

---

## 7. Prompt dán cho Claude Code

```
Đọc HUONG-DAN_cap-nhat-rule-skill_2026-10-15.md và áp vào repo này. Làm lần lượt:
1. git pull. Dùng rules/tc-authoring.md đang có trên máy làm nền (không lấy bản v0.6 trên GitHub đè lên).
2. Thêm rule 36–56 vào mục F, sửa các rule ở mục 2; tăng version, thêm dòng changelog.
   Rule 53 (Critical): DỪNG và hỏi tôi đồng ý hay không trước khi áp.
3. Ghi mục 5 vào profile.md của sgs-dtp.
4. Chép tc_fix_xlsx.py vào .claude/skills/tc-authoring/scripts/, áp tc_check_dinh-dang.patch,
   thêm các phép kiểm ở mục 4 vào tc_check.py, sửa SKILL.md, tc_add_sheet.py, references/tu-soat.md theo mục 3.
   Từ tc_edit_helpers_reference.py viết script tc_rows.py (chèn, xoá case giữ mã và cụm gộp; dựng lại Test_Report theo nhóm).
5. Ghi các FB ở mục 6 theo quy trình trong CLAUDE.md.
6. Chạy tc_check.py --creator Hanna --uc <danh sách UC v5.4> trên file SGS-DTP_TestCase_v0_2_Phase1.xlsx.
   Báo số lỗi theo rule. KHÔNG sửa file TC.
7. Cho tôi xem diff. Tôi đồng ý thì commit "rules+skill: rule 36–56 (15/10)" và push lên GitHub.
```

## 8. File kèm theo

| File | Dùng để |
|---|---|
| `tc_fix_xlsx.py` | Script kiểm và sửa định dạng mức XML (rule 36–39) |
| `tc_check_dinh-dang.patch` | Vá `tc_check.py` (đã thử `git apply --check` trên bản ở repo) |
| `tc_edit_helpers_reference.py` | Mã tham khảo để viết `tc_rows.py`; chưa chuẩn hoá, đọc phần chú thích đầu file |
| `CAP-NHAT_2026-10-12_dinh-dang-chung.md` | Hồ sơ nguyên nhân gốc của rule 36–39 |