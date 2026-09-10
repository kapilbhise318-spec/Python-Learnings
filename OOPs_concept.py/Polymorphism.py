# Polymorphism in Python

# Polymorphism means "many forms". It allows the same method,
#  function, or operator to behave differently depending on the 
# object or data type.

# In Python, polymorphism is mainly achieved through:

# Method Overriding
# Operator Overloading
# Duck Typing
# 1. Method Overriding

# A child class provides a different implementation of a method that already 
# exists in the parent class.

# Example:
# class Animal:

#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")


# class Cat(Animal):

#     def sound(self):
#         print("Cat meows")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()
# Output:
# Dog barks
# Cat meows

# Here, the same method sound() behaves differently for Dog and Cat.

# 2. Operator Overloading

# The same operator works differently with different data types.

# Example:

# print(5 + 10)

# print("Hello " + "Python")

# Output:

# 15
# Hello Python

# + adds numbers and joins strings.

# 3. Duck Typing

# Python allows objects to be used based on their behavior, not their class.

# Example:

# class Dog:
#     def sound(self):
#         print("Bark")


# class Cat:
#     def sound(self):
#         print("Meow")


# def make_sound(animal):
#     animal.sound()


# d = Dog()
# c = Cat()

# make_sound(d)
# make_sound(c)

# Output:

# Bark
# Meow

# The function only cares that the object has a sound() method.

# Polymorphism with Built-in Functions

# Same function works with different objects:

# print(len("Python"))

# print(len([1,2,3,4]))

# Output:

# 6
# 4

# len() works with strings, lists, tuples, etc.

# Advantages of Polymorphism
# Makes code flexible
# Reduces code duplication
# Easier to maintain
# Allows different objects to share the same interface

# In short:
# Polymorphism = One name, many behaviors
# Example: sound() method gives different outputs for different animals.




print(5 + 10)

print("Hello " + "Python")