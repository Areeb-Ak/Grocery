import grocery_logo
import reglog
from time import sleep
"""
importing grocery logo from the grocery_animation file
it is the combination of list, pause and clearing screen
~Akshay
"""

grocery_logo.print_animation()
print(grocery_logo.logo)
print("""
**************************** WELCOME TO GROCERY APP *******************************
                                1==>LOGIN
                                2==>SIGNUP
                                
""")

"""
Registration and Login
~Areeb 
"""
choice = reglog.display()
reglog.clear_screen()
email = ''
is_login = False
while not is_login :
    if choice == 1:
        is_login,email = reglog.login()
    elif choice == 2:
        reglog.register()
        sleep(2)
        reglog.clear_screen()
        # add a print statement to greet like great thanks for sigining up
        choice = input("\n\nDo you want to login now?(yes/no) ")
        if choice.lower() == "yes":
            reglog.clear_screen()
            is_login, eamil = reglog.login()

print(email)