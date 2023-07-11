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
    print("""
                              ___   ___    ___      ___    ___  ___   __   _ 
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
            
             _     ___   ____ ___ _   _                     ____ ___ ____ _   _ ___ _   _ 
            | |   / _ \\ / ___|_ _| \\ | |                   / ___|_ _/ ___| \\ | |_ _| \\ | | 
ENTER 1 for | |  | | | | |  _ | ||  \\| |     ENTER 2 for   \\___ \\| | |  _|  \\| || ||  \\| |
            | |__| |_| | |_| || || |\\  |                    ___) | | |_| | |\\  || || |\\  |
            |_____\\___/ \\____|___|_| \\_|                   |____|___\\____|_| \\_|___|_| \\_|

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
                        login()
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
                while not re.search(r"^[0-9]{10}$", id[i]):
                    print("Invalid Phone number. Enter a valid number")
                    id[i] = input(f"{i}: \033[95m")
                    print("\033[0m")
            elif i == "Security Question":
                sleep(2)
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
                sleep(2)
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
    Validates the password returns False if the password is validated(correct)
    or else returns false and also outputs the requirements of the password
    which it does not have.
    """
    if password == "":
        print("Password must contain atleast 8 character")
        return False
    l = True if len(password) >= 8 else False
    cp = False
    num = False
    sp = False
    for i in password:
        if i.isupper():
            cp = True
        if i.isnumeric():
            num = True
        if not i.isalnum():
            sp = True
    if not num and not sp and not cp and not l:
        print(
            "Password must contain atleast 8 characters, 1 digit, 1 special character and 1 capital alphabet"
        )  # FFFF
    elif not num and not sp and not cp and l:
        print(
            "Password must contain atleast 1 digit, 1 special character and 1 capital alphabet"
        )  # FFFT
    elif not num and not sp and cp and not l:
        print(
            "Password must contain atleast 8 characters, 1 digit and 1 special character"
        )  # FFTF
    elif not num and sp and not cp and not l:
        print(
            "Password must contain atleast 8 characters, 1 capital alphabet and 1 digit"
        )  # FTFF
    elif not num and sp and not cp and l:
        print("Password must contain 1 capital alphabet and 1 digit")  # FTFT
    elif not num and sp and cp and not l:
        print("Password must contain atleast 8 characters  and 1 digit")  # FTTF
    elif not num and sp and cp and l:
        print("Password must contain 1 digit")  # FTTT
    elif num and sp and cp and not l:
        print("Password must contain atleast 8 characters")  # TTTF
    elif num and not sp and not cp and not l:
        print(
            "Password must have atleast 8 characters, 1 special character and 1 capital alphabet"
        )  # TFFF
    elif num and sp and not cp and not l:
        print(
            "Password must contain atleast 8 characters  and 1 capital alphabet"
        )  # TTFF
    elif num and not sp and cp and not l:
        print("Password must have atleast 8 characters and 1 special character")  # TFTF
    elif not num and not sp and cp and l:
        print("Password must contain 1 digit  and 1 special character")  # FFTT
    elif num and sp and not cp and not l:
        print(
            "Password must contain atleast 8 characters  and 1 capital alphabet"
        )  # TTFF
    elif num and not sp and cp and l:
        print("Password must contain 1 special character")  # TFTT
    elif num and sp and not cp and l:
        print("Password must contain 1 capital character")  # TTFT
    if num and sp and cp and l:  # TTTT
        return True
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
            print("username not found")

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
    figlet.setFont(font="small")
    for _ in range(3):
        x = numbers.index(random.choice(numbers))
        y = numbers.index(random.choice(numbers))
        z = x + y
        for k, j in enumerate(figlet.renderText("Captcha").splitlines(), start=1):
            if k == 2 or k == 3:
                print("\033[96m", j, "\033[0m", " .")
            elif k == 5:
                print("\033[96m", j, "\033[0m", end="   ")
                ans = input(
                    f"  {emoji.emojize(numbers[x])}  + {emoji.emojize(numbers[y])}  =  \033[92m"
                )
                print("\033[0m")
            else:
                print("\033[96m", j, "\033[0m")
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
