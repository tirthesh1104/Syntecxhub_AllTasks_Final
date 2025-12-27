import csv
from datetime import datetime

FILE = "expenses.csv"

def add_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Category: ")
    amount = float(input("Amount: "))
    type = input("Type (income/expense): ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, type])

def summary():
    income = expense = 0
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[3] == "income":
                    income += float(row[2])
                else:
                    expense += float(row[2])
    except FileNotFoundError:
        pass

    print("Income:", income)
    print("Expense:", expense)
    print("Balance:", income - expense)

while True:
    print("1.Add Entry  2.View Summary  3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_entry()
    elif ch == "2":
        summary()
    else:
        break
