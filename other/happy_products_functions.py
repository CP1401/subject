"""
16/04/2021 - Online class focused on functions
CP1401 - Coding Checkpoint 1 Happy Products rewritten using functions
https://github.com/CP1401/Practicals/blob/master/checkpoints/checkpoint_01.md

Enter the number of products you want to buy and your chosen price.
If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!
"""
MENU = "Menu:\n(I)nstructions\n(C)alculate\n(Q)uit"


def main():
    print(MENU)
    choice = input("Choice: ").lower()
    while choice != "q":
        if choice == 'i':
            print_instructions()
        elif choice == 'c':
            do_quote()
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").lower()
    print("Farewell")


def do_quote():
    number_of_products = get_nonnegative_integer("Number of products: ")
    price = get_positive_float("Price: ")
    total = calculate_total(number_of_products, price)
    print_result(number_of_products, price, total)


def get_nonnegative_integer(prompt):
    number = int(input(prompt))
    while number < 0:
        print("Invalid")
        number = int(input(prompt))
    return number


def get_positive_float(prompt):
    number = float(input(prompt))
    while number <= 0:
        print("Invalid")
        number = float(input(prompt))
    return number


def print_result(number_of_products, price, total):
    print("{} x ${:.2f} products = ${:.2f}".format(number_of_products, price, total))


def calculate_total(number_of_products, price):
    total = number_of_products * price
    if number_of_products > 5:
        total = total * 0.9
    return total


def print_instructions():
    print("Enter the number of products you want to buy and your chosen price.\nIf you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")


def run_tests():
    print(calculate_total(5, 10))  # should be 50
    print(calculate_total(6, 10))  # should be 60 - 6 = 54


# run_tests()
main()
