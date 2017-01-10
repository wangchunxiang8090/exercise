#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import os
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

LOG_PATH = r'C:\Users\djn1\Desktop\t'
LAST_FILE = r'C:\Users\djn1\Desktop\last_log_sie_record.txt'
tm = time.strftime('%Y-%m-%d')

class handler_log(object):
    def __init__(self):
        pass

    @staticmethod
    def write(f,v):
        """
        写入指定数据到指定的文件中
        """
        with open(f,'w') as fe:
            fe.write(v)

    def __exists_log_dir(self):
        """
        确定日志目录存在
        """
        if os.path.isdir(LOG_PATH):
            return True

    def last_size(self):
        """
        获取最近一次日志的大小
        """
        if not os.path.isfile(LAST_FILE):
            return None
        else:
            with open(LAST_FILE) as f:
                size = f.readline()
                if int(size) > 1:
                    return size
                else:
                    return None

    def now_size(self):
        """
        获取当前日志大小
        """
        exist = self.__exists_log_dir()
        if exist:
            for i in os.listdir(LOG_PATH):
                if i.startswith(tm) and i.endswith('.log'):
                    size = os.path.getsize(os.path.join(LOG_PATH,i))
                    return size
            else:
                print('not exists today file ')
                exit()


    def size(self):
        """
        返回当前大小和上一次日志大小之间的差值
        """
        last = self.last_size()
        now = self.now_size()
        if now and not last:
            handler_log.write(LAST_FILE,str(now))
            return 0
        else:
            differ = int(now) - int(last)
            handler_log.write(LAST_FILE,str(now))
            return differ

def sendmail(sub,mail_content,to='2459244378@qq.com'):
    """
    发送邮件预警
    """
    try:
        msg = MIMEText(mail_content, 'plain', 'utf-8')
        msg['From'] = formataddr(["python_used@163.com",'python_used@163.com'])
        msg['To'] = formataddr(["python_used@163.com",to])
        msg['Subject'] = sub

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("python_used@163.com", "11qqQQQ")
        server.sendmail('python_used@163.com', to, msg.as_string())
        server.quit()
        return True
    except:
        return False

def approximate_size(size,a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human‐readable form.
    Keyword arguments:
    size ‐‐ file size in bytes
    a_kilobyte_is_1024_bytes ‐‐ if True (default), use multiples of 1024
    if False, use multiples of 1000
    Returns: string
    '''

    SUFFIXES = {1000: ['KB','MB','GB','TB','PB','EB','ZB','YB'],
                1024: ['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB'],
     }

    if size < 0:
        raise ValueError('number must be non-negative')
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    return size
    #raise ValueError('number too large')


if __name__ == "__main__":
    t = handler_log()
    size = t.size()
    print(size)
    if size > 2000:
        result = approximate_size(size,False)
        sub = "日志大小超标"
        content = "指定日志文件超过阈值，请注意查看文件，最近一次产生的数据大小是： %s"  %(result)
        sendmail(sub,content)

