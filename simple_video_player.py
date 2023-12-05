import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget


class VideoPlayerWindow(QMainWindow):
    def __init__(self, video_path) -> None:
        super().__init__()

        self.setWindowTitle("Video Player")

        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()

        video_sink = self.video_widget.videoSink()
        self.media_player.setVideoSink(video_sink)

        self.media_player.setSource(QUrl.fromLocalFile(video_path))

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.video_widget.setMinimumSize(800, 600)
        self.media_player.play()


def main() -> None:
    app = QApplication(sys.argv)

    video_path = "resources/D(1,0)_C(0,1)_K_Ψ-(o,1,1).mp4"

    main_window = VideoPlayerWindow(video_path)
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
