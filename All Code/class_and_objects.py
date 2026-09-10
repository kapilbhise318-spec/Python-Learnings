class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks

    def average(self):
        return sum(self.marks)/len(self.marks)

a=Student(101,"Sahil",[69,96,35,87,91])
print("The student's roll_no is ",a.roll_no)
print("The student's name is ",a.name)
print("Marks of student is ",a.marks)
print("The average of marks is ",a.average())