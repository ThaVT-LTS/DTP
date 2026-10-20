# RTM — ma trận truy vết

Sinh bởi `rtm_check.py` lúc 2026-09-28 07:55. Không sửa tay.

Nguồn: examples/test-basis-demo.md, examples/design-UC-DEMO-001.md · Test case: examples/cases-demo.md

## Tóm tắt

| Chỉ số | Giá trị |
|---|---|
| ID trong test basis + thiết kế | 78 |
| Đã có TC | 73 |
| Loại trừ có lý do | 5 |
| Lỗ hổng (chưa có TC) | 0 |
| TC đang dùng | 46 (Redirect 9 · Validation 21 · Function 16) |
| Theo loại | Positive 18 · Negative 22 · Abnormal 6 |
| TC deprecated | 0 |
| Lỗi | 0 |
| Cảnh báo | 0 |

## Lỗi

Không có.

## Số TC theo UC

| UC | Redirect | Validation | Function | Tổng |
|---|---|---|---|---|
| UC-DEMO-001 | 9 | 21 | 16 | 46 |

## Truy vết ID → TC

### (dùng chung)

| ID | Loại | TC |
|---|---|---|
| PM-USER-01 | PM | UC-DEMO-001-TC-F01, UC-DEMO-001-TC-R01 |
| PM-USER-02 | PM | UC-DEMO-001-TC-F09, UC-DEMO-001-TC-R04, UC-DEMO-001-TC-R05 |
| PM-USER-03 | PM | UC-DEMO-001-TC-F10 |
| ST-USER-01 | ST | UC-DEMO-001-TC-F01 |
| ST-USER-02 | ST | — [THUỘC UC-DEMO-005] |
| ST-USER-03 | ST | — [THUỘC UC-DEMO-006] |
| ST-USER-04 | ST | — [THUỘC UC-DEMO-004] |
| ST-USER-05 | ST | — [THUỘC UC-DEMO-004] |
| ST-USER-06 | ST | — [THUỘC UC-DEMO-005] |

### UC-DEMO-001

| ID | Loại | TC |
|---|---|---|
| UC-DEMO-001-NV-01 | NV | R01 |
| UC-DEMO-001-NV-02 | NV | R02 |
| UC-DEMO-001-NV-03 | NV | R03 |
| UC-DEMO-001-NV-04 | NV | R04 |
| UC-DEMO-001-NV-05 | NV | R06 |
| UC-DEMO-001-NV-06 | NV | R07, R08 |
| UC-DEMO-001-NV-07 | NV | R09 |
| UC-DEMO-001-FD-01 | FD | V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V21 |
| UC-DEMO-001-FD-02 | FD | V13, V14, V15, V16, V17, V18, V19 |
| UC-DEMO-001-FD-03 | FD | R09, V20 |
| UC-DEMO-001-MS-01 | MS | V03, V04 |
| UC-DEMO-001-MS-02 | MS | V05, V08, V09 |
| UC-DEMO-001-MS-03 | MS | V10, V11 |
| UC-DEMO-001-MS-04 | MS | V13 |
| UC-DEMO-001-MS-05 | MS | V14, V15, V16, V19 |
| UC-DEMO-001-MS-06 | MS | F04, F15 |
| UC-DEMO-001-MS-07 | MS | R06 |
| UC-DEMO-001-MS-08 | MS | F06 |
| UC-DEMO-001-MS-09 | MS | F07 |
| UC-DEMO-001-MS-10 | MS | F03 |
| UC-DEMO-001-MS-11 | MS | F08 |
| UC-DEMO-001-MS-12 | MS | R07, R08 |
| UC-DEMO-001-MS-13 | MS | V20 |
| UC-DEMO-001-MS-14 | MS | V21 |
| UC-DEMO-001-MF-01 | MF | F01 |
| UC-DEMO-001-MF-02 | MF | F01 |
| UC-DEMO-001-MF-03 | MF | F01 |
| UC-DEMO-001-MF-04 | MF | F01 |
| UC-DEMO-001-AF-01 | AF | F06 |
| UC-DEMO-001-EF-01 | EF | F07 |
| UC-DEMO-001-EF-02 | EF | F08 |
| UC-DEMO-001-BR-01 | BR | F01, F04, F05, F06, F15 |
| UC-DEMO-001-BR-02 | BR | F02, F03 |
| UC-DEMO-001-SE-01 | SE | F01 |
| UC-DEMO-001-SE-02 | SE | F11 |
| UC-DEMO-001-SE-03 | SE | F12 |
| UC-DEMO-001-EP-01 | EP | V01 |
| UC-DEMO-001-EP-02 | EP | V02 |
| UC-DEMO-001-EP-03 | EP | V03 |
| UC-DEMO-001-EP-04 | EP | V04 |
| UC-DEMO-001-EP-05 | EP | V10 |
| UC-DEMO-001-EP-06 | EP | V11 |
| UC-DEMO-001-EP-07 | EP | V12 |
| UC-DEMO-001-EP-08 | EP | F01 |
| UC-DEMO-001-EP-09 | EP | V13 |
| UC-DEMO-001-EP-10 | EP | V14 |
| UC-DEMO-001-EP-11 | EP | V15 |
| UC-DEMO-001-EP-12 | EP | V16 |
| UC-DEMO-001-EP-13 | EP | V17 |
| UC-DEMO-001-EP-14 | EP | V17 |
| UC-DEMO-001-EP-15 | EP | F02 |
| UC-DEMO-001-EP-16 | EP | F01 |
| UC-DEMO-001-EP-17 | EP | V20 |
| UC-DEMO-001-BV-01 | BV | V05 |
| UC-DEMO-001-BV-02 | BV | V06 |
| UC-DEMO-001-BV-03 | BV | V07 |
| UC-DEMO-001-BV-04 | BV | V08, V21 |
| UC-DEMO-001-BV-05 | BV | V09 |
| UC-DEMO-001-BV-06 | BV | V18 |
| UC-DEMO-001-BV-07 | BV | V19 |
| UC-DEMO-001-DT-01-R1 | DT | F01, F05 |
| UC-DEMO-001-DT-01-R2 | DT | F02 |
| UC-DEMO-001-DT-01-R3 | DT | F03 |
| UC-DEMO-001-DT-01-R4 | DT | F04 |
| UC-DEMO-001-DT-01-R5 | DT | F06 |
| UC-DEMO-001-EG-01 | EG | F13 |
| UC-DEMO-001-EG-02 | EG | F14 |
| UC-DEMO-001-EG-03 | EG | F15 |
| UC-DEMO-001-EG-04 | EG | F16 |
