

class Protected:
    def __init__(self):
        self.__privateVar = 12
        self._protectedVar = 13

    def getPrivate(self):
        print(self.__privateVar)
        print(self._protectedVar)

    def setPrivate(self, private):
        self.__privateVar = private
        self._protectedVar = Protected


obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
