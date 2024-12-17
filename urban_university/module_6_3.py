import random
class Animal:
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
class Bird(Animal):
    beak = True
    def lay_eggs(self):
       print(f"Here are(is) {random.randint(0,4)} eggs for you")
       return
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dzm=1
        if(dz<0):
            dzm=-1
        self._cords[2]-=int(dz*dzm*(self.speed/2))
        return
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill(PoisonousAnimal,AquaticAnimal,Bird):
    sound = "Click-click-click"


db = Duckbill("Duckbill",10)

print(db.live)
print(db.beak)


db.speak()
db.attack()


db.move((1, 2, 3))
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()