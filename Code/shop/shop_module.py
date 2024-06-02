import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
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

        # Create a QStackedWidget for different views
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        
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

        # Connect buttons to methods
        self.shop_button.clicked.connect(self.open_shop)
        self.cart_button.clicked.connect(self.open_cart)
        self.products_button.clicked.connect(self.open_products)
        self.users_button.clicked.connect(self.open_users)
        self.reports_button.clicked.connect(self.open_reports)
        self.analytics_button.clicked.connect(self.open_analytics)
        self.returns_button.clicked.connect(self.open_returns)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Admin Dashboard"))
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


    def open_shop(self):
        self.shop_tab = ShopTab()
        self.stackedWidget.addWidget(self.shop_tab)
        self.stackedWidget.setCurrentWidget(self.shop_tab)
        self.shop_tab.item_added_to_cart.connect(self.update_cart_tab)

    def open_cart(self):
        self.cart_tab = CartTab()
        self.stackedWidget.addWidget(self.cart_tab)
        self.stackedWidget.setCurrentWidget(self.cart_tab)
        self.update_cart_tab()

    def update_cart_tab(self):
        if hasattr(self, 'cart_tab'):
            self.cart_tab.load_cart_items()

    def open_products(self):
        pass

    def open_users(self):
        pass

    def open_reports(self):
        self.reports_tab = ReportsTab()
        self.stackedWidget.addWidget(self.reports_tab)
        self.stackedWidget.setCurrentWidget(self.reports_tab)

    def open_analytics(self):
        pass

    def open_returns(self):
        pass

    def search_products(self):
        search_text = self.lineEdit.text()
        print(f"Searching for '{search_text}'")

    def add_to_cart(self):
        # Implement the add to cart functionality here
        pass

class AddToCartDialog(QDialog):
    def __init__(self, parent=None, max_quantity=10):
        super().__init__(parent)
        self.setWindowTitle("Add to Cart")
        self.layout = QVBoxLayout()
        self.label = QLabel("Enter quantity:")
        self.layout.addWidget(self.label)
        self.spin_box = QSpinBox()
        self.spin_box.setMaximum(max_quantity)
        self.layout.addWidget(self.spin_box)
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.accept)
        self.layout.addWidget(self.add_button)
        self.setLayout(self.layout)

    def get_quantity(self):
        return self.spin_box.value()

# Class for Shop
class ShopTab(QtWidgets.QWidget):
    item_added_to_cart = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def load_products(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE qty > 0")
        rows = cursor.fetchall()
        self.tableWidget.setRowCount(len(rows))
        for row_number, row_data in enumerate(rows):
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))  # product
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))  # brand
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[5])))  # price
            qty = row_data[6]  # qty
            self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(qty)))  # Convert qty to string before setting it as text
        conn.close()

    def on_selection_changed(self):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item:
                    item.setSelected(True)

    def initUI(self):
        self.setWindowTitle('Shop')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Product', 'Brand', 'Price', 'Items in Stock'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.layout.addWidget(self.tableWidget)

        self.load_products()

        self.add_to_cart_button = QPushButton("Add to Cart")
        self.add_to_cart_button.clicked.connect(self.show_add_to_cart_dialog)
        self.layout.addWidget(self.add_to_cart_button)

        # Connect itemSelectionChanged signal to handle row selection
        self.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)

    def add_to_cart(self, quantity):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            product_item = self.tableWidget.item(row, 0)  # Product name
            price_item = self.tableWidget.item(row, 2)  # Price
            qty_item = self.tableWidget.item(row, 3)  # Items in stock

            if qty_item is not None and product_item is not None and price_item is not None:
                try:
                    current_qty = float(qty_item.text())
                    new_qty = current_qty - quantity
                    if new_qty >= 0:
                        qty_item.setText(str(int(new_qty)))

                        # Add item to cart in database
                        conn = sqlite3.connect('j7h.db')
                        cursor = conn.cursor()
                        cursor.execute('''CREATE TABLE IF NOT EXISTS cart (
                                            cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            qty INTEGER,
                                            product_name TEXT,
                                            date TEXT,
                                            total_price NUMERIC,
                                            transaction_id INTEGER,
                                            product_id INTEGER,
                                            user_id INTEGER,
                                            log_id INTEGER)''')

                        product_id = 1  # Replace with actual product ID retrieval logic
                        product_name = product_item.text()
                        price = float(price_item.text())
                        total_price = quantity * price
                        user_id = 1  # Replace with actual user ID retrieval logic
                        log_id = 1  # Replace with actual log ID retrieval logic
                        transaction_id = 1  # Replace with actual transaction ID logic
                        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time

                        cursor.execute('''INSERT INTO cart (qty, product_name, date, total_price, transaction_id, product_id, log_id)
                  VALUES (?, ?, ?, ?, ?, ?, ?)''', (quantity, product_name, date, total_price, transaction_id, product_id, log_id))

                        conn.commit()

                        # If the new quantity is 0, remove the row from the table
                        if new_qty == 0:
                            self.tableWidget.removeRow(row)
                        conn.close()

                        # Emit signal to notify cart tab
                        self.item_added_to_cart.emit()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Quantity Error", "Not enough items in stock.")
                except ValueError:
                    pass

    def show_add_to_cart_dialog(self):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        if selected_rows:
            max_quantity = float("inf")
            for row in selected_rows:
                qty_item = self.tableWidget.item(row, 3) 
                if qty_item is not None:
                    try:
                        qty = float(qty_item.text())
                        max_quantity = min(max_quantity, qty)
                    except ValueError:
                        pass
            if max_quantity == float("inf"):  # Check if max_quantity is infinity
                max_quantity = 1000000  # Set a large maximum value
            dialog = AddToCartDialog(max_quantity=int(max_quantity))  # Convert to integer
            if dialog.exec_() == QDialog.Accepted:
                quantity = dialog.get_quantity()
                self.add_to_cart(quantity)
                self.add_to_cart_button.clicked.connect(lambda: self.add_to_cart(quantity))
        else:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a product to add to the cart.")     

#Class for Cart Tab
class CartTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Cart')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create a table to display cart items
        self.cart_table = QtWidgets.QTableWidget()
        self.cart_table.setColumnCount(4)
        self.cart_table.setHorizontalHeaderLabels(['Product', 'Quantity', 'Price', 'Total'])
        self.cart_table.horizontalHeader().setStretchLastSection(True)
        self.cart_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.layout.addWidget(self.cart_table)

        # Create buttons for cart operations
        self.remove_button = QtWidgets.QPushButton("Remove Item")
        self.update_button = QtWidgets.QPushButton("Update Quantity")
        self.clear_button = QtWidgets.QPushButton("Clear Cart")
        self.checkout_button = QtWidgets.QPushButton("Checkout")


        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.update_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.checkout_button)
        
        # Connect buttons to methods
        self.remove_button.clicked.connect(self.remove_item)
        self.update_button.clicked.connect(self.update_quantity)
        self.clear_button.clicked.connect(self.clear_cart) 
        self.checkout_button.clicked.connect(self.checkout)
        

        # Connect itemSelectionChanged signal to handle row selection
        self.cart_table.itemSelectionChanged.connect(self.on_selection_changed)

    def load_cart_items(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("SELECT product_name, qty, total_price FROM cart")
        rows = cursor.fetchall()
        self.cart_table.setRowCount(len(rows))
        for row_number, row_data in enumerate(rows):
            self.cart_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))  # Product Name
            self.cart_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))  # Quantity
            self.cart_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[2])))  # Price
            self.cart_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data[2])))  # Total
        conn.close()
        
    def on_selection_changed(self):
        selected_rows = set()
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.cart_table.columnCount()):
                item = self.cart_table.item(row, column)
                if item:
                    item.setSelected(True)

    def remove_item(self):
        selected_rows = set()
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        for row in selected_rows:
            product_item = self.cart_table.item(row, 0)
            if product_item is not None:
                product_name = product_item.text()
                cursor.execute("DELETE FROM cart WHERE product_name = ?", (product_name,))
        conn.commit()
        conn.close()
        self.load_cart_items()

    def update_quantity(self):
        selected_rows = set()
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        if selected_rows:
            dialog = AddToCartDialog()
            if dialog.exec_() == QDialog.Accepted:
                quantity = dialog.get_quantity()
                conn = sqlite3.connect('j7h.db')
                cursor = conn.cursor()
                for row in selected_rows:
                    product_item = self.cart_table.item(row, 0)
                    price_item = self.cart_table.item(row, 2)
                    if product_item is not None and price_item is not None:
                        product_name = product_item.text()
                        price = float(price_item.text())
                        total = quantity * price
                        cursor.execute("UPDATE cart SET qty = ?, total_price = ? WHERE product_name = ?", (quantity, total, product_name))
                conn.commit()
                conn.close()
                self.load_cart_items()

    def clear_cart(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cart")
        conn.commit()
        conn.close()
        self.load_cart_items()
        QtWidgets.QMessageBox.information(self, "Clear Cart", "All items have been removed from the cart.")

    def checkout(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        # Create transactions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            customer TEXT,
                            product_name TEXT,
                            brand TEXT,
                            var TEXT,
                            size TEXT,
                            qty INTEGER,
                            total_price NUMERIC,
                            date TEXT,
                            type TEXT,
                            product_id INTEGER,
                            log_id INTEGER)''')

        # Get current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        cursor.execute("SELECT * FROM cart")
        rows = cursor.fetchall()
        for row in rows:
            # Fetch additional details from the products table based on product_id
            cursor.execute("SELECT product_name, brand, var, size, price FROM products WHERE product_id = ?", (row[6],))
            product_data = cursor.fetchone()
            if product_data:
                product_name, brand, var, size, price = product_data
                total_price = row[3]  # Assuming total_price is stored in cart table
                cursor.execute("INSERT INTO transactions (transaction_id, product_name, brand, var, size, qty, total_price, date, product_id, log_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (None, product_name, brand, var, size, row[2], total_price, current_date, row[6], row[7]))
        cursor.execute("DELETE FROM cart")
        conn.commit()
        conn.close()
        self.load_cart_items()
        QtWidgets.QMessageBox.information(self, "Checkout", "Checkout successful!")


#Class for Products Tab
class ProductsTab(QtWidgets.QWidget):
   pass

#Class for Reports Tab
class ReportsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Reports')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create tab widget and sub-tabs
        self.tab_widget = QtWidgets.QTabWidget()
        self.reports_tab = QtWidgets.QWidget()
        self.transactions_tab = QtWidgets.QWidget()

        # Add sub-tabs to the tab widget
        self.tab_widget.addTab(self.reports_tab, "Reports")  
        self.tab_widget.addTab(self.transactions_tab, "Transactions")

        # Set layouts for each sub-tab
        self.initReportsTab()
        self.initTransactionsTab()

        self.layout.addWidget(self.tab_widget)

    def initReportsTab(self):
        layout = QtWidgets.QVBoxLayout(self.reports_tab)
        self.reports_label = QtWidgets.QLabel("This is the Reports section.")
        layout.addWidget(self.reports_label)

    def initTransactionsTab(self):
        layout = QtWidgets.QVBoxLayout(self.transactions_tab)
        
        # Create the table widget
        self.transactions_table = QtWidgets.QTableWidget()
        self.transactions_table.setColumnCount(8)
        self.transactions_table.setHorizontalHeaderLabels([
            'ID', 'Quantity', 'Product Name', 'Date', 'Total Price', 
            'Transaction ID', 'Product ID', 'Log ID'
        ])
        self.transactions_table.horizontalHeader().setStretchLastSection(True)
        self.transactions_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Add the table widget to the layout
        layout.addWidget(self.transactions_table)

        # Load transactions into the table
        self.load_transactions()

    def load_transactions(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT transactions.transaction_id, transactions.qty, transactions.date, transactions.total_price, 
                            transactions.product_id, products.product_name, products.brand, products.var, products.size
                        FROM transactions
                        JOIN products ON transactions.product_id = products.product_id""")
        rows = cursor.fetchall()
        print(rows)  # Print query results
        self.transactions_table.setRowCount(len(rows))
        for row_number, row_data in enumerate(rows):
            for column_number, data in enumerate(row_data):
                self.transactions_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
