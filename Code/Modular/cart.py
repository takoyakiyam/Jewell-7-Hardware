import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton, QLineEdit
from PyQt5 import QtWidgets
import uuid

class CustomerNameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Name")
        self.layout = QVBoxLayout()
        self.label = QLabel("Enter customer name:")
        self.layout.addWidget(self.label)
        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

    def get_customer_name(self):
        return self.line_edit.text()
    
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

        # Search Component
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.clicked.connect(self.search_cart)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.search_button)
        self.layout.addLayout(self.horizontalLayout)

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

    def load_cart_items(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        if search_query:
            query = """
                SELECT c.product_name, c.qty, c.brand, c.var, c.size, p.price, (c.qty * p.price) AS total_price
                FROM cart c
                INNER JOIN products p ON c.product_name = p.product_name
                WHERE c.product_name LIKE ? OR c.brand LIKE ? OR c.var LIKE ? OR c.size LIKE ?
            """
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        else:
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

    def search_cart(self):
        search_query = self.lineEdit.text()
        self.load_cart_items(search_query)

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
                # Retrieve current quantity from the cart
                cursor.execute("SELECT qty FROM cart WHERE product_name = ?", (product_name,))
                current_qty_in_cart = cursor.fetchone()[0]
                # Update product quantity in the database
                cursor.execute("SELECT qty FROM products WHERE product_name = ?", (product_name,))
                current_qty_in_db = cursor.fetchone()[0]
                new_qty_in_db = current_qty_in_db + current_qty_in_cart
                cursor.execute("UPDATE products SET qty = ? WHERE product_name = ?", (new_qty_in_db, product_name))
                # Delete item from the cart
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
        
        # Retrieve quantities of all products in the cart before clearing
        cursor.execute("SELECT product_name, qty FROM cart")
        quantities_removed = {row[0]: row[1] for row in cursor.fetchall()}

        # Update quantities of items in the products table
        for product_name, qty in quantities_removed.items():
            cursor.execute("UPDATE products SET qty = qty + ? WHERE product_name = ?", (qty, product_name))

        # Clear the cart
        cursor.execute("DELETE FROM cart")
        
        conn.commit()
        conn.close()
        
        # Reload cart items
        self.load_cart_items()
        
        # Inform the user about the cleared cart
        QtWidgets.QMessageBox.information(self, "Clear Cart", "All items have been removed from the cart.")
        
        # Return the quantities of all products removed
        return quantities_removed

    def checkout(self):
        # Prompt user for customer name
        customer_dialog = CustomerNameDialog()
        if customer_dialog.exec_() == QDialog.Accepted:
            customer_name = customer_dialog.get_customer_name()

            # Get current date
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Generate a unique transaction ID
            transaction_id = str(uuid.uuid4())  # Generate a random UUID as a transaction ID

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

                    # Replace with actual transaction type logic
                    transaction_type = "Purchase"
                    # Replace with actual product ID retrieval logic
                    product_id = 1
                    # Replace with actual log ID retrieval logic
                    log_id = 1
                    # Inside the loop where you insert data into the transactions table

                    transaction_id = str(uuid.uuid4())
                    # Insert into transactions table
                    conn = sqlite3.connect('j7h.db')
                    cursor = conn.cursor()
                    cursor.execute('''INSERT INTO transactions (transaction_id, customer, product_name, qty, total_price, date, type, product_id, log_id, brand, var, size)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                (transaction_id, customer_name, product_name, qty, total_price, current_date, transaction_type, product_id, log_id, brand, var, size))
                    conn.commit()
                    conn.close()

            # Clear cart table
            self.clear_cart()

            # Display success message
            QtWidgets.QMessageBox.information(self, "Checkout", "Checkout successful!")

