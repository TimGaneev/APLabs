import csv


class PathsIterator:
    """
    Итератор по путям к файлам. Принимает путь к файлу аннотации как параметр конструктора
    """
    def __init__(self, path: str):
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            self.paths = [row for row in reader]
            self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.paths):
            self.count += 1
            return self.paths[self.count]
        else:
            raise StopIteration
