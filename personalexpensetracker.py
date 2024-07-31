from datetime import datetime

expenses = []

def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({"amount": amount, "category": category, "date": date})

def view_expenses():
    for expense in expenses:
        print(f"{expense['date']}: ${expense['amount']} on {expense['category']}")

def expenses_by_category(category):
    total = sum(exp['amount'] for exp in expenses if exp['category'] == category)
    print(f"Total spent on {category}: ${total}")

while True:
    print("\nOptions: add, view, category, exit")
    choice = input("Choose an option: ").strip().lower()
    if choice == 'add':
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        add_expense(amount, category)
    elif choice == 'view':
        view_expenses()
    elif choice == 'category':
        category = input("Enter the category: ")
        expenses_by_category(category)
    elif choice == 'exit':
        break
    else:
        print("Invalid choice, try again.")
