"""
CP1404_Pratical
Student Name: Yu Bohan
Student ID: 14161276
"""
from prac_08.taxi import Taxi

def main():
    # Put the information here
    new_taxi = Taxi('Prius 1', 100)
    new_taxi.drive(40)  # Car drive 40 unit
    print(f"{new_taxi.__str__()}")  # Using the __str__ function to print it out

    # Restart the Taxi
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(f"{new_taxi.__str__()}")


if __name__ == "__main__":
    main()