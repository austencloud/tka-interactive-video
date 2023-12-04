import os
import re
from PyQt6.QtWidgets import QGridLayout, QSizePolicy, QFrame, QWidget
from custom_label import CustomLabel
from typing import Any
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QImage, QPainter, QPixmap
from PyQt6.QtCore import Qt
from custom_label import CustomLabel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import MainWindow


class PictographFrame(QFrame):
    def __init__(self, main_window: "MainWindow") -> None:
        super().__init__()
        self.main_window = main_window

        pictograph_path = "resources/D(1,0)_C(0,1)_K_Ψ-(o,1,1)/individual_pictographs"
        self.pictographs = self.load_pictographs(pictograph_path)

        grid_size = 4

        max_height = 0
        for qimage in self.pictographs:
            pixmap = QPixmap.fromImage(qimage)
            if pixmap.height() > max_height:
                max_height = pixmap.height()

        box_size = max_height
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        self.pictograph_labels = []
        for i, qimage in enumerate(self.pictographs):
            row, col = divmod(i, grid_size)
            pixmap = QPixmap.fromImage(qimage)
            img_label = CustomLabel(pixmap, self, box_size)
            grid_layout.addWidget(img_label, row, col)
            self.pictograph_labels.append(img_label)

        self.setLayout(grid_layout)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)


    def load_pictographs(self, path: str) -> list[QImage]:
        file_list = [f for f in os.listdir(path) if f.endswith(".svg")]
        file_list.sort(key=self.natural_sort_key)

        pictographs = []
        for f in file_list:
            svg_path = os.path.join(path, f)
            renderer = QSvgRenderer(svg_path)

            image = QImage(renderer.defaultSize(), QImage.Format.Format_ARGB32)
            image.fill(Qt.GlobalColor.transparent)

            painter = QPainter(image)
            renderer.render(painter)
            painter.end()

            pictographs.append(image)

        return pictographs

    def natural_sort_key(self, s) -> list[int | str | Any]:
        return [
            int(text) if text.isdigit() else text.lower()
            for text in re.split(r"(/d+)", s)
        ]


    def select_pictograph(self, label: QWidget) -> None:
        for label in self.pictograph_labels:
            label.setStyleSheet("border: none")
        label.setStyleSheet("border: 2px solid green")