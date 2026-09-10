class Vehicle:
    def __init__(self):
        self.engine=False 
        self.brake=False

    def start_engine(self):
        self.engine=True
        self.brake=True
        print("Engine Started. ")

car1=Vehicle()
car1.start_engine()

# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass


# class Car(Vehicle):
#     def start_engine(self):
#         print("Car Started. ")
# car=Car()
# car.start_engine()
