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
    print("""
                              ___   ___     ___     ___   ___   ___   __   __ 
                             / __| | _ \\   / _ \\   / __| | __| | _ \\  \\ \\ / / 
  --------------------------| (_ | |   /  | (_) | | (__  | _|  |   /   \\ V /  ---------------------------------
                             \\___| |_|_\\   \\___/   \\___| |___| |_|_\\    |_|   
    """)


def display():
    """
    Gets whether the user wants to login or register
    """
    while True:
        x = input("ENTER YOUR CHOICE: ")
        try:
            x = int(x)
            if x != 1 and x != 2:
                raise Exception
            break
        except:
            clear_screen()
            print(
                """Invalid Choice 

             _     ___   ____ ___ _   _                      ____ ___ ____ _   _ _   _ ____  
            | |   / _ \\ / ___|_ _| \\ | |                    / ___|_ _/ ___| \\ | | | | |  _ \ 
ENTER 1 for | |  | | | | |  _ | ||  \\| |     ENTER 2 for    \\___ \\| | |  _|  \\| | | | | |_) |
            | |__| |_| | |_| || || |\\  |                     ___) | | |_| | |\\  | |_| |  __/ 
            |_____\\___/ \\____|___|_| \\_|                    |____|___\\____|_| \\_|\\___/|_|  

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
                print("\033[92mPersonal Information\033[0m")
                print("\033[91m-------- -----------\033[0m")
            if details.index(i) < 3:
                id[i] = input(f"{i}: \033[95m")
                print("\033[0m")
            if i == "Email Id":
                id[i] = id[i].lower().strip()
                while check_id(id[i]):
                    print("You already have an account with this email")
                    x = input(
                        "Enter '\033[31mlogin\033[0m' to go to login page\nEnter '\033[31mcontinue\033[0m' to create new id\nEnter: \033[95m"
                    )
                    print("\033[0m")
                    if x == "login":
                        clear_screen()
                        return login()
                    else:
                        print("Please enter another Email id: ")
                        id[i] = input(f"{i}: \033[95m").lstrip().lower()
                        print("\033[0m")
                while not validate_email(id[i]):
                    print("\033[0mInvalid Email")
                    print("Email format: user123@example.com\n")
                    id[i] = input(f"{i}: \033[95m")
                    print("\033[0m")
                flag = False
                break
            elif i == "Phone Number":
                while not re.search(r"^[6789][0-9]{9}$", id[i]):
                    print("Invalid Phone number. Enter a valid number")
                    id[i] = input(f"{i}: \033[95m")
                    print("\033[0m")
            elif i == "Security Question":
                sleep(0.5)
                clear_screen()
                print("\033[92mSecurity Key\033[0m")
                print("\033[91m-------- ---\033[0m")
                print(
                    "Choose a \033[93mSecurity Question\033[0m and provide the corresponding \033[93mAnswer\033[0m.\nThis information will be used for identity verification during the password recovery process.\n"
                )
                # print(
                #     "Select a security question that is easy for you to remember but difficult for others to guess."
                # )
                # print(
                #     "The answer should be something known only to you, avoiding easily discoverable information."
                # )
                id[i] = input(f"{i}: \033[93m")
                print("\033[0m")
            elif i == "Answer":
                id[i] = input(f"{i}: \033[93m")
                print("\033[0m", end="")
            elif i == "Password":
                sleep(0.5)
                clear_screen()
                print("\033[92mPassword\033[0m")
                print("\033[91m--------\033[0m")
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
    print("\033[93mPassword must have atleast \033[95m8\033[93m characters, \033[95m1\033[93m digit, \033[95m1\033[93m special character and \033[95m1\033[93m capital alphabet\033[0m")
    i = "Password"
    id[i] = input(f"{i}: \033[91m")
    print("\033[0m")
    while not validate_password(id[i]):
        id[i] = input(f"\033[0m\n{i}: \033[91m")
        print("\033[0m")
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
    Validates the password and returns False if the password is valid (meets the requirements),
    or else returns False and outputs the specific requirements that are not met.
    """
    if len(password) < 8:
        print("Password must contain at least 8 characters")
        return False
    
    requirements = []
    if not any(char.isdigit() for char in password):
        requirements.append("at least 1 digit")
    if not any(not char.isalnum() for char in password):
        requirements.append("at least 1 special character")
    if not any(char.isupper() for char in password):
        requirements.append("at least 1 capital letter")
    
    if requirements:
        print("Password must contain " + ", ".join(requirements))
        return False
    
    return True



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
    for _ in range(5):
        email = input("Enter your Email Id: \033[96m").strip().lower()
        print("\033[0m")
        if email == 'signup':
            clear_screen()
            return register()
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
                                        sleep(0.5)
                                        clear_screen()
                                        print("Create new password: ")
                                        if not create_password(temp[i]):
                                            return False
                                        change(i, temp[i])
                                        print("Password Changed")
                                        sleep(0.5)
                                        clear_screen()
                                        return login()
                                    print("Invalid Answer")
                                    if _ == 2:
                                        return False
                            elif password == passw:
                                captcha()
                                return i, temp[i]["Name"]
                            print(
                                "Invalid password. \t\t If you forgot your password enter '\033[31mforgot\033[0m'"
                            )
            print("Try again later")
            return False
        else:
            print("username not found\t\tIf you want to register enter '\033[91msignup\033[0m'.")


    return False


def captcha():
    numbers = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
    figlet.setFont(font="small")
    for _ in range(3):
        x = numbers.index(random.choice(numbers))
        y = numbers.index(random.choice(numbers))
        z = x + y
        sleep(0.3)
        clear_screen()
        print()
        for j in figlet.renderText("Captcha").splitlines():
            print("\033[96m", j, "\033[0m")
        print("\n\033[95mSolve the above equation to prove you are human\033[0m\n")
        ans = input(
                    f"  {numbers[x]}  + {numbers[y]}  =  \033[92m"
                )
        print("\033[0m")
        if ans == str(z):
            return True
        print("Invalid response")
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
