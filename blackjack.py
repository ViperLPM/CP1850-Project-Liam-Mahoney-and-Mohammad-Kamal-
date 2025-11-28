import csv


def read_money_file():
    with open("money.csv", newline="") as file:
        reader= csv.reader(file)
        for row in reader:
            current_money=float(row[1])

    return current_money

def write_money_file(current_money):
    with open("money.csv", "w", newline="") as file:
        writer=csv.writer(file)
        new_balance= round(current_money, 2)
        writer.writerow(["Money", new_balance])



def main():
    read_money_file()
    user_input=int(input("Enter amount: "))
    write_money_file(user_input)

if __name__=="__main__":
    main()










