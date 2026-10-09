# Cách dựng lại `SGS-DTP_TestCase1_v1.5.xlsx` (07/10/2026)

Thư mục này giữ đúng bộ script và số đo đã dùng để dựng bản v1.5 từ bản v1.4 Hanna gửi, để chat khác dựng lại hoặc sửa tiếp được (vd đổi thứ tự nhóm, thêm bớt case) mà không phải viết lại từ đầu. Đây là script riêng cho bản này, chưa phải script của skill; việc đưa thành script chung ghi ở `docs/VIEC-CON-MO.md`.

Mọi script làm thẳng trên XML của file `.xlsx`, không lưu bằng openpyxl (openpyxl làm rơi logo và dropdown). Cần Python có `lxml`; `tc_add_sheet.py` và `tc_palette.py` lấy ở `_cho-duyet/tc-authoring-v0.3/skill/scripts/` (đổi chỗ thì đặt biến môi trường `TC_LIB`).

## File

| File | Việc |
|---|---|
| `scopes_v15.py` | **Nội dung** sheet Scopes bản v1.5: phần Hanna sửa lấy từ v1.4 kèm danh sách chỗ chạm vào (`TOUCH`, `UC_FILL`), 4 case biên Evidence coverage (`EC_NEW`), phần viết lại (`part_b`), case bỏ kèm lý do (`REMOVED`). Muốn sửa nội dung thì sửa ở đây |
| `flat.py`, `xl.py` | Đọc một sheet TC thành bảng phẳng (ô gộp được điền xuống) |
| `build_v15.py` | Dựng file: phông Times New Roman 10 cho mọi kiểu ô, dựng lại vùng dữ liệu Scopes, tô dòng còn câu hỏi mở, dấu nháy đơn đầu ô, dựng lại Test_Report, sửa chỗ trỏ sang TC của Scopes, thêm dòng ở Cover, dựng lại bảng chuỗi dạng NFC |
| `lo_measure.py` | Nhờ LibreOffice đo chiều cao dòng vừa chữ và tính giá trị công thức (cần `soffice` và `python3-uno`) |
| `measure_v1.5.json` | Số đo đã dùng cho bản v1.5. Đổi nội dung thì phải đo lại |
| `verify_v15.py` | Kiểm bản dựng ở mức XML và so với v1.4: phông, màu, dấu nháy, nội dung Scopes đúng bảng phẳng, gộp ô, công thức, Test_Report, các sheet khác không đổi |
| `make_docs.py` | Sinh `exports/_flat/Scopes_v1.5.tsv` và `tests/design/so-sanh_v1.4-v1.5.md` |
| `compare_edit.py` | So một file TC người dùng đã sửa tay với bản gốc: từng ô theo TVP_ID, case bỏ, thêm, đổi chỗ; kiểm định dạng sau khi lưu (phông, dạng chữ, dấu nháy đơn, màu nền, công thức ra lỗi). Chạy mỗi khi Hanna gửi lại file đã sửa, trước khi làm tiếp |
| `make_questions.py` | Sinh `tests/design/cau-hoi_Scopes.md`: 28 câu hỏi Q-S, TC nào đang chờ câu nào. Câu hỏi, căn cứ, ghi nhận nằm trong script; có trả lời thì sửa ở đó rồi chạy lại |

## Lệnh (đứng ở gốc `qa-pipeline`; `T` là một thư mục tạm ngoài `qa-pipeline`)

    B=projects/sgs-dtp/exports/_build/v1.5
    E=projects/sgs-dtp/exports
    python $B/flat.py $E/SGS-DTP_TestCase1_v1.4.xlsx Scopes $T/v1.4.Scopes.json
    python $B/scopes_v15.py $T/v1.4.Scopes.json $T/scopes_v15.json
    python $B/build_v15.py --book $E/SGS-DTP_TestCase1_v1.4.xlsx --rows $T/scopes_v15.json --out $T/pass1.xlsx
    python $B/lo_measure.py $T/pass1.xlsx $T/measure.json --rows "Scopes:13-149" --rows "Cover:11-19:raw" --rows "Test_Report:4-69:raw" --values Scopes --values Test_Report
    python $B/build_v15.py --book $E/SGS-DTP_TestCase1_v1.4.xlsx --rows $T/scopes_v15.json --measure $T/measure.json --out $T/SGS-DTP_TestCase1_v1.5.xlsx --log $T/build_log.json
    python $B/verify_v15.py $E/SGS-DTP_TestCase1_v1.4.xlsx $T/SGS-DTP_TestCase1_v1.5.xlsx $T/scopes_v15.json
    python $B/make_docs.py $T/scopes_v15.json $T/v1.4.Scopes.json $E/SGS-DTP_TestCase1_v1.4.xlsx $T/build_log.json $T/out

- Nội dung không đổi thì bỏ hai lệnh `pass1` và `lo_measure`, dùng luôn `--measure $B/measure_v1.5.json`.
- Số đo của `lo_measure.py` cho sheet Cover và Test_Report là chiều cao thô; bản v1.5 đã làm tròn tới 0.25 pt và không để dưới 15.75 pt.
- Kết quả đúng của `verify_v15.py`: `0 lỗi`.
- Đã chạy lại cả chuỗi lệnh trên ngày 07/10 từ một bản sao của thư mục. Dựng với `--measure $B/measure_v1.5.json`: file ra giống bản đã giao ở cả 21 phần bên trong, chỉ khác giờ ghi trong file nén nên mã md5 của file khác; `_flat/Scopes_v1.5.tsv` và `so-sanh_v1.4-v1.5.md` giống từng byte. Số đo mới của `lo_measure.py` trùng số đo đã lưu ở sheet Scopes và ở giá trị công thức; ở Cover và Test_Report lệch 0.01 pt vì là chiều cao thô chưa làm tròn.

## Khi Hanna gửi lại file đã sửa

    python $B/compare_edit.py $E/SGS-DTP_TestCase1_v1.5.xlsx <file Hanna gửi>.xlsx Scopes --out $T/so-sanh.md
    python $B/make_questions.py <file Hanna gửi>.xlsx projects/sgs-dtp/tests/design/cau-hoi_Scopes.md "<ghi chú về file>"

Bản Hanna sửa ngày 07/10 (`$E/SGS-DTP_TestCase1_v1.5_Hanna-sua-0710.xlsx`) đã được so; kết quả ở `tests/design/so-sanh_v1.5-ban-Hanna-sua-0710.md`.
Bản kế tiếp phải dựng **từ file Hanna gửi** (giữ mọi chỗ Hanna sửa), không chạy lại `scopes_v15.py` từ bản v1.4: `scopes_v15.py` chỉ mô tả nội dung của bản v1.5.
