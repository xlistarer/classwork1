from parkomesat import Bikemesto,Carmesto,Busmesto
from tz import Transport


class Parkovka:
    def __init__(self,countb,countc,countbus):
        self.__countbus = countbus
        self.__countc = countc
        self.__countb = countb
        self.__kassa=0
        self.__mesta=[]
        for i in range(countb):
            self.__mesta.append(Bikemesto(str(i)+"b"))
        for i in range(countc):
            self.__mesta.append(Carmesto(str(i) + "c"))
        for i in range(countbus):
            self.__mesta.append(Busmesto(str(i) + "v"))
    def __str__(self):
        free={1:0,
              2:0,
              3: 0}
        for mesto in self.__mesta:
            if mesto.is_free:
                free[mesto.size] += 1
        return f"Na parkovke mesta for bike {free[1]}, for car {free[2]}, for bus {free[3]} mest"


    def try_park(self,tz):
        for mesto in self.__mesta:
            if mesto.zaniat(tz)==True:
                return True
        return False
    def try_leave(self,number):
        for mesto in self.__mesta:
            if mesto.zabrat(number)==True:
                self.__kassa+=mesto.price
                return True
        return False
    @property
    def kassa(self):
        return self.__kassa

