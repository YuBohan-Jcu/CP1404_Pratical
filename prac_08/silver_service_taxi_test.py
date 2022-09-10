"""
CP1404_Pratical
Student Name: Yu Bohan
Student ID: 14161276
"""
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    # To test the price
    test_run = SilverServiceTaxi('Benz', 145, 2)  # information provided
    test_run.drive(18)  # 18km
    print(test_run)  # print the message
    print(f"${test_run.calculate_fare()}")  # count fare

if __name__ == "__main__":
    main()