import cv2 as cv
import numpy as np
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
dir_path = '../openCV/s12/'
dir_path2 = '../openCV/pic/'
res = []
res2 = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(dir_path + path)

for path2 in os.listdir(dir_path2):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path2, path2)):
        res2.append(dir_path2 + path2)



#
# for i in range (1,11):
#     pics.append('s12/'+f'{i}.pgm')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 310, 120, 22))
        self.comboBox.setObjectName("comboBox")
        ##add items
        self.comboBox.addItems(res)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 310, 120, 22))
        self.comboBox_2.setObjectName("comboBox_2")


        ##add items
        self.comboBox_2.addItems(res2)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 741, 281))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ##кнопка для темплейт метода
        self.pushButton.clicked.connect(self.showPicts)
        ##
        self.label.setPixmap(QtGui.QPixmap(self.comboBox.currentText()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
    def showPicts(self):
        self.template()


    def template(self):
        img_rgb = cv.imread(self.comboBox_2.currentText())
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread(self.comboBox.currentText(),0)
        crop_img = template[40:95,10:80]
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,crop_img,cv.TM_CCOEFF_NORMED)
        threshold = 0.1
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        # cv.imwrite('res.png',img_rgb)
        frame = cv.cvtColor(img_rgb, cv.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    # cv.imshow("Template", crop_img)
    # cv.imshow("img_rgb", img_rgb)
    # cv.waitKey(0)
