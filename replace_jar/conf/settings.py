#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

import os
import time
import logging
import datetime

MONTH = time.strftime('%m')
DATE_TIME = time.strftime('%Y-%m-%d')
DEFAULT_ONLINE_FIND_PATH = r'C:\Users\djn1\Desktop'
DEFAULT_REPLACE_JAR_PATH = '%s\%s\%s' %(DEFAULT_ONLINE_FIND_PATH,MONTH,DATE_TIME)
xml_temp_file = os.path.join(DEFAULT_ONLINE_FIND_PATH,'xml_temp.xml')

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = '%s/logs/%s' %(BASE_PATH,datetime.date.today())
logconf = logging.basicConfig(filename=log_file +'replace.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')