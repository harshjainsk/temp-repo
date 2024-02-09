class Parent:

    def func1(self):

        print("This is in the parent fucntion!")


class Child(Parent):

    def func2(self):

        print("This is in the child function")


child_object = Child()

child_object.func1()

child_object.func2()