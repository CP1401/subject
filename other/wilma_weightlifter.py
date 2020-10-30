"""
CP1401 Do This Now - Live Session 27/10/2020

Today's programming challenge:
Wilma Weightlifter weally wants to keep track of her lifts
Each gym sesh, she should enter how many lifts and the weights she lifted
Your useful program should show her the total weight lifted
If a lift is a PB (highest ever), she wants some serious smileys :) :)
She don't want no bad data like negs in her stats
She doesn't always remember her PB, so this needs to be stored between runs

total = 0
open "pb.txt" as file_in for reading
get pb from file_in
close file_in
pb = ... get pb from file
get number_of_lifts
repeat number_of_lifts times
    get current_weight
    while current_weight < 0
        print error
        get current_weight
    total = total + current_weight
    if current_weight > pb
        print smileys
        pb = current_weight
print total
open "pb.txt" as file_out for writing
write pb to file_out
close file_out
"""


def main():
    total = 0
    is_pb = False
    filename = "pb.txt"

    pb = get_pb(filename)
    number_of_lifts = int(input("Number of lifts: "))
    for i in range(number_of_lifts):
        current_lift = float(input("Lift weight (kg): "))
        while current_lift < 0:
            print("Error")
            current_lift = float(input("Lift weight (kg): "))
        total += current_lift
        if current_lift > pb:
            print(":) :)")
            pb = current_lift
            is_pb = True
        print(total)
    if is_pb:
        save_pb(filename, pb)


def save_pb(filename, pb):
    file_out = open(filename, "w")
    print(pb, file=file_out)
    file_out.close()


def get_pb(filename):
    try:
        file_in = open(filename, "r")
        pb = float(file_in.read())
        file_in.close()
    except FileNotFoundError:
        pb = 0.0
    return pb


main()
