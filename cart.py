import csv
def search(item):
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item in row:
                print(row[0],".",row[3],"(",row[4],") : Rs.",row[5])
        print("---------------------------")

def retriever(item):
    print("Item no. Item (Quantity) : Price")
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if item == row[1]:
                print(row[0], ".", row[3], "(", row[4], ") : Rs.", row[5])
        print("---------------------------")

def add_(number,quantity):
    l = []
    with open('data1.csv', 'r') as item_retriever:
        reader = csv.reader(item_retriever)
        for row in reader:
            if number == row[0]:
                l = row.copy()
        l.append(quantity)
    with open('cart.csv','w') as adder:
        adding = csv.writer(adder)
        adding.writerow(l)
def print_section(choice):
    if choice not in range(7):
        b = wrong_choice(choice)
        print(b)
        print_section(b)
    elif choice == 0:
        search(input("search : ").lower())
    elif choice == 1:
        retriever("kirana")
    elif choice == 2:
        retriever("instant and frozen foods")
    elif choice == 3:
        retriever('juices and cold drinks')
    elif choice == 4:
        retriever('dairy bread and eggs')
    elif choice == 5:
        retriever('snacks')
    else:
        retriever('dry fruits oils and masalas')
def wrong_choice(choice):

    if choice <7:
        c = choice
        print(c)
        return c
    else:
        print("Wrong Input")
        choice = int(input("Enter your choice:"))
        wrong_choice(choice)

print('MENU:\n0.Search\n1.Kirana\n2.Instant and Frozen Foods\n3.Juices and Cold drinks\n4.Dairy , Bread and Eggs\n5.Snacks\n6.Dry Fruits , Oils and Masalas\n')
choice = int(input("Enter your choice:"))
print_section(choice)
i_n ,quantity = input("enter item number :").split()
add_(i_n,quantity)



