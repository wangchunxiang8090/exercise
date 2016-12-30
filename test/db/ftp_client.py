# __author__ = "Alex Li"
# _*_ coding: utf-8 _*_

# import socket
# import hashlib
#
# client = socket.socket()
#
# client.connect(('localhost', 9999))
#
# while True:
#     cmd = input(">>:").strip()
#     if len(cmd) == 0: continue
#     if cmd.startswith("get"):
#         client.send(cmd.encode())
#         server_response = client.recv(1024)
#         print("servr response:", server_response)
#         client.send(b"ready to recv file")
#         file_total_size = int(server_response.decode())
#         print("file size" ,file_total_size)
#         received_size = 0
#         filename = cmd.split()[1]
#         f = open(filename + ".new", "wb")
#         m = hashlib.md5()
#
#         while received_size < file_total_size:
#             if file_total_size - received_size > 1024:  # 要收不止一次
#                 size = 1024
#             else:  # 最后一次了，剩多少收多少
#                 size = file_total_size - received_size
#                 print("last receive:", size)
#
#             data = client.recv(size)
#             received_size += len(data)
#             m.update(data)
#             f.write(data)
#             # print(file_total_size,received_size)
#
#         else:
#             new_file_md5 = m.hexdigest()
#             print("file recv done", received_size, file_total_size)
#             f.close()
#
#             server_file_md5 = client.recv(1024)
#             print("server file md5:", server_file_md5)
#             print("client file md5:", new_file_md5)
#
# client.close()


#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# import socket
#
# client = socket.socket()
# client.connect(('localhost',9999))
# while True:
#     inp = input(">>> ".strip())
#     client.send(inp.encode())
#     if len(inp) ==0:continue
#     data = client.recv(1024)
#     print(data.decode())

# import os
# import socket
#
# ip_port = ('localhost',9999)
# sk = socket.socket()
# sk.connect(ip_port)
#
# while True:
#     inp = raw_input(">>>").strip()
#     if len(inp) == 1:
#         cmd,path = 'get|%s' %(inp)
#     else:
#         cmd,path = inp.split("|")
#     if not os.path.isfile(path):
#         print('not exists file',path)
#         continue
#     file_name = os.path.basename(path)
#     file_size = os.stat(path).st_size
#     sk.send(cmd+"|"+file_name+'|'+str(file_size))
#     send_size = 0
#     f = open(path,'rb')
#     Flag = True
#     while Flag:
#         if send_size + 1024 > file_size:
#             data = f.read(file_size - send_size)
#             Flag = False
#         else:
#             data = f.read(1024)
#             send_size+=len(data)
#         sk.send(data)
#     f.close()
# sk.close()







import os
import json
import socket

class ftp_client(object):
    def __init__(self):
        self.client = socket.socket()

    def connect(self,ip,port):
        self.client.connect((ip,port))

    def help(self):
        msg = '''
        put filename
        '''
        print(msg.strip())

    def interactive(self):
        while True:
            cmd = input(">>> ").strip()
            if len(cmd) ==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,cmd_str):
                func = getattr(self,cmd_str)
                func(cmd)
            else:
                self.help()

    def put(self,*args):    #put xxx.txt
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action":cmd_split[0],
                    "filename":filename,
                    "filesize":filesize,
                    "overridden":True
                }
                self.client.send(json.dumps(msg_dic).encode())
                print("send",json.dumps(msg_dic).encode())
                server_response = self.client.recv(1024)
                f = open(filename,'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload success...")
                    f.close()
            else:
                print(filename,"is not exist")

    def get(self):
        print("get method is write code")

clint = ftp_client()
clint.connect('localhost',9999)
clint.interactive()


























