#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# class Animal:
#     def eat(self):
#         print('%s 吃' %self.name)
#     def drink(self):
#         print('%s 喝' %self.name)
#     def shit(self):
#         print('%s 拉' %self.name)
#     def pee(self):
#         print('%s 撒 ' %self.name)
#
# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name
#         self.breed = '猫'
#
#     def cry(self):
#         print('喵喵叫')
#
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#         self.breed = '够'
#     def cry(self):
#         print('汪汪叫')
#
# c1 = Cat('小白家的小黑猫')
# c1.eat()
#
# c2 = Cat('小黑的小白猫')
# c2.drink()
#
# d1 = Dog('胖子家的小搜狗')
# d1.eat()

# class D:
#     def bar(self):
#         print('D.bar')
#
# class C(D):
#     def bar(self):
#         print('C.bar')
#
# class B(D):
#     def bar(self):
#         print('B.bar')
#
# class A(B,C):
#     # def bar(self):
#     #     print('A.bar')
#     pass
#
# a = A()
# a.bar()




# class D(object):
#
#     def bar(self):
#         print( 'D.bar')
#
#
# class C(D):
#
#     def bar(self):
#         print('C.bar')
#
#
# class B(D):
#
#     def bar(self):
#         print( 'B.bar')
#
#
# class A(B, C):
#
#     def bar(self):
#         print( 'A.bar')
#
# a = A()
# # 执行bar方法时
# # 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# # 所以，查找顺序：A --> B --> C --> D
# # 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
# a.bar()



