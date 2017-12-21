# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facereg_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 475)
        self.label_img = QtWidgets.QLabel(Form)
        self.label_img.setGeometry(QtCore.QRect(70, 100, 511, 311))
        self.label_img.setObjectName("label_img")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(430, 420, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 420, 311, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        #self.pushButton.clicked.connect(Form.camera)
        self.pushButton.clicked.connect(Form.showCamera)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_img.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "录入"))
        self.label.setText(_translate("Form", "请等待画面出现绿色方框后再点击录入按钮"))

