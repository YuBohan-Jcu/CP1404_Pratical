"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sale = float(input("Putting sales in here:$"))  # in here we put number in the first step
while sale >= 1000:   # if your sale is over or equal $1000
    bonus = sale * 0.15  # you get 10% of the sale number
    print(f"Your Bonus is ${bonus:.2f}")
    sale = float(input("Putting sales in here:$"))
    if sale < 1000:   # if sale under $1000
        bonus = sale * 0.1  # you get 10% of the sale number
        print(f"Your Bonus is ${bonus:.2f}")
        sale = float(input("Putting sales in here:$"))