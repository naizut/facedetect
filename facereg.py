#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'
from PyQt5 import QtWidgets, QtGui,QtCore
from facereg_gui import Ui_Form
from PyQt5.QtCore import *
import cv2
cap = cv2.VideoCapture(0)

class facereg(QtWidgets.QWidget,Ui_Form):
    close_signal = pyqtSignal() #QtCore
    def __init__(self):
        super(facereg,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('人脸识别学习 作者：Kevin.Z')
        self.setWindowIcon(QtGui.QIcon('icons/K.ico'))
        self.num = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showCamera)
        self.pushButton.setEnabled(False)

    def showCamera(self):
        if self.num >= 10:
            self.pushButton.setEnabled(True)
        ret, frame = cap.read()  # show a frame
        path = 'D:/test/'
        face_patterns = cv2.CascadeClassifier('D:/project/py/dissertation/haarcascade_frontalface_default.xml')
        faces = face_patterns.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        if len(faces) > 0 and self.num<10:
            for (x, y, w, h) in faces:
                square = frame[y:y + h, x:x + w]  # 反之则定位错位
                cv2.imwrite(path + str(self.num) + 'face.jpg', square)
            self.num += 1

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        self.r1 = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.label_img.setPixmap(QtGui.QPixmap.fromImage(self.r1))
        self.timer.start(40)

    def handle_click(self):
        if not self.isVisible():
            self.show()
            self.showCamera()

    def releaseResource(self):
        cap.release()
        cv2.waitKey(0)
        self.timer.stop()#不加会报错#
        cv2.destroyAllWindows()
