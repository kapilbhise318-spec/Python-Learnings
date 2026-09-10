class A:
    def name(self):
        print("Welcome")

    def name(self, first_name=""):
        print("Welcome",first_name)

    def name(self,first_name="",last_name=""):
        print("Welcome",first_name,last_name)

obj=A()
obj.name()
obj.name("Sahil")
obj.name("Sahil","Gaikwad")



# method overloading = same method or functions but 
# diffrent parameters or behavior