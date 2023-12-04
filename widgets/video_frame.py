from PyQt6.QtWidgets import (
    QSlider,
    QPushButton,
    QLabel,
    QSizePolicy,
    QStyle,
)
from PyQt6.QtCore import Qt, QUrl, QSize, QSize
from PyQt6.QtMultimedia import QMediaPlayer, QMediaMetaData
from PyQt6.QtMultimediaWidgets import QVideoWidget

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import MainWindow


class VideoFrame(QVideoWidget):
    def __init__(self, main_window: "MainWindow") -> None:
        super().__init__()
        self.main_window = main_window
        video_path = "resources/D(1,0)_C(0,1)_K_Ψ-(o,1,1).mp4"
        video_size = QSize(800, 600)
        self.media_player: QMediaPlayer = QMediaPlayer()

        # Get the video sink from QVideoWidget and set it as the video output
        video_sink = self.videoSink()
        self.media_player.setVideoSink(video_sink)

        self.slider: QSlider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.status_bar: QLabel = QLabel()
        self.status_bar.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )

        self.play_button: QPushButton = QPushButton()
        self.play_button.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        )
        self.play_button.clicked.connect(self.play)

        self.media_player.setSource(QUrl.fromLocalFile(video_path))

        self.media_player.playbackStateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.errorOccurred.connect(self.handle_error)

        self.media_player.hasVideoChanged.connect(self.update_video_size)
        self.update_video_size(video_size)

    def update_video_size(self, grid_height: int) -> None:
        if self.media_player.hasVideo():
            self.adjust_video_widget_size(grid_height)

    def adjust_video_widget_size(self, grid_height: int) -> None:
        metadata = self.media_player.metaData()
        video_size: QSize = metadata.value(QMediaMetaData.Key.Resolution)
        if video_size and video_size.isValid():
            aspect_ratio = video_size.width() / video_size.height()
            self.setFixedWidth(int(grid_height * aspect_ratio))
            self.setFixedHeight(grid_height)

    def play(self) -> None:
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def media_state_changed(self, state: QMediaPlayer.PlaybackState) -> None:
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.play_button.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
            )
        else:
            self.play_button.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
            )

    def position_changed(self, position: int) -> None:
        self.slider.setValue(position)

    def set_position(self, position: int) -> None:
        self.media_player.setPosition(position)

    def duration_changed(self, duration: int) -> None:
        self.slider.setRange(0, duration)

    def handle_error(self) -> None:
        self.status_bar.setText("Error: " + self.media_player.errorString())
