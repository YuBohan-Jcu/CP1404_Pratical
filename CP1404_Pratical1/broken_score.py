"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))    # Put the score here
if 100 >= score >= 90:   # Set the score between 100(=) and 90(=)
    print("Excellent")
elif 50 <= score < 90:  # Set the score between 50(=) and 90(less)
    print("Pass")
elif 0 < score < 50:    # Set the score between less than 50
    print("Bad")
else:                   # other option all wrong
    print("Invalid Score")