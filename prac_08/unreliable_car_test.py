from prac_08.unreliable_car import UnreliableCar


def main():
    """Do a Test of unreliable_car.py"""
    test_car = UnreliableCar('Mosoko', 200, 5)
    test_car.drive(20)
    print(test_car)
main()