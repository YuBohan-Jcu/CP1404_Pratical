'''
CP1404 prac_06
Name: YuBohan
StudentID: 14161276
Date: 28/08/2022
'''


from prac_06.guitar import guitar

standard = 50

def test():
    n = "Gibson L-5 CES"
    y = 1922
    c = 16035.40

    original = guitar(n,y,c)
    others = guitar('Other one Info', 1987, 4845.90)

    print(f"{original.name} get_age() - Expected {original.get_age()}. Got {original.get_age()}")
    print(f"{others.name} get_age() - Expected {others.get_age()}. Got {others.get_age()}")
    print(f"{original.name} is_vintage() - Expected {original.is_vintage()}. Got {original.is_vintage()}")
    print(f"{others.name} is_vintage() - Expected {others.is_vintage()}. Got {others.is_vintage()}")

if __name__ == '__main__':
    test()
