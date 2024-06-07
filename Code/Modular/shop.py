import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets


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
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[3])))  # var
            self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data[4])))  # size
            self.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(row_data[5])))  # price
            qty = row_data[6]  # qty
            self.tableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(qty)))  # Convert qty to string before setting it as text
        conn.close()

    def search_products(self):
        search_query = self.lineEdit.text()
        self.load_data(search_query)

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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['Product', 'Brand', 'Variation', 'Size', 'Price', 'Items in Stock'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.layout.addWidget(self.tableWidget)

        self.load_products()

        self.add_to_cart_button = QPushButton("Add to Cart")
        self.add_to_cart_button.clicked.connect(self.show_add_to_cart_dialog)
        self.layout.addWidget(self.add_to_cart_button)

        self.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)

    def add_to_cart(self, quantity):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            product_item = self.tableWidget.item(row, 0)  # Product name
            brand_item = self.tableWidget.item(row, 1)  # Brand
            var_item = self.tableWidget.item(row, 2)  # Variation
            size_item = self.tableWidget.item(row, 3)  # Size
            price_item = self.tableWidget.item(row, 4)  # Price
            qty_item = self.tableWidget.item(row, 5)  # Items in stock

            if qty_item is not None and product_item is not None and price_item is not None:
                try:
                    current_qty = float(qty_item.text())
                    new_qty = current_qty - quantity
                    if new_qty >= 0:
                        qty_item.setText(str(int(new_qty)))

                        conn = sqlite3.connect('j7h.db')
                        cursor = conn.cursor()
                        cursor.execute('''CREATE TABLE IF NOT EXISTS cart (
                                            cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            product_name TEXT,
                                            qty INTEGER,
                                            total_price NUMERIC,
                                            date TEXT,
                                            transaction_id INTEGER,
                                            product_id INTEGER,
                                            log_id INTEGER,
                                            brand TEXT,
                                            var TEXT,
                                            size TEXT)''')

                        product_id = 1  # Replace with actual product ID retrieval logic
                        product_name = product_item.text()
                        brand = brand_item.text()
                        var = var_item.text()
                        size = size_item.text()
                        price = float(price_item.text())
                        total_price = quantity * price
                        user_id = 1  # Replace with actual user ID retrieval logic
                        log_id = 1  # Replace with actual log ID retrieval logic
                        transaction_id = 1  # Replace with actual transaction ID logic
                        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        cursor.execute('''INSERT INTO cart (product_name, qty, total_price, date, transaction_id, product_id, log_id, brand, var, size)
                                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                       (product_name, quantity, total_price, date, transaction_id, product_id, log_id, brand, var, size))

                        conn.commit()

                        if new_qty == 0:
                            self.tableWidget.removeRow(row)
                        conn.close()

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
                qty_item = self.tableWidget.item(row, 5)
                if qty_item is not None:
                    try:
                        qty = float(qty_item.text())
                        max_quantity = min(max_quantity, qty)
                    except ValueError:
                        pass
            if max_quantity == float("inf"):
                max_quantity = 1000000
            dialog = AddToCartDialog(max_quantity=int(max_quantity))
            if dialog.exec_() == QDialog.Accepted:
                quantity = dialog.get_quantity()
                self.add_to_cart(quantity)
        else:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a product to add to the cart.")


class CartTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cart')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.cart_table = QtWidgets.QTableWidget()
        self.cart_table.setColumnCount(7)
        self.cart_table.setHorizontalHeaderLabels(['Product', 'Brand', 'Variation', 'Size', 'Quantity', 'Price', 'Total'])
        self.cart_table.horizontalHeader().setStretchLastSection(True)
        self.cart_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.layout.addWidget(self.cart_table)

        self.remove_button = QtWidgets.QPushButton("Remove Item")
        self.update_button = QtWidgets.QPushButton("Update Quantity")
        self.clear_button = QtWidgets.QPushButton("Clear Cart")
        self.checkout_button = QtWidgets.QPushButton("Checkout")

        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.update_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.checkout_button)

        self.remove_button.clicked.connect(self.remove_item)
        self.update_button.clicked.connect(self.update_quantity)
        self.clear_button.clicked.connect(self.clear_cart)
        self.checkout_button.clicked.connect(self.checkout)

        self.cart_table.itemSelectionChanged.connect(self.on_selection_changed)

    def load_cart_items(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT c.product_name, c.qty, c.brand, c.var, c.size, p.price, (c.qty * p.price) AS total_price
            FROM cart c
            INNER JOIN products p ON c.product_name = p.product_name
        """)
        rows = cursor.fetchall()

        self.cart_table.setRowCount(len(rows))
        for row_number, row_data in enumerate(rows):
            product_name = str(row_data[0])
            quantity = int(row_data[1])
            brand = str(row_data[2])
            var = str(row_data[3])
            size = str(row_data[4])
            price = float(row_data[5])
            total_price = float(row_data[6])

            self.cart_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(product_name))  # Product Name
            self.cart_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(brand))  # Brand
            self.cart_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(var))  # Variation
            self.cart_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(size))  # Size
            self.cart_table.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(quantity)))  # Quantity
            self.cart_table.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(price)))  # Price
            self.cart_table.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(total_price)))  # Total

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
        if selected_rows:
            conn = sqlite3.connect('j7h.db')
            cursor = conn.cursor()
            for row in selected_rows:
                product_name = self.cart_table.item(row, 0).text()
                cursor.execute("DELETE FROM cart WHERE product_name = ?", (product_name,))
            conn.commit()
            conn.close()
            self.load_cart_items()
        else:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select an item to remove.")

    def update_quantity(self):
        selected_rows = set()
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        if selected_rows:
            conn = sqlite3.connect('j7h.db')
            cursor = conn.cursor()
            for row in selected_rows:
                product_name = self.cart_table.item(row, 0).text()
                quantity, ok = QtWidgets.QInputDialog.getInt(self, "Update Quantity", "Enter new quantity:")
                if ok:
                    cursor.execute("UPDATE cart SET qty = ? WHERE product_name = ?", (quantity, product_name))
            conn.commit()
            conn.close()
            self.load_cart_items()
        else:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select an item to update.")

    def clear_cart(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cart")
        conn.commit()
        conn.close()
        self.load_cart_items()

    def checkout(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cart")
        cart_items = cursor.fetchall()

        if cart_items:
            for item in cart_items:
                cart_id, product_name, qty, total_price, date, transaction_id, product_id, log_id, brand, var, size = item
                cursor.execute('''INSERT INTO orders (product_name, qty, total_price, date, transaction_id, product_id, log_id, brand, var, size)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                               (product_name, qty, total_price, date, transaction_id, product_id, log_id, brand, var, size))
                cursor.execute("DELETE FROM cart WHERE cart_id = ?", (cart_id,))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Checkout", "Order placed successfully!")
        else:
            QtWidgets.QMessageBox.warning(self, "Checkout", "Cart is empty.")

        conn.close()
        self.load_cart_items()
