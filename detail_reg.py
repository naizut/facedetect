# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'
from gui.detail_reg_gui import Ui_Form
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
        global userid
        userid = studentID
        cardID = self.cardid.text().strip()
        major = self.major.text().strip()

        grade = self.grade.currentText()
        college = self.college.currentText()
        classNo = self.classno.currentText()

        months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        date = self.birthday.selectedDate().toString()[3:]
        themonth = date[:date.index('月')]
        theday = date[date.index('月') + 2:-5]
        theyear = date[-4:]
        birthday = theyear + '-' + themonth + '-' + theday

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


# if __name__=='__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     detail_reg_window = detail_reg()
#
#     detail_reg_window.show()
#     sys.exit(app.exec_())
