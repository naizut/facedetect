import cv2
from PyQt5 import QtWidgets,QtGui
cap=cv2.VideoCapture(0)

class camera(QtWidgets.QWidget,UiForm):
    def __init__(self):
        super(camera, self).__init__()
        self.setupUi(self)
        while (1):  # get a frame
            ret, frame = cap.read()  # show a frame

            face_patterns = cv2.CascadeClassifier('D:/project/py/dissertation/haarcascade_frontalface_default.xml')
            faces = face_patterns.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("author:KevinZ", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
