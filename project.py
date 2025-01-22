def main():
    print("Welcome to the Personal Budget Tracker!")
    budget = float(input("Enter your total budget: "))
    expenses = []

    while True:
        expense = input("Enter an expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        try:
            expenses.append(float(expense))
        except ValueError:
            print("Please enter a valid number.")

    total_expense = calculate_total_expenses(expenses)
    remaining_budget = calculate_remaining_budget(budget, total_expense)

    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

def calculate_total_expenses(expenses):
    return sum(expenses)

def calculate_remaining_budget(budget, total_expenses):
    return budget - total_expenses

def categorize_expenses(expenses):
    categories = {}
    for expense in expenses:
        category = input(f"Enter category for expense ${expense:.2f}: ")
        if category in categories:
            categories[category].append(expense)
        else:
            categories[category] = [expense]
    return categories

if __name__ == "__main__":
    main()