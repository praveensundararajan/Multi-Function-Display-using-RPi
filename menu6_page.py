from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QGridLayout,
    QHBoxLayout,
    QSizePolicy,
)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush
from PyQt5.QtCore import Qt, pyqtSignal, QPoint


class MenuPage(QWidget):
    page_selected_signal = pyqtSignal(int)
    back_to_main_signal = pyqtSignal()  # Signal to return to main page

    def __init__(self):
        super().__init__()
        self.highlighted_index = 0
        self.icons = []
        self.arrow_button_text_color = "black"
        self.highlight_color = "rgba(255,255,255, 0.2)"
        self.buttons = {}  # Dictionary to store button references
        
        # Define custom button positions
        self.button_positions = {
            "up": QPoint(50, 200),     # Left side, middle
            "down": QPoint(50, 300),   # Left side, lower
            "left": QPoint(50, 100),   # Left side, upper
            "right": QPoint(700, 200), # Right side, middle
            "select": QPoint(700, 300),# Right side, lower
            "back": QPoint(700, 100)   # Right side, upper
        }

        self.init_ui()
        self.update_background()
        self.update_highlight()

    def init_ui(self):
        # Use absolute positioning
        self.setLayout(None)
        
        # Create navigation buttons
        self.create_navigation_buttons()
        
        # Grid of Icons (centered)
        icon_container = QWidget(self)
        icon_container.setGeometry(150, 50, 500, 400)  # Adjust size as needed
        icon_layout = QGridLayout(icon_container)
        self.icons = self.create_icon_grid(icon_layout)

    def create_navigation_buttons(self):
        button_configs = {
            "up": ("↑", self.navigate_up),
            "down": ("↓", self.navigate_down),
            "left": ("←", self.navigate_left),
            "right": ("→", self.navigate_right),
            "select": ("Select", self.select_highlighted_icon),
            "back": ("Back", self.back_to_main)
        }

        for button_id, (text, callback) in button_configs.items():
            button = QPushButton(text, self)
            button.setFixedSize(80, 40)  # Set fixed size for all buttons
            
            # Set position based on the predefined positions
            pos = self.button_positions[button_id]
            button.move(pos.x(), pos.y())
            
            button.clicked.connect(callback)
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: rgba(255, 255, 255, 0.1);
                    border: 1px solid gray;
                    border-radius: 5px;
                    color: {self.arrow_button_text_color};
                }}
                QPushButton:hover {{
                    background-color: rgba(255, 255, 255, 0.2);
                }}
                QPushButton:pressed {{
                    background-color: rgba(255, 255, 255, 0.3);
                }}
            """)
            self.buttons[button_id] = button

    def navigate_up(self):
        self.navigate("up")

    def navigate_down(self):
        self.navigate("down")

    def navigate_left(self):
        self.navigate("left")

    def navigate_right(self):
        self.navigate("right")

    def back_to_main(self):
        self.back_to_main_signal.emit()

    # Rest of the existing methods remain the same, just remove the layout-related code
    def create_icon_grid(self, layout):
        icon_size = 100
        pages = ["Input", "INFO", "MAP", "Waypoints", "Weather", "Engine"]
        icons = []
        for i, page_name in enumerate(pages):
            button_widget = QWidget()
            button_widget.setObjectName("iconContainer")
            widget_layout = QVBoxLayout(button_widget)
            widget_layout.setAlignment(Qt.AlignCenter)
            widget_layout.setSpacing(5)
            
            icon_label = QLabel()
            icon_path = self.get_icon_path(page_name)
            pixmap = QPixmap(icon_path).scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(pixmap)
            icon_label.setAlignment(Qt.AlignCenter)
            widget_layout.addWidget(icon_label)

            page_label = QLabel(page_name)
            page_label.setFont(QFont("Arial", 12, QFont.Bold))
            page_label.setAlignment(Qt.AlignCenter)
            widget_layout.addWidget(page_label)

            button_widget.setStyleSheet("#iconContainer { background-color: transparent; }")
            icons.append(button_widget)

            row, col = divmod(i, 3)
            layout.addWidget(button_widget, row, col)

        return icons


    def get_icon_path(self, page_name):
        icon_mapping = {
            "Input": "menu_icons/input.png",
            "INFO": "menu_icons/info.png",
            "MAP": "menu_icons/map.png",
            "Waypoints": "menu_icons/waypoint.png",
            "Weather": "menu_icons/weather.png",
            "Engine": "menu_icons/engine.png",
        }
        return icon_mapping.get(page_name, "images/visibility_icon.png")

    def navigate(self, direction):
        num_icons = len(self.icons)
        if num_icons == 0:
            return

        rows = 2
        cols = 3
        if direction == "up":
            self.highlighted_index = (self.highlighted_index - cols + num_icons) % num_icons
        elif direction == "down":
            self.highlighted_index = (self.highlighted_index + cols) % num_icons
        elif direction == "left":
            self.highlighted_index = (self.highlighted_index - 1 + num_icons) % num_icons
        elif direction == "right":
            self.highlighted_index = (self.highlighted_index + 1) % num_icons

        self.update_highlight()

    def update_highlight(self):
        for i, icon in enumerate(self.icons):
            if i == self.highlighted_index:
                icon.setStyleSheet("""
                    #iconContainer {
                        background-color: rgba(0, 0, 230, 0.2);
                        border-radius: 5px;
                        padding: 5px;
                        margin: 5px;
                    }
                """)
            else:
                icon.setStyleSheet("#iconContainer { background-color: transparent; }")

    def select_highlighted_icon(self):
        self.page_selected_signal.emit(self.highlighted_index + 1)


if __name__ == "__main__":
    from PyQt5.QtWidgets import (
        QApplication,
        QMainWindow,
        QWidget,
        QVBoxLayout,
        QStackedWidget,
        QLabel,
    )
    from PyQt5.QtGui import QPalette, QBrush, QPixmap
    from PyQt5.QtCore import Qt

    # MenuPage class here

    # Sample Page Classes
    class InputPage(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout(self)
            label = QLabel("Input Page")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

    class InfoPage(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout(self)
            label = QLabel("Info Page")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

    class MapPage(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout(self)
            label = QLabel("Map Page")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

    class WeatherPage(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout(self)
            label = QLabel("Weather Page")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

    class EnginePage(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout(self)
            label = QLabel("Engine Page")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

    class WaypointsPage(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout(self)
            label = QLabel("Waypoints Page")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Navigation App")
            self.setGeometry(100, 100, 800, 600)

            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            self.main_layout = QVBoxLayout(self.central_widget)

            # Create Pages
            self.input_page = InputPage()
            self.info_page = InfoPage()
            self.map_page = MapPage()
            self.weather_page = WeatherPage()
            self.engine_page = EnginePage()
            self.waypoint_page = WaypointsPage()

            # Create the stacked widget
            self.stacked_widget = QStackedWidget()
            self.stacked_widget.addWidget(self.input_page)
            self.stacked_widget.addWidget(self.info_page)
            self.stacked_widget.addWidget(self.map_page)
            self.stacked_widget.addWidget(self.waypoint_page)
            self.stacked_widget.addWidget(self.weather_page)
            self.stacked_widget.addWidget(self.engine_page)

            self.main_layout.addWidget(self.stacked_widget)

            # Menu Page
            self.menu_page = MenuPage()
            self.menu_page.page_selected_signal.connect(self.switch_page)
            self.main_layout.addWidget(self.menu_page)

        def switch_page(self, page_index):
            self.stacked_widget.setCurrentIndex(
                page_index - 1
            )  # Adjust for 0-based index

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
