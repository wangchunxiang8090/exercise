#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

# from threading import Thread
# import time

# def foo(arg,v):
#     print(arg)
#
# print('before')
# t1 = Thread(target=foo,args=(1,2,))
# t1.start()
# print('after')

# def foo(arg,v):
#     for item in range(10):
#         print(item)
#         time.sleep(1)
# print('before')
# t1 = Thread(target=foo,args=(1,2,))
# t1.setDaemon(1)
# t1.start()
# print('after')
#


# class MyThreade(Thread):
#     def run(self):
#         time.sleep(3)
#         print('我是线程')
#
# def Bar():
#     print('bar')
#
# t1 = MyThreade(target=Bar)
# t1.start()
# print('over')

# import time
# import threading
#
# def run(n):
#     time.sleep(1)   #线程被挂起
#     print(n)
#
# t_obj = []
# for i in range(50):
#     t1 = threading.Thread(target=run,args=(i,))
#     t1.start()
#     t_obj.append(t1)    #将每个线程实例添加到列表中
#
# for i in t_obj:
#     i.join()            #join每个线程实例
#
# print('main thread')    #所有线程执行完毕后才执行主线程



# class MyThread(Thread):
#     def run(self):
#         print('mythread')
#         Thread.run(self)
#
# def Bar():
#     print('bar')
#
# t1 = MyThread(target=Bar)
# t1.start()
# print('over')

# from queue import Queue
# que = Queue(maxsize=10)
# for i in range(5):
#     que.put(i)
#
#
# print(que.qsize())
# for i in range(que.qsize()):
#     print(que.get())
#
# if que.empty():
#     print('队列是空')
# else:
#     print(que.get())

# from queue import Queue
#
# class Procuder(Thread):
#
#     def __init__(self,name,queue):
#         self.__Name = name
#         self.__Queue = queue
#         super(Procuder,self).__init__()
#
#     def run(self):
#         while 1:
#             if self.__Queue.full():
#                 time.sleep(1)
#             else:
#                 self.__Queue.put('baozi')
#                 time.sleep(1)
#                 print('%s 生产了一个包子' %self.__Name)
#
#
# class consumer(Thread):
#
#     def __init__(self,name,queue):
#         self.__Name = name
#         self.__Queue = queue
#         super(consumer,self).__init__()
#
#
#     def run(self):
#         while 1:
#             if self.__Queue.empty():
#                 time.sleep(3)
#                 print('包子满了'.center(50,'-'))
#             else:
#                 self.__Queue.get()
#                 time.sleep(2)
#                 print('%s 消费了一个包子' %self.__Name)
#
# que = Queue(maxsize=10)
#
# laogou1 = Procuder('老狗1',que)
# laogou2 = Procuder('老狗2',que)
# laogou3 = Procuder('老狗3',que)
# laogou1.start()
# laogou2.start()
# laogou3.start()
#
# for item in range(20):
#     name = 'abc%d' %(item)
#     temp = consumer(name,que)
#     temp.start()
#


# import threading,time,queue
# import random
#
# def Proudcer(name,que):
#     while True:
#         if que.qsize() < 3:
#             que.put('baozi')
#             print('%s: make a baozi...' %name)
#         else:
#             print('还有%d个包子' %que.qsize())
#
#
# def Consumer(name,que):
#     while 1:
#         try:
#             que.get_nowait()
#             print("%s: got a baozi..." %name)
#         except Exception as e:
#             print('没有包子了')
#         time.sleep(random.randrange(1))
#
# q = queue.Queue()
# p1 = threading.Thread(target=Proudcer,args=('chef1',q))
# p2 = threading.Thread(target=Proudcer,args=('chef2222',q))
# p1.start()
# p2.start()
#
# c1 = threading.Thread(target=Consumer,args=('abc1',q))
# c2 = threading.Thread(target=Consumer,args=('abc2222',q))
# c1.start()
# c2.start()
#



# num = 0
# def run(n):
#     global num
#     num+=1
#     print(num)
# run('d')


# from threading import Thread,Lock,RLock
# import time
#
# num = 0
#
# def run(n):
#     time.sleep(1)
#     global num
#     lock.acquire()
#     num += 1
#     lock.release()
#     time.sleep(0.01)
#     print('%s \n' %num)
#
# lock = RLock()
#
# for i in range(10):
#     t = Thread(target=run,args=(i,))
#     t.start()
#


# import threading
# import time
#
# num = 0
#
# def run(n):
#     time.sleep(1)
#     global  num
#     samp.acquire()
#     time.sleep(0.01)
#     num += 1
#     print('%s' %num)
#     samp.release()
#
# samp = threading.BoundedSemaphore(4)
#
# for i in range(100):
#     t = threading.Thread(target=run,args=(i,))
#     t.start()
#
#



# import threading
# import time
#
# def producer():
#     print('chef: 等人来买包子...')
#     event.wait()
#     event.clear()
#     print('chef: sb is coming for baozi...')
#
#     print('chef: makeing a baozi for sb...')
#     time.sleep(3)
#     event.set()
#
#     print('chef: 你的包子做好了')
#
# def consumer():
#     print('chenchao: 去买包子===')
#     event.set()
#     time.sleep(2)
#     print('chenchao: waiting for baozi to be ready')
#     print(event.wait())
#
#     print('chenchao: 包子真好吃')
#
# event = threading.Event()
#
# p = threading.Thread(target=producer)
# c = threading.Thread(target=consumer)
#
# p.start()
# c.start()



# import threading
# import time
#
#
#
# def producer():
#     print ('chef: 等人来买包子...')
#     event.wait()    #阻塞，只要flag变成true，阻塞就没了，直接往下走
#     event.clear()   #清空set等于True，如果不改一直都为true
#     print('chef: sb is coming for baozi...')
#
#     print ('chef:making a baozi for sb...')
#     time.sleep(3)
#     event.set()
#
#     print ('chef: 你的包子做好了')
#
# def consumer():
#     print ('chengchao: 去买包子===')
#     event.set() #flag 默认是false，set是把flag变成true
#
#     time.sleep(2)
#     print('chengchao:waiting for baozi to be ready')
#     while True:
#         if event.isSet():
#             print ('thanks...')
#             break
#         else:
#             print ('还你吗没好啊')
#             time.sleep(1)
#
#     print ('chengchao: 包子真好吃')
# event = threading.Event()
#
# p = threading.Thread(target=producer)
# c = threading.Thread(target=consumer)
# p.start()
# c.start()



import time
import threading

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if count > 5 and count < 10:
            event.clear()
            print("\033[41;1mred light is on....\033[0m")
        elif count > 10:
            event.set()
            count = 0
        else:
            print("\033[42;1mgreen light is on....\033[0m")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print("[%s] running..."% name )
            time.sleep(1)
        else:
            print("[%s] sees red light , waiting...." %name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)

light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("tes;a",))
car1.start()
