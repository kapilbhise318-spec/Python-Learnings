class Student:

    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage

    def get_data(self):
        return (self.percentage>90)
    
Student1=Student("Kapil","A",95)
print(Student1.get_data())   # Reutrn True or False
print(Student1.name, Student1.grade, Student1.percentage)
print(Student1.grade)
print(Student1.percentage)