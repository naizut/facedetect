#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *

from menu_gui import Ui_Form    # 导入生成main.py里生成的类\
from facereg import facereg
from log_in import log_in
from detail_reg import detail_reg

class menu(QtWidgets.QWidget,Ui_Form):
    close_signal = pyqtSignal() #QtCore
    def __init__(self):
        super(menu,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('人脸识别学习 作者：Kevin.Z')
        self.setWindowIcon(QtGui.QIcon('icons/K.ico'))

    #定义槽函数
    def close_window(self):
        self.close()

    def handle_click(self):
        if not self.isVisible():
            self.show()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    menu_window = menu()
    facereg_window = facereg()
    log_in_window = log_in()
    detail_reg_window = detail_reg()

    menu_window.pushButton_1.clicked.connect(facereg_window.handle_click)
    menu_window.pushButton_1.clicked.connect(menu_window.hide)
    menu_window.close_signal.connect(menu_window.close)

    menu_window.pushButton_2.clicked.connect(log_in_window.handle_click)
    menu_window.pushButton_2.clicked.connect(menu_window.hide)
    menu_window.close_signal.connect(menu_window.close)

    facereg_window.pushButton.clicked.connect(detail_reg_window.handle_click)
    facereg_window.pushButton.clicked.connect(facereg_window.hide)
    facereg_window.pushButton.clicked.connect(facereg_window.releaseResource)
    facereg_window.close_signal.connect(facereg_window.close)

    menu_window.show()
    sys.exit(app.exec_())