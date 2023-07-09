import json

import grocery_logo
import reglog
from time import sleep
import cart
import billing
import csv

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

x = open("temp.txt", 'w')
x.write(is_login)
x.write('\n')
x.write(email)
x.close()

# print(is_login, email)
# Here returning the login_id and email from the login if login is successful
f = open("cart.csv", "w")
f.close()
"""
classifying add collecting information regarding goods (currently 100 items are available)
searching and adding grocery to cart
returning cart for billing
~ Darsh
"""
cart.menu()

"""
accessing data from cart and representing it in a bill
generating a uniques order number consisting of date and time and the order id 
~Akshay
"""

payment_type = 'cash'


def payment(amount):
    pass


def add_to_successful_orders():
    fp = open("cart.csv", 'r')
    order_items = csv.DictReader(fp, ["item_id", 'category', 'sub_cat', "item_name", 'type', 'cost', "quantity"])
    fp.close()

    order_details = ()
    for item in order_items:
        order_details += ((item['item_id'], item['cost'], item['quantity']))
    temp = {'order_id': billing.order_id,
            'order_details': order_details,
            'total_price': billing.total_price,
            'payment_type': payment_type}

    fp = open('successful_orders.json', 'a')
    json.dump(temp, fp)


if billing.conform_order():
    if payment(billing.total_price):
        cart.clear_screen()
        print("Thank you !")
        billing.generate_bill()
        add_to_successful_orders()
    else:
        print('COME BACK AGAIN ')
