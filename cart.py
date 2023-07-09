import csv
import sys
import os

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
    print("Item no.         Item             : Price")
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item in row:
                print("{:3}. {:20} ({:5}) : Rs {:3}".format(row[0], row[3], row[4], row[5]))
        print("------------------------------------------------------------------------------")
        item_retriever.close()
    if selection():
        return True


def retriever(item):
    print("Item no.         Item             : Price")
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item == row[1]:
                print("{:3}. {:20} ({:5}) : Rs {:3}".format(row[0], row[3], row[4], row[5]))
        print("---------------------------")
        item_retriever.close()


def check_if_in_cart(number):
    checker = open('cart.csv', 'r')
    if len(checker.readlines()) == 0:
        checker.close()
        return True
    else:
        with open('cart.csv','r') as checker:
            reader = csv.reader(checker)
            for row in reader:
                if number == row[0]:
                    print("This item already added to cart :  ",end="")
                    print(row[3], "(", row[4], ")x", row[6])
                    return False
            return True


def add_():
    number, quantity = input("enter item number and quantity :").split()
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
        with open('cart.csv', 'a', newline='') as adder:
            adding = csv.writer(adder)
            adding.writerow(l)
        adder.close()
        clear_screen()
        print(l[3], "(" + str(l[4]) + ") x", l[6], "has been added to cart")
        print("---------------------------")
    else:
        print("---------------------------")
        clear_screen()
    if selection():
        return True


def view_cart():
    with open('cart.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            print(row[3], "(", row[4], ") x", row[6])
        print("---------------------------")
        item_retriever.close()
    if selection():
        return True


def print_section(choice):
    if choice not in ['A','B','C','D','E','F','G']:
        b = wrong_choice(choice)
        print_section(b)
    elif choice == 'A':
        clear_screen()
        if search(input("search : ").lower()):
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
        choice = (input("Enter your choice:"))
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
        return True
    elif select__ == 'search':
        if search(input("search : ").lower()):
            return True
    else:
        print("incorrect command")
        if selection():
            return True


def menu():
    clear_screen()
    print("MENU:\nA.Search\nB.Kirana\nC.Instant and Frozen Foods\nD.Juices and Cold drinks\nE.Dairy , Bread and "
          "Eggs\nF.Snacks\nG.Dry Fruits , Oils and Masalas\n")
    choice = (input("Enter your choice:")).upper()
    print()
    if print_section(choice):
        return True


def selection():

    print("COMMANDS:| add | view cart | search | menu | place order |")
    select_ = input("enter command : ").lower().strip()

    if command(select_):
        return True

