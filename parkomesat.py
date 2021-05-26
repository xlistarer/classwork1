from tz import Transport


class Parkmesto:

    def __init__(self, size, price, adress):
        self.__size = size
        self.__price = price
        self.__adress = adress
        self.__object: Transport = None

    def __str__(self):
        if self.__object:
            return f"adress: {self.__adress} free"
        return f"adress: {self.__adress} zanato"

    @property
    def size(self):
        return self.__size

    @property
    def price(self):
        return self.__price

    @property
    def is_free(self) -> bool:
        return not self.__object

    def zaniat(self, tz):
        if self.size >= tz.size and not self.__object:
            self.__object = tz
            return True
        return False

    def zabrat(self, number):
        if not self.is_free and self.__object.number == number:
            self.__object = None
            return True
        return False


class Bikemesto(Parkmesto):
    def __init__(self, adress):
        super().__init__(1, 5, adress)


class Carmesto(Parkmesto):
    def __init__(self, adress):
        super().__init__(2, 10, adress)


class Busmesto(Parkmesto):
    def __init__(self, adress):
        super().__init__(3, 15, adress)
