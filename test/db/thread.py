#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

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
#     t_obj.append(t1)    #将每个线程实例调价到列表中
#
# for i in t_obj:
#     i.join()            #join每个线程实例
#
# print('main thread')    #所有线程执行完毕后才执行主线程


# import time
# import threading

# def run(n):
#     print('task',n)
#     time.sleep(2)
#     print('task done',n)
#
# start_time = time.time()
# t_obj = []
#
# for i in range(50):
#     t = threading.Thread(target=run,args=('t-%s' %i,))
#     t.start()
#     t_obj.append(t)
#
# for i in t_obj:
#     i.join()
#
# print('----------all threads has finished...')
# print('cost:',time.time() - start_time)

# class MyThread(threading.Thread):
#     def __init__(self,n,sleep_time):
#         super(MyThread,self).__init__()
#         self.n =  n
#         self.sleep = sleep_time
#
#     def run(self):
#         print('runnit task',self.n)
#         time.sleep(self.sleep)
#         print('task done',self.n)
#
# t1 = MyThread("t1",2)
# t2 = MyThread("t1",4)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print('main thread...')


# def run(n):
#     print('task',n)
#     time.sleep(2)
#     print('task done',n,threading.current_thread())
#
# start_time = time.time()
# t_objs = []
#
# for i in range(50):
#     t1 = threading.Thread(target=run,args=('t-%s' %i,))
#     t1.setDaemon(True)
#     t1.start()
#     t_objs.append(t1)
#
# # for t in t_objs:
# #     t.join()
#
# print('done',threading.current_thread(),threading.active_count())
# print('cost',time.time() - start_time)



# import  threading
# def read(file):
#     with open(file,'rb') as f:
#         for i in f:
#             print(i.decode())
#
# for i in range(10):
#     t1 = threading.Thread(target=read,args=(r'C:\Users\djn1\Desktop\nginx.log',))
#     t1.start()

# import time
# import threading
#
# def mu(name):
#     time.sleep(3)
#     print('mu',name)
#
# def run(x):
#     time.sleep(3)
#     print('run',x)
#
# thread = []
#
# for t in ['ma','run']:
#     t1 = threading.Thread(target=t,args=(t,))
#     t1.start()
#     thread.append(t1)
#
# for i in thread:
#     i.join()
# import re
# def replace_after_data(filename):
#     """
#     将指定nginx文件的中的标准格式替换成 正常格式(2016-11-03)并返回
#     """
#     data = []
#     with open(filename,'r') as f:
#         for i in f:
#             x = re.search(r'.*\[(.*:[0-9]+ ).*',i.strip())
#
# replace_after_data(r'C:\Users\djn1\Desktop\nginx.log')

# import time
# import queue
# import threading
#
#
# que = queue.Queue()
# start = time.time()
# def run(q):
#     while not q.empty():
#         print(q.get())
#
# f = open(r'C:\Users\djn1\Desktop\nginx.log','r',encoding="utf-8")
# for i in f:
#     que.put(i)
#
# thread = []
# for i in range(100):
#     t1 = threading.Thread(target=run,args=(que,))
#     t1.start()
#     thread.append(t1)
#
# for i in thread:
#     i.join()
#
# print('over,' ,time.time()-start)

#
# import  time
# start = time.time()
# f = open(r'C:\Users\djn1\Desktop\nginx.log','r',encoding="utf-8")
# for i in f:
#     print(i)
# print('over',time.time()-start)
#
# '''''示例7: 在示例4的基础上，让装饰器带参数，
# 和上一示例相比在外层多了一层包装。
# 装饰函数名实际上应更有意义些'''
#
# def deco(arg):
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, arg))
#             func()
#             print("  after %s called [%s]." % (func.__name__, arg))
#         return __deco
#     return _deco
#
# @deco("mymodule")
# def myfunc():
#     print(" myfunc() called.")
#
# @deco("module2")
# def myfunc2():
#     print(" myfunc2() called.")
#
# myfunc()
# print(''.center(40,'-'))
# myfunc2()



# import subprocess
#
# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# obj.stdin.write("print(1)\n")
# obj.stdin.write("print(2)")
# obj.stdin.close()
#
# cmd_out = obj.stdout.read()
# obj.stdout.close()
# cmd_error = obj.stderr.read()
# obj.stderr.close()
#
# print(cmd_out)
# print(cmd_error)




# import time
# import logging
# # logging.warning("user")
# # logging.critical("test")
#
#
# logging.basicConfig(filename="example.log",level=logging.INFO,
#                     format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#
# for i in range(5):
#     logging.debug("debug")
#     logging.info("info")
#     logging.warning("warning")
#     logging.critical("critical")
#     time.sleep(1)






import logging

#create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)


# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')