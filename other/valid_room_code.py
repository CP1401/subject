"""
CP1401 Demo - Valid room codes
This program shows using a Boolean-returning function, reusing that function and testing

Rules for valid room codes:
- must start with a letter
- must end with a number
- length must be 2 (B12 is not a valid room even though it's a great vitamin)
- can't have a 0 room like A0
Valid examples: A3, C1, D9
"""


def main():
    """Get and validate a room code."""
    # Get and validate a room code
    room_code = input("Room code: ")
    if is_room_code_valid(room_code):
        print(f"{room_code} is valid :)")
    else:
        print(f"{room_code} is invalid :(")

    # Keep getting room code until valid
    room_code = get_valid_room_code()
    print(f"Your room is {room_code}")


def is_room_code_valid(code):
    """Determine if a room code is valid or not."""
    # Each kind of problem is tested.
    # Note that there are no elses or elifs since the return handles this
    if len(code) != 2:
        return False
    # Note how the len check happens first, before we test if the specific characters are valid
    # We don't want to check the 2nd character if there are no characters!
    if not code.isupper():
        return False
    if not code[0].isalpha():
        return False
    if not code[1].isnumeric():
        return False
    if code[1] == '0':
        return False
    # If we get to the end, then none of the checks failed, so the code must be valid
    return True


def get_valid_room_code():
    """Get a valid room code."""
    # Note that this function reuses the existing is_room_code_valid
    # DRY!
    room_code = input("Room code: ")
    while not is_room_code_valid(room_code):
        print("Invalid room code")
        room_code = input("Room code: ")
    return room_code


def run_tests():
    """Test is_room_code_valid."""
    # One way: use print statements with known/expected outputs
    # This way, you need to use your eyes to spot any discrepancies like "True should be False"
    print(is_room_code_valid("A3"), "should be True")
    print(is_room_code_valid("3A3"), "should be False")
    print(is_room_code_valid(""), "should be False")
    print(is_room_code_valid("3A"), "should be False")
    print(is_room_code_valid("AA"), "should be False")
    print(is_room_code_valid("A0"), "should be False")

    # Another way (more advanced; we'll cover this in Programming 2)
    # The assert statement requires that the expression that follows it evaluates to True
    # and it crashes the program if the expression is False
    assert is_room_code_valid("A3")
    assert not is_room_code_valid("")  # length must be 2
    assert not is_room_code_valid("AA3")  # length must be 2
    assert not is_room_code_valid("3A")  # must start with a letter
    assert not is_room_code_valid("AA")  # must end with a number
    assert not is_room_code_valid("A0")  # can't have a 0 room
    print("All tests passed :)")


run_tests()
main()
