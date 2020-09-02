"""
CP1401 Example (from Help Session 01/09/2020)
Score -> Result program with menu, accumulation, etc.
(a bit similar to smiley, frowny from prac 4)

Now with added functions.
This version improves on the previous one by removing the duplication (DRY)
of the section that prints the status.
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 10
MENU = """Menu:
- instructions
- enter score
- print status
- quit
> """


def main():
    """Program to determine smileyness of scores"""
    total_score = 0
    number_of_scores = 0
    print(MENU, end="")
    choice = input().lower()
    while choice != "q":
        if choice == 'i':
            print("Instructions")
        elif choice == 'e':
            score = int(input(f"Enter score {number_of_scores + 1}: "))
            while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
                print(f"Invalid score. Score must be between {MINIMUM_SCORE} and {MAXIMUM_SCORE}")
                score = int(input(f"Enter score {number_of_scores + 1}: "))
            # print # of smileys that matches their score
            # 3 -> :):):)
            for i in range(score):
                print(":)", end="")
            print()  # Note, we could also just use print(":)" * score)
            total_score += score
            number_of_scores += 1
        elif choice == 'p':
            print_status(number_of_scores, total_score)
        else:
            print("Invalid choice")
        print(MENU, end="")
        choice = input().lower()
    print("Finished")
    print_status(number_of_scores, total_score)


def print_status(number_of_scores, total_score):
    """Display current status of scores entered so far"""
    if number_of_scores > 0:
        average = total_score / number_of_scores
        print(f"From {number_of_scores} scores, total is {total_score}.")
        if average < 5:
            status_word = "bad"
        else:
            status_word = "good"
        print(f"The average score is {average}, which is {status_word}.")
    else:
        print("No scores.")


main()
