#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os
import  glob

ip_port = ('192.168.1.208',9999)
sk = socket.socket()
sk.connect(ip_port)
os.chdir(r'C:\Users\djn1\Desktop')

while True:
    inp = raw_input('path: ')
    if inp.startswith('cd'):
        try:
            os.chdir(inp.split(' ')[-1])
        except Exception,e:
            print e
            continue
    elif inp.startswith('ls'):
        if len(inp) > 2:
            print glob.glob(inp.split()[-1])
        else:
            print os.listdir(os.getcwd())
    elif inp.startswith('put'):
        f = inp.split(' ')[-1]
        file_name = os.path.basename(f)
        file_size = os.stat(f).st_size
        sk.send(file_name+'|'+str(file_size))
        send_size = 0
        fl = file(file_name,'rb')
        Flag = True
        while Flag:
            if send_size + 1024 >file_size:
                data = fl.read(file_size-send_size)
                Flag = False
            else:
                data = fl.read(1024)
                send_size+=1024
            sk.send(data)
        fl.close()
        print 'upload file %s success!' %f
    else:
        if len(inp) == 0:
            continue
        print 'exit...'
        exit()
sk.close()


