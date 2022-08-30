'''
CP1404 prac_06
Name: YuBohan
StudentID: 14161276
Date: 28/08/2022
'''

from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    limo = Car('limo',100)   # Set 100 fuel for car - limo
    limo.add_fuel(20)        # Add 20 fuel in car - limo
    print(limo.fuel)         # Print result


main()