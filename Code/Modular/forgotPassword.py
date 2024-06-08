import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Ui_ForgotPassword(object):
    def setupUi(self, ForgotPassword):
        ForgotPassword.setObjectName("ForgotPassword")
        ForgotPassword.resize(592, 481)
        self.centralwidget = QtWidgets.QWidget(ForgotPassword)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 110, 531, 225))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.birthdate_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.birthdate_label.setFont(font)
        self.birthdate_label.setObjectName("birthdate_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.birthdate_label)
        self.middleName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.middleName_label.setFont(font)
        self.middleName_label.setObjectName("middleName_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.middleName_label)
        self.birthdate_input = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.birthdate_input.setFont(font)
        self.birthdate_input.setMouseTracking(False)
        self.birthdate_input.setStyleSheet("background-color:#FFFFFF;")
        self.birthdate_input.setCalendarPopup(True)
        self.birthdate_input.setObjectName("birthdate_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.birthdate_input)
        self.middleName_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.middleName_input.setFont(font)
        self.middleName_input.setObjectName("middleName_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.middleName_input)
        self.newPassword_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.newPassword_label.setFont(font)
        self.newPassword_label.setObjectName("newPassword_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.newPassword_label)
        self.confirmPassword_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.confirmPassword_label.setFont(font)
        self.confirmPassword_label.setObjectName("confirmPassword_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.confirmPassword_label)
        self.newPassword_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.newPassword_input.setFont(font)
        self.newPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassword_input.setObjectName("newPassword_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.newPassword_input)
        self.confirmPassword_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.confirmPassword_input.setFont(font)
        self.confirmPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword_input.setObjectName("confirmPassword_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.confirmPassword_input)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.changePassword_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.changePassword_button.setFont(font)
        self.changePassword_button.setStyleSheet("background-color:#53C851;")
        self.changePassword_button.setDefault(True)
        self.changePassword_button.setFlat(False)
        self.changePassword_button.setObjectName("changePassword_button")
        self.horizontalLayout.addWidget(self.changePassword_button)
        
        # Add the Back button
        self.back_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background-color:#C85353;")
        self.back_button.setDefault(False)
        self.back_button.setFlat(False)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        ForgotPassword.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ForgotPassword)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 22))
        self.menubar.setObjectName("menubar")
        ForgotPassword.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ForgotPassword)
        self.statusbar.setObjectName("statusbar")
        ForgotPassword.setStatusBar(self.statusbar)

        self.retranslateUi(ForgotPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgotPassword)

        # Connect the "Change Password" button to the change_password method
        self.changePassword_button.clicked.connect(self.change_password)
        # Connect the "Back" button to the go_back method
        self.back_button.clicked.connect(self.go_back)

    def retranslateUi(self, ForgotPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgotPassword.setWindowTitle(_translate("ForgotPassword", "Forgot Password"))
        self.birthdate_label.setText(_translate("ForgotPassword", "Birthdate:"))
        self.middleName_label.setText(_translate("ForgotPassword", "Middle Name:"))
        self.newPassword_label.setText(_translate("ForgotPassword", "New Password:"))
        self.confirmPassword_label.setText(_translate("ForgotPassword", "Confirm Password:"))
        self.changePassword_button.setText(_translate("ForgotPassword", "Change Password"))
        self.back_button.setText(_translate("ForgotPassword", "Back"))

    def change_password(self):
        birthdate = self.birthdate_input.date().toString(QtCore.Qt.ISODate)
        middle_name = self.middleName_input.text().strip()
        new_password = self.newPassword_input.text().strip()
        confirm_password = self.confirmPassword_input.text().strip()

        # Validation: Check if any field is empty
        if not all([birthdate, middle_name, new_password, confirm_password]):
            self.show_error_message("Please fill in all the fields.")
            return

        # Validation: Check if new password and confirm password match
        if new_password != confirm_password:
            self.show_error_message("New password and confirm password do not match.")
            return

        # Establishing connection with SQLite database
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            # SQL query to verify the birthdate and middle name
            query = "SELECT user_id FROM admin WHERE birthdate = ? AND middle_name = ?"
            cursor.execute(query, (birthdate, middle_name))
            result = cursor.fetchone()

            # Check if the query returned a result
            if result is None:
                self.show_error_message("Invalid birthdate or middle name.")
                return

            # If the details are correct, update the password in the database
            user_id = result[0]
            # Get the current date and time
            current_datetime = datetime.today()
            date_log = current_datetime.strftime('%Y-%m-%d')
            time_log = current_datetime.strftime("%I:%M %p")

            # Inserting data into the user_logs table
            action = "changed password"
            cursor.execute('''INSERT INTO user_logs (user_id, action, time, date) 
                      VALUES (?, ?, ?, ?)''', (user_id, action, time_log, date_log))
    
            # Update the password in the users table
            cursor.execute("UPDATE users SET password = ? WHERE user_id = ?", (new_password, user_id))

            conn.commit()

            # Display success message
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Password changed successfully!")
            msg.setWindowTitle("Success")
            msg.exec_()

            # Close the forgot password window
            self.close_window()
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

    def close_window(self):
        QtWidgets.QApplication.instance().activeWindow().close()

    def go_back(self):
        # Close the forgot password window
        self.close_window()
        # Reopen the login window
        self.open_login_window()

    def open_login_window(self):
        self.login_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.login_window)
        self.login_window.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 90, 601, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.username_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)
        self.username_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_input.setFont(font)
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 0, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 2, 0, 1, 2)
        self.forgotPassword_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.forgotPassword_button.setFont(font)
        self.forgotPassword_button.setObjectName("forgotPassword_button")
        self.forgotPassword_button.setGeometry(QtCore.QRect(90, 350, 601, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the "Forgot Password" button to the open_forgot_password method
        self.forgotPassword_button.clicked.connect(self.open_forgot_password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Username:"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.forgotPassword_button.setText(_translate("MainWindow", "Forgot Password"))

    def open_forgot_password(self):
        self.forgot_password_window = QtWidgets.QMainWindow()
        self.ui = Ui_ForgotPassword()
        self.ui.setupUi(self.forgot_password_window)
        self.forgot_password_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
