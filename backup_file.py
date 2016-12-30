#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import glob
import shutil
import zipfile
import datetime

SRC = r'C:\Users\djn1\Desktop'
DES = r'W:\dj\dianjing'
TXT = [f.split('\\')[-1] for f in glob.glob('%s/*.txt' %SRC)]
PY = [f.split('\\')[-1] for f in glob.glob('%s/*.py' %SRC)]
DIR = datetime.date.today()
DES_DIR = os.path.join(DES,str(DIR))

class copy:
    def __init__(self,src):
        self.src = src

    def zip_file(self,zn):
        zip_file_name = zn
        if not os.path.isdir(DES_DIR):
            os.makedirs(DES_DIR)
        with zipfile.ZipFile(os.path.join(DES_DIR,'%s.zip' %zip_file_name),'w') as zip_obj:
            for i in self.src:
                os.chdir(SRC)
                i = i.split('\\')[-1]
                zip_obj.write(i)

t = copy(TXT)
t.zip_file('txt')

p = copy(PY)
p.zip_file('py')


