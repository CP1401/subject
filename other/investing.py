"""
CP1401 Do This Now - Live Session 20/10/2020
NOTE: This is not standalone 'good code'.
It's a work-in-progress developed interactively in the live session.
The intention is only as a reference for those at the session,
or for people who watch the session recording.

Simple 'investing'
get starting balance (we changed this to constant)
menu: i)nvest, h)istory, q)uit
i = balance = balance * random percentage, 80-120%
h = display list of results and running total
q = display overall profit or loss (not done)
"""
import random

MENU = """i)nvest
h)istory
q)uit
"""
MINIMUM_RESULT = 80
MAXIMUM_RESULT = 120
STARTING_BALANCE = 100


def main():
    results = []
    balance = STARTING_BALANCE
    print("Let's \"Invest\"")
    print(f"You can get {MINIMUM_RESULT}% - {MAXIMUM_RESULT}%")
    print(MENU, end="")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "i":
            result = determine_result(balance)
            results.append(result)
            balance += result
        elif choice == "h":
            print("history")
            display_history(results)
        else:
            print("Invalid choice")
        print(f"${balance:.2f}")
        print(MENU, end="")
        choice = input(">>> ").lower()
    print("")  # TODO overall profit/loss


def determine_result(balance):
    scaling_factor = random.randint(MINIMUM_RESULT, MAXIMUM_RESULT) / 100
    result = scaling_factor * balance - balance
    return result


"""
Examples:
balance = $100
sf = 80 -> 0.8
result = -20
balance => 80

balance = $200
sf = 110 => 1.1
result = +20
balance = $220
"""


def display_history(results):
    current_balance = STARTING_BALANCE
    print("Results:")
    print(f"Starting balance: ${STARTING_BALANCE}")
    for result in results:
        current_balance += result
        print(f"Investment result: ${result:.2f} Balance: ${current_balance:.2f}")
    print(f"Current balance: ${current_balance:>4.2f}")


main()

# results = [-1, 2, 3, 4, -5, 20]
# display_history(results)

# print(determine_result(100))
