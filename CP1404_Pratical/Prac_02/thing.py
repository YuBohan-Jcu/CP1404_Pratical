"""
CP1404 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:  #TO check the length of the passport
        return False

    count_lower = 0  # to set the number start with 0
    count_upper = 0  # same
    count_digit = 0  # same
    count_special = 0  # same
    for sth in password: # start to calculate the number
        if sth.isdigit():
            count_digit += 1
        elif sth.isupper():
            count_upper += 1
        elif sth.islower():
            count_lower += 1
        elif sth in SPECIAL_CHARACTERS:
            count_special += 1
    if count_digit == 0 or count_upper == 0 or count_lower == 0:
        return False
main()