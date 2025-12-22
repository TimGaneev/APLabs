import img_iterator as imit
import main_window
from PyQt6 import QtWidgets, QtGui


class TurtleApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, csv_path: str):
        super().__init__()
        self.setupUi(self)
        self.iterator = imit.PathsIterator(csv_path)
        self.image.setPixmap(QtGui.QPixmap(self.iterator.cur()))
        self.nextimage.clicked.connect(self.next_image)
        self.previmage.clicked.connect(self.prev_image)

    def next_image(self):
        self.image.setPixmap(QtGui.QPixmap(self.iterator.__next__()))

    def prev_image(self):
        self.image.setPixmap(QtGui.QPixmap(self.iterator.prev()))