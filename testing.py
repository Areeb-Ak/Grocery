# import csv
# with open('cart.csv', 'r') as item_retriever:
#     reader = csv.reader(item_retriever)
#     s = ["Item Name","Item Desc","Quant"]
#     print("-------------------------------------------")
#     print(f"| {s[0]:20}| {s[1]:10} | {s[2]:4}|")
#     while True:
#         try:
#             row = next(reader)
#         except StopIteration:
#                 break
#         print("|---------------------|------------|------|")
#         print(f"| \033[91m{row[3]:20}\033[0m| {row[4]:10} | \033[92m{row[6]:4} \033[0m|")
#     print("-------------------------------------------")



import reglog
import emoji
from pyfiglet import Figlet
figlet = Figlet()
figlet.setFont(font="standard")
reglog.clear_screen()
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
print("\033[0m",end="")