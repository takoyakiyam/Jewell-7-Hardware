# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from register import Ui_ProductManagement
from StaffOrAdmin import Ui_Registration
from login import Ui_Dialog
from forgotpassword import Ui_ForgotPassword
from Staff import Ui_Staff
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
   
    def open(self):
        self.window1 = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window1)
        MainWindow1.hide()
        self.window1.exec_()
    
    def openwindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.window, MainWindow1)
        MainWindow1.hide()
        self.window.show()

    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.setEnabled(True)
        MainWindow1.resize(500, 400)
        MainWindow1.setStyleSheet("background-color:#D9D9D9;")
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(130, 30, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(120, 90, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.registerbtn = QtWidgets.QPushButton(self.centralwidget)
        self.registerbtn.setGeometry(QtCore.QRect(80, 270, 331, 51))
        self.registerbtn.clicked.connect(self.openwindow)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.registerbtn.setFont(font)
        self.registerbtn.setStyleSheet("background-color:#53C851;")
        self.registerbtn.setDefault(True)
        self.registerbtn.setFlat(False)
        self.registerbtn.setObjectName("registerbtn")
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtn.setGeometry(QtCore.QRect(80, 200, 331, 51))
        self.LoginBtn.clicked.connect(self.open)

      


        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LoginBtn.setFont(font)
        self.LoginBtn.setStyleSheet("background-color:#53C851;")
        self.LoginBtn.setDefault(True)
        self.LoginBtn.setFlat(False)
        self.LoginBtn.setObjectName("LoginBtn")

          

        MainWindow1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

      

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.label2.setText(_translate("MainWindow1", "   Jewell 7 "))
        self.label3.setText(_translate("MainWindow1", "  Hardware"))
        self.registerbtn.setText(_translate("MainWindow1", "Register"))
        self.LoginBtn.setText(_translate("MainWindow1", "Login"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
