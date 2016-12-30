#!/usr/bin/env python 
# _*_ coding: utf-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def sendmail(sub,mail_content,to='2459244378@qq.com'):

	try:
		msg = MIMEText(mail_content, 'plain', 'utf-8')
		msg['From'] = formataddr(["fafa",'python_used@163.com'])
		msg['To'] = formataddr(["fafa",to])
		msg['Subject'] = sub

		server = smtplib.SMTP("smtp.163.com", 25)
		server.login("python_used@163.com", "11qqQQQ")
		server.sendmail('python_used@163.com', to, msg.as_string())
		server.quit()
		return True
	except:
		return False

