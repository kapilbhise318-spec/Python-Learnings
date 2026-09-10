class A:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def get_info_student(self):
        return (f"my name is {self.name} and my age is {self.age}, i live in {self.city}.")
    
class B(A):
    def student_details(self):

        print(f"{self.name}")



# Polymoprism in Action...

C=B("Ajay",32,"Mumbai")


print(C.get_info_student())

print(C.student_details())