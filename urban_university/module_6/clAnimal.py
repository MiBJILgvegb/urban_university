from module_6.clPlant import *
class Animal:
    alive = True
    fed = False
    #6.3
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    speed=0
    def __init__(self,name,speed=0):
        if(not isinstance(name,str)):
            print("Имя должно быть строкой.")
            return
        self.name=name
        #6.3
        if(not isinstance(speed,int)):
            print("Скорость должна быть указана числом.")
            return
        self.speed=speed
    def eat(self, food):
        if(not isinstance(food,Plant)):
            print(f"{food.name} - не еда.")
            return False
        if(not food.edible):
            print(f"{self.name} не стал есть {food.name}.")
            self.alive=False
            return False
        print(f"{self.name} съел {food.name}.")
        self.fed=True
        return True
    def __str__(self):
        return self.name
    #6.3
    def move(self, d):
        if(not isinstance(d,tuple)):
            print("Координаты необходимо указывать в виде кортежа.")
            return False
        d1=[d[0]*self.speed,d[1]*self.speed,d[2]*self.speed]
        if(d1[2]<=0):
            print("It's too deep, i can't dive :(")
            return False
        self._cords=d1
        return True
    def get_cords(self):
       print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
       return
    def attack(self):
        echo="Sorry, i'm peaceful :)"
        if(self._DEGREE_OF_DANGER>5):
            echo="Be careful, i'm attacking you 0_0" 
        print(echo)
        return
    def speak(self):
        if(isinstance(self.sound,str)):
            print(self.sound)
        return