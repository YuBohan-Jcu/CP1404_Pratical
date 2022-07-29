is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        break   # Using break to stop the recycle.
    except ValueError:  # Using an value error checking to make sure that it is actually a number
        print("Please enter a valid integer.")
print("Valid result is:", result)