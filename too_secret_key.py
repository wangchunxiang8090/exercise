#!/usr/bin/env python 
# _*_ coding: utf-8 _*_

import paramiko
import threading
import sys

#command = ['touch /tmp/abc.txt','mkdir /tmp/abc','ls /tmp']
command = sys.argv[1:]

IP = ['192.168.1.122','192.168.1.116']
event = threading.RLock()

def conn(ip,port,user):
  private_key_path = '/root/.ssh/id_rsa'
  try:
    key = paramiko.RSAKey.from_private_key_file(private_key_path)
  except Exception,e:
    print('not found user design private...')
    exit()

  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(ip,port,username=user,pkey=key)

  for i in command:
    stdin,stdout,stderr = ssh.exec_command(i)
    event.acquire()
    print ip
    print stdout.read()
    event.release()
  ssh.close()

for a in range(len(IP)):
  t = threading.Thread(target=conn,args=(IP[a],22,'root'))
  t.start()  	

