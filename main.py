# import sys
# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QWidget,
#     QVBoxLayout,
#     QHBoxLayout,
#     QLabel,
#     QStackedWidget,
# )
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont

# # Import the page classes
# from input_page import InputPage
# from info_page import InfoPage
# from map_page import MapPage
# from waypoints_page import WaypointsPage
# from weather_page import WeatherPage
# from engine_page import InstrumentPanel


# class FlightManagementSystem(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.current_page_index = 0  # Track the current page

#         # Page names (keep the order from the main window)
#         self.pages = ["Input", "INFO", "MAP", "Waypoints", "Weather", "Engine"]

#         # Set up the main window
#         self.setWindowTitle("Flight Management System")
#         self.setGeometry(0, 0, 800, 600)

#         # Main layout
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#         self.main_layout = QVBoxLayout(self.central_widget)
#         self.main_layout.setContentsMargins(0, 0, 0, 0)

#         # Create the white rectangular box
#         self.box = QWidget(self)
#         self.main_layout.addWidget(self.box)
#         self.box.setStyleSheet("background-color: #FFFFFF; border: 2px solid black;")

#         # Stacked widget to manage multiple pages
#         self.stacked_widget = QStackedWidget(self)
#         self.main_layout.addWidget(self.stacked_widget)

#         # Create InfoPage instance first
#         self.info_page = InfoPage()

#         # Pass the InfoPage instance to InputPage constructor
#         self.info_page = InfoPage()  # Initialize info_page first
#         self.map_page = MapPage()  # Initialize map_page next
#         self.waypoints_page = WaypointsPage()
#         self.weather_page = WeatherPage()
#         self.engine_page = InstrumentPanel()
#         self.input_page = InputPage(
#             self.info_page, self.map_page, self.waypoints_page
#         )  # Now, use both info_page and map_page

#         # Add pages to stacked widget
#         self.stacked_widget.addWidget(self.input_page)
#         self.stacked_widget.addWidget(self.info_page)
#         self.stacked_widget.addWidget(self.map_page)
#         self.stacked_widget.addWidget(self.waypoints_page)
#         self.stacked_widget.addWidget(self.weather_page)
#         self.stacked_widget.addWidget(self.engine_page)

#         # Add navigation bar
#         self.navigation_bar = QWidget(self)
#         self.navigation_bar.setStyleSheet("background-color: #00008b;")
#         self.navigation_layout = QHBoxLayout(self.navigation_bar)
#         self.navigation_bar.setFixedHeight(90)
#         self.navigation_layout.setContentsMargins(10, 5, 10, 5)
#         self.navigation_layout.setSpacing(5)

#         # Page name labels (Clickable)
#         self.page_labels = []
#         for index, page in enumerate(self.pages):
#             label = QLabel(page, self.navigation_bar)
#             label.setFont(QFont("Arial", 16, QFont.Bold))
#             label.setAlignment(Qt.AlignCenter)
#             label.setStyleSheet("color: white;")
#             label.mousePressEvent = lambda event, i=index: self.navigate_to_page(i)
#             self.page_labels.append(label)
#             self.navigation_layout.addWidget(label)

#         # Add navigation bar to the main layout
#         self.main_layout.addWidget(self.navigation_bar)

#         # Highlight the default current page
#         self.update_highlighted_page()

#         # Automatically maximize the window
#         self.showMaximized()

#     def navigate_to_page(self, index):
#         """Navigate to the page clicked."""
#         self.current_page_index = index
#         self.stacked_widget.setCurrentIndex(index)
#         self.update_highlighted_page()

#     def update_highlighted_page(self):
#         """Update the highlighted page color."""
#         for i, label in enumerate(self.page_labels):
#             if i == self.current_page_index:
#                 label.setStyleSheet("color: yellow;")
#             else:
#                 label.setStyleSheet("color: white;")


# # Entry point for the application
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FlightManagementSystem()
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QWidget,
#     QVBoxLayout,
#     QHBoxLayout,
#     QLabel,
#     QStackedWidget,
# )
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont

# # Import the page classes
# from input_page import InputPage
# from info_page import InfoPage
# from map_page import MapPage
# from waypoints_page import WaypointsPage
# from weather_page import WeatherPage
# from engine_page import InstrumentPanel


# class FlightManagementSystem(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.current_page_index = 0  # Track the current page

#         # Page names (keep the order from the main window)
#         self.pages = ["Input", "INFO", "MAP", "Waypoints", "Weather", "Engine"]

#         # Set up the main window
#         self.setWindowTitle("Flight Management System")
#         self.setGeometry(0, 0, 800, 600)

#         # Main layout
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#         self.main_layout = QVBoxLayout(self.central_widget)
#         self.main_layout.setContentsMargins(0, 0, 0, 0)

#         # Add navigation bar at the top
#         self.navigation_bar = QWidget(self)
#         self.navigation_bar.setStyleSheet("background-color: #00008b;")
#         self.navigation_layout = QHBoxLayout(self.navigation_bar)
#         self.navigation_bar.setFixedHeight(90)
#         self.navigation_layout.setContentsMargins(10, 5, 10, 5)
#         self.navigation_layout.setSpacing(5)

#         # Page name labels (Clickable)
#         self.page_labels = []
#         for index, page in enumerate(self.pages):
#             label = QLabel(page, self.navigation_bar)
#             label.setFont(QFont("Arial", 16, QFont.Bold))
#             label.setAlignment(Qt.AlignCenter)
#             label.setStyleSheet("color: white;")
#             label.mousePressEvent = lambda event, i=index: self.navigate_to_page(i)
#             self.page_labels.append(label)
#             self.navigation_layout.addWidget(label)

#         self.main_layout.addWidget(self.navigation_bar)  # Add navigation bar to the top

#         # Create the white rectangular box
#         self.box = QWidget(self)
#         self.main_layout.addWidget(self.box)
#         self.box.setStyleSheet("background-color: #FFFFFF; border: 2px solid black;")

#         # Stacked widget to manage multiple pages
#         self.stacked_widget = QStackedWidget(self)
#         self.main_layout.addWidget(self.stacked_widget)

#         # Create InfoPage instance first
#         self.info_page = InfoPage()

#         # Pass the InfoPage instance to InputPage constructor
#         self.info_page = InfoPage()  # Initialize info_page first
#         self.map_page = MapPage()  # Initialize map_page next
#         self.waypoints_page = WaypointsPage()
#         self.weather_page = WeatherPage()
#         self.engine_page = InstrumentPanel()
#         self.input_page = InputPage(
#             self.info_page, self.map_page, self.waypoints_page
#         )  # Now, use both info_page and map_page

#         # Add pages to stacked widget
#         self.stacked_widget.addWidget(self.input_page)
#         self.stacked_widget.addWidget(self.info_page)
#         self.stacked_widget.addWidget(self.map_page)
#         self.stacked_widget.addWidget(self.waypoints_page)
#         self.stacked_widget.addWidget(self.weather_page)
#         self.stacked_widget.addWidget(self.engine_page)

#         # Highlight the default current page
#         self.update_highlighted_page()

#         # Automatically maximize the window
#         self.showMaximized()

#     def navigate_to_page(self, index):
#         """Navigate to the page clicked."""
#         self.current_page_index = index
#         self.stacked_widget.setCurrentIndex(index)
#         self.update_highlighted_page()

#     def update_highlighted_page(self):
#         """Update the highlighted page color."""
#         for i, label in enumerate(self.page_labels):
#             if i == self.current_page_index:
#                 label.setStyleSheet("color: yellow;")
#             else:
#                 label.setStyleSheet("color: white;")


# # Entry point for the application
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FlightManagementSystem()
#     window.show()
#     sys.exit(app.exec_())

'''
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStackedWidget,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Import the page classes
from input_page import InputPage
from info_page import InfoPage
from map_page import MapPage
from waypoints_page import WaypointsPage
from weather_page import WeatherPage
from engine_page1 import InstrumentPanel
from menu5_page import MenuPage  # Import the menu page


class FlightManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_page_index = 0  # Track the current page

        # Page names (keep the order from the main window)
        self.pages = ["Menu", "Input", "INFO", "MAP", "Waypoints", "Weather", "Engine"]

        # Set up the main window
        self.setWindowTitle("Flight Management System")
        self.setGeometry(0, 0, 800, 600)

        # Main layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Add navigation bar at the top
        self.navigation_bar = QWidget(self)
        self.navigation_bar.setStyleSheet("background-color: #00008b;")
        self.navigation_layout = QHBoxLayout(self.navigation_bar)
        self.navigation_bar.setFixedHeight(90)
        self.navigation_layout.setContentsMargins(10, 5, 10, 5)
        self.navigation_layout.setSpacing(5)

        # Page name labels (Clickable)
        self.page_labels = []
        for index, page in enumerate(self.pages):
            label = QLabel(page, self.navigation_bar)
            label.setFont(QFont("Arial", 16, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("color: white;")
            label.mousePressEvent = lambda event, i=index: self.navigate_to_page(i)
            self.page_labels.append(label)
            self.navigation_layout.addWidget(label)

        self.main_layout.addWidget(self.navigation_bar)  # Add navigation bar to the top

        # Create the white rectangular box
        self.box = QWidget(self)
        self.main_layout.addWidget(self.box)
        self.box.setStyleSheet("background-color: black; border: 2px solid black;")

        # Stacked widget to manage multiple pages
        self.stacked_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.stacked_widget)

        # Create InfoPage instance first
        self.info_page = InfoPage()

        # Pass the InfoPage instance to InputPage constructor
        self.info_page = InfoPage()  # Initialize info_page first
        self.map_page = MapPage()  # Initialize map_page next
        self.waypoints_page = WaypointsPage()
        self.weather_page = WeatherPage()
        self.engine_page = InstrumentPanel()
        self.input_page = InputPage(
            self.info_page, self.map_page, self.waypoints_page
        )  # Now, use both info_page and map_page

        # Create Menu Page instance
        self.menu_page = MenuPage()

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.menu_page)  # Add Menu Page first
        self.stacked_widget.addWidget(self.input_page)
        self.stacked_widget.addWidget(self.info_page)
        self.stacked_widget.addWidget(self.map_page)
        self.stacked_widget.addWidget(self.waypoints_page)
        self.stacked_widget.addWidget(self.weather_page)
        self.stacked_widget.addWidget(self.engine_page)

        # Connect menu page signal to navigate
        self.menu_page.page_selected_signal.connect(self.navigate_to_page)

        # Highlight the default current page
        self.update_highlighted_page()

        # Automatically maximize the window
        self.showMaximized()

    def navigate_to_page(self, index):
        """Navigate to the page clicked."""
        if isinstance(index, int):
            self.current_page_index = index
            self.stacked_widget.setCurrentIndex(index)
            self.update_highlighted_page()
        else:
            # if navigated from menu page
            self.current_page_index = index
            self.stacked_widget.setCurrentIndex(index)
            self.update_highlighted_page()

    def update_highlighted_page(self):
        """Update the highlighted page color."""
        for i, label in enumerate(self.page_labels):
            if i == self.current_page_index:
                label.setStyleSheet("color: yellow;")
            else:
                label.setStyleSheet("color: white;")


# Entry point for the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlightManagementSystem()
    window.show()
    sys.exit(app.exec_())
'''


#This works
'''
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStackedWidget,
)
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal
from PyQt5.QtGui import QFont
import threading
import time

# Import the page classes
from input_page3 import InputPage
from info_page2 import InfoPage
from map_page2 import MapPage
from waypoints_page2 import WaypointsPage
from weather_page2 import WeatherPage
from engine_page import InstrumentPanel
from menu5_page import MenuPage  # Import the menu page

try:
    import RPi.GPIO as GPIO
    GPIO_AVAILABLE = True
except ImportError:
    print("RPi.GPIO library not found. GPIO functionality will be disabled.")
    GPIO_AVAILABLE = False

class RotarySignalHandler(QObject):
    """Signal handler for rotary events to communicate with the PyQt5 UI."""

    page_signal = pyqtSignal(int)

class FlightManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_page_index = 0  # Track the current page
        self.pages = ["Menu", "Input", "INFO", "MAP", "Waypoints", "Weather", "Engine"]

        # Set up the main window
        self.setWindowTitle("Flight Management System")
        self.setGeometry(0, 0, 800, 600)

        # Main layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Add navigation bar at the top
        self.navigation_bar = QWidget(self)
        self.navigation_bar.setStyleSheet("background-color: #00008b;")
        self.navigation_layout = QHBoxLayout(self.navigation_bar)
        self.navigation_bar.setFixedHeight(90)
        self.navigation_layout.setContentsMargins(10, 5, 10, 5)
        self.navigation_layout.setSpacing(5)

        # Page name labels (Clickable)
        self.page_labels = []
        for index, page in enumerate(self.pages):
            label = QLabel(page, self.navigation_bar)
            label.setFont(QFont("Arial", 16, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("color: white;")
            label.mousePressEvent = lambda event, i=index: self.navigate_to_page(i)
            self.page_labels.append(label)
            self.navigation_layout.addWidget(label)

        self.main_layout.addWidget(self.navigation_bar)  # Add navigation bar to the top

        # Create the white rectangular box
        self.box = QWidget(self)
        self.main_layout.addWidget(self.box)
        self.box.setStyleSheet("background-color: black; border: 2px solid black;")

        # Stacked widget to manage multiple pages
        self.stacked_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.stacked_widget)

        # Create InfoPage instance first
        self.info_page = InfoPage()

        # Pass the InfoPage instance to InputPage constructor
        self.info_page = InfoPage()  # Initialize info_page first
        self.map_page = MapPage()  # Initialize map_page next
        self.waypoints_page = WaypointsPage()
        
        self.engine_page = InstrumentPanel()
        self.input_page = InputPage(
            self.info_page, self.map_page, self.waypoints_page
        )  # Now, use both info_page and map_page
        self.weather_page = WeatherPage()

        # Create Menu Page instance
        self.menu_page = MenuPage()

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.menu_page)  # Add Menu Page first
        self.stacked_widget.addWidget(self.input_page)
        self.stacked_widget.addWidget(self.info_page)
        self.stacked_widget.addWidget(self.map_page)
        self.stacked_widget.addWidget(self.waypoints_page)
        self.stacked_widget.addWidget(self.weather_page)
        self.stacked_widget.addWidget(self.engine_page)

        # Connect menu page signal to navigate
        self.menu_page.page_selected_signal.connect(self.navigate_to_page)

        # Highlight the default current page
        self.update_highlighted_page()

        # Automatically maximize the window
        self.showMaximized()

        # --- GPIO Setup (if available) ---
        if GPIO_AVAILABLE:
             self.gpio_setup()

        # --- Start Polling Timer (if available) ---
        if GPIO_AVAILABLE:
            self.gpio_timer = QTimer(self)
            self.gpio_timer.timeout.connect(self.check_gpio_buttons)
            self.gpio_timer.start(50) # Adjust polling interval (milliseconds)

        # Rotary signal handler
        self.rotary_handler = RotarySignalHandler()
        self.rotary_handler.page_signal.connect(self.navigate_to_page)

        # Start the rotary switch thread
        self.rotary_thread = threading.Thread(target=self.run_rotary_listener)
        self.rotary_thread.daemon = True
        self.rotary_thread.start()


    def navigate_to_page(self, index):
        """Navigate to the page clicked."""
        if isinstance(index, int):
            self.current_page_index = index
            self.stacked_widget.setCurrentIndex(index)
            self.update_highlighted_page()
        else:
            # if navigated from menu page
            self.current_page_index = index
            self.stacked_widget.setCurrentIndex(index)
            self.update_highlighted_page()
            
    def navigate_from_menu(self, index):
       """Navigate to the page selected from the menu page"""
       # Map menu index to page index
       # menu indices: 1=input, 2=info, 3=map, 4=waypoints, 5=weather, 6=engine
       page_map = {
           1: 1,  # Input
           2: 2,  # Info
           3: 3,  # Map
           4: 4, #Waypoints
           5: 5, #Weather
           6: 6 #Engine
       }
        
       page_index = page_map.get(index,0) # Default to Menu
        
       self.current_page_index = page_index
       self.stacked_widget.setCurrentIndex(page_index)
       self.update_highlighted_page()


    def update_highlighted_page(self):
        """Update the highlighted page color."""
        for i, label in enumerate(self.page_labels):
            if i == self.current_page_index:
                label.setStyleSheet("color: yellow;")
            else:
                label.setStyleSheet("color: white;")

    def run_rotary_listener(self):
        """Run the rotary switch listener in a separate thread."""
        # Set up GPIO
        GPIO.setmode(GPIO.BCM)

        encoder_pins = [5, 22, 27, 4, 14, 15, 23, 12]
        GPIO.setup(encoder_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        encoder_map = {
            5: 1,
            22: 2,
            27: 3,
            4: 4,
            14: 5,
            15: 6,
            23: 7,
            12: 8,
        }

        # Function to get the status of the encoder
        def get_encoder_status():
            current_value = 0

            for pin, value in encoder_map.items():
                if GPIO.input(pin) == GPIO.LOW:  # Active LOW (when pin is pressed/active)
                    current_value = value

            return current_value
        
        previous_value = get_encoder_status()

        try:
            while True:
                current_value = get_encoder_status()
                if current_value != previous_value:
                    
                    if (current_value == 1 and previous_value == 8):
                        self.rotary_handler.page_signal.emit(0) #MenuPage
                    elif (current_value == 8 and previous_value == 1):
                        self.rotary_handler.page_signal.emit(6) #EnginePage
                    elif current_value > previous_value:
                        page_index = self.current_page_index + 1
                        if page_index > len(self.pages)-1:
                            page_index = 0
                        self.rotary_handler.page_signal.emit(page_index)
                        
                    elif current_value < previous_value:
                        page_index = self.current_page_index - 1
                        if page_index < 0:
                            page_index = len(self.pages)-1
                        self.rotary_handler.page_signal.emit(page_index)
                    
                    previous_value = current_value
                time.sleep(0.1)

        except KeyboardInterrupt:
            GPIO.cleanup()
        finally:
            GPIO.cleanup()

    def gpio_setup(self):
        """Initializes GPIO settings."""
        GPIO.setmode(GPIO.BCM) # Using BCM numbering
        self.gpio_pins = {
            "up": 26,
            "down": 20,
            "left": 25,
            "right": 19,
            "select": 13,
        }
        for pin in self.gpio_pins.values():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pull up for active high

        self.last_button_states = {pin: GPIO.input(pin) for pin in self.gpio_pins.values()}
        self.button_debounce_time = 0.05 # Adjust debounce time (seconds)

    def check_gpio_buttons(self):
         """Checks the state of GPIO buttons and trigger actions"""
         if self.current_page_index != 0:
             return # Only process button presses on menu page

         for button, pin in self.gpio_pins.items():
            current_state = GPIO.input(pin)
            if current_state != self.last_button_states[pin]:
                 if current_state == GPIO.LOW: # Button pressed
                    self.handle_gpio_button_press(button)
                 self.last_button_states[pin] = current_state

    def handle_gpio_button_press(self, button):
          """Handles a single gpio button press"""
          if button == "up":
                self.menu_page.navigate("up")
          elif button == "down":
                 self.menu_page.navigate("down")
          elif button == "left":
                  self.menu_page.navigate("left")
          elif button == "right":
                 self.menu_page.navigate("right")
          elif button == "select":
                self.menu_page.select_highlighted_icon()


    def closeEvent(self, event):
        """Clean up GPIO settings on close."""
        if GPIO_AVAILABLE:
           GPIO.cleanup()
        super().closeEvent(event)



# Entry point for the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlightManagementSystem()
    window.show()
    sys.exit(app.exec_())





'''

#This works fine with centre button in rotary button as well

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStackedWidget,
)
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal
from PyQt5.QtGui import QFont
import threading
import time

# Import the page classes
from input_page3 import InputPage
from info_page2 import InfoPage
from map_page2 import MapPage
from waypoints_page2 import WaypointsPage
from weather_page2 import WeatherPage
from engine_page import InstrumentPanel
from menu5_page import MenuPage  # Import the menu page

# try:
#     import RPi.GPIO as GPIO
#     GPIO_AVAILABLE = True
# except ImportError:
#     print("RPi.GPIO library not found. GPIO functionality will be disabled.")
#     GPIO_AVAILABLE = False

# class RotarySignalHandler(QObject):
#     """Signal handler for rotary events to communicate with the PyQt5 UI."""

#     page_signal = pyqtSignal(int)

class FlightManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_page_index = 0  # Track the current page
        self.pages = ["Menu", "Input", "INFO", "MAP", "Waypoints", "Weather", "Engine"]

        # Set up the main window
        self.setWindowTitle("Flight Management System")
        self.setGeometry(0, 0, 800, 600)

        # Main layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Add navigation bar at the top
        self.navigation_bar = QWidget(self)
        self.navigation_bar.setStyleSheet("background-color: #00008b;")
        self.navigation_layout = QHBoxLayout(self.navigation_bar)
        self.navigation_bar.setFixedHeight(90)
        self.navigation_layout.setContentsMargins(10, 5, 10, 5)
        self.navigation_layout.setSpacing(5)

        # Page name labels (Clickable)
        self.page_labels = []
        for index, page in enumerate(self.pages):
            label = QLabel(page, self.navigation_bar)
            label.setFont(QFont("Arial", 16, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("color: white;")
            label.mousePressEvent = lambda event, i=index: self.navigate_to_page(i)
            self.page_labels.append(label)
            self.navigation_layout.addWidget(label)

        self.main_layout.addWidget(self.navigation_bar)  # Add navigation bar to the top

        # Create the white rectangular box
        self.box = QWidget(self)
        self.main_layout.addWidget(self.box)
        self.box.setStyleSheet("background-color: black; border: 2px solid black;")

        # Stacked widget to manage multiple pages
        self.stacked_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.stacked_widget)

        # Create InfoPage instance first
        self.info_page = InfoPage()

        # Pass the InfoPage instance to InputPage constructor
        self.info_page = InfoPage()  # Initialize info_page first
        self.map_page = MapPage()  # Initialize map_page next
        self.waypoints_page = WaypointsPage()
        
        self.engine_page = InstrumentPanel()
        self.input_page = InputPage(
            self.info_page, self.map_page, self.waypoints_page
        )  # Now, use both info_page and map_page
        self.weather_page = WeatherPage()

        # Create Menu Page instance
        self.menu_page = MenuPage()

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.menu_page)  # Add Menu Page first
        self.stacked_widget.addWidget(self.input_page)
        self.stacked_widget.addWidget(self.info_page)
        self.stacked_widget.addWidget(self.map_page)
        self.stacked_widget.addWidget(self.waypoints_page)
        self.stacked_widget.addWidget(self.weather_page)
        self.stacked_widget.addWidget(self.engine_page)

        # Connect menu page signal to navigate
        self.menu_page.page_selected_signal.connect(self.navigate_to_page)

        # Highlight the default current page
        self.update_highlighted_page()

        # Automatically maximize the window
        self.showMaximized()

        # --- GPIO Setup (if available) ---
        # if GPIO_AVAILABLE:
        #      self.gpio_setup()

        # # --- Start Polling Timer (if available) ---
        # if GPIO_AVAILABLE:
        #     self.gpio_timer = QTimer(self)
        #     self.gpio_timer.timeout.connect(self.check_gpio_buttons)
        #     self.gpio_timer.start(50) # Adjust polling interval (milliseconds)

        # # Rotary signal handler
        # self.rotary_handler = RotarySignalHandler()
        # self.rotary_handler.page_signal.connect(self.navigate_to_page)

        # # Start the rotary switch thread
        # self.rotary_thread = threading.Thread(target=self.run_rotary_listener)
        # self.rotary_thread.daemon = True
        # self.rotary_thread.start()


    def navigate_to_page(self, index):
        """Navigate to the page clicked."""
        if isinstance(index, int):
            self.current_page_index = index
            self.stacked_widget.setCurrentIndex(index)
            self.update_highlighted_page()
        else:
            # if navigated from menu page
            self.current_page_index = index
            self.stacked_widget.setCurrentIndex(index)
            self.update_highlighted_page()
            
    def navigate_from_menu(self, index):
       """Navigate to the page selected from the menu page"""
       # Map menu index to page index
       # menu indices: 1=input, 2=info, 3=map, 4=waypoints, 5=weather, 6=engine
       page_map = {
           1: 1,  # Input
           2: 2,  # Info
           3: 3,  # Map
           4: 4, #Waypoints
           5: 5, #Weather
           6: 6 #Engine
       }
        
       page_index = page_map.get(index,0) # Default to Menu
        
       self.current_page_index = page_index
       self.stacked_widget.setCurrentIndex(page_index)
       self.update_highlighted_page()


    def update_highlighted_page(self):
        """Update the highlighted page color."""
        for i, label in enumerate(self.page_labels):
            if i == self.current_page_index:
                label.setStyleSheet("color: yellow;")
            else:
                label.setStyleSheet("color: white;")

    # def run_rotary_listener(self):
    #     """Run the rotary switch listener in a separate thread."""
    #     # Set up GPIO
    #     GPIO.setmode(GPIO.BCM)

    #     encoder_pins = [5, 22, 27, 4, 14, 15, 23, 12]
    #     GPIO.setup(encoder_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #     encoder_map = {
    #         5: 1,
    #         22: 2,
    #         27: 3,
    #         4: 4,
    #         14: 5,
    #         15: 6,
    #         23: 7,
    #         12: 8,
    #     }
    #     center_button = 16
    #     GPIO.setup(center_button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Pull up resistor for centre button

    #     # Function to get the status of the encoder
    #     def get_encoder_status():
    #         current_value = 0

    #         for pin, value in encoder_map.items():
    #             if GPIO.input(pin) == GPIO.LOW:  # Active LOW (when pin is pressed/active)
    #                 current_value = value

    #         return current_value
        
    #     previous_value = get_encoder_status()

    #     try:
    #         while True:
    #             current_value = get_encoder_status()
    #             if current_value != previous_value:
                    
    #                 if (current_value == 1 and previous_value == 8):
    #                     self.rotary_handler.page_signal.emit(0) #MenuPage
    #                 elif (current_value == 8 and previous_value == 1):
    #                     self.rotary_handler.page_signal.emit(6) #EnginePage
    #                 elif current_value > previous_value:
    #                     page_index = self.current_page_index + 1
    #                     if page_index > len(self.pages)-1:
    #                         page_index = 0
    #                     self.rotary_handler.page_signal.emit(page_index)
                        
    #                 elif current_value < previous_value:
    #                     page_index = self.current_page_index - 1
    #                     if page_index < 0:
    #                         page_index = len(self.pages)-1
    #                     self.rotary_handler.page_signal.emit(page_index)
                    
    #                 previous_value = current_value
                
    #             if GPIO.input(center_button) == GPIO.LOW: #If center button is pressed, it is active low
    #                 self.rotary_handler.page_signal.emit(0) # Navigate to the Menu Page (index 0)
    #                 time.sleep(0.2) # Debounce for a short time

    #             time.sleep(0.1)

    #     except KeyboardInterrupt:
    #         GPIO.cleanup()
    #     finally:
    #         GPIO.cleanup()

    # def gpio_setup(self):
    #     """Initializes GPIO settings."""
    #     GPIO.setmode(GPIO.BCM) # Using BCM numbering
    #     self.gpio_pins = {
    #         "up": 26,
    #         "down": 20,
    #         "left": 25,
    #         "right": 19,
    #         "select": 13,
    #     }
    #     for pin in self.gpio_pins.values():
    #         GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pull up for active high

    #     self.last_button_states = {pin: GPIO.input(pin) for pin in self.gpio_pins.values()}
    #     self.button_debounce_time = 0.05 # Adjust debounce time (seconds)

    # def check_gpio_buttons(self):
    #      """Checks the state of GPIO buttons and trigger actions"""
    #      if self.current_page_index != 0:
    #          return # Only process button presses on menu page

    #      for button, pin in self.gpio_pins.items():
    #         current_state = GPIO.input(pin)
    #         if current_state != self.last_button_states[pin]:
    #              if current_state == GPIO.LOW: # Button pressed
    #                 self.handle_gpio_button_press(button)
    #              self.last_button_states[pin] = current_state

    # def handle_gpio_button_press(self, button):
    #       """Handles a single gpio button press"""
    #       if button == "up":
    #             self.menu_page.navigate("up")
    #       elif button == "down":
    #              self.menu_page.navigate("down")
    #       elif button == "left":
    #               self.menu_page.navigate("left")
    #       elif button == "right":
    #              self.menu_page.navigate("right")
    #       elif button == "select":
    #             self.menu_page.select_highlighted_icon()


    # def closeEvent(self, event):
    #     """Clean up GPIO settings on close."""
    #     if GPIO_AVAILABLE:
    #        GPIO.cleanup()
    #     super().closeEvent(event)



# Entry point for the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlightManagementSystem()
    window.show()
    sys.exit(app.exec_())
