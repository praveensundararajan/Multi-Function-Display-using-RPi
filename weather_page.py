'''from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QGridLayout, QFrame, QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QPixmap

class WeatherPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather Dashboard")
        self.setGeometry(200, 100, 1000, 700)
        
        self.main_layout = QHBoxLayout(self)  # Use QHBoxLayout to add buttons on the left
        
        # Button Section
        self.button_layout = QVBoxLayout()
        
        self.source_button = QPushButton("Source")
        self.destination_button = QPushButton("Destination")
        
        # Reduce button size by setting a fixed size
        self.source_button.setFixedSize(120, 40)  # width, height
        self.destination_button.setFixedSize(120, 40)  # width, height
        
        # Connect buttons to functions
        self.source_button.clicked.connect(self.show_source_page)
        self.destination_button.clicked.connect(self.show_destination_page)
        
        self.button_layout.addWidget(self.source_button)
        self.button_layout.addWidget(self.destination_button)
        self.button_layout.addStretch()  # Add stretch to push buttons to the top
        
        self.main_layout.addLayout(self.button_layout)
        
        # Main content section
        self.content_layout = QVBoxLayout()

        # Header Section
        self.header_frame = QFrame(self)
        self.header_frame.setStyleSheet("background-color: #3A81C3; color: white;")
        self.header_layout = QVBoxLayout(self.header_frame)
        
        self.date_label = QLabel("FRIDAY APRIL 23")
        self.date_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.date_label.setAlignment(Qt.AlignCenter)
        
        self.temp_label = QLabel("18°C")
        self.temp_label.setFont(QFont("Arial", 48))
        self.temp_label.setAlignment(Qt.AlignCenter)
        
        self.weather_desc = QLabel("Partly Cloudy")
        self.weather_desc.setFont(QFont("Arial", 18))
        self.weather_desc.setAlignment(Qt.AlignCenter)

        self.header_layout.addWidget(self.date_label)
        self.header_layout.addWidget(self.temp_label)
        self.header_layout.addWidget(self.weather_desc)
        self.content_layout.addWidget(self.header_frame)
        
        # Current weather section for windspeed, rain, humidity, and visibility
        self.weather_info_layout = QGridLayout()

        self.wind_speed = "15 km/h"
        self.rain = "30%"
        self.humidity = "60%"
        self.visibility = "10 km"

        self.weather_data = [
            ("WIND", f"{self.wind_speed}", "images/wind_icon.png"),
            ("RAIN", f"{self.rain}", "images/rain_icon.png"),
            ("HUMIDITY", f"{self.humidity}", "images/humidity_icon.png"),
            ("VISIBILITY", f"{self.visibility}", "images/visibility_icon.png")
        ]

        for i, (label, value, icon_path) in enumerate(self.weather_data):
            section_frame = QFrame(self)
            section_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
            section_layout = QVBoxLayout(section_frame)
            
            if icon_path:  # Only add icon if path is provided
                icon_label = QLabel()
                icon_pixmap = QPixmap(icon_path)
                icon_label.setPixmap(icon_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                icon_label.setAlignment(Qt.AlignCenter)
                section_layout.addWidget(icon_label)
            
            title_label = QLabel(label)
            title_label.setFont(QFont("Arial", 16))
            title_label.setAlignment(Qt.AlignCenter)
            
            value_label = QLabel(value)
            value_label.setFont(QFont("Arial", 12))
            value_label.setAlignment(Qt.AlignCenter)
            
            section_layout.addWidget(title_label)
            section_layout.addWidget(value_label)
            self.weather_info_layout.addWidget(section_frame, i // 2, i % 2)  # 2x2 grid logic

        self.content_layout.addLayout(self.weather_info_layout)

        # Section for Morning, Afternoon, Evening
        self.parts_of_day = QGridLayout()
        
        self.sections = [
            ("MORNING", "22°C", "Light Rain"),
            ("AFTERNOON", "24°C", "Thunderstorm"),
            ("EVENING", "19°C", "Partly Cloudy")
        ]
        
        for i, (part, temp, desc) in enumerate(self.sections):
            section_frame = QFrame(self)
            section_frame.setStyleSheet("background-color: #4A90E2; color: white;")
            section_layout = QVBoxLayout(section_frame)
            
            part_label = QLabel(part)
            part_label.setFont(QFont("Arial", 18))
            part_label.setAlignment(Qt.AlignCenter)
            
            temp_label = QLabel(temp)
            temp_label.setFont(QFont("Arial", 32))
            temp_label.setAlignment(Qt.AlignCenter)
            
            desc_label = QLabel(desc)
            desc_label.setAlignment(Qt.AlignCenter)
            
            section_layout.addWidget(part_label)
            section_layout.addWidget(temp_label)
            section_layout.addWidget(desc_label)
            self.parts_of_day.addWidget(section_frame, 0, i)

        self.content_layout.addLayout(self.parts_of_day)
        
        # Footer Section - Weekly Forecast
        self.footer_frame = QFrame(self)
        self.footer_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
        self.footer_layout = QGridLayout(self.footer_frame)
        
        self.week_date = ["24-April", "25-April", "26-April", "27-April","28-April", "29-April", "30-April", "01-May"]
        self.week_days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
        self.week_temps = ["21°C", "21°C", "25°C", "26°C", "22°C", "19°C", "18°C"]
        
        for i, (date, day, temp) in enumerate(zip(self.week_date, self.week_days, self.week_temps)):
            date_label = QLabel(date)
            day_label = QLabel(day)
            temp_label = QLabel(temp)
            date_label.setFont(QFont("Arial", 12))
            day_label.setFont(QFont("Arial", 12))
            temp_label.setFont(QFont("Arial", 12))
            date_label.setAlignment(Qt.AlignCenter)
            day_label.setAlignment(Qt.AlignCenter)
            temp_label.setAlignment(Qt.AlignCenter)
            self.footer_layout.addWidget(date_label, 0, i)
            self.footer_layout.addWidget(day_label, 1, i)
            self.footer_layout.addWidget(temp_label, 2, i)
        
        self.content_layout.addWidget(self.footer_frame)
        self.main_layout.addLayout(self.content_layout)  # Add content to the main layout

        self.setLayout(self.main_layout)

    def show_source_page(self):
        # Reset temperature labels to the source values
        self.temp_label.setText("18°C")
        
        for i, (label, value, icon_path) in enumerate(self.weather_data):
            value_label = self.weather_info_layout.itemAtPosition(i // 2, i % 2).widget().layout().itemAt(1).widget()
            value_label.setText(value)

        # Reset temperatures for other sections as well
        for i, (part, temp, desc) in enumerate(self.sections):
            section_frame = self.parts_of_day.itemAtPosition(0, i).widget()
            temp_label = section_frame.layout().itemAt(1).widget()
            temp_label.setText(temp)

        for i, temp in enumerate(self.week_temps):
            footer_temp_label = self.footer_layout.itemAtPosition(2, i).widget()
            footer_temp_label.setText(temp)

    def show_destination_page(self):
        # Alter temperature values for the destination page
        self.temp_label.setText("20°C")  # Example of changed temperature
        
        # Change temperatures in other sections as well
        for i, (part, temp, desc) in enumerate(self.sections):
            section_frame = self.parts_of_day.itemAtPosition(0, i).widget()
            temp_label = section_frame.layout().itemAt(1).widget()
            temp_label.setText(str(int(temp.split("°")[0]) + 2) + "°C")  # Increment by 2°C for example

        # Alter weekly forecast temperatures as well
        for i, temp in enumerate(self.week_temps):
            footer_temp_label = self.footer_layout.itemAtPosition(2, i).widget()
            footer_temp_label.setText(str(int(temp.split("°")[0]) + 2) + "°C")  # Increment by 2°C for example

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherPage()
    window.show()
    sys.exit(app.exec_())

'''
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QLabel, QGridLayout, QFrame, QPushButton, QHBoxLayout
# )
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
# import sys
# from PyQt5.QtGui import QPixmap

# class WeatherPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("Weather Dashboard")
#         self.setGeometry(200, 100, 1000, 700)

#         self.main_layout = QHBoxLayout(self)  # Use QHBoxLayout to add buttons on the left
        
#         # Button Section
#         button_layout = QVBoxLayout()
        
#         source_button = QPushButton("Source")
#         destination_button = QPushButton("Destination")
        
#         # Reduce button size by setting a fixed size
#         source_button.setFixedSize(120, 40)  # width, height
#         destination_button.setFixedSize(120, 40)  # width, height
        
#         button_layout.addWidget(source_button)
#         button_layout.addWidget(destination_button)
#         button_layout.addStretch()  # Add stretch to push buttons to the top
        
#         self.main_layout.addLayout(button_layout)
        
#         # Main content section (initially with source page values)
#         self.content_layout = QVBoxLayout()

#         # Header Section
#         self.header_frame = QFrame(self)
#         self.header_frame.setStyleSheet("background-color: #3A81C3; color: white;")
#         self.header_layout = QVBoxLayout(self.header_frame)
        
#         self.date_label = QLabel("FRIDAY APRIL 23")
#         self.date_label.setFont(QFont("Arial", 24, QFont.Bold))
#         self.date_label.setAlignment(Qt.AlignCenter)
        
#         self.temp_label = QLabel("18°C")  # Default temperature value
#         self.temp_label.setFont(QFont("Arial", 48))
#         self.temp_label.setAlignment(Qt.AlignCenter)
        
#         self.weather_desc = QLabel("Partly Cloudy")
#         self.weather_desc.setFont(QFont("Arial", 18))
#         self.weather_desc.setAlignment(Qt.AlignCenter)

#         self.header_layout.addWidget(self.date_label)
#         self.header_layout.addWidget(self.temp_label)
#         self.header_layout.addWidget(self.weather_desc)
#         self.content_layout.addWidget(self.header_frame)
        
#         # Current weather section for windspeed, rain, humidity, and visibility
#         weather_info_layout = QGridLayout()

#         windspeed = "15 km/h"
#         rain = "30%"
#         humidity = "60%"
#         visibility = "10 km"

#         weather_data = [
#             ("WIND", f"{windspeed}", "images/wind_icon.png"),
#             ("RAIN", f"{rain}", "images/rain_icon.png"),
#             ("HUMIDITY", f"{humidity}", "images/humidity_icon.png"),
#             ("VISIBILITY", f"{visibility}", "images/visibility_icon.png")
#         ]

#         for i, (label, value, icon_path) in enumerate(weather_data):
#             section_frame = QFrame(self)
#             section_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
#             section_layout = QVBoxLayout(section_frame)
            
#             if icon_path:  # Only add icon if path is provided
#                 icon_label = QLabel()
#                 icon_pixmap = QPixmap(icon_path)
#                 icon_label.setPixmap(icon_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
#                 icon_label.setAlignment(Qt.AlignCenter)
#                 section_layout.addWidget(icon_label)
            
#             title_label = QLabel(label)
#             title_label.setFont(QFont("Arial", 16))
#             title_label.setAlignment(Qt.AlignCenter)
            
#             value_label = QLabel(value)
#             value_label.setFont(QFont("Arial", 12))
#             value_label.setAlignment(Qt.AlignCenter)
            
#             section_layout.addWidget(title_label)
#             section_layout.addWidget(value_label)
#             weather_info_layout.addWidget(section_frame, i // 2, i % 2)  # 2x2 grid logic

#         self.content_layout.addLayout(weather_info_layout)

#         # Section for Morning, Afternoon, Evening
#         parts_of_day = QGridLayout()
        
#         sections = [
#             ("MORNING", "22°C", "Light Rain"),
#             ("AFTERNOON", "24°C", "Thunderstorm"),
#             ("EVENING", "19°C", "Partly Cloudy")
#         ]
        
#         for i, (part, temp, desc) in enumerate(sections):
#             section_frame = QFrame(self)
#             section_frame.setStyleSheet("background-color: #4A90E2; color: white;")
#             section_layout = QVBoxLayout(section_frame)
            
#             part_label = QLabel(part)
#             part_label.setFont(QFont("Arial", 18))
#             part_label.setAlignment(Qt.AlignCenter)
            
#             temp_label = QLabel(temp)
#             temp_label.setFont(QFont("Arial", 32))
#             temp_label.setAlignment(Qt.AlignCenter)
            
#             desc_label = QLabel(desc)
#             desc_label.setAlignment(Qt.AlignCenter)
            
#             section_layout.addWidget(part_label)
#             section_layout.addWidget(temp_label)
#             section_layout.addWidget(desc_label)
#             parts_of_day.addWidget(section_frame, 0, i)

#         self.content_layout.addLayout(parts_of_day)
        
#         # Footer Section - Weekly Forecast
#         footer_frame = QFrame(self)
#         footer_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
#         footer_layout = QGridLayout(footer_frame)
        
#         week_date = ["24-April", "25-April", "26-April", "27-April","28-April", "29-April", "30-April", "01-May"]
#         week_days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
#         week_temps = ["21°C", "21°C", "25°C", "26°C", "22°C", "19°C", "18°C"]
        
#         for i, (date, day, temp) in enumerate(zip(week_date, week_days, week_temps)):
#             date_label = QLabel(date)
#             day_label = QLabel(day)
#             temp_label = QLabel(temp)
#             date_label.setFont(QFont("Arial", 12))
#             day_label.setFont(QFont("Arial", 12))
#             temp_label.setFont(QFont("Arial", 12))
#             date_label.setAlignment(Qt.AlignCenter)
#             day_label.setAlignment(Qt.AlignCenter)
#             temp_label.setAlignment(Qt.AlignCenter)
#             footer_layout.addWidget(date_label, 0, i)
#             footer_layout.addWidget(day_label, 1, i)
#             footer_layout.addWidget(temp_label, 2, i)
        
#         self.content_layout.addWidget(footer_frame)
#         self.main_layout.addLayout(self.content_layout)  # Add content to the main layout

#         self.setLayout(self.main_layout)

#         # Connect buttons to their respective functionality
#         source_button.clicked.connect(self.show_source_page)
#         destination_button.clicked.connect(self.show_destination_page)

#     def show_source_page(self):
#         """Display the original weather page (with source temperatures)."""
#         self.temp_label.setText("18°C")  # Reset to the original temperature

#     def show_destination_page(self):
#         """Display the altered weather page (with destination temperatures)."""
#         self.temp_label.setText("22°C")  # Altered temperature for destination page

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = WeatherPage()
#     window.show()
#     sys.exit(app.exec_())


# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QLabel, QGridLayout, QFrame, QPushButton, QHBoxLayout
# )
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
# import sys
# from PyQt5.QtGui import QPixmap

# class WeatherPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("Weather Dashboard")
#         self.setGeometry(200, 100, 1000, 700)
        
#         main_layout = QHBoxLayout(self)  # Use QHBoxLayout to add buttons on the left
        
#         # Button Section
#         button_layout = QVBoxLayout()
        
#         source_button = QPushButton("Source")
#         destination_button = QPushButton("Destination")
        
#         # Reduce button size by setting a fixed size
#         source_button.setFixedSize(120, 40)  # width, height
#         destination_button.setFixedSize(120, 40)  # width, height
        
#         button_layout.addWidget(source_button)
#         button_layout.addWidget(destination_button)
#         button_layout.addStretch()  # Add stretch to push buttons to the top
        
#         main_layout.addLayout(button_layout)
        
#         # Main content section
#         content_layout = QVBoxLayout()

#         # Header Section
#         header_frame = QFrame(self)
#         header_frame.setStyleSheet("background-color: #3A81C3; color: white;")
#         header_layout = QVBoxLayout(header_frame)
        
#         date_label = QLabel("FRIDAY APRIL 23")
#         date_label.setFont(QFont("Arial", 24, QFont.Bold))
#         date_label.setAlignment(Qt.AlignCenter)
        
#         temp_label = QLabel("18°C")
#         temp_label.setFont(QFont("Arial", 48))
#         temp_label.setAlignment(Qt.AlignCenter)
        
#         weather_desc = QLabel("Partly Cloudy")
#         weather_desc.setFont(QFont("Arial", 18))
#         weather_desc.setAlignment(Qt.AlignCenter)

#         header_layout.addWidget(date_label)
#         header_layout.addWidget(temp_label)
#         header_layout.addWidget(weather_desc)
#         content_layout.addWidget(header_frame)
        
#         # Current weather section for windspeed, rain, humidity, and visibility
#         weather_info_layout = QGridLayout()

#         windspeed = "15 km/h"
#         rain = "30%"
#         humidity = "60%"
#         visibility = "10 km"

#         weather_data = [
#             ("WIND", f"{windspeed}", "images/wind_icon.png"),
#             ("RAIN", f"{rain}", "images/rain_icon.png"),
#             ("HUMIDITY", f"{humidity}", "images/humidity_icon.png"),
#             ("VISIBILITY", f"{visibility}", "images/visibility_icon.png")
#         ]

#         for i, (label, value, icon_path) in enumerate(weather_data):
#             section_frame = QFrame(self)
#             section_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
#             section_layout = QVBoxLayout(section_frame)
            
#             if icon_path:  # Only add icon if path is provided
#                 icon_label = QLabel()
#                 icon_pixmap = QPixmap(icon_path)
#                 icon_label.setPixmap(icon_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
#                 icon_label.setAlignment(Qt.AlignCenter)
#                 section_layout.addWidget(icon_label)
            
#             title_label = QLabel(label)
#             title_label.setFont(QFont("Arial", 16))
#             title_label.setAlignment(Qt.AlignCenter)
            
#             value_label = QLabel(value)
#             value_label.setFont(QFont("Arial", 12))
#             value_label.setAlignment(Qt.AlignCenter)
            
#             section_layout.addWidget(title_label)
#             section_layout.addWidget(value_label)
#             weather_info_layout.addWidget(section_frame, i // 2, i % 2)  # 2x2 grid logic

#         content_layout.addLayout(weather_info_layout)

#         # Section for Morning, Afternoon, Evening
#         parts_of_day = QGridLayout()
        
#         sections = [
#             ("MORNING", "22°C", "Light Rain"),
#             ("AFTERNOON", "24°C", "Thunderstorm"),
#             ("EVENING", "19°C", "Partly Cloudy")
#         ]
        
#         for i, (part, temp, desc) in enumerate(sections):
#             section_frame = QFrame(self)
#             section_frame.setStyleSheet("background-color: #4A90E2; color: white;")
#             section_layout = QVBoxLayout(section_frame)
            
#             part_label = QLabel(part)
#             part_label.setFont(QFont("Arial", 18))
#             part_label.setAlignment(Qt.AlignCenter)
            
#             temp_label = QLabel(temp)
#             temp_label.setFont(QFont("Arial", 32))
#             temp_label.setAlignment(Qt.AlignCenter)
            
#             desc_label = QLabel(desc)
#             desc_label.setAlignment(Qt.AlignCenter)
            
#             section_layout.addWidget(part_label)
#             section_layout.addWidget(temp_label)
#             section_layout.addWidget(desc_label)
#             parts_of_day.addWidget(section_frame, 0, i)

#         content_layout.addLayout(parts_of_day)
        
#         # Footer Section - Weekly Forecast
#         footer_frame = QFrame(self)
#         footer_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
#         footer_layout = QGridLayout(footer_frame)
        
#         week_date = ["24-April", "25-April", "26-April", "27-April","28-April", "29-April", "30-April", "01-May"]
#         week_days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
#         week_temps = ["21°C", "21°C", "25°C", "26°C", "22°C", "19°C", "18°C"]
        
#         for i, (date, day, temp) in enumerate(zip(week_date, week_days, week_temps)):
#             date_label = QLabel(date)
#             day_label = QLabel(day)
#             temp_label = QLabel(temp)
#             date_label.setFont(QFont("Arial", 12))
#             day_label.setFont(QFont("Arial", 12))
#             temp_label.setFont(QFont("Arial", 12))
#             date_label.setAlignment(Qt.AlignCenter)
#             day_label.setAlignment(Qt.AlignCenter)
#             temp_label.setAlignment(Qt.AlignCenter)
#             footer_layout.addWidget(date_label, 0, i)
#             footer_layout.addWidget(day_label, 1, i)
#             footer_layout.addWidget(temp_label, 2, i)
        
#         content_layout.addWidget(footer_frame)
#         main_layout.addLayout(content_layout)  # Add content to the main layout

#         self.setLayout(main_layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = WeatherPage()
#     window.show()
#     sys.exit(app.exec_())



from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QSpacerItem, 
                           QSizePolicy, QPushButton, QHBoxLayout, QFrame, QGridLayout
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import sys
import time
#For GPIO
import threading
import RPi.GPIO as GPIO

class SwitchMonitorThread(QThread):
    """Monitors switches and emits a signal when activated."""
    switch_source_activated = pyqtSignal()
    switch_destination_activated = pyqtSignal()


    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True
        self.SWITCH_SOURCE_PIN = 26
        self.SWITCH_DESTINATION_PIN = 20
        self.last_button_source_state = GPIO.HIGH
        self.last_button_destination_state = GPIO.HIGH

        # Pin configuration
    

    def run(self):              
        """Simulates switch input.

        In a real setup, this would read the state of a GPIO pin.
        """
        
        # GPIO setup
        GPIO.setmode(GPIO.BCM)  # Use BCM numbering
        GPIO.setup(self.SWITCH_SOURCE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable pull-up resistor for source button
        GPIO.setup(self.SWITCH_DESTINATION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Enable pull-up resistor for destination button

        while self.running:
            button_source_state = GPIO.input(self.SWITCH_SOURCE_PIN)
            button_destination_state = GPIO.input(self.SWITCH_DESTINATION_PIN)
            
            if button_source_state != self.last_button_source_state:
                self.last_button_source_state = button_source_state
                if button_source_state == GPIO.LOW:
                     self.switch_source_activated.emit()
                     time.sleep(0.2)  #Adding debounce delay for 200 ms
            if button_destination_state != self.last_button_destination_state:
                 self.last_button_destination_state = button_destination_state
                 if button_destination_state == GPIO.LOW:
                     self.switch_destination_activated.emit()
                     time.sleep(0.2)  #Adding debounce delay for 200 ms
            time.sleep(0.1)

    def stop(self):
        """Stops the thread."""
        self.running = False
        GPIO.cleanup()
        self.wait()



class WeatherPage(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_button = None #Keeps track of the last selected button.
        self.init_ui()
        
         # Create and start the switch monitoring thread
        self.switch_thread = SwitchMonitorThread()
        self.switch_thread.switch_source_activated.connect(self.on_source_button_activated)
        self.switch_thread.switch_destination_activated.connect(self.on_destination_button_activated)
        self.switch_thread.start()
        self.on_source_button_activated() # Initial selection as "source" and apply style

    def init_ui(self):
        self.setWindowTitle("Weather Dashboard")
        self.setGeometry(200, 100, 1000, 700)
        
        self.main_layout = QHBoxLayout(self)  # Use QHBoxLayout to add buttons on the left
        
        # Button Section
        self.button_layout = QVBoxLayout()
        
        self.source_button = QPushButton("Source")
        self.destination_button = QPushButton("Destination")
        
        # Reduce button size by setting a fixed size
        self.source_button.setFixedSize(120, 40)  # width, height
        self.destination_button.setFixedSize(120, 40)  # width, height
        
        # Remove button connection
        #self.source_button.clicked.connect(self.show_source_page)
        #self.destination_button.clicked.connect(self.show_destination_page)
        
        self.button_layout.addWidget(self.source_button)
        self.button_layout.addWidget(self.destination_button)
        self.button_layout.addStretch()  # Add stretch to push buttons to the top
        
        self.main_layout.addLayout(self.button_layout)
        
        # Main content section
        self.content_layout = QVBoxLayout()

        # Header Section
        self.header_frame = QFrame(self)
        self.header_frame.setStyleSheet("background-color: #3A81C3; color: white;")
        self.header_layout = QVBoxLayout(self.header_frame)
        
        self.date_label = QLabel("FRIDAY APRIL 23")
        self.date_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.date_label.setAlignment(Qt.AlignCenter)
        
        self.temp_label = QLabel("18°C")
        self.temp_label.setFont(QFont("Arial", 48))
        self.temp_label.setAlignment(Qt.AlignCenter)
        
        self.weather_desc = QLabel("Partly Cloudy")
        self.weather_desc.setFont(QFont("Arial", 18))
        self.weather_desc.setAlignment(Qt.AlignCenter)

        self.header_layout.addWidget(self.date_label)
        self.header_layout.addWidget(self.temp_label)
        self.header_layout.addWidget(self.weather_desc)
        self.content_layout.addWidget(self.header_frame)
        
        # Current weather section for windspeed, rain, humidity, and visibility
        self.weather_info_layout = QGridLayout()

        self.wind_speed = "15 km/h"
        self.rain = "30%"
        self.humidity = "60%"
        self.visibility = "10 km"

        self.weather_data = [
            ("WIND", f"{self.wind_speed}", "images/wind_icon.png"),
            ("RAIN", f"{self.rain}", "images/rain_icon.png"),
            ("HUMIDITY", f"{self.humidity}", "images/humidity_icon.png"),
            ("VISIBILITY", f"{self.visibility}", "images/visibility_icon.png")
        ]

        for i, (label, value, icon_path) in enumerate(self.weather_data):
            section_frame = QFrame(self)
            section_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
            section_layout = QVBoxLayout(section_frame)
            
            if icon_path:  # Only add icon if path is provided
                icon_label = QLabel()
                icon_pixmap = QPixmap(icon_path)
                icon_label.setPixmap(icon_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                icon_label.setAlignment(Qt.AlignCenter)
                section_layout.addWidget(icon_label)
            
            title_label = QLabel(label)
            title_label.setFont(QFont("Arial", 16))
            title_label.setAlignment(Qt.AlignCenter)
            
            value_label = QLabel(value)
            value_label.setFont(QFont("Arial", 12))
            value_label.setAlignment(Qt.AlignCenter)
            
            section_layout.addWidget(title_label)
            section_layout.addWidget(value_label)
            self.weather_info_layout.addWidget(section_frame, i // 2, i % 2)  # 2x2 grid logic

        self.content_layout.addLayout(self.weather_info_layout)

        # Section for Morning, Afternoon, Evening
        self.parts_of_day = QGridLayout()
        
        self.sections = [
            ("MORNING", "22°C", "Light Rain"),
            ("AFTERNOON", "24°C", "Thunderstorm"),
            ("EVENING", "19°C", "Partly Cloudy")
        ]
        
        for i, (part, temp, desc) in enumerate(self.sections):
            section_frame = QFrame(self)
            section_frame.setStyleSheet("background-color: #4A90E2; color: white;")
            section_layout = QVBoxLayout(section_frame)
            
            part_label = QLabel(part)
            part_label.setFont(QFont("Arial", 18))
            part_label.setAlignment(Qt.AlignCenter)
            
            temp_label = QLabel(temp)
            temp_label.setFont(QFont("Arial", 32))
            temp_label.setAlignment(Qt.AlignCenter)
            
            desc_label = QLabel(desc)
            desc_label.setAlignment(Qt.AlignCenter)
            
            section_layout.addWidget(part_label)
            section_layout.addWidget(temp_label)
            section_layout.addWidget(desc_label)
            self.parts_of_day.addWidget(section_frame, 0, i)

        self.content_layout.addLayout(self.parts_of_day)
        
        # Footer Section - Weekly Forecast
        self.footer_frame = QFrame(self)
        self.footer_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
        self.footer_layout = QGridLayout(self.footer_frame)
        
        self.week_date = ["24-April", "25-April", "26-April", "27-April","28-April", "29-April", "30-April", "01-May"]
        self.week_days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
        self.week_temps = ["21°C", "21°C", "25°C", "26°C", "22°C", "19°C", "18°C"]
        
        for i, (date, day, temp) in enumerate(zip(self.week_date, self.week_days, self.week_temps)):
            date_label = QLabel(date)
            day_label = QLabel(day)
            temp_label = QLabel(temp)
            date_label.setFont(QFont("Arial", 12))
            day_label.setFont(QFont("Arial", 12))
            temp_label.setFont(QFont("Arial", 12))
            date_label.setAlignment(Qt.AlignCenter)
            day_label.setAlignment(Qt.AlignCenter)
            temp_label.setAlignment(Qt.AlignCenter)
            self.footer_layout.addWidget(date_label, 0, i)
            self.footer_layout.addWidget(day_label, 1, i)
            self.footer_layout.addWidget(temp_label, 2, i)
        
        self.content_layout.addWidget(self.footer_frame)
        self.main_layout.addLayout(self.content_layout)  # Add content to the main layout

        self.setLayout(self.main_layout)
    
    def on_source_button_activated(self):
        self.selected_button = self.source_button # Assigning the selected button
        self.update_button_style() # Apply highlight for the source button
        self.show_source_page() # Calling the corresponding page to display
   
    def on_destination_button_activated(self):
         self.selected_button = self.destination_button  # Assigning the selected button
         self.update_button_style() # Apply highlight for the source button
         self.show_destination_page() #Calling the corresponding page to display


    def update_button_style(self):
        """Updates the style of the buttons to indicate the selected one."""
        # Reset style for both buttons
        self.source_button.setStyleSheet("")
        self.destination_button.setStyleSheet("")
        
        # Apply yellow background to selected button
        if self.selected_button:  # Check if selected_button is not None
             self.selected_button.setStyleSheet("background-color: black; color: white")
        
    def show_source_page(self):
        # Reset temperature labels to the source values
        self.temp_label.setText("18°C")
        
        for i, (label, value, icon_path) in enumerate(self.weather_data):
            value_label = self.weather_info_layout.itemAtPosition(i // 2, i % 2).widget().layout().itemAt(1).widget()
            value_label.setText(value)

        # Reset temperatures for other sections as well
        for i, (part, temp, desc) in enumerate(self.sections):
            section_frame = self.parts_of_day.itemAtPosition(0, i).widget()
            temp_label = section_frame.layout().itemAt(1).widget()
            temp_label.setText(temp)

        for i, temp in enumerate(self.week_temps):
            footer_temp_label = self.footer_layout.itemAtPosition(2, i).widget()
            footer_temp_label.setText(temp)
            
      

    def show_destination_page(self):
        # Alter temperature values for the destination page
        self.temp_label.setText("20°C")  # Example of changed temperature
        
        # Change temperatures in other sections as well
        for i, (part, temp, desc) in enumerate(self.sections):
            section_frame = self.parts_of_day.itemAtPosition(0, i).widget()
            temp_label = section_frame.layout().itemAt(1).widget()
            temp_label.setText(str(int(temp.split("°")[0]) + 2) + "°C")  # Increment by 2°C for example

        # Alter weekly forecast temperatures as well
        for i, temp in enumerate(self.week_temps):
            footer_temp_label = self.footer_layout.itemAtPosition(2, i).widget()
            footer_temp_label.setText(str(int(temp.split("°")[0]) + 2) + "°C")  # Increment by 2°C for example

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherPage()
    window.show()
    sys.exit(app.exec_())




