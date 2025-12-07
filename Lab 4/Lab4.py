import csv

import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt


def make_rgb_data(base_data):
    channels = []
    for path in base_data["Относительный путь"]:
        image = cv2.imread(path)
        avg = image.mean(axis=0).mean(axis=0)
        channels.append(avg)
    return pd.DataFrame(channels, columns=["blue", "green", "red"])


def main() -> None:
    try:
        images = pd.read_csv("annotation.csv")
        channels_data = make_rgb_data(images)
        data = pd.concat([images, channels_data], axis=1)
        print(data)
    except Exception as exc:
        print(f"Возникла ошибка: {exc}")


if __name__ == "__main__":
    main()