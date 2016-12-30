#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os
import re
import time
import datetime

TODAY = datetime.date.today()
url = {
    'http://www.dianjingyun.com/':0,
    'http://www.zfwx.com/static_cooperateLowyerfirm.jsp':0,
    'http://www.zfwx.com/static_cooperateLawyer.jsp':0,
    'http://www.zfwx.com/static_cooperateLawyerAssociation.jsp':0,
    'http://www.zfwx.com/static_major\?jsp':0,
    'http://www.zfwx.com/DjActivity/getActivityList.do':0,
    'http://www.zfwx.com/schoolLessonDetail.do\?courseId=2202':0,
    'http://www.zfwx.com/wxgr/':0,
    'http://www.zfwx.com/wxqt/':0
}

def nginx_tiem_replace(tm):
    """
    将nginx的标准日期格式的时间转换成 年-月-日的格式并返回
    """
    struct_time = time.strptime(tm,'%d/%b/%Y:%H:%M:%S ')
    return time.strftime("%Y-%m-%d %H:%M:%S ",struct_time)

def replace_after_data(filename):
    """
    将指定nginx文件的中的标准格式替换成 正常格式(2016-11-03)并返回
    """
    data = []
    with open(filename,'r') as f:
        for i in f:
            x = re.search(r'.*\[(.*:[0-9]+ ).*',i.strip())
            try:
                i=i.replace(x.group(1),nginx_tiem_replace(x.group(1))).strip()
                data.append(i)
            except Exception as e:
                pass
    return data

def last_month(filename,number):
    """
    过滤指定天数的数据并返回
    """
    data = []
    x = replace_after_data(filename)
    for day in range(0,number):
        result = TODAY - datetime.timedelta(days=day)
        for i in x:
            if str(result) in i:
                data.append(i)
    return data

def need_data(filename,number):
    data = last_month(filename,number)
    if os.path.isfile(filename):
        with open(filename,'r') as f:
            for line in f:
                for k in url.keys():
                    result = re.search(r'.*(%s).*' %k,line)
                    if result:
                        if result.groups()[0] in line:
                            url[k] += 1
    else:
        exit('not exists file ',filename)

need_data(r'C:\Users\djn1\Desktop\t.log',30)
for i in url:
    print(i,url[i])