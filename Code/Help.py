# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(1066, 885)
        self.centralwidget = QtWidgets.QWidget(Help)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.help_button.setFont(font)
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        self.aboutUs_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.aboutUs_button.setFont(font)
        self.aboutUs_button.setObjectName("aboutUs_button")
        self.horizontalLayout.addWidget(self.aboutUs_button)
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shop_button = QtWidgets.QPushButton(self.centralwidget)
        self.shop_button.setMinimumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.shop_button.setFont(font)
        self.shop_button.setObjectName("shop_button")
        self.verticalLayout_2.addWidget(self.shop_button)
        self.cart_button = QtWidgets.QPushButton(self.centralwidget)
        self.cart_button.setMinimumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cart_button.setFont(font)
        self.cart_button.setObjectName("cart_button")
        self.verticalLayout_2.addWidget(self.cart_button)
        self.products_button = QtWidgets.QPushButton(self.centralwidget)
        self.products_button.setMinimumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.products_button.setFont(font)
        self.products_button.setObjectName("products_button")
        self.verticalLayout_2.addWidget(self.products_button)
        self.users_button = QtWidgets.QPushButton(self.centralwidget)
        self.users_button.setMinimumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.users_button.setFont(font)
        self.users_button.setObjectName("users_button")
        self.verticalLayout_2.addWidget(self.users_button)
        self.reports_button = QtWidgets.QPushButton(self.centralwidget)
        self.reports_button.setMinimumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reports_button.setFont(font)
        self.reports_button.setObjectName("reports_button")
        self.verticalLayout_2.addWidget(self.reports_button)
        self.analytics_button = QtWidgets.QPushButton(self.centralwidget)
        self.analytics_button.setMinimumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.analytics_button.setFont(font)
        self.analytics_button.setObjectName("analytics_button")
        self.verticalLayout_2.addWidget(self.analytics_button)
        self.returns_button = QtWidgets.QPushButton(self.centralwidget)
        self.returns_button.setMinimumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.returns_button.setFont(font)
        self.returns_button.setObjectName("returns_button")
        self.verticalLayout_2.addWidget(self.returns_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setStyleSheet("background-color:#E7E7E7;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_2.addWidget(self.textEdit_3, 2, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 3, 1, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_2.addWidget(self.textEdit_4, 3, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("background-color:#E7E7E7;")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 2, 1, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setStyleSheet("background-color:#E7E7E7;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_2.addWidget(self.textEdit_5, 4, 1, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setStyleSheet("background-color:#E7E7E7;")
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_2.addWidget(self.textEdit_6, 4, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Help.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Help)
        self.statusbar.setObjectName("statusbar")
        Help.setStatusBar(self.statusbar)

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Help"))
        self.label.setText(_translate("Help", "Jewell 7 Hardware"))
        self.help_button.setText(_translate("Help", "Help"))
        self.aboutUs_button.setText(_translate("Help", "About Us"))
        self.logout_button.setText(_translate("Help", "Logout"))
        self.shop_button.setText(_translate("Help", "Shop"))
        self.cart_button.setText(_translate("Help", "Cart"))
        self.products_button.setText(_translate("Help", "Products"))
        self.users_button.setText(_translate("Help", "Users"))
        self.reports_button.setText(_translate("Help", "Reports"))
        self.analytics_button.setText(_translate("Help", "Analytics"))
        self.returns_button.setText(_translate("Help", "Returns"))
        self.textEdit_3.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">1. Go to Menu<br />2. Select an item<br />3. Press the “Add to Cart” button</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">What does the colored stock value mean?</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">orange = “low stock”<br />red = “extremely low stock”</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">How to add an item in the cart?</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Is the search bar case-sensitive?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Help = QtWidgets.QMainWindow()
    ui = Ui_Help()
    ui.setupUi(Help)
    Help.show()
    sys.exit(app.exec_())
