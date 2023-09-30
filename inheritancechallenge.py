


class Amphibian:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def printname(self):
        print(self.name, self.origin)

class Salamander(Amphibian):
    def __init__(self, name, origin):
        Amphibian.__init__(self, name, origin)


x = Salamander("Jake", "China")
x.printname()
    
