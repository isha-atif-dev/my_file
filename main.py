from storage import read_expenses


def main():
    program_run = True
    while program_run:
        menu_options = ["Add expense", "View expense", "Exit"]
        for index, menu in enumerate(menu_options):
            print(f'{index + 1}: {menu}')
        
        user_choice = int(input("Enter your choice:"))

        if user_choice == 1:
            amount = float(input("Enter your amount:£"))
            category = input("Enter you category:")
            date = input("Press enter for today!")
            note = input("Enter your note:")
            
        elif user_choice == 2:
            print(read_expenses())
        elif user_choice == 3:
            program_run = False
            print("exit")
        else:
            print("Invalid input")


main()
