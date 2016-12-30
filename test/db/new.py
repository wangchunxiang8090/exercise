#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

import time
import queue
import threading


full_data = queue.Queue()

url = {
    'http://www.dianjingyun.com/':0,
    'http://www.zfwx.com/static_cooperateLowyerfirm.jsp':0,
    'http://www.zfwx.com/static_cooperateLawyer.jsp':0,
    'http://www.zfwx.com/static_cooperateLawyerAssociation.jsp':0,
    'http://www.zfwx.com/static_major\?jsp':0,
    'http://www.zfwx.com/DjActivity/getActivityList.do':0,
    'http://www.zfwx.com/schoolLessonDetail.do\?courseId=2202':0,
    'http://www.zfwx.com/wxgr/':0,
    'http://www.zfwx.com/wxqt/':0
}

start = time.time()
def run(filename):
    f = open(filename,'r',encoding="utf-8")
    for i in f:
        full_data.put(i)

def producer():
    while full_data.qsize() >1:
        for i in url.keys():
            if i in full_data.get():
                lock.acquire()
                url[i] += 1
                lock.release()

if __name__ == "__main__":
    lock = threading.Lock()
    run(r'C:\Users\djn1\Desktop\t.log')
    producer()
    for i in range(10):
        t1 = threading.Thread(target=producer)
        t1.start()
    for i in url:
        print(i,url[i])
    print('over',time.time()-start)