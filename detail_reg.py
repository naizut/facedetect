# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'
from detail_reg_gui import Ui_Form
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
import pymysql

class detail_reg(QtWidgets.QWidget,Ui_Form):
    close_signal = pyqtSignal()  # QtCore
    def __init__(self):
        super(detail_reg,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('人脸识别学习 作者：Kevin.Z')
        self.setWindowIcon(QtGui.QIcon('icons/K.ico'))

    def upload(self):
        name = self.name.text().strip()
        studentID = self.studentid.text().strip()
        cardID = self.cardid.text().strip()
        major = self.major.text().strip()

        grade = self.grade.currentText()
        college = self.college.currentText()
        classNo = self.classno.currentText()

        months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        date = self.birthday.selectedDate()
        themonth = date.toString()[4:7]
        theday = date.toString()[8:9]
        theyear = date.toString()[10:14]
        birthday = theyear + '-' + str(months.index(themonth)) + '-' + theday

        conn = pymysql.connect('localhost', 'root', 'root','dissertation',charset='utf8')
        cur1 = conn.cursor()

        sql = "INSERT INTO `personal_info`(`username`,`studentID`,`cardID`,`major`,`grade`,`college`,`classNo`,`birthday`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cur1.execute(sql, (name,studentID,cardID,major,grade,college,classNo,birthday))

        conn.commit()
        cur1.close()
        conn.close()

    def handle_click(self):
        if not self.isVisible():
            self.show()
#
# if __name__=='__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     detail_reg_window = detail_reg()
#
#     detail_reg_window.show()
#     sys.exit(app.exec_())
