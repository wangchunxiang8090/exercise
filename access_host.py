#!/usr/bin/env python 

import json
import time


IP = {'10.165.98.212':'120.26.41.137(On-zfwx-n1)',
      '10.168.155.79':'121.41.27.55(On-zfwx-n4)',
      '10.117.12.22':'121.43.123.144(On-zfwx-n3)',
      '10.27.214.155':'114.55.106.153(zfwx-n6)',
      '10.171.230.27':'121.40.109.191(MySQL-db-a)'
}

with open(r'/usr/local/nginx/logs/access.log') as f:
    f.seek(0,2)
    while True:
    	try:
   	  d  = f.readline()
    	  if d:
            data = json.loads(d)
            ip = data['client']
  	    if ip == '121.69.129.106':
 	      print(IP[data['upstream_host'].split(':')[0]])
	      break
        except Exception,e:
          continue
