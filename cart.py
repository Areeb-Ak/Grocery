import csv
import sys


def search(item):
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item in row:
                print("{:3}. {:20} ({:4}) : Rs {:3}".format(row[0], row[3], row[4], row[5]))
        print("---------------------------")
        item_retriever.close()
    selection()


def retriever(item):
    print("Item no. Item  : Price")
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item == row[1]:
                print("{:3}. {:20} ({:4}) : Rs {:3}".format(row[0], row[3], row[4], row[5]))
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
        print(l[3], "(" + str(l[4]) + ") x", l[6], "has been added to cart")
        print("---------------------------")
    else:
        print("---------------------------")
    selection()


def view_cart():
    with open('cart.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            print(row[3], "(", row[4], ") x", row[6])
        print("---------------------------")
        item_retriever.close()
    selection()


def print_section(choice):
    if choice not in ['A','B','C','D','E','F','G']:
        b = wrong_choice(choice)
        print_section(b)
        selection()
    elif choice == 'A':
        search(input("search : ").lower())
        selection()
    elif choice == 'B':
        retriever("kirana")
        selection()
    elif choice == 'C':
        retriever("instant and frozen foods")
        selection()
    elif choice == 'D':
        retriever('juices and cold drinks')
        selection()
    elif choice == 'E':
        retriever('dairy bread and eggs')
        selection()
    elif choice == 'F':
        retriever('snacks')
        selection()
    else:
        retriever('dry fruits oils and masalas')
        selection()


def wrong_choice(choice):

    while choice not in['A','B','C','D','E','F','G'] :
        print("Wrong Input")
        choice = (input("Enter your choice:"))
    return choice


def command(select__):
    if select__ == 'add':
        add_()
    elif select__ == 'view cart':
        view_cart()
    elif select__ == 'menu':
        menu()
    elif select__ == 'exit':
        sys.exit()
    elif select__ == 'search':
        search(input("search : ").lower())
    else:
        print("incorrect command")
        selection()


def menu():
    print("MENU:\nA.Search\nB.Kirana\nC.Instant and Frozen Foods\nD.Juices and Cold drinks\nE.Dairy , Bread and Eggs\nF.Snacks\nG.Dry Fruits , Oils and Masalas\n")
    choice = (input("Enter your choice:")).upper()
    print_section(choice)


def selection():
    print("COMMANDS:| add | view cart | search | menu | exit |")
    select_ = input("enter command : ").lower().strip()
    command(select_)


print("COMMANDS:\n-add\n-view cart\n-search\n-print commands\n-exit\n")
menu()
