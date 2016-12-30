#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

#!/usr/local/python27/bin/python
#coding:utf-8

import xlrd

data = xlrd.open_workbook('/root/tmp/qz.xls')
table  = data.sheets()[0]
nrows = table.nrows

for i in range(nrows):
    x = table.row_values(i)[:5]
    print "%s:%s" %(x[2],x[4])