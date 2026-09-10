# Inheritance in Python

# Inheritance allows a child class to use the properties 
# and methods of a parent class.

# Syntax:

# class Parent:
#     # properties and methods


# class Child(Parent):
#     # child properties and methods
# 1. Single Inheritance

# One parent → one child

# class Animal:
#     def eat(self):
#         print("Animal is eating")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")


# d = Dog()

# d.eat()    # parent method
# d.bark()   # child method

# Output:

# Animal is eating
# Dog is barking
# 2. Multilevel Inheritance

# Grandparent → Parent → Child

# class Grandfather:
#     def house(self):
#         print("Grandfather house")


# class Father(Grandfather):
#     def car(self):
#         print("Father car")


# class Son(Father):
#     def bike(self):
#         print("Son bike")


# s = Son()

# s.house()
# s.car()
# s.bike()

# Output:

# Grandfather house
# Father car
# Son bike
# 3. Multiple Inheritance

# One child inherits from multiple parents

# class Father:
#     def money(self):
#         print("Father money")


# class Mother:
#     def gold(self):
#         print("Mother gold")


# class Child(Father, Mother):
#     def study(self):
#         print("Child studies")


# c = Child()

# c.money()
# c.gold()
# c.study()

# Output:

# Father money
# Mother gold
# Child studies
# 4. Hierarchical Inheritance

# One parent → multiple children

# class Animal:
#     def eat(self):
#         print("Eating")


# class Dog(Animal):
#     def bark(self):
#         print("Barking")


# class Cat(Animal):
#     def meow(self):
#         print("Meowing")


# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()

# Output:

# Eating
# Barking
# Eating
# Meowing
# 5. Hybrid Inheritance

# Combination of multiple inheritance types

# class A:
#     def show(self):
#         print("Class A")


# class B(A):
#     pass


# class C(A):
#     pass


# class D(B, C):
#     pass


# obj = D()

# obj.show()

# Output:

# Class A
# Constructor Inheritance Example (super())
# class Person:
#     def __init__(self, name):
#         self.name = name


# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age


# s = Student("Kapil", 22)

# print(s.name)
# print(s.age)

# Output:

# Kapil
# 22
# Types of inheritance in Python:
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance