#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# 冒泡排序
data = [11,234,32,1,23,99,89,77,1543,43,213,43,2,23,231,341,43,54,6545,75,4]
for j in range(1,len(data)):
    for i in range(len(data)-j):
        if data[i] > data[i+1]:
            temp = data[i+1]
            data[i+1] = data[i]
            data[i]= temp
print len(data)
print data
