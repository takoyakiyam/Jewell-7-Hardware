# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(592, 481)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 50, 471, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Jewell7_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        self.Jewell7_label.setFont(font)
        self.Jewell7_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Jewell7_label.setObjectName("Jewell7_label")
        self.verticalLayout.addWidget(self.Jewell7_label)
        self.Hardware_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        self.Hardware_label.setFont(font)
        self.Hardware_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Hardware_label.setObjectName("Hardware_label")
        self.verticalLayout.addWidget(self.Hardware_label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.username_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("background-color:#FFFFFF;")
        self.username_input.setText("")
        self.username_input.setPlaceholderText("")
        self.username_input.setObjectName("username_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_input)
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("background-color:#FFFFFF;")
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setPlaceholderText("")
        self.password_input.setObjectName("password_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_input)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color:#53C851;")
        self.loginButton.setDefault(True)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        # Connect the "Login" button to the login_user method
        self.loginButton.clicked.connect(self.login_user)
        self.horizontalLayout.addWidget(self.loginButton)
        self.forgotButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.forgotButton.setFont(font)
        self.forgotButton.setStyleSheet("background-color:#E14545;\n"
"")
        self.forgotButton.setDefault(True)
        self.forgotButton.setObjectName("forgotButton")
        self.horizontalLayout.addWidget(self.forgotButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 22))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.Jewell7_label.setText(_translate("Login", "Jewell 7 "))
        self.Hardware_label.setText(_translate("Login", "Hardware"))
        self.username_label.setText(_translate("Login", "Username:"))
        self.password_label.setText(_translate("Login", "Password:"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.forgotButton.setText(_translate("Login", "Forgot Password?"))

    def login_user(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        # Validation: Check if any field is empty
        if not all([username, password]):
            self.show_error_message("Please fill in all the fields.")
            return

        # Establishing connection with SQLite database
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            # SQL query to check if the username exists and retrieve user_id and password
            query = "SELECT user_id, password FROM users WHERE username = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
        
            # Check if the query returned a result
            if result is None:
                self.show_error_message("Invalid username or password.")
                return

            # If username exists, check if password matches
            user_id, stored_password = result
            if stored_password == password:
                # Get the current date and time
                current_datetime = datetime.today()
                date_log = current_datetime.strftime('%Y-%m-%d')
                time_log = current_datetime.strftime("%I:%M %p")

                # Inserting data into the user_logs table
                action = "login"
                cursor.execute('''INSERT INTO user_logs (user_id, action, time, date) 
                              VALUES (?, ?, ?, ?)''', (user_id, action, time_log, date_log))
                conn.commit()

                # Display success message
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("User Logged In Successfully!")
                msg.setWindowTitle("Success")
                msg.exec_()
            else:
                self.show_error_message("Invalid username or password.")
        except sqlite3.Error as e:
            self.show_error_message(f"Database error: {e}")
        finally:
            # Closing connection
            conn.close()

    def show_error_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
