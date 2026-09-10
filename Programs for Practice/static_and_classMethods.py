# # Class Method..
# # @classmethod

# class Employee:
#     company="Google"
#     def __init__(self,name):
#         self.name=name

#     @classmethod

#     def change_company(cls,new_company):
#         cls.company = new_company



# print(Employee.company)

# Employee.change_company("Microsoft")

# print(Employee.company)




# 2) statis method
# @staticmethod

# class Calcy:
#     @staticmethod
#     def add(a,b):
#         return a + b
    
# print(Calcy.add(10,20))


# All 3 methods 
# instance, class, static METHOD


class Car:
    company='MNW'
    def __init__(self,model):
        self.model=model

    #instance method
    def show_model(self):
        print(self.model)

    # class method
    @classmethod
    def show_company(cls):
        print(cls.company) 
    
    # staticMethod
    @staticmethod
    def info():
        print('Cars have Engines')

car=Car('55')
car.show_model()
car.show_company()
car.info()