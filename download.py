#!/usr/bin/env python 
# _*_ coding: utf-8 _*_

import os
os.chdir(r'D:\share')
print 'current directory: %s' %os.getcwd()
os.system('python -m SimpleHTTPServer 80')