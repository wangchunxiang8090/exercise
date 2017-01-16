#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

import os
import sys
import shutil
import hashlib

class copy(object):
    def __init__(self):
        self.result = {}

    def md5sum(self,f):
        result = {}
        t = hashlib.md5()
        with open(f,'rb') as fl:
            for j in fl:
                t.update(j)
            else:
                result[f] = t.hexdigest()
            return result

    def src(self,*args):
        for i in args:
            #path = i if os.path.abspath(i) else os.path.join(os.getcwd(),i)
            path = r'%s' %i if os.path.abspath(i) else os.path.join(os.getcwd(),i)
            print('path--',path)
            #path = os.path.join(os.getcwd(),i)
            if os.path.exists(path):
                if os.path.isfile(path):
                    res = self.md5sum(i)
                    self.result.update(res)
                else:
                    continue
            else:
                print('not exist ',path)
        return self.result

    def dest(self,*args):
        src = self.result
        for k,v in src.items():
            if os.path.isfile(os.path.join(args[0],k)):
                s = self.result.get(k)
                d = self.md5sum(os.path.join(args[0],k))
                dmd5 = d.get(os.path.join(args[0],k))
                if s == dmd5:
                    print(s,dmd5)
                    print('skipping %s'%k)
                    continue

            s,d = os.path.join(os.getcwd(),k),args[0]
            print('copy src: %s  dest: %s' %(s,d))
            shutil.copy(s,d)

if __name__ == "__main__":
    if not len(sys.argv) >= 3:
        print('%s <src[,...]> <des>' %sys.argv[0])
        exit()
    SRC = sys.argv[1:-1]
    DESC = sys.argv[-1]

    obj = copy()
    res = obj.src(*SRC)
    obj.dest(DESC)


