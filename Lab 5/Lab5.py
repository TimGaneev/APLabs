import argparse
import sys

import turtle_app
from PyQt6 import QtWidgets


def parse_arguments() -> str:
    """
    Парсинг аргументов из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_path", default="annotation.csv", type=str, help="annotation file path")
    args = parser.parse_args()
    return args.csv_path


def main() -> None:
    try:
        annotation_path = parse_arguments()
        app = QtWidgets.QApplication(sys.argv)
        window = turtle_app.TurtleApp(annotation_path)
        window.show()
        app.exec()
    except Exception as exc:
        print(f"Возникла ошибка: {exc}")


if __name__ == "__main__":
    main()