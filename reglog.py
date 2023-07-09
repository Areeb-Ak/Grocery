import emoji
import json
import os
from pyfiglet import Figlet
import random
import re
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
            clear_screen()
            print(
                """Invalid choice can only Enter 1 or 2
                                1==>LOGIN
                                2==>SIGNUP
                """
            )
    return x


def register():
    figlet.setFont(font="slant")
    for i in figlet.renderText("Sign up").splitlines():
        if i.strip() == "":
            continue
        print("\t\t\t\t\033[95m\033[40m" + i + "\033[0m")
    id = {}
    details = [
        "Name",
        "Email Id",
        "Phone Number",
        "Security Question",
        "Answer",
        "Password",
    ]
    figlet.setFont(font="cybermedium")
    for i in details:
        flag = True
        while flag:
            if i == "Name":
                print("\tPersonal Information")
            if details.index(i) < 3:
                id[i] = input(f"{i}: \033[92m")
                print("\033[0m", end="")
            if i == "Email Id":
                id[i] = id[i].lower().strip()
                while check_id(id[i]):
                    print("You already have an account with this email")
                    x = input(
                        "Enter '\033[31mlogin\033[0m' to go to login page\nEnter '\033[31mcontinue\033[0m' to create new id\nEnter: \033[92m"
                    )
                    print("\033[0m", end="")
                    if x == "login":
                        clear_screen()
                        login()
                    else:
                        print("Please enter another Email id: ")
                        id[i] = input(f"{i}: \033[92m").lstrip().lower()
                        print("\033[0m", end="")
                while not validate_email(id[i]):
                    print("\033[0mInvalid Email")
                    print("Email format: user123@example.com\n")
                    id[i] = input(f"{i}: \033[92m")
                print("\033[0m", end="")
                flag = False
                break
            elif i == "Phone Number":
                while not re.search(r"^[0-9]{10}$", id[i]):
                    print("Invalid Phone number. Enter a valid number")
                    id[i] = input(f"{i}: \033[92m")
                    print("\033[0m", end="")
            elif i == "Security Question":
                sleep(2)
                clear_screen()
                print("\tSecurity Key")
                print(
                    "Choose a \033[93mSecurity Question\033[0m and provide the corresponding \033[93mAnswer\033[0m.\nThis information will be used for identity verification during the password recovery process."
                )
                # print(
                #     "Select a security question that is easy for you to remember but difficult for others to guess."
                # )
                # print(
                #     "The answer should be something known only to you, avoiding easily discoverable information."
                # )
                id[i] = input(f"{i}: \033[93m")
                print("\033[0m", end="")
            elif i == "Answer":
                id[i] = input(f"{i}: \033[93m")
                print("\033[0m", end="")
            elif i == "Password":
                sleep(2)
                clear_screen()
                print("\tPassword")
                if not create_password(id):
                    return False
                break
            if id[i].strip() == "":
                print("This field is compulsory")
            else:
                flag = False
    with open(file) as fh:
        temp = json.load(fh)
    x = random.randint(0, 999999)
    while x in temp["users"]:
        x = random.randit(0, 999999)
    temp["users"][f"{x:06}"] = id
    with open(file, "w") as fh:
        json.dump(temp, fh, indent=4)
    print("\033[33mRegistrations Successful\033[0m")
    return True


def create_password(id):
    i = "Password"
    id[i] = input(f"{i}: \033[91m")
    print("\033[0m", end="")
    while not validate_password(id[i]):
        id[i] = input(f"\033[0m\n{i}: \033[91m")
        print("\033[0m", end="")
    c = input("Confirm Password: \033[91m")
    print("\033[0m", end="")
    if c != id[i]:
        print("\033[0mPassword should be same as previous password")
        q = input("Confirm Password: \033[91m")
        print("\033[0m", end="")
        if q != id[i]:
            print("Wrong Password")
            return False
    return True


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
    figlet.setFont(font="slant")
    for i in figlet.renderText("Login").splitlines():
        if i.strip() == "":
            break
        print("\t\t\t\t\033[92m\033[40m" + i + "\033[0m")
    print("\033[0m\n")
    for _ in range(3):
        email = input("Enter your Email Id: \033[96m").strip().lower()
        print("\033[0m")
        if check_id(email):
            with open(file) as fh:
                temp = json.load(fh)["users"]
                for i in temp.keys():
                    if temp[i]["Email Id"] == email:
                        passw = temp[i]["Password"]
                        for _ in range(3):
                            password = input("Enter your Password: \033[96m")
                            print("\033[0m")
                            if password == "forgot":
                                print(temp[i]["Security Question"])
                                for _ in range(3):
                                    ans = input("Answer: ")
                                    if ans == temp[i]["Answer"]:
                                        sleep(2)
                                        clear_screen()
                                        print("Create new password: ")
                                        if not create_password(temp[i]):
                                            return False
                                        change(i, temp[i])
                                        print("Password Changed")
                                        sleep(2)
                                        clear_screen()
                                        _ = -1
                                        break
                                    print("Invalid Answer")
                                    if _ == 2:
                                        return False
                                    
                            elif password == passw:
                                figlet.setFont(font="short")
                                for j in figlet.renderText("Captcha").splitlines():
                                    if j.strip() == "":
                                        continue
                                    print("\033[96m" + j + "  \033[0m")
                                captcha()
                                return i,temp[i]["Name"]
                            if _ == -1:
                                break
                            print(
                                "Invalid password. \t\t If you forgot your password enter '\033[31mforgot\033[0m'"
                            )
                    if _ == -1:
                        break
                if _ == -1:
                    break
            if _ == -1:
                break
            print("Try again later")
            return False
        else:
            print("username not found")
    if _ == -1:
        return login()
    else:
        return False



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
    for _ in range(3):
        x = numbers.index(random.choice(numbers))
        y = numbers.index(random.choice(numbers))
        z = x + y
        print(f"\n{emoji.emojize(numbers[x])}  + {emoji.emojize(numbers[y])}  = ", end="")
        if len(str(z)) == 1:
            print(emoji.emojize(numbers[z]))
        else:
            z = str(z)
            print(
                emoji.emojize(numbers[int(z[0])]),
                emoji.emojize(numbers[int(z[1])]),
                sep=" ",
            )
        ans = input(f" {x}  + {y} = \033[031m")
        print("\033[0m")
        if ans == str(z):
            return True
    return False


def change(key, id):
    with open(file) as fh:
        temp = json.load(fh)
        u = {}
    for i in temp["users"].keys():
        if temp["users"][i]["Email Id"] != id["Email Id"]:
            u[i] = temp["users"][i]
        else:
            u[key] = id
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
        t = json.load(fh)
        m = t["users"]
        for i in m.keys():
            if m[i]["Email Id"] == email:
                flag = True
                break
    return flag

