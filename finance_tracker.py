# Cognizant Capstone Finance Tracker
## This is a project to showcase a culmination of basic python skills to create a finance tracker
## This project will incorporate different variables, data types, functions, loops, and other key programming basics
def add_expense(data):
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Expense description cannot be empty.")

        category = input("Enter expense category: ").strip()
        if not category:
            raise ValueError("Expense category cannot be empty.")

        amount_input = input("Enter expense amount: ").strip()
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")

    except ValueError as e:
        print(f'Invalid input: {e}')
        return

    if category not in data:
        data[category] = []

    data[category].append((description, amount))
    print("expense added successfully! :)")

def view_expenses(data):
    if not data:
        print("No expenses to display yet.")
        return

    for category, expenses in data.items():
        print(f'\nCategory: {category}')
        for description, amount in expenses:
              print(f'  - {description}: ${amount:.2f}')

def view_summary(data):
    if not data:
        print("No expenses to summarize yet.")
        return

    print(f"\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f'{category}: ${total:.2f}')

def show_menu():
    print("\nMenu:")
    print("What would you like to do?")
    print("1. Enter an expense")
    print("2. View all expenses")
    print("3. View expense summary")
    print("4. Exit")

def finance_tracker():
    print("Welcome to the Personal Financial Tracker!")

    data = {}

    while True: ## creating the menu to select from and loop to keep the program running till exited
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()  ## enter the choice from the menu

        if choice == '1':  ## if choice is 1 it
            add_expense(data)

        elif choice == '2':  ## if choice is 2 it
            view_expenses(data)

        elif choice == '3':  ## if Choice is 3 it
            view_summary(data)

        elif choice == '4':  ## if a user wants to leave it exits them from the program
            print("Goodbye!")
            break  ## breaks the loop

        else:  ## makes sure the initial choice is between 1 and 4
            print("Invalid choice. Please enter 1-4.")

finance_tracker()