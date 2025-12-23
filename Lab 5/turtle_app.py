import os

import img_iterator as imit
import main_window
from PyQt6 import QtWidgets, QtGui, QtCore


class TurtleApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, csv_path: str):
        super().__init__()
        self.setupUi(self)
        self.iterator = imit.PathsIterator(csv_path)
        self.set_image(self.iterator.cur())

        self.nextimage.clicked.connect(self.next_image)
        self.previmage.clicked.connect(self.prev_image)
        self.choosecsv.clicked.connect(self.choose_csv)

    def set_image(self, img: str):
        image = QtGui.QPixmap(img)
        image = image.scaled(600, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setPixmap(image)

    def choose_csv(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл аннотации")[0]
        if file.endswith(".csv"):
            self.iterator = imit.PathsIterator(file)
            self.set_image(self.iterator.cur())

    def next_image(self):
        self.set_image(self.iterator.__next__())

    def prev_image(self):
        self.set_image(self.iterator.prev())