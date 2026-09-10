
# Calling constructo by super() keyword....

# class Animal:
#     def __init__(self,name):
#         self.name=name
#         print("Animal eats")

# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age

# d=Dog("TARS",8)
# print(d.name, d.age)


# 2) Calling Method by super() keyward...

class Animal:
    def show(self):
        print('Looking Outside..')

class Dog(Animal):
    def show(self):
        super().show()
        print("Dog is barking...")

d=Dog()
d.show()