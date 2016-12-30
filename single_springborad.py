#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os

memu = {
    'remote':{
        'gray':{
            'zfwx-n5':'120.55.185.40',
            'zfwx-api':'120.55.185.111'
        },
        'test':{
            'cas':'121.40.51.45',
            'redis':'121.40.34.17',
            'wq':'121.40.51.43',
            'zfwx':'115.29.221.112',

        },
        'online':{
            'zfwx-n2':'120.26.40.197',
            'zfwx-n1':'120.26.41.137',
            'onwq':'121.40.115.120',
            'zfwx-n4':'121.41.27.55',
            'zfwx-n3':'121.43.123.144',
            'oncas':'121.43.227.30',
            'gzdj':'123.57.71.11',
            'dbb':'121.43.112.66',
        },
    },

   #'local':"exit('welcome to localhost!')"
}


flag = True
while flag: # 全局变量，设置跳出整个循环
    for i,v in enumerate(memu.keys()): #遍历第一层字典
	print '\033[31;1m%s %s\033[0m'  %(i,v)
    num_1=raw_input("请输入一级菜单号,按\033[31;1mq\033[0m退出：").strip()
    if num_1 == 'q':
        flag = False
        break
    if num_1.isdigit():
        num_1=int(num_1)
        if num_1<= len(memu):
            key_1 = memu.keys()[num_1]
            while flag:
                for i1,v1 in enumerate(memu[key_1]):
                    print i1,v1
                    #if 'local' in memu[key_1]:
                        #s = compile(memu[key_1],'string','exec')
                        #exec s
                num_2 = raw_input("请输入二级菜单号,按q退出,b返回：").strip()
                if num_2 == 'q':
                    flag = False
                    break
                if num_2 == 'b':
                    break
                if num_2.isdigit():
                    num_2 = int(num_2)
                    if num_2 <= len(memu[key_1]):
                        key_2 = memu[key_1].keys()[num_2]
                        while flag:
                            for i2,v2 in enumerate(memu[key_1][key_2]):
                                print i2 ,v2
                            num_3 = raw_input("请输入三级菜单号,按q退出,b返回：").strip()
                            if num_3 == 'q':
                                flag = False
                                break
                            if num_3 == 'b':
                                break
                            if num_3.isdigit():
                                num_3 = int(num_3)
                                if num_3 <= len(memu[key_1][key_2]):
                                    key_3 = memu[key_1][key_2].keys()[num_3]
                                    while flag:
                                        result = (memu[key_1][key_2][key_3])
  					print('\033[31;1mConnecting to  %s...\033[0m' %result)
					os.system('conn %s' %result)
                                        flag = False
        else:
			print '数字不能超出边界'
			continue
    else:
      print
      print('只能选择跳板机的序列号或按"q"退出')
      continue
