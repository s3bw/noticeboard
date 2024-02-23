import csv


def read_csv(path, cls):

    data = []
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        data = [cls(**row) for row in reader]

    return data
