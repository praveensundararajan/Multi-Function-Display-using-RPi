from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QPushButton,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class InfoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.current_info_type = "waiting"  # Initially no button is selected
        self.airport_data_received = False  # New variable
        self.init_ui()
        self.update_background()

    def update_background(self):
        # Load the image and scale it to the full window size
        pixmap = QPixmap("images/bg.png")
        scaled_pixmap = pixmap.scaled(
            self.size(), aspectRatioMode=0
        )  # 0 = Qt.IgnoreAspectRatio
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

    def init_ui(self):
        # Main layout for the whole widget
        main_layout = QHBoxLayout(self)

        # Layout for buttons on the left side
        left_buttons_layout = QVBoxLayout()
        self.left_buttons = self.create_buttons()
        for i, button in enumerate(self.left_buttons):
            left_buttons_layout.addWidget(button)
            if (
                i < len(self.left_buttons) - 1
            ):  # Add spacer after each button except the last one
                left_buttons_layout.addItem(
                    QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
                )

        main_layout.addLayout(left_buttons_layout)

        # Layout for the main info content
        self.info_layout = QVBoxLayout()

        # Create a QLabel instance for initial instruction message
        self.label = QLabel("Waiting for input...", self)

        # Set font to Arial, size 14, bold
        font = QFont("Arial", 14)
        font.setBold(True)
        self.label.setFont(font)

        # Set text color to blue
        self.label.setStyleSheet("color: blue;")

        # Set the label text alignment to centered
        self.label.setAlignment(Qt.AlignCenter)

        # Add the initial instruction label to the layout
        self.info_layout.addWidget(self.label)

        # Make sure the layout stretches appropriately
        self.info_layout.setContentsMargins(0, 20, 0, 0)
        self.info_layout.setSpacing(15)  # Increase space between rows

        main_layout.addLayout(self.info_layout)

        # Layout for buttons on the right side
        right_buttons_layout = QVBoxLayout()

        # Layout for buttons on the right side
        self.right_buttons = self.create_buttons()
        for i, button in enumerate(self.right_buttons):
            right_buttons_layout.addWidget(button)
            if (
                i < len(self.right_buttons) - 1
            ):  # Add spacer after each button except the last one
                right_buttons_layout.addItem(
                    QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
                )

        main_layout.addLayout(right_buttons_layout)

        self.setLayout(main_layout)

    def create_buttons(self):
        button_names = [
            "Airport Details",
            "Basic Information",
            """Technical 
Specifications""",
            """Operational 
Information""",
            """Passengers
Capacity""",
            "Aerodynamics",
        ]
        buttons = []
        for name in button_names:
            button = QPushButton(name)
            button.setFixedSize(150, 80)  # Set fixed width to 150 and height to 40
            button.clicked.connect(
                lambda checked, btn_name=name: self.on_button_clicked(btn_name)
            )
            buttons.append(button)
        return buttons

    def on_button_clicked(self, button_name):
        self.current_info_type = button_name
        self.update_display()

    def update_display(self):
        # Clear the existing layout
        for i in reversed(range(self.info_layout.count())):
            item = self.info_layout.itemAt(i)
            if item.widget():
                item.widget().setParent(None)
            elif item.layout():
                self.clear_layout(item.layout())

        if self.current_info_type == "Airport Details":
            if not self.airport_data_received:
                self.label = QLabel("Waiting for input...", self)

                # Set font to Arial, size 14, bold
                font = QFont("Arial", 14)
                font.setBold(True)
                self.label.setFont(font)

                # Set text color to blue
                self.label.setStyleSheet("color: blue;")

                # Set the label text alignment to centered
                self.label.setAlignment(Qt.AlignCenter)

                # Add the initial instruction label to the layout
                self.info_layout.addWidget(self.label)

                # Make sure the layout stretches appropriately
                self.info_layout.setContentsMargins(0, 20, 0, 0)
                self.info_layout.setSpacing(15)  # Increase space between rows
            else:
                self.display_airport_details()

        elif self.current_info_type == "Basic Information":
            self.display_hardcoded_info(
                "<b>Basic Information</b>",
                [
                    "Type: Commercial Airliner",
                    "Manufacturer: Generic Aircraft Corp.",
                    "Typical Capacity: 150-200 passengers",
                    "Wingspan: 35.8 meters",
                    "Length: 40 meters",
                ],
            )

        elif (
            self.current_info_type
            == """Technical 
Specifications"""
        ):
            self.display_hardcoded_info(
                "<b>Technical Specifications</b>",
                [
                    "Engines: 2x Turbofan",
                    "Max Takeoff Weight: 70,000 kg",
                    "Cruise Speed: 850 km/h",
                    "Service Ceiling: 12,000 m",
                    "Range: 5,000 km",
                ],
            )
        elif (
            self.current_info_type
            == """Operational 
Information"""
        ):
            self.display_hardcoded_info(
                "<b>Operational Information</b>",
                [
                    "Typical Cruise Altitude: 10,000 m",
                    "Landing Speed: 250 km/h",
                    "Takeoff Distance: 2,000 m",
                    "Landing Distance: 1,800 m",
                    "Max Operating Altitude: 12,000 m",
                ],
            )

        elif (
            self.current_info_type
            == """Passengers
Capacity"""
        ):
            self.display_hardcoded_info(
                "<b>Passenger Capacity</b>",
                [
                    "Cabin Class: Economy/Business",
                    "Seat Pitch: 31-32 inches (economy)",
                    "Emergency Exits: 8",
                    "Lavatories: 4",
                    "Galley: Front and rear",
                ],
            )
        elif self.current_info_type == "Aerodynamics":
            self.display_hardcoded_info(
                "<b>Aerodynamics</b>",
                [
                    "Wing Type: Swept wing",
                    "Lift Coefficient: 0.5",
                    "Drag Coefficient: 0.03",
                    "Stall Speed: 200 km/h",
                    "Max Operating Speed: 900 km/h",
                ],
            )

    def display_hardcoded_info(self, title, lines):
        """Display hardcoded information in the info_layout."""
        self.clear_layout(self.info_layout)
    
        # Add a stretching spacer at the top to push content down
        self.info_layout.addItem(
        QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    )

        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setStyleSheet("color: blue;")
        title_label.setAlignment(Qt.AlignCenter)
        self.info_layout.addWidget(title_label)

        # Add some space after the title
        self.info_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        )

        for line in lines:
            label = QLabel(line)
            label.setFont(QFont("Arial", 12))
            label.setAlignment(Qt.AlignCenter)
            self.info_layout.addWidget(label)
            
            # Add a small fixed spacer after each line
            self.info_layout.addItem(
                QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
            )

        # Add a stretching spacer at the bottom to push content up
        self.info_layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

    def update_label(
        self,
        source_icao,
        source_apt_name,
        source_lat_long,
        source_elevation,
        source_country,
        source_region,
        destination_icao,
        destination_apt_name,
        destination_lat_long,
        destination_elevation,
        destination_country,
        destination_region,
    ):
        """Update the label with the source and destination in a tabular format."""
        self.airport_data_received = True  # Mark that data is received
        self.current_info_type = "Airport Details"  # Set the current info type.
        # Store data as class variables
        self.source_icao = source_icao
        self.source_apt_name = source_apt_name
        self.source_lat_long = source_lat_long
        self.source_elevation = source_elevation
        self.source_country = source_country
        self.source_region = source_region
        self.destination_icao = destination_icao
        self.destination_apt_name = destination_apt_name
        self.destination_lat_long = destination_lat_long
        self.destination_elevation = destination_elevation
        self.destination_country = destination_country
        self.destination_region = destination_region
        self.update_display()  # Call update_display

    def display_airport_details(self):

        # Clear the initial label after data is received
        self.clear_layout(self.info_layout)

        # Create tabular layout for source and destination data
        table_layout = QVBoxLayout()

        # Add spacer between sections (optional)
        table_layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )  # Space before the table

        # Row 1: Parameters
        row1 = QHBoxLayout()
        param_label = QLabel("<b>Parameters</b>")
        param_label.setFont(QFont("Arial", 14, QFont.Bold))
        param_label.setStyleSheet("color: blue;")
        param_label.setAlignment(Qt.AlignCenter)
        row1.addWidget(param_label)

        source_label = QLabel("<b>Source Airport</b>")
        source_label.setFont(QFont("Arial", 14, QFont.Bold))
        source_label.setStyleSheet("color: blue;")
        source_label.setAlignment(Qt.AlignCenter)
        row1.addWidget(source_label)

        destination_label = QLabel("<b>Destination Airport</b>")
        destination_label.setFont(QFont("Arial", 14, QFont.Bold))
        destination_label.setStyleSheet("color: blue;")
        destination_label.setAlignment(Qt.AlignCenter)
        row1.addWidget(destination_label)

        table_layout.addLayout(row1)

        # Add extra space between rows
        table_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Row 2: ICAO Values
        row2 = QHBoxLayout()

        icao_label = QLabel("<b>ICAO</b>")
        icao_label.setFont(QFont("Arial", 14, QFont.Bold))
        icao_label.setAlignment(Qt.AlignCenter)
        row2.addWidget(icao_label)

        source_icao_label = QLabel(self.source_icao)
        source_icao_label.setFont(QFont("Arial", 14, QFont.Bold))
        source_icao_label.setStyleSheet("color: green;")
        source_icao_label.setAlignment(Qt.AlignCenter)
        row2.addWidget(source_icao_label)

        destination_icao_label = QLabel(self.destination_icao)
        destination_icao_label.setFont(QFont("Arial", 14, QFont.Bold))
        destination_icao_label.setStyleSheet("color: green;")
        destination_icao_label.setAlignment(Qt.AlignCenter)
        row2.addWidget(destination_icao_label)

        table_layout.addLayout(row2)

        # Add extra space between rows
        table_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Row 3: Airport Name
        row3 = QHBoxLayout()

        apt_label = QLabel("<b>Airport Name</b>")
        apt_label.setFont(QFont("Arial", 14, QFont.Bold))
        apt_label.setAlignment(Qt.AlignCenter)
        row3.addWidget(apt_label)

        source_apt_label = QLabel(self.source_apt_name)
        source_apt_label.setFont(QFont("Arial", 14, QFont.Bold))
        source_apt_label.setStyleSheet("color: green;")
        source_apt_label.setAlignment(Qt.AlignCenter)
        row3.addWidget(source_apt_label)

        destination_apt_label = QLabel(self.destination_apt_name)
        destination_apt_label.setFont(QFont("Arial", 14, QFont.Bold))
        destination_apt_label.setStyleSheet("color: green;")
        destination_apt_label.setAlignment(Qt.AlignCenter)
        row3.addWidget(destination_apt_label)

        table_layout.addLayout(row3)

        # Add extra space between rows
        table_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Row 4: Latitude, Longitude
        row4 = QHBoxLayout()

        lat_long_label = QLabel("<b>Latitude, Longitude (deg)</b>")
        lat_long_label.setFont(QFont("Arial", 14, QFont.Bold))
        lat_long_label.setAlignment(Qt.AlignCenter)
        row4.addWidget(lat_long_label)

        source_lat_long_label = QLabel(self.source_lat_long)
        source_lat_long_label.setFont(QFont("Arial", 14, QFont.Bold))
        source_lat_long_label.setStyleSheet("color: green;")
        source_lat_long_label.setAlignment(Qt.AlignCenter)
        row4.addWidget(source_lat_long_label)

        destination_lat_long_label = QLabel(self.destination_lat_long)
        destination_lat_long_label.setFont(QFont("Arial", 14, QFont.Bold))
        destination_lat_long_label.setStyleSheet("color: green;")
        destination_lat_long_label.setAlignment(Qt.AlignCenter)
        row4.addWidget(destination_lat_long_label)

        table_layout.addLayout(row4)

        # Add extra space between rows
        table_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Row 5: Elevation
        row5 = QHBoxLayout()

        elevation_label = QLabel("<b>Elevation (ft)</b>")
        elevation_label.setFont(QFont("Arial", 14, QFont.Bold))
        elevation_label.setAlignment(Qt.AlignCenter)
        row5.addWidget(elevation_label)

        source_elevation_label = QLabel(self.source_elevation)
        source_elevation_label.setFont(QFont("Arial", 14, QFont.Bold))
        source_elevation_label.setStyleSheet("color: green;")
        source_elevation_label.setAlignment(Qt.AlignCenter)
        row5.addWidget(source_elevation_label)

        destination_elevation_label = QLabel(self.destination_elevation)
        destination_elevation_label.setFont(QFont("Arial", 14, QFont.Bold))
        destination_elevation_label.setStyleSheet("color: green;")
        destination_elevation_label.setAlignment(Qt.AlignCenter)
        row5.addWidget(destination_elevation_label)

        table_layout.addLayout(row5)

        # Add extra space between rows
        table_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Row 6: Country
        row6 = QHBoxLayout()

        country_label = QLabel("<b>Country</b>")
        country_label.setFont(QFont("Arial", 14, QFont.Bold))
        country_label.setAlignment(Qt.AlignCenter)
        row6.addWidget(country_label)

        source_country_label = QLabel(self.source_country)
        source_country_label.setFont(QFont("Arial", 14, QFont.Bold))
        source_country_label.setStyleSheet("color: green;")
        source_country_label.setAlignment(Qt.AlignCenter)
        row6.addWidget(source_country_label)

        destination_country_label = QLabel(self.destination_country)
        destination_country_label.setFont(QFont("Arial", 14, QFont.Bold))
        destination_country_label.setStyleSheet("color: green;")
        destination_country_label.setAlignment(Qt.AlignCenter)
        row6.addWidget(destination_country_label)

        table_layout.addLayout(row6)

        # Add extra space between rows
        table_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Row 7: Region
        row7 = QHBoxLayout()

        region_label = QLabel("<b>Region</b>")
        region_label.setFont(QFont("Arial", 14, QFont.Bold))
        region_label.setAlignment(Qt.AlignCenter)
        row7.addWidget(region_label)

        source_region_label = QLabel(self.source_region)
        source_region_label.setFont(QFont("Arial", 14, QFont.Bold))
        source_region_label.setStyleSheet("color: green;")
        source_region_label.setAlignment(Qt.AlignCenter)
        row7.addWidget(source_region_label)

        destination_region_label = QLabel(self.destination_region)
        destination_region_label.setFont(QFont("Arial", 14, QFont.Bold))
        destination_region_label.setStyleSheet("color: green;")
        destination_region_label.setAlignment(Qt.AlignCenter)
        row7.addWidget(destination_region_label)

        table_layout.addLayout(row7)

        # Add extra space between rows
        table_layout.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        self.info_layout.addLayout(table_layout)

    def clear_layout(self, layout):
        """Helper function to clear a layout."""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())
