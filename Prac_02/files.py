open_file = open('name.txt')
print(f"Your name is {open_file.read()}")
number_file = open('number.txt','r')
total = int(number_file.readline())+int(number_file.readline())  # First number of list plus second number of list
print(total)

#
numbers_file = open('number.txt','r')
print(numbers_file.read())
