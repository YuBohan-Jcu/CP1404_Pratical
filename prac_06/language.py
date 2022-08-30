'''
CP1404 prac_06
Name: YuBohan
StudentID: 14161276
Date: 28/08/2022
'''

from prac_06.programming import ProgrammingLanguage
def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    fields = [ruby,python,visual_basic]
    print(python)
    print("The dynamically typed languages are:")
    for i in fields:
        if i.is_dynamic():
            print(i.field)

main()