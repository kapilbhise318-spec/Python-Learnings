class A:
    def hello(self):
        return ("hello World")
    
class B(A):
    def who(self):
        return ("Who are you..")
class C(A):
    def i(self):
        return ("I'm your friend..")
class D(B,C):
    def ok(self):
        return ("Ok! I got it..")
    
# print(D.__mro__)
print(D().hello())
print(D().who())
print(D().i())
print(D().ok())