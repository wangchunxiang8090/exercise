#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'


import os
import json
import socket


class ftp_client(object):
    def __init__(self):
        self.client = socket.socket()

    def connect(self,ip,port):
        self.client.connect((ip,port))

    def help(self):
        msg = """
        <put filename>
        <ls>

        """
        print(msg.strip())

    def interactive(self):
        while True:
            cmd = input('>>> ').strip()
            if len(cmd) == 0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,cmd_str):
                func = getattr(self,cmd_str)
                func(cmd)
            else:
                self.help()

    def ls(self,*args):
        cmd_split = args[0].split() #ls
        if len(cmd_split) >= 1:
            msg = {
                'action': 'ls'
            }
            self.client.send(json.dumps(msg).encode())
            data = self.client.recv(1024)
            print(data.decode())

    def put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.path.getsize(filename)
                msg_dic = {
                    'action': cmd_split[0],
                    "filename": filename,
                    "filesize": filesize,
                    "overridden": True,
                }
                self.client.send(json.dumps(msg_dic).encode())
                print("send",json.dumps(msg_dic).encode())
                server_response = self.client.recv(1024)
                f = open(filename,'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print('file upload success...')
                    f.close()
            else:
                print(filename,"is not exist")

    def get(self):
        pass

client = ftp_client()
client.connect('localhost',6666)
client.interactive()