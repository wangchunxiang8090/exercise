#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import json
try:
    import requests
except ImportError,e:
    print e

payload = {'key1':'value1','key2':'value2'}
ret = requests.get("http://httpbin.org/get", params=payload)
ip = json.loads(ret.text)
print ip['origin']