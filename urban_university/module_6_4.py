import math

class Figure:
    sides_count = 0
    __sides=[]
    __color=[0,0,0]
    filled=False
    
    def __is_valid_color(self,c):
        return 0<=c<=255
    def __is_valid_sides(self,*sides):
        if(len(sides)!=self.sides_count):
            print("Неправльное количество сторон")
            return False
        for side in sides:
            if(side<=0):
                print("Неправльная длина сторон")
                return False
        return True
    def __len__(self):
        return self.__sides.sum()

    def get_color(self):
        return self.__color
    def set_color(self,r,g,b):
        if(self.__is_valid_color(r) & self.__is_valid_color(g) & self.__is_valid_color(b)):
            self.__color=[r,g,b]
            return True
        print("Неправльно указан код цвета")
        return False
    def set_color(self,c=[]):
        if(len(c)==2):
            return self.set_color(c[0],c[1],c[2])
        return False
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
        return self.get_sides[0]/math.pi
    def get_square(self):
        return math.pi * (self.radius**2)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12
    __sides=[]
    def __is_valid_sides(self,side):
        if(side<=0):
            print("Неправльная длина сторон")
            return False
        return True
    def set_sides(self,side):
        if(self.__is_valid_sides(side)):
            for i in range(0,self.sides_count-1):
                self.__sides[i]=side
            return True
        return False
    def get_volume(self):
        return self.__sides[0]**3