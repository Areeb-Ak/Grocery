"""
the cart data is in the cart.csv
"""
import datetime
import csv
import prettytable

no = 1  # need to import the order number from the successful orders list
date_time = datetime.datetime.now()

order_id = date_time.strftime("%d%m%Y%H%M%S") + str(no).zfill(4)
print(order_id)
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


def generate_bill():
    global bill_in_string
    bill_in_string += "--------------------------------------------------------------\n"
    bill_in_string += '|' + "GROCERY MART".center(61) + '|\n'
    bill_in_string += "--------------------------------------------------------------\n"
    bill_in_string += f"Date :- {date_time.date().strftime('%d-%m-%Y')}\n"
    bill_in_string += f"Order ID:-{order_id}\n"
    bill_in_string += str(bill)
    bill_in_string += '\n' + f"TOTAL PRICE :- {total_price}".center(100)


generate_bill()
print(bill_in_string)
