class A:
    def display(self):
        print("This is parent class 1")

class B(A):
    def display(self):
        super().display()
        print("This is child class 2")

object=B()
object.display()
# object.display()