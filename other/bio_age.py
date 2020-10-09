"""
CP1401 Do This Now - Live Session 09/10/2020
Write a program to determine someone's "bio age" based on their real age
and life experiences

Get their real age at the start (between 0 and a MAX of 120)
Menu:
Lie down - adds 1 to bio age
Hack assignment - doubles bio age
Take unknown substance - randomly modifies bio age (you decide; can go up or down)
Quit - at end, print their final real age and bio age and the difference
Each time through menu loop:
- real age goes up 1
- print real & bio age
Bio age can never be lower than 0 (you control this)

The following is a somewhat-incomplete solution created with the class

Pseudocode:
MAXIMUM_REAL_AGE = 120

function main
    real_age = get_valid_age(MAXIMUM_REAL_AGE)
    bio_age = real_age

    display menu
    get choice
    while choice != Q
        if choice == L
            bio_age = lie_down(bio_age)
        else if choice == H
            bio_age = hack_assignment(bio_age)
        else if choice == T
            bio_age = take_substance(bio_age)
        else
            display invalid input error message
        real_age = real_age + 1
        display real_age, bio_age
        display menu
        get choice

    print final age and bio age and the difference

function get_valid_age(maximum_age)
    get age
    while age < 0 or age > maximum_age
        display invalid message
        get age
    return age

# Not like this:
function modify_bio_age(choice)
    if choice == L
        bio_age + 1
    ...
"""

import random

RANDOM_CHANGE_AMOUNT = 50
MAXIMUM_REAL_AGE = 120
MENU = """> (L) Lie down - adds 1 to bio age
> (H) Hack assignment - doubles bio age
> (T) Take unknown substance - randomly modifies bio age
> (Q) Quit
>>  """


def main():
    real_age = get_valid_age(MAXIMUM_REAL_AGE)
    bio_age = real_age

    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            bio_age = lie_down(bio_age)
        elif choice == "H":
            bio_age = hack_assignment(bio_age)
        elif choice == "T":
            bio_age = take_substance(bio_age)
        else:
            print("Invalid choice")
        real_age += 1
        print(f"Real age: {real_age}. Bio age: {bio_age}")
        choice = input(MENU).upper()
    print(f"Real age: {real_age}. Bio age: {bio_age} (difference: {bio_age - real_age})")


def get_valid_age(maximum_age):
    age = int(input("Age: "))
    while age < 0 or age > maximum_age:
        print("Invalid age!")
        age = int(input("Age: "))
    return age


def lie_down(bio_age):
    return bio_age + 1


def take_substance(bio_age):
    random_change = random.randint(-RANDOM_CHANGE_AMOUNT, RANDOM_CHANGE_AMOUNT)
    # print(random_change)  # Debug so we know what's happening
    bio_age = bio_age + random_change
    if bio_age > 0:
        return bio_age
    return 0


def hack_assignment(bio_age):
    return bio_age * 2


main()
