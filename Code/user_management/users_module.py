import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 851)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.help_button.setFont(font)
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        
        self.aboutUs_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.aboutUs_button.setFont(font)
        self.aboutUs_button.setObjectName("aboutUs_button")
        self.horizontalLayout.addWidget(self.aboutUs_button)
    
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_2.addWidget(self.search_button)
        self.search_button.clicked.connect(self.search_users)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        button_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.shop_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.shop_button.setFont(font)
        self.shop_button.setObjectName("shop_button")
        self.shop_button.setMinimumSize(QtCore.QSize(400, 25))
        self.shop_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.shop_button)
        self.cart_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cart_button.setFont(font)
        self.cart_button.setObjectName("cart_button")
        self.cart_button.setMinimumSize(QtCore.QSize(400, 25))
        self.cart_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.cart_button)
        self.products_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.products_button.setFont(font)
        self.products_button.setObjectName("products_button")
        self.products_button.setMinimumSize(QtCore.QSize(400, 25))
        self.products_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.products_button)
        self.users_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.users_button.setFont(font)
        self.users_button.setObjectName("users_button")
        self.users_button.setMinimumSize(QtCore.QSize(400, 25))
        self.users_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.users_button)
        self.reports_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reports_button.setFont(font)
        self.reports_button.setObjectName("reports_button")
        self.reports_button.setMinimumSize(QtCore.QSize(400, 25))
        self.reports_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.reports_button)
        self.analytics_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.analytics_button.setFont(font)
        self.analytics_button.setObjectName("analytics_button")
        self.analytics_button.setMinimumSize(QtCore.QSize(400, 25))
        self.analytics_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.analytics_button)
        self.returns_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.returns_button.setFont(font)
        self.returns_button.setObjectName("returns_button")
        self.returns_button.setMinimumSize(QtCore.QSize(400, 25))
        self.returns_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.returns_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)

        # Create a QScrollArea and set the QTableWidget inside it
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")

        # Set fixed height for the QTableWidget to show only 10 rows
        self.tableWidget.setFixedHeight(self.tableWidget.verticalHeader().defaultSectionSize() * 30)
        
        self.scrollArea.setWidget(self.tableWidget)
        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)

        self.modifyUser_button = QtWidgets.QPushButton(self.centralwidget)

        self.modifyUser_button.setFont(font)
        self.modifyUser_button.setObjectName("modifyUser_button")
        self.modifyUser_button.setMinimumSize(QtCore.QSize(80, 80))
        self.horizontalLayout_5.addWidget(self.modifyUser_button)
        self.voidProduct_button = QtWidgets.QPushButton(self.centralwidget)

        self.voidProduct_button.setFont(font)
        self.voidProduct_button.setObjectName("voidProduct_button")
        self.voidProduct_button.setMinimumSize(QtCore.QSize(80, 80))
        self.horizontalLayout_5.addWidget(self.voidProduct_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.modifyUser_button.clicked.connect(self.open_modify_user_dialog)
        self.modifyUser_button.setIcon(QtGui.QIcon("edit_icon.png"))  # Set icon for the modify button
        self.modifyUser_button.setIconSize(QtCore.QSize(36, 36))  # Increase icon size


        self.voidProduct_button.clicked.connect(self.void_user)  # Connect void button to the void_product method
        self.voidProduct_button.setIcon(QtGui.QIcon("bin_icon.png"))  # Set icon for the modify button
        self.voidProduct_button.setIconSize(QtCore.QSize(36, 36))  # Increase icon size
        self.load_data()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jewell 7 Hardware"))
        self.help_button.setText(_translate("MainWindow", "Help"))
        self.aboutUs_button.setText(_translate("MainWindow", "About Us"))
        self.logout_button.setText(_translate("MainWindow", "Logout"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.shop_button.setText(_translate("MainWindow", "Shop"))
        self.cart_button.setText(_translate("MainWindow", "Cart"))
        self.products_button.setText(_translate("MainWindow", "Products"))
        self.users_button.setText(_translate("MainWindow", "Users"))
        self.reports_button.setText(_translate("MainWindow", "Reports"))
        self.analytics_button.setText(_translate("MainWindow", "Analytics"))
        self.returns_button.setText(_translate("MainWindow", "Returns"))
        self.modifyUser_button.setText(_translate("MainWindow", ""))
        self.voidProduct_button.setText(_translate("MainWindow", ""))

    def load_data(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()

        if search_query:
            # Filter users based on the search query
            cur.execute("SELECT rowid, username, password, loa FROM users WHERE "
                        "username LIKE ? OR password LIKE ? OR loa LIKE ?",
                        ('%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query)))
        else:
            # Fetch all users if no search query provided
            cur.execute("SELECT rowid, username, password, loa FROM users")

        users = cur.fetchall()
    
        # Display data in the tableWidget
        self.tableWidget.setRowCount(len(users))
        self.tableWidget.setColumnCount(4)  # Adjusted column count to include rowid
        self.tableWidget.setHorizontalHeaderLabels(["RowID", "Username", "Password", "LOA"])

        for i, product in enumerate(users):
            for j, value in enumerate(product):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        self.resize_table()
        conn.close()

        # Hide the RowID column
        self.tableWidget.setColumnHidden(0, True)


    def resize_table(self):
        header = self.tableWidget.horizontalHeader()
        for i in range(1, self.tableWidget.columnCount() - 1):  # Skip RowID column
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(self.tableWidget.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

        vertical_header = self.tableWidget.verticalHeader()
        vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


    def open_modify_user_dialog(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            rowid_item = self.tableWidget.item(selected_row, 0)  # RowID is the first column
            if rowid_item:
                rowid = int(rowid_item.text())

                conn = sqlite3.connect('j7h.db')
                cur = conn.cursor()
                cur.execute("SELECT username, password, loa FROM users WHERE rowid = ?", (rowid,))
                user = cur.fetchone()
                conn.close()

                if user:
                    dialog = ModifyUserDialog(rowid, user)
                    dialog.exec_()
                    self.load_data()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to modify.")

    def void_user(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            # Get the RowID of the selected user
            rowid_item = self.tableWidget.item(selected_row, 0)  # RowID is the first column
            if rowid_item:
                rowid = int(rowid_item.text())

                # Show confirmation dialog
                reply = QtWidgets.QMessageBox.question(
                    None,
                    'Confirmation',
                    'Are you sure you want to void this user?',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No
                )

                if reply == QtWidgets.QMessageBox.Yes:
                    conn = sqlite3.connect('j7h.db')
                    cur = conn.cursor()
                    cur.execute("DELETE FROM users WHERE rowid = ?", (rowid,))
                    conn.commit()
                    conn.close()
                    self.load_data()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to void.")

    def search_users(self):
        search_query = self.lineEdit.text()
        self.load_data(search_query)

class ModifyUserDialog(QtWidgets.QDialog):
    def __init__(self, rowid, user, parent=None):
        super(ModifyUserDialog, self).__init__(parent)
        self.setWindowTitle("Modify User")
        self.setGeometry(300, 300, 400, 400)
        self.rowid = rowid

        self.layout = QtWidgets.QVBoxLayout()
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9]+"))

        self.username_label = QtWidgets.QLabel("Username (required)")
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setText(user[0])
        self.username_input.setValidator(validator)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        self.password_label = QtWidgets.QLabel("Password (required)")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setValidator(validator)
        self.password_input.setText(user[1] or "")
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        self.loa_label = QtWidgets.QLabel("LOA (required)")
        self.loa_input = QtWidgets.QLineEdit()
        self.loa_input.setText(user[2] or "")
        self.layout.addWidget(self.loa_label)
        self.layout.addWidget(self.loa_input)

        self.modify_button = QtWidgets.QPushButton("Modify")
        self.modify_button.clicked.connect(self.modify_user)
        self.layout.addWidget(self.modify_button)
        self.setLayout(self.layout)

    def modify_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        loa = self.loa_input.text()

        if not username or not password or not loa:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Username, password, and loa fields must be filled")
            return

        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("UPDATE users SET username = ?, password = ?, loa = ? WHERE rowid = ?",
                    (username, password, loa, self.rowid))
        conn.commit()
        conn.close()

        self.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
