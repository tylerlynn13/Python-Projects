

#parent class

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Beep Beep Move!")

#first child class
#while learning this part of program found pass,and wanted to include
class Car(Vehicle):
    pass

#second class

class Boat(Vehicle):
    def move(self):
        print("Sail around the world!")

#third and final class

class Plane(Vehicle):
    def move(self):
        print("Fly like eagle!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")


for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
