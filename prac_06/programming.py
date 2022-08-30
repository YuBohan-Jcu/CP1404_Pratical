'''
CP1404 prac_06
Name: YuBohan
StudentID: 14161276
Date: 28/08/2022
'''


class ProgrammingLanguage:
    field ='',
    typing = '',
    reflection = '',
    year = '',
    def __init__(self,f,t,r,y):
        self.field = f
        self.typing = t
        self.reflection = r
        self.year = y

    def __str__(self):
        return "%s, %s Typing, Reflection = %s, First appeared in %d"%(self.field, self.typing, self.reflection,
                                                                       self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"

def check_process():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    fields = ['ruby','python','visual_basic']
    print(python)
    print("The dynamically typed languages are:")
    for i in fields:
        if i.is_dynamic():
            print(i.t)

if __name__ == "__main__":
    check_process()