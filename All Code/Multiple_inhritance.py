class Flyable:
    def fly(self):
        return "Bumble Bee can alse Fly"
    
class Swimmable:
    def swim(self):
        return "Seals can Be Swim.."

class Duck(Flyable,Swimmable):
    def speak(self):
        return "Ducks speak Like Quack Quack"  

d=Duck()
print(d.fly())
print(d.swim()) 
print(d.speak()) 
    
    
        