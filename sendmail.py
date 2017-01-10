#!/usr/bin/env python 
# _*_ coding: utf-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def sendmail(sub,mail_content,to='2459244378@qq.com'):
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
if __name__ == "__main__":
  content = "这是一封测试邮件"
  sendmail(content,content)
