# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail_reg_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(758, 716)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 50, 543, 557))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.major = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.major.setObjectName("major")
        self.gridLayout.addWidget(self.major, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.grade = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.grade.setObjectName("grade")
        self.grade.addItems(['请选择','大一', '大二', '大三', '大四', '研究生', '教职工'])
        self.gridLayout.addWidget(self.grade, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.studentid = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.studentid.setObjectName("studentid")
        self.gridLayout.addWidget(self.studentid, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cardid = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cardid.setObjectName("cardid")
        self.gridLayout.addWidget(self.cardid, 2, 1, 1, 1)
        self.classno = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.classno.setObjectName("classno")
        self.classno.addItems(['选择班级','1','2','3'])
        self.gridLayout.addWidget(self.classno, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.college = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.college.setObjectName("college")
        self.college.addItems(
            ['选择学院', '人文与传播学院', '法政学院', '外国语学院', '教育学院', '音乐学院', '商学院', '美术学院', '数理学院', '生命与环境科学学院', '旅游学院', '体育学院',
             '信息与机电工程学院', '对外汉语学院', '马克思主义学院', '谢晋影视艺术学院'])
        self.gridLayout.addWidget(self.college, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.birthday = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        self.birthday.setMinimumSize(QtCore.QSize(464, 317))
        self.birthday.setObjectName("birthday")
        self.gridLayout.addWidget(self.birthday, 7, 1, 1, 1)
        self.sumbit_btn = QtWidgets.QPushButton(Form)
        self.sumbit_btn.setGeometry(QtCore.QRect(370, 650, 112, 34))
        self.sumbit_btn.setObjectName("sumbit_btn")

        self.retranslateUi(Form)
        self.sumbit_btn.clicked.connect(Form.upload)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "学号："))
        self.label_4.setText(_translate("Form", "专业："))
        self.label_3.setText(_translate("Form", "卡号："))
        self.label_5.setText(_translate("Form", "身份："))
        self.label.setText(_translate("Form", "姓名："))
        self.label_7.setText(_translate("Form", "班级："))
        self.label_6.setText(_translate("Form", "学院："))
        self.label_8.setText(_translate("Form", "生日："))
        self.sumbit_btn.setText(_translate("Form", "提交"))

