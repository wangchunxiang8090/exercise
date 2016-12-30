#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import shutil
import datetime

#DIRECTORY = os.path.abspath(os.path.split(__file__)[0])
DIRECTORY = os.path.abspath(os.getcwd())

def copy(directory):
    flag = False
    backup_dir_name = os.path.join(DIRECTORY,'%s-%s-w' %(directory[0].split('/')[0],datetime.date.today()))
    copy_dir_abs = [os.path.join(DIRECTORY,elem) for elem in directory]
    abs_down_path = [elem.split('/')[-1] for elem in directory]

    # dir_is_true = [os.path.isdir(item) for item in copy_dir_abs]
    # print all(dir_is_true)
	
	# dir_is_true = map(lambda path: os.path.isdir(path),copy_dir_abs)
    # print dir_is_true	
	
    for k,i in enumerate(copy_dir_abs):
        des_path = os.path.join(backup_dir_name,abs_down_path[k])
        if not os.path.isdir(i):
            return i
        if os.path.exists(des_path):
            des_path += '-%s' %k
        print 'copy directory src: %s  det: %s' %(i,des_path)
        shutil.copytree(i,os.path.join(des_path))
    return 'True'

if __name__ == '__main__':
    directory = raw_input('directory: ').split(' ')
    copy_dir = [elem.split('/')[-1] for elem in directory]
    result = copy(directory)
    if not result == 'True':
        print 'There is no specified directory: %s' %result


