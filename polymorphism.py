

#parent class

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Beep Beep Move!")


#first class

class Boat(Vehicle):
    def __init__(self, brand, model, color, passengers):
        self.brand = brand
        self.model = model
        self.color = color
        self.passengers = passengers
    def move(self):
        print("Sail around the world!")
        

#second class

class Plane(Vehicle):
    def __init__(self, brand, model, color, passengers):
        self.brand = brand
        self.model = model
        self.color = color
        self.passengers = passengers
    def move(self):
        print("Fly like eagle!")
        

boat1 = Boat("Ibiza", "Touring 20", "Blue", "eight")
plane1 = Plane("Boeing", "747", "Pink", "six")


for x in (boat1, plane1):
    print(x.brand)
    print(x.model)
    print(x.color)
    print(x.passengers)
    x.move()
