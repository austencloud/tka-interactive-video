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
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import MainWindow

class MainWidget(QWidget):
    def __init__(self, main_window: 'MainWindow'):
        super().__init__(main_window)

        pictograph_frame = PictographFrame(self)
        video_frame = VideoFrame(self)


        main_layout = QHBoxLayout()
        main_layout.addWidget(pictograph_frame)
        main_layout.addWidget(video_frame)
        
        self.setLayout(main_layout)

        video_controls_layout = QHBoxLayout()
        video_controls_layout.addWidget(video_frame.play_button)
        video_controls_layout.addWidget(video_frame.slider)
        video_controls_layout.addWidget(video_frame.status_bar)

        video_window_layout = QVBoxLayout()
        video_window_layout.addWidget(video_frame)
        video_window_layout.addLayout(video_controls_layout)

        video_container = QFrame()
        video_container.setLayout(video_window_layout)


