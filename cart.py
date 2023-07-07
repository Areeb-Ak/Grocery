import csv


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
    with open('cart.csv','a') as adder:
        adding = csv.writer(adder)
        adding.writerow(l)
    selection()


def veiw_cart():
    c = 0
    with open('cart.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            print(row[3], "(", row[4], ") . Quantity : ", row[6])
        print("---------------------------")
        item_retriever.close()
    selection()


def print_section(choice):
    if choice not in range(7):
        b = wrong_choice(choice)
        print(b)
        print_section(b)
        selection()
    elif choice == 0:
        search(input("search : ").lower())
        selection()
    elif choice == 1:
        retriever("kirana")
        selection()
    elif choice == 2:
        retriever("instant and frozen foods")
        selection()
    elif choice == 3:
        retriever('juices and cold drinks')
        selection()
    elif choice == 4:
        retriever('dairy bread and eggs')
        selection()
    elif choice == 5:
        retriever('snacks')
        selection()
    else:
        retriever('dry fruits oils and masalas')
        selection()


def wrong_choice(choice):

    if choice <7:
        c = choice
        print(c)
        return c
    else:
        print("Wrong Input")
        choice = int(input("Enter your choice:"))
        wrong_choice(choice)


def command(selection):
    if selection == 'add':
        add_()
    elif selection == 'veiw cart':
        veiw_cart()
    elif selection == 'menu':
        menu()
    else:
        print("incorrect command")


def menu():
    print("MENU:\n0.Search\n1.Kirana\n2.Instant and Frozen Foods\n3.Juices and Cold drinks\n4.Dairy , Bread and Eggs\n5.Snacks\n6.Dry Fruits , Oils and Masalas\n")
    choice = int(input("Enter your choice:"))
    print_section(choice)


def selection():
    select_ = input("enter commmand : ").lower()
    command(select_)


menu()




