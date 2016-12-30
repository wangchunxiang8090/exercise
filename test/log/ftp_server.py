#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# import socketserver
#
# class my_tcp_handler(socketserver.BaseRequestHandler):
#     def setup(self):
#         pass  # 连接之前做一些操作
#
#     def handle(self):
#         # conn,addr = server.accept()
#         # self.request,self.client_address = server.accept()
#         # 所有客户端交互都在该方法中进行处理 server --> bind --> listen --> accept都已经封装过了,直接处理后续的操作
#         print(self.client_address)
#         while True:
#             self.data = self.request.recv(1024)
#             print(self.data.decode())
#             self.request.send(self.data.upper())
#
#     def finish(self):
#         pass    #连接之后做一些操作
#
#
# server = socketserver.ThreadingTCPServer(('localhost',9999),my_tcp_handler)
# server.serve_forever()

# import os
# import SocketServer
#
# class my_server(SocketServer.BaseRequestHandler):
#
#     def handle(self):
#         base_path = r'W:\iso'
#         conn = self.request
#         print('connected...  for ',self.client_address)
#
#         while True:
#             pre_data = conn.recv(1024)
#             cmd,file_name,file_size = pre_data.split("|")
#             recv_size = 0
#             file_dir = os.path.join(base_path,file_name.decode())
#             f = open(file_dir,'wb')
#             Flag = True
#             while Flag:
#                 if int(file_size.decode()) > recv_size:
#                     data = conn.recv(1024)
#                     recv_size+=len(data)
#                 else:
#                     recv_size = 0
#                     Flag = False
#                     continue
#                 f.write(data)
#             print('upload successed.file',file_name)
#             f.close()
#
# server = SocketServer.ThreadingTCPServer(('localhost',9999),my_server)
# server.serve_forever()


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

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("client socket",self.client_address)
                print("receive data format",self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic['action']
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
            except ConnectionRefusedError as e:
                print('err',e)
                break

server = socketserver.ThreadingTCPServer(('localhost',9999),my_ftp)
server.serve_forever()


