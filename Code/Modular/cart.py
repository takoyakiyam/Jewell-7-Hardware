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
        self.cart_table.setColumnCount(7)
        self.cart_table.setHorizontalHeaderLabels(['Product', 'Brand', 'Variation', 'Size', 'Quantity', 'Price', 'Total'])
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

        # Join the 'cart' and 'products' tables to retrieve all necessary fields
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
                    price_item = self.cart_table.item(row, 5)
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
        # Get current date
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Iterate over rows in the cart table
        for row in range(self.cart_table.rowCount()):
            product_name_item = self.cart_table.item(row, 0)
            qty_item = self.cart_table.item(row, 4)
            price_item = self.cart_table.item(row, 5)
            total_price_item = self.cart_table.item(row, 6)
            brand_item = self.cart_table.item(row, 1)
            var_item = self.cart_table.item(row, 2)
            size_item = self.cart_table.item(row, 3)

            # Extract data from table items
            if all(item is not None for item in [product_name_item, qty_item, price_item, total_price_item, brand_item, var_item, size_item]):
                product_name = product_name_item.text()
                qty = int(qty_item.text())
                price = float(price_item.text())
                total_price = float(total_price_item.text())
                brand = brand_item.text()
                var = var_item.text()
                size = size_item.text()

                # Replace with actual customer logic
                customer = "Default Customer"
                # Replace with actual transaction type logic
                transaction_type = "Purchase"
                # Replace with actual product ID retrieval logic
                product_id = 1
                # Replace with actual log ID retrieval logic
                log_id = 1

                # Insert into transactions table
                conn = sqlite3.connect('j7h.db')
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO transactions (customer, product_name, qty, total_price, date, type, product_id, log_id, brand, var, size)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (customer, product_name, qty, total_price, current_date, transaction_type, product_id, log_id, brand, var, size))
                conn.commit()
                conn.close()

        # Clear cart table
        self.clear_cart()

        # Display success message
        QtWidgets.QMessageBox.information(self, "Checkout", "Checkout successful!")

