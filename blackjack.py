import csv


def read_money_file():
    with open("money.csv", newline="") as file:
        reader= csv.reader(file)
        for row in reader:
            current_money=float(row[1])

    return current_money










