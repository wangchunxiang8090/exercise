#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import sys
import shutil
import datetime

ROOT_PATH = os.getcwd()
#ROOT_PATH = r'W:\backup_Desktop'
TODAY = datetime.date.today()

class delete_dir:
    def __init__(self,day):
        self.day = day
        print '%s ----> %s'.center(50,'*') %(TODAY - datetime.timedelta(days=100),TODAY - datetime.timedelta(days=self.day))

    def how(self):
        os.chdir(ROOT_PATH)
        for i in range(self.day,100):
            Date = TODAY - datetime.timedelta(days=i)
            directory = os.path.join('%s-%s' %(inp,str(Date)))
            for dir in os.listdir(ROOT_PATH):
                if not dir.startswith(directory):
                    continue
                else:
                    print('delete %s' %os.path.join(ROOT_PATH,dir))
                    try:
                        shutil.rmtree(dir)
                    except Exception:
                        print 'delete {0} error'.format(dir)
                        exit()
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open('%s/record.txt' %'/tmp','a') as f:
                    #with open('%s/record.txt' %ROOT_PATH,'a') as f:
                        f.write('%s 删除目录：%s\n' %(now,os.path.join(ROOT_PATH,dir)))

if __name__ == '__main__':
    d = delete_dir(7) if len(sys.argv) <2 else delete_dir(int(sys.argv[1]))
    while True:
        inp = raw_input('press q exit, delete: ').strip()
        if inp == 'q':
           exit() 
        d.how()

