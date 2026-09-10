# Method Resolution Order in Python Inheritance



# Method Resolution Order (MRO) defines the order in which Python 
# searches for a method in a class and its parent classes. It becomes 
# important when the same method exists in more than one class in an 
# inheritance chain, especially in multiple inheritance.



# The example shows how Python decides which method to execute when 
# both a parent and a child class have a method with the same name.




# class A:
#     def fun(self):
#         print("In class A")
# ​
# class B(A):
#     def fun(self):
#         print("In class B")
# ​
# a = B()
# a.fun()

# Output
# In class B
# Explanation:

# When obj.fun() is called, Python first looks in class B.
# Since B defines fun(), it runs that method and does not check class A.
# The MRO here is: B -> A.
# Multiple Inheritance (Diamond Problem)
# In multiple inheritance, a child class can inherit from more than one parent class.
#  When these parent classes come from a common base class, the structure forms a diamond 
#  shape and Python must decide which class method should be used.




# class A:
#     def fun(self):
#         print("In class A")
# ​
# class B(A):
#     def fun(self):
#         print("In class B")
# ​
# class C(A):
#     def fun(self):
#         print("In class C")
# ​
# class D(B, C):
#     pass
# ​
# a = D()
# a.fun()

# Output
# In class B
# Explanation:

# D inherits from B and C.
# Python follows the MRO: D -> B -> C -> A.
# Since B has fun(), it is executed and the search stops.
# C3 Linearization in MRO
# Python uses the C3 linearization algorithm to decide the order
# in which classes are searched when a method is called. 
# This algorithm produces a single, consistent order that respects 
# both inheritance and the order in which parent classes are written.

# Example: This program prints the exact order Python uses for method lookup.




# class A:
#     def fun(self):
#         print("In class A")
# ​
# class B(A):
#     def fun(self):
#         print("In class B")
# ​
# class C(A):
#     def fun(self):
#         print("In class C")
# ​
# class D(B, C):
#     pass
# ​
# obj = D()
# obj.fun()
# ​
# print(D.__mro__)

# Output
# In class B

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>,
#   <class 'object'>)


# Explanation:

# When obj.fun() is called, Python follows the MRO shown by D.__mro__.
# It checks D, then B, then C, then A.
# Since B defines fun(), that method is executed and the search stops.
# Methods to View Method Resolution Order (MRO) of a Class
# Python provides two ways to check the method resolution order (MRO) of a class:

# __mro__ attribute: shows a tuple of classes in the order Python searches for methods.
# mro() method: returns a list of classes in the MRO.



# class A:
#     def fun(self):
#         print("In class A")
# ​
# class B:
#     def fun(self):
#         print("In class B")
# ​
# class C(A, B):
#     def __init__(self):
#         print("Constructor C")
# ​
# obj = C()
# ​
# print(C.__mro__) 
# print(C.mro())

# Output
# Constructor C

# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# Explanation:

# C.__mro__ returns the method resolution order as a tuple.
# C.mro() returns the same order as a list.
# This sequence shows that Python will search C, then A, then B, and 
# finally object when resolving any method call.



# class A:
#     def sum(self):
#         print("Addition of two numbers: ")

# class B:
#     def sum(self):
#         print("144+144=288: ")
    
# class C(A,B):
#     pass

# obj=C()
# obj.sum()
# print(C.__mro__)   or
# print(C.mro())




class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()
obj.show()
# print(D.mro())   or
print(D.__mro__)