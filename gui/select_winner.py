# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_winner.ui'
#
# Created: Wed Aug  9 17:02:21 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 909)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(9, 10, 1280, 781))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_load = QtGui.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(7, 830, 61, 27))
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_success = QtGui.QPushButton(self.centralwidget)
        self.pushButton_success.setGeometry(QtCore.QRect(640, 800, 81, 27))
        self.pushButton_success.setObjectName("pushButton_success")
        self.pushButton_fail = QtGui.QPushButton(self.centralwidget)
        self.pushButton_fail.setGeometry(QtCore.QRect(560, 800, 81, 27))
        self.pushButton_fail.setObjectName("pushButton_fail")
        self.pushButton_save = QtGui.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(1160, 835, 120, 27))
        self.pushButton_save.setObjectName("pushButton_save")
        self.checkBox_evaluation_exists = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_evaluation_exists.setGeometry(QtCore.QRect(830, 830, 111, 21))
        self.checkBox_evaluation_exists.setObjectName("checkBox_evaluation_exists")
        self.pushButton_next = QtGui.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(730, 800, 81, 27))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_pre = QtGui.QPushButton(self.centralwidget)
        self.pushButton_pre.setGeometry(QtCore.QRect(470, 800, 81, 27))
        self.pushButton_pre.setObjectName("pushButton_pre")
        self.textEdit_path = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_path.setGeometry(QtCore.QRect(70, 830, 721, 30))
        self.textEdit_path.setReadOnly(False)
        self.textEdit_path.setObjectName("textEdit_path")
        self.textEdit_evaluation_value = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_evaluation_value.setGeometry(QtCore.QRect(950, 825, 151, 30))
        self.textEdit_evaluation_value.setReadOnly(False)
        self.textEdit_evaluation_value.setObjectName("textEdit_evaluation_value")
        self.checkBox_auto_save = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_auto_save.setGeometry(QtCore.QRect(830, 800, 171, 21))
        self.checkBox_auto_save.setObjectName("checkBox_auto_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_load.setText(QtGui.QApplication.translate("MainWindow", "load", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_success.setText(QtGui.QApplication.translate("MainWindow", "success", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_fail.setText(QtGui.QApplication.translate("MainWindow", "fail", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("MainWindow", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_evaluation_exists.setText(QtGui.QApplication.translate("MainWindow", "evaluation exist", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next.setText(QtGui.QApplication.translate("MainWindow", "next>>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pre.setText(QtGui.QApplication.translate("MainWindow", "<<previous", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_auto_save.setText(QtGui.QApplication.translate("MainWindow", "save automatically", None, QtGui.QApplication.UnicodeUTF8))

