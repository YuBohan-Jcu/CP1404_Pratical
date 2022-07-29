"""
CP1404 - Practical 3
Name: Yu Bohan
Student ID：14161276
Using def() function to rearrange the program
"""



def main():  # Set the main function
    score = float(input("Enter score: "))    # Enter your score here
    determine_score = evaluate_score(score)  # Set a function to evaulate the score
    print(determine_score)                   # Print the result of the evaluate function

def evaluate_score(score):                   # Get the evaluate score here
    if 100 >= score >= 90:                   # Define different situation
        return "Excellent"
    elif 50 <= score < 90:
        return "Pass"
    elif 0 < score < 50:
        return "Bad"
    else:
        return "Invalid Score"


main()                                      # Run function