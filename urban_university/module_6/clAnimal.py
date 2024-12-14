from module_6.clPlant import *
class Animal:
    alive = True
    fed = False
    
    def __init__(self,name):
        if(not isinstance(name,str)):
            print("Имя должно быть строкой.")
            return None
        self.name=name
        self.alive = True
        self.fed = False
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