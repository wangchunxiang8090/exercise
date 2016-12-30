#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#创建类
# class Foo:
#
#     #创建类中的函数，类中的函数在类中叫做方法
#     def Bar(self):
#         pass    #一些代码
#
# # 根据类Foo创建对象obj
# obj = Foo() #在实例化的过程中会自动执行该类的__init__()构造函数


class Foo:
    def Bar(self):
        print('Bar')

    def Hello(self,name):
        print('i am  %s ' %name)

obj = Foo()
obj.Bar()
obj.Hello("wupeiqi")