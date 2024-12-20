import math
from functools import singledispatch

class Figure:
    sides_count = 0
    __sides=[]
    __color=[0,0,0]
    filled=False
#перегрузка метода для валидации цвета
    @singledispatch
    def __is_valid_color(self,color):
        pass
#https://docs-python.ru/tutorial/klassy-jazyke-python/peregruzka-metodov/
    @__is_valid_color.register(int)
    @__is_valid_color.register(str)
    def _(self,color):
        return 0 <= int(color) <= 255

    @__is_valid_color.register(tuple)
    @__is_valid_color.register(list)
    def _(self,color):
        result = True
        i=0
        while(i<len(color) and result):
            result = self.__is_valid_color(i)
            i+=1
        return result
#перегрузка метода для валидации сторон
    @singledispatch
    def __is_valid_sides(self, side):
        pass

    @__is_valid_sides.register(int)
    @__is_valid_sides.register(str)
    def _(self,side):
        return int(side) > 0

    @__is_valid_sides.register(tuple)
    @__is_valid_sides.register(list)
    def _(self,side):
        result=False
        for s in side:
            result=self.__is_valid_sides(s)
        return result

    def __len__(self):
        return sum(self.__sides)

    def __new__(cls,color,*sides):
        if (not cls.__is_valid_color(color)):
            print("Не правильно указан код цвета.")
            return None
    def __init__(self,color,*sides):
        self.set_color(color)
        s=sides
        if(len(sides)!=self.sides_count):
            s=[1]*self.sides_count
        self.set_sides(self,s)

    def get_color(self):
        return self.__color
    #перегрузка метода
    @singledispatch
    def set_color(self,r,g,b):
        pass

    @set_color.register(tuple)
    @set_color.register(list)
    def _(self,colors):
        result=self.__is_valid_color(colors)
        if(result):
            self.__color = list(colors)
        return result
    @set_color.register(int)
    def _(self,r,g,b):
        result=self.__is_valid_color((r,g,b))
        if(result):
            self.__color=(r,g,b)
            return result
        print("Неправильно указан код цвета")
        return result
    def get_sides(self):
        return self.__sides

    def set_sides(self,*sides):
        if(self.__is_valid_sides(*sides)):
            self.__sides=sides
            return True
        return False

class Circle(Figure):
    sides_count = 1
    def __radius(self):
        return self.get_sides()[0]/math.pi
    def get_square(self):
        return math.pi * (self.__radius**2)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = sum(self.__sides) / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.set_color(color)
        s = sides
        if(len(sides)==1):
            s = [sides] * self.sides_count
        elif(len(sides) != self.sides_count):
            s = [1] * self.sides_count
        self.set_sides(self, s)

    def set_sides(self,side):
        if(self.__is_valid_sides(side)):
            for i in range(0,self.sides_count-1):
                self.__sides[i]=side
            return True
        return False
    def get_volume(self):
        return self.__sides[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())