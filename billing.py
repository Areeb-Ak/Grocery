"""
the cart data is in the cart.csv
"""
import datetime
import json
import csv
import prettytable
import os
bill_in_string = ""

with open("cart.csv", 'r') as items:
    # items in the cart.json are in the form of
    order_items = csv.DictReader(items, ["item_id", 'category', 'sub_cat', "item_name", 'type', 'cost', "quantity"])
    s_no = 1
    bill = prettytable.PrettyTable()
    bill.field_names = ["S.NO", "ITEM_ID", "ITEM_NAME", "TYPE", "QTY", "RATE", "AMOUNT"]
    total_price = 0
    for each_order in order_items:
        price = int(each_order['cost']) * int(each_order['quantity'])
        bill.add_row([s_no, each_order["item_id"], each_order["item_name"], each_order["type"], each_order['quantity'],
                      each_order['cost'], price])
        s_no += 1
        total_price += price



def conform_order():
    print(f"\033[47m\033[30m{str(bill)}\033[0m")
    print('\n' + f"TOTAL PRICE :- {total_price}".center(100))

    if input("Do You want to confirm order ?(Yes/No)").lower() == 'yes':
        return True
    return False


def generate_bill():
    # generating order number
    fp = open('successful_orders.json', 'r')
    no = 0
    with open("successful_orders.json") as fh:
        temp = json.load(fh)
        for i in temp.keys():
            for j in temp[i]:    
                no = int(j["order_id"][-4:]) + 1
    date_time = datetime.datetime.now()
    x = len(str(bill).splitlines()[0])
    print(x)
    global order_id
    order_id = date_time.strftime("%d%m%Y%H%M%S") + str(no).zfill(4)
    global bill_in_string
    bill_in_string += "\033[47m\033[30m"+"-"*x+"\n"
    bill_in_string += '|' + "\033[34mGROCERY MART\033[30m".center(x+8) + '|\n'
    bill_in_string += "|"+"-"*(x-2)+"|\n"
    bill_in_string += f"|Date :- {date_time.date().strftime('%d-%m-%Y')}"+" "*(x-20)+"|\n"
    bill_in_string += f"|Order ID:-{order_id}"+" "*(x-30)+"|\n"
    bill_in_string += str(bill)
    bill_in_string += '\n'+" "*(x-22) + f"TOTAL PRICE :- {total_price}  "
    print(bill_in_string)
    return order_id
