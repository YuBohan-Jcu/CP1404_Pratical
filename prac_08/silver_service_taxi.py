"""
CP1404_Pratical
Student Name: Yu Bohan
Student ID: 14161276
"""
from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):

    # Set flagfall
    flagfall = 4.5
    # Set the __init__() function
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    # Set the __str__() function
    def __str__(self):
        print_message = f"{super().__str__()} plus flagfall of ${self.flagfall:.1f}. "
        return print_message

    # To calculate fare
    def calculate_fare(self):
        final_fare = self.flagfall + super().get_fare()
        return final_fare