"""
CP1404_Pratical
Student Name: Yu Bohan
Student ID: 14161276
"""
from random import randint
from prac_08.car import Car

class UnreliableCar(Car):

    # inherit
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliablity = reliability

    # Set another function drive()
    def drive(self, distance):
        a_random_number = randint(0,100)
        if a_random_number > self.reliablity:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
