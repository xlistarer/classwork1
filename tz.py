class Transport:
    def __init__(self, size, kind, number):
        self.__number = number
        self.__kind = kind
        self.__size = size
    @property
    def size(self):
        return self.__size

    @property
    def number(self):
        return self.__number
class Bike(Transport):
    def __init__(self, number):
        super().__init__(1, "bike", number)
class Car(Transport):
    def __init__(self, number):
        super().__init__(2, "car", number)
class Bus(Transport):
    def __init__(self, number):
        super().__init__(3, "bus", number)