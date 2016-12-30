#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import urllib2
import json
try:
    tmp = urllib2.urlopen("http://base.zfwx.com/v3/user/onlineusers.json",timeout=5).read()
    result=json.loads(tmp)
    print(u'当前在线人数：%s' %result["num"])
except Exception,e:
    print("不能连接到 Base Server",e)


