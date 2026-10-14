#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phông và bảng màu duy nhất của file test case — nguồn chung cho mọi script của skill tc-authoring.

Khớp `references/format.md` §4. Đổi phông hay màu thì sửa ở đây và ở format.md,
không sửa trong từng script. Mã màu viết hoa, 6 ký tự, không có dấu #.
"""
FONT = "Times New Roman"
SIZE = 10

HEAD_FILL = "00B0F0"   # mọi ô có nền: hàng tiêu đề, nhãn khối thông tin, khối tổng kết, dòng tổng
HEAD_FONT = "FFFFFF"   # chữ trên nền tiêu đề
TEXT = "363A45"        # chữ ở mọi ô không có nền
OPEN_FILL = "FBE9E7"   # dòng còn câu hỏi mở: ô Open question, và ô Expected result khi còn trống
OPEN_FONT = "B8362B"   # chữ trong ô Open question

PALETTE_FILL = {HEAD_FILL, OPEN_FILL}
PALETTE_FONT = {HEAD_FONT, TEXT, OPEN_FONT}
