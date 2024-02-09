class Mother:

    motherName = ""

    def mother(self):

        print(self.motherName)


class Father:

    fatherName = ""
    
    def father(self):

        print(self.fatherName)


class Son(Mother, Father):

    def parents(self):

        print("Father:", self.fatherName)
        print("Mother:", self.motherName)



son_object = Son()

son_object.fatherName = "SSSSS"
son_object.motherName = "KKKKK"

son_object.parents()