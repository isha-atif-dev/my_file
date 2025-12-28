from storage import read_expenses
from datetime import date

def main():
    program_run = True
    while program_run:
        menu_options = ["Add expense", "View expense", "Exit"]
        for index, menu in enumerate(menu_options):
            print(f'{index + 1}: {menu}')

        user_choice = int(input("Enter your choice:"))

        if user_choice == 1:

            while True:
                try:
                    amount = float(input("Enter your amount:£"))
                    if amount <= 0:
                        print("Enter amount greater than 0:")
                        continue
                    break
                except ValueError:
                    print("Enter amount in numbers!")
                    continue

            while True:
                category = input("Enter you category:")
                if category.strip() == '':
                    print("Category should not be empty!")
                    continue
                break

            user_date = input("Enter date (YYYY-MM-DD) or press Enter for today:")

            if user_date == "":
                expense_date = date.today().isoformat()
            else:
                expense_date = user_date
            
            note = input("Enter your note:")

        elif user_choice == 2:
            print(read_expenses())
        elif user_choice == 3:
            program_run = False
            print("exit")
        else:
            print("Invalid input")


main()
