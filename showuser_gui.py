# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showuser_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(554, 550)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 80, 361, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img.setObjectName("img")
        self.horizontalLayout.addWidget(self.img)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.studentID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.studentID.setObjectName("studentID")
        self.verticalLayout_4.addWidget(self.studentID)
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout_4.addWidget(self.name)
        self.cardID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cardID.setObjectName("cardID")
        self.verticalLayout_4.addWidget(self.cardID)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.major = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.major.setObjectName("major")
        self.verticalLayout_3.addWidget(self.major)
        self.grade = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.grade.setObjectName("grade")
        self.verticalLayout_3.addWidget(self.grade)
        self.college = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.college.setObjectName("college")
        self.verticalLayout_3.addWidget(self.college)
        self.birthday = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.birthday.setObjectName("birthday")
        self.verticalLayout_3.addWidget(self.birthday)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.img.setText(_translate("Form", "TextLabel"))
        self.studentID.setText(_translate("Form", "TextLabel"))
        self.name.setText(_translate("Form", "TextLabel"))
        self.cardID.setText(_translate("Form", "TextLabel"))
        self.major.setText(_translate("Form", "TextLabel"))
        self.grade.setText(_translate("Form", "TextLabel"))
        self.college.setText(_translate("Form", "TextLabel"))
        self.birthday.setText(_translate("Form", "TextLabel"))

