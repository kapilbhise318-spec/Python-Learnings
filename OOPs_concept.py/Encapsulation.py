# Encapsulation in Python:->

# Encapsulation is an OOP concept that combines data (variables) and methods
#  (functions) into a single unit (class) and restricts direct access to some data.

# Goal: Protect data from unwanted changes and control how it is accessed.

# Real-Life Example

# A bank account: You cannot directly change your account balance.
#  You use methods like deposit() and withdraw() to modify it safely.

# Example of Encapsulation in Python
# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance   # private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance


# account = BankAccount(5000)

# account.deposit(2000)

# print(account.get_balance())
# Output:
# 7000

# Here:

# __balance is a private variable
# It cannot be accessed directly from outside the class
# It can be modified only through methods
# Trying to Access Private Variable
# print(account.__balance)

# Output:

# AttributeError: 'BankAccount' object has no attribute '__balance'
# Types of Access Modifiers in Python
# 1. Public

# Accessible anywhere.

# class Student:
#     def __init__(self):
#         self.name = "Kapil"

# s = Student()
# print(s.name)

# Output:

# Kapil
# 2. Protected (_)

# Accessible inside class and subclasses (by convention).

# class Student:
#     def __init__(self):
#         self._marks = 90
# 3. Private (__)

# Accessible only inside the class.

# class Student:
#     def __init__(self):
#         self.__marks = 90
# Encapsulation Using Getter and Setter
# class Student:

#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks


# s = Student()

# s.set_marks(95)

# print(s.get_marks())

# Output:

# 95
# Abstraction vs Encapsulation
# Abstraction	Encapsulation
# Hides implementation details	Hides data
# Focuses on what an object does	Focuses on protecting data
# Uses abstract classes	Uses private/protected variables
# Example: Car driving system	Example: Bank account balance

# In short:

# Abstraction → hides complexity
# Encapsulation → protects data














# cOdE-->

# class BankAccount:

#     def __init__(self,balance):
#         self.__balance= balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance
    
# account=BankAccount(10000)
# account.deposit(5000)
# print('Current Balance: $',account.get_balance())



# Types of Access modifiers in python...
# (public, protected(_), private(__))




# 1). Public Access modifiers...  -Accessible Anywhere.
# class Student:
#     def __init__(self):
#         self.name='kapil'
# s=Student()
# print(s.name)


# protected (_)  -Accessible inside the class and subclasses.
# class Student:
#     def __init__(self):
#         self._name='kapil'
# s=Student()
# print(s._name)


# 3).Private(__)   --Accesible only insid the class.

# class Student:
#     def __init__(self):
#         self.__marks= 90

    
#     def get_marks(self):
#         return self.__marks

# s=Student()
# print("You've got.",s.get_marks())


# Encapsulation using getters and setters methods...

class Student:

    def __init__(self):
        self.__marks=90

    def set_marks(self,marks):
        self.__marks=marks

    def get_marks(self):
        return self.__marks

s=Student()
s.set_marks(952)
print(s.get_marks())