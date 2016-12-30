#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

import os
import sys
import zipfile
import shutil
import logging

from conf import settings

class base(object):
    def __init__(self,path,name):
        self.path = path
        self.name = name

class extract_compress(base):
    def __init__(self,path,name):
        super(extract_compress,self).__init__(path,name)

    def find_jar(self):
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
        解压找打的jar文件临时目录
        """
        jar_f = self.find_jar()
        if jar_f:
            pass
            #print('jar file path：',jar_f)
            logging.info('jar file path：' +  jar_f)
        else:
            print('not specify jar file',os.path.join(self.path,self.name))
            logging.error('not specify jar file' + os.path.join(self.path,self.name))
            exit()

        with zipfile.ZipFile(jar_f,'r') as jar:
            temp = '%s/temp' %self.path
            if not os.path.isdir(temp):
                os.makedirs(temp)
                jar.extractall(temp)
            return jar_f,temp

    def compress(self):
        """
        压缩指定目录
        """
        path = self.unzip()
        print('compress path',path)
        print('compress file: ',path[0])
        logging.info('compress file: ' + path[0])
        if len(path) >= 2:
            os.chdir(path[-1])
            os.system('jar -cf %s .' %path[-1])
            # filelist = []
            # if os.path.isfile(path[-1]):
            #     filelist.append(path[-1])
            # else:
            #     for root, dirs, files in os.walk(path[-1]):
            #         for name in files:
            #             filelist.append(os.path.join(root, name))
            #
            # zf = zipfile.ZipFile(path[0], "w", zipfile.zlib.DEFLATED)
            # for tar in filelist:
            #     arcname = tar[len(path[-1]):]
            #     zf.write(tar,arcname)
            # zf.close()
        else:
            print('error')
            logging.error('error')
            exit()

    # def make_jar(self):
    #     jar,temp = self.unzip()
    #     os.chdir(temp)
    #     os.system('jar -cf %s .' %jar)

    def xml_file(self):
        jar_file,temp = self.unzip()
        tmp = os.listdir('%s/META-INF/spring/' %temp)
        for i in tmp:
            if i.startswith('dubbo') and i.endswith('xml'):
                #print(os.path.join('%s/META-INF/spring/' %temp,i))
                logging.info(os.path.join('%s/META-INF/spring/' %temp,i))
                return os.path.join('%s/META-INF/spring/' %temp,i)

    def __call__(self, *args, **kwargs):
        result = self.find_jar()
        dest_file = result + '.bak'
        if not  os.path.isfile(dest_file):
            print("backup source file: source %s  destination: %s" %(result,dest_file))
            logging.info("backup source file: source %s  destination: %s" %(result,dest_file))
            shutil.copy(result,dest_file)

    def __del__(self):
        directory = os.path.join(self.path,'temp')
        if os.path.isdir(directory):
            try:
                print('delete temp directory',directory)
                logging.info('delete temp directory' + directory)
                shutil.rmtree(directory)
            except Exception as e:
                pass
        if os.path.isfile(settings.xml_temp_file):
            print('delete temp file', settings.xml_temp_file)
            logging.info('delete temp file' + settings.xml_temp_file)
            os.remove(settings.xml_temp_file)
