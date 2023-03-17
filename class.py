class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(self.firstname, self.lastname)


class student(Person):
    pass
num1 = student("Mike", "Olivie")
person1 = Person("John", "Utah")
person1.printname()
num1.printname()
