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
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import time
# For GPIO
import threading
# import RPi.GPIO as GPIO

class SwitchMonitorThread(QThread):
    """Monitors switches and emits a signal when activated."""
    switch_1_activated = pyqtSignal()
    switch_2_activated = pyqtSignal()
    switch_3_activated = pyqtSignal()
    switch_4_activated = pyqtSignal()
    switch_5_activated = pyqtSignal()
    switch_6_activated = pyqtSignal()


    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True
        self.SWITCH_1_PIN = 26 # Replace with your GPIO pin number for button 1
        self.SWITCH_2_PIN = 20  # Replace with your GPIO pin number for button 2
        self.SWITCH_3_PIN = 25  # Replace with your GPIO pin number for button 3
        self.SWITCH_4_PIN = 19  # Replace with your GPIO pin number for button 4
        self.SWITCH_5_PIN = 13 # Replace with your GPIO pin number for button 5
        self.SWITCH_6_PIN = 9  # Replace with your GPIO pin number for button 6
        # self.last_button_1_state = GPIO.HIGH
        # self.last_button_2_state = GPIO.HIGH
        # self.last_button_3_state = GPIO.HIGH
        # self.last_button_4_state = GPIO.HIGH
        # self.last_button_5_state = GPIO.HIGH
        # self.last_button_6_state = GPIO.HIGH
        # Pin configuration
    

    # def run(self):              
    #     """Simulates switch input.

    #     In a real setup, this would read the state of a GPIO pin.
    #     """
        
    #     # GPIO setup
    #     GPIO.setmode(GPIO.BCM)  # Use BCM numbering
    #     GPIO.setup(self.SWITCH_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable pull-up resistor for button 1
    #     GPIO.setup(self.SWITCH_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Enable pull-up resistor for button 2
    #     GPIO.setup(self.SWITCH_3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable pull-up resistor for button 3
    #     GPIO.setup(self.SWITCH_4_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Enable pull-up resistor for button 4
    #     GPIO.setup(self.SWITCH_5_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Enable pull-up resistor for button 5
    #     GPIO.setup(self.SWITCH_6_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Enable pull-up resistor for button 6
    #     while self.running:
    #         button_1_state = GPIO.input(self.SWITCH_1_PIN)
    #         button_2_state = GPIO.input(self.SWITCH_2_PIN)
    #         button_3_state = GPIO.input(self.SWITCH_3_PIN)
    #         button_4_state = GPIO.input(self.SWITCH_4_PIN)
    #         button_5_state = GPIO.input(self.SWITCH_5_PIN)
    #         button_6_state = GPIO.input(self.SWITCH_6_PIN)

            
    #         if button_1_state != self.last_button_1_state:
    #             self.last_button_1_state = button_1_state
    #             if button_1_state == GPIO.LOW:
    #                 self.switch_1_activated.emit()
    #                 time.sleep(0.2)   # Adding debounce delay of 200 ms so that multiple inputs are not considered
    #         if button_2_state != self.last_button_2_state:
    #              self.last_button_2_state = button_2_state
    #              if button_2_state == GPIO.LOW:
    #                 self.switch_2_activated.emit()
    #                 time.sleep(0.2) #Adding debounce delay for 200 ms
    #         if button_3_state != self.last_button_3_state:
    #             self.last_button_3_state = button_3_state
    #             if button_3_state == GPIO.LOW:
    #                  self.switch_3_activated.emit()
    #                  time.sleep(0.2)
    #         if button_4_state != self.last_button_4_state:
    #              self.last_button_4_state = button_4_state
    #              if button_4_state == GPIO.LOW:
    #                 self.switch_4_activated.emit()
    #                 time.sleep(0.2)
    #         if button_5_state != self.last_button_5_state:
    #             self.last_button_5_state = button_5_state
    #             if button_5_state == GPIO.LOW:
    #                 self.switch_5_activated.emit()
    #                 time.sleep(0.2)
    #         if button_6_state != self.last_button_6_state:
    #             self.last_button_6_state = button_6_state
    #             if button_6_state == GPIO.LOW:
    #                  self.switch_6_activated.emit()
    #                  time.sleep(0.2)
    #         time.sleep(0.1)

    # def stop(self):
    #     """Stops the thread."""
    #     self.running = False
    #     GPIO.cleanup()
    #     self.wait()


class InfoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.current_info_type = "Airport Details"  # Initially no button is selected
        self.airport_data_received = False  # New variable
        self.airport_button_enabled = True
        self.basic_info_enabled = False  # For toggling Basic Info
        self.technical_info_enabled = False #For toggling technical info
        self.operational_info_enabled = False #For toggling operational info
        self.passenger_info_enabled = False #For toggling passenger capacity info
        self.aerodynamics_info_enabled = False #For toggling aerodynamics info
        self.source_data = {}
        self.destination_data = {}
        self.button_states = {
            "Airport Details":False,
            "Basic Information":False,
            """Technical 
Specifications""":False,
            """Operational 
Information""":False,
            """Passengers
Capacity""":False,
            "Aerodynamics":False,

        }

        self.init_ui()
        self.update_background()
        # Initialize the "Airport Details" display at the start
        self.update_display()
          # Create and start the switch monitoring thread
        self.switch_thread = SwitchMonitorThread()
        self.switch_thread.switch_1_activated.connect(self.on_switch_1_activated)
        self.switch_thread.switch_2_activated.connect(self.on_switch_2_activated)
        self.switch_thread.switch_3_activated.connect(self.on_switch_3_activated)
        self.switch_thread.switch_4_activated.connect(self.on_switch_4_activated)
        self.switch_thread.switch_5_activated.connect(self.on_switch_5_activated)
        self.switch_thread.switch_6_activated.connect(self.on_switch_6_activated)
        self.switch_thread.start()


    def update_background(self):
         # Set background to white
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.white)  # Set background to white
        self.setPalette(palette)
        self.setAutoFillBackground(True)  # Needed for palette to work
        

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
        self.label = QLabel("", self) # Removed the waiting label

        # Set font to Arial, size 14, bold
        font = QFont("Arial", 14)
        font.setBold(True)
        self.label.setFont(font)

        # Set text color to blue
        self.label.setStyleSheet("color: blue;")

        # Set the label text alignment to centered
        self.label.setAlignment(Qt.AlignCenter)

        # Add the initial instruction label to the layout
        #self.info_layout.addWidget(self.label) # Removed the label so that it doesnt display by default

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
            if name == "Airport Details":
                button.clicked.connect(
                lambda checked, btn_name=name: self.on_airport_button_clicked(btn_name)
            )
            buttons.append(button)
        return buttons
    
    def on_airport_button_clicked(self, button_name):
        if button_name == "Airport Details":
            self.airport_button_enabled = not self.airport_button_enabled
            self.update_airport_button_state()

    def update_airport_button_state(self):
        # Enable or disable the Airport Details button based on the state
        for button in self.left_buttons:
            if button.text() == "Airport Details":
                if self.airport_button_enabled:
                    button.setStyleSheet("background-color: yellow;")
                else:
                    button.setStyleSheet("")  # Revert to default style
        if self.airport_button_enabled:
             self.current_info_type = "Airport Details"
        else:
             self.current_info_type = "waiting"

        self.update_display()

    def update_display(self):
        # Clear the existing layout
        for i in reversed(range(self.info_layout.count())):
            item = self.info_layout.itemAt(i)
            if item.widget():
                item.widget().setParent(None)
            elif item.layout():
                self.clear_layout(item.layout())


        if self.current_info_type == "Airport Details" and self.airport_button_enabled:
            if not self.airport_data_received:
                pass # Do not show initial label
            else:
                self.display_airport_details()

        elif self.current_info_type == "Basic Information" and self.basic_info_enabled:
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
        elif self.current_info_type == """Technical 
Specifications""" and self.technical_info_enabled:
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
        elif self.current_info_type == "Operational Information" and self.operational_info_enabled:
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
        elif self.current_info_type == """Passengers
Capacity""" and self.passenger_info_enabled:
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
        elif self.current_info_type == "Aerodynamics" and self.aerodynamics_info_enabled:
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

    def on_switch_1_activated(self):
        """Called when the switch 1 is activated. Only update when the button state changes"""
        self.airport_button_enabled = True
        self.button_states["Airport Details"]= True
        self.current_info_type ="Airport Details"
        self.update_airport_button_state()

    def on_switch_2_activated(self):
        """Called when the switch 2 is activated. Only update when the button state changes"""
        self.basic_info_enabled = True
        self.button_states["Basic Information"]= True
        self.current_info_type = "Basic Information"
        self.update_display()

    def on_switch_3_activated(self):
        """Called when the switch 3 is activated. Only update when the button state changes"""
        self.technical_info_enabled = True
        self.button_states["""Technical 
Specifications"""] = True
        self.current_info_type = """Technical 
Specifications"""
        self.update_display()

    def on_switch_4_activated(self):
         """Called when the switch 4 is activated. Only update when the button state changes"""
         self.operational_info_enabled = True
         self.button_states["""Operational 
Information"""] = True
         self.current_info_type = "Operational Information"
         self.update_display()

    def on_switch_5_activated(self):
        """Called when the switch 5 is activated. Only update when the button state changes"""
        self.passenger_info_enabled = True
        self.button_states["""Passengers
Capacity"""] = True
        self.current_info_type = """Passengers
Capacity"""
        self.update_display()

    def on_switch_6_activated(self):
        """Called when the switch 6 is activated. Only update when the button state changes"""
        self.aerodynamics_info_enabled = True
        self.button_states["Aerodynamics"] = True
        self.current_info_type = "Aerodynamics"
        self.update_display()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    info_page = InfoPage()
    info_page.show()

    # Simulate receiving data:
    info_page.update_label(
        source_icao="KLAX",
        source_apt_name="Los Angeles International",
        source_lat_long="33.9425° N, 118.4081° W",
        source_elevation="125 ft",
        source_country="USA",
        source_region="California",
        destination_icao="KJFK",
        destination_apt_name="John F. Kennedy International",
        destination_lat_long="40.6413° N, 73.7781° W",
        destination_elevation="13 ft",
        destination_country="USA",
        destination_region="New York",
    )

    sys.exit(app.exec_())
