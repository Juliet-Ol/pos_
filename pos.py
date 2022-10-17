from customer import customer_menu
from product import product_menu
from purchase import purchase_menu


def main_menu():
    print('*' *49)
    print(f"\t\t Welcome to bright Shop".title())
    print('*' *49)
    print(f"\tThis is the main menu")
    print('*' *49)
    while True:
        print(""" press this code to go to the particular menu: 
        press 1 - Customer menu , 
        press 2 - Product menu, 
        press 3 - Purchase menu""")

        short_code = input()

        if short_code == "1":
            customer_menu()

        elif short_code == "2":
            product_menu() 

        elif short_code == "3":
            purchase_menu() 

        elif short_code == "4":
            ("back to main menu")

        else:
            print("you entered wrong code")             


if __name__ == "__main__":

    main_menu()              