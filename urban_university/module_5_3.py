from module_5.clHouse import *

#house1=House(input("Название 1го дома - "),int(input("Количество этажей - ")))
#house2=House(input("Название 2го дома - "),int(input("Количество этажей - ")))

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print("__eq__ ",h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print("__add__ ",h1)
print(h1 == h2)

h1 += 10 # __iadd__
print("__iadd__ ",h1)

h2 = 10 + h2 # __radd__
print("__radd__ ",h2)

print("__gt__ ",h1 > h2) # __gt__
print("__ge__ ",h1 >= h2) # __ge__
print("__lt__ ",h1 < h2) # __lt__
print("__le__ ",h1 <= h2) # __le__
print("__ne__ ",h1 != h2) # __ne__