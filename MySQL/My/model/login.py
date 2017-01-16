#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

from My.utility.sql_helper import MysqlHelper

class Login(object):
    def __init__(self):
        self.__helper = MysqlHelper()

    def get_one(self,id):
        sql = 'select * from login where id = %s'
        params = (id,)

        return self.__helper.get_one(sql,params)

    def checkvalidata(self,username,password):
        sql = 'select name,passwd from login where name = %s and passwd = %s'
        params = (username,password)
        return self.__helper.get_one(sql,params)

