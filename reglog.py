import json
from sys import exit
from time import sleep
from os import name, system

file = "grocery.json"


osname = name


def clear():
    if osname == "nt":
        system("cls")
    elif osname == "posix":
        system("clear")


def display():
    """
    Gets whether the user wants to login or register
    """
    while True:
        x = input("Enter 1 to Login\nEnter 2 to registration\nEnter: ")
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
    id = {}
    details = [
        "Name",
        "Email Id",
        "Phone Number",
        "Security Question",
        "Answer",
        "Password",
    ]
    for n, i in enumerate(details, start=1):
        flag = True
        while flag:
            if n == 1:
                print("Personal Information")
            elif n == 4:
                sleep(2)
                clear()
                print("Security Key:\n", end="")
                print(
                    "Choose a security question and provide the corresponding answer. This information will be used for identity verification during the password recovery process."
                )
                print(
                    "Select a security question that is easy for you to remember but difficult for others to guess."
                )
                print(
                    "The answer should be something known only to you, avoiding easily discoverable information."
                )
            elif n == 6:
                sleep(2)
                clear()
                print(
                    "Password:\nSet a strong and secure password for your account. This password will be used to log in to your account."
                )
                create_password(id)
                break
            id[i] = input(f"{i}: ")
            if id[i].strip() == "":
                print("This field is compulsory")
            else:
                flag = False
    with open(file) as fh:
        temp = json.load(fh)
    temp["users"].append(id)
    with open(file, "w") as fh:
        json.dump(temp, fh, indent=4)
    print("Registrations Successful")


def create_password(id):
    i = "Password"
    id[i] = input(f"{i}: ")
    while validate(id[i]):
        id[i] = input(f"\n{i}: ")
    c = input("Confirm Password: ")
    if c != id[i]:
        print("Password should be same as previous password")
        q = input("Confirm Password: ")
        if q != id[i]:
            exit("Wrong Password")


def validate(password):
    """
    Validates the password returns False if the password is validated(correct)
    or else returns false and also outputs the requirements of the password
    which it does not have.
    """
    if password == "":
        print("Password must contain atleast 8 character")
        return True
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
            return False
    else:
        if not password[0].isupper():
            print("Password must start with a capital alphabet")
        if len(password) < 8:
            print("Password must contain atleast 8 character")
    return True


def login():
    """
    Asks the user for username, calls check_id (returns true if the
    username in the file) and it asks for password and checks the
    password from the file if it is correct or not
    """
    for _ in range(3):
        email = input("Enter your Email Id: ")
        if check_id(email):
            with open(file, "r+") as fh:
                temp = json.load(fh)["users"]
                for i in temp:
                    if i["Email Id"] == email:
                        passw = i["Password"]
                        for _ in range(3):
                            password = input("Enter your password: ")
                            if password == "forgot":
                                print(i["Security Question"])
                                for _ in range(3):
                                    ans = input("Answer: ")
                                    if ans == i["Answer"]:
                                        sleep(2)
                                        clear()
                                        print("Create new password: ")
                                        create_password(i)
                                        print(i)
                                        print(type(i))
                                        change(i)
                                        print("Password Changed")
                                        sleep(2)
                                        clear()
                                        login()
                                    print("Invalid Answer")
                            elif password == passw:
                                exit("Logged in")
                            print(
                                "Invalid password. \t\t If you forgot your password enter 'forgot'"
                            )
            exit("Try again later")
        else:
            print("username not found")


def change(id):
    print(id)
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


def main():
    clear()
    choice = display()
    clear()
    if choice == 1:
        login()
    elif choice == 2:
        register()
        sleep(2)
        clear()
        choice = input("\n\nDo you want to login now? ")
        if choice.lower() == "yes":
            login()


main()
