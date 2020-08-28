"""
CP1401 Example (from Help Session 28/08/2020)
Score -> Result program with menu, accumulation, etc.
(a bit similar to smiley, frowny from prac 4)
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 10
MENU = """Menu:
- (i)nstructions
- (e)nter score
- (p)rint status
- (q)uit
> """
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
            print(f"Invalid score. Score must be between {MINIMUM_SCORE} and {MAXIMUM_SCORE}.")
            score = int(input(f"Enter score {number_of_scores + 1}: "))
        # print # of smileys that matches their score
        # 3 -> :):):) (0-10)
        for i in range(score):
            print(":)", end="")
        print()  # Note, we could also just use print(":)" * score)
        total_score += score
        number_of_scores += 1
    elif choice == 'p':
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
    else:
        print("Invalid choice")
    print(MENU, end="")
    choice = input().lower()
print("Finished")
# Oh my gosh... look how much of this code is copy-pasted (repeated)!
# We should feel concerned by this... and we'll solve the problem using...
# Functions!
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
