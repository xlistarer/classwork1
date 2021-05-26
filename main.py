# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from parkovka import Parkovka
from tz import Bike, Bus

a=Parkovka(5,3,1)
b1=Bike("FG2345")
bus=Bus("ttttt")
bus2=Bus("tteeee")
print(a)
a.try_park(b1)
a.try_park(bus)
a.try_park(bus2)
print(a)
a.try_leave("FG2345")
a.try_leave("ttttt")
print(a)
print(f"{a.kassa} dollarov v kasse")