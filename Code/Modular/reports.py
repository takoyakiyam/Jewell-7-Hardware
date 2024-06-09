import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5 import QtWidgets, QtCore


#Class for Reports Tab
class ReportsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flagged_rows = set()
        
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

        # Create buttons for clearing logs and flagging transactions
        buttons_layout = QtWidgets.QHBoxLayout()
        clear_logs_button = QtWidgets.QPushButton("Clear Transaction Logs")
        flag_transaction_button = QtWidgets.QPushButton("Flag Transaction")
        delete_log_button = QtWidgets.QPushButton("Remove Transction")

        # Connect button signals to slots
        clear_logs_button.clicked.connect(self.clear_logs)
        flag_transaction_button.clicked.connect(self.flag_transaction)
        delete_log_button.clicked.connect(self.remove_log)

        # Add buttons to the layout
        buttons_layout.addWidget(clear_logs_button)
        buttons_layout.addWidget(flag_transaction_button)
        buttons_layout.addWidget(delete_log_button)

        # Add buttons layout to the main layout
        layout.addLayout(buttons_layout)

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
            if len(group) > 1:
                self.transactions_table.setSpan(row_number, 0, len(group), 1)  # Span from row_number, column 0, spanning len(group) rows, 1 column
            for row_data in group:
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.transactions_table.setItem(row_number, column_number, item)
                row_number += 1

        # Resize columns to fit contents
        self.transactions_table.resizeColumnsToContents()
    
    def flag_transaction(self):
        for item in self.transactions_table.selectedItems():
            row = item.row()
            if row not in self.flagged_rows:
                self.flagged_rows.add(row)
                for column in range(self.transactions_table.columnCount()):
                    item = self.transactions_table.item(row, column)
                    if item:
                        item.setData(QtCore.Qt.ItemDataRole.UserRole, 'flagged')  # Set a flag to mark the row as flagged
            else:
                self.flagged_rows.remove(row)
                for column in range(self.transactions_table.columnCount()):
                    item = self.transactions_table.item(row, column)
                    if item:
                        item.setData(QtCore.Qt.ItemDataRole.UserRole, None)  # Remove the flag

        # Apply the stylesheet to the flagged rows
        self.transactions_table.setStyleSheet('''
            QTableWidgetItem[data-flagged="true"] {
                border: 2px solid red;
                border-style: solid;
            }
        ''')

    def remove_log(self):
        selected_items = self.transactions_table.selectedItems()
        if not selected_items:
            return

        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to remove selected logs?', 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            rows_to_remove = set()
            transaction_ids = []  # Store transaction IDs to delete from the database
            for item in selected_items:
                row = item.row()
                column = item.column()
                transaction_id = self.transactions_table.item(row, 0).text()  # Assuming transaction ID is in column 0
                rows_to_remove.add(row)
                transaction_ids.append(transaction_id)

            # Remove the flagged rows from the table
            for row in sorted(rows_to_remove, reverse=True):
                self.transactions_table.removeRow(row)
                # Since the rows are removed, adjust the flagged rows set accordingly
                self.flagged_rows.discard(row)

            # Delete logs from the database
            for transaction_id in transaction_ids:
                self.delete_log_from_database(transaction_id)

    def delete_log_from_database(self, transaction_id):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE transaction_id = ?", (transaction_id,))
        conn.commit()
        conn.close()

    def clear_logs(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to clear all logs?', 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Clear the table
            self.transactions_table.clearContents()
            self.transactions_table.setRowCount(0)
            # Delete all log entries from the database
            self.delete_all_logs_from_database()

    def delete_all_logs_from_database(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions")
        conn.commit()
        conn.close()
