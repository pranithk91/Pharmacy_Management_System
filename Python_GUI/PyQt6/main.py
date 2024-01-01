from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QFormLayout, QStackedWidget, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pharmacy App")
        self.setGeometry(100, 100, 1920, 1080)
        self.setStyleSheet("background-color: gold;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Sidebar
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        op_button = QPushButton("OP")
        op_button.clicked.connect(self.show_op_frame)
        self.sidebar_layout.addWidget(op_button)

        new_bill_button = QPushButton("New Bill")
        new_bill_button.clicked.connect(self.show_new_bill_frame)
        self.sidebar_layout.addWidget(new_bill_button)

        returns_button = QPushButton("Returns")
        self.sidebar_layout.addWidget(returns_button)

        # Stacked Widget to switch between frames
        self.stacked_widget = QStackedWidget(self.central_widget)
        self.stacked_widget.addWidget(QWidget())  # Placeholder for the default view
        self.stacked_widget.addWidget(self.create_op_frame())
        self.stacked_widget.addWidget(self.create_new_bill_frame())

        # Set up the main layout
        main_layout = QHBoxLayout(self.central_widget)
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget)

    def create_op_frame(self):
        op_frame = QWidget()
        op_layout = QVBoxLayout(op_frame)
        op_frame.setStyleSheet("background-color: white;")

        # Form for collecting data
        form_layout = QHBoxLayout()

        name_entry = QLineEdit()
        age_entry = QLineEdit()

        gender_combo = QComboBox()
        gender_combo.addItems(["Male", "Female", "Other"])

        phone_entry = QLineEdit()

        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(name_entry)
        form_layout.addWidget(QLabel("Age:"))
        form_layout.addWidget(age_entry)
        form_layout.addWidget(QLabel("Gender:"))
        form_layout.addWidget(gender_combo)
        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(phone_entry)

        op_layout.addLayout(form_layout)

        # Table for displaying data
        op_table = QTableWidget()
        op_table.setColumnCount(4)
        op_table.setHorizontalHeaderLabels(["Name", "Age", "Gender", "Phone"])
        op_layout.addWidget(op_table)

        # Submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(lambda: self.update_table(op_table, name_entry.text(), age_entry.text(), gender_combo.currentText(), phone_entry.text()))
        op_layout.addWidget(submit_button)

        return op_frame

    def create_new_bill_frame(self):
        new_bill_frame = QWidget()
        new_bill_layout = QVBoxLayout(new_bill_frame)
        new_bill_frame.setStyleSheet("background-color: white;")

        # Form for collecting data
        form_layout = QFormLayout()

        item_name_entry = QLineEdit()
        quantity_entry = QLineEdit()

        form_layout.addRow("Item Name:", item_name_entry)
        form_layout.addRow("Quantity:", quantity_entry)

        new_bill_layout.addLayout(form_layout)

        # Table for displaying data
        new_bill_table = QTableWidget()
        new_bill_table.setColumnCount(2)
        new_bill_table.setHorizontalHeaderLabels(["Item Name", "Quantity"])
        new_bill_layout.addWidget(new_bill_table)

        # Submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(lambda: self.update_table(new_bill_table, item_name_entry.text(), quantity_entry.text()))
        new_bill_layout.addWidget(submit_button)

        return new_bill_frame

    def show_op_frame(self):
        self.stacked_widget.setCurrentIndex(1)  # Index 1 corresponds to the OP frame

    def show_new_bill_frame(self):
        self.stacked_widget.setCurrentIndex(2)  # Index 2 corresponds to the New Bill frame

    def update_table(self, table, *data):
        # Update the table with the entered data
        row_position = table.rowCount()
        table.insertRow(row_position)
        for column, value in enumerate(data):
            table.setItem(row_position, column, QTableWidgetItem(value))


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
