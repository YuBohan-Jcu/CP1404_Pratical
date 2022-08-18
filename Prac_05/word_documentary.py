"""
CP1404 Prac_05
Student Name: Yu Bohan
Student ID: 14161276
"""


text = input("Text: ")
devide_up = text.split()
count = {}
for i in devide_up:
    count[i] = count.get(i,0) + 1
for x,y in count.items():
    print('{:5}: {}'.format(x,y))