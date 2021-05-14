"""
Do this now - 14/05/2021 in-class session (Work in Progress)
Write a program that stores a list of users:
users = [["Name", "password", clearance], ...]
That is, a list of lists where each item is a user
Write a menu:
- Add user - Only level 3+ can add users
- Login (existing user)
- Logout
- Access information
- Quit
When accessing, each clearance level gives more information
0 = Nothing
1 = Public
2 = Secret
3 = Top Secret
4 = Lindsay's profile picture
Challenge: read the users data from a file :)
"""

MENU_PROMPT = """- A)dd user
- Log(i)n
- Log(o)ut
- A(x)ess information
- Q)uit"""


def main():
    users = []
    users = [['Lindsay', 'IloveCP1401', 8], ['Bob', 'Jo', 2]]
    current_user = None
    print(MENU_PROMPT)
    choice = input("> ").upper()
    while choice != "Q":
        print(current_user)
        if choice == "A":
            add_user(users)
        if choice == "I":
            current_user = login(users)
        else:
            print("Invalid")
        choice = input("> ").upper()
    print("Goodbye")


def get_valid_string(prompt):
    string = input(prompt)
    while string == "":
        print("Invalid input")
        string = input(prompt)
    return string


def get_valid_number(prompt):
    number = int(input(prompt))
    while number < 0:
        print("Invalid")
        number = int(input(prompt))
    return number


def add_user(users):
    """Add a new user to the list of users."""
    name = get_valid_string("Name: ")
    password = get_valid_string("Password: ")
    clearance = get_valid_number("Clearance: ")
    user = [name, password, clearance]
    users.append(user)


def login(users):
    name = get_valid_string("Name: ")
    password = get_valid_string("Password: ")
    # name = "xLindsay"
    # password = "IloveCP1401"
    # name = "Bob"
    # password = "Jo"
    for user in users:
        # print(user, user[0])
        if name == user[0] and password == user[1]:
            print("Login success")
            return user
    print("Login failed")
    return None


main()
# current_user = login(None)
# print(current_user)
