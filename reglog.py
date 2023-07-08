import emoji
import json
import os
from pyfiglet import Figlet
import random
import re
from sys import exit
from time import sleep

file = "grocery.json"

figlet = Figlet()

osname = os.name


def clear_screen():
    os.system("cls" if osname == "nt" else "clear")


def display():
    """
    Gets whether the user wants to login or register
    """
    while True:
        x = input("Enter choice: ")
        try:
            x = int(x)
            if x != 1 and x != 2:
                raise Exception
            break
        except:
            print(
                "Invalid choice can only Enter 1 or 2",
            )
    return x


def register():
    figlet.setFont(font="slant")
    for i in figlet.renderText("Sign up").splitlines():
        if i.strip() == "":
            continue
        print("\t\t\t\t\033[32m\033[42m" + i + "\033[0m")
    id = {}
    details = [
        "Name",
        "Email Id",
        "Phone Number",
        "Security Question",
        "Answer",
        "Password",
    ]
    figlet.setFont(font="small")
    for i in details:
        flag = True
        while flag:
            if i == "Name":
                print(
                    "\033[95m" + figlet.renderText("Personal Information") + "\033[0m"
                )
            if details.index(i) < 3:
                id[i] = input(f"{i}: \033[31m")
                print("\033[0m", end="")
            if i == "Email Id":
                while not validate_email(id[i]):
                    print("\033[0mInvalid Email")
                    print("Email format: user123@example.com\n")
                    id[i] = input(f"{i}: \033[31m")
                print("\033[0m", end="")
                flag = False
                break
            elif i == "Phone Number":
                while not re.search(r"^[0-9]{10}$",id[i]):
                    print("Invalid Phone number. Enter a valid number")
                    id[i] = input(f"{i}: \033[31m")
                    print("\033[0m", end="")
            elif i == "Security Question":
                sleep(2)
                clear_screen()
                print(
                    "\033[36m" + figlet.renderText("Security Key") + "\033[0m\n", end=""
                )
                print(
                    "Choose a security question and provide the corresponding answer. This information will be used for identity verification during the password recovery process."
                )
                print(
                    "Select a security question that is easy for you to remember but difficult for others to guess."
                )
                print(
                    "The answer should be something known only to you, avoiding easily discoverable information."
                )
                id[i] = input(f"{i}: \033[31m")
                print("\033[0m", end="")
            elif i == "Answer":
                id[i] = input(f"{i}: \033[31m")
                print("\033[0m", end="")   
            elif i == "Password":
                sleep(2)
                clear_screen()
                print(
                    "\033[31m"
                    + figlet.renderText("Password")
                    + "\033[0m\nSet a strong and secure password for your account. This password will be used to log in to your account."
                )
                create_password(id)
                break
            if id[i].strip() == "":
                print("This field is compulsory")
            else:
                flag = False
    with open(file) as fh:
        temp = json.load(fh)
    temp["users"].append(id)
    with open(file, "w") as fh:
        json.dump(temp, fh, indent=4)
    print("\033[33mRegistrations Successful\033[0m")


def create_password(id):
    i = "Password"
    id[i] = input(f"{i}: \033[31m")
    print("\033[0m", end="")
    while not validate_password(id[i]):
        id[i] = input(f"\033[0m\n{i}: \033[31m")
        print("\033[0m", end="")
    c = input("Confirm Password: \033[31m")
    print("\033[0m", end="")
    if c != id[i]:
        print("\033[0mPassword should be same as previous password")
        q = input("Confirm Password: \033[31m")
        print("\033[0m", end="")
        if q != id[i]:
            exit("Wrong Password")


def validate_password(password):
    """
    Validates the password returns False if the password is validated(correct)
    or else returns false and also outputs the requirements of the password
    which it does not have.
    """
    if password == "":
        print("Password must contain atleast 8 character")
        return False
    elif len(password) >= 8 and password[0].isupper():
        num = False
        sp = False
        for i in password:
            if i.isnumeric():
                num = True
            if not i.isalnum():
                sp = True
        if not num:
            if not sp:
                print("Password must contain atlest 1 digit and 1 special character")
            else:
                print("Password must contain atleat 1 digit")
        elif not sp:
            print("Password must contain atleast 1 special character")
        if num and sp:
            return True
    else:
        if not password[0].isupper():
            print("Password must start with a capital alphabet")
        if len(password) < 8:
            print("Password must contain atleast 8 character")
    return False


validate_email = (
    lambda email: True
    if re.search(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$", email)
    else False
)


def login():
    """
    Asks the user for username, calls check_id (returns true if the
    username in the file) and it asks for password and checks the
    password from the file if it is correct or not
    """
    figlet.setFont(font="larry3d")
    print("\033[95m\033[41m")
    for i in figlet.renderText("Login").splitlines():
        if i.strip() == "":
            break
        print("\t\t\t\t" + i)
    print("\033[0m\n")
    for _ in range(3):
        email = input("Enter your Email Id: \033[36m")
        print("\033[0m")
        if check_id(email):
            with open(file, "r+") as fh:
                temp = json.load(fh)["users"]
                for i in temp:
                    if i["Email Id"] == email:
                        passw = i["Password"]
                        for _ in range(3):
                            password = input("Enter your Password: \033[36m")
                            print("\033[0m")
                            if password == "forgot":
                                print(i["Security Question"])
                                for _ in range(3):
                                    ans = input("Answer: ")
                                    if ans == i["Answer"]:
                                        sleep(2)
                                        clear_screen()
                                        print("Create new password: ")
                                        create_password(i)
                                        change(i)
                                        print("Password Changed")
                                        sleep(2)
                                        clear_screen()
                                        login()
                                    print("Invalid Answer")
                            elif password == passw:
                                figlet.setFont(font="small")
                                for i in figlet.renderText("Captcha").splitlines():
                                    if i.strip() == "":
                                        continue
                                    print("\033[30m\033[47m" + i + "\033[0m")
                                captcha()
                                exit("Logged in")
                            print(
                                "Invalid password. \t\t If you forgot your password enter '\033[31mforgot\033[0m'"
                            )
            exit("Try again later")
        else:
            print("username not found")


def captcha():
    numbers = [
        ":keycap_0:",
        ":keycap_1:",
        ":keycap_2:",
        ":keycap_3:",
        ":keycap_4:",
        ":keycap_5:",
        ":keycap_6:",
        ":keycap_7:",
        ":keycap_8:",
        ":keycap_9:",
    ]
    x = numbers.index(random.choice(numbers))
    y = numbers.index(random.choice(numbers))
    z = x + y
    print(f"\n{emoji.emojize(numbers[x])}  + {emoji.emojize(numbers[y])}  = ", end="")
    if len(str(z)) == 1:
        print(emoji.emojize(numbers[z]))
    else:
        z = str(z)
        print(
            emoji.emojize(numbers[int(z[0])]), emoji.emojize(numbers[int(z[1])]), sep=""
        )
    ans = input(f" {x}  +  {y} = \033[031m")
    print("\033[0m")
    if ans == str(z):
        return True
    else:
        captcha()


def change(id):
    with open(file) as fh:
        temp = json.load(fh)
        u = []
    for i in temp["users"]:
        if i["Email Id"] != id["Email Id"]:
            u.append(i)
    u.append(id)
    temp["users"] = u
    with open(file, "w") as fh:
        json.dump(temp, fh, indent=4)


def check_id(email):
    """
    Checks whether the username is in the file or not
    Return True if it is present or else false
    """
    flag = False
    with open(file) as fh:
        for i in json.load(fh)["users"]:
            if i["Email Id"] == email:
                flag = True
    return flag


def reglog():
    clear_screen()
    choice = display()
    clear_screen()
    if choice == 1:
        login()
    elif choice == 2:
        register()
        sleep(2)
        clear_screen()
        choice = input("\n\nDo you want to login now?(yes/no) ")
        if choice.lower() == "yes":
            clear_screen()
            login()


reglog()
