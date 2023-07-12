# from time import sleep
# print(" " + "_" * 67)
# print("| (add) ➕| (view cart) 🛒| (search) 🔍| (menu) ☰| (place order) 📦|")
# print(" " + "_" * 67)
# print("""
#    TO SELECT OPTION PLEASE ENTER TEXT INSIDE ()
#    """)
# sleep(0.3)
# select_ = input("Enter Command : ").lower().strip()

import csv
with open("data1.csv") as fh:
   print(fh)
   print(type(fh))
   reader = (csv.DictReader(fh))
   print(zip(dict([i for i in range(len(list(reader)))],list(reader))))
   print(type(reader))
