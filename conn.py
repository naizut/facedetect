#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'
import pymysql
conn = pymysql.connect('localhost', 'root', 'root', 'dissertation')
cur = conn.cursor()
sql = "INSERT INTO `personal_info`(`studentID`, `username`, `cardID`, `birthday`, `college`, `major`, `classNo`, `grade`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
cur.execute(sql,('123123','1','094487','1995-12-12','f','2','2','2'))
conn.commit()
cur.close()
conn.close()