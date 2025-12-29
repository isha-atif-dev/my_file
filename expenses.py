

def display_expenses(expenses):
    if not expenses:
        print("You don't have any expenses yet!")
    else:
        for expense in expenses:
            print(f"ID: {expense['id']} | DATE: {expense['date']} | Amount: £{expense['amount']} | Category: {expense['category']} | Note: {expense['note']}")
