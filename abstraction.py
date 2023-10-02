
# import abc 

from abc import ABC

# define base class
class Polygon(ABC):
    # abstract method
    def sides(self):            # no sides method used
        pass


class Triangle(Polygon):        # implemented base class
    def sides(self):            # sides() method being used
        print("Triangle has 3 sides")

class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")

class Hexagon(Polygon):
    def sides(self):
        print("Hexagin has 6 sides")

class square(Polygon):
    def sides(self):
        print("I have four sides")


t = Triangle()
t.sides()

s = square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()
