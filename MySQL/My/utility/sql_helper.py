#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

import MySQLdb

from My.conf import conn


class MysqlHelper(object):
    def __init__(self):
        self.conn = conn

    def get_one(self,sql,params):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()

        recount = cur.execute(sql,params)
        data = cur.fetchone()

        cur.close()
        conn.close()

        return data

