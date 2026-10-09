# So sánh bản v1.5 với bản Hanna sửa — sheet Scopes (07/10/2026, gửi lúc 13:28)

- Bản gốc: `exports/SGS-DTP_TestCase1_v1.5.xlsx` (AI giao sáng 07/10).
- Bản Hanna sửa: `exports/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx` — file Hanna gửi lúc 13:28, lưu nguyên, không sửa gì. Hanna giữ tên file `SGS-DTP_TestCase1_v1.5.xlsx`; trong thư mục đổi tên để không đè bản gốc.
- Bảng ở mục 1 và mục 4 do script sinh: `exports/_build/v1.5/compare_edit.py`. Góp ý gốc: FB-050, FB-051 trong `feedback/log.md`.
- AI **chưa dựng bản mới**. Mục 6 ghi việc chờ Hanna.

## 1. Hanna đã đổi gì

| | Bản gốc | Bản đã sửa |
|---|---|---|
| Số TC | 137 | 136 |
| TC đổi chữ | | 17 |
| TC bỏ | | 1 |
| TC thêm | | 0 |
| TC đổi chỗ | | 1 |
| TC còn câu hỏi mở | | 76 |
| TC để trống Expected | | 4: Scope_021, Scope_119, Scope_131, Scope_137 |

| TC | Dòng | Cột | Trước | Sau |
|---|---|---|---|---|
| Scope_031 | 43 | Expected result | (trống) | - Hệ thống hiển thị data đúng định dạng, không phân biệt chữ hoa hay không |
| Scope_044 | 56 | Test case name | Calculate Evidence coverage with multiple frameworks |  Evidence coverage có nhiều framework |
| Scope_045 | 57 | Test case name | Calculate Evidence coverage with 2 frameworks |  Evidence coverage có 2 framework |
| Scope_046 | 58 | Test case name | All requirements have mandatory evidence | Tất cả requirement đều có mandatory evidence |
| Scope_047 | 59 | Test case name | No requirements have mandatory evidence | Không có requirement nào có mandatory evidence |
| Scope_048 | 60 | Test case name | Only one framework is linked | Chỉ có 1 framework được gắn link |
| Scope_049 | 61 | Test case name | One framework has 100% and another has 0% | Một framework đạt 100%, một framework đạt 0% |
| Scope_050 | 62 | Expected result | (trống) | - Hiển thị Evidence coverage:— |
| Scope_051 | 63 | Expected result | (trống) | - Hiển thị Evidence coverage = 1/8 × 100 = 12.5% → 13% |
| Scope_052 | 64 | Expected result | (trống) | - Hiển thị Evidence coverage = 1/250 × 100 = 0.4% → 0%. |
| Scope_053 | 65 | Expected result | (trống) | - Hiển thị Evidence coverage = 249/250 × 100 = 99.6% → 100%. |
| Scope_084 | 96 | Expected result | (trống) | - Hiển thị title:<br>"No framework linked yet. Link one to create a workspace and start collecting evidence." |
| Scope_098 | 110 | Expected result | (trống) | - Vẫn hiển thị lựa chọn framword đó nhưng có thông báo đỏ:<br>"[Tên framwork] is already linked to this scope. |
| Scope_100 | 112 | Expected result | (trống) | - Không hiển thị button "Change tier" |
| Scope_104 | 117 | Classification III | Không thành công | Thành công |
| Scope_104 | 117 | Expected result | (trống) | - Hiển thị chọn framwork bình thường |
| Scope_104 | 117 | Open question | Text khoá chỉ nói sửa scope và gỡ framework bị chặn; gắn thêm có bị chặn → Q-S-16 | (trống) |
| Scope_104 | 117 | UC | UC-SCP-006 | (trống) |
| Scope_114 | 125 | Expected result | (trống) | - Sau bước 3: có cảnh báo số requirement tăng và độ phủ sẽ giảm<br>- Sau bước 5: hộp thoại đóng, cột Tier đổi thành Medium |
| Scope_126 | 137 | Expected result | (trống) | - Hiển thị thông tin giống khung Frameworks |

**TC bỏ**

| TC | Khu vực ▸ nhóm ▸ case | Tên case | Expected | Open question |
|---|---|---|---|---|
| Scope_108 | Gỡ framework - Unlink framework ▸ Lối vào ▸ Tìm chức năng gỡ | Kiểm tra lối vào gỡ framework khỏi scope | (trống) | Không có lối vào ở Figma lẫn prototype dù SCP-007 có 8 giờ → Q-S-21 |

**TC đổi chỗ:** Scope_104 nay ở dòng 117 (thứ tự mới: Scope_103 → Scope_105 → Scope_104 → Scope_106).

Kiểm nhanh: TC thiếu UC: Scope_104.

Sheet khác: không ô nào đổi nội dung (không tính ô công thức).

Tóm lại: Hanna điền Expected cho 11 TC đang để trống (10 TC vẫn giữ câu hỏi ở cột Open question), đổi 6 tên case tiếng Anh sang tiếng Việt, bỏ Scope_108, chuyển Scope_104 từ nhóm Không thành công sang nhóm Thành công. TVP_ID giữ nguyên, cột No. đánh lại 1 → 136.

## 2. Điều AI hiểu từ các chỗ sửa — chờ Hanna xác nhận

Chưa điều nào được đưa vào rule. Ba điều đầu khác rule hoặc quyết định đang ghi trong thư mục, nên cần Hanna nói rõ.

| # | Hanna làm | AI hiểu là | Đang khác với | Câu cần Hanna trả lời |
|---|---|---|---|---|
| 1 | Điền Expected theo hệ thống đang chạy cho chỗ UC, Figma chưa nói, và vẫn giữ câu hỏi (bản v1.4: 8 TC; bản này: 10 TC) | Cách viết của Hanna: Expected tạm theo hệ thống đang chạy, câu hỏi giữ lại tới khi SGS xác nhận | `rules/tc-authoring.md` rule 1 ("không bao giờ lấy hành vi của prototype làm kết quả mong đợi") và rule 13 (chưa có căn cứ thì để trống) | Sửa rule 1 và 13 theo cách này, đúng không? Khi đó AI điền tiếp các TC còn trống theo hệ thống đang chạy |
| 2 | Case biên của Evidence coverage ghi phép tính và kết quả: 12.5% → 13%, 0.4% → 0%, 99.6% → 100% | Hanna chọn cách A của FB-048: giá trị tính toán ghi phép tính và kết quả, kèm câu hỏi | Quyết định ngày 05/10 trong `profile.md`: giá trị tính toán không ghi cách tính trong TC | Bỏ quyết định 05/10, theo cách A, đúng không? |
| 3 | Đổi 6 tên case Evidence coverage từ tiếng Anh sang tiếng Việt | File TC của SGS DTP viết tiếng Việt | `profile.md`: "Ngôn ngữ viết file TC: tiếng Anh" (quyết định 05/10) | Sửa `profile.md` thành tiếng Việt, đúng không? |
| 4 | Bỏ Scope_108 (Gỡ framework: Expected trống, không có lối vào trên Figma lẫn prototype) | Case không chạy được và chưa có Expected thì không để trong file TC, chỉ giữ câu hỏi | Rule 13 đang cho phép viết TC để trống Expected kèm câu hỏi | Xem câu A/B ở mục 5 |
| 5 | Chuyển Scope_104 sang nhóm Thành công, Expected "Hiển thị chọn framwork bình thường", bỏ câu hỏi Q-S-16 | Trên hệ thống đang chạy, scope đang có audit vẫn gắn thêm framework được | — | Không cần trả lời; AI ghi vào danh sách câu hỏi là phần 3 của Q-S-16 có câu trả lời theo hệ thống đang chạy |

## 3. Chỗ cần Hanna xem lại — AI không tự sửa

| TC | Ô | Đang ghi | Vì sao cần xem |
|---|---|---|---|
| Scope_114 (Hạ tier) | Expected | - Sau bước 3: có cảnh báo số requirement tăng và độ phủ sẽ giảm<br>- Sau bước 5: hộp thoại đóng, cột Tier đổi thành Medium | Giống hệt Expected của Scope_113 (Nâng tier), chỉ đổi High thành Medium. Case này hạ từ High xuống Medium nên số requirement giảm, không tăng; Step chỉ có 4 bước, không có bước 5. Câu hỏi "Hạ tier có cảnh báo gì" (Q-S-22) vẫn còn ở cột Open question |
| Scope_100 (Chọn framework không phân tier) | Expected | - Không hiển thị button "Change tier" | Step dừng ở hộp thoại Link a framework, còn nút Change tier nằm ở bảng Frameworks sau khi gắn xong. Ý Hanna là phần chọn tier không hiện trong hộp thoại, hay dòng framework đó không có nút Change tier? |
| Scope_104 (Gắn thêm framework khi scope đang có audit) | UC · Step | UC trống · Step dừng ở "2. Bấm nút gắn framework" | Ô UC bị trống sau khi sửa (trước là UC-SCP-006); `tc_check.py` báo lỗi thiếu UC. Case nằm ở nhóm Thành công nhưng Step chưa có bước chọn framework và bấm Link and create workspace |
| Scope_098 | Expected | - Vẫn hiển thị lựa chọn framword đó nhưng có thông báo đỏ:<br>"[Tên framwork] is already linked to this scope. | Gõ nhầm "framword", "framwork"; thiếu dấu ngoặc kép đóng |
| Scope_126 (Khối Summary) | Expected | - Hiển thị thông tin giống khung Frameworks | Chưa nói giống ở thông tin nào (tên framework, %, số requirement?). FB-034 của Hanna: không viết lửng lơ ở Expected |
| Scope_031 | Expected | - Hệ thống hiển thị data đúng định dạng, không phân biệt chữ hoa hay không | "đúng định dạng" chưa nói thấy gì. Gợi ý: "- Bảng hiện các scope có tên chứa [từ khóa], không phân biệt chữ hoa, chữ thường" |
| Scope_044, Scope_045 | Tên case | " Evidence coverage có nhiều framework", " Evidence coverage có 2 framework" | Có một khoảng trắng ở đầu ô |
| Scope_044 → Scope_049 | Tên case | vd "Chỉ có 1 framework được gắn link" | 6 tên case này không mở đầu bằng "Kiểm tra…" như các case khác của sheet. Để vậy hay thêm cho đồng nhất? |
| Scope_052, Scope_053 | Expected | "… → 0%." · "… → 100%." | Có dấu chấm cuối câu, các Expected khác không có |
| Scope_050 | Expected | - Hiển thị Evidence coverage:— | Thiếu khoảng trắng sau dấu hai chấm (Scope_040 ghi "Belongs to: —") |

## 4. File sau khi lưu bằng ONLYOFFICE

| Kiểm | Kết quả |
|---|---|
| Ô khác Times New Roman 10 | Scopes: 18 ô (K39, K62 → K65, K96, K117, K125, K130, H56 → H61, E130, C142, C148) |
| Ô có chữ dạng tổ hợp (chưa NFC) | Scopes: 7 ô (K43, K96, K110, K112, K117, K137, H60) |
| Ô bắt đầu bằng - + = @ thiếu dấu nháy đơn | không có |
| Màu nền ngoài bảng màu | Scopes: nền trắng (theme 0) ở 33 ô, dòng 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 96, 117; Scopes: nền vàng (indexed 5) ở 24 ô, dòng 130, 142, 148 |
| Công thức ra lỗi | Test_Report: 54 ô, vd E29 = #REF! |
| Ô Open question tô lệch | Scopes: W117 (hết câu hỏi, còn tô) |

Giải thích:

- **Test_Report có 54 ô `#REF!`** ở ba dòng: dòng "Gỡ framework - Unlink framework" (dòng 29), dòng Total của Scopes (dòng 40) và dòng Total cuối (dòng 69). Nguyên nhân: khu vực Gỡ framework chỉ có một dòng TC là Scope_108; khi dòng đó bị xoá, công thức đếm của dòng 29 mất vùng tham chiếu, kéo theo hai dòng Total. Xoá một dòng trong khu vực còn nhiều dòng thì không sao; xoá dòng cuối cùng của một khu vực thì phải dựng lại Test_Report. Khối tổng kết đầu sheet Scopes vẫn đúng (đếm 136).
- **18 ô về phông Arial**: đều là ô Hanna vừa sửa hoặc vừa tô màu. Trong file, kiểu của 18 ô này không còn khai phông riêng nên ô lấy phông mặc định của file (kiểu Normal), mà phông đó là Arial 10. Bốn ô Hanna cũng sửa nội dung (K43, K110, K112, K137) vẫn giữ Times New Roman, nên việc sửa chữ tự nó không làm mất phông. AI chưa biết thao tác nào làm mất phông — cần hỏi Hanna (mục 6).
- **7 ô có chữ dạng tổ hợp**: do bộ gõ, mắt thường không thấy khác; script tự chuẩn hoá lúc dựng file.
- **Nền trắng 33 ô**: khác "không tô nền" (nhìn giống nhau trên nền trắng, nhưng ô có màu nền riêng). **Nền vàng 24 ô**: ba dòng Hanna đánh dấu chưa hiểu.
- Còn nguyên sau khi lưu bằng ONLYOFFICE: logo ở Cover, dropdown Priority và Result ở cả 4 sheet TC, ô gộp, độ rộng cột, công thức khối tổng kết, dấu nháy đơn đầu ô. Login, Users, Profile, Cover, Cần xác nhận không đổi nội dung.

## 5. Ba case Hanna chưa hiểu (FB-051)

Cả ba là case **để trống Expected vì chưa ai chốt kết quả đúng**, viết ra để giữ chỗ cho một câu hỏi. Chữ ở ô nhóm và ô Step quá cụt nên không đọc ra ý.

| TC | Ý của case | Vì sao Expected trống | Chỗ AI viết chưa đạt | Đề xuất |
|---|---|---|---|---|
| Scope_119 · Vai trò trong danh sách | Mở hộp thoại Assign users, xem danh sách người để tick gồm người thuộc vai trò nào: chỉ Customer User, hay có cả Customer Viewer và người chưa kích hoạt | UC ghi chỉ cấp quyền cho Customer User; ghi chú ngày 01/10 về hệ thống đang chạy thấy cả Customer Viewer và người "invitation pending" trong danh sách → Q-S-23 | Step 3 ghi "Đối chiếu vai trò của từng người", nhưng hộp thoại chỉ hiện tên và email, không hiện vai trò. Hai ý "không có Customer Admin" và "người chưa kích hoạt" đã có ở Scope_118 | Bỏ Scope_119; thêm một dòng vào Expected của Scope_118: "- Có Customer Viewer trong danh sách" hoặc "- Không có Customer Viewer trong danh sách", theo điều Hanna thấy trên hệ thống |
| Scope_131 · Customer Viewer | Đăng nhập bằng tài khoản Customer Viewer (vai trò chỉ xem), xem người này có vào được màn Scopes và chi tiết scope không; vào được thì có nút tạo, sửa không | UC không ghi Customer Viewer trong các vai trò được xem scope, nhưng hệ thống cho gán Viewer vào scope → Q-S-24. `bo-cuc-sheet_uc-v4.md` (05/10) ghi mặc định theo UC List v4: không mở được | Ô cấp IV ghi "Quyền xem"; Step không nói xem cái gì | Viết lại như hai case Customer User phía trên (Scope_127, Scope_129). Nhóm: Danh sách và chi tiết ▸ Mở màn Scopes. Step: "1. Tìm mục Scopes trên menu / 2. Mở màn Scopes / 3. Bấm tên một scope để mở chi tiết". Expected: Hanna điền theo điều thấy trên hệ thống |
| Scope_137 · Ghi vết - Audit log | Làm các thao tác thay đổi dữ liệu trên scope (tạo, sửa, gắn framework, gán người dùng), rồi mở màn nhật ký hoạt động (audit log) xem hệ thống có ghi lại từng thao tác không: ai làm, làm gì, lúc nào | UC chỉ ghi "thao tác nhạy cảm được ghi lại", không kể thao tác nào → Q-S-27 | Step ghi "Mở Audit Logs": tên màn AI viết từ ngày 01/10, nay không tìm lại được căn cứ. Sheet Login ghi "Audit Trail", sheet Users ghi "nhật ký hoạt động của tổ chức" — ba tên cho một màn, chưa tên nào được kiểm chứng | Customer Portal có màn nhật ký thì viết lại theo đúng tên màn, mỗi thao tác một dòng Expected. Chưa có màn đó thì bỏ case, chỉ giữ câu hỏi, như Scope_108 |

Scope_021 (Quá giới hạn ký tự) cùng kiểu: Step ghi "dài hơn giới hạn" khi chưa ai biết giới hạn là bao nhiêu, Expected trống.

**Câu cần Hanna chọn** cho loại case này (chưa có Expected, tester không tự xác định được kết quả trên hệ thống):

- **A.** Giữ trong file TC, AI viết lại cho rõ nhìn gì, so với gì.
- **B.** Bỏ khỏi file TC, chỉ giữ ở danh sách câu hỏi (`tests/design/cau-hoi_Scopes.md`), như Hanna đã làm với Scope_108.

## 6. Việc tiếp theo — chờ Hanna

1. Chọn A hoặc B ở mục 5, và cho biết ý với 3 đề xuất của từng case.
2. Trả lời 3 câu ở mục 2 (dòng 1, 2, 3).
3. Cho AI biết Hanna sửa 18 ô ở mục 4 bằng cách nào: gõ thẳng vào ô, hay chép từ ô khác hoặc từ chỗ khác rồi dán vào? Biết cách thì mới chặn được việc ô quay về Arial.
4. Khi Hanna bảo dựng, AI dựng bản kế tiếp từ file Hanna gửi: giữ mọi chỗ Hanna sửa; đưa 18 ô về Times New Roman 10; chuẩn hoá dạng chữ; dựng lại Test_Report; bỏ nền trắng và nền vàng; điền lại UC-SCP-006 cho Scope_104; sửa các chỗ ở mục 3 theo ý Hanna.
