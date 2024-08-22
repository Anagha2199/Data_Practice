class Expense:
    def __init__(self,expense_id,date,category,description,amount):
        self.expense_id=expense_id
        self.date=date
        self.category=category
        self.description=description
        self.amount=amount
    def __str__(self):
        return(f"Expense_id = {self.expense_id}\n"
               f"Date = {self.date}\n"
               f"Category = {self.category}\n"
               f"Description = {self.description}\n"
               f"Amount = {self.amount}")

expenses = []
def add_expense(expense):
    expenses.append(expense)
    print(f"Added new expense : {expenses}")

def update_expense(expense_id,new_expense):
    for i,expense in enumerate(expenses):
        if expenses[i].expense_id == expense_id:
            expenses[i] = new_expense
            print(f"Expense with id : {expense_id} has been updated")
            return True
    print("Expense not found")

def delete_expense(expense_id):
    for i,expense in enumerate(expenses):
        if expenses[i].expense_id == expense_id:
            expenses.pop(i)
            print(f"Expense with id : {expense_id} has been removed")
            return True
    print("Expense not found")

def display_expenses():
    if not expenses:
        print("No expenses to display")
    for expense in expenses:
        print(expense)

users = {"user1" : "Welcome@1",
         "user2" : "Welcome@1"}

def authenticate_user(username,password):
    if username in users:
        if users[username] == password:
            print("Authetication Successful")
            return True
        else:
            print("Authentication Failed : Incorrect password")
            return False
def categorize_expenses():
    categories={}
    for expense in expenses:
        if expense.category not in categories:
            categories[expense.category] = 0
        categories[expense.category] += expense.amount
    return categories

def summarize_expenses():
    total = 0
    for expense in expenses:
        total+=expense.amount
    return total

def calculate_total_expenses():
    return sum(expense.amount for expense in expenses)

def generate_summary_report():
    categories = categorize_expenses()
    print("Categorized expenses : ")
    for category,amount in categories.items():
        print(f"Category : {category}, Total : {amount}")
    total = calculate_total_expenses()
    print(f"Total Expenses : {total}")

def cli():
    while True:
        print("\nExpense Tracker Menu:")
        print("\n1.Add a new expense")
        print("\n2.Update an existing expense")
        print("\n3.Delete an expense")
        print("\n4.Display all expenses")
        print("\n5.Generate a summary report")
        print("\n6.Exit")
        choice = int(input("Enter your choice"))
        if choice == 1:
            expense_id = int(input("Enter expense id : "))
            date = input("Enter date (YYYY-MM-DD) : ")
            category = input("Enter category : ")
            description = input("Enter description : ")
            amount = float(input("Enter amount : "))
            expense = Expense(expense_id,date,category,description,amount)
            add_expense(expense)
        elif choice == 2:
            expense_id = int(input("Enter the id of expense to be updated : "))
            date = input("Enter new date (YYYY-MM-DD) : ")
            category = input("Enter new category : ")
            description = input("Enter new description : ")
            amount = float(input("Enter the amount : "))
            new_expense = Expense(expense_id,date,category,description,amount)
            if update_expense(expense_id,new_expense):
                print("Expense Updated!")
            else:
                print("Expense ID not found!")
        elif choice == 3:
            expense_id = int(input("Enter the ID of the expense to delete : "))
            delete_expense(expense_id)
        elif choice == 4:
            display_expenses()
        elif choice == 5:
            generate_summary_report()
        elif choice == 6:
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    username = input("Enter username : ")
    password = input("Enter password : ")
    if authenticate_user(username,password):
        cli()

