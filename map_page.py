import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QSpacerItem, 
                           QSizePolicy, QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os

class MapPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1600, 600)
        self.resize(1800, 750)
        self.zoom_factor = 1.0
        self.current_lat_padding = 8
        self.current_lon_padding = 15
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        # Minimal spacer
        self.layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        )

        # Label for status message
        self.label = QLabel("Waiting for input...", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 18px; color: blue; font-weight: bold;")
        self.layout.addWidget(self.label)

        # Create horizontal layout for map and zoom controls
        map_layout = QHBoxLayout()

        # Create vertical layout for left zoom buttons
        left_zoom_layout = QVBoxLayout()
        right_zoom_layout = QVBoxLayout()
        
        # Create zoom buttons style
        button_style = """
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                padding: 10px;
                width: 40px;
                height: 40px;
                border-radius: 20px;
                background-color: white;
                border: 2px solid #808080;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """
        
        # Create left zoom buttons
        left_zoom_in_btn = QPushButton("+", self)
        left_zoom_out_btn = QPushButton("-", self)
        left_zoom_in_btn.setStyleSheet(button_style)
        left_zoom_out_btn.setStyleSheet(button_style)
        
        # Create right zoom buttons
        right_zoom_in_btn = QPushButton("+", self)
        right_zoom_out_btn = QPushButton("-", self)
        right_zoom_in_btn.setStyleSheet(button_style)
        right_zoom_out_btn.setStyleSheet(button_style)
        
        # Connect all zoom buttons to their functions
        left_zoom_in_btn.clicked.connect(self.zoom_in)
        left_zoom_out_btn.clicked.connect(self.zoom_out)
        right_zoom_in_btn.clicked.connect(self.zoom_in)
        right_zoom_out_btn.clicked.connect(self.zoom_out)
        
        # Add buttons to left zoom layout with spacers
        left_zoom_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        left_zoom_layout.addWidget(left_zoom_in_btn)
        left_zoom_layout.addSpacing(10)
        left_zoom_layout.addWidget(left_zoom_out_btn)
        left_zoom_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Add buttons to right zoom layout with spacers
        right_zoom_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        right_zoom_layout.addWidget(right_zoom_in_btn)
        right_zoom_layout.addSpacing(10)
        right_zoom_layout.addWidget(right_zoom_out_btn)
        right_zoom_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create figure and canvas
        self.fig, self.ax = plt.subplots(figsize=(16, 9))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Add layouts and canvas to map layout
        map_layout.addLayout(left_zoom_layout)
        map_layout.addWidget(self.canvas)
        map_layout.addLayout(right_zoom_layout)
        
        # Add map layout to main layout
        self.layout.addLayout(map_layout)
        
        # Minimize margins
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)
        
        self.setLayout(self.layout)
        
        # Store the current data
        self.current_data = None

    def zoom_in(self):
        if self.current_data is not None:
            self.zoom_factor *= 0.8  # Reduce padding by 20%
            self.update_map()

    def zoom_out(self):
        if self.current_data is not None:
            self.zoom_factor *= 1.2  # Increase padding by 20%
            self.update_map()

    def update_map(self):
        df = self.current_data
        latitudes = df.iloc[:, 3].tolist()
        longitudes = df.iloc[:, 4].tolist()

        # Apply zoom factor to padding
        lat_padding = self.current_lat_padding * self.zoom_factor
        lon_padding = self.current_lon_padding * self.zoom_factor

        min_lat = min(latitudes) - lat_padding
        max_lat = max(latitudes) + lat_padding
        min_lon = min(longitudes) - lon_padding
        max_lon = max(longitudes) + lon_padding

        self.ax.clear()

        m = Basemap(
            projection="merc",
            llcrnrlat=min_lat,
            urcrnrlat=max_lat,
            llcrnrlon=min_lon,
            urcrnrlon=max_lon,
            resolution="i",
            ax=self.ax,
        )

        m.drawcoastlines(linewidth=0.8)
        m.drawcountries(linewidth=0.6)
        m.drawmapboundary(fill_color="azure")
        m.fillcontinents(color="lightgreen", lake_color="azure")
        
        m.drawparallels(range(int(min_lat), int(max_lat), 3), 
                       labels=[1, 0, 0, 0], 
                       fontsize=8)
        m.drawmeridians(range(int(min_lon), int(max_lon), 3), 
                       labels=[0, 0, 0, 1], 
                       fontsize=8)

        x, y = m(longitudes, latitudes)
        m.scatter(x, y, color="red", marker="o", label="Flight Path", s=50)
        m.plot(x, y, color="blue", linewidth=2, linestyle="-", alpha=0.7)

        self.ax.set_title(
            f"Flight Path: {self.current_source_icao} → {self.current_destination_icao}",
            pad=10,
            fontsize=14,
            fontweight='bold'
        )

        self.ax.legend(loc='upper right')
        plt.tight_layout(pad=1.5)
        self.canvas.draw()

    def receive_message(self, source_icao, destination_icao):
        sheet_name = f"{source_icao}-{destination_icao}"
        excel_file = "DB_PATHS.xlsx"

        try:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)

            if not df.empty:
                # Store current data and ICAO codes
                self.current_data = df
                self.current_source_icao = source_icao
                self.current_destination_icao = destination_icao
                
                # Reset zoom factor when loading new data
                self.zoom_factor = 1.0
                
                # Update the map
                self.update_map()

                self.label.setText("Map with flight path generated.")
                self.label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
                self.label.setStyleSheet(
                    "font-size: 20px; color: green; font-weight: bold;"
                )

            else:
                self.label.setText("No data found in the sheet.")
                self.label.setStyleSheet(
                    "font-size: 18px; color: red; font-weight: bold;"
                )

        except Exception as e:
            self.label.setText(f"Error: {str(e)}")
            self.label.setStyleSheet("font-size: 18px; color: red; font-weight: bold;")