#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import webbrowser

open_list = ['http://crm.51dj.cn/crm/main/LoginNew','http://www.zfwx.com/wxqt/']
inp = raw_input('please input number: ').strip()
try:
    result = webbrowser.open(open_list[int(inp)]) if inp.isdigit() else webbrowser.open(open_list[int(0)])
except IndexError:
    webbrowser.open(open_list[int(-1)])