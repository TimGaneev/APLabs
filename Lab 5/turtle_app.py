import img_iterator as imit
import main_window
from PyQt6 import QtWidgets, QtGui, QtCore


class TurtleApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, csv_path: str):
        super().__init__()
        self.setupUi(self)
        self.iterator = imit.PathsIterator(csv_path)
        image = QtGui.QPixmap(self.iterator.cur())
        image = image.scaled(600, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setPixmap(image)
        self.nextimage.clicked.connect(self.next_image)
        self.previmage.clicked.connect(self.prev_image)

    def next_image(self):
        image = QtGui.QPixmap(self.iterator.__next__())
        image = image.scaled(600, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setPixmap(image)

    def prev_image(self):
        image = QtGui.QPixmap(self.iterator.prev())
        image = image.scaled(600, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setPixmap(image)