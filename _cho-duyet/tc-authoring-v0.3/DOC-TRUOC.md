# Skill tc-authoring v0.3 — chờ chép vào `.claude/skills/tc-authoring/`

> **07/10/2026 — ĐỪNG chép cả thư mục `skill/` nữa.** Lệnh `Copy-Item` ở mục "Cách cài" bên dưới đã lỗi thời.
> Ngày 05/10 skill đang cài ở `.claude/skills/tc-authoring/` đã được cập nhật bằng `CAP-NHAT_2026-10-05_ban-gop.md` (Hanna duyệt ngày 05/10, trừ các phần ghi chờ duyệt trong changelog), đi theo nhánh khác với 8 file ở đây.
> Chép đè sẽ làm mất các thay đổi ngày 05/10 ở `SKILL.md`, `references/format.md`, `references/templates.md`, `scripts/tc_check.py`, `scripts/tc_build_xlsx.py`
> (vd bỏ sheet `_Data`, `_Labels`; tham số `--lang en`).
>
> Ba file ở đây **không có** trong skill đang cài và vẫn dùng được: `scripts/tc_add_sheet.py`, `scripts/tc_restyle.py`, `scripts/tc_palette.py`.
> Bộ script dựng bản v1.5 (`projects/sgs-dtp/exports/_build/v1.5/`) đang gọi `tc_add_sheet.py` và `tc_palette.py` từ thư mục này, nên **chưa xoá thư mục này**.
> Việc đưa ba script đó vào skill đang cài: chờ Hanna quyết, ghi ở `docs/VIEC-CON-MO.md`.

Ngày: 2026-10-02 · Nguồn: FB-019 · FB-016 · Trạng thái: **chờ duyệt**

## Vì sao nằm ở đây
Phiên chat chạy trên đám mây ghi được vào thư mục `qa-pipeline`, nhưng **không được phép ghi vào `.claude/`** của máy. Tám file dưới `skill/` là bản v0.3 của skill `tc-authoring`; chúng chỉ có hiệu lực sau khi được chép vào `.claude/skills/tc-authoring/`.

`rules/tc-authoring.md` v0.3 (rule 24) đã nằm đúng chỗ, không cần chép.

## Cách cài
PowerShell, đứng ở gốc thư mục `qa-pipeline`:

    Copy-Item -Recurse -Force _cho-duyet\tc-authoring-v0.3\skill\* .claude\skills\tc-authoring\

Hoặc mở Claude Code tại thư mục này và nói: "chép `_cho-duyet/tc-authoring-v0.3/skill` vào `.claude/skills/tc-authoring`".

Máy cần Python có `openpyxl` và `lxml` (`pip install openpyxl lxml`).

## Kiểm sau khi chép

    python .claude/skills/tc-authoring/scripts/tc_check.py projects/sgs-dtp/exports/SGS-DTP_TestCase.xlsx --like Login

Kết quả đúng: `2 sheet · 17 UC được phủ · 0 lỗi · 0 cảnh báo`.

Trước khi chép, script kiểm đang cài (v0.2) vẫn dùng bảng màu cũ (tiêu đề `17324D`) nên báo lỗi màu trên file mới. Lỗi đó do script cũ, không do file.

Chép xong thì xoá thư mục `_cho-duyet/tc-authoring-v0.3/` (kể cả `__pycache__` — bộ đệm Python sinh ra khi chạy thử script ở đây, không cần chép).

## Danh sách file

| File | Mới / sửa | Thay đổi |
|---|---|---|
| `SKILL.md` | sửa (v0.2 → v0.3) | Bước 6 có ba đường dựng, mặc định là thêm sheet vào file mẫu của dự án; bước 7 dùng `--like` |
| `references/format.md` | sửa | §4: một màu nền tiêu đề `00B0F0`, chữ `363A45`, Times New Roman 10 mọi ô; bố cục theo file mẫu |
| `references/templates.md` | sửa | Lệnh dựng file theo hai trường hợp: có file mẫu, chưa có file mẫu |
| `scripts/tc_palette.py` | mới | Một nguồn phông và bảng màu cho mọi script. Đổi màu tiêu đề: sửa `HEAD_FILL` rồi chạy `tc_restyle.py` |
| `scripts/tc_add_sheet.py` | mới | Thêm sheet TC vào file mẫu, nhân bản form của một sheet TC đã có; giữ logo, dropdown; dựng lại sheet báo cáo |
| `scripts/tc_restyle.py` | mới | Đưa cả file về một phông, một bảng màu; tuỳ chọn chép kiểu ô, đổi tên cột, sửa vùng đếm khối tổng kết |
| `scripts/tc_check.py` | sửa | `--like`; kiểm mọi kiểu ô đang dùng (cả ô trống, kiểu cột/dòng, chữ từng đoạn, màu theme/indexed); khối tổng kết đếm thiếu dòng |
| `scripts/tc_build_xlsx.py` | sửa | Dùng `tc_palette.py`; sửa nhãn `UC-[NGOÀI UC]`; chiều cao dòng theo nội dung |

## File TC hiện tại được dựng bằng lệnh nào

    python tc_add_sheet.py --book <file mẫu người dùng gửi 01/10>.xlsx --like Login --sheet Scopes --data projects/sgs-dtp/exports/_flat/Scopes.tsv \
        --function "SCP-L0001_Quản lý scope" --screen "Scopes · Customer Portal" --creator "AI (Claude)" --created "01/10/2026" \
        --source "Figma SGS-DTP-DS · Screens 05 Scopes · prototype" --report Test_Report \
        --change "01/10/2026|1.0|Login, Scopes|A|Tạo mới|UC List v2.1, Figma" --out step1.xlsx
    python tc_restyle.py step1.xlsx --out SGS-DTP_TestCase.xlsx \
        --copy-style "*!F11>W11,X11" --copy-style "*!F12>W12,X12" --rename-header "Chờ text=Open question" --fix-summary \
        --change "02/10/2026|1.1|Tất cả sheet|M|Một màu, một phông|FB-016, FB-019" \
        --change "02/10/2026|1.1|Login|M|Sửa vùng đếm tổng kết|FB-019"
