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
#         self.button_layout = QVBoxLayout()
        
#         self.source_button = QPushButton("Source")
#         self.destination_button = QPushButton("Destination")
        
#         # Reduce button size by setting a fixed size
#         self.source_button.setFixedSize(120, 40)  # width, height
#         self.destination_button.setFixedSize(120, 40)  # width, height
        
#         # Connect buttons to functions
#         self.source_button.clicked.connect(self.show_source_page)
#         self.destination_button.clicked.connect(self.show_destination_page)
        
#         self.button_layout.addWidget(self.source_button)
#         self.button_layout.addWidget(self.destination_button)
#         self.button_layout.addStretch()  # Add stretch to push buttons to the top
        
#         self.main_layout.addLayout(self.button_layout)
        
#         # Main content section
#         self.content_layout = QVBoxLayout()

#         # Header Section
#         self.header_frame = QFrame(self)
#         self.header_frame.setStyleSheet("background-color: #3A81C3; color: white;")
#         self.header_layout = QVBoxLayout(self.header_frame)
        
#         self.date_label = QLabel("FRIDAY APRIL 23")
#         self.date_label.setFont(QFont("Arial", 24, QFont.Bold))
#         self.date_label.setAlignment(Qt.AlignCenter)
        
#         self.temp_label = QLabel("18°C")
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
#         self.weather_info_layout = QGridLayout()

#         self.wind_speed = "15 km/h"
#         self.rain = "30%"
#         self.humidity = "60%"
#         self.visibility = "10 km"

#         self.weather_data = [
#             ("WIND", f"{self.wind_speed}", "images/wind_icon.png"),
#             ("RAIN", f"{self.rain}", "images/rain_icon.png"),
#             ("HUMIDITY", f"{self.humidity}", "images/humidity_icon.png"),
#             ("VISIBILITY", f"{self.visibility}", "images/visibility_icon.png")
#         ]

#         for i, (label, value, icon_path) in enumerate(self.weather_data):
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
#             self.weather_info_layout.addWidget(section_frame, i // 2, i % 2)  # 2x2 grid logic

#         self.content_layout.addLayout(self.weather_info_layout)

#         # Section for Morning, Afternoon, Evening
#         self.parts_of_day = QGridLayout()
        
#         self.sections = [
#             ("MORNING", "22°C", "Light Rain"),
#             ("AFTERNOON", "24°C", "Thunderstorm"),
#             ("EVENING", "19°C", "Partly Cloudy")
#         ]
        
#         for i, (part, temp, desc) in enumerate(self.sections):
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
#             self.parts_of_day.addWidget(section_frame, 0, i)

#         self.content_layout.addLayout(self.parts_of_day)
        
#         # Footer Section - Weekly Forecast
#         self.footer_frame = QFrame(self)
#         self.footer_frame.setStyleSheet("background-color: #D0E5F3; color: black;")
#         self.footer_layout = QGridLayout(self.footer_frame)
        
#         self.week_date = ["24-April", "25-April", "26-April", "27-April","28-April", "29-April", "30-April", "01-May"]
#         self.week_days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
#         self.week_temps = ["21°C", "21°C", "25°C", "26°C", "22°C", "19°C", "18°C"]
        
#         for i, (date, day, temp) in enumerate(zip(self.week_date, self.week_days, self.week_temps)):
#             date_label = QLabel(date)
#             day_label = QLabel(day)
#             temp_label = QLabel(temp)
#             date_label.setFont(QFont("Arial", 12))
#             day_label.setFont(QFont("Arial", 12))
#             temp_label.setFont(QFont("Arial", 12))
#             date_label.setAlignment(Qt.AlignCenter)
#             day_label.setAlignment(Qt.AlignCenter)
#             temp_label.setAlignment(Qt.AlignCenter)
#             self.footer_layout.addWidget(date_label, 0, i)
#             self.footer_layout.addWidget(day_label, 1, i)
#             self.footer_layout.addWidget(temp_label, 2, i)
        
#         self.content_layout.addWidget(self.footer_frame)
#         self.main_layout.addLayout(self.content_layout)  # Add content to the main layout

#         self.setLayout(self.main_layout)

#     def show_source_page(self):
#         # Reset temperature labels to the source values
#         self.temp_label.setText("18°C")
        
#         for i, (label, value, icon_path) in enumerate(self.weather_data):
#             value_label = self.weather_info_layout.itemAtPosition(i // 2, i % 2).widget().layout().itemAt(1).widget()
#             value_label.setText(value)

#         # Reset temperatures for other sections as well
#         for i, (part, temp, desc) in enumerate(self.sections):
#             section_frame = self.parts_of_day.itemAtPosition(0, i).widget()
#             temp_label = section_frame.layout().itemAt(1).widget()
#             temp_label.setText(temp)

#         for i, temp in enumerate(self.week_temps):
#             footer_temp_label = self.footer_layout.itemAtPosition(2, i).widget()
#             footer_temp_label.setText(temp)

#     def show_destination_page(self):
#         # Alter temperature values for the destination page
#         self.temp_label.setText("20°C")  # Example of changed temperature
        
#         # Change temperatures in other sections as well
#         for i, (part, temp, desc) in enumerate(self.sections):
#             section_frame = self.parts_of_day.itemAtPosition(0, i).widget()
#             temp_label = section_frame.layout().itemAt(1).widget()
#             temp_label.setText(str(int(temp.split("°")[0]) + 2) + "°C")  # Increment by 2°C for example

#         # Alter weekly forecast temperatures as well
#         for i, temp in enumerate(self.week_temps):
#             footer_temp_label = self.footer_layout.itemAtPosition(2, i).widget()
#             footer_temp_label.setText(str(int(temp.split("°")[0]) + 2) + "°C")  # Increment by 2°C for example

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = WeatherPage()
#     window.show()
#     sys.exit(app.exec_())


from PyQt5.QtWidgets import (
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
    def __init__(self, source_icao="Source", destination_icao="Destination"):
        super().__init__()
        self.source_icao = source_icao
        self.destination_icao = destination_icao
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather Dashboard")
        self.setGeometry(200, 100, 1000, 700)
        
        self.main_layout = QHBoxLayout(self)  # Use QHBoxLayout to add buttons on the left
        
        # Button Section
        self.button_layout = QVBoxLayout()
        
        self.source_button = QPushButton(self.source_icao)
        self.destination_button = QPushButton(self.destination_icao)
        
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

    def update_icao_codes(self, source_icao, destination_icao):
        """Update the button texts with new ICAO codes"""
        self.source_icao = source_icao
        self.destination_icao = destination_icao
        self.source_button.setText(source_icao)
        self.destination_button.setText(destination_icao)
        
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


