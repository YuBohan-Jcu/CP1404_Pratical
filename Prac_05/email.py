"""
CP1404 Prac_05
Student Name: Yu Bohan
Student ID: 14161276
"""

is_finished = True
def main():
    storage = {}
    while is_finished != False:
        enter_email = input("Enter your email: ")
        if enter_email == "":
            print("\nEmail:")
            for x,y in storage.items():
                print(f"{x.title()}({y.title()})")
            exit()
        name = enter_email.split("@")
        while is_finished != False:
            choose = input(f"Is your name {name[0].title()}? (Y/n)").lower()
            if choose == "y":
                storage[name[0]] = enter_email
                break
            elif choose == "n":
                enter_name = input("Name: ")
                storage[enter_name] = enter_email
                break
            else:
                print("Invalid choose")
main()