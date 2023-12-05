from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from overlay import Overlay
from PyQt6.QtGui import QPixmap

class CustomLabel(QWidget):
    def __init__(self, pixmap: QPixmap, main_window, box_size) -> None:
        super().__init__()
        self.main_window = main_window
        self.original_pixmap = pixmap
        self.label = QLabel(self)
        self.label.setPixmap(
            pixmap.scaled(
                box_size,
                box_size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.label.setFixedSize(box_size, box_size)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        self.setFixedSize(box_size, box_size)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: white;")
        self.overlay = Overlay(self)
        self.overlay.setGeometry(0, 0, box_size, box_size)
        self.overlay.hide()

    def enterEvent(self, event) -> None:
        self.show_overlay()

    def leaveEvent(self, event) -> None:
        self.hide_overlay()

    def show_overlay(self) -> None:
        self.overlay.show()

    def hide_overlay(self) -> None:
        self.overlay.hide()
