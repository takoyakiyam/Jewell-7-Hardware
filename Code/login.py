# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 399)
        Dialog.setStyleSheet("background-color:#D9D9D9;")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(130, 100, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(140, 40, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(20, 10, 121, 20))
        self.label1.setObjectName("label1")
        self.userlogintext = QtWidgets.QLineEdit(Dialog)
        self.userlogintext.setGeometry(QtCore.QRect(70, 180, 351, 40))
        self.userlogintext.setStyleSheet("background-color:#FFFFFF;")
        self.userlogintext.setText("")
        self.userlogintext.setObjectName("userlogintext")
        self.lineEdit4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit4.setGeometry(QtCore.QRect(70, 240, 351, 40))
        self.lineEdit4.setStyleSheet("background-color:#FFFFFF;")
        self.lineEdit4.setText("")
        self.lineEdit4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit4.setObjectName("lineEdit4")
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(90, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("background-color:#53C851;")
        self.pushButton1.setDefault(True)
        self.pushButton1.setFlat(False)
        self.pushButton1.setObjectName("pushButton1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 310, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("color: red;\n"
"text-decoration: underline;")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label3.setText(_translate("Dialog", "  Hardware"))
        self.label2.setText(_translate("Dialog", "   Jewell 7 "))
        self.label1.setText(_translate("Dialog", "User Login"))
        self.userlogintext.setPlaceholderText(_translate("Dialog", "First Name:"))
        self.lineEdit4.setPlaceholderText(_translate("Dialog", "Password:"))
        self.pushButton1.setText(_translate("Dialog", "Confirm"))
        self.label.setText(_translate("Dialog", "Forgot Password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
