import pandas as pd
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
 
class WaypointsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        # Create main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
 
        # Create table widget
        self.table_widget = QTableWidget()
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Stretch columns
        self.table_widget.setColumnCount(3)  # Three columns: Waypoint, Latitude, Longitude
        self.table_widget.setHorizontalHeaderLabels(["Waypoint", "Latitude", "Longitude"])
 
        # Create scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.table_widget)
 
 
        # Create QLabel for instructions
        self.label = QLabel("Waiting for input...", self)
 
        # Set font properties
        font = QFont("Arial", 12)
        font.setBold(True)
        self.label.setFont(font)
 
        # Set label color and alignment
        self.label.setStyleSheet("color: blue;")
        self.label.setAlignment(Qt.AlignCenter)
 
         # Add label to the main layout
        self.main_layout.addWidget(self.label)
        # Add scroll area to the main layout
        self.main_layout.addWidget(self.scroll_area)
 
        self.setLayout(self.main_layout)
 
    def receive_waypoints(self, source_icao, destination_icao):
        excel_file = "DB_PATHS.xlsx"  # Path to your Excel file
        sheet_name = f"{source_icao}-{destination_icao}"
 
        try:
            # Read the Excel sheet for the given ICAO route
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
 
            if not df.empty:
                # Extract waypoints, latitudes, and longitudes (2nd, 4th, 5th columns)
                waypoints = df.iloc[:, 1].tolist()
                latitudes = df.iloc[:, 3].tolist()
                longitudes = df.iloc[:, 4].tolist()
 
                # Clear previous table data
                self.table_widget.setRowCount(0)
                self.label.setText("")
 
                # Add data to the table
                for row, (waypoint, lat, lon) in enumerate(zip(waypoints, latitudes, longitudes)):
                    self.table_widget.insertRow(row)
                    self.table_widget.setItem(row, 0, QTableWidgetItem(waypoint))
                    self.table_widget.setItem(row, 1, QTableWidgetItem(f"{lat:.6f}"))
                    self.table_widget.setItem(row, 2, QTableWidgetItem(f"{lon:.6f}"))
               
                self.label.setStyleSheet("color: yellow; font-size: 14px;")
               
            else:
                self.label.setText("No data found for this route.")
                self.label.setStyleSheet("color: red; font-size: 14px;")
                self.table_widget.setRowCount(0)
 
 
        except Exception as e:
            self.label.setText(f"Error: {str(e)}")
            self.label.setStyleSheet("color: red; font-size: 14px;")
            self.table_widget.setRowCount(0)
 