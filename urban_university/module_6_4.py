import math

class Figure:
    sides_count = 0
    __sides=[]
    __color=[0,0,0]
    filled=False
    
    def __is_valid_color(self,color):
        if(isinstance(color,list) or isinstance(color,tuple)):
            result=False
            for c in color:
                result=self.__is_valid_color(c)
            return result
        elif(isinstance(color,int)):
            return 0 <= int(color) <= 255
        return False
        
    def __is_valid_sides(self, sides):
        if(isinstance(sides,list)or isinstance(sides,tuple)):
            result=False
            for s in sides:
                result=self.__is_valid_sides(s)
            return result
        elif(isinstance(sides,int)):
            return int(sides) > 0
        return False

    def __len__(self):
        return sum(self.__sides)

    def __init__(self,color,*sides):
        if (not self.__is_valid_color(color)):
            print("Не правильно указан код цвета.")
            return
        self.set_color(*color)
        s=sides
        if(len(sides)!=self.sides_count):
            s=[1]*self.sides_count
        self.set_sides(*s)

    def set_color(self,*color):
        if(not self.__is_valid_color(color[0])):
            print("Неправильно указан код цвета")
            return False
        if(len(color)==1):
            if(isinstance(color,list)or isinstance(color,tuple)):
                self.__color=color
                return True
        elif(len(color)==3):
            self.__color=[color[0],color[1],color[2]]
            return True
        return False
    
    def set_sides(self,*sides):
        if(self.__is_valid_sides(*sides)):
            sl=[]
            for s in sides:
                sl.append(s)
            self.__sides=sl
            return True
        return False
    
    def get_color(self):
        return self.__color
    
    def get_sides(self):
        return self.__sides
class Circle(Figure):
    sides_count = 1
    
    def __radius(self):
        return self.get_sides()[0]/math.pi

    def get_square(self):
        return math.pi * (self._Figure__radius**2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self._Figure__sides) / 2
        return math.sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if (not self._Figure__is_valid_color(color)):
            print("Не правильно указан код цвета.")
            return
        self.set_color(*color)
        s = sides
        if(len(sides)==1):
            s = [sides[0]] * self.sides_count
        elif(len(sides) != self.sides_count):
            s = [1] * self.sides_count
        self.set_sides(*s)

    def set_sides(self,*sides):
        if(len(sides)==1):
            for i in range(0,self.sides_count-1):
                self._Figure__sides[i]=sides[0]
            return True
        elif(len(sides)==self.sides_count):
            self._Figure__sides=sides
        return False
    def get_volume(self):
        return self._Figure__sides[0]**3

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