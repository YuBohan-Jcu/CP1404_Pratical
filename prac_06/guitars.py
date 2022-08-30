from prac_06.guitar import guitar

def main():
    guitar_a = []
    print("My guitars!")
    n = input("Name: ")
    while n != "":
        y = int(input("Year: "))
        c = float(input("Cost: $"))
        adding_guitar = guitar(n,y,c)
        guitar_a.append(adding_guitar)
        print(f"{n} ({y}) : ${c} added.")
        n = input("Name: ")

    guitar_a.append(guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_a.append(guitar("Line 6 JTV-59", 2010, 1512.9))

    guitar_a.sort(key=lambda x: 1 / x.age)
    if guitar_a:
        print("These are my guitars:")
        for i, guitars in enumerate(guitar_a):
            string = " (vintage)"
            if guitars.is_vintage():

                print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guitars, string))
            else:
                print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}".format(i + 1, guitars))


main()




