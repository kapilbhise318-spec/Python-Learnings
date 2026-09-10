# __Init__ constructor with Parameters

class Employee:
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept

e1=Employee('Rahul',27,'IT')

print(e1.name)
print(e1.age)
print(e1.dept)


# __init__() with default counstructor...

class A:
    def __init__(self):
        self.color='Red'
a=A()
print(a.color)



# After django Aunthentications...

# Django Forms & ModelForms
# Custom User Model
# JWT Authentication (Django REST Framework)
# Permissions & Authorization
# Social Login (Google/GitHub)