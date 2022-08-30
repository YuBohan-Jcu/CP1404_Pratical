'''
CP1404 prac_06
Name: YuBohan
StudentID: 14161276
Date: 28/08/2022
'''


class Car:

    name = ''

    def __init__(self, n, fuel=0):
        self.fuel = fuel
        self.name = n
        self.odometer = 0

    def __str__(self):
        return "%s, fuel = %d, odometer = %d"%(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance