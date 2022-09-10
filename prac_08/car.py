"""
CP1404_Pratical
Student Name: Yu Bohan
Student ID: 14161276
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance