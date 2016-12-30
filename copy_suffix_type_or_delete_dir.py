#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import glob
import shutil
import zipfile
import datetime

TODAY = datetime.date.today()

SRC_DIR = r'C:\Users\djn1\Desktop'
DES_DIR = r'W:\backup_Desktop'
DES_DIR_PATH = os.path.join(DES_DIR,str(TODAY))

class copy(object):
    def __init__(self,suffix_type):
        self.__suffix = suffix_type
        self.__suffix_type = [f.split('\\')[-1] for f in glob.glob('%s/*.%s' %(SRC_DIR,suffix_type))]

    def zip_file(self):
        if not os.path.isdir(DES_DIR_PATH):
            os.makedirs(DES_DIR_PATH)
        with zipfile.ZipFile(os.path.join(DES_DIR_PATH,'%s.zip' %(self.__suffix)),'w') as zip_obj:
            for i in self.__suffix_type:
                os.chdir(SRC_DIR)
                i = i.split('\\')[-1]
                zip_obj.write(i)

class delete(object):
    def __init__(self,expire_day):
        self.__day = expire_day

    def how_day(self):
        for i in range(self.__day,31):
            expire = TODAY - datetime.timedelta(days=i)
            expire_directory = os.path.join(DES_DIR,str(expire))
            if not os.path.isdir(expire_directory):
                continue
            else:
                shutil.rmtree(expire_directory)
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open('%s/delete_record.txt' %DES_DIR,'a') as f:
                    f.write('%s 删除目录：%s\n' %(now,expire_directory))

def put_git():
    command = ['git add .','git commit -am {}'.format(str(TODAY)),'git push desktop master']
    os.chdir(DES_DIR)
    for i in command:
        os.system(i)

if __name__ == '__main__':
    if not os.path.isdir(SRC_DIR) or not os.path.isdir(DES_DIR):
        print 'not exists src directory: %s or des directory: %s' %(SRC_DIR,DES_DIR)

    txt = copy('txt')
    txt.zip_file()

    py = copy('py')
    py.zip_file()

    delete_expire_dir = delete(6)
    delete_expire_dir.how_day()

    put_git()