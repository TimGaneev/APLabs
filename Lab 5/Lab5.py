import argparse
import sys

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import main_window
import img_iterator
from PyQt6 import QtWidgets


class MyApp(QtWidgets.QMainWindow, main_window.Ui_Form):
    def __init__(self):
        self.choosecsv.clicked.connect(self.choose_annotation)
        super().__init__()
        self.setupUi(self)
    def choose_annotation(self):
        


def parse_arguments() -> list:
    """
    Парсинг аргументов из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_path", default="annotation.csv", type=str, help="annotation file path")
    args = parser.parse_args()
    return [args.csv_path]


def main() -> None:
    try:
        annotation_path = parse_arguments()
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        app.exec()
    except Exception as exc:
        print(f"Возникла ошибка: {exc}")


if __name__ == "__main__":
    main()