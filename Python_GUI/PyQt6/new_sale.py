from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, QComboBox, QFrame, QLineEdit, QDockWidget

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys



class CTk:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.root = QMainWindow()
        self.root.setWindowTitle("Pranith Pharmacy")
        self.root.setGeometry(100, 100, 800, 600)
    
    def initUI(self):
        # Sidebar Frame
        self.sidebar_frame = SidebarFrame(self.root)
        dock_widget = QDockWidget("Sidebar")
        dock_widget.setWidget(self.sidebar_frame)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)

        # Main View Frame
        self.main_view = MainViewFrame(self.root)
        self.root.setCentralWidget(self.main_view)

    def run(self):
        self.root.show()
        sys.exit(self.app.exec())

class SidebarFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(176)
        self.setStyleSheet("background-color: #2A8C55;")

        # Logo
        self.logoLabel = QLabel(self)
        self.logoLabel.setGeometry(50, 38, 77, 85)
        self.logoLabel.setPixmap(QPixmap("Python_GUI/ctk/logo.png"))

        # Buttons
        self.create_button("OP Register", "plus_icon.png", self.clientWindow, 160, 160)
        self.create_button("Orders", "list_icon.png", None, 160, 160)
        self.create_button("Returns", "returns_icon.png", None, 160, 160)
        self.create_button("Settings", "settings_icon.png", None, 160, 160)
        self.create_button("Account", "person_icon.png", None, 160, 160)

    def create_button(self, text, image_filename, command, width, height):
        button = QPushButton(self)
        #button.setIconSize(32)
        button.setGeometry(8, height, width, height)
        button.setText(text)
        button.setStyleSheet("background-color: transparent; color: white; font: bold 14px;")
        icon = QIcon(QPixmap("Python_GUI\ctk\{image_filename}"))
         
        button.setIcon(icon)

        if command:
            button.clicked.connect(command)

    def clientWindow(self):
        self.main_view.showFrame(ClientMainViewFrame)

class MainViewFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("background-color: #fff;")

        self.initUI()

    def initUI(self):
        # Clear Bill Table
        def clearBillTable():
            numRows = self.billTable.rowCount()
            for row in range(numRows):
                self.billTable.removeRow(0)
            self.billTotalLabel.setText("Bill Total: 0")


        """def get_time():
            string = strftime('%H:%M:%S %p')
            self.timeLabel.configure(text=string)
            self.timeLabel.after(1000, get_time)
        get_time()"""

        # New Sale Section
        self.titleLabel = QLabel("New Bill", self)
        self.titleLabel.setStyleSheet("font: bold 25px; color: #2A8C55;")
        self.titleLabel.setGeometry(27, 29, 200, 30)

        # Time Label
        self.timeLabel = QLabel(self)
        self.timeLabel.setStyleSheet("font: bold 17px; color: #2A8C55;")
        self.timeLabel.setGeometry(650, 0, 150, 30)

        # Client Section
        self.clientGrid = QFrame(self)
        self.clientGrid.setGeometry(27, 90, 626, 150)
        self.clientGrid.setStyleSheet("background-color: transparent;")

        self.clientNameLabel = QLabel("Patient Name", self.clientGrid)
        self.clientNameLabel.setGeometry(0, 0, 150, 30)
        # ... (Continue for other labels and entries)

        # Search Section
        self.searchGrid = QFrame(self)
        self.searchGrid.setGeometry(27, 270, 626, 150)
        self.searchGrid.setStyleSheet("background-color: transparent;")

        self.itemNameLabel = QLabel("Item Name", self.searchGrid)
        self.itemNameLabel.setGeometry(0, 0, 150, 30)
        # ... (Continue for other labels and entries)

        # Buttons and Quantity Frame
        self.addToBillButton = QPushButton("Add to Bill", self.searchGrid)
        self.addToBillButton.setGeometry(485, 60, 120, 40)
        self.addToBillButton.setStyleSheet("background-color: #2A8C55; color: #fff; font: bold 17px;")
        self.addToBillButton.clicked.connect(self.getMedDetails)

        quantity_frame = QFrame(self.searchGrid)
        quantity_frame.setGeometry(330, 60, 150, 40)
        quantity_frame.setStyleSheet("background-color: transparent;")

        self.qtyDecreaseButton = QPushButton("-", quantity_frame)
        self.qtyDecreaseButton.setGeometry(0, 0, 40, 40)
        self.qtyDecreaseButton.setStyleSheet("background-color: #2A8C55; color: #fff; font: bold 16px;")
        self.qtyDecreaseButton.clicked.connect(self.quantityDecrease)

        self.qtySaleEntry = QLineEdit(self.searchGrid)
        self.qtySaleEntry.setGeometry(400, 60, 60, 40)
        # ... (Continue for other buttons and labels)

        self.qtyIncreaseButton = QPushButton("+", quantity_frame)
        self.qtyIncreaseButton.setGeometry(110, 0, 40, 40)
        self.qtyIncreaseButton.setStyleSheet("background-color: #2A8C55; color: #fff; font: bold 16px;")
        self.qtyIncreaseButton.clicked.connect(self.quantityIncrease)

        self.qtyInStockLabel = QLabel("Quantity in Stock: 0", self.searchGrid)
        self.qtyInStockLabel.setGeometry(0, 120, 300, 30)

        # Bill Table
        billTableFrame = QFrame(self)
        billTableFrame.setGeometry(27, 440, 626, 150)
        billTableFrame.setStyleSheet("background-color: transparent;")

        self.newSaleButton = QPushButton("Clear Table", billTableFrame)
        self.newSaleButton.setGeometry(506, 0, 120, 30)
        self.newSaleButton.setStyleSheet("background-color: #2A8C55; color: #fff; font: bold 17px;")
        self.newSaleButton.clicked.connect(clearBillTable)

        self.billTable = QTableWidget(billTableFrame)
        self.billTable.setGeometry(0, 30, 626, 90)
        self.billTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.billTable.setColumnCount(6)
        self.billTable.setHorizontalHeaderLabels(["Name", "Type", "Stock", "MRP", "Quantity", "Total Price"])
        # ... (Adjust styles and properties as needed)

        self.billTotalLabel = QLabel("Bill Total: 0", billTableFrame)
        self.billTotalLabel.setGeometry(400, 120, 200, 30)
        self.billTotalLabel.setStyleSheet("font: bold 17px; color: #52A476;")

    def getMedDetails(self):
        # Implementation for getting medicine details
        pass

    def quantityDecrease(self):
        # Implementation for decreasing quantity
        pass

    def quantityIncrease(self):
        # Implementation for increasing quantity
        pass

    def showFrame(self, frame_class):
        frame = frame_class(self)
        self.parent().setCentralWidget(frame)

class ClientMainViewFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("background-color: #fff;")

        self.initUI()

    def initUI(self):
        # Add your functions here

        # New Sale Section
        self.titleLabel = QLabel("New Bill", self)
        self.titleLabel.setStyleSheet("font: bold 25px; color: #2A8C55;")
        self.titleLabel.setGeometry(27, 29, 200, 30)

        # Time Label
        self.timeLabel = QLabel(self)
        self.timeLabel.setStyleSheet("font: bold 17px; color: #2A8C55;")
        self.timeLabel.setGeometry(650, 0, 150, 30)

        # Client Section
        self.clientGrid = QFrame(self)
        self.clientGrid.setGeometry(27, 90, 626, 150)
        self.clientGrid.setStyleSheet("background-color: transparent;")

        self.clientNameLabel = QLabel("Patient Name", self.clientGrid)
        self.clientNameLabel.setGeometry(0, 0, 150, 30)
        # ... (Continue for other labels and entries)

        # Client Details Section
        self.clientdetGrid = QFrame(self)
        self.clientdetGrid.setGeometry(27, 270, 626, 150)
        self.clientdetGrid.setStyleSheet("background-color: transparent;")

        self.clientGenderLabel = QLabel("Gender", self.clientdetGrid)
        self.clientGenderLabel.setGeometry(0, 0, 150, 30)
        # ... (Continue for other labels and entries)

        # Table section
        self.opTableFrame = QFrame(self)
        self.opTableFrame.setGeometry(27, 440, 626, 150)
        self.opTableFrame.setStyleSheet("background-color: transparent;")

        self.confirmDetailsButton = QPushButton("Confirm Details", self.opTableFrame)
        self.confirmDetailsButton.setGeometry(506, 0, 120, 30)
        self.confirmDetailsButton.setStyleSheet("background-color: #2A8C55; color: #fff; font: bold 17px;")
        self.confirmDetailsButton.clicked.connect(self.addToTable)

        self.warningLabel = QLabel(self.opTableFrame)
        self.warningLabel.setGeometry(0, 30, 626, 30)
        self.warningLabel.setStyleSheet("font: bold 17px; color: #52A476;")

        self.opTable = QTableWidget(self.opTableFrame)
        self.opTable.setGeometry(0, 60, 626, 60)
        self.opTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.opTable.setColumnCount(6)
        self.opTable.setHorizontalHeaderLabels(["Patient Name", "Phone No.", "Gender", "Age", "OP/Proc", "Amount"])
        # ... (Adjust styles and properties as needed)

        self.billTotalLabel = QLabel("Bill Total: 0", self.opTableFrame)
        self.billTotalLabel.setGeometry(400, 120, 200, 30)
        self.billTotalLabel.setStyleSheet("font: bold 17px; color: #52A476;")

    def addToTable(self):
        # Implementation for adding details to the table
        pass

if __name__ == "__main__":
    app = CTk()
    app.run()
