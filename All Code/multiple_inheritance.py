# class Animal:
#     def breathe(self):
#         return "Animal taking breathe.."
# class Mammals(Animal):
#     def feed_milk(self):
#         return "Animal feed their kittens"
# class Dog(Mammals):
#     def speak(self):
#         return "Make Sound Woof!!"

# c=Dog()
# c.breathe()
# c.feed_milk()
# c.speak()



class Animal:
    def breathe(self):
        return "Breathing..."

class Mammal(Animal):
    def feed_milk(self):
        return "Feeding milk"

class Dog(Mammal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.breathe())     # from Animal
print(d.feed_milk())   # from Mammal
print(d.speak())       # own method