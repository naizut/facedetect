#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'
from PyQt5 import QtWidgets, QtGui,QtCore
from gui.showuser_gui import Ui_Form
from PyQt5.QtCore import *
import pymysql
import cv2
class showuser(QtWidgets.QWidget,Ui_Form):
    close_signal = pyqtSignal()
    def __init__(self):
        super(showuser,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('人脸识别学习 作者：Kevin.Z')
        self.setWindowIcon(QtGui.QIcon('icons/K.ico'))

    def handle_click(self,string):
        self.id = string
        if not self.isVisible():
            self.show()
            self.showDetail()
    def endNow(self):
        print("fuck")
    def showDetail(self):
        conn = pymysql.connect('localhost', 'root', 'root', 'dissertation', charset='utf8')
        cur = conn.cursor()
        sql = ("SELECT * FROM `personal_info` WHERE studentID=(%s)")
        cur.execute(sql, self.id)
        list1=[]
        for i in cur.fetchone():
            list1.append(i)
        png = QtGui.QPixmap(list1[8])
        self.img.setPixmap(png)
        self.studentID.setText(self.id)
        self.name.setText(list1[1])
        self.cardID.setText(list1[2])
        self.birthday.setText(list1[3].strftime('%Y-%m-%d'))
        self.college.setText(list1[4])
        self.major.setText(list1[5]+list1[6]+'班')
        self.grade.setText(list1[7])
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Facereg", "验证通过！欢迎使用本系统，" +list1[1])
        conn.commit()
        cur.close()
        conn.close()
