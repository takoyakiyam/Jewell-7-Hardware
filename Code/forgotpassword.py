# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotpassword.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ForgotPassword(object):
    def setupUi(self, ForgotPassword, previous_window=None):
        self.previous_window = previous_window  # Store the reference to the previous window
        self.ForgotPassword = ForgotPassword  # Store reference to the current dialog
        ForgotPassword.setObjectName("ForgotPassword")
        ForgotPassword.resize(500, 400)
        ForgotPassword.setStyleSheet("background-color:#D9D9D9;")
        self.dateEdit = QtWidgets.QDateEdit(ForgotPassword)
        self.dateEdit.setGeometry(QtCore.QRect(90, 140, 351, 40))
        self.dateEdit.setStyleSheet("background-color:#FFFFFF;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit5 = QtWidgets.QLineEdit(ForgotPassword)
        self.lineEdit5.setGeometry(QtCore.QRect(90, 200, 351, 40))
        self.lineEdit5.setStyleSheet("background-color:#FFFFFF;")
        self.lineEdit5.setText("")
        self.lineEdit5.setObjectName("lineEdit5")
        self.pushButton1 = QtWidgets.QPushButton(ForgotPassword)
        self.pushButton1.setGeometry(QtCore.QRect(290, 260, 141, 41))
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
        self.pushButton = QtWidgets.QPushButton(ForgotPassword)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.pushButton.setStyleSheet("background-color:#D9D9D9;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_back)

        self.retranslateUi(ForgotPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgotPassword)

    def retranslateUi(self, ForgotPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgotPassword.setWindowTitle(_translate("ForgotPassword", "Forgot Password"))
        self.lineEdit5.setPlaceholderText(_translate("ForgotPassword", "Mother's maiden name:"))
        self.pushButton1.setText(_translate("ForgotPassword", "Confirm"))
        self.pushButton.setText(_translate("ForgotPassword", "← Forgot Password"))

    def go_back(self):
        if self.previous_window:
            self.previous_window.show()
        self.ForgotPassword.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPassword = QtWidgets.QDialog()
    ui = Ui_ForgotPassword()
    ui.setupUi(ForgotPassword)
    ForgotPassword.show()
    sys.exit(app.exec_())
