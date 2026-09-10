# Abstraction in Python

# Abstraction is an Object-Oriented Programming (OOP) concept
#  that hides the implementation details and shows only the essential 
# features of an object.

# Goal: Focus on what an object does rather than how it does it.

# Real-Life Example

# When you drive a car, you use the steering wheel, accelerator, 
# and brake pedals. You don't need to know how the engine works internally. 
# This is abstraction.

# Abstraction Using Abstract Classes

# Python provides the ABC (Abstract Base Class) module to implement abstraction.

# Example
# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):

#     def sound(self):
#         return "Bark"

# class Cat(Animal):

#     def sound(self):
#         return "Meow"

# dog = Dog()
# cat = Cat()

# print(dog.sound())  # Bark
# print(cat.sound())  # Meow
# Output
# Bark
# Meow
# Key Points
# Abstract Class
# A class that contains one or more abstract methods.
# Cannot be instantiated directly.
# Abstract Method
# A method declared using @abstractmethod.
# Must be implemented by child classes.
# Example: Instantiating an Abstract Class
# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# s = Shape()  # Error

# Error:

# TypeError: Can't instantiate abstract class Shape


# Benefits of Abstraction:

# Hides complex implementation details.
# Improves code security.
# Reduces code complexity.
# Makes code easier to maintain and extend.
# Enforces a common interface across subclasses.


# Difference Between Abstraction and Encapsulation

# Abstraction	                                      Encapsulation
# -Hides implementation details	                       - Hides data
# -Focuses on "what" an object does	                   - Focuses on "how" data is protected
# -Implemented using abstract classes/interfaces	   - Implemented
                                                    #  - using access modifiers and getters/setters

# In short:
#  Abstraction means exposing only the necessary
#  functionality while hiding internal implementation details.



# Code

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
dog=Dog()
cat=Cat()

print('The sound of dog while barking...', dog.sound())
print('The sound of cat while talking...', cat.sound())