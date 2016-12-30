#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import time
import shutil
import datetime

DIRECTORY = os.path.abspath(os.getcwd())
class copy(object):
    """
    这个类只能复制指定目录下的“第一层”的目录或文件
    """
    def __init__(self,*args):
        self.des_dir = os.path.join(DIRECTORY,'%s-%s-w' %(args[0],datetime.date.today()))

    def dir(self,src):
        t = os.path.join(self.des_dir,os.path.basename(src))
        print('copy directory src: %s  det: %s' %(src,t))
        shutil.copytree(src,t)

    def file(self,src):
        t = os.path.join(self.des_dir,os.path.basename(src))
        print('copy file src: %s  det: %s' %(src,t))
        if not  os.path.isdir(os.path.dirname(t)):
            os.makedirs(os.path.dirname(t))
        shutil.copy(src,t)

if __name__ == "__main__":
    inp = input("directory: ").split()
    obj = copy(*inp)
    new_inp = inp[1:]  if len(inp) > 1 else inp
    for i in new_inp:
        temp = os.path.join(DIRECTORY,inp[0],i) if len(inp) > 1 else os.path.join(DIRECTORY,i)
        if os.path.isdir(temp):
            obj.dir(temp)
        elif os.path.isfile(temp):
            obj.file(temp)
        else:
            print('invalid file or directory: ',temp)


