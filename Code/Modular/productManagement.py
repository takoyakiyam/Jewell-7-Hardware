import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

#Class for Products Tab
class ProductsTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.search_button = QtWidgets.QPushButton(self)
        self.search_button.setFont(font)
        self.search_button.setText("Search")
        self.search_button.clicked.connect(self.search_products)
        self.horizontalLayout_2.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setFixedHeight(self.tableWidget.verticalHeader().defaultSectionSize() * 30)
        self.scrollArea.setWidget(self.tableWidget)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        
        self.addProduct_button = QtWidgets.QPushButton(self)
        self.addProduct_button.setFont(font)
        self.addProduct_button.setMinimumSize(QtCore.QSize(80, 80))
        self.addProduct_button.setIcon(QtGui.QIcon("plus_icon.png"))
        self.addProduct_button.setIconSize(QtCore.QSize(36, 36))
        self.addProduct_button.clicked.connect(self.open_add_product_dialog)
        self.horizontalLayout_5.addWidget(self.addProduct_button)
        
        self.modifyProduct_button = QtWidgets.QPushButton(self)
        self.modifyProduct_button.setFont(font)
        self.modifyProduct_button.setMinimumSize(QtCore.QSize(80, 80))
        self.modifyProduct_button.setIcon(QtGui.QIcon("edit_icon.png"))
        self.modifyProduct_button.setIconSize(QtCore.QSize(36, 36))
        self.modifyProduct_button.clicked.connect(self.open_modify_product_dialog)
        self.horizontalLayout_5.addWidget(self.modifyProduct_button)
        
        self.voidProduct_button = QtWidgets.QPushButton(self)
        self.voidProduct_button.setFont(font)
        self.voidProduct_button.setMinimumSize(QtCore.QSize(80, 80))
        self.voidProduct_button.setIcon(QtGui.QIcon("bin_icon.png"))
        self.voidProduct_button.setIconSize(QtCore.QSize(36, 36))
        self.voidProduct_button.clicked.connect(self.void_product)
        self.horizontalLayout_5.addWidget(self.voidProduct_button)
        
        self.verticalLayout.addLayout(self.horizontalLayout_5)

    def set_cell_background_color(self, row, column, color):
        item = self.tableWidget.item(row, column)
        if item is not None:
            item.setBackground(QtGui.QColor(color))

    def highlight_qty_cells(self):
        for row in range(self.tableWidget.rowCount()):
            qty_item = self.tableWidget.item(row, 6)
            if qty_item is not None:
                try:
                    qty = float(qty_item.text())
                    if qty <= 5:
                        self.set_cell_background_color(row, 6, "#ffcccc")
                    elif 5 < qty < 15:
                        self.set_cell_background_color(row, 6, "#ffcc99")
                    else:
                        self.set_cell_background_color(row, 6, "#ccffcc")
                except ValueError:
                    self.set_cell_background_color(row, 6, "#ffffff")

    def load_data(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        if search_query:
            cur.execute("SELECT rowid, product_name, brand, var, size, price, qty FROM products WHERE "
                        "product_name LIKE ? OR brand LIKE ? OR var LIKE ? OR size LIKE ?",
                        ('%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query)))
        else:
            cur.execute("SELECT rowid, product_name, brand, var, size, price, qty FROM products")

        products = cur.fetchall()
        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["RowID", "Product Name", "Brand", "Var", "Size", "Price", "Qty"])

        for i, product in enumerate(products):
            for j, value in enumerate(product):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        self.resize_table()
        conn.close()
        self.tableWidget.setColumnHidden(0, True)
        self.highlight_qty_cells()

    def resize_table(self):
        header = self.tableWidget.horizontalHeader()
        for i in range(1, self.tableWidget.columnCount() - 1):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(self.tableWidget.columnCount() - 1, QtWidgets.QHeaderView.ResizeToContents)

    def search_products(self):
        search_query = self.lineEdit.text()
        self.load_data(search_query)

    def open_add_product_dialog(self):
        dialog = AddProductDialog(self)
        dialog.exec_()
        self.load_data()

    def open_modify_product_dialog(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a product to modify.")
            return

        row = selected_items[0].row()
        rowid = self.tableWidget.item(row, 0).text()
        product_name = self.tableWidget.item(row, 1).text()
        brand = self.tableWidget.item(row, 2).text()
        var = self.tableWidget.item(row, 3).text()
        size = self.tableWidget.item(row, 4).text()
        price = self.tableWidget.item(row, 5).text()
        qty = self.tableWidget.item(row, 6).text()

        dialog = ModifyProductDialog(self, rowid, product_name, brand, var, size, price, qty)
        dialog.exec_()
        self.load_data()

    def void_product(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a product to void.")
            return

        row = selected_items[0].row()
        rowid = self.tableWidget.item(row, 0).text()
        
        confirmation = QtWidgets.QMessageBox.question(self, "Confirm Deletion",
                                                      "Are you sure you want to void this product?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if confirmation == QtWidgets.QMessageBox.Yes:
            conn = sqlite3.connect('j7h.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM products WHERE rowid=?", (rowid,))
            conn.commit()
            conn.close()
            self.load_data()
            QtWidgets.QMessageBox.information(self, "Success", "Product successfully voided.")

class AddProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Product")
        self.setGeometry(100, 100, 300, 200)
        layout = QtWidgets.QVBoxLayout()

        self.product_name_label = QtWidgets.QLabel("Product Name:")
        self.product_name_input = QtWidgets.QLineEdit()
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_input)

        self.brand_label = QtWidgets.QLabel("Brand:")
        self.brand_input = QtWidgets.QLineEdit()
        layout.addWidget(self.brand_label)
        layout.addWidget(self.brand_input)

        self.var_label = QtWidgets.QLabel("Var:")
        self.var_input = QtWidgets.QLineEdit()
        layout.addWidget(self.var_label)
        layout.addWidget(self.var_input)

        self.size_label = QtWidgets.QLabel("Size:")
        self.size_input = QtWidgets.QLineEdit()
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)

        self.price_label = QtWidgets.QLabel("Price:")
        self.price_input = QtWidgets.QLineEdit()
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.qty_label = QtWidgets.QLabel("Qty:")
        self.qty_input = QtWidgets.QLineEdit()
        layout.addWidget(self.qty_label)
        layout.addWidget(self.qty_input)

        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_product(self):
        product_name = self.product_name_input.text()
        brand = self.brand_input.text()
        var = self.var_input.text()
        size = self.size_input.text()
        price = self.price_input.text()
        qty = self.qty_input.text()

        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO products (product_name, brand, var, size, price, qty) VALUES (?, ?, ?, ?, ?, ?)",
                    (product_name, brand, var, size, price, qty))
        conn.commit()
        conn.close()

        self.accept()

class ModifyProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, rowid=None, product_name=None, brand=None, var=None, size=None, price=None, qty=None):
        super().__init__(parent)
        self.setWindowTitle("Modify Product")
        self.setGeometry(100, 100, 300, 200)
        self.rowid = rowid

        layout = QtWidgets.QVBoxLayout()

        self.product_name_label = QtWidgets.QLabel("Product Name:")
        self.product_name_input = QtWidgets.QLineEdit(product_name)
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_input)

        self.brand_label = QtWidgets.QLabel("Brand:")
        self.brand_input = QtWidgets.QLineEdit(brand)
        layout.addWidget(self.brand_label)
        layout.addWidget(self.brand_input)

        self.var_label = QtWidgets.QLabel("Var:")
        self.var_input = QtWidgets.QLineEdit(var)
        layout.addWidget(self.var_label)
        layout.addWidget(self.var_input)

        self.size_label = QtWidgets.QLabel("Size:")
        self.size_input = QtWidgets.QLineEdit(size)
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)

        self.price_label = QtWidgets.QLabel("Price:")
        self.price_input = QtWidgets.QLineEdit(price)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.qty_label = QtWidgets.QLabel("Qty:")
        self.qty_input = QtWidgets.QLineEdit(qty)
        layout.addWidget(self.qty_label)
        layout.addWidget(self.qty_input)

        self.modify_button = QtWidgets.QPushButton("Modify")
        self.modify_button.clicked.connect(self.modify_product)
        layout.addWidget(self.modify_button)

        self.setLayout(layout)

    def modify_product(self):
        product_name = self.product_name_input.text()
        brand = self.brand_input.text()
        var = self.var_input.text()
        size = self.size_input.text()
        price = self.price_input.text()
        qty = self.qty_input.text()

        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("UPDATE products SET product_name=?, brand=?, var=?, size=?, price=?, qty=? WHERE rowid=?",
                    (product_name, brand, var, size, price, qty, self.rowid))
        conn.commit()
        conn.close()

        self.accept()