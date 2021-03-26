""" 26/03/2021 - Do this now:

1. Write a loop to print the numbers from 0 up to a user's age
2. Update the first program with error-checking for the age

3. Write a menu-driven program with the options
- (G)et number
- (U)p
- (D)own
- (Q)uit
Up should print numbers 0 to number
Down should print numbers number down to 0
After quitting, print a :)
"""
MENU_PROMPT = """- (G)et number
- (U)p
- (D)own
- (Q)uit"""


def main():
    number = get_positive_number()
    print(MENU_PROMPT)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            number = get_positive_number()
        elif choice == "U":
            for i in range(number + 1):
                print(i, end=" ")
            print()
        elif choice == "D":
            for i in range(number, -1, -1):
                print(i, end=" ")
            print()
        else:
            print("Invalid choice")
        print(MENU_PROMPT)
        choice = input(">>> ").upper()
    print(":)")


def get_positive_number():
    number = int(input("Number: "))
    while number <= 0:
        print("Invalid number")
        number = int(input("Number: "))
    return number


main()

# 1. Write a loop to print the numbers from 0 up to a user's age
# age = int(input("Age: "))
# while age < 0:
#     print("Invalid age!")
#     age = int(input("Age: "))
# for i in range(age + 1):
#     print(i, end=" ")
