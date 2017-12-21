# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(611, 552)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 271, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_img = QtWidgets.QLabel(Form)
        self.label_img.setGeometry(QtCore.QRect(137, 120, 361, 251))
        self.label_img.setObjectName("label_img")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 430, 112, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.showCamera)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请将脸对准摄像头"))
        self.label_img.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "PushButton"))

