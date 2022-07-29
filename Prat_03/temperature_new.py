"""
CP1404 - Practical 3
Name: Yu Bohan
Student ID:14161276
Using def() to replace the program
"""

def main():
    MENU = """\tC - Convert Celsius to Fahrenheit  
    F - Convert Fahrenheit to Celsius
    Q - Quit"""  # Set the Menu
    print(MENU)  # TO put the menu to customer
    choice = input(">>> ").upper()      # Customer will choose option here
    eval_choice = evaluating_choice(choice,MENU)  # Put an estimate process funciton here

def evaluating_choice(choice,MENU):   # TO fill the function to estimate the cutomer's choose
    while choice != "Q":              # When choice is not quit then ...
        if choice == "C":             # choice celsius calculate will ...
            celsius = float(input("Celsuis: "))  # then a number should be put in here to calculate
            fahrenheit = get_fahrenheit(celsius) # Set another function to calculate
            print(f"Result: {fahrenheit:.2f} F") # Get the result here
            print(MENU)                          # Out of the cycle help cutomer to rechoose the menu
            choice = input(">>> ").upper()       # customer will choose new option here
        elif choice == "F":                      # Set the option with when choose fahrenheit
            fahrenheit = float(input("Fahrenheit:")) # Number here
            celsius = get_celsius(fahrenheit)        # Set the function here
            print(f"Result: {fahrenheit:.2f} C")     # What the print result looks like
            print(MENU)
            choice = input(">>> ").upper()
        else:                                        # When the choice is not in option, this line will come out
            print("Invalid Choice")                  # option not valid
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you")

def get_fahrenheit(celsius):                    # Set the def function of deverse from celsius to fahrenheit
    return celsius * 9.0 / 5 + 32

def get_celsius(fahrenheit):                    # Set the def function of deverse from fahrenheit to celsius
    return 5 / 9 * (fahrenheit - 32)

main()                                          # Run all function