# print the odd number between 1 to 20
for odd_number in range(1,21,2):    # 1,3,5...,so plus 2 space
    print(odd_number, end=' ')
print()
for value in range(0,100,10):   # 0,10,20,..., so plus 10
    print(value,end=" ")
print()
for doc in range(20,0,-1):     # 20,19,18,...., so plus -1
    print(doc,end=" ")
print()

# stars
put_star = int(input("Number of star:"))
star = "*"      # Set the star looks
count_star = put_star * star   # using the calculator to achieve
print(count_star)
n = int(input("Enter Number:"))
for i in range(n):    # using range() to make it 
    print(i*'*')