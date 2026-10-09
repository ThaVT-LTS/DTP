"""Trải phẳng một sheet TC: mỗi dòng dữ liệu một bản ghi, ô gộp được điền xuống."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from xl import *

COLS = {"No": 1, "I": 2, "II": 3, "III": 4, "IV": 5, "Pri": 6, "ID": 7, "Name": 8, "Pre": 9, "Step": 10, "Exp": 11,
        "Dev": 12, "R1": 13, "P1": 14, "D1": 15, "B1": 16, "Rm1": 17, "R2": 18, "P2": 19, "D2": 20, "B2": 21, "Rm2": 22, "OQ": 23, "UC": 24}

def flat(book, sheet, first=13):
    cells = book.cells(sheet); merges = book.merges(sheet)
    anchor = {}
    for c1, r1, c2, r2 in merges:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                anchor[(c, r)] = (c1, r1)
    last = max((r for (c, r), v in cells.items() if v[0] not in (None, "") and c <= 24), default=first)
    rows = []
    for r in range(first, last + 1):
        rec = {"row": r}
        for k, c in COLS.items():
            a = anchor.get((c, r), (c, r))
            v = cells.get(a, (None,))[0]
            rec[k] = v if v is not None else ""
        rec["extra"] = {col_name(c): v[0] for (c, rr), v in cells.items() if rr == r and c > 24 and v[0] not in (None, "")}
        rec["merged"] = {k: ("%s%d" % (col_name(anchor[(c, r)][0]), anchor[(c, r)][1])) for k, c in COLS.items() if (c, r) in anchor}
        if any(rec[k] for k in COLS):
            rows.append(rec)
    return rows

if __name__ == "__main__":
    path, sheet, out = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = flat(Book(path), sheet)
    json.dump(rows, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(rows), "dòng →", out)
