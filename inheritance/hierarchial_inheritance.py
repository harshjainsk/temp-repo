class Parent:

    def func1(self):

        print("This is the PArent class")

class Child1(Parent):

    def func2(self):

        print("This is child1 class")

class Child2(Parent):

    def func3(self):

        print("This is child3 class")


child1_object = Child1()

child1_object.func1()
child1_object.func2()


child2_object = Child2()

child2_object.func1()
child2_object.func3()

