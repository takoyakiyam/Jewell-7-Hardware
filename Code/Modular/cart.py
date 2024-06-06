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

        # Join the 'cart' and 'products' tables to retrieve product price
        cursor.execute("""
            SELECT c.product_name, c.qty, p.price AS price
            FROM cart c
            INNER JOIN products p ON c.product_name = p.product_name
        """)
        rows = cursor.fetchall()

        self.cart_table.setRowCount(len(rows))
        for row_number, row_data in enumerate(rows):
            product_name = str(row_data[0])
            quantity = int(row_data[1])
            price = float(row_data[2])  # Access price from the joined 'products' table
            total_price = quantity * price

            self.cart_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(product_name))  # Product Name
            self.cart_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(quantity)))  # Quantity
            self.cart_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(price)))  # Price
            self.cart_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(total_price)))  # Total

        conn.close()



    def search_products(self):
        search_query = self.lineEdit.text()
        self.load_data(search_query)

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
                total_price = row[3] * price  
                cursor.execute("INSERT INTO transactions (customer, product_name, brand, var, size, qty, total_price, date, product_id, log_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (None, product_name, brand, var, size, row[2], total_price, current_date, row[6], row[7]))

        cursor.execute("DELETE FROM cart")
        conn.commit()
        conn.close()
        self.load_cart_items()
        QtWidgets.QMessageBox.information(self, "Checkout", "Checkout successful!")
