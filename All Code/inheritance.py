# class Animal:          # Parent / Base class
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound"

# class Dog(Animal):     # Child / Derived class
#     def speak(self):   # Override parent method
#         return f"{self.name} says Woof!"

# d = Dog("Rex")
# print(d.speak())       # Rex says Woof!
# print(d.name)          # Rex  ← inherited attribute.










class Animal:
    def __init__(self,name):
        self.name=name

    def name(self):
        return (f"{self.name} makes a sound. ")
class Dog(Animal):
    def speak(self):
        return (f"{self.name} says Woof!!")
d=Dog("Rex")
print(d.speak())
print(d.name)