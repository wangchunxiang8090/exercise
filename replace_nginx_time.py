#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re
import time
def nginx_tiem_replace(tm):
    struct_time = time.strptime(tm,'%m/%b/%Y:%H:%M:%S ')
    return time.strftime("%Y-%m-%d %H:%M:%S ",struct_time)

with open(r"C:\Users\djn1\Desktop\tx.txt",'r',encoding="utf-8") as f,open(r"C:\Users\djn1\Desktop\new_log.txt",'a+') as new_obj:
    for i in f:
        x = re.search('.*\[(.*:[0-9]+ ).*',i.strip())
        i=i.replace(x.group(1),nginx_tiem_replace(x.group(1))).strip()
        new_obj.write('%s\n' %i)
