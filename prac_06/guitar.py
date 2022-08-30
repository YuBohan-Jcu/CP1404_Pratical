'''
CP1404 prac_06
Name: YuBohan
StudentID: 14161276
Date: 28/08/2022
'''


now_time = 2020
standard = 50


class guitar:
    def __init__(self, n, y, c):
        self.name = n
        self.year = y
        self.cost = c
        self.age = now_time - y

    def __str__(self):
        return "%s (%d) : %d" % (self.name, self.year, self.cost)

    # def get_age(self):
    #     self.age = now_time - self.year
    #     return self.age

    def is_vintage(self):
        return self.age >= standard

    def _It_(self, other):
        return self.year < other.year


