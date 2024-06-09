import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView
from PyQt5 import QtWidgets

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

        # Connect itemSelectionChanged signal to handle row selection
        self.transactions_table.itemSelectionChanged.connect(self.on_selection_changed)

    def initReportsTab(self):
        layout = QtWidgets.QVBoxLayout(self.reports_tab)
        self.reports_label = QtWidgets.QLabel("This is the Reports section.")
        layout.addWidget(self.reports_label)

    def initTransactionsTab(self):
        layout = QtWidgets.QVBoxLayout(self.transactions_tab)
        
        # Create the table widget
        self.transactions_table = QtWidgets.QTableWidget()
        self.transactions_table.setColumnCount(10)  # Update column count to match the number of columns
        self.transactions_table.setHorizontalHeaderLabels([
            'Transaction ID', 'Customer', 'Quantity', 'Date and Time', 'Total Price', 'Product ID', 'Product Name', 
            'Brand', 'Size', 'Variation'
        ])
        self.transactions_table.horizontalHeader().setStretchLastSection(True)
        self.transactions_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Add the table widget to the layout
        layout.addWidget(self.transactions_table)

        # Load transactions into the table
        self.load_transactions()

    def on_selection_changed(self):
        selected_rows = set()
        for item in self.transactions_table.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.transactions_table.columnCount()):
                item = self.transactions_table.item(row, column)
                if item:
                    item.setSelected(True)

    def load_transactions(self):
            conn = sqlite3.connect('j7h.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT transactions.transaction_id, transactions.customer, transactions.qty, transactions.date, transactions.total_price, 
                                transactions.product_id, products.product_name, products.brand, products.size, products.var, transactions.log_id
                            FROM transactions
                            JOIN products ON transactions.product_id = products.product_id""")
            rows = cursor.fetchall()
            conn.close()

            # Group rows by date
            grouped_rows = {}
            for row in rows:
                date = row[3]  # Assuming date is at index 3
                if date not in grouped_rows:
                    grouped_rows[date] = []
                grouped_rows[date].append(row)

            # Calculate total number of rows after grouping
            total_rows = sum(len(group) for group in grouped_rows.values())

            # Set the number of rows in the table
            self.transactions_table.setRowCount(total_rows)

            # Populate the table with transaction data
            row_number = 0
            for date, group in grouped_rows.items():
                # Span rows with the same date
                self.transactions_table.setSpan(row_number, 0, len(group), 1)  # Span from row_number, column 0, spanning len(group) rows, 1 column
                for row_data in group:
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        self.transactions_table.setItem(row_number, column_number, item)
                    row_number += 1

            # Resize columns to fit contents
            self.transactions_table.resizeColumnsToContents()
