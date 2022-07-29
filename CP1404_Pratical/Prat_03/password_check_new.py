"""
CP1404 - Practical 3
Student Name: YuBohan
Student ID: 14161276
Using a function to make an password length checking program and shows up with '*'
"""

MIN_LENGTH = 5   # Set the minimum number
is_finished = False
def main():           # Set the main function
    password = input("Enter your Password here >>> ")  # User can enter a passport
    check_pass = password_check(password)  # Using a function to check the passport which user entered

def password_check(password):   #Set the rule of this function
    while is_finished != True:  # Using a while function to repeat ask user to reset password when its too short
        if len(password) < MIN_LENGTH:    # As request, password length cannot less than 5 chracters
            print("Your Passport is too short")      # if yes, should be rearrange one
            password = input("Enter your Password here >>> ")   # reinput
        else:    # if no
            print(len(password)*"*")   #They can see the length of it
            break   # when no, recycle should be stop

main()