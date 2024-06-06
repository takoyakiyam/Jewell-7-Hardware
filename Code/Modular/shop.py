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
