class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def get_grade(self):
        return(F"{self.name} is a grade in {self.grade}.")
    
Student1=Student("Kapil","A")
# print("Name of student is",Student1.name)
# print("and his grade is",Student1.grade)
print(Student1.get_grade())
print(type(Student))

