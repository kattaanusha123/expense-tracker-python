from modules.expense import Expense

FILE_PATH = "data/expenses.txt"

def save_expense(expense):
    with open(FILE_PATH, "a") as file:
        file.write(expense.to_file_string())

def load_expenses():
    expenses = []
    try:
        with open(FILE_PATH, "r") as file:
            for line in file:
                expenses.append(Expense.from_file_string(line))
    except FileNotFoundError:
        pass
    return expenses
