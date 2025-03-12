# from PyQt5.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QHBoxLayout,
#     QLabel,
#     QLineEdit,
#     QPushButton,
#     QGridLayout,
#     QSpacerItem,
#     QSizePolicy,
#     QFrame,
#     QApplication,
# )
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt, QSize
# import pandas as pd
# import sys
# from info_page import InfoPage
# from map_page import MapPage
# from waypoints_page import WaypointsPage
# from PyQt5.QtGui import QPalette, QBrush, QPixmap
# from PyQt5.QtWidgets import QWidget


# class CustomLineEdit(QLineEdit):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setStyleSheet(
#             """
#             QLineEdit {
#                 background-color: white;
#                 color: blue;
#                 border: 1px solid blue;
#                 padding: 5px;
#                 selection-background-color: blue;
#                 selection-color: white;
#             }
#             QLineEdit:focus {
#                 border: 2px solid blue;
#             }
#             """
#         )

#     def focusInEvent(self, event):
#         super().focusInEvent(event)
#         if hasattr(self.parent(), "show_virtual_keyboard"):
#             self.parent().show_virtual_keyboard(self)


# class InputPage(QWidget):
#     def __init__(self, info_page, map_page, waypoints_page):
#         super().__init__()
#         self.info_page = info_page  # Store reference to InfoPage instance
#         self.map_page = map_page
#         self.waypoints_page = waypoints_page
#         self.excel_file = "database.xlsx"  # Update with your actual Excel file path
#         self.source_icao = None
#         self.destination_icao = None
#         self.source_lat_long = None
#         self.destination_lat_long = None
#         self.source_elevation = None
#         self.destination_elevation = None
#         self.source_country = None
#         self.destination_country = None
#         self.source_region = None
#         self.destination_region = None
#         self.init_ui()
#         self.setAutoFillBackground(True)  # Enable background filling

#         # Set the initial background

#         self.update_background()

#     def update_background(self):
#         # Load the image and scale it to the full window size
#         pixmap = QPixmap("images/bng.JPG")
#         scaled_pixmap = pixmap.scaled(
#             self.size(), aspectRatioMode=0
#         )  # 0 = Qt.IgnoreAspectRatio
#         palette = QPalette()
#         palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
#         self.setPalette(palette)

#     def resizeEvent(self, event):
#         # Update the background image size on window resize
#         self.update_background()
#         super().resizeEvent(event)

#     def init_ui(self):
#         self.setWindowTitle("Input Page with Virtual Keyboard")
#         self.setMinimumSize(800, 600)

#         # Layout setup
#         outer_layout = QHBoxLayout(self)
#         outer_layout.setContentsMargins(0, 0, 0, 0)
#         outer_layout.setSpacing(0)

#         # Left-side layout for main content
#         left_layout = QVBoxLayout()
#         left_layout.setContentsMargins(20, 20, 20, 20)
#         left_layout.setSpacing(30)
#         self.main_layout = left_layout

#         # Add main content to left layout
#         self.source_label = QLabel("")  # Label to display search result
#         self.source_label.setFont(QFont("Arial", 14))
#         self.source_label.setAlignment(Qt.AlignCenter)

#         source_section = self.create_input_section("Source", "blue")
#         left_layout.addLayout(source_section)
#         left_layout.addWidget(self.source_label)

#         self.destination_label = QLabel("")  # Label to display search result
#         self.destination_label.setFont(QFont("Arial", 14))
#         self.destination_label.setAlignment(Qt.AlignCenter)

#         destination_section = self.create_input_section("Destination", "blue")
#         left_layout.addLayout(destination_section)
#         left_layout.addWidget(self.destination_label)

#         left_layout.addSpacerItem(
#             QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
#         )

#         self.keyboard_frame = QFrame()
#         self.keyboard_frame.setLayout(QVBoxLayout())
#         left_layout.addWidget(self.keyboard_frame)

#         self.keyboard_layout = QGridLayout()
#         self.keyboard_layout.setSpacing(10)
#         self.keyboard_frame.layout().addLayout(self.keyboard_layout)
#         self.create_virtual_keyboard()
#         self.keyboard_frame.hide()

#         # Add left and right layouts to the outer layout
#         outer_layout.addLayout(left_layout, 2)  # Left side = 60%
#         outer_layout.addStretch(3)  # Right side = 40% empty space

#     def create_input_section(self, title, text_color):
#         section_layout = QVBoxLayout()

#         label = QLabel(title)
#         label.setFont(QFont("Arial", 16, QFont.Bold))
#         label.setStyleSheet(f"color: {text_color};")
#         label.setAlignment(Qt.AlignCenter)
#         section_layout.addWidget(label)

#         text_box = CustomLineEdit(self)
#         text_box.setFont(QFont("Arial", 14))
#         text_box.setMinimumHeight(40)
#         section_layout.addWidget(text_box)

#         submit_button = QPushButton("Submit")
#         submit_button.setFont(QFont("Arial", 14))
#         submit_button.setStyleSheet(
#             "background-color: #00008b; color: white; border: 1px solid #00008b; padding: 5px;"
#         )
#         submit_button.setMinimumHeight(40)
#         submit_button.clicked.connect(lambda: self.on_submit(title, text_box))
#         section_layout.addWidget(submit_button)

#         if title == "Source":
#             self.source_textbox = text_box  # Keep reference to source text box

#         return section_layout

#     def create_virtual_keyboard(self):
#         keyboard_layout = [
#             ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
#             ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
#             ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
#             ["Z", "X", "C", "V", "B", "N", "M"],
#             ["Space", "Backspace", "Clear"],
#         ]

#         for row_idx, row in enumerate(keyboard_layout):
#             start_col = (10 - len(row)) // 2 if row_idx > 0 else 0
#             for col_idx, key in enumerate(row):
#                 button = QPushButton(key)
#                 button.setFont(QFont("Arial", 14, QFont.Bold))
#                 button.setMinimumSize(
#                     QSize(60, 60)
#                     if key not in ["Space", "Backspace", "Clear"]
#                     else QSize(120, 60)
#                 )
#                 button.setStyleSheet(
#                     """
#                     QPushButton {
#                         background-color: white;
#                         color: blue;
#                         border: 2px solid blue;
#                         border-radius: 5px;
#                         padding: 5px;
#                     }
#                     QPushButton:pressed {
#                         background-color: #00008b;
#                         color: white;
#                     }
#                     """
#                 )
#                 button.clicked.connect(lambda _, k=key: self.on_key_click(k))
#                 self.keyboard_layout.addWidget(button, row_idx, start_col + col_idx)

#     def on_key_click(self, key):
#         if not hasattr(self, "current_textbox") or self.current_textbox is None:
#             return

#         if key == "Space":
#             self.current_textbox.insert(" ")
#         elif key == "Clear":
#             self.current_textbox.clear()
#         elif key == "Backspace":
#             self.current_textbox.backspace()
#         else:
#             self.current_textbox.insert(key)

#         self.current_textbox.setFocus()

#     def show_virtual_keyboard(self, text_box):
#         self.current_textbox = text_box
#         self.keyboard_frame.show()

#     def on_submit(self, title, text_box):
#         input_text = text_box.text()
#         if title == "Source":
#             self.source = input_text
#             self.search_in_excel(self.source, "s")
#         if title == "Destination":
#             self.destination = input_text
#             self.search_in_excel(self.destination, "d")

#     def search_in_excel(self, data, mode):
#         """Search for source and destination in Excel file."""
#         try:
#             df = pd.read_excel(self.excel_file)
#             icao = df[df.iloc[:, 1] == data]  # B Column

#             if mode == "s":
#                 if not icao.empty:
#                     self.source_label.setText("Source found")
#                     self.source_label.setStyleSheet("color: green;")
#                     self.source_icao = data
#                     self.source_apt_name = icao.iloc[
#                         0, 3
#                     ]  ## Get the name of the airport from Dth column of the row where the ICAO code is found
#                     lat = icao.iloc[0, 4]
#                     long = icao.iloc[0, 5]
#                     self.source_lat_long = f"({lat},{long})"
#                     self.source_elevation = str(icao.iloc[0, 6])
#                     self.source_country = icao.iloc[0, 8]
#                     self.source_region = icao.iloc[0, 9]
#                 else:
#                     self.source_label.setText("Source not found")
#                     self.source_label.setStyleSheet("color: red;")

#             elif mode == "d":
#                 if not icao.empty:
#                     self.destination_label.setText("Destination found")
#                     self.destination_label.setStyleSheet("color: green;")
#                     self.destination_icao = data
#                     self.destination_apt_name = icao.iloc[
#                         0, 3
#                     ]  ## Get the name of the airport from Dth column of the row where the ICAO code is found
#                     lat = icao.iloc[0, 4]
#                     long = icao.iloc[0, 5]
#                     self.destination_lat_long = f"({lat},{long})"
#                     self.destination_elevation = str(icao.iloc[0, 6])
#                     self.destination_country = icao.iloc[0, 8]
#                     self.destination_region = icao.iloc[0, 9]
#                 else:
#                     self.destination_label.setText("Destination not found")
#                     self.destination_label.setStyleSheet("color: red;")

#             # Update InfoPage if both source and destination are found
#             if self.source_icao and self.destination_icao:
#                 self.info_page.update_label(
#                     self.source_icao,
#                     self.source_apt_name,
#                     self.source_lat_long,
#                     self.source_elevation,
#                     self.source_country,
#                     self.source_region,
#                     self.destination_icao,
#                     self.destination_apt_name,
#                     self.destination_lat_long,
#                     self.destination_elevation,
#                     self.destination_country,
#                     self.destination_region,
#                 )
#                 self.map_page.receive_message(self.source_icao, self.destination_icao)
#                 self.waypoints_page.receive_waypoints(
#                     self.source_icao, self.destination_icao
#                 )

#         except Exception as e:
#             error_message = f"Error: {e}"
#             self.source_label.setText(error_message)
#             self.source_label.setStyleSheet("color: red;")
#             self.destination_label.setText(error_message)
#             self.destination_label.setStyleSheet("color: red;")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     # Create an instance of InfoPage
#     info_page = InfoPage()
#     map_page = MapPage()
#     waypoints_page = WaypointsPage()
#     # Pass the InfoPage instance to the InputPage constructor
#     window = InputPage(info_page, map_page, waypoints_page)
#     window.show()
#     sys.exit(app.exec_())



from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QSpacerItem,
    QSizePolicy,
    QFrame,
    QApplication,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize
import pandas as pd
import sys
from info_page import InfoPage
from map_page import MapPage
from waypoints_page import WaypointsPage
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QWidget
from weather_page2 import WeatherPage


class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QLineEdit {
                background-color: white;
                color: blue;
                border: 1px solid blue;
                padding: 5px;
                selection-background-color: blue;
                selection-color: white;
            }
            QLineEdit:focus {
                border: 2px solid blue;
            }
            """
        )

    def focusInEvent(self, event):
        super().focusInEvent(event)
        if hasattr(self.parent(), "show_virtual_keyboard"):
            self.parent().show_virtual_keyboard(self)


class InputPage(QWidget):
    def __init__(self, info_page, map_page, waypoints_page):
        super().__init__()
        self.info_page = info_page  # Store reference to InfoPage instance
        self.map_page = map_page
        self.waypoints_page = waypoints_page
        self.weather_page = WeatherPage() 
        self.excel_file = "database.xlsx"  # Update with your actual Excel file path
        self.source_icao = None
        self.destination_icao = None
        self.source_apt_name = None         
        self.destination_apt_name = None
        self.source_lat_long = None
        self.destination_lat_long = None
        self.source_elevation = None
        self.destination_elevation = None
        self.source_country = None
        self.destination_country = None
        self.source_region = None
        self.destination_region = None
        self.init_ui()
        self.setAutoFillBackground(True)  # Enable background filling

        # Set the initial background

        self.update_background()

    def update_background(self):
        # Load the image and scale it to the full window size
        pixmap = QPixmap("images/bng.JPG")
        scaled_pixmap = pixmap.scaled(
            self.size(), aspectRatioMode=0
        )  # 0 = Qt.IgnoreAspectRatio
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

    def resizeEvent(self, event):
        # Update the background image size on window resize
        self.update_background()
        super().resizeEvent(event)

    def init_ui(self):
        self.setWindowTitle("Input Page with Virtual Keyboard")
        self.setMinimumSize(800, 600)

        # Layout setup
        outer_layout = QHBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)

        # Left-side layout for main content
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(20, 20, 20, 20)
        left_layout.setSpacing(30)
        self.main_layout = left_layout

        # Add main content to left layout
        self.source_label = QLabel("")  # Label to display search result
        self.source_label.setFont(QFont("Arial", 14))
        self.source_label.setAlignment(Qt.AlignCenter)

        source_section = self.create_input_section("Source", "blue")
        left_layout.addLayout(source_section)
        left_layout.addWidget(self.source_label)

        self.destination_label = QLabel("")  # Label to display search result
        self.destination_label.setFont(QFont("Arial", 14))
        self.destination_label.setAlignment(Qt.AlignCenter)

        destination_section = self.create_input_section("Destination", "blue")
        left_layout.addLayout(destination_section)
        left_layout.addWidget(self.destination_label)

        left_layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        self.keyboard_frame = QFrame()
        self.keyboard_frame.setLayout(QVBoxLayout())
        left_layout.addWidget(self.keyboard_frame)

        self.keyboard_layout = QGridLayout()
        self.keyboard_layout.setSpacing(10)
        self.keyboard_frame.layout().addLayout(self.keyboard_layout)
        self.create_virtual_keyboard()
        self.keyboard_frame.hide()

        # Add left and right layouts to the outer layout
        outer_layout.addLayout(left_layout, 2)  # Left side = 60%
        outer_layout.addStretch(3)  # Right side = 40% empty space

    def create_input_section(self, title, text_color):
        section_layout = QVBoxLayout()

        label = QLabel(title)
        label.setFont(QFont("Arial", 16, QFont.Bold))
        label.setStyleSheet(f"color: {text_color};")
        label.setAlignment(Qt.AlignCenter)
        section_layout.addWidget(label)

        text_box = CustomLineEdit(self)
        text_box.setFont(QFont("Arial", 14))
        text_box.setMinimumHeight(40)
        section_layout.addWidget(text_box)

        submit_button = QPushButton("Submit")
        submit_button.setFont(QFont("Arial", 14))
        submit_button.setStyleSheet(
            "background-color: #00008b; color: white; border: 1px solid #00008b; padding: 5px;"
        )
        submit_button.setMinimumHeight(40)
        submit_button.clicked.connect(lambda: self.on_submit(title, text_box))
        section_layout.addWidget(submit_button)

        if title == "Source":
            self.source_textbox = text_box  # Keep reference to source text box

        return section_layout

    def create_virtual_keyboard(self):
        keyboard_layout = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"],
            ["Space", "Backspace", "Clear"],
        ]

        for row_idx, row in enumerate(keyboard_layout):
            start_col = (10 - len(row)) // 2 if row_idx > 0 else 0
            for col_idx, key in enumerate(row):
                button = QPushButton(key)
                button.setFont(QFont("Arial", 14, QFont.Bold))
                button.setMinimumSize(
                    QSize(60, 60)
                    if key not in ["Space", "Backspace", "Clear"]
                    else QSize(120, 60)
                )
                button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: white;
                        color: blue;
                        border: 2px solid blue;
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton:pressed {
                        background-color: #00008b;
                        color: white;
                    }
                    """
                )
                button.clicked.connect(lambda _, k=key: self.on_key_click(k))
                self.keyboard_layout.addWidget(button, row_idx, start_col + col_idx)

    def on_key_click(self, key):
        if not hasattr(self, "current_textbox") or self.current_textbox is None:
            return

        if key == "Space":
            self.current_textbox.insert(" ")
        elif key == "Clear":
            self.current_textbox.clear()
        elif key == "Backspace":
            self.current_textbox.backspace()
        else:
            self.current_textbox.insert(key)

        self.current_textbox.setFocus()

    def show_virtual_keyboard(self, text_box):
        self.current_textbox = text_box
        self.keyboard_frame.show()

    def on_submit(self, title, text_box):
        input_text = text_box.text()
        if title == "Source":
            self.source = input_text
            self.search_in_excel(self.source, "s")
        if title == "Destination":
            self.destination = input_text
            self.search_in_excel(self.destination, "d")

    def search_in_excel(self, data, mode):
        """Search for source and destination in Excel file."""
        try:
            df = pd.read_excel(self.excel_file)
            icao = df[df.iloc[:, 1] == data]  # B Column

            if mode == "s":
                if not icao.empty:
                    self.source_label.setText("Source found")
                    self.source_label.setStyleSheet("color: green;")
                    self.source_icao = data
                    self.source_apt_name = icao.iloc[
                        0, 3
                    ]  ## Get the name of the airport from Dth column of the row where the ICAO code is found
                    lat = icao.iloc[0, 4]
                    long = icao.iloc[0, 5]
                    self.source_lat_long = f"({lat},{long})"
                    self.source_elevation = str(icao.iloc[0, 6])
                    self.source_country = icao.iloc[0, 8]
                    self.source_region = icao.iloc[0, 9]
                else:
                    self.source_label.setText("Source not found")
                    self.source_label.setStyleSheet("color: red;")

            elif mode == "d":
                if not icao.empty:
                    self.destination_label.setText("Destination found")
                    self.destination_label.setStyleSheet("color: green;")
                    self.destination_icao = data
                    self.destination_apt_name = icao.iloc[
                        0, 3
                    ]  ## Get the name of the airport from Dth column of the row where the ICAO code is found
                    lat = icao.iloc[0, 4]
                    long = icao.iloc[0, 5]
                    self.destination_lat_long = f"({lat},{long})"
                    self.destination_elevation = str(icao.iloc[0, 6])
                    self.destination_country = icao.iloc[0, 8]
                    self.destination_region = icao.iloc[0, 9]
                else:
                    self.destination_label.setText("Destination not found")
                    self.destination_label.setStyleSheet("color: red;")

            # Update InfoPage if both source and destination are found
            if hasattr(self, 'source_icao') and hasattr(self, 'destination_icao'):
                self.weather_page.update_icao_codes(self.source_icao, self.destination_icao)
                self.info_page.update_label(
                    self.source_icao,
                    self.source_apt_name,
                    self.source_lat_long,
                    self.source_elevation,
                    self.source_country,
                    self.source_region,
                    self.destination_icao,
                    self.destination_apt_name,
                    self.destination_lat_long,
                    self.destination_elevation,
                    self.destination_country,
                    self.destination_region,
                )
                self.map_page.receive_message(self.source_icao, self.destination_icao)
                self.waypoints_page.receive_waypoints(
                    self.source_icao, self.destination_icao
                )

        except Exception as e:
            error_message = f"Error: {e}"
            self.source_label.setText(error_message)
            self.source_label.setStyleSheet("color: red;")
            self.destination_label.setText(error_message)
            self.destination_label.setStyleSheet("color: red;")
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Create an instance of InfoPage
    info_page = InfoPage()
    map_page = MapPage()
    waypoints_page = WaypointsPage()
    # Pass the InfoPage instance to the InputPage constructor
    window = InputPage(info_page, map_page, waypoints_page)
    window.show()
    sys.exit(app.exec_())

