import csv
import sys


def search(item):
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item in row:
                print(row[0],".",row[3],"(",row[4],") : Rs.",row[5])
        print("---------------------------")
        item_retriever.close()
    selection()


def retriever(item):
    print("Item no. Item (Quantity) : Price")
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item == row[1]:
                print(row[0], ".", row[3], "(", row[4], ") : Rs.", row[5])
        print("---------------------------")
        item_retriever.close()


def add_():
    number, quantity = input("enter item number and quantity :").split()
    l = []
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if number == row[0]:
                l = row.copy()
        l.append(quantity)
        item_retriever.close()
    with open('cart.csv','a') as adder:
        adding=csv.writer(adder)
        adding.writerow(l)
    adder.close()
    print(l[3],"("+str(l[4])+")has been added to cart")
    selection()


def view_cart():
    c = 0
    with open('cart.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            print(row[3], "(", row[4], ") . Quantity : ", row[6])
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
    elif select__ == 'print commands':
        print_commands()
    else:
        print("incorrect command")
        selection()

def print_commands():
    print("COMMANDS:\n-add\n-view cart\n-search\n-print commands\n-exit\n")
def menu():
    print("MENU:\nA.Search\nB.Kirana\nC.Instant and Frozen Foods\nD.Juices and Cold drinks\nE.Dairy , Bread and Eggs\nF.Snacks\nG.Dry Fruits , Oils and Masalas\n")
    choice = (input("Enter your choice:")).upper()
    print_section(choice)


def selection():
    select_ = input("enter command : ").lower()
    command(select_)


print_commands()
menu()





