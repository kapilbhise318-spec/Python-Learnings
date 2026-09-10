class Vehicle:
    def start(self):
        return "The Vehicle Isnt moving yet!!"
    
class Car(Vehicle):
    def drive(self):
        return "The Vehicle Finallly Start their engine!!"
    

c=Car()
print(c.start())
print(c.drive())