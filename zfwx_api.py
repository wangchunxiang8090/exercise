#!/usr/bin/python
#coding:utf-8
import time
import urllib
import os

try:
    urllib.urlopen('http://api.zfwx.com/v3/auth/login.json?j_password=11111111&appid=e30d6495ef264cac94fd5b29911ed83f&j_username=ceshi001&choose_domain=0&deviceinfo=Phone_OSX&version=4.19&channelId=4523442464381775171%20HTTP/1.1%22%20200%20480%20%22-%22%20%22-%22%20%22-%22', timeout=3)
except:
    os.system('/etc/init.d/tomcat2 stop;cp -rfp /usr/local/tomcat1/logs{,-`date +%F`};rm -f /usr/local/tomcat1/logs/*;/etc/init.d/tomcat2 start')
    currrnt = time.strftime("%Y-%m-%d %H:%M:%S")
    f = open(r'/root/api_check/restart.txt','w+')
    f.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    f.close()
