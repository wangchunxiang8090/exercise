#!/usr/bin/env python 
#_*_ coding: utf-8 _*_

import os
import time
import shutil
import zipfile

desktop = r'C:\Users\djn1\Desktop'
month = time.strftime('%m')
now_time = time.strftime('%Y-%m-%d')
default_new_jar_path = os.path.join(desktop,month,now_time)
tmp_file = os.path.join(desktop,'temp.xml')

class base(object):
    def __init__(self,path,name):
        self.path = path
        self.name = name

class jar_package(base):
    def __init__(self,path,name):
        super(jar_package,self).__init__(path,name)

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

    def exists(self):
        jar_file = self.find_jar()
        if not jar_file:
            print('not exists specify jar jar_package',os.path.join(self.path,self.name))
            exit()
        return jar_file

    def extract_jar(self,copy=False):
        """
        提取指定对象文件
        """
        jar_file = self.exists()
        if copy:
            shutil.copy(jar_file,jar_file + '.bak')
            print('copy src: %s dest: %s' %(jar_file,jar_file + '.bak'))

        with zipfile.ZipFile(jar_file,'r') as jar:
            temp = '%s/temp' %self.path
            if not os.path.isdir(temp):
                os.makedirs(temp)
            jar.extractall(temp)
            return temp

    def make_jar(self,path,name):
        """
        制作jar包
        """
        if os.path.isdir(path):
            os.chdir(path)
            print("src jar dir: %s generator: %s " %(path,os.path.join(self.path,name)))
            return os.popen("jar -cf %s ." %(os.path.join(self.path,name),))
        else:
            print("compress jar file error no exists specifi directory: %s" %path)


    def __del__(self):
        directory = os.path.join(self.path,'temp')
        if os.path.isdir(directory):
            print("delete directory: %s" %directory)
            shutil.rmtree(directory)

class operat_file(object):

    def __init__(self,path):
        self.path = path

    def xml_file(self):
        """
        获取配置文件
        """
        tmp = os.listdir('%s/META-INF/spring/' %self.path)
        for i in tmp:
            if i.startswith('dubbo') and i.endswith('xml'):
                return os.path.join('%s/META-INF/spring/' %self.path,i)
        return None

    def generate_context(self,flag=None):
        """
        生成配置文件内容
        """
        data = []
        xml_file = self.xml_file()
        if xml_file:
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

    @staticmethod
    def write(f,obj):
        for i in obj:
            f.write(i.encode('utf-8'))

if __name__ == "__main__":
    inp = input("input jar file name [default shop-service-1.0.0-SNAPSHOT.jar]: ")
    if len(inp) == 0:
        inp = "shop-service-1.0.0-SNAPSHOT.jar"
    else:
        inp = inp

    #new = jar_package(default_new_jar_path,'shop-service-1.0.0-SNAPSHOT.jar')
    #生成两个实例
    new = jar_package(default_new_jar_path,inp)
    online = jar_package(desktop,inp)

    #解压指定路径下的jar包
    new_result = new.extract_jar(True)
    online_result = online.extract_jar()

    #实例化操作文件类
    new_xml_file = operat_file(new_result)
    online_xml_file = operat_file(online_result)

    #生成配置文件内容列表
    new_config = new_xml_file.generate_context()
    online_config = online_xml_file.generate_context(flag=True)

    #生成临时文件
    with open(tmp_file,'wb+') as f:
        operat_file.write(f,online_config)
        operat_file.write(f,new_config)

    #删除就的配置文件
    dest_file = new_xml_file.xml_file() #必须是先确定目标位置,如果删除就为None
    os.remove(new_xml_file.xml_file())

    #移动临时文件为新的配置文件
    os.rename(tmp_file,dest_file)
    print("remove file  SRC: %s  DEST: %s" %(tmp_file,dest_file))

    #生成新的jar文件
    new.make_jar(new_result,inp)
    os.chdir(os.environ['HOMEPATH'])
    time.sleep(1)   #必须sleep

