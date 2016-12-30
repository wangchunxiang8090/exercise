#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# class foo:
#
#     def __init__(self,name,age):    #构造函数，根据类创建对象时自动执行
#         self.name = name
#         self.age = age
#
# # 根据类foo创建对象
# # 自动执行foo类的__init__方法
# obj1 = foo('wupeiqi',18) #将wupeiqi和18分别封装到obj1的name和age属性中
# print(obj1.name)    #直接调用obj1对象的name属性
# print(obj1.age)     #直接调用obj1对象的age属性
#
#
# # 根据类foo创建对象
# # 自动执行foo类的__init__方法
# obj2 = foo('alexi',78) #将wupeiqi和78分别封装到obj1的name和age属性中
# print(obj2.name)#直接调用obj2对象的name属性
# print(obj2.age) #直接调用obj2对象的age属性


# class foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def detail(self):
#         print(self.name)
#         print(self.age)
#
# obj1 = foo('wupeiqi',18)
# obj1.detail()
#
# obj2 = foo('alex',78)
# obj2.detail()

# class foo:
#
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def kanchai(self):
#         print('%s,%s岁,%s,上山去砍柴' %(self.name,self.age,self.gender))
#     def qudongbei(self):
#         print('%s,%s岁,%s,开车去东北' %(self.name,self.age,self.gender))
#     def dabaojian(self):
#         print('%s,%s岁,%s,最爱大保健' %(self.name,self.age,self.gender))
#
# xiaoming = foo('小明',10,'男')
# xiaoming.kanchai()
# xiaoming.qudongbei()
# xiaoming.dabaojian()
#
#
# laoli = foo('老李',90,'男')
# laoli.kanchai()
# laoli.qudongbei()
# laoli.dabaojian()


class Person(object):
    def __init__(self,ne,gen,age,fig):
        self.name = ne
        self.gender = gen
        self.age = age
        self.fight = fig
    def grassland(self):
        self.fight -= 200
    def practice(self):
        self.fight += 200
    def incest(self):
        self.fight -= 500
    def detail(self):
        temp = "姓名:%s; 性别: %s ; 年龄: %s ；战斗力: %s" %(self.name,self.gender,self.age,self.fight)
        print(temp)


cang = Person('苍井井', '女', 18, 1000)    # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)      # 创建波多多角色

cang.incest() #苍井空参加一次多人游戏
dong.practice()#东尼木木自我修炼了一次
bo.grassland() #波多多参加一次草丛战斗


#输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()


cang.incest() #苍井空又参加一次多人游戏
dong.incest() #东尼木木也参加了一个多人游戏
bo.practice() #波多多自我修炼了一次

#输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()