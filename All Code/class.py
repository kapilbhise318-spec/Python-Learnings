class Faculty:
    def putdata(self):
        self.id=int(input("Enter a faculty's ID "))
        self.name=input("Enter faculty name ")
        self.salary=int(input("Enter faculty's Salary "))
    
    def display(self):
        print("\nFaculty ID is", self.id)
        print("Faculty name is",self.name)
        print("Faculty Salary is",self.salary)

a=Faculty()
a.putdata()
a.display()