#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'
from PyQt5 import QtWidgets, QtGui,QtCore
from log_in_gui import Ui_Form
import cv2
import time
cap=cv2.VideoCapture(0)

class log_in(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(log_in,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('人脸识别学习 作者：Kevin.Z')
        self.setWindowIcon(QtGui.QIcon('icons/K.ico'))
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showCamera)
        #self.playTimer = Timer("updatePlay()")
        #self.pushButton.clicked.connect(self.playTimer, QtCore.pyqtSignal("updatePlay()"), self.showCamera)

    def showCamera(self):
        #while (1):  # get a frame
        ret, frame = cap.read()  # show a frame

        face_patterns = cv2.CascadeClassifier('D:/project/py/dissertation/haarcascade_frontalface_default.xml')
        faces = face_patterns.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        self.r1 = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.label_img.setPixmap(QtGui.QPixmap.fromImage(self.r1))
        self.timer.start(40)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     cap.release()
        #     cv2.destroyAllWindows()
        #     cv2.destroyAllWindows()


    def handle_click(self):
        if not self.isVisible():
            self.show()

#
# class Timer(QtCore.QThread):
#
#     def __init__(self, signal="updateTime()", parent=None):
#         super(Timer, self).__init__(parent)
#         self.stoped = False
#         self.signal = signal
#         self.mutex = QtCore.QMutex()
#
#     def run(self):
#         with QtCore.QMutexLocker(self.mutex):
#             self.stoped = False
#         while True:
#             if self.stoped:
#                 return
#             self.emit(QtCore.SIGNAL(self.signal))
#             #40毫秒发送一次信号
#             time.sleep(0.04)
#
#     def stop(self):
#         with QtCore.QMutexLocker(self.mutex):
#             self.stoped = True
#
#     def isStoped(self):
#         with QtCore.QMutexLocker(self.mutex):
#             return self.stoped
if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    face_detect_window = log_in()
    face_detect_window.show()
    sys.exit(app.exec_())