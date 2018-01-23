#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'k3v1n.Z'
import sys,os,dlib,glob,numpy,re,pymysql
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtCore import *
from gui.log_in_gui import Ui_Form
import cv2
import time
from gui.showuser import showuser
cap=cv2.VideoCapture(0)
predictor_path = 'D:/girl/1.dat'
face_rec_model_path = 'D:/girl/2.dat'
faces_folder_path = 'D:/test/imgbase/'

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)
descriptors = {}
book = {}

class Detected(QObject):
    openWin = pyqtSignal(str)

class log_in(QtWidgets.QWidget,Ui_Form):
    close_signal = pyqtSignal()

    def __init__(self):
        super(log_in,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('人脸识别学习 作者：Kevin.Z')
        self.setWindowIcon(QtGui.QIcon('icons/K.ico'))

        self.c = Detected()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showCamera)
        #self.playTimer = Timer("updatePlay()")
        #self.pushButton.clicked.connect(self.playTimer, QtCore.pyqtSignal("updatePlay()"), self.showCamera)

    def matchFace(self, face):
        dets = detector(face, 1)
        for k, d in enumerate(dets):
            shape = sp(self.img, d)
            face_descriptor = facerec.compute_face_descriptor(self.img, shape)
            d_test = numpy.array(face_descriptor)
            for i in descriptors.keys():
                dist_ = numpy.linalg.norm(descriptors[i] - d_test)
                descriptors[i] = dist_
        cd_sorted = sorted(descriptors.items(), key=lambda d: d[1])
        self.id = cd_sorted[0][0]
        self.id = re.sub("\D", "", self.id)

        conn = pymysql.connect('localhost', 'root', 'root', 'dissertation', charset='utf8')
        cur1 = conn.cursor()
        sql = ("SELECT username FROM `personal_info` WHERE studentID=(%s)")
        cur1.execute(sql, self.id)
        self.label.setText(cur1.fetchone()[0])
        conn.commit()
        cur1.close()
        conn.close()
        return True
        # print("\n The person is: ", cd_sorted[0][0])
        # print(dist)

    def showCamera(self):
        #while (1):  # get a frame
        ret, frame = cap.read()  # show a frame

        face_patterns = cv2.CascadeClassifier('D:/project/py/dissertation/haarcascade_frontalface_default.xml')
        faces = face_patterns.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                square = frame[y:y + h, x:x + w]  # 反之则定位错位
            if self.matchFace(square):
                self.timer.stop()
                self.c.openWin.emit(self.id)
                print("running")
                #self.timer.timeout.connect(self.close_signal)


        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        self.r1 = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.label_img.setPixmap(QtGui.QPixmap.fromImage(self.r1))
        self.timer.start(40)

    def showDetail(self):
        print("show")

    def handle_click(self):
        for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
            print("Processing file: {}".format(f))
            self.img = cv2.imread(f)
            dets = detector(self.img, 1)
            print("Number of faces detected: {}".format(len(dets)))
            for k, d in enumerate(dets):
                shape = sp(self.img, d)
                face_descriptor = facerec.compute_face_descriptor(self.img, shape)
                v = numpy.array(face_descriptor)
                descriptors[f] = v
            print(self.img)
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