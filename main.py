import cv2 as cv
import numpy as np
# pyuic5 QTest.ui -o name.py

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from end import Ui_MainWindow
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def application():
    app = QApplication(sys.argv)
    window = mywindow()

    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    application()

#
# def template(temp, pic):
#     img_rgb = cv.imread(pic)
#     img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
#     template = cv.imread(temp,0)
#     crop_img = template[40:95,10:80]
#     w, h = template.shape[::-1]
#     res = cv.matchTemplate(img_gray,crop_img,cv.TM_CCOEFF_NORMED)
#     threshold = 0.8
#     loc = np.where( res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#     # cv.imwrite('res.png',img_rgb)
#
#     cv.imshow("Template", crop_img)
#     cv.imshow("img_rgb", img_rgb)
#     cv.waitKey(0)
# template('s12/1.pgm','s12/s12_all.pbm')
