#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'


import os
import json
import socketserver

class my_ftp(socketserver.BaseRequestHandler):

    def put(self,*args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["filesize"]
        f = open(filename + '.new','wb') if os.path.isfile(filename) else open(filename,'wb')

        self.request.send(b'200 ok')
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file [%s] has uploaded ..." % filename)
            f.close()

    def ls(self,*args):
        data = os.path.dirname(os.path.abspath(__file__))
        dir = os.listdir(data)
        self.request.send(' '.join(dir).encode())
        print('send： %s' %' '.join(dir).encode())

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("client socket",self.client_address)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic.get('action')
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
            except ConnectionRefusedError as e:
                print('err',e)
                break

server = socketserver.ThreadingTCPServer(('localhost',6666),my_ftp)
server.serve_forever()