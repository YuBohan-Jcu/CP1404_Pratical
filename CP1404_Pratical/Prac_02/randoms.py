import random
print(random.randint(5, 20))  # line 1
#in line 1, i runed 50 times, i see different number between 5 and 20, the smallest number
#is 5 and the largest number is 20
print(random.randrange(3, 10, 2))  # line 2
#in line 2, i runed also 50 times to ensure, i see different number in 3 to 10
#and the inteval between numbers is 2, the smallest number is 3 and
#the lagest number is 9, because the interval between number is 2, so it's impossible
#to see 4 in the result, the result only be posted like 3,5,7,9
print(random.uniform(2.5, 5.5))  # line 3
#i see the different floating number between 2.5, and 5.5, the largest number is 5.5
#and the smallest number is 2.5

#1-100
import random
print(random.randint(1,100))