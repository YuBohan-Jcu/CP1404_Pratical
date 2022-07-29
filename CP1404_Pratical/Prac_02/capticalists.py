
"""
CP1404 - Practical
"""
import random

MAX_INCREASE = 0.175  # change it to 17.6%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0   #change max price to 100
INITIAL_PRICE = 10.0
DAY = 0   #Put the day defination in here
out_file = open('OUTPUT_FILE','w')  #open file to write

price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))  #To put the starting price in


while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    DAY += 1   #The day will plus with the hole range
    print(f"On day {DAY} price is ${price:,.2f}",file = out_file)  #plus some element to make it true

    out_file.close() #when it printed , close the file