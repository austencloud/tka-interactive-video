import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QApplication,
    QFrame,
)


from custom_label import CustomLabel
from widgets.video_frame import VideoFrame
from widgets.pictograph_frame import PictographFrame
from widgets.main_widget import MainWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("TKA Interactive Video Player (v0.1.0-alpha)")
        self.setFixedSize(800, 600) 
    
        self.configure_window()
        self.init_main_window()

    def configure_window(self) -> None:
        screens = QApplication.screens()
        if len(screens) > 1:
            screen = screens[1]  # Use the second screen if available
        else:
            screen = QApplication.primaryScreen()

        screen_geometry = screen.geometry()

        # Adjust size based on the screen used
        self.main_window_width = int(screen_geometry.width() * 0.9)
        self.main_window_height = int(screen_geometry.height() * 0.8)

        # Positionsing the window
        self.move(
            screen_geometry.x()
            + (screen_geometry.width() - self.main_window_width) // 2
            - 50,
            screen_geometry.y()
            + (screen_geometry.height() - self.main_window_height) // 2
            - 50,
        )

    def init_main_window(self) -> None:
        self.setMinimumSize(self.main_window_width, self.main_window_height)
        self.main_widget = MainWidget(self)
        self.installEventFilter(self.main_widget)
        self.setCentralWidget(self.main_widget)
        self.show()


def main() -> None:
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.setFocus()
    exit_code = app.exec()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
