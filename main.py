import grocery_logo
import reglog
from time import sleep
import cart
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" GROCERY ".center(70, "_"))
    print(f"USER ID :- {is_login}")
    print(f"~{email}")
    print("*"*70)



"""
importing grocery logo from the grocery_animation file
it is the combination of list, pause and clearing screen
~Akshay
"""

grocery_logo.print_animation()
# print the creators name
print(grocery_logo.logo)
print(
    """
**************************** WELCOME TO GROCERY APP *******************************
"""
)

"""
Registration and Login
~Areeb 
"""

email = ""
is_login = False
while not is_login:
    print(
        """
                                1==>LOGIN
                                2==>SIGNUP
        """
    )

    choice = reglog.display()
    reglog.clear_screen()
    if choice == 1:
        try:
            is_login, email = reglog.login()
        except TypeError:
            reglog.clear_screen()
            print("Unable to Login")
            continue
    elif choice == 2:
        if not reglog.register():
            reglog.clear_screen()
            print("Unable to register")
            continue
        sleep(2)
        reglog.clear_screen()
        # add a print statement to greet like great thanks for sigining up
        choice = input("\n\nDo you want to login now?(yes/no): ")
        if choice.lower() == "yes":
            reglog.clear_screen()
            try:
                is_login, email = reglog.login()
            except TypeError:
                reglog.clear_screen()
                print("Unable to Login")
                continue
        else:
            exit("Thanks for signing up")

# print(is_login, email)
# Here returning the login_id and email from the login if login is successful
"""
classifying add collecting information regarding goods (currently 100 items are available)
searching and adding grocery to cart
returning cart for billing
~ Darsh
"""
cart.menu()