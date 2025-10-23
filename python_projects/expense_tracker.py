import csv
import os

FILE_NAME = "expenses.csv"

# Create the file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport, Entertainment): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!\n")

def view_expenses():
    total = 0
    print("\nAll Expenses:\n")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"Date: {row[0]} | Category: {row[1]} | Desc: {row[2]} | Amount: ₱{row[3]}")
            total += float(row[3])
    print(f"\nTotal Spent: ₱{total:.2f}\n")

def category_summary():
    categories = {}
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[3])
            categories[category] = categories.get(category, 0) + amount

    print("\nExpenses by Category:\n")
    for cat, amt in categories.items():
        print(f"{cat}: ₱{amt:.2f}")
    print()

def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()