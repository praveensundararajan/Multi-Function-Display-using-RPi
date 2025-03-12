from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QGridLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush
from PyQt5.QtCore import Qt, pyqtSignal

class MenuPage(QWidget):
    page_selected_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.highlighted_index = 0
        self.icons = []
        self.arrow_button_text_color = "black"
        self.highlight_color = "rgba(255,255,255, 0.2)"

        self.init_ui()
        self.update_background()
        self.update_highlight()

    def update_background(self):
        image_path = "images/menu_bg.png"
        if not QPixmap(image_path).isNull():
            pixmap = QPixmap(image_path).scaled(
                self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(pixmap))
            self.setAutoFillBackground(True)
            self.setPalette(palette)
        else:
            print(f"Error: Image not found at {image_path}")

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        
        # Create top section with navigation buttons and icons
        top_section = QHBoxLayout()
        
        # Left Navigation Buttons (first 4 buttons)
        left_buttons_layout = QVBoxLayout()
        left_buttons_layout.setAlignment(Qt.AlignCenter)
        self.create_nav_buttons(left_buttons_layout)
        top_section.addLayout(left_buttons_layout)
        
        # Grid of Icons
        self.icon_grid_layout = QGridLayout()
        self.icons = self.create_icon_grid()
        top_section.addLayout(self.icon_grid_layout)
        
        main_layout.addLayout(top_section)
        
        # Add spacer to push select button to bottom
        main_layout.addStretch()
        
        # Create bottom section for Select button
        bottom_section = QHBoxLayout()
        bottom_section.setAlignment(Qt.AlignCenter)
        self.create_select_button(bottom_section)
        main_layout.addLayout(bottom_section)

    def create_nav_buttons(self, layout):
        buttons = ["↑", "↓", "←", "→"]
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet(
                f"""
                QPushButton {{
                    background-color: rgba(255, 255, 255, 0.1);
                    border: 1px solid gray;
                    padding: 10px;
                    border-radius: 5px;
                    color: {self.arrow_button_text_color};
                    min-width: 50px;
                    max-width: 50px;
                    min-height: 50px;
                    max-height: 50px;
                }}
                QPushButton:hover {{
                    background-color: rgba(255, 255, 255, 0.2);
                }}
                QPushButton:pressed {{
                    background-color: rgba(255, 255, 255, 0.3);
                }}
                """
            )
            if button_text == "↑":
                button.clicked.connect(lambda: self.navigate("up"))
            elif button_text == "↓":
                button.clicked.connect(lambda: self.navigate("down"))
            elif button_text == "←":
                button.clicked.connect(lambda: self.navigate("left"))
            elif button_text == "→":
                button.clicked.connect(lambda: self.navigate("right"))
            
            layout.addWidget(button)

    def create_select_button(self, layout):
        select_button = QPushButton("Select")
        select_button.setStyleSheet(
            f"""
            QPushButton {{
                background-color: rgba(255, 255, 255, 0.1);
                border: 1px solid gray;
                padding: 15px 30px;
                border-radius: 5px;
                color: {self.arrow_button_text_color};
                min-width: 120px;
                max-width: 120px;
                min-height: 60px;
                max-height: 60px;
                margin-bottom: 20px;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 255, 255, 0.2);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 0.3);
            }}
            """
        )
        select_button.clicked.connect(self.select_highlighted_icon)
        layout.addWidget(select_button)

    # Rest of the methods remain the same
    def create_icon_grid(self):
        icon_size = 100
        pages = ["Input", "INFO", "MAP", "Waypoints", "Weather", "Engine"]
        icons = []
        for i, page_name in enumerate(pages):
            button_widget = QWidget()
            button_widget.setObjectName("iconContainer")
            layout = QVBoxLayout(button_widget)
            layout.setAlignment(Qt.AlignCenter)
            layout.setSpacing(5)
            
            icon_label = QLabel()
            icon_path = self.get_icon_path(page_name)
            pixmap = QPixmap(icon_path).scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(pixmap)
            icon_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(icon_label)

            page_label = QLabel(page_name)
            page_label.setFont(QFont("Arial", 12, QFont.Bold))
            page_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(page_label)

            button_widget.setStyleSheet("#iconContainer { background-color: transparent; }")
            icons.append(button_widget)

            row, col = divmod(i, 3)
            self.icon_grid_layout.addWidget(button_widget, row, col)

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
