#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

from My.model.login import Login

use = raw_input('username: ')
pas = raw_input('password: ')
login = Login()
result = login.checkvalidata(use,pas)
if not result:
    print '用户密码错误'
else:
    print '登录后台管理页面'