#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import sys
import json
import time
import urllib2

class api_data(object):
    def __init__(self,dir):
        self.dir = dir
        self.time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    def __sure_dir(self):
        root_dir = self.dir
        month_dir = os.path.join(root_dir,time.strftime('%m'))
        if not os.path.isdir(month_dir):
            os.makedirs(month_dir)
        return month_dir

    def __get_today_file(self):
        directory = self.__sure_dir()
        today_file = '%s.json' %os.path.join(directory,time.strftime("%Y-%m-%d"))
        if not os.path.isfile(today_file):
            with open(today_file,'wb') as f:
                json.dump({},f)
        return today_file

    def get_old_data(self):
        file_path = self.__get_today_file()
        old_data = json.load(open(file_path))
        return old_data


    def today_num(self):
        try:
            tmp = urllib2.urlopen("http://base.zfwx.com/v3/user/onlineusers.json",timeout=5).read()
            result=json.loads(tmp)
            #print(u'当前在线人数：%s' %result["num"])
            return result["num"]
        except Exception,e:
            print("不能连接到 Base Server",e)


    def __new_data_write_file(self):
        old = self.get_old_data()
        file_path = self.__get_today_file()
        today_num = self.today_num()
        old[today_num] = self.time
        json.dump(old,open(file_path,'wb'))


    def __call__(self):
        self.__new_data_write_file()

if __name__ == "__main__":
    m = api_data(r'W:\dj')
    if len(sys.argv) > 1:
        if sys.argv[1] == "m":
            data = m.get_old_data()
            li = [i for i in data.keys()]
            print(data[max(li)],max(li))
        elif sys.argv[1] == "t":
            result = m.today_num()
            print(u'当前在线人数：%s' %result)
    else:
        m()
