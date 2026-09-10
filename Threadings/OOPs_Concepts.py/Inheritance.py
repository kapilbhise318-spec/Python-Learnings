class Student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage


    def student_details(self):
        print(f"{self.name} is in {self.grade} {self.percentage}%.")


class A(Student):
    def __init__(self, name, grade, percentage,stream):

        
        super().__init__(name, grade, percentage)

        self.stream=stream

    
    def student_details(self):
        super().student_details()
        print(f"and the stream is {self.stream}")


Graduate_Student=A("Kapil","A",95,"PCMB")

Graduate_Student.student_details()


















