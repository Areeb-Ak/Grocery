import csv
import sys
import os
import emoji
from pyfiglet import Figlet
from time import sleep

cart = []
figlet = Figlet()

with open('temp.txt', 'r') as f:
    data = f.readlines()
    is_login = data[0]
    email = data[1]
    f.close()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" GROCERY ".center(70, "_"))
    print(f"USER ID :- {is_login}")
    print(f"~{email}")
    print("_"*70)

def search(item):
    print("\033[0m",end="")
    clear_screen()
    item_present = False
    with open("data1.csv", "r") as item_retriever:
        reader = csv.reader(item_retriever)
        while True:
            try:
                row = next(reader)
            except StopIteration:
                break
            if item in row:
                item_present = True
    if item_present:
        x = item.title()
        figlet.setFont(font="smslant")
        for i in figlet.renderText(x).splitlines():
            print("  \033[95m",i,"\033[0m")
        print(
            "\033[0mItem |                    |           |      \nno.  |  Item              | Item Desc | Price "
        )
        print("-----|--------------------|-----------|------")
        with open("data1.csv") as item_retriever:
            reader = csv.reader(item_retriever)
            while True:
                try:
                    row = next(reader)
                except StopIteration:
                    break
                if item in row:
                        print(
                            f"\033[36m{row[0]:5}\033[0m|\033[33m{row[3]:20}\033[0m|{row[4]:11}|\033[32m{row[5]:6}\033[0m"
                        )
            print("--------------------------------------------", end="\n\n")
    else:
        print("No matches found...")
    if selection():
        return True


def retriever(item):
    clear_screen()
    print()
    x = item.title()
    figlet.setFont(font="smslant")
    for i in figlet.renderText(x).splitlines():
        print("  \033[95m",i,"\033[0m")
    print(
        "\033[0mItem |                    |           |      \nno.  |  Item              | Item Desc | Price "
    )
    print("-----|--------------------|-----------|------")
    with open("data1.csv", "r") as item_retriever:
        reader = csv.reader(item_retriever)
        row = next(reader)
        while True:
            try:
                row = next(reader)
            except StopIteration:
                break
            if item == row[1]:
                print(
                    f"\033[36m{row[0]:5}\033[0m|\033[33m{row[3]:20}\033[0m|{row[4]:11}|\033[32m{row[5]:6}\033[0m"
                )
        print("--------------------------------------------", end="\n\n")


def check_if_in_cart(number):
    ans = ""
    if len(cart) == 0:
        return True
    else:
        for row in cart:
            if number == row[0]:
                print("This item already added to cart :  ", end="")
                print(row[3], "(", row[4], ")x", row[6])
                ans = input("Would you like to a.'Continue' or b.'Change Quantity' :  ").lower().strip()
                if ans == 'a' or ans == 'continue':
                    return False
                elif ans == 'b' or 'change quantity':
                    qty = int(input("Enter Quantity : "))
                    row[6] = str(qty)
                    print(row[3], "(" + str(row[4]) + ") x", row[6], "has been added to cart")
                    return False
                else:
                    while ans not in ['a', 'b', 'continue', 'change quantity']:
                        print("Wrong Input")
                        ans = input("Would you like to a.'Continue' or b.'Change Quantity' ").lower().strip()
                    if ans == 'a' or ans == 'continue':
                        return False
                    else:
                        qty = int(input("Enter Quantity : "))
                        row[6] = str(qty)
                        print(row[3], "(" + str(row[4]) + ") x", row[6], "has been added to cart")
                        return False
            return True


def add_():
    try:
        number, quantity = input("enter item number and quantity :").split()
    except ValueError:
        print("Invalid input item number and quantity must be separated")
        return add_()
    try:
        int(quantity)
    except ValueError:
        print("Quantity must be an integer")
        return add_()
    r = check_if_in_cart(number)
    if r:
        l = []
        with open('data1.csv', 'r') as item_retriever:
            reader = csv.reader(item_retriever)
            for row in reader:
                if number == row[0]:
                    l = row.copy()
            l.append(quantity)
            item_retriever.close()
        cart.append(l)
        clear_screen()
        print(l[3], "(" + str(l[4]) + ") x", l[6], "has been added to cart")
        print("---------------------------")
    else:
        print("---------------------------")

    if selection():
        return True


def view_cart():
    figlet.setFont(font='rounded')
    for i in figlet.renderText("Cart").splitlines():
        print("\t\t\t\t\033[96m",i,"\033[0m")
    reader = iter(cart)
    s = ["Item No.","Item Name","Item Desc","Quant"]
    print("----------------------------------------------------")
    print(f"|{s[0]:8}| {s[1]:20}| {s[2]:10} | {s[3]:4}|")
    while True:
        try:
            row = next(reader)
        except StopIteration:
                break
        print("|--------|---------------------|------------|------|")
        print(f"|\033[93m{row[0]:8}\033[0m| \033[91m{row[3]:20}\033[0m| {row[4]:10} | \033[92m{row[6]:4} \033[0m|")
    print("----------------------------------------------------")
    answer = input("Would you like to make changes in cart (yes/no) : ").lower().strip()
    if answer == 'yes':
        change_cart()
    elif answer == 'no':
        pass
    else:
        while answer not in ['yes', 'no']:
            answer = input("Would you like to make changes in cart (yes/no) : ").lower().strip()

    if selection():
        return True

def change_cart():
    print("a.Delete item in cart\nb.Update quantity of an item")
    key = input("Enter your choice : ").lower().strip()
    name = ""
    if key == 'a':
        item = input("Enter Item Number : ")
        for row in cart:
            if item == row[0]:
                name = row[3]
                cart.remove(row)
        print(name,"has been removed from cart")
    elif key =='b':
        item , quantity = input("Enter Item Number and Quantity : ").split()
        for row in cart:
            if row[0] == item:
                row[6]=quantity
                print(row[3], "(" + str(row[4]) + ") x", row[6], "has been added to cart")
    else:
        while key not in ['a','b']:
            print("Wrong Input")
        if key == 'a':
            item = input("Enter Item Number : ")
            for row in cart:
                if item == row[0]:
                    name = row[3]
                    cart.remove(row)
            print(name, "has been removed from cart")
        else:
            item, quantity = input("Enter Item Number and Quantity : ")
            for row in cart:
                if row[0] == item:
                    row[6] = quantity
                    print(row[3], "(" + str(row[4]) + ") x", row[6], "has been added to cart")


def print_section(choice):
    if choice not in ['A','B','C','D','E','F','G']:
        b = wrong_choice(choice)
        print_section(b)
    elif choice == 'A':
        clear_screen()
        if search(input("Search : \033[95m").lower()):
            return True
    elif choice == 'B':
        retriever("kirana")
    elif choice == 'C':
        retriever("instant and frozen foods")
    elif choice == 'D':
        retriever('juices and cold drinks')
    elif choice == 'E':
        retriever('dairy bread and eggs')
    elif choice == 'F':
        retriever('snacks')
    else:
        retriever('dry fruits oils and masalas')
    if selection():
        return True


def wrong_choice(choice):

    while choice not in['A','B','C','D','E','F','G'] :
        print("Wrong Input")
        choice = (input("Enter your choice: \033[95m"))
        print("\033[0m",end="")
    return choice


def command(select__):
    if select__ == 'add':
        if add_():
            return True
    elif select__ == 'view cart':
        if view_cart():
            return True
    elif select__ == 'menu':
        if menu():
            return True
    elif select__ == 'place order':
        with open('cart.csv','a',newline="") as putter:
            writer = csv.writer(putter)
            for row in cart:
                writer.writerow(row)
        clear_screen()
        print("Placing your order....")
        sleep(2)

        return True
    elif select__ == 'search':
        if search(input("Search : \033[95m").lower()):
            return True
    else:
        print("incorrect command")
        clear_screen()
        if selection():
            return True


def menu():
    clear_screen()
    figlet = Figlet()
    figlet.setFont(font="standard")
    for i in figlet.renderText("Menu").splitlines():
        print("\t\t\t\t\033[93m",i,"\033[0m")
    print("\t\t\t     -------------------------------")
    print("\t\t\33[95m  A. \033[91mSearch\033[0m",end=" ")
    print("|                           ",emoji.emojize(":magnifying_glass_tilted_left:"),"| ",)
    print("\t\t\t     -------------------------------")
    print("\t     \033[95mB. \033[96mKirana\033[0m")
    print("\n\t     \033[95mC. \033[96mInstant and Frozen Foods\033[0m")
    print("\n\t     \033[95mD. \033[96mJuices and Cold drinks\033[0m")
    print("\n\t     \033[95mE. \033[96mDairy , Bread and Eggs\033[0m")
    print("\n\t     \033[95mF. \033[96mSnacks\033[0m")
    print("\n\t     \033[95mG. \033[96mDry Fruits , Oils and Masalas\033[0m")
    choice = (input("\nEnter your choice: \033[95m")).upper()
    print("\033[0m")
    if print_section(choice):
        return True


def selection():

    print("COMMANDS:| add | view cart | search | menu | place order |")
    select_ = input("enter command : ").lower().strip()

    if command(select_):
        return True

menu()