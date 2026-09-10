class Student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.__percentage=percentage

    def get_percentage(self):
        return self.__percentage
    
Student1=Student("Madhav","B",98)

print(F"{Student1.name}' percentage is {Student1.get_percentage()}%.")

print(Student1.__percentage)