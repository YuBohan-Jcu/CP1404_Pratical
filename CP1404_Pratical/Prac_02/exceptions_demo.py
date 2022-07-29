try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
# When the input is not a number, it will show Value error, for example: x9(Which is not a number)
# When the one of numerator or denominator is 0 or both are 0, ZeroDevisionError will occur
# I think that is not possible to change it, i've tried using if,else, but the if,else function() doesn't work when 0
# put in whether numerator or denominator, some other function i also tried, result same, zerodevisionerror is an errorchecking
# so i don't think it can be replaced by other function.
