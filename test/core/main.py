#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from conf import settings
def run():
    for i in settings.LOG_TYPES:
        print(i,settings.LOG_TYPES[i])
    print('dict print done'.center(50,'-'))
    print(__file__)