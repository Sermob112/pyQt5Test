# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qttest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 630, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.Template_but = QtWidgets.QPushButton(self.centralwidget)
        self.Template_but.setGeometry(QtCore.QRect(20, 690, 281, 51))
        self.Template_but.setStyleSheet("font: 16pt \"Lucida Console\";\n"
"background-color: rgb(0, 170, 0);")
        self.Template_but.setObjectName("Template_but")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(540, 630, 161, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(70, 270, 741, 281))
        self.result.setObjectName("result")
        self.tmplate = QtWidgets.QLabel(self.centralwidget)
        self.tmplate.setGeometry(QtCore.QRect(20, 50, 241, 221))
        self.tmplate.setObjectName("tmplate")
        self.pictures = QtWidgets.QLabel(self.centralwidget)
        self.pictures.setGeometry(QtCore.QRect(510, 40, 251, 201))
        self.pictures.setObjectName("pictures")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 230, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(-1)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(-1)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 0, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setLineWidth(-1)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 590, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(-1)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(540, 590, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setLineWidth(-1)
        self.label_8.setObjectName("label_8")
        self.Viola_but = QtWidgets.QPushButton(self.centralwidget)
        self.Viola_but.setGeometry(QtCore.QRect(330, 690, 281, 51))
        self.Viola_but.setStyleSheet("font: 16pt \"Lucida Console\";\n"
"background-color: rgb(0, 170, 0);")
        self.Viola_but.setObjectName("Viola_but")
        self.Sim_but = QtWidgets.QPushButton(self.centralwidget)
        self.Sim_but.setGeometry(QtCore.QRect(660, 690, 281, 51))
        self.Sim_but.setStyleSheet("font: 16pt \"Lucida Console\";\n"
"background-color: rgb(0, 170, 0);")
        self.Sim_but.setObjectName("Sim_but")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 630, 111, 21))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 590, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setLineWidth(-1)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Template_but.setText(_translate("MainWindow", "Template метод"))
        self.result.setText(_translate("MainWindow", "Result"))
        self.tmplate.setText(_translate("MainWindow", "template"))
        self.pictures.setText(_translate("MainWindow", "pictures"))
        self.label_4.setText(_translate("MainWindow", "результат"))
        self.label_5.setText(_translate("MainWindow", "Шаблон"))
        self.label_6.setText(_translate("MainWindow", "Картинка"))
        self.label_7.setText(_translate("MainWindow", "Выбрать картинку 1"))
        self.label_8.setText(_translate("MainWindow", "Выбрать картинку 2"))
        self.Viola_but.setText(_translate("MainWindow", "Метод Виолы-Джонса"))
        self.Sim_but.setText(_translate("MainWindow", "Линии симметрии"))
        self.label_9.setText(_translate("MainWindow", "Уровень точности"))
