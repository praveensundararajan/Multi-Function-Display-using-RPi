
import sys
import math
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QFrame,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QPolygon, QBrush, QPixmap
from PyQt5.QtCore import Qt, QRect, QPoint, QSize, QThread, pyqtSignal
import time
# GPIO
# import RPi.GPIO as GPIO


class SwitchMonitorThread(QThread):
    """Monitors switches and emits a signal when activated."""
    button_activated = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True
        self.switch_pins = [26, 20, 25, 19, 13, 9]  # GPIO pins for the buttons
        # self.last_button_states = [GPIO.HIGH] * len(self.switch_pins)  # Initial HIGH states
        
    # def run(self):
    #     # GPIO setup
    #     GPIO.setmode(GPIO.BCM)
    #     for pin in self.switch_pins:
    #       GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    #     while self.running:
    #         for i, pin in enumerate(self.switch_pins):
    #             button_state = GPIO.input(pin)
    #             if button_state != self.last_button_states[i]:
    #                 self.last_button_states[i] = button_state
    #                 if button_state == GPIO.LOW:  # Active low
    #                      self.button_activated.emit(i + 1)  # Emit button index (1-based)
    #                      time.sleep(0.2)


    #         time.sleep(0.1)

    # def stop(self):
    #     """Stops the thread."""
    #     self.running = False
    #     GPIO.cleanup()
    #     self.wait()

class BarGauge(QWidget):
    def __init__(
        self,
        min_val,
        max_val,
        current_val,
        title,
        is_horizontal=True,
        bar_width=10,
        height_reduction_factor=30,
        parent=None,
    ):
        super().__init__(parent)
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = current_val
        self.title = title
        self.is_horizontal = is_horizontal
        self.bar_width = bar_width
        self.height_reduction_factor = height_reduction_factor
        self.setMinimumSize(80, 40)  # Adjust as needed - Increased for title space

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        background_color = QColor(50, 50, 50)  # Dark gray
        painter.fillRect(self.rect(), background_color)

        bar_width = self.width() - 20
        bar_height = self.height() - self.height_reduction_factor  # Reduced bar height

        if not self.is_horizontal:
            bar_width, bar_height = bar_height, bar_width
        if self.is_horizontal:
            bar_rect = QRect(
                10, 25, int(bar_width), int(bar_height)
            )  # Use actual dimensions
        else:
            bar_rect = QRect(
                5, 10, int(bar_height), int(bar_width)
            )  # Use actual dimensions
        pen = QPen(Qt.white)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRect(bar_rect)

        # Calculate bar fill
        value_range = self.max_val - self.min_val
        if value_range != 0:
            normalized_val = (self.current_val - self.min_val) / value_range
        else:
            normalized_val = 0.0
        fill_length = (
            bar_width * normalized_val
            if self.is_horizontal
            else bar_height * normalized_val
        )

        # Fill the bar
        fill_color = QColor(0, 255, 0)  # Green for normal
        if (
            self.current_val < 0.2 * self.max_val
            or self.current_val > 0.8 * self.max_val
        ):
            fill_color = QColor(255, 0, 0)  # Red for extreme values
        if self.is_horizontal:
            fill_rect = QRect(10, 25, int(fill_length), int(bar_height))
        else:
            fill_rect = QRect(5, 10, int(bar_height), int(fill_length))
        painter.fillRect(fill_rect, fill_color)

        # Draw title above
        font = QFont("Arial", 8)
        painter.setFont(font)
        painter.setPen(Qt.white)
        if self.is_horizontal:
            text_rect = QRect(0, 0, self.width(), 20)
            painter.drawText(text_rect, Qt.AlignCenter, self.title)
        else:
            text_rect = QRect(self.width() - 30, 0, 30, 20)
            painter.rotate(-90)
            painter.translate(-self.height(), 0)
            painter.drawText(text_rect, Qt.AlignCenter, self.title)
            painter.resetTransform()

class HorizontalMeter(QWidget):
    def __init__(
        self,
        min_val,
        max_val,
        current_val,
        title,
        unit="m",
        bar_width=10,
        height_reduction_factor=30,
        parent=None,
    ):
        super().__init__(parent)
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = current_val
        self.title = title
        self.unit = unit
        self.bar_width = bar_width
        self.height_reduction_factor = height_reduction_factor
        self.setMinimumSize(150, 50)  # Adjust as needed

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        background_color = QColor(50, 50, 50)  # Dark gray
        painter.fillRect(self.rect(), background_color)

        bar_width = self.width() - 20
        bar_height = self.height() - self.height_reduction_factor  # Reduced bar height

        # Draw bar outline
        bar_rect = QRect(10, 25, int(bar_width), int(bar_height))
        pen = QPen(Qt.white)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRect(bar_rect)

        # Calculate bar fill
        value_range = self.max_val - self.min_val
        if value_range != 0:
            normalized_val = (self.current_val - self.min_val) / value_range
        else:
            normalized_val = 0.0
        fill_length = bar_width * normalized_val

        # Fill the bar
        fill_color = QColor(0, 255, 0)  # Green for normal
        if (
            self.current_val < 0.2 * self.max_val
            or self.current_val > 0.8 * self.max_val
        ):
            fill_color = QColor(255, 0, 0)  # Red for extreme values
        fill_rect = QRect(10, 25, int(fill_length), int(bar_height))
        painter.fillRect(fill_rect, fill_color)

        # Draw title above
        font = QFont("Arial", 8)
        painter.setFont(font)
        painter.setPen(Qt.white)
        text_rect = QRect(0, 0, self.width(), 20)
        painter.drawText(text_rect, Qt.AlignCenter, self.title + f" ({self.unit})")

        # Draw current numerical value to the left
        # text = str(self.current_val)
        # painter.setFont(QFont("Arial", 10))
        # text_rect = QRect(0, 0, 50, 20)
        # painter.drawText(text_rect, Qt.AlignLeft, text)

        # Background
        # painter.fillRect(self.rect(), QColor(50, 50, 50))

        # # Meter rectangle
        # meter_rect = QRect(10, 10, self.width() - 20, 20)
        # pen = QPen(Qt.white)
        # pen.setWidth(1)
        # painter.setPen(pen)
        # painter.drawRect(meter_rect)

        # # Calculate fill length
        # value_range = self.max_val - self.min_val
        # if value_range != 0:
        #     normalized_val = (self.current_val - self.min_val) / value_range
        # else:
        #     normalized_val = 0.0
        # fill_length = (self.width() - 20) * normalized_val

        # # Fill the bar
        # fill_color = QColor(0, 255, 0)  # Green for normal
        # if (
        #     self.current_val < 0.2 * self.max_val
        #     or self.current_val > 0.8 * self.max_val
        # ):
        #     fill_color = QColor(255, 0, 0)  # Red for extreme values
        # fill_rect = QRect(10, 10, int(fill_length), 20)
        # painter.fillRect(fill_rect, fill_color)

        # # Draw text label
        # font = QFont("Arial", 10)
        # painter.setFont(font)
        # painter.setPen(Qt.white)
        # text_rect = QRect(0, 30, self.width(), 20)
        # painter.drawText(text_rect, Qt.AlignCenter, self.title + f" ({self.unit})")
        # # Draw current numerical value
        # text = str(self.current_val)
        # painter.setFont(QFont("Arial", 10))
        # text_rect = QRect(0, 0, self.width(), 20)
        # painter.drawText(text_rect, Qt.AlignLeft, text)

class CircularGauge(QWidget):
    def __init__(self, min_val, max_val, current_val, title, unit="", parent=None):
        super().__init__(parent)
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = current_val
        self.title = title
        self.unit = unit
        self.setMinimumSize(100, 100)  # Adjust as needed

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2
        radius = min(center_x, center_y) * 0.8  # Reduce radius a bit
        # Conversion to int added
        dial_rect = QRect(
            int(center_x - radius),
            int(center_y - radius),
            int(2 * radius),
            int(2 * radius),
        )

        # Draw dial outline
        pen = QPen(Qt.white)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawArc(
            dial_rect, 150 * 16, 240 * 16
        )  # Adjust start and span as needed

        # Calculate current angle based on value
        angle_range = 240  # Adjust as needed
        value_range = self.max_val - self.min_val
        if value_range != 0:
            normalized_val = (self.current_val - self.min_val) / value_range
        else:
            normalized_val = 0.0
        angle = 150 + (normalized_val * angle_range)  # Start angle is 150 degrees

        # Draw needle
        needle_length = radius * 0.7
        needle_start = QPoint(int(center_x), int(center_y))
        needle_end_x = center_x + needle_length * 0.8 * (angle_range + 150 - angle)
        needle_end_y = center_y - needle_length * 0.8 * (angle_range + 150 - angle)
        needle_end = QPoint(
            int(center_x + needle_length * (angle_range + 150 - angle) / 200),
            int(center_y - needle_length * (angle_range + 150 - angle) / 200),
        )
        pen = QPen(Qt.white)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawLine(needle_start, needle_end)

        # Draw text label
        font = QFont("Arial", 10)
        painter.setFont(font)
        painter.setPen(Qt.white)
        text_rect = QRect(
            0, self.height() - 20, self.width(), 20
        )  # Position it beneath
        painter.drawText(text_rect, Qt.AlignCenter, self.title + f" ({self.unit})")

        # Draw numerical value (below dial)
        text = str(self.current_val)
        painter.setFont(QFont("Arial", 10))
        text_rect = QRect(0, int(center_y + radius + 15), self.width(), 20)
        painter.drawText(text_rect, Qt.AlignCenter, text)


class LargeNumberDisplay(QWidget):
    def __init__(self, value, unit, title, parent=None):
        super().__init__(parent)
        self.value = value
        self.unit = unit
        self.title = title
        self.setMinimumSize(100, 50)  # Adjust as needed

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw title
        font = QFont("Arial", 10)
        painter.setFont(font)
        painter.setPen(Qt.black)
        title_rect = QRect(0, 0, self.width(), 20)
        painter.drawText(title_rect, Qt.AlignCenter, self.title)
        # Draw numerical value
        font = QFont("Arial", 25, QFont.Bold)
        painter.setFont(font)
        num_rect = QRect(0, 20, self.width(), 35)
        painter.drawText(num_rect, Qt.AlignCenter, f"{self.value}")
        # draw unit
        font = QFont("Arial", 12)
        painter.setFont(font)
        unit_rect = QRect(0, 30, self.width() - 20, 20)
        painter.drawText(unit_rect, Qt.AlignRight, f"{self.unit}")


class LabeledValueDisplay(QWidget):
    def __init__(self, label_text, value_text, parent=None):
        super().__init__(parent)
        self.label_text = label_text
        self.value_text = value_text
        self.setMinimumSize(100, 50)  # Adjust this as needed

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Set font and color for text
        font = QFont("Arial", 10)
        painter.setFont(font)
        painter.setPen(Qt.white)

        # Draw label text
        label_rect = QRect(0, 0, self.width(), 20)
        painter.drawText(label_rect, Qt.AlignLeft, self.label_text)

        # Draw value text
        value_rect = QRect(0, 20, self.width(), 20)
        painter.drawText(value_rect, Qt.AlignLeft, self.value_text)


class InstrumentPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instrument Panel")
        self.setStyleSheet("background-color: black;")
        
        # Load the background image. Replace 'background.png' with your image file path
        self.background_image = QPixmap("images/bg.png")  # Add image file name.

        # Initialize different page values
        self.page_values = {
            1: {  # Default/Page 1 values
                "power": 90,
                "rpm": 2640,
                "man_hg": 27.0,
                "fflow_gph": 16.7,
                "oil": 192,
                "fuel_flows": [50, 70, 30, 90],
                "oil_pressure": 75,
                "power_gauge": 60,
                "rpm_meter": 180,
                "engine_temp": 125,
            },
            2: {  # Page 2 values
                "power": 85,
                "rpm": 2500,
                "man_hg": 25.0,
                "fflow_gph": 15.5,
                "oil": 185,
                "fuel_flows": [45, 65, 35, 85],
                "oil_pressure": 70,
                "power_gauge": 55,
                "rpm_meter": 170,
                "engine_temp": 120,
            },
            3: {  # Page 3 values
                "power": 95,
                "rpm": 2800,
                "man_hg": 29.0,
                "fflow_gph": 18.0,
                "oil": 198,
                "fuel_flows": [55, 75, 40, 95],
                "oil_pressure": 80,
                "power_gauge": 65,
                "rpm_meter": 190,
                "engine_temp": 130,
            },
            4: {  # Page 4 values
                "power": 80,
                "rpm": 2300,
                "man_hg": 23.0,
                "fflow_gph": 14.0,
                "oil": 180,
                "fuel_flows": [40, 60, 25, 80],
                "oil_pressure": 65,
                "power_gauge": 50,
                "rpm_meter": 160,
                "engine_temp": 115,
            },
             5: { # Page 5 values (for button 5)
                "power": 70,
                "rpm": 2000,
                "man_hg": 22.0,
                "fflow_gph": 12.0,
                "oil": 170,
                "fuel_flows": [30, 50, 20, 70],
                 "oil_pressure": 60,
                "power_gauge": 45,
                "rpm_meter": 150,
                "engine_temp": 105,

            },
              6: { # Page 6 values (for button 6)
                "power": 90,
                "rpm": 2900,
                "man_hg": 30.0,
                "fflow_gph": 20.0,
                "oil": 200,
                "fuel_flows": [60, 80, 50, 100],
                "oil_pressure": 85,
                "power_gauge": 70,
                "rpm_meter": 200,
                "engine_temp": 135,
            },
        }

        self.current_page = 1
        self.nav_buttons = []
        self.initializeGauges()
        self.initUI()
        self.update_button_highlight() #Highlight first button on startup
    
        # Create and start the switch monitoring thread
        self.switch_thread = SwitchMonitorThread()
        self.switch_thread.button_activated.connect(self.on_button_activated)
        self.switch_thread.start()
    
    def on_button_activated(self, button_index):
        """Switch page when a button is activated.

        Args:
            button_index: The button index (1 to 6) that was activated.
        """
        if 1 <= button_index <= 6: #Allow all buttons to update pages
           self.switchPage(button_index)
        print(f"Button {button_index} activated")
            
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw the background image (scaled to widget size)
        if not self.background_image.isNull():
            scaled_background = self.background_image.scaled(
                self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
            painter.drawPixmap(self.rect(), scaled_background)
        
        # Let other widgets paint over the background
        super().paintEvent(event)


    def initializeGauges(self):
        # Initialize with page 1 values
        vals = self.page_values[1]

        self.fuel_flow_1 = BarGauge(
            0,
            100,
            vals["fuel_flows"][0],
            "Fuel Flow 1",
            bar_width=5,
            height_reduction_factor=10,
        )
        self.fuel_flow_2 = BarGauge(
            0,
            100,
            vals["fuel_flows"][1],
            "Fuel Flow 2",
            bar_width=5,
            height_reduction_factor=10,
        )
        self.fuel_flow_3 = BarGauge(
            0,
            100,
            vals["fuel_flows"][2],
            "Fuel Flow 3",
            bar_width=5,
            height_reduction_factor=10,
        )
        self.fuel_flow_4 = BarGauge(
            0,
            100,
            vals["fuel_flows"][3],
            "Fuel Flow 4",
            bar_width=5,
            height_reduction_factor=10,
        )

        self.oil_pressure_gauge = BarGauge(
            0,
            150,
            vals["oil_pressure"],
            "Oil Pressure",
            True,
            bar_width=5,
            height_reduction_factor=10,
        )
        self.power_gauge = BarGauge(
            0,
            100,
            vals["power_gauge"],
            "Power",
            True,
            bar_width=5,
            height_reduction_factor=10,
        )
        self.rpm_meter = HorizontalMeter(
            0,
            360,
            vals["rpm_meter"],
            "RPM",
            "deg",
            bar_width=5,
            height_reduction_factor=10,
        )
        self.engine_temp_gauge = BarGauge(
            0,
            250,
            vals["engine_temp"],
            "Engine Temp",
            True,
            bar_width=5,
            height_reduction_factor=10,
        )

        self.power_display = LargeNumberDisplay(vals["power"], "%", "% Power")
        self.rpm_display = LargeNumberDisplay(vals["rpm"], "x100", "RPM")
        self.man_hg_display = LargeNumberDisplay(vals["man_hg"], "Man Hg", "Man Hg")
        self.fflow_gph_display = LargeNumberDisplay(
            vals["fflow_gph"], "GPH", "FFlow GPH"
        )
        self.oil_display = LargeNumberDisplay(vals["oil"], "Â°F", "Oil")

        # Initialize other displays
        # self.cht_display = LabeledValueDisplay("CHT Â°F", "352.340")
        # self.egt_display = LabeledValueDisplay("EGT Â°F", "1335.1274")
        # self.current_display = LabeledValueDisplay("Current (A)", "Alt1 Alt2 Batt1")
        # self.bus_volts_display = LabeledValueDisplay("Bus Volts (V)", "Ess M1 M2")
        # self.fuel_qty_bar = BarGauge(
        #     0, 100, 60, "Fuel Qty", True, bar_width=5, height_reduction_factor=10
        # )
        self.air_data_1_bar = BarGauge(
            0, 100, 60, "", True, bar_width=5, height_reduction_factor=10
        )
        self.air_data_2_bar = BarGauge(
            0, 100, 60, "", True, bar_width=5, height_reduction_factor=10
        )

        self.fuel_calc_label = QLabel(
            "Fuel Calculation:\nUsed 0.0 GAL\nRem 40.0 GAL\nTime Rem 03+19 (H+MM)\nRange 427 NM\nEcon 9.2 NMPG"
        )
        # self.heading_display = LabeledValueDisplay("Heading:", "164")
        # self.text_display = LabeledValueDisplay("Text:", "Some Text")
        pass

    def createNavigationButtons(self):
        nav_layout = QVBoxLayout()

        button_style = """
            QPushButton {
                background-color: #404040;
                color: white;
                border: 1px solid #606060;
                border-radius: 3px;
                padding: 3px;
                min-width: 70px;
                max-width: 70px;
                min-height: 40px;
                max-height: 40px;
                margin: 2px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QPushButton:pressed {
                background-color: #303030;
            }
        """

        # Create 6 buttons with spacers
        for i in range(4):
            btn = QPushButton(f"ENG {i+1}")
            btn.setStyleSheet(button_style)
            btn.setCheckable(True)
            if i == 0:
                btn.setChecked(True)
            # Remove old button connections (signals handled by GPIO)
            nav_layout.addWidget(btn)
            self.nav_buttons.append(btn) # Store button to the list
            if i < 3:  # Add spacer after each button except the last one
                nav_layout.addItem(
                    QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
                )

        return nav_layout

    def switchPage(self, page_num):
        if page_num not in self.page_values:
            return

        self.current_page = page_num
        vals = self.page_values[page_num]
        # Update all displays with new values
        self.power_display.value = vals["power"]
        self.rpm_display.value = vals["rpm"]
        self.man_hg_display.value = vals["man_hg"]
        self.fflow_gph_display.value = vals["fflow_gph"]
        self.oil_display.value = vals["oil"]

        self.fuel_flow_1.current_val = vals["fuel_flows"][0]
        self.fuel_flow_2.current_val = vals["fuel_flows"][1]
        self.fuel_flow_3.current_val = vals["fuel_flows"][2]
        self.fuel_flow_4.current_val = vals["fuel_flows"][3]

        self.oil_pressure_gauge.current_val = vals["oil_pressure"]
        self.power_gauge.current_val = vals["power_gauge"]
        self.rpm_meter.current_val = vals["rpm_meter"]
        self.engine_temp_gauge.current_val = vals["engine_temp"]

        self.update_button_highlight()
        # Trigger repaint
        self.update()
        pass
        
    def update_button_highlight(self):
      for i, button in enumerate(self.nav_buttons):
          if i+1 == self.current_page:
             button.setStyleSheet("""
                QPushButton {
                    background-color: #606060;
                    color: yellow;
                    border: 1px solid #808080;
                    border-radius: 3px;
                    padding: 3px;
                    min-width: 70px;
                    max-width: 70px;
                    min-height: 40px;
                    max-height: 40px;
                    margin: 2px;
                    font-size: 12px;
                }
                 QPushButton:hover {
                    background-color: #505050;
                }
                QPushButton:pressed {
                    background-color: #303030;
                }
             """)
          else:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #404040;
                    color: white;
                    border: 1px solid #606060;
                    border-radius: 3px;
                    padding: 3px;
                    min-width: 70px;
                    max-width: 70px;
                    min-height: 40px;
                    max-height: 40px;
                    margin: 2px;
                    font-size: 12px;
                }
                 QPushButton:hover {
                    background-color: #505050;
                }
                QPushButton:pressed {
                    background-color: #303030;
                }
             """)

    def initUI(self):
        main_layout = QHBoxLayout()

        # Left navigation buttons
        left_nav_buttons = self.createNavigationButtons()
        main_layout.addLayout(left_nav_buttons)

        # Instrument grid layout
        instrument_layout = QGridLayout()

        instrument_layout.setVerticalSpacing(80)  # Adjust spacing as needed
        instrument_layout.setHorizontalSpacing(50)  # Adjust the spacing as needed

        instrument_layout.setColumnStretch(0, 1)  # Left column (for navigation buttons)
        instrument_layout.setColumnStretch(1, 2)  # Fuel flow columns
        instrument_layout.setColumnStretch(2, 2)  # Fuel flow columns
        instrument_layout.setColumnStretch(3, 2)  # Gauges columns
        instrument_layout.setColumnStretch(4, 2)
        instrument_layout.setColumnStretch(5, 1)

        # Set the row stretch factors so that bars are centered vertically
        instrument_layout.setRowStretch(0, 1)  # Row 0 (empty row before fuel flow) - low stretch
        instrument_layout.setRowStretch(1, 3)  # Row 1 (fuel_flow_1) - higher stretch
        instrument_layout.setRowStretch(2, 3)  # Row 2 (fuel_flow_2) - higher stretch
        instrument_layout.setRowStretch(3, 3)  # Row 3 (fuel_flow_3) - higher stretch
        instrument_layout.setRowStretch(4, 3)  # Row 4 (fuel_flow_4) - higher stretch

        # You can also set minimum heights for each row to ensure bars stay centered
        instrument_layout.setRowMinimumHeight(1, 100)  # Fuel flow bars height
        instrument_layout.setRowMinimumHeight(2, 100)
        instrument_layout.setRowMinimumHeight(3, 100)
        instrument_layout.setRowMinimumHeight(4, 100)

        instrument_layout.setRowMinimumHeight(5, 100)  # Other gauges height
        instrument_layout.setRowMinimumHeight(6, 100)
        instrument_layout.setRowMinimumHeight(7, 100)
        instrument_layout.setRowMinimumHeight(8, 100)
        
        # Adjust the height of the fuel flow bars and other gauges
        self.fuel_flow_1.setFixedHeight(90)  # Reduce height of the fuel flow bars
        self.fuel_flow_2.setFixedHeight(90)
        self.fuel_flow_3.setFixedHeight(90)
        self.fuel_flow_4.setFixedHeight(90)

        self.oil_pressure_gauge.setFixedHeight(90)  # Reduce height of the gauges
        self.power_gauge.setFixedHeight(90)
        self.rpm_meter.setFixedHeight(90)
        self.engine_temp_gauge.setFixedHeight(90)

        # Add a blank row above the instruments to move them down
        instrument_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0, 1, 6)

        # Add all instruments to the grid (same as before)
        instrument_layout.addWidget(self.power_display, 0, 0, 1, 1)
        instrument_layout.addWidget(self.rpm_display, 0, 1, 1, 1)
        instrument_layout.addWidget(self.man_hg_display, 0, 2, 1, 1)
        instrument_layout.addWidget(self.fflow_gph_display, 0, 3, 1, 1)
        instrument_layout.addWidget(self.oil_display, 0, 4, 1, 1)

        instrument_layout.addWidget(self.fuel_flow_1, 2, 1, 1, 2)
        instrument_layout.addWidget(self.fuel_flow_2, 3, 1, 1, 2)
        instrument_layout.addWidget(self.fuel_flow_3, 4, 1, 1, 2)
        instrument_layout.addWidget(self.fuel_flow_4, 5, 1, 1, 2)

        instrument_layout.addWidget(self.oil_pressure_gauge, 2, 3, 1, 2)
        instrument_layout.addWidget(self.power_gauge, 3, 3, 1, 2)
        instrument_layout.addWidget(self.rpm_meter, 4, 3, 1, 2)
        instrument_layout.addWidget(self.engine_temp_gauge, 5, 3, 1, 2)

        # instrument_layout.addWidget(self.oil_pressure_gauge, 5, 1, 1, 2)
        # instrument_layout.addWidget(self.power_gauge, 6, 1, 1, 2)
        # instrument_layout.addWidget(self.rpm_meter, 7, 1, 1, 2)
        # instrument_layout.addWidget(self.engine_temp_gauge, 8, 1, 1, 2)

        # instrument_layout.addWidget(self.cht_display, 2, 3, 1, 1)
        # instrument_layout.addWidget(self.egt_display, 2, 4, 1, 1)
        # instrument_layout.addWidget(self.current_display, 3, 3, 1, 1)
        # instrument_layout.addWidget(self.bus_volts_display, 3, 4, 1, 1)
        # instrument_layout.addWidget(self.fuel_qty_bar, 4, 3, 1, 4)
        # instrument_layout.addWidget(QLabel("F"), 4, 3, 1, 1, alignment=Qt.AlignRight)
        # instrument_layout.addWidget(
            # QLabel("L  R GAL"), 4, 6, 1, 1, alignment=Qt.AlignLeft
        # )

        # instrument_layout.addWidget(self.air_data_1_bar, 5, 3, 1, 2)
        # instrument_layout.addWidget(self.air_data_2_bar, 5, 5, 1, 2)
        # instrument_layout.addWidget(
        #     QLabel("Air Data"), 6, 3, 1, 4, alignment=Qt.AlignCenter
        # )

        # instrument_layout.addWidget(self.fuel_calc_label, 7, 3, 1, 4)

        # instrument_layout.addWidget(self.heading_display, 8, 3, 1, 2)
        # instrument_layout.addWidget(self.text_display, 8, 5, 1, 2)

        # Add instrument layout to main layout
        main_layout.addLayout(instrument_layout)

        # Right navigation buttons
        right_nav_buttons = self.createNavigationButtons()
        main_layout.addLayout(right_nav_buttons)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    panel = InstrumentPanel()
    panel.show()
    sys.exit(app.exec_())
