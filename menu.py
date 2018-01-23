#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *

from gui.detail_reg import detail_reg
from gui.facereg import facereg
from gui.log_in import log_in
from gui.showuser import showuser
from gui.menu_gui import Ui_Form  # 导入生成main.py里生成的类\

class menu(QtWidgets.QWidget,Ui_Form):
    close_signal = pyqtSignal() #QtCore
    def __init__(self):
        super(menu,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('人脸识别学习 作者：Kevin.Z')
        self.setWindowIcon(QtGui.QIcon('icons/K.ico'))

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
    showuser_window = showuser()

    menu_window.pushButton_1.clicked.connect(detail_reg_window.handle_click)
    menu_window.pushButton_1.clicked.connect(menu_window.hide)
    menu_window.close_signal.connect(menu_window.close)

    menu_window.pushButton_2.clicked.connect(log_in_window.handle_click)
    menu_window.pushButton_2.clicked.connect(menu_window.hide)
    menu_window.close_signal.connect(menu_window.close)

    detail_reg_window.sumbit_btn.clicked.connect(facereg_window.handle_click)
    detail_reg_window.sumbit_btn.clicked.connect(detail_reg_window.hide)
        #detail_reg_window.sumbit_btn.clicked.connect(detail_reg_window.releaseResource)
    detail_reg_window.close_signal.connect(detail_reg_window.close)

    facereg_window.pushButton.clicked.connect(menu_window.handle_click)
    facereg_window.pushButton.clicked.connect(facereg_window.storePath)
    facereg_window.pushButton.clicked.connect(facereg_window.hide)
    facereg_window.close_signal.connect(facereg_window.close)

    log_in_window.c.openWin.connect(showuser_window.handle_click)
    log_in_window.c.openWin.connect(log_in_window.hide)
    log_in_window.c.openWin.connect(log_in_window.close)
    log_in_window.close_signal.connect(log_in_window.close_signal)

    menu_window.show()
    sys.exit(app.exec_())