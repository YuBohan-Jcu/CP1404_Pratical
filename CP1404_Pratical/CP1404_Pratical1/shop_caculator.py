total = 0
item = int(input("Number of item:"))  # put the number here
if item < 0:    # Add an error checking
    print("Invalid number of items!Please Putting again")
    item = int(input("Number of item:"))
for price in range(item):      # using range() to print the number of item
    price = float(input("Price of item:"))   # Put the price here
    if price < 0:     # Add an error checking with the price number
        print("Invalid Price!Please reputting it!!!")
        price = float(input("Price of item:"))
    total += price    # total = the sum of price
    if total >= 100:  # if the total number over 100
        final_price = total * 0.9   # get the final number
print(f"Total Price of {item} items is ${final_price:.2f}")
