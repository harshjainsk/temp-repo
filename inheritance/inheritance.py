class Person:


    def __init__(self, fname, lname):

        self.firstname = fname
        self.lastname = lname

    
    def printName(self):

        print(f"THe name of the person is: {self.firstname} {self.lastname}!")


class Student(Person):
    
    def __init__(self, fname, lname):
        super.__init__(fname, lname)
        self.firstname = fname
    

    def printName(self):

        print(f"The first name is {self.firstname}")


p1 = Person("Harsh", "Jain")
s1 = Student("HHHHH", "JJJJJ")

p1.printName()
s1.printName()
