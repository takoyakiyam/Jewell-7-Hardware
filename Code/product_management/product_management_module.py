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
        self.search_button.clicked.connect(self.search_products)
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
        self.addProduct_button_2 = QtWidgets.QPushButton(self.centralwidget)

        self.addProduct_button_2.setFont(font)
        self.addProduct_button_2.setObjectName("addProduct_button_2")
        self.addProduct_button_2.setMinimumSize(QtCore.QSize(80, 80))

        self.horizontalLayout_5.addWidget(self.addProduct_button_2)
        self.modifyProduct_button_2 = QtWidgets.QPushButton(self.centralwidget)

        self.modifyProduct_button_2.setFont(font)
        self.modifyProduct_button_2.setObjectName("modifyProduct_button_2")
        self.modifyProduct_button_2.setMinimumSize(QtCore.QSize(80, 80))
        self.horizontalLayout_5.addWidget(self.modifyProduct_button_2)
        self.voidProduct_button_2 = QtWidgets.QPushButton(self.centralwidget)

        self.voidProduct_button_2.setFont(font)
        self.voidProduct_button_2.setObjectName("voidProduct_button_2")
        self.voidProduct_button_2.setMinimumSize(QtCore.QSize(80, 80))
        self.horizontalLayout_5.addWidget(self.voidProduct_button_2)
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

        # Connect button signals to functions
        self.addProduct_button_2.clicked.connect(self.open_add_product_dialog)
        self.addProduct_button_2.setIcon(QtGui.QIcon("plus_icon.png"))  # Set icon for the add button
        self.addProduct_button_2.setIconSize(QtCore.QSize(36, 36))  # Increase icon size
        

        self.modifyProduct_button_2.clicked.connect(self.open_modify_product_dialog)
        self.modifyProduct_button_2.setIcon(QtGui.QIcon("edit_icon.png"))  # Set icon for the modify button
        self.modifyProduct_button_2.setIconSize(QtCore.QSize(36, 36))  # Increase icon size


        self.voidProduct_button_2.clicked.connect(self.void_product)  # Connect void button to the void_product method
        self.voidProduct_button_2.setIcon(QtGui.QIcon("bin_icon.png"))  # Set icon for the modify button
        self.voidProduct_button_2.setIconSize(QtCore.QSize(36, 36))  # Increase icon size
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
        self.addProduct_button_2.setText(_translate("MainWindow", ""))
        self.modifyProduct_button_2.setText(_translate("MainWindow", ""))
        self.voidProduct_button_2.setText(_translate("MainWindow", ""))

    def set_cell_background_color(self, row, column, color):
        item = self.tableWidget.item(row, column)
        if item is not None:
            item.setBackground(QtGui.QColor(color))

    def highlight_qty_cells(self):
        for row in range(self.tableWidget.rowCount()):
            qty_item = self.tableWidget.item(row, 6)  # Assuming the "Qty" column is at index 6
            if qty_item is not None:
                try:
                    qty = float(qty_item.text())
                    if qty <= 5:
                        self.set_cell_background_color(row, 6, "#ffcccc")  # Highlight red
                    elif 5 < qty < 15:
                        self.set_cell_background_color(row, 6, "#ffcc99")  # Highlight orange
                    else:
                        self.set_cell_background_color(row, 6, "#ccffcc")  # Highlight green
                except ValueError:
                    self.set_cell_background_color(row, 6, "#ffffff")  # No highlight for invalid values

    def load_data(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()

        if search_query:
            # Filter products based on the search query
            cur.execute("SELECT rowid, product_name, brand, var, size, price, qty FROM products WHERE "
                        "product_name LIKE ? OR brand LIKE ? OR var LIKE ? OR size LIKE ?",
                        ('%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query)))
        else:
            # Fetch all products if no search query provided
            cur.execute("SELECT rowid, product_name, brand, var, size, price, qty FROM products")

        products = cur.fetchall()
        
        
        
        

        # Display data in the tableWidget
        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(7)  # Adjusted column count to include rowid
        self.tableWidget.setHorizontalHeaderLabels(["RowID", "Product Name", "Brand", "Var", "Size", "Price", "Qty"])

        for i, product in enumerate(products):
            for j, value in enumerate(product):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        self.resize_table()
        conn.close()

        # Hide the RowID column
        self.tableWidget.setColumnHidden(0, True)

        # Highlight Qty cells after loading data
        self.highlight_qty_cells()

    def resize_table(self):
        header = self.tableWidget.horizontalHeader()
        for i in range(1, self.tableWidget.columnCount() - 1):  # Skip RowID column
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(self.tableWidget.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

        vertical_header = self.tableWidget.verticalHeader()
        vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def open_add_product_dialog(self):
        dialog = AddProductDialog()
        dialog.exec_()
        self.load_data()

    def open_modify_product_dialog(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            rowid_item = self.tableWidget.item(selected_row, 0)  # RowID is the first column
            if rowid_item:
                rowid = int(rowid_item.text())

                # Fetch the product details
                conn = sqlite3.connect('j7h.db')
                cur = conn.cursor()
                cur.execute("SELECT product_name, brand, var, size, price, qty FROM products WHERE rowid = ?", (rowid,))
                product = cur.fetchone()
                conn.close()

                if product:
                    dialog = ModifyProductDialog(rowid, product)
                    dialog.exec_()
                    self.load_data()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a product to modify.")

    def void_product(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            # Get the RowID of the selected product
            rowid_item = self.tableWidget.item(selected_row, 0)  # RowID is the first column
            if rowid_item:
                rowid = int(rowid_item.text())

                # Show confirmation dialog
                reply = QtWidgets.QMessageBox.question(
                    None,
                    'Confirmation',
                    'Are you sure you want to void this product?',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No
                )

                if reply == QtWidgets.QMessageBox.Yes:
                    conn = sqlite3.connect('j7h.db')
                    cur = conn.cursor()
                    cur.execute("DELETE FROM products WHERE rowid = ?", (rowid,))
                    conn.commit()
                    conn.close()
                    self.load_data()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a product to void.")

    def search_products(self):
        search_query = self.lineEdit.text()
        self.load_data(search_query)

class AddProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddProductDialog, self).__init__(parent)
        self.setWindowTitle("Add Product")
        self.setGeometry(300, 300, 400, 400)

        self.layout = QtWidgets.QVBoxLayout()

        self.product_name_label = QtWidgets.QLabel("Product Name (required)")
        self.product_name_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.product_name_label)
        self.layout.addWidget(self.product_name_input)

        self.brand_label = QtWidgets.QLabel("Brand")
        self.brand_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.brand_label)
        self.layout.addWidget(self.brand_input)

        self.var_label = QtWidgets.QLabel("Var")
        self.var_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.var_label)
        self.layout.addWidget(self.var_input)

        self.size_label = QtWidgets.QLabel("Size")
        self.size_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.size_label)
        self.layout.addWidget(self.size_input)

        self.price_label = QtWidgets.QLabel("Price (required)")
        self.price_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_input)

        self.qty_label = QtWidgets.QLabel("Qty (required)")
        self.qty_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.qty_label)
        self.layout.addWidget(self.qty_input)

        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)

    def add_product(self):
        product_name = self.product_name_input.text()
        brand = self.brand_input.text() or None
        var = self.var_input.text() or None
        size = self.size_input.text() or None
        price = self.price_input.text()
        qty = self.qty_input.text()

        if not product_name or not price or not qty:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Product name, price, and quantity fields must be filled")
            return

        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO products (product_name, brand, var, size, price, qty) VALUES (?, ?, ?, ?, ?, ?)",
                    (product_name, brand, var, size, float(price), int(qty)))
        conn.commit()
        conn.close()

        self.accept()


class ModifyProductDialog(QtWidgets.QDialog):
    def __init__(self, rowid, product, parent=None):
        super(ModifyProductDialog, self).__init__(parent)
        self.setWindowTitle("Modify Product")
        self.setGeometry(300, 300, 400, 400)
        self.rowid = rowid

        self.layout = QtWidgets.QVBoxLayout()

        self.product_name_label = QtWidgets.QLabel("Product Name (required)")
        self.product_name_input = QtWidgets.QLineEdit()
        self.product_name_input.setText(product[0])
        self.layout.addWidget(self.product_name_label)
        self.layout.addWidget(self.product_name_input)

        self.brand_label = QtWidgets.QLabel("Brand")
        self.brand_input = QtWidgets.QLineEdit()
        self.brand_input.setText(product[1] or "")
        self.layout.addWidget(self.brand_label)
        self.layout.addWidget(self.brand_input)

        self.var_label = QtWidgets.QLabel("Var")
        self.var_input = QtWidgets.QLineEdit()
        self.var_input.setText(product[2] or "")
        self.layout.addWidget(self.var_label)
        self.layout.addWidget(self.var_input)

        self.size_label = QtWidgets.QLabel("Size")
        self.size_input = QtWidgets.QLineEdit()
        self.size_input.setText(product[3] or "")
        self.layout.addWidget(self.size_label)
        self.layout.addWidget(self.size_input)

        self.price_label = QtWidgets.QLabel("Price (required)")
        self.price_input = QtWidgets.QLineEdit()
        self.price_input.setText(str(product[4]))
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_input)

        self.qty_label = QtWidgets.QLabel("Qty (required)")
        self.qty_input = QtWidgets.QLineEdit()
        self.qty_input.setText(str(product[5]))
        self.layout.addWidget(self.qty_label)
        self.layout.addWidget(self.qty_input)

        self.modify_button = QtWidgets.QPushButton("Modify")
        self.modify_button.clicked.connect(self.modify_product)
        self.layout.addWidget(self.modify_button)

        self.setLayout(self.layout)

    def modify_product(self):
        product_name = self.product_name_input.text()
        brand = self.brand_input.text() or None
        var = self.var_input.text() or None
        size = self.size_input.text() or None
        price = self.price_input.text()
        qty = self.qty_input.text()

        if not product_name or not price or not qty:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Product name, price, and quantity fields must be filled")
            return

        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("UPDATE products SET product_name = ?, brand = ?, var = ?, size = ?, price = ?, qty = ? WHERE rowid = ?",
                    (product_name, brand, var, size, float(price), int(qty), self.rowid))
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
