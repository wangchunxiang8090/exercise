#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import time
import shutil
import zipfile

DESKTOP = r'C:\Users\djn1\Desktop'
MONTH = time.strftime('%m')
DATE_TIME = time.strftime('%Y-%m-%d')
DIR = '%s\%s\%s' %(DESKTOP,MONTH,DATE_TIME)

class xml(object):
    def __init__(self,path,name):
        self.path = path
        self.name = name

    def find(self):
		"""
		获取JAR文件绝对路径
		"""
        for fpathe,dirs,fs in os.walk(self.path):
          for f in fs:
            result = os.path.join(fpathe,f)
            if result.endswith(self.name):
                return os.path.join(fpathe,f)
        return None

    def unzip(self):
		"""
		解压找到的jar文件到临时目录
		"""
        result = self.find()
        if not result:
            exit()
        with zipfile.ZipFile(result,'r') as z:
            temp = '%s/temp' %self.path
            if not os.path.isdir(temp):
                os.makedirs(temp)
            z.extractall(temp)
            return temp


    def xml_file(self):
		"""
		获取服务的配置文件
		"""
        path = self.unzip()
        temp = os.listdir('%s/META-INF/spring/' %path)
        for i in temp:
            if i.startswith('dubbo') and i.endswith('xml'):
                return os.path.join('%s/META-INF/spring/' %path,i)


def online_config(name):
	"""
	获取线上配置：IP、USERNAME、PASSWORD
	"""
    desktop = xml(r'C:\Users\djn1\Desktop',name)
    result = desktop.xml_file()
    config = []
    with open(result,'r') as f:
        for i in f:
            if i.strip().startswith('<property name="url" value="jdbc:mysql'):
                config.append(i)
            elif i.strip().startswith('<property name="username"'):
                config.append(i)
            elif i.strip().startswith('<property name="password"'):
                config.append(i)
    return config

def today(name):
    t = xml(DIR,name)
    result = t.xml_file()
    return result


def zip_dir(dirname,zipfilename):
	"""
	压缩指定目录
	"""
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)
    zf.close()


if __name__ == '__main__':
    inp = raw_input('jar package name: ').strip()
    online_value = online_config(inp)
    new_file = today(inp)
    flag = True
	#复制原有配置文件内容并替差异内容(线上配置)至配置文件
    with open(new_file,'r') as old,open('%s.bak' %new_file,'w') as new:
        for i in old:
            if '<property name="username"' in i:
                flag = False
                new.write(online_value[-2])
                continue
            elif '<property name="password"' in i:
                flag = False
                new.write(online_value[-1])
                continue
            elif '<property name="url"' in i:
                flag = False
                new.write(online_value[0])
                continue
            if not flag:
                new.write(i)
            else:
                new.write(i)
	#删除临时文件，并改名
    os.remove('%s' %new_file)
    os.rename('%s.bak' %new_file,'%s' %new_file)

	#压缩jar文件
    jar = xml(DIR,inp)
    jar_dir = os.path.dirname(jar.find())
    zip_dir('%s/temp' %DIR,'%s/%s' %(jar_dir,inp))

	#删除临时文件
    shutil.rmtree('%s/temp' %DESKTOP)
    shutil.rmtree('%s/temp' %DIR)