# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(613, 555)
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(160, 160, 301, 81))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 300, 301, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 460, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(150, 50, 321, 51))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close_window)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "身份录入"))
        self.pushButton_2.setText(_translate("Form", "身份验证"))
        self.pushButton.setText(_translate("Form", "关闭窗口"))
        self.title.setText(_translate("Form", "欢迎使用人脸识别身份验证系统"))

