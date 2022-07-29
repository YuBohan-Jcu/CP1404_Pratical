"""
CP1404/CP5632 - Practical 1
Name: Yu Bohan
Student ID:14161276
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit:"))   # put fahrenheit number in
        celsius = 5/9*(fahrenheit - 32)   # put the equation here
        print(f"Result:{celsius:.2f} C")  # put the result here using format function
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")