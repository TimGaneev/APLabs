import argparse

import pandas as pd
import cv2
import matplotlib.pyplot as plt


def parse_arguments() -> list:
    """
    Парсинг аргументов из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_path", default="annotation.csv", type=str, help="annotation file path")
    parser.add_argument("-d", "--dtfr_path", default="dataframe.csv",  type=str, help="dataframe save path")
    parser.add_argument("-g", "--grph_path", default="graph.jpg",  type=str, help="graph save path")
    parser.add_argument("-s", "--channel", default="red",  type=str, help="red, green or blue")
    args = parser.parse_args()
    return [args.csv_path, args.dtfr_path, args.grph_path, args.channel]


def make_rgb_data(base_data: pd.DataFrame) -> pd.DataFrame:
    channels = []
    for path in base_data["Относительный путь"]:
        image = cv2.imread(path)
        avg = image.mean(axis=0).mean(axis=0)
        channels.append(avg[::-1])
    return pd.DataFrame(channels, columns=["red", "green", "blue"])


def sort_by_channel_value(data: pd.DataFrame, channel: str) -> pd.DataFrame:
    return data.sort_values(channel, ignore_index=True)


def display_channel_value_greater(data: pd.DataFrame, channel: str, value: float) -> pd.DataFrame:
    return data[data[channel]>value]


def display_channel_value_equal(data: pd.DataFrame, channel: str, value: float) -> pd.DataFrame:
    return data[data[channel]==value]


def display_channel_value_less(data: pd.DataFrame, channel: str, value: float) -> pd.DataFrame:
    return data[data[channel]<value]


def display_channels_graph(data: pd.DataFrame, save_path: str) -> None:
    data["red"].plot(color="red")
    data["blue"].plot(color="blue")
    data["green"].plot(color="green")
    plt.ylabel("Яркость канала")
    plt.legend()
    plt.savefig(save_path)
    plt.show()
    return


def main() -> None:
    try:
        annotation_path, dataframe_path, graph_path, channel = parse_arguments()
        images = pd.read_csv(annotation_path)
        channels_data = make_rgb_data(images)
        data = pd.concat([images, channels_data], axis=1)
        sorted_data = sort_by_channel_value(data, channel)
        print(sorted_data)
        data.to_csv(dataframe_path, index=False)
        display_channels_graph(sorted_data, graph_path)
    except Exception as exc:
        print(f"Возникла ошибка: {exc}")


if __name__ == "__main__":
    main()