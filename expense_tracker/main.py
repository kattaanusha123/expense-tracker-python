import re
from modules.expense import Expense
from modules.file_operations import save_expense, load_expenses
from modules.category_summarizer import summarize_by_category

DATE_REGEX = r"\d{4}-\d{2}-\d{2}"

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        date = input("Enter date (YYYY-MM-DD): ")

        if not re.fullmatch(DATE_REGEX, date):
            raise ValueError("Invalid date format")

        expense = Expense(amount, category, date)
        save_expense(expense)
        print("✅ Expense added successfully!")

    except ValueError as e:
        print("❌ Error:", e)

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded.")
        return

    print("\nAmount\tCategory\tDate")
    print("-" * 30)
    for e in expenses:
        print(f"{e.amount}\t{e.category}\t{e.date}")

def summarize_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to summarize.")
        return

    summary = summarize_by_category(expenses)

    print("\n--- Expense Summary by Category ---")
    print("Category\tTotal Amount")
    print("-" * 30)
    for category, total in summary.items():
        print(f"{category}\t{total:.2f}")

def main_menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
