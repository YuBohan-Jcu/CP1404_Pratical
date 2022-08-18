"""
CP1404 Prac_05
Student Name: Yu Bohan
Student ID: 14161276
"""


is_finished = True
choose_color = {
    'Absolutezero':'#40048ba',
    'Acidzero':'#b0bfia',
    'Aqua':'#00ffff',
    'Azurer':'#f0ffff',
    'Babypink':'f4c2c2',
    'Banana yellow':'ffe135',
    'Beige':'#f5f5dc',
    'Bisquel':'#ffe4c4',
    'Black':'000000',
    'Bole':'#79443b'
}
choice_color = input("Choose a color: ").title()  # help user more easier to find code
while is_finished != False:
    if choice_color in choose_color:
        choice_value = choose_color.get(choice_color)# Set when its avaliable
        print(f"{choice_color}'s code is {choice_value}")
    elif choice_color == "":
        print(f"{choice_color}' is not exit, please try again.")
    else:
        print(f"{choice_color} is not exit, please try again.")
    choice_color = input("Choose a color: ").title()
