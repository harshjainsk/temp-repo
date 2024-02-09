#base Class

class GrandFather:

    def __init__(self, grandFatherName):

        self.grandFatherName = grandFatherName



# intermediate Class
        
class Father(GrandFather):

    def __init__(self, fatherName, grandFatherName):

        self.fatherName = fatherName

        GrandFather.__init__(self, grandFatherName)


# derived class
        
class Son(Father):

    def __init__(self, sonName, fatherName, grandFatherName):

        self.sonName = sonName

        Father.__init__(self, fatherName, grandFatherName)

    
    def print_names(self):
        
        print("GrandFather's name is:", self.grandFatherName)
        print("Father's name is:", self.fatherName)
        print("Son's name is:", self.sonName)


son_object = Son("Lov and Kush", "Ram", "Dashrath")
son_object.print_names()
