"""
CP1404_Pratical
Student Name: Yu Bohan
Student ID: 14161276
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

# Set the title
print("Let's drive!")
# Menu should be posted
Menu = "q)uit, c)hoose taxi, d)rive"
print(Menu)

def main():
    # User can choose here
    choose = input(">>> ").lower()
    # The avaliable Taxi be posted
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
                    SilverServiceTaxi("Hummer", 200, 4)]
    # From Beginning we have no Taxi
    current_taxi = None
    # Set a bill from 0
    total = 0
    # use a while function make sure before quit it can always ask
    while choose != "q":
        # Taxi list and Information post
        if choose == "c":
            print("Taxi Avaliable: ")
            list_taxi(taxis)
            print("flagfall of $4.50")
            # What type Taxi they want
            choose_taxi = int(input("Choose taxi: "))
            # Value check
            try:
                current_taxi = taxis[choose_taxi]
            except IndexError:
                print("Invalid taxi choice")
        # fee should be post
        elif choose == 'd':
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                travel_fee = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${travel_fee:.2f}.")
                total += travel_fee
            else:
                print("You need to choose a taxi before you can drive")
        #  error checking of choice
        else:
            print("Invalid option")
        # Ensure that the following message is printed after each loop
        print("Bill to date: ${:.2f}".format(total))
        print(Menu)
        choose = input(">>> ").lower()
    # when while loop end
    print("Total trip cost: ${:.2f}".format(total))
    print("Taxis are now:")
    list_taxi(taxis)

# set a for,in function to enumerate the information of taxis
def list_taxi(taxis):
    for i,taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()