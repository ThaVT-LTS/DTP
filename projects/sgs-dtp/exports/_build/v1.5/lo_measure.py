#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nhờ LibreOffice (chạy ẩn) đo chiều cao dòng vừa chữ và tính giá trị công thức của một file .xlsx. Không lưu file.

    python3 lo_measure.py <file.xlsx> <out.json> --rows "Scopes:13-149" --rows "Cover:11-19" --values Scopes --values Test_Report

Chiều cao: LibreOffice đặt chiều cao tối ưu cho từng dòng (độ rộng cột thu hẹp --shrink để phòng lệch cách ngắt dòng
giữa LibreOffice và Excel), rồi quy về số dòng chữ. Kết quả ghi theo quy ước của file: 13.5 pt mỗi dòng chữ + 8.1 pt.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import time

import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.table.CellContentType import FORMULA


def prop(name, value):
    p = PropertyValue()
    p.Name, p.Value = name, value
    return p


def connect(port, profile):
    proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--norestore", "--nologo", "--nodefault",
                             "-env:UserInstallation=file://" + profile,
                             "--accept=socket,host=127.0.0.1,port=%d;urp;" % port],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
    for _ in range(120):
        try:
            ctx = resolver.resolve("uno:socket,host=127.0.0.1,port=%d;urp;StarOffice.ComponentContext" % port)
            return proc, ctx
        except Exception:
            time.sleep(0.5)
    proc.kill()
    raise SystemExit("Không nối được LibreOffice")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("xlsx")
    ap.add_argument("out")
    ap.add_argument("--rows", action="append", default=[], help="<sheet>:<dòng đầu>-<dòng cuối>[:raw]")
    ap.add_argument("--values", action="append", default=[], help="tên sheet cần lấy giá trị công thức")
    ap.add_argument("--shrink", type=float, default=0.97)
    ap.add_argument("--line", type=float, default=13.5)
    ap.add_argument("--pad", type=float, default=8.1)
    ap.add_argument("--min-lines", type=int, default=2)
    ap.add_argument("--raw", action="store_true", help="ghi chiều cao thô (pt) thay vì quy về số dòng chữ")
    a = ap.parse_args()

    profile = tempfile.mkdtemp(prefix="lo_profile_")
    proc, ctx = connect(2002 + os.getpid() % 500, profile)
    try:
        desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        url = uno.systemPathToFileUrl(os.path.abspath(a.xlsx))
        doc = desktop.loadComponentFromURL(url, "_blank", 0, (prop("Hidden", True), prop("ReadOnly", True)))
        doc.calculateAll()
        sheets = doc.Sheets
        out = {"heights": {}, "raw": {}, "values": {}, "errors": {}}

        for name in a.values:
            sh = sheets.getByName(name)
            cur = sh.createCursor()
            cur.gotoEndOfUsedArea(False)
            last_r, last_c = cur.RangeAddress.EndRow, cur.RangeAddress.EndColumn
            vals, errs = {}, {}
            for r in range(0, last_r + 1):
                for c in range(0, last_c + 1):
                    cell = sh.getCellByPosition(c, r)
                    if cell.Type == FORMULA:
                        ref = cell.AbsoluteName.split(".")[-1].replace("$", "")
                        if cell.getError():
                            errs[ref] = cell.getString()
                        else:
                            vals[ref] = cell.getValue()
            out["values"][name], out["errors"][name] = vals, errs

        for spec in a.rows:
            parts = spec.split(":")
            raw_mode = a.raw or (len(parts) == 3 and parts[2] == "raw")
            name, rng = parts[0], parts[1]
            lo, hi = [int(x) for x in rng.split("-")]
            sh = sheets.getByName(name)
            cols = sh.Columns
            cur = sh.createCursor()
            cur.gotoEndOfUsedArea(False)
            for c in range(0, cur.RangeAddress.EndColumn + 1):
                col = cols.getByIndex(c)
                col.Width = int(col.Width * a.shrink)
            rows = sh.Rows
            hs, raw = {}, {}
            for r in range(lo, hi + 1):
                row = rows.getByIndex(r - 1)
                row.OptimalHeight = True
                pt = row.Height / 100.0 / 25.4 * 72.0
                raw[r] = round(pt, 2)
            out["raw"][name] = raw
            # LibreOffice đặt chiều cao tối ưu = 13.5 pt mỗi dòng chữ + 8.1 pt (đúng quy ước các sheet TC của file);
            # quy về số dòng chữ để khỏi lệch vài phần trăm pt do đơn vị 1/100 mm.
            for r, pt in raw.items():
                if raw_mode:
                    hs[r] = pt
                else:
                    lines = max(a.min_lines, int(round((pt - a.pad) / a.line)))
                    hs[r] = round(a.line * lines + a.pad, 2)
            out["heights"][name] = hs
        doc.close(True)
    finally:
        try:
            desktop.terminate()
        except Exception:
            pass
        try:
            proc.wait(timeout=20)
        except Exception:
            proc.kill()
    json.dump(out, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("đã đo:", {k: len(v) for k, v in out["heights"].items()}, "· giá trị:", {k: len(v) for k, v in out["values"].items()},
          "· lỗi công thức:", {k: v for k, v in out["errors"].items() if v})


if __name__ == "__main__":
    sys.exit(main())
