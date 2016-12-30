#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

import os
import re
import sys
import shutil
from conf import settings
from core import extract_compress

def make_context(obj,flag=None):
    data = []
    xml_file = obj.xml_file()
    with open(xml_file,'r',encoding="utf-8") as f:
        if flag:
            for i in f:
                if "<dubbo:service" in i or i.startswith("</beans>"):
                    continue
                data.append(i)
        else:
            for i in f:
                if "<dubbo:service" in i or i.startswith("</beans>"):
                    data.append(i)
    return data

def write(f,obj):
    for i in obj:
        f.write(i.encode('utf-8'))

def run():
    #实例化两个对象
    jar_name = input("please input jar package name, default [shop-service-1.0.0-SNAPSHOT.jar]: ")
    if jar_name.isdigit():
        print('invalid input must input jar package name')
        exit()
    else:
        jar_name = jar_name.strip()

    if len(jar_name) == 0:
        jar_name = 'shop-service-1.0.0-SNAPSHOT.jar'
    t = extract_compress.extract_compress('%s' %(os.path.join(settings.DEFAULT_ONLINE_FIND_PATH,settings.MONTH,settings.DATE_TIME)),jar_name)
    x = extract_compress.extract_compress('%s' %(os.path.join(settings.DEFAULT_ONLINE_FIND_PATH)),jar_name)

    #获取指定对象xml文件中合法内容
    new = make_context(t)
    old = make_context(x,flag=True)

    #生成临时文件
    with open(settings.xml_temp_file,'wb+') as f:
        write(f,old)
        write(f,new)

    #写入数据到临时目录中
    new_xml_file = t.xml_file()
    with open(settings.xml_temp_file,'r',encoding='utf-8') as obj_read,open(new_xml_file,'wb+') as obj_write:
        for i in obj_read:
            obj_write.write(i.encode())

    #复制原有jar文件为备份文件
    t()

    #压缩修改后的数据
    t.compress()
    # t.make_jar()

    # if 'win' in sys.platform:
    #     os.system('pause')
