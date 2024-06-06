import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.transactions_table.setColumnCount(9)  # Update column count to include 'Customer'
        self.transactions_table.setHorizontalHeaderLabels([
            'ID', 'Customer', 'Quantity', 'Product Name', 'Date', 'Total Price', 
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
        cursor.execute("""SELECT transactions.transaction_id, transactions.customer, transactions.qty, transactions.date, transactions.total_price, 
                            transactions.product_id, products.product_name, products.brand, products.var, products.size, transactions.log_id
                        FROM transactions
                        JOIN products ON transactions.product_id = products.product_id""")
        rows = cursor.fetchall()
        self.transactions_table.setRowCount(len(rows))
        for row_number, row_data in enumerate(rows):
            for column_number, data in enumerate(row_data):
                if column_number == 0:
                    self.transactions_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(data)))
                elif column_number == 1:
                    self.transactions_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(data)))
                elif column_number == 2:
                    self.transactions_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(data)))
                elif column_number == 5:
                    self.transactions_table.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(data)))
                elif column_number == 6:
                    self.transactions_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(data)))
                elif column_number == 7:
                    self.transactions_table.setItem(row_number, 8, QtWidgets.QTableWidgetItem(str(data)))
                elif column_number == 10:
                    self.transactions_table.setItem(row_number, 9, QtWidgets.QTableWidgetItem(str(data)))
                else:
                    self.transactions_table.setItem(row_number, column_number + 3, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()